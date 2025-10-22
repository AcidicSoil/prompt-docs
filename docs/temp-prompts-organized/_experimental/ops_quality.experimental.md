```md
<!--
$1 = target: "plan-id:step-id" | "plan-id:range" | "plan-id:all" | bare step-id(s) ("2" or "1,3-5")
$2 = commands string (e.g., "pnpm run lint && pnpm test && pnpm run e2e")
$3 = exec driver: "detect" | "local" | "codex" | "none" (emit script only)
$4 = working directory (e.g., ".")
$5 = artifacts dir (e.g., ".ops/quality")
$6 = timeout seconds per step (e.g., "3600")
$7 = retries on failure per step (e.g., "0")
$8 = parallelism: integer ≥1 (e.g., "2")
$9 = environment: "inherit" | path to .env | inline "KEY=VAL,KEY2=VAL2"
-->

/ops:quality "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9"

Goal

- Execute step-scoped quality checks and normalize results. Preserve logs and metrics for CI or manual review.

Inputs

- Target: $1
- Commands: $2
- Driver: $3
- CWD: $4
- Artifacts: $5
- Timeout: $6
- Retries: $7
- Parallelism: $8
- Env: $9

Contract

- Read thresholds and gates from the referenced plan steps when present (coverage, lint, perf, memory, LOC caps).
- Do not modify source files.

Algorithm

1) Resolve $1 to an ordered step list. Load declared gates for each step when available.
2) Prepare run context:
   - Apply env from $9 (merge with inherit if a file is provided).
   - Ensure $4 exists; create $5 with subdirs per step: `$5/step-<id>/`.
3) For each step (≤ $8 in parallel):
   a) Compose a POSIX shell script: `set -euo pipefail; $2`.
   b) If $3 == "none": write`run.sh` and skip execution.
      Else execute via driver ($3). Enforce per-step timeout $6.
   c) Capture stdout and stderr to `stdout.log` and `stderr.log`.
   d) Collect common artifacts if present:
      - JUnit XML → `junit.xml`
      - Coverage summaries → `coverage-summary.json` or `lcov.info`
      - Lint reports → `lint.json` or `lint.txt`
      - Perf/profiling → `perf.json`
   e) Evaluate gates against collected artifacts. Compute PASS/FAIL with reasons.
   f) On failure and retries remaining ($7): rerun with exponential backoff and tag attempt N.
4) Write `step-report.json` with: timings, attempts, exit code, gate results, and file counts.
5) Aggregate into `$5/quality-summary.md` and `$5/quality-summary.json`:
   - step → status, duration, retries, failing gates, pointers to logs.
6) Exit non-zero if any mandatory gate fails.

Outputs

- `$5/step-<id>/stdout.log`, `stderr.log`, `run.sh`, `step-report.json`, collected tool artifacts.
- `$5/quality-summary.md` and `$5/quality-summary.json`.
- If $3 == "none": also emit `manual-run.md` with copy-paste commands and expected artifacts.

Constraints

- No source writes. No network unless commands require it.
- Respect per-step thresholds from the plan when available; otherwise do best-effort parsing from artifacts.
- Keep per-step log files ≤10 MB by truncation with notice.

Failure handling

- On driver error or timeout, mark step as ERROR with captured diagnostics; continue other steps.
- Produce `$5/quality-error.md` summarizing root causes and next actions.

Examples

- Run quality for step 2 with local execution and default env:
  /ops:quality "plan-123:2" "pnpm run lint && pnpm test" "local" "." ".ops/quality" "1800" "0" "1" "inherit"

- Emit manual script for steps 1–3, no execution:
  /ops:quality "plan-123:1-3" "pnpm run lint && pnpm test && pnpm run e2e" "none" "." ".ops/quality" "3600" "0" "1" ".env"

- Parallel run for all steps with retries:
  /ops:quality "plan-123:all" "pnpm run -s lint && pnpm -s test" "detect" "." ".ops/quality" "2400" "1" "3" "KEY=A,CI=1"
```