```md
# Workflow Sequence

Users request/idea --> gemini-2.5:pro

TM parses prd into tasks.json

## Response item from gemini

gemini's response is sent to GPT-5 for enhancements

Delivers --> <gpt5-reviewed-gemini-refact>.md

## POST PRD PARSING WITH TM

### Users Query to gpt-5

```md
"Does the prd.md and tasks.json reflect the <gpt5-reviewed-gemini-ui-refact>.md and honor its requests?"
```

#### OPTIONAL (Highly Recommended)

!!! tip "Better output on iterations"
    - curated prompt templates specific to scope of user
    - general gpt-5 response and Q&A
    - Outputs --> discrepancies surfaced from tasks.json

#### Rinse & Repeat w/ Complexity Report

## Optional (Provide curated kickoff prompt template)

### If template method

* Give prompt template to GPT-5 and take the output and add to the template file.

Query

```md
"instructions on it's usage for user?"
```

* Drag copy of the template into codebase
Provide gemini your session id and edit the settings.json to allow as a working directory (location of the session)

* Once gemini-2.5:Pro is fully configured and primed have gemini fill out the template.

* Take the inputs and use the a notepad to draft your query to codex and send.

#### Feed the prePrompt to codex

## Refactor workflow examples

### /prompts:<>

```md
/prompts:QA-ready_refactor-plan "Inventory and harden the existing app to support the UI refactor without reinitializing the project." "Entire `codex-session-viewer` application." "All public-facing
  components and their props, especially `<codex-session-viewer>`." "Virtualized timeline rendering should remain >55 FPS on 1,000 events, and memory usage should stay under 300 MB with a 10k-event
  dataset." "`pnpm run lint && pnpm test && pnpm run e2e`" "Coverage ≥ 85%; ≤ 150 LOC touched per step; ≤ 5 files per step."
```

```md
/prompts:<NameOfPrompt> "Inventory and harden the existing app to support the UI refactor without reinitializing the project." "Entire `codex-session-viewer` application." "All public-facing
  components and their props, especially `<codex-session-viewer>`." "Virtualized timeline rendering should remain >55 FPS on 1,000 events, and memory usage should stay under 300 MB with a 10k-event
  dataset." "`pnpm run lint && pnpm test && pnpm run e2e`" "Coverage ≥ 85%; ≤ 150 LOC touched per step; ≤ 5 files per step."
```

### /prompts:ops_apply

```md
# 1) Dry-run all steps, emit unified diffs to .ops
/ops:apply "./plans/refactor-plan.md" "dry-run" "all" "unified-diff" "fail-fast" ".ops" ""

# 2) Apply steps 1–3 via git apply, continue on errors
/ops:apply "plan-123" "apply" "1-3" "git-apply" "continue-on-error" ".ops" "hotfix window"

# 3) Apply a single step using filesystem writes (no VCS), fail fast
/ops:apply "plan-123" "apply" "2" "fs-write" "fail-fast" ".ops" "surgical change"

# 4) Dry-run selected steps 1,4,7 to review patches only
/ops:apply "plan-123" "dry-run" "1,4,7" "unified-diff" "fail-fast" ".ops" "review before apply"

# 5) Apply remaining steps after a pause; keep artifacts separate
/ops:apply "plan-123" "apply" "5-9" "git-apply" "continue-on-error" ".ops/phase-2" "phase 2 rollout"

# 6) Plan resolved from URL; generate diffs only for compliance sign-off
/ops:apply "https://example.com/plan-123.md" "dry-run" "all" "unified-diff" "fail-fast" ".ops/signoff" "audit"

# 7) Create manual-apply packets when Git patches won’t fit (fs-write)
/ops:apply "./plans/edge-cases.md" "dry-run" "3" "fs-write" "fail-fast" ".ops/manual" "legacy tree shape"

# 8) Canary apply a single risky step with rich notes
/ops:apply "plan-123" "apply" "6" "git-apply" "fail-fast" ".ops/canary" "canary on small cohort"

```

### /prompts:ops_quality

```md
# 1) Run step 2 locally with default env
/ops:quality "plan-123:2" "pnpm run lint && pnpm test" "local" "." ".ops/quality" "1800" "0" "1" "inherit"

# 2) All steps via auto driver detection, with retries and parallelism
/ops:quality "plan-123:all" "pnpm run -s lint && pnpm -s test" "detect" "." ".ops/quality" "2400" "1" "3" "CI=1,FORCE_COLOR=1"

# 3) Steps 1–3, emit script only (no execution)
/ops:quality "plan-123:1-3" "pnpm run lint && pnpm run e2e" "none" "." ".ops/quality" "3600" "0" "1" ".env"

# 4) Comma list selection with longer timeout
/ops:quality "plan-123:1,4,7" "pnpm test" "local" "." ".ops/quality" "5400" "0" "2" "inherit"

# 5) Bare step IDs resolved against current plan
/ops:quality "2,5-6" "npm run test" "local" "." ".ops/quality" "1800" "0" "1" "inherit"

# 6) Perf-heavy checks with capped logs via env var
/ops:quality "plan-abc:all" "make lint test perf" "detect" "." ".ops/quality" "7200" "0" "2" "CI=1,LOG_MAX=10485760"

# 7) Single step with custom working dir and artifacts path
/ops:quality "plan-xyz:3" "pytest -q && coverage xml" "local" "services/api" ".ops/api-quality" "1800" "0" "1" "inherit"

# 8) Generate manual packet for offline runner
/ops:quality "plan-123:all" "pnpm run lint && pnpm test && pnpm run e2e" "none" "." ".ops/manual-quality" "3600" "0" "1" "KEY=A,CI=1"

# 9) Re-run flaky step with retries
/ops:quality "plan-123:7" "pnpm test --filter '@app/*'" "local" "." ".ops/quality" "1800" "2" "1" "inherit"

```

!!! tip "Run these next"
    - QA-ready_refactor-plan
    - ops_apply
    - ops_quality

=== "What's next"
    - Need to refactor? Run first [QA-ready_refactor-plan](QA-ready_refactor-plan.experimental.md)
    - Then, Run second [ops_apply](ops_apply.experimental.md)
    - If needed, run [ops_quality](ops_quality.experimental.md)
```
