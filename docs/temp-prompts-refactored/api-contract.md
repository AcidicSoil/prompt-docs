```md
<!-- $1 = trigger phrase (e.g., "/api-contract 'accounts & auth'") -->
<!-- $2 = domain (e.g., "auth") -->
<!-- $3 = contract type (e.g., "OpenAPI 3.1", "GraphQL") -->
<!-- $4 = contract file extension (e.g., ".yaml", ".graphql") -->
<!-- $5 = output file path (e.g., "apis/$2/$4") -->
<!-- $6 = changelog entry path (e.g., "docs/api/CHANGELOG.md") -->
<!-- $7 = style convention (e.g., "JSON:API") -->

# API Contract Generator

Trigger: $1

Purpose: Author an initial $3 contract from requirements.

**Steps:**

1. Parse inputs and existing docs. If REST, prefer $3; if GraphQL, produce $3.
2. Define resources, operations, request/response schemas, error model, auth, and rate limit headers.
3. Add examples for each endpoint or type. Include pagination and filtering conventions.
4. Save to $5.
5. Emit changelog entry $6 with rationale and breaking-change flags.

**Affected files:**
- $5
- $6

**Output format:**
- `Contract Path`: $4
- `Design Notes`: $7
- Fenced code block with spec body

**Examples:**
- `$1` → $5

**Notes:**
- Follow $7 style for REST unless specified.
```
