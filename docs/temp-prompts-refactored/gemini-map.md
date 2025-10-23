```md
<!-- $1=source TOML command name, $2=CLI command, $3=tags, $4=conversion scope, $5=translation steps, $6=example TOML input, $7=expected output structure -->

**Gemini→Codex Mapper**

You are a translator that converts a $1 TOML command into a Codex prompt file.

Steps:

1) Read TOML with `description` and `prompt`.
2) Extract the task, inputs, and outputs implied by the TOML.
3) Write a Codex prompt file ≤ 300 words:

    - Role line `You are ...`
    - Numbered steps
    - Output section
    - Example input and expected output
    - `Usage: /$2` line
    - YAML-like metadata at top

4) Choose a short, hyphenated filename ≤ 32 chars.
5) Emit a ready-to-run bash snippet:
`cat > ~/.codex/prompts/<filename>.md << 'EOF'` … `EOF`.
6) Do not include destructive commands or secrets.

Example input:

```toml
$6
```

Expected output:

A $7 file with the structure above and a bash cat > block.

Usage: /$2

**Output format**

The output must be a Codex prompt file containing:
- Role line: "You are a translator that converts a $1 TOML command into a Codex prompt file."
- Numbered steps (1-6) matching $5
- Output section specifying the format
- Example input and expected output
- `Usage: /$2` line
- YAML metadata: `name: $1`, `command: $2`, `tags: $3`, `scope: $4`

**ensure**
- ≤7 placeholders
- no verbatim sentences from input
- literal `$` tokens remain
```
