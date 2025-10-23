```md
<!-- $1 = input task IDs (e.g., TM-42, TM-43) -->
<!-- $2 = task title from tasks.json -->
<!-- $3 = step-by-step plan description -->
<!-- $4 = list of file touch-points -->
<!-- $5 = test hooks for the task -->
<!-- $6 = measurable acceptance criteria -->
<!-- $7 = Conventional Commits message (e.g., `feat(parser): implement rule X`) -->

**Advance Task Plan Generator**

Trigger: For given $1, produce a concrete work plan, acceptance criteria, tests, and a Conventional Commits message to move status toward done.

Purpose: For given task id(s), produce a concrete work plan, acceptance criteria, tests, and a Conventional Commits message to move status toward done.

Steps:

1. Read tasks.json; resolve each provided $1. If none provided, pick the top item from /tm-next.
2. For each task: restate $2, goals, and related dependencies.
3. Draft a step-by-step plan with $4 and $5.
4. Provide a minimal commit plan and a Conventional Commits message ($7).
5. List measurable acceptance criteria ($6).

Output format:

- One section per task: "## $1 — $2"
- Subsections: Plan, Files, Tests, Acceptance, Commit Message ($7), Risks.

Notes:
- Do not mutate tasks.json. Emit proposed changes only.
```
