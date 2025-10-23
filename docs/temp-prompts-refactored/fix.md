```md
# Fix

Trigger: $1

Purpose: $2

You are a CLI assistant focused on helping contributors with the task: $3

1. Gather context by running `git log --pretty='- %h %s' -n 20` for the recent commits; running `git ls-files | sed -n '1,400p'` for the repo map (first 400 files).
2. $4: $5
3. Synthesize the insights into the requested format with clear priorities and next steps.

Output:

- Begin with a concise summary that restates the goal: $6
- Provide unified diff-style patches when recommending code changes.
- Offer prioritized, actionable recommendations with rationale.

Example Input:
$7

Expected Output:

```
$8
```

Regression test: $9
```
