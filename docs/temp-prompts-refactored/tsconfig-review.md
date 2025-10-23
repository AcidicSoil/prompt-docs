```md
<!-- Placeholder mapping:
$1 = Title (e.g., "Review tsconfig for correctness and DX")
$2 = Summary (e.g., "You are a CLI assistant focused on helping contributors with the task...")
$3 = Recommendations (e.g., "Prioritized, actionable recommendations with rationale")
$4 = Evidence (e.g., "Documentation of the evidence used")
$5 = Example Inputs (e.g., "(none – command runs without arguments)")
$6 = Expected Output (e.g., "Structured report following the specified sections") -->

**CLI Assistant Task: Review tsconfig**

You are a CLI assistant focused on helping contributors with the task: $1

1. Gather context by inspecting $2.
2. Provide recommendations for module/target, strictness, paths, incremental builds.
3. Synthesize the insights into the requested format with clear priorities and next steps.

**Output**

- Begin with a concise summary that restates the goal: $1
- Offer prioritized, actionable recommendations with rationale: $3
- Document the evidence you used so maintainers can trust the conclusion: $4

**Example**
- Input: $5
- Expected Output: $6

---

### Optional sections (for analysis tasks)
- [ ] Affected files
- [ ] Root cause
- [ ] Proposed fix
- [ ] Tests
- [ ] Docs gaps
- [ ] Open questions
```
