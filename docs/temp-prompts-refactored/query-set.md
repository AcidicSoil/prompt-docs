```md
<!-- Placeholder mapping:
$1 = Goal statement
$2 = Number of queries (4-8)
$3 = Time window (e.g., 'past year')
$4 = Input entities (e.g., 'OpenAI Responses API streaming server-sent events')
$5 = Query types (e.g., 'define, compare, integrate') -->

**High-Yield Query Generator**

Trigger: /query-set

Purpose: Generate {1} targeted web search queries with operators, entity variants, and recency filters for a given objective.

Steps:
1. Restate the goal with entities and time window.
2. Produce queries using operators: site:, filetype:, inurl:, quotes, OR, date filters.
3. Include synonyms and common misspellings.
4. Mix intents: {2}

Output format:
```
### Goal
{3}

### Query Set
- {4}
- {5}
... up to 8
```

Examples:
- Input: `/query-set {6} {7}`
- Output: Goal + {8} queries with operators.

Notes:
- No evidence logging here. Use /research-item to execute.
```
