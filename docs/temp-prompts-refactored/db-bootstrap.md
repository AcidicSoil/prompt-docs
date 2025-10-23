```md
# DB Bootstrap

Trigger: $1

Purpose: $2

**Steps:**

1. Create $3 for local dev (skip for sqlite).
2. Choose ORM/driver ($4) for SQL. Add migration config.
3. Create $5 with baseline tables (users, sessions, audit_log).
4. Add $6, $7, $8 scripts. Write seed data for local admin user.
5. Update $9 with `DATABASE_URL` and test connection script.

**Output format:** Migration plan list and generated file paths.

**Examples:** $10 → $11

**Notes:** Avoid destructive defaults; provide `--preview-feature` warnings if relevant.

---

### Affected files

- $12: db/compose.yaml
- $13: $5
- $14: $6
- $15: $7
- $16: $8
- $17: .env.example
```
