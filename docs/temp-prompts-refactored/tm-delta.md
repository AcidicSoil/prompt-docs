```md
# $1 → Tasks Delta

Trigger: $2

Purpose: Compare $1 against tasks.json and propose add/update/remove operations.

Steps:

$3. Extract $4, $5, $6, and $7 from $1.
$4. Map them to existing tasks by fuzzy match on title and keywords; detect gaps.

Propose: new tasks, updates to titles/descriptions/priority, and deprecations.

Output format:

- "# Delta Summary"
- Tables: adds | updates | removals.
- "## JSON Patch" with an ordered list of operations: add/replace/remove.
- "## Assumptions" and "## Open Questions".

Examples:

- Input: $2
- Output: tables with a small JSON Patch block.

Notes:

- Keep patches minimal and reversible. Flag any destructive changes explicitly.
```
