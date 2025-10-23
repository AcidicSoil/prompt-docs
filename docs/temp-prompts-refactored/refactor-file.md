```md
# Refactor Analysis

<!-- Placeholder mapping:  
$1 = File path (e.g., src/components/Button.tsx)
$2 = Before/after snippet (code diff)
$3 = Evidence used (e.g., lines 1-400 of file)
$4 = Refactor goal (e.g., extract shared styling hook)
$5 = Summary (concise restatement of goal)
$6 = Complexity reduction justification (why refactoring improves readability)
$7 = Next steps (actionable items for maintainers) -->

**Refactor Analysis**

1. Gather context by running `sed -n '1,400p' $1` for the first 400 lines of the file.
2. Suggest refactors that reduce complexity and improve readability without changing behavior. Provide $2 with commentary.
3. Synthesize insights into $5 with clear priorities and $7.

**Output Format**

- Begin with a concise summary: $5
- Include $2 with commentary
- Document evidence: $3

*Note: $4 is implied by the refactoring goal but can be explicitly stated for clarity*
```
