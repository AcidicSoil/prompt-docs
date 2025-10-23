```md
# Audit

Trigger: $1

Purpose: $2

## Steps

1. Gather context by running `ls -la` for the top-level listing. Inspect $3, $4, $5, $6, $7, and $8 if present to understand shared conventions.
2. Assess repository hygiene across documentation, testing, CI, linting, and security. Highlight gaps and existing automation.
3. Synthesize the findings into a prioritized checklist with recommended next steps.

## Output format

- Begin with a concise summary that restates the goal: Audit repository hygiene and suggest improvements.
- Offer prioritized, actionable recommendations with rationale.
- Call out test coverage gaps and validation steps.
- Highlight workflow triggers, failing jobs, and proposed fixes.

## Missing sections

* Affected files: $9
* Root cause: $10
* Proposed fix: $11
* Tests: $12
* Docs gaps: $13
* Open questions: $14

<!--
$1 = Trigger
$2 = Purpose
$3 = .editorconfig
$4 = .gitignore
$5 = .geminiignore
$6 = .eslintrc.cjs
$7 = .eslintrc.js
$8 = tsconfig.json
$9 = Affected files
$10 = Root cause
$11 = Proposed fix
$12 = Tests
$13 = Docs gaps
$14 = Open questions
-->
```
