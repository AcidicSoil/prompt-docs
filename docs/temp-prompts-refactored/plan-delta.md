```md
<!-- $1=command, $2=purpose, $3=tasks file path pattern, $4=latest plan doc pattern, $5=artifacts directory, $6=date format string, $7=mode selection rules -->

**How-to: $2**

Trigger: $1

Purpose: $2

Steps:

1. Discover repository context:
   1. Detect tasks file path: prefer $3; else search `**/$3`.
   2. Detect latest plan doc: prefer $4; else `**/*(prd|spec|plan)*.md`.
2. Snapshot:
   1. Create $5 if missing.
   2. Copy current tasks file to `$5/tasks-$(date +%$6).json` using: `cp -f <tasks.json> $5/tasks-$(date +%$6).json`.
3. Input collection:
   1. Read new objectives, constraints, and findings from user input.
   2. Parse selection rules to choose mode: **$7**.
4. Delta Doc generation:
   1. Create `$5/delta-$(date +%$6).md` containing sections:
      - Objectives (new)
      - Constraints (new)
      - Impacts
      - Decisions
      - Evidence log (sources, dates, links)
5. Task graph update:
   1. Never alter historical states (`done`/`in_progress`/`blocked`) of existing tasks.
   2. Do not reuse IDs. For replaced tasks, set `superseded_by` on old tasks and include ID in new task's `supersedes[]`.
   3. Add `source_doc`, `lineage[]` on new/changed tasks.
   4. Create new tasks only for new/changed work. Link predecessors via `dependencies` or `relations`.
   5. Keep deprecated tasks with `status: "deprecated"` and `reason`.
6. **Tests**:
   1. Recompute dependency order and validate acyclicity.
   2. Flag contradictions as `blocked` with machine-readable `blocked_reason`.
   3. Verify critical-path tasks are correctly prioritized.
7. **Affected files**:
   - $5/tasks-$(date +%$6).json
   - $5/delta-$(date +%$6).md
8. Readiness and selection:
   1. Implement `ready/next()` to select tasks with all dependencies `done` and not `blocked`.
   2. Produce readiness report grouped by `ready | blocked | deprecated`.
9. Outputs:
   1. Write updated tasks file in-place.
   2. Persist Delta Doc under $5.
   3. Emit decision hooks: one line per change stating what it enables.

**Output format**:
- Produce three artifacts:
  1. **Updated tasks file**: Valid JSON. Preserve existing fields. Append new/changed tasks and relations.
  2. **Delta document**: Markdown with sections `# Delta`, `## Objectives`, `## Constraints`, `## Impacts`, `## Decisions`, `## Evidence`.
  3. **Readiness report**: Plain text with sections `READY`, `BLOCKED`, `DEPRECATED`. Format: `- <id> <title>` (blocked items add `[reason=<code>]`).
- Print **Decision hooks** as lines starting with `HOOK: <id> enables <capability>`.

**Open questions**:
- What evidence is missing to resolve inputs?
- How to handle partial scope changes (<20%)?
- Should deprecated tasks be automatically archived?
```
