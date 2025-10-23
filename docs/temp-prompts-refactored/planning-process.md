```md
**Planning Process Prompt**

<!-- $1 = Feature description (e.g., "Add OAuth login") -->
<!-- $2 = Plan file name (e.g., "PLAN.md") -->
<!-- $3 = Max checklist line length (e.g., "100 chars") -->

# Planning Process

Trigger: $2

Purpose: Draft, refine, and execute a feature plan with strict scope control and progress tracking.

## Steps

1. If no plan file exists, create $2. If it exists, load it.
2. Draft sections: **Goal**, **User Story**, **Milestones**, **Tasks**, **Won't do**, **Ideas for later**, **Validation**, **Risks**.
3. Trim bloat. Convert vague bullets into testable tasks with acceptance criteria.
4. Tag each task with an owner and estimate. Link to files or paths that will change.
5. Maintain two backlogs: **Won't do** (explicit non-goals) and **Ideas for later** (deferrable work).
6. Mark tasks done after tests pass. Append commit SHAs next to completed items.
7. After each milestone: run tests, update **Validation**, then commit $2.

## Output format

- Update or create $2 with the sections above.
- Include a checklist for **Tasks**. Keep lines under $3 chars.

## Examples
**Input**: $1

**Output**:

- Goal: Let users sign in with Google.
- Tasks: [ ] add Google client, [ ] callback route, [ ] session, [ ] E2E test.
- Won't do: org SSO.
- Ideas for later: Apple login.

## Notes

- Planning only. No code edits.
- Assume a Git repo with test runner available.
```
