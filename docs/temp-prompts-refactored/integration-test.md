```md
<!-- $1=trigger command, $2=purpose statement, $3=output format -->

**E2E Test Generation Prompt**

# Integration Test

Trigger: $1

Purpose: $2

## Steps

1. Detect framework from `package.json` or repo (Playwright/Cypress/Vitest).
2. Identify critical path scenarios from `PLAN.md`.
3. Produce test files under `e2e/` with arrange/act/assert and selectors resilient to DOM changes.
4. Include login helpers and data setup. Add CI commands.

## Output format

- $3

## Examples

- Login, navigate to dashboard, create record, assert toast.

## Notes

- Prefer data-test-id attributes. Avoid brittle CSS selectors.
```
