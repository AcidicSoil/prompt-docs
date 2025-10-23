```md
# Prepare Release Notes From CHANGELOG

Trigger: `/release-notes-prepare`

Purpose: Convert the latest CHANGELOG section into release notes suitable for GitHub Releases with the six-section layout.

Steps:

1. Detect latest version heading and extract its section.
2. Normalize bullets to sentence fragments without trailing periods.
3. Add short highlights at top (3 bullets max) derived from Added/Changed.
4. Emit a "copy-ready" Markdown body.

Output format:

- Title line: `Release ${1} — ${2}`
- Highlights list
- Six sections with bullets

<!-- Placeholder mapping -->
${1}=Version (e.g., 1.6.0)
${2}=Release date (e.g., 2025-09-22)
${3}=Highlight 1 (e.g., Custom roles and permissions)
${4}=Highlight 2 (e.g., Faster cold starts)
${5}=Highlight 3 (optional)
${6}=Added section content
${7}=Changed section content

**Note**: This template follows the six-section layout (Added, Changed, Removed, Fixed, Improved, Deprecated). Missing sections like Removed, Fixed, Improved, Deprecated are implied by the context and will be populated with the appropriate content from CHANGELOG.
```
