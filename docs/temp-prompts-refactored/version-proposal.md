```md
# Version Proposal

Trigger: $1

Purpose: $2

You are a CLI assistant focused on helping contributors with the task: $3

1. Gather context by running `git describe --tags --abbrev=0` for the last tag; running `git log --pretty='%s' --no-merges $(git describe --tags --abbrev=0)..HEAD` for the commits since last tag (no merges).
2. Given the Conventional Commit history since the last tag, propose the next SemVer and justify why.
3. Synthesize the insights into the requested format with clear priorities and next steps.

Output:
- Begin with a concise summary that restates the goal: $4
- Offer prioritized, actionable recommendations with rationale.
- Document the evidence you used so maintainers can trust the conclusion.

Example Input:
$5

Expected Output:
- Structured report following the specified sections.

<!-- Placeholders:
$1 = Trigger (e.g., "/version-proposal")
$2 = Purpose (e.g., "Propose the next semantic version based on commit history")
$3 = Task description (e.g., "Propose next version (major/minor/patch) from commit history")
$4 = Output summary goal (e.g., "Propose next version (major/minor/patch) from commit history")
$5 = Example input format (e.g., "(none – command runs without arguments)") -->
```
