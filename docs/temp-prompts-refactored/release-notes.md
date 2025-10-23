```md
<!-- $1=git-range argument, $2=commit log output, $3=change categories (e.g., Features, Fixes), $4=input file path, $5=specific change entry, $6=summary text, $7=evidence description -->

## How to Generate Release Notes

Trigger: /release-notes $1

Purpose: Generate human-readable release notes from recent commits.

You are a CLI assistant focused on helping contributors with the task: Generate human‑readable release notes from recent commits.

1. Gather context by running `git log --pretty='* %s (%h) — %an' --no-merges $2` for the commit log (no merges).
2. Produce release notes grouped by type $3. Include a Highlights section and a full changelog list.
3. Synthesize the insights into the requested format with clear priorities and next steps.

Output:

- Begin with a concise summary: $6
- Document the evidence: $7

Example Input:
$4

Expected Output:
## $3

- $5
```
