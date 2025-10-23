```md
<!-- Placeholder mapping:
$1 = Title (System-level instruction)
$2 = Purpose
$3 = Inputs
$4 = Steps
$5 = Deconstruct request
$6 = Locate insertion points
$7 = Apply minimal change and invariants -->

**System-Level Instruction Editor**

Trigger: $1

Purpose: $2

## Inputs

- $3

## Steps

1. $4
2. $5
3. $6

1. **Deconstruct the request:** $7

2. **Locate insertion points:** Use semantic matching on headings and content to find the best-fit sections for the user’s request. If no clear section exists, create a new minimal section with a logically consistent title.

3. **Apply minimal change:** Insert or modify content to satisfy the request while preserving tone, structure, and cross-references. Keep unrelated sections unchanged.

4. **Run invariants:**

   - The entire file must be present (no placeholders, no truncation).
   - Markdown structure and formatting must remain valid.
   - Internal references and links stay accurate.

5. **Render in Canvas:**

   - If editing an existing file: open in Canvas and **replace the full contents** with the updated version.
   - If creating a new file: create it in Canvas and display the **entire file**.

6. **Variants (optional):** Generate $1.md and/or $2.md from the updated $3.md using only the Platform Substitution Rules. Render each variant’s **entire file** in Canvas (one file per Canvas operation).

7. **Size-limit fallback:** If a size cap prevents full-file rendering in Canvas, output the **entire file in chat**, then append:

   - "*Note: Full content was output in chat due to a size limit preventing Canvas rendering.*"

## Output format

- Table: $1 → $2 → $3 → $4 → $5

## Example rows

- "<example symptom or error>" → $6 → $7 → $1 → $2
```
