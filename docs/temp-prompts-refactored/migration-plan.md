```md
<!-- 
$1 = trigger phrase (e.g., "/migration-plan")
$2 = change summary (e.g., "orders add status enum")
$3 = current vs target schema description
$4 = migration steps details
$5 = online migration strategies for large tables
$6 = SQL snippets
$7 = PR checklist items
$8 = rollback capability flag (can_rollback: true|false)
-->

**Migration Plan Template**

Trigger: $1

Purpose: Produce safe up/down migration steps with checks and rollback notes.

**Steps:**

1. $3
2. $4

**Output format:** `Plan`, `SQL`, `Rollback`, `Checks` sections.

**Examples:** $2.

**Notes:** $5

**Additional requirements:** $6 and $7 with $8 flag.
```
