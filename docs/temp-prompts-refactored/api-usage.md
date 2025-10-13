```

<!-- Placeholder mapping for api-usage.md:
$1 = Example input symbol (e.g., 'HttpClient')
$2 = API usage pattern (e.g., 'Key usages')
$3 = Evidence type (e.g., 'File paths')
$4 = Definition source (e.g., 'src/network/httpClient.ts')
 -->

**How to show internal API usage**

1. Gather context by running `rg -n $1 . || grep -RIn $1 .`.
2. Summarize common usage patterns and potential misuses for the symbol.
3. Synthesize the insights into the requested format with clear priorities and next steps.

**Output format**

- Begin with a concise summary that restates the goal: Show how an internal API is used across the codebase.
- Organize details under clear subheadings so contributors can scan quickly.
- Document the evidence you used so maintainers can trust the conclusion.

**Example**

- Input: $2
- Expected output: 
  - Definition: $3
  - Key usages: $4

```
