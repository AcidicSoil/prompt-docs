```
<!-- Placeholder mapping -->
$1 = Trigger command (e.g., "/update-changelog")
$2 = Purpose statement (e.g., "Generate a user-facing CHANGELOG entry...")
$3 = Step 1 description (e.g., "Inspect repo state:")
$4 = Step 2 description (e.g., "Collect changes:")
$5 = Step 3 description (e.g., "De-dupe and rewrite:")
$6 = Step 4 description (e.g., "Emit Markdown snippet...")
$7 = Step 5 description (e.g., "Decide placement:")

**How-to: Update CHANGELOG**

$1

Purpose: $2

Steps:

$3

$4

$5

$6

$7

Output format:

- Heading line with target section (Unreleased or version)
- Six-section block in Markdown with only non-empty sections in order: Added, Changed, Deprecated, Removed, Fixed, Security
- A short "Link references" block suggestion for `[Unreleased]` and new version comparison links
- A unified diff (context 3) for `CHANGELOG.md`

Examples:

Input →
```
$8
```

Output →
```
$9
```

Notes:

- Assumes git repository is available and tags follow SemVer.
- Keep content end-user focused. Avoid internal file names and refactor notes.
- If no Conventional Commits, infer section from message heuristics.
- Do not include secrets or internal ticket links.
```
