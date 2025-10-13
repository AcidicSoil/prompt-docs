```markdown
<!-- Placeholder mapping (from input fields):
$1 = Claim text
$2 = Source URL
$3 = Source Title
$4 = Publisher
$5 = Publication Date
$6 = Access Date
$7 = Quote (≤25 words) -->

# Evidence Logger

Trigger: /evidence-capture

Purpose: Capture sources for a specified claim with dates, ≤25-word quotes, findings, relevance, and confidence.

Steps:

1. Read the claim text and optional URLs provided.
2. For each source, record metadata and a ≤25-word quote.
3. Add a brief Finding, Relevance (H/M/L), and Confidence (0.0–1.0).

Output format:

```
### Evidence Log
| SourceID | Title | Publisher | URL | PubDate | Accessed | Quote (≤25w) | Finding | Rel | Conf |
|---|---|---|---|---|---|---|---|---|---|
```

Examples:

- Input: `/evidence-capture $1` with $2
- Output: Evidence table entries with dates.

Notes:

- Mark missing PubDate as n/a. Prefer official documentation.
```
