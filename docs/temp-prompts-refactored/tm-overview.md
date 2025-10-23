```md
# TaskMaster Overview

Trigger: $1

Purpose: $2

Steps:
1. Locate the active tasks.json at repo root or the path supplied in the user message. Do not modify it.
2. Parse fields: id, title, description, status, priority, dependencies, subtasks.
3. Compute counts per status and a table of top pending items by priority.
4. Detect dependency issues: cycles, missing ids, orphans (no deps and not depended on).
5. Approximate a critical path: longest dependency chain among pending→in_progress tasks.

Output format: $3

Examples:
- Input: $4
- Output: $5

Notes:
- $6: Read-only. Assume statuses: pending | in_progress | blocked | done.
- If tasks.json is missing or invalid, output an "## Errors" section with a concise diagnosis.

<!-- Placeholder mapping -->
$1 = Task description
$2 = Purpose statement
$3 = Output format specification
$4 = Example input format
$5 = Expected output structure
$6 = Critical path details (optional) -->
```
