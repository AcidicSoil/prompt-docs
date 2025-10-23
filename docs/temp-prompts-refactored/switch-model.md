```md
<!-- Placeholders: $1=Task type, $2=Model selection criteria, $3=Input suite, $4=Metrics, $5=Recommended model, $6=Rationale, $7=Output format -->

**Switch Model**

Trigger: $1

Purpose: Decide when to try a different AI backend and how to compare.

## Steps

1. Define task type: $2
2. Select candidate models and temperature/tooling options.
3. Run a fixed input suite: $3 and measure $4.
4. Recommend a model per task: $5 with $6.

## Output format

- Table: task → model → settings → $7.
```
