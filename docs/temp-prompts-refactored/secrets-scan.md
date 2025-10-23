```md
<!-- 
$1 = Core task description (e.g., "Review secret scan output and highlight real leaks")
$2 = Command to run (e.g., "gitleaks detect --no-banner --redact 2>/dev/null")
$3 = Interpretation method (e.g., "de-dupe false positives and propose rotations")
$4 = Output format requirement (e.g., "structured report with prioritized recommendations")
$5 = Example input format (e.g., "none – command runs without arguments")
$6 = Expected output structure (e.g., "concise summary, prioritized recommendations, evidence documentation")
$7 = Specific evidence type (e.g., "scanner results from gitleaks")
-->
**Secrets Scan Analysis**

1. Gather context by running `$2` for the if `$2` is available, output will appear below.
2. Interpret the scanner results using `$3` to de‑dupe false positives and propose rotations/remediation.
3. Synthesize the insights into `$4` with clear priorities and next steps.

Output:
- Begin with a concise summary restating `$1`
- Offer prioritized, actionable recommendations with rationale
- Document the evidence used for maintainers' trust

Example Input:
$5

Expected Output:
$6

Affected files: 
Root cause: 
Proposed fix: 
Tests: 
Docs gaps: 
Open questions:
```
