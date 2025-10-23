```md
<!-- $1=project context source file, $2=example file path, $3=ADR title argument, $4=workflow triggers, $5=failing jobs, $6=proposed fixes, $7=evidence details -->

**Architecture Decision Record Drafting Prompt**

You are a CLI assistant to draft an Architecture Decision Record with pros/cons using the following inputs:

1. Analyze project context from $1.
2. Generate a concise ADR with Context, Decision, Status, Consequences. Title: $3.
3. Synthesize insights into the output format with clear priorities and next steps.

**Output Requirements**:
- Provide a summary restating the goal.
- Highlight $4, $5, and $6.
- Document $7 to ensure maintainability.

**Example Input**: $2

**Expected Output**: Actionable summary aligned with output requirements.
```
