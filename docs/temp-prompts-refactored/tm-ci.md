```md
<!-- $1 = task path (e.g., "/tm-ci") -->
<!-- $2 = purpose statement -->
<!-- $3 = ready tasks path (e.g., "/tm-next") -->
<!-- $4 = grouping method (e.g., "by component/tag") -->
<!-- $5 = CI job details (name | trigger | commands | est_time) -->
<!-- $6 = test matrix (scope | command | expected_artifacts) -->
<!-- $7 = risk areas -->

# CI/Test Checklist Template

## Analysis

- [ ] Affected files
- [ ] Root cause
- [ ] Proposed fix
- [ ] Tests
- [ ] Docs gaps
- [ ] Open questions

## How-to Steps

1. Compute ready tasks (see $3) and collect testStrategy fields.
2. Group by $4; otherwise by path keywords in titles.
3. Propose CI jobs and test commands with approximate runtimes and gating rules ($5).
4. Include a smoke-test matrix ($6) and minimal code coverage targets if relevant.

Output format:

- "# CI Plan"
- Tables: jobs ($5) and tests ($6)
- "## Risk Areas" ($7)

Examples:

- Input: $1
- Output: one CI plan with 3–8 jobs and a test table.

Notes:

- Non-binding guidance. Adapt to the repo’s actual CI system.
```
