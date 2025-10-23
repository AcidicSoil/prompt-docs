```md
<!-- Placeholders: $1=short title, $2=goal sentence, $3=assumption bullet, $4=first query, $5=second query, $6=third query, $7=fourth query to eighth query (range) -->

**Conversation-Aware Research**

# Conversation-Aware Research — Single Item

Trigger: /research-item

Purpose: Run the full per-item research workflow for one objective and return queries, evidence, synthesis, contradictions, gaps, decision hook, plus a conversation state update.

Steps:
1. Read the objective text following the trigger.
2. Capture starting context if provided.
3. Apply the Process (per item): Goal, Assumptions, Query Set (4–8), Search Plan, Run & Capture, Cross-check, Synthesis, Gaps & Next, Decision Hook.
4. Track PubDate and Accessed (ISO) for every source; prefer primary docs.
5. Enforce quotes ≤25 words; mark inferences as "Inference".

Output format:

```
## Item 1: $1

### Goal
$2

### Assumptions
- $3

### Query Set
- $4
- $5
- $6
- $7

### Evidence Log
| SourceID | Title | Publisher | URL | PubDate | Accessed | Quote (≤25w) | Finding | Rel | Conf |
|---|---|---|---|---|---|---|---|---|---|

### Synthesis
- $8
- $9
- $10

### Contradictions
- $11 → $12

### Gaps & Next
- $13

### Decision Hook
$14

### Conversation State Update
- New facts: $15
- Constraints learned: $16
- Entities normalized: $17
```

Examples:
- Input: `/research-item Compare OpenAPI 3.1 tooling for Python clients in 2024; budget $0; prefer official docs.`
- Output: As per format with SourceIDs and dates.

Notes:
- Safety: No personal data. Do not fabricate sources.
- Provenance: Cite reputable sources; record n/a for missing PubDate.
```
