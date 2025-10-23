```md
<!-- $1=task ID (e.g., "TM-09"), $2=subtasks table content, $3=JSON patch array -->

**Refine Task into Subtasks**

Trigger: /tm-refine

Purpose: Expand a vague or large task into actionable subtasks with clear acceptance criteria.

Steps:

1. Load the task by $1 and analyze description for ambiguity and scope.
2. Propose 3–8 subtasks with titles, brief descriptions, and dependencies between them.
3. Define acceptance criteria per subtask using Given/When/Then or bullet checks.
4. Suggest test coverage and doc updates triggered by completion.

Output format:

- "# Refinement: $1"
- Subtasks as a Markdown table: $2
- "## JSON Patch" fenced code of suggested additions suitable for tasks.json editing: $3

Examples:

- Input: /tm-refine $1
- Output: $2 plus a minimal JSON Patch array.

Constraints:
- Do not assume authority to change files; provide patches the user can apply.
```
