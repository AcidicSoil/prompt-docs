# Recursive Text Search with ripgrep/grep Injection

## Inputs

- Input text to search for (e.g., `HttpClient`)
- Target directory (default: current project root)

## Canonical taxonomy (exact strings)

- search
- analysis
- insight
- debugging
- documentation
- configuration
- automation

### Stage hints (for inference)

- search → investigation or debugging
- analysis → analysis or insight generation
- insight → synthesis or reporting

## Algorithm

1. Extract signals from the prompt  
   _Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing._

2. Determine the primary identifier  
   _Prefer explicit input; otherwise infer from main action + object._  
   Normalized to: `recursive-text-search`

3. Determine categories  
   _Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy._  
   Selected: search, analysis, insight

4. Determine lifecycle/stage (optional)  
   _Map via stage hints:_ "search" → debugging; "analysis" → investigation; final inferred stage: debugging

5. Determine dependencies (optional)  
   _CLI tools required: ripgrep or grep, file system access._  
   Identified: `rg`, `grep`

6. Determine provided artifacts (optional)  
   _Synthesized outputs from evidence:_
   - Usage cluster in a code directory
   - Note on inconsistent error handling

7. Compose summary  
   "Do recursive text search with ripgrep/grep injection to achieve insight into usage clusters and inconsistent error handling."

8. Produce metadata in the requested format
   - Identifier: `recursive-text-search`
   - Categories: `search`, `analysis`, `insight`
   - Stage: `debugging`
   - Dependencies: `rg`, `grep`
   - Artifacts: `usage-cluster`, `error-handling-note`
   - Summary: "Do recursive text search with ripgrep/grep injection to achieve insight into usage clusters and inconsistent error handling."

9. Reconcile if input already contains metadata  
   _No explicit metadata present; inferred values used._

## Assumptions & Constraints

- Output must contain exactly one document: metadata block, blank line, then original body.
- Limit distinct placeholders to ≤7.
- Body text remains unaltered.

## Validation

- Identifier matches normalized pattern (kebab-case, lowercase).
- Categories are non-empty and drawn from canonical taxonomy (≤3).
- Stage (`debugging`) is implied by stage hints.
- Dependencies are id-shaped and relevant.
- Artifacts are concise and derived from output examples.
- Summary ≤120 chars; punctuation coherent.

## Output format examples

- Identifier: `recursive-text-search`
- Categories: `search`, `analysis`, `insight`
- Stage: `debugging`
- Dependencies: `rg`, `grep`
- Artifacts: `usage-cluster`, `error-handling-note`
- Summary: "Do recursive text search with ripgrep/grep injection to achieve insight into usage clusters and inconsistent error handling."
