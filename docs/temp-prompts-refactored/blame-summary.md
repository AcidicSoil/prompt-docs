```md
<!-- Placeholder mapping:
$1 = git blame command with arguments
$2 = example input file path
$3 = expected output format description
$4 = proposed refactor example snippet
-->
**How-to: Summarize authorship hotspots**

1. Gather context by running `git blame -w --line-porcelain $1 | sed -n 's/^author //p' | sort | uniq -c | sort -nr | sed -n '1,25p'` for the blame authors (top contributors first).
2. Given the blame summary below, identify ownership hotspots and potential reviewers.
3. Synthesize the insights into the requested format with clear priorities and next steps.

Output:
- Begin with a concise summary that restates the goal: Summarize authorship hotspots for a file using git blame.
- Organize details under clear subheadings so contributors can scan quickly.
- Reference evidence from CODEOWNERS or git history for each owner suggestion.

Example Input:
$2

Expected Output:
$3

Proposed Fix Examples:
$4
```
