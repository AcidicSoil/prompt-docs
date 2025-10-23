```md
<!-- $1 = target command (e.g., /changelog-verify) -->
<!-- $2 = validation status (PASS|FAIL) -->
<!-- $3 = line number in CHANGELOG -->
<!-- $4 = reason for failure (e.g., "Section order incorrect") -->
<!-- $5 = suggested normalized Markdown block -->
<!-- $6 = unified diff to apply -->

# Verify CHANGELOG Completeness

Trigger: $1

Purpose: Check that the latest merge introduced a CHANGELOG entry with the six-section policy and that sections are concise and non-empty where applicable.

Steps:

1. Parse $1 and locate `## [Unreleased]` or the latest version heading.
2. Validate presence and order of sections: Added, Changed, Deprecated, Removed, Fixed, Security.
3. Flag anti-patterns: paragraphs longer than 2 lines, trailing periods, internal-only jargon, file paths, or empty sections left in place.
4. Cross-check against commits since last tag to detect missing items.
5. Emit a diagnostic report and a suggested patch to fix ordering and brevity issues.

Output format:

- `$2`
- Table of findings with line numbers ($3) and reasons ($4)
- Suggested normalized Markdown block ($5)
- Unified diff to apply ($6)

Examples:
Input → $1
Output →

```
$2
- $3: $4
- Missing section stub

$5
```

Constraints:
- Static analysis only; no network calls.
- Treat any section with 0 bullets as removable unless policy requires stubs.
```
