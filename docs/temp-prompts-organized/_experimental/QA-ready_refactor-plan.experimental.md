```md
<!--
$1 = goal
$2 = scope
$3 = API contracts to keep stable
$4 = performance guardrails
$5 = quality commands pipeline (lint then tests)
$6 = thresholds (coverage target and per-step change budget for lines and files)
$7 = per-step details bundle (title, files touched, reused symbols, patch summary, tests, risk, rollback note)
-->

# {$2 or QA-Ready Refactor Plan}

**Inputs**

- Objective: $1
- Area: $2
- Contracts: $3
- Performance: $4
- Quality run: $5
- Thresholds: $6

**Guardrails**

- Reuse first: move, extract, or facade. Avoid new patterns unless justified.
- Small deltas: each step stays within $6 across limited files.
- Stability: keep $3 intact; add shims if needed.
- Gate per step: run $5 then enforce $6.

## 1) Assessment

- Seams within $2
- Safe extraction points
- Test gaps to close first
- Affected files
- Root cause summary
- Proposed fix outline

## 2) Stepwise Plan

*For each step i:*

- Name: $7
- Change type: extract | rename | move | inline | split
- Files: $7
- Reuse targets: $7
- Patch outline: $7
- Tests to add or update: $7
- Risk and rollback: $7
- Validation: run $5 and record result

## 3) Execution Log

- Step i → status, notes, follow-ups

## 4) Exit Report

- What changed and what stayed invariant
- Performance check against $4
- Coverage and thresholds met: $6
- Open items
- Docs to update

**Acceptance Criteria**

- All steps pass gates.
- No ABI/API break beyond approved list for $3.
- Coverage and limits meet $6.

---

### Output format

- Plan table of steps with $7 fields
- Minimal diffs per step
- Test and coverage summary from $5
- Prune ledger: path | evidence | action | owner
```