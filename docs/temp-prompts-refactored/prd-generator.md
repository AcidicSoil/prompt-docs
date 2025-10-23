```md
<!-- $1=project plan text (visible link text), $2=product name, $3=problem statement, $4=key constraints -->
**PRD Generator Template**

Output a plain-text file named `prd.txt` containing **only** these sections in this order (separated by one blank line):
# Overview
# Core Features
# User Experience
# Technical Architecture
# Development Roadmap
# Logical Dependency Chain
# Risks and Mitigations
# Appendix

**Output Format**

- `# Overview`: $3
- `# Core Features`: Each includes *What*, *Why*, *High-level How*, and BDD criteria:
  `Given ...`
  `When ...`
  `Then ...`
- `# User Experience`: Personas, key flows, UI/UX, accessibility
- `# Technical Architecture`: Components, data models, APIs/integrations, infrastructure, NFRs
- `# Development Roadmap`: MVP and Future Enhancements with acceptance criteria (no dates)
- `# Logical Dependency Chain`: Work ordering for foundations, earliest front end, extensible units
- `# Risks and Mitigations`: Each includes *Description*, *Likelihood*, *Impact*, *Mitigation*
- `# Appendix`:
  • Assumptions (bulleted)
  • Research findings from $1
  • Context notes (`- <visible text> — inferred topic`)
  • Technical specs

**Validation Checks**

- Headers present and ordered
- All BDD criteria included for features/fallbacks
- Risks include likelihood and impact
- No URLs/secrets; exactly one blank line between sections
- $1 contains **only** visible link text (no external browsing)
```
