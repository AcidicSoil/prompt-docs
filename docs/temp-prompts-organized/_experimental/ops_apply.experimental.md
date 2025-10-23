```md
<!--
$1 = plan identifier (string or path/URL)
$2 = apply mode: "dry-run" | "apply"
$3 = step selector: "all" | comma list (e.g., "1,2,5") | range (e.g., "3-7")
$4 = patch strategy: "git-apply" | "unified-diff" | "fs-write"
$5 = stop policy: "fail-fast" | "continue-on-error"
$6 = artifact dir (e.g., ".ops/artifacts")
$7 = notes (optional free text)
-->

/ops:apply "$1" "$2" "$3" "$4" "$5" "$6" "$7"

Goal

- Apply the planned patches stepwise and emit verifiable artifacts. Do not execute build/test commands.

Inputs

- Plan: $1  (must resolve to a QA-Ready Refactor Plan doc)
- Mode: $2
- Steps: $3
- Patch strategy: $4
- Stop policy: $5
- Artifacts dir: $6
- Notes: $7

Plan contract (must match):

- Use step schema and gates from the QA-Ready Refactor Plan: name, files, reuse targets, patch outline, tests, risk, validation. Each step stays within thresholds and respects stable contracts.

Algorithm

1) Load plan $1 and parse step table + $7 fields per step. Validate thresholds and invariant contracts before any write.
2) Select steps per $3. Preserve original ordering.
3) For each step i:
   a) Generate minimal patch from “Patch outline” against listed Files.
   b) If $2 == "dry-run": produce diffs only.
   c) If $2 == "apply": apply using $4.
   d) Record “Execution Log” entry with status, touched files count, LOC delta, and any deviations from thresholds.
   e) Emit artifacts: `step-i.diff`, `step-i.patch.json` (metadata), `step-i.report.md`.
   f) If $5 == "fail-fast" and a step violates plan guardrails, stop and mark remaining as pending.
4) After final step, write `exit-report.md` with what changed vs invariants, perf and coverage placeholders, open items, and docs updates needed. Do not run tests here.

Outputs

- `apply-summary.md`: table of steps → status, files, LOC, notes.
- Per-step diffs and metadata under $6.
- `prune-ledger.md`: path | evidence | action | owner (aggregated from plan).

Constraints

- No shell or node execution. No `pnpm` invocation.
- Respect stable API/ABI contracts listed in plan.
- Enforce per-step thresholds before writing.

Fallback when no executor exists

- Always succeed in producing diffs and manual apply instructions:
  - For each step, include a ready-to-run `git apply step-i.diff` and, if not applicable, a file-by-file patch block.

Failure handling

- Produce `apply-error.md` with failing step id, reason, and next actions.
- If plan structure is invalid, emit `plan-parse-error.md` and exit.

Examples

- Dry run for all steps with unified diffs to `.ops`:
  /ops:apply "./plans/refactor-plan.md" "dry-run" "all" "unified-diff" "fail-fast" ".ops" ""
- Apply steps 1–3 using git apply and continue on errors:
  /ops:apply "plan-123" "apply" "1-3" "git-apply" "continue-on-error" ".ops" "hotfix window"

Notes

- Pair with `/ops:quality <step-id> "<commands>"` to run quality gates separately, e.g.:
  /ops:quality 2 "pnpm run lint && pnpm test && pnpm run e2e"
```