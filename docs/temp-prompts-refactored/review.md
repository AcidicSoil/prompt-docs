```md
# Review

Trigger: $1

Purpose: Review code matching $1 and deliver actionable feedback.

You are a CLI assistant focused on helping contributors with the task: Review code matching $1 and give actionable feedback.

1. Gather context by running `rg -n $2 . || grep -RIn $2 .` for the search results for $2 (filename or regex).
2. Perform a thorough code review. Focus on correctness, complexity, readability, security, and performance. Provide concrete patch suggestions.

3. Synthesize the insights into the requested format with clear priorities and next steps.

Output:
- Begin with a concise summary that restates the goal: Review code matching $1 and give actionable feedback.
- Provide unified diff-style patches when recommending code changes.
- Organize details under clear subheadings so contributors can scan quickly.

Example Input:
$3

Expected Output:
- Usage cluster in src/network/* with note on inconsistent error handling.

<!-- Placeholders:
- $1 = trigger pattern (e.g., `HttpClient`)
- $2 = search pattern for code context (e.g., `HttpClient`)
- $3 = example input pattern (e.g., `HttpClient`)
 -->
```
