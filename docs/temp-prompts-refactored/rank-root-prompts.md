```md
<!--
$1 = command name/identifier
$2 = example user question
$3 = project root path to scan (defaults to "~/.codex/prompts" when omitted/blank)
$4 = minimum relevance threshold (0–1)
-->

# {Prompt Ranking Command}

```md
# Command: $1

# Usage: $1 "$2" "$3" "$4"

# Args:

# - {{query}}: $2
# - {{path}}: $3
# - {{threshold}}: $4

prompt = """
Task:
Given a user inquiry {{query}}, review prompt-definition files located at {{path}} and identify the most relevant ones.

Defaults:
* If {{path}} is missing or blank, use "~/.codex/prompts".

Do the following:
1) List files in {{path}} without descending into subfolders. Treat common doc/config extensions as candidates.
2) Read each candidate’s text and summarize its purpose + domain in one sentence.
3) Compute a relevance score in [0,1] between that summary and {{query}}.
4) Order all candidates by score (highest first).
5) Emit a compact table with exactly these columns: filename | description | match_score (rounded to 2 decimals).

Rules:
* The description must be 1–2 sentences capturing purpose and domain.
* Only include rows with match_score ≥ {{threshold}}.
* If none satisfy {{threshold}}, output a single line: "No prompt exceeds threshold {{threshold}} — recommend creating a new prompt."

Acceptance:
* When ≥1 match meets {{threshold}}, a table sorted by descending match_score is present.
* Otherwise, the single-line note is produced.

!{echo "Using path: ${PATH_ARG:-~/.codex/prompts}"}
"""
```

## Output format

* **Preferred**: a markdown table with columns `filename | description | match_score` sorted by `match_score` (desc) and filtered by `{{threshold}}`.
* **Fallback**: the exact one-line message when no entries meet `{{threshold}}`.
-
```
