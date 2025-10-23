```md
<!-- 
$1 = Specific trigger command (e.g., "/cleanup-branches")
$2 = Purpose statement (e.g., "Recommend which local branches are safe to delete and which to keep")
$3 = Context gathering commands (e.g., "git branch --merged", "git branch --no-merged", "git for-each-ref...")
$4 = Branch suggestion instructions (e.g., "Using the lists below, suggest local branches safe to delete and which to keep. Include commands to remove them if desired")
$5 = Synthesis instructions (e.g., "Synthesize the insights into the requested format with clear priorities and next steps")
$6 = Output format requirements (e.g., "Begin with a concise summary that restates the goal: Suggest safe local branch cleanup (merged/stale). Document the evidence you used so maintainers can trust the conclusion.")
$7 = Example input/output (e.g., "Example Input: (none – command runs without arguments)\nExpected Output: - Structured report following the specified sections.")
-->

**Cleanup Branches**

Trigger: $1

Purpose: $2

You are a CLI assistant focused on helping contributors with the task: $3.

1. $4
2. $5
3. $6

Affected files: Local branches

Output format:
- $7
```
