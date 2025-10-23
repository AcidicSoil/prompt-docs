# Prompt Docs

A structured playbook for ideation → scaffold → implementation → refactor → testing → docs → release.
Use the sidebar to explore, or jump straight into a workflow below.

[Get Started](#quick-start)

[Browse Sections](#whats-inside)

[Contribute](#contributing)

---

## Quick start

!!! tip "New Workflow!"
    - Sample workflow
    - QA-ready_refactor-plan
    - ops_apply
    - ops_quality
    - UniversalStarterPreOpsPromptTemplate

=== "Try these out first"
    - Follow for successful prompting [Sample workflow](temp-prompts-organized/_experimental/sample_workflow.experimental.md)
    - Need to refactor? Run first [QA-ready_refactor-plan](temp-prompts-organized/_experimental/QA-ready_refactor-plan.experimental.md)
    - Then, Run second [ops_apply](temp-prompts-organized/_experimental/ops_apply.experimental.md)
    - If needed, run [ops_quality](temp-prompts-organized/_experimental/ops_quality.experimental.md)
    - Universal Starter PreOps Prompt Template: [Universal Starter PreOps Prompt Template](temp-prompts-organized/_experimental/UniversalStarterPreOpsPromptTemplate.experimental.md)

!!! tip "First time here?"
    - Skim the **3 lanes** below (Plan / Build / Ship).
    - Use the **search** in the top-right.
    - Every page is Markdown—click **Edit this page** to propose improvements.

=== "Plan"
    - Write a quick PRD → [PRD generator](temp-prompts-organized/00-ideation/requirements/prd-generator.requirements.md)
    - Pick an architecture approach → [ADR – new](temp-prompts-organized/00-ideation/architecture/adr-new.architecture.md) • [Modular architecture](temp-prompts-organized/00-ideation/architecture/modular-architecture.architecture.md)
    - Define logging & SLOs → [Logging strategy](temp-prompts-organized/00-ideation/architecture/logging-strategy.architecture.md) • [SLO setup](temp-prompts-organized/10-scaffold/ci-setup/slo-setup.ci-setup.md)

=== "Build"
    - Bootstrap env & CI → [Env setup](temp-prompts-organized/10-scaffold/ci-setup/env-setup.ci-setup.md) • [DevOps automation](temp-prompts-organized/10-scaffold/ci-setup/devops-automation.ci-setup.md)
    - Start coding prompts → [Generate](temp-prompts-organized/20-implementation/impl/generate.impl.md) • [Feature flags](temp-prompts-organized/20-implementation/impl/feature-flags.impl.md)
    - Review & tighten → [PR description](temp-prompts-organized/20-implementation/review/pr-desc.review.md) • [Audit](temp-prompts-organized/20-implementation/review/audit.review.md)

=== "Ship"
    - Test coverage → [Coverage guide](temp-prompts-organized/40-testing/coverage/guide.coverage.md)
    - Prepare release notes → [Release notes (prepare)](temp-prompts-organized/60-release/changelog/release-notes-prepare.changelog.md)
    - Versioning → [Version proposal](temp-prompts-organized/60-release/versioning/version-proposal.versioning.md)

---

## What’s inside

- **Temp Prompts (organized)** — curated, step-by-step:
  - **00 · Ideation** → [Architecture](temp-prompts-organized/00-ideation/architecture/adr-new.architecture.md), [Design](temp-prompts-organized/00-ideation/design/api-contract.design.md), [Requirements](temp-prompts-organized/00-ideation/requirements/prd-generator.requirements.md)
  - **10 · Scaffold** → [CI setup](temp-prompts-organized/10-scaffold/ci-setup/devops-automation.ci-setup.md), [Conventions](temp-prompts-organized/10-scaffold/conventions/version-control-guide.conventions.md), [Scaffold](temp-prompts-organized/10-scaffold/scaffold/fullstack.scaffold.md)
  - **20 · Implementation** → [Impl](temp-prompts-organized/20-implementation/impl/commit.impl.md), [Review](temp-prompts-organized/20-implementation/review/review.review.md), [Spec-oriented](temp-prompts-organized/20-implementation/spec-orient/explain-code.spec-orient.md)
  - **30 · Refactor** → [Refactor file](temp-prompts-organized/30-refactor/refactor/refactor-file.refactor.md), [Perf eval](temp-prompts-organized/30-refactor/perf/model-evaluation.perf.md)
  - **40 · Testing** → [Integration test](temp-prompts-organized/40-testing/gen-tests/integration-test.gen-tests.md), [Flake fixes](temp-prompts-organized/40-testing/fix-flakes/explain-failures.fix-flakes.md)
  - **50 · Docs** → [API docs (local)](temp-prompts-organized/50-docs/api-docs/api-docs-local.api-docs.md)
  - **60 · Release** → [Changelog from commits](temp-prompts-organized/60-release/changelog/from-commits.changelog.md), [Post-release checks](temp-prompts-organized/60-release/post-release-checks/license-report.post-release-checks.md)

- **Temp Prompts (refactored)** — same ideas, reworked as single-file flows:
  - Jump in: [Action diagram](temp-prompts-refactored/action-diagram.md), [Prompt Optimizer](temp-prompts-refactored/Prompt-Optimizer.md), [Scaffold (full-stack)](temp-prompts-refactored/scaffold-fullstack.md)
  - Docs helpers: [Generate README](temp-prompts-refactored/generate-readme.md), [Docs 100%](temp-prompts-refactored/docs-fulfilled-100.md)

- **Shared & Templates**
  - `_Shared` → [TM overview](temp-prompts-organized/_shared/tm/overview.tm.md), [Reset strategy](temp-prompts-organized/_shared/reset-strategy.shared.md)
  - `_Templates` → [Instruction file](temp-prompts-organized/_templates/instruction-file.templates.md), [Prompt sequence generator](temp-prompts-organized/_templates/prompt-sequence-generator.templates.md)

---

## Common tasks

??? abstract "Plan a change (ADR + PRD checklist)"
    1. Start an ADR → [ADR – new](temp-prompts-organized/00-ideation/architecture/adr-new.architecture.md)
    2. Draft PRD → [PRD generator](temp-prompts-organized/00-ideation/requirements/prd-generator.requirements.md)
    3. Stakeholder review → [Planning process](temp-prompts-organized/00-ideation/requirements/planning-process.requirements.md)

??? example "Spin up a project scaffold"
    - CI & secrets → [Secrets manager](temp-prompts-organized/10-scaffold/ci-setup/secrets-manager-setup.ci-setup.md)
    - Monitoring & SLOs → [Monitoring setup](temp-prompts-organized/10-scaffold/ci-setup/monitoring-setup.ci-setup.md) • [SLO setup](temp-prompts-organized/10-scaffold/ci-setup/slo-setup.ci-setup.md)

??? tip "Run a crisp PR review"
    Use the trio:
    - [PR description helper](temp-prompts-organized/20-implementation/review/pr-desc.review.md)
    - [Cross-check](temp-prompts-organized/20-implementation/review/cross-check.review.md)
    - [Evidence capture](temp-prompts-organized/20-implementation/review/evidence-capture.review.md)

---

## Search like a pro

- Use **filters** in the search box (e.g. `flag lang:impl`), or just keywords like _“release notes prepare”_.
- Prefer **relative links** when you add content (keeps GitHub Pages happy under `/prompt-docs/`).
- Add a short **front-matter description** on new pages to improve search snippets.

!!! info "Helpful deep links"
    - Spec-oriented helpers: [Explain code](temp-prompts-organized/20-implementation/spec-orient/explain-code.spec-orient.md) • [Changed files](temp-prompts-organized/20-implementation/spec-orient/changed-files.spec-orient.md) • [Grep](temp-prompts-organized/20-implementation/spec-orient/grep.spec-orient.md)
    - Testing: [Integration test](temp-prompts-organized/40-testing/gen-tests/integration-test.gen-tests.md) • [Regression guard](temp-prompts-organized/40-testing/coverage/regression-guard.coverage.md)

---

## Contributing

1. Create a branch, add or edit Markdown under the appropriate section.
2. Keep file names consistent with the existing pattern (e.g., `*.impl.md`, `*.review.md`).
3. Submit a PR—use the [PR description helper](temp-prompts-organized/20-implementation/review/pr-desc.review.md).
4. After merge, the site auto-deploys (using `mkdocs build` + Pages).

[Open a new issue](https://github.com/AcidicSoil/prompt-docs/issues/new)  [Propose a change](https://github.com/AcidicSoil/prompt-docs/pulls)

---

## Release & versioning

- Draft notes → [Release notes (prepare)](temp-prompts-organized/60-release/changelog/release-notes-prepare.changelog.md)
- Generate from commits → [Changelog from commits](temp-prompts-organized/60-release/changelog/from-commits.changelog.md)
- Sanity pass → [Verify](temp-prompts-organized/60-release/changelog/verify.changelog.md)

---

### Credits

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and maintained in the **prompt-docs** repo.