```md
# Dead Code Scan Template

<!-- $1 = command string (e.g., `rg -n "export |module.exports|...`) -->
<!-- $2 = goal statement (e.g., "List likely dead or unused files and exports (static signals)") -->
<!-- $3 = purpose statement (e.g., "Identify likely dead or unused files and exports using static signals") -->

# Dead Code Scan

Trigger: `/dead-code-scan`

Purpose: $3

You are a CLI assistant focused on helping contributors with the task: $2.

1. Gather context by running $1 for the file reference graph (best‑effort).
2. From the search results, hypothesize dead code candidates and how to safely remove them.
3. Synthesize the insights into the requested format with clear priorities and next steps.

Output:

- Begin with a concise summary that restates the goal: $2.
- Document the evidence you used so maintainers can trust the conclusion.
```
