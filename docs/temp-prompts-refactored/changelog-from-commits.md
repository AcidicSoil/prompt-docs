```md
<!-- $1=command syntax (e.g., "since=v2.0.0 until=HEAD"), $2=commit range (e.g., "v2.0.0..HEAD"), $3=change type category (e.g., "Added"), $4=change description (e.g., "Import data from XLSX"), $5=PR reference (e.g., "#612") -->
**Draft CHANGELOG From Commits**

Purpose: Produce a first-draft six-section CHANGELOG block from commit messages and PR titles between $1.

Steps:

1. Inputs: `since=<ref or tag>` optional, `until=<ref>` default HEAD, `include_prs=true|false` default true.
2. Gather data with:
   - `git log --pretty=%H%x09%s%x09%b <since>.. <until>`
   - If available, `gh pr view` for merged PR titles by commit SHA; else rely on merge commit subjects.
3. Heuristics:
   - Map types: `feat|add`→$3, `fix|bug`→$3, `perf|refactor|opt`→$3, `deprecate`→$3, `remove|drop`→$3, `sec|cve|security`→$3.
   - Shorten to 12–80 chars. Strip scope parentheses.
4. Emit Markdown with only non-empty sections and a short preface noting the range.

Expected output:
- Range preface line: `Range: $2`
- Six-section Markdown block (each section starts with $3, followed by bullet points of $4 and $5)

Notes:
- This is a draft; run `/update-changelog` to finalize and create links.
- Keep bullets user-facing; avoid internal refactor noise.
```
