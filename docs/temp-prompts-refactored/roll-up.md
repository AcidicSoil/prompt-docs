```md
<!-- $1 = trigger phrase (e.g., "/roll-up") -->
<!-- $2 = purpose statement (e.g., "Summarize per-item statuses, enabled decisions, unresolved risks, and count sources by domain type") -->
<!-- $3 = step 1 description (e.g., "Aggregate Conversation State Updates from prior items") -->
<!-- $4 = step 2 description (e.g., "Produce per-item status lines and decisions") -->
<!-- $5 = step 3 description (e.g., "Tally sources by domain type: gov, org, docs, blog, news, academic") -->
<!-- $6 = output format template (e.g., the code block below) -->
<!-- $7 = example input (e.g., "/roll-up from items 1–3") -->

# Research Roll-up Summary

Trigger: $1

Purpose: $2

Steps:
1. $3
2. $4
3. $5

Output format:
```
## Roll-up Summary
- Item {n}: {status} — decision enabled: {…}; risks: {…}
- Sources by domain type: {gov:X, org:Y, docs:Z, blog:A, news:B, academic:C}
```

Examples:
- Input: $7
- Output: [see above]

Notes:
- Domain Count Analysis: $6 (explain why counts vary across domains)
- Evidence Log Reference: Use counts derived from the Evidence Logs
```
