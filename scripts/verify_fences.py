#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Iterable, List, Tuple, Optional, Set

TEXT_EXTS_DEFAULT = {
    "md","txt","py","js","ts","tsx","jsx","json","yml","yaml","toml","sh","bash",
    "css","scss","html","xml","rs","go","rb","php","java","kt","swift","c","h",
    "cpp","hpp","cs","sql","ini","conf","cfg"
}
IGNORES_DEFAULT = {".git","node_modules",".venv","venv",".mypy_cache","dist","build","target",".idea",".vscode","__pycache__"}

@dataclass
class CheckResult:
    root: Path
    root_name: str
    path: Path
    rel: Path
    status: str            # pass | warn | fail
    reason: str
    fix_preview: Optional[str]
    changed: bool = False

def read_lines(path: Path) -> List[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    return text.splitlines()

def write_lines(dest: Path, lines: List[str]) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines) + ("\n" if lines and not lines[-1].endswith("\n") else ""), encoding="utf-8")

def infer_fence_language(path: Path) -> str:
    return (path.suffix[1:].lower() if path.suffix else "").strip()

def analyze_file(root: Path, path: Path) -> CheckResult:
    try:
        lines = read_lines(path)
    except Exception as e:
        return CheckResult(root, root.name, path, path.relative_to(root), "fail", f"read-error: {e}", None, False)

    if not lines:
        return CheckResult(root, root.name, path, path.relative_to(root), "fail", "empty-file", None, False)

    first = lines[0].strip()
    # find last non-blank
    last_nonblank = None
    for ln in reversed(lines):
        if ln.strip():
            last_nonblank = ln.strip()
            break
    if last_nonblank is None:
        last_nonblank = ""

    ext = infer_fence_language(path)
    expected_first = f"```{ext}" if ext else "```"
    expected_last = "```"

    ok_start = first.startswith("```")
    ok_end = last_nonblank == "```"

    status = "pass" if (ok_start and ok_end) else ("warn" if ok_start or ok_end else "fail")

    reason_bits = []
    if not ok_start:
        reason_bits.append(f"missing-start:{expected_first}")
    if not ok_end:
        reason_bits.append("missing-end:```")
    reason = ",".join(reason_bits) if reason_bits else "ok"

    # preview fix
    fixed = list(lines)
    if not ok_start:
        fixed.insert(0, expected_first)
    if not ok_end:
        fixed.append("```")

    preview = None
    if fixed != lines:
        # only show the first and last two lines in preview
        head = fixed[:3]
        tail = fixed[-3:] if len(fixed) > 3 else []
        preview = "\n".join(head + (["..."] if tail else []) + tail)

    return CheckResult(root, root.name, path, path.relative_to(root), status, reason, preview, False)

def scan_tree(root: Path, include_exts: Set[str], ignore_dirs: Set[str]) -> List[CheckResult]:
    results: List[CheckResult] = []
    for p in root.rglob("*"):
        if p.is_dir():
            if p.name in ignore_dirs:
                # skip traversing into ignored dirs
                # rglob still iterates into them so we guard by not processing children files since we check on files only
                pass
            continue
        if not p.is_file():
            continue
        ext = p.suffix[1:].lower()
        if include_exts and ext not in include_exts:
            continue
        results.append(analyze_file(root, p))
    return results

def apply_fix(res: CheckResult, out_dir: Optional[Path], dry_run: bool, mirror: bool, out_parent: Optional[Path]) -> Tuple[bool, str, Optional[Path]]:
    try:
        lines = read_lines(res.path)
    except Exception as e:
        return False, f"read-error:{e}", None

    first = lines[0].strip() if lines else ""
    last_nonblank_idx = None
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip():
            last_nonblank_idx = i
            break
    last_is_fence = (last_nonblank_idx is not None and lines[last_nonblank_idx].strip() == "```")
    start_is_fence = first.startswith("```")

    ext = infer_fence_language(res.path)
    expected_first = f"```{ext}" if ext else "```"

    new_lines = list(lines)
    changed = False
    if not start_is_fence:
        new_lines.insert(0, expected_first)
        changed = True
    if not last_is_fence:
        new_lines.append("```")
        changed = True

    if not changed:
        return True, "no-change", res.path

    # Destination resolution
    # Mirror preserves the full folder structure under <out-parent>/<target-name>/<relative-path>
    if mirror and out_parent:
        dest = out_parent / res.root_name / res.rel
    elif out_dir:
        dest = out_dir / res.rel
    else:
        dest = res.path

    if dry_run:
        return True, f"dry-run would write:{dest}", dest

    try:
        write_lines(dest, new_lines)
        return True, "written", dest
    except Exception as e:
        return False, f"write-error:{e}", None

def summarize(results: List[CheckResult]) -> Tuple[int,int,int,int]:
    checked = len(results)
    passed = sum(1 for r in results if r.status == "pass")
    warned = sum(1 for r in results if r.status == "warn")
    failed = sum(1 for r in results if r.status == "fail")
    return checked, passed, warned, failed

def main() -> int:
    ap = argparse.ArgumentParser(description="Verify code fences and optionally fix them.")
    ap.add_argument("targets", nargs="+", help="Files or directories to scan")
    ap.add_argument("-e","--ext", action="append", default=[], help="File extensions to include. Repeatable. Default is a broad set.")
    ap.add_argument("-x","--ignore-dir", action="append", default=[], help="Directory names to ignore. Repeatable.")
    ap.add_argument("-A","--apply", action="store_true", help="Apply automatic fixes")
    ap.add_argument("-n","--dry-run", action="store_true", help="Do not write. Report only.")
    ap.add_argument("-M","--mirror", action="store_true", help="Mirror folder structure under out parent")
    ap.add_argument("-P","--out-parent", type=Path, help="Parent directory to write into when mirroring with -M")
    ap.add_argument("-o","--out-dir", type=Path, help="Output directory keeping relative paths (no project prefix)")
    args = ap.parse_args()

    include_exts = set(e.lower().lstrip(".") for e in (args.ext or [])) or set(TEXT_EXTS_DEFAULT)
    ignore_dirs = set(args.ignore_dir or []) or set(IGNORES_DEFAULT)

    targets = [Path(t).resolve() for t in args.targets]

    results: List[CheckResult] = []
    for t in targets:
        if t.is_dir():
            results.extend(scan_tree(t, include_exts, ignore_dirs))
        elif t.is_file():
            root = t.parent
            res = analyze_file(root, t)
            results.append(res)
        else:
            print(f"skip: not found {t}", file=sys.stderr)

    checked, passed, warned, failed = summarize(results)
    print(f"checked={checked} passed={passed} warned={warned} failed={failed}")

    if not args.apply:
        # simple report
        for r in results:
            if r.status != "pass":
                print(f"{r.path}: {r.status} {r.reason}")
        return 0 if failed == 0 else 1

    # apply
    fixed_ok = 0
    fixed_err = 0
    for r in results:
        ok, msg, dest = apply_fix(r, args.out_dir, args.dry_run, args.mirror, args.out_parent)
        if ok:
            fixed_ok += 1
        else:
            fixed_err += 1
        print(f"{r.rel} -> {dest if dest else 'N/A'} : {msg}")

    # re-scan written outputs if they are in a different tree
    if args.dry_run:
        return 0 if failed == 0 else 1

    # If writing to a different location, we do not reanalyze.
    return 0 if fixed_err == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
