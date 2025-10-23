```md
<!-- Placeholder mapping:
$1 = file paths
$2 = threshold values (e.g., >500 lines)
$3 = extraction targets (components, hooks, utilities, schemas)
$4 = before/after examples
$5 = import updates
$6 = refactor plan
$7 = patch details -->

**File Modularity**

Trigger: $1

Purpose: Enforce smaller files and propose safe splits for giant files.

## Steps

1. Find files over thresholds ($2).
2. Suggest extraction targets: $3.
3. Provide before/after examples and $5.

## Output format

- $6

---

### Affected files

- $1

### Root cause

- Files exceeding size thresholds

### Proposed fix

- $4
- $5

### Tests

- Unit tests for extracted components

### Docs gaps

- Documentation for new file structure

### Open questions

- How to handle circular dependencies
- Should we include type definitions in the extraction?
```
