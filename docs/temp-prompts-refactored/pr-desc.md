```md
<!-- 
$1 = Input context path (e.g., "src/example.ts")
$2 = Base branch (e.g., "origin/main")
$3 = User context (e.g., "<args>")
$4 = High-level diff stats (e.g., "2 files changed, 10 insertions")
$5 = List of changed files (e.g., "src/example.ts")
$6 = Desired output structure (e.g., "Summary, Context, Changes, Screenshots, Risk, Test Plan, Rollback, Release Notes")
$7 = Example output (e.g., "Actionable summary...")
-->

**PR Description Template**

Trigger: /pr-desc $1

Purpose: Draft a PR description from the branch diff.

1. Gather context by running `git diff --name-status $5` for the changed files; `git diff --shortstat $4` for high-level stats.
2. Create a crisp PR description following this structure: $6
   - Base branch: $2
   - User context: $3
3. Synthesize insights into the requested format.

Output requirements:
- Begin with a concise summary: $7
- Prioritized recommendations with rationale
- Test coverage gaps and validation steps
- Workflow triggers, failing jobs, and proposed fixes

Affected Files: $5
Root Cause: [Optional]
Proposed Fix: [Optional]
Test Plan: [Optional]
Risk: [Optional]
Rollback Plan: [Optional]
Release Notes: [Optional]
```
