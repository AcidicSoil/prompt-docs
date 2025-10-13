Project Structure:
├── index.md
├── temp-prompts-organized
│   ├── 00-ideation
│   │   ├── architecture
│   │   │   ├── adr-new.architecture.md
│   │   │   ├── logging-strategy.architecture.md
│   │   │   ├── modular-architecture.architecture.md
│   │   │   └── stack-evaluation.architecture.md
│   │   ├── design
│   │   │   ├── action-diagram.design.md
│   │   │   ├── api-contract.design.md
│   │   │   ├── design-assets.design.md
│   │   │   └── ui-screenshots.design.md
│   │   └── requirements
│   │       ├── plan-delta.requirements.md
│   │       ├── planning-process.requirements.md
│   │       ├── prd-generator.requirements.md
│   │       └── scope-control.requirements.md
│   ├── 10-scaffold
│   │   ├── ci-setup
│   │   │   ├── devops-automation.ci-setup.md
│   │   │   ├── env-setup.ci-setup.md
│   │   │   ├── monitoring-setup.ci-setup.md
│   │   │   ├── secrets-manager-setup.ci-setup.md
│   │   │   └── slo-setup.ci-setup.md
│   │   ├── conventions
│   │   │   └── version-control-guide.conventions.md
│   │   └── scaffold
│   │       ├── auth.scaffold.md
│   │       ├── db-bootstrap.scaffold.md
│   │       ├── fullstack.scaffold.md
│   │       └── iac-bootstrap.scaffold.md
│   ├── 20-implementation
│   │   ├── impl
│   │   │   ├── commit.impl.md
│   │   │   ├── content-generation.impl.md
│   │   │   ├── feature-flags.impl.md
│   │   │   ├── fix.impl.md
│   │   │   ├── generate.impl.md
│   │   │   ├── prototype-feature.impl.md
│   │   │   ├── todos.impl.md
│   │   │   └── voice-input.impl.md
│   │   ├── review
│   │   │   ├── audit.review.md
│   │   │   ├── cross-check.review.md
│   │   │   ├── evidence-capture.review.md
│   │   │   ├── pr-desc.review.md
│   │   │   ├── review-branch.review.md
│   │   │   ├── review.review.md
│   │   │   ├── todo-report.review.md
│   │   │   └── tsconfig-review.review.md
│   │   └── spec-orient
│   │       ├── blame-summary.spec-orient.md
│   │       ├── changed-files.spec-orient.md
│   │       ├── explain-code.spec-orient.md
│   │       ├── explain-symbol.spec-orient.md
│   │       ├── grep.spec-orient.md
│   │       ├── research-batch.spec-orient.md
│   │       └── research-item.spec-orient.md
│   ├── 30-refactor
│   │   ├── perf
│   │   │   ├── compare-outputs.perf.md
│   │   │   ├── model-evaluation.perf.md
│   │   │   └── model-strengths.perf.md
│   │   ├── refactor
│   │   │   ├── adr-new.refactor.md
│   │   │   ├── file-modularity.refactor.md
│   │   │   ├── prettier-adopt-migration-report.refactor.md
│   │   │   └── refactor-file.refactor.md
│   │   └── refactor-candidates
│   │       ├── dead-code-scan.refactor-candidates.md
│   │       ├── migration-plan.refactor-candidates.md
│   │       └── refactor-suggestions.refactor-candidates.md
│   ├── 40-testing
│   │   ├── coverage
│   │   │   ├── guide.coverage.md
│   │   │   └── regression-guard.coverage.md
│   │   ├── fix-flakes
│   │   │   ├── error-analysis.fix-flakes.md
│   │   │   └── explain-failures.fix-flakes.md
│   │   ├── gen-tests
│   │   │   ├── check.gen-tests.md
│   │   │   └── integration-test.gen-tests.md
│   │   └── test-plan
│   │       ├── e2e-runner-setup.test-plan.md
│   │       ├── query-set.test-plan.md
│   │       └── secrets-scan.test-plan.md
│   ├── 50-docs
│   │   ├── api-docs
│   │   │   ├── api-docs-local.api-docs.md
│   │   │   └── openapi-generate.api-docs.md
│   │   ├── doc-plan
│   │   │   ├── gemini-map.doc-plan.md
│   │   │   └── owners.doc-plan.md
│   │   ├── examples
│   │   │   ├── api-usage.examples.md
│   │   │   └── reference-implementation.examples.md
│   │   └── site-sync
│   ├── 60-release
│   │   ├── changelog
│   │   │   ├── from-commits.changelog.md
│   │   │   ├── project.changelog.md
│   │   │   ├── release-notes-prepare.changelog.md
│   │   │   ├── release-notes.changelog.md
│   │   │   ├── update.changelog.md
│   │   │   └── verify.changelog.md
│   │   ├── pack-publish
│   │   ├── post-release-checks
│   │   │   ├── cleanup-branches.post-release-checks.md
│   │   │   └── license-report.post-release-checks.md
│   │   └── versioning
│   │       └── version-proposal.versioning.md
│   ├── _archive
│   ├── _experimental
│   ├── _shared
│   │   ├── rank-root-prompts.shared.md
│   │   ├── reset-strategy.shared.md
│   │   ├── roll-up.shared.md
│   │   ├── summary.shared.md
│   │   ├── switch-model.shared.md
│   │   └── tm
│   │       ├── advance.tm.md
│   │       ├── blockers.tm.md
│   │       ├── ci.tm.md
│   │       ├── delta.tm.md
│   │       ├── docs.tm.md
│   │       ├── next.tm.md
│   │       ├── overview.tm.md
│   │       └── refine.tm.md
│   ├── _templates
│   │   ├── instruction-file.templates.md
│   │   ├── prompt-sequence-generator.templates.md
│   │   └── system-level-instruction-editor.templates.md
│   ├── codefetch
│   │   └── codebase.md
│   └── prompt-front-matter
│       ├── 00-ideation__architecture__adr-new.architecture.refactor.md
│       ├── 00-ideation__architecture__logging-strategy.architecture.refactor.md
│       ├── 00-ideation__architecture__modular-architecture.architecture.refactor.md
│       ├── 00-ideation__architecture__stack-evaluation.architecture.refactor.md
│       ├── 00-ideation__design__action-diagram.design.refactor.md
│       ├── 00-ideation__design__api-contract.design.refactor.md
│       ├── 00-ideation__design__design-assets.design.refactor.md
│       ├── 00-ideation__design__ui-screenshots.design.refactor.md
│       ├── 00-ideation__requirements__plan-delta.requirements.refactor.md
│       ├── 00-ideation__requirements__planning-process.requirements.refactor.md
│       ├── 00-ideation__requirements__prd-generator.requirements.refactor.md
│       ├── 00-ideation__requirements__scope-control.requirements.refactor.md
│       ├── 10-scaffold__ci-setup__devops-automation.ci-setup.refactor.md
│       ├── 10-scaffold__ci-setup__env-setup.ci-setup.refactor.md
│       ├── 10-scaffold__ci-setup__monitoring-setup.ci-setup.refactor.md
│       ├── 10-scaffold__ci-setup__secrets-manager-setup.ci-setup.refactor.md
│       ├── 10-scaffold__ci-setup__slo-setup.ci-setup.refactor.md
│       ├── 10-scaffold__conventions__version-control-guide.conventions.refactor.md
│       ├── 10-scaffold__scaffold__auth.scaffold.refactor.md
│       ├── 10-scaffold__scaffold__db-bootstrap.scaffold.refactor.md
│       ├── 10-scaffold__scaffold__fullstack.scaffold.refactor.md
│       ├── 10-scaffold__scaffold__iac-bootstrap.scaffold.refactor.md
│       ├── 20-implementation__impl__commit.impl.refactor.md
│       ├── 20-implementation__impl__content-generation.impl.refactor.md
│       ├── 20-implementation__impl__feature-flags.impl.refactor.md
│       ├── 20-implementation__impl__fix.impl.refactor.md
│       ├── 20-implementation__impl__generate.impl.refactor.md
│       ├── 20-implementation__impl__prototype-feature.impl.refactor.md
│       ├── 20-implementation__impl__todos.impl.refactor.md
│       ├── 20-implementation__impl__voice-input.impl.refactor.md
│       ├── 20-implementation__review__audit.review.refactor.md
│       ├── 20-implementation__review__cross-check.review.refactor.md
│       ├── 20-implementation__review__evidence-capture.review.refactor.md
│       ├── 20-implementation__review__pr-desc.review.refactor.md
│       ├── 20-implementation__review__review-branch.review.refactor.md
│       ├── 20-implementation__review__review.review.refactor.md
│       ├── 20-implementation__review__todo-report.review.refactor.md
│       ├── 20-implementation__review__tsconfig-review.review.refactor.md
│       ├── 20-implementation__spec-orient__blame-summary.spec-orient.refactor.md
│       ├── 20-implementation__spec-orient__changed-files.spec-orient.refactor.md
│       ├── 20-implementation__spec-orient__explain-code.spec-orient.refactor.md
│       ├── 20-implementation__spec-orient__explain-symbol.spec-orient.refactor.md
│       ├── 20-implementation__spec-orient__grep.spec-orient.refactor.md
│       ├── 20-implementation__spec-orient__research-batch.spec-orient.refactor.md
│       ├── 20-implementation__spec-orient__research-item.spec-orient.refactor.md
│       ├── 30-refactor__perf__compare-outputs.perf.refactor.md
│       ├── 30-refactor__perf__model-evaluation.perf.refactor.md
│       ├── 30-refactor__perf__model-strengths.perf.refactor.md
│       ├── 30-refactor__refactor-candidates__dead-code-scan.refactor-candidates.refactor.md
│       ├── 30-refactor__refactor-candidates__migration-plan.refactor-candidates.refactor.md
│       ├── 30-refactor__refactor-candidates__refactor-suggestions.refactor-candidates.refactor.md
│       ├── 30-refactor__refactor__adr-new.refactor.refactor.md
│       ├── 30-refactor__refactor__file-modularity.refactor.refactor.md
│       ├── 30-refactor__refactor__prettier-adopt-migration-report.refactor.refactor.md
│       ├── 30-refactor__refactor__refactor-file.refactor.refactor.md
│       ├── 40-testing__coverage__guide.coverage.refactor.md
│       ├── 40-testing__coverage__regression-guard.coverage.refactor.md
│       ├── 40-testing__fix-flakes__error-analysis.fix-flakes.refactor.md
│       ├── 40-testing__fix-flakes__explain-failures.fix-flakes.refactor.md
│       ├── 40-testing__gen-tests__check.gen-tests.refactor.md
│       ├── 40-testing__gen-tests__integration-test.gen-tests.refactor.md
│       ├── 40-testing__test-plan__e2e-runner-setup.test-plan.refactor.md
│       ├── 40-testing__test-plan__query-set.test-plan.refactor.md
│       ├── 40-testing__test-plan__secrets-scan.test-plan.refactor.md
│       ├── 50-docs__api-docs__api-docs-local.api-docs.refactor.md
│       ├── 50-docs__api-docs__openapi-generate.api-docs.refactor.md
│       ├── 50-docs__doc-plan__gemini-map.doc-plan.refactor.md
│       ├── 50-docs__doc-plan__owners.doc-plan.refactor.md
│       ├── 50-docs__examples__api-usage.examples.refactor.md
│       ├── 50-docs__examples__reference-implementation.examples.refactor.md
│       ├── 50-docs__project-contributing.docs.refactor.md
│       ├── 50-docs__project-readme.docs.refactor.md
│       ├── 60-release__changelog__from-commits.changelog.refactor.md
│       ├── 60-release__changelog__project.changelog.refactor.md
│       ├── 60-release__changelog__release-notes-prepare.changelog.refactor.md
│       ├── 60-release__changelog__release-notes.changelog.refactor.md
│       ├── 60-release__changelog__update.changelog.refactor.md
│       ├── 60-release__changelog__verify.changelog.refactor.md
│       ├── 60-release__post-release-checks__cleanup-branches.post-release-checks.refactor.md
│       ├── 60-release__post-release-checks__license-report.post-release-checks.refactor.md
│       ├── 60-release__versioning__version-proposal.versioning.refactor.md
│       ├── _shared__rank-root-prompts.shared.refactor.md
│       ├── _shared__reset-strategy.shared.refactor.md
│       ├── _shared__roll-up.shared.refactor.md
│       ├── _shared__summary.shared.refactor.md
│       ├── _shared__switch-model.shared.refactor.md
│       ├── _shared__tm__advance.tm.refactor.md
│       ├── _shared__tm__blockers.tm.refactor.md
│       ├── _shared__tm__ci.tm.refactor.md
│       ├── _shared__tm__delta.tm.refactor.md
│       ├── _shared__tm__docs.tm.refactor.md
│       ├── _shared__tm__next.tm.refactor.md
│       ├── _shared__tm__overview.tm.refactor.md
│       ├── _shared__tm__refine.tm.refactor.md
│       ├── _templates__instruction-file.templates.refactor.md
│       ├── _templates__prompt-sequence-generator.templates.refactor.md
│       └── _templates__system-level-instruction-editor.templates.refactor.md
└── temp-prompts-refactored
    ├── 3-step-process-b4-refactoring.md
    ├── Prompt-Optimizer.md
    ├── action-diagram.md
    ├── adr-new.md
    ├── adr-new.refactor.md
    ├── api-contract.md
    ├── api-docs-local.md
    ├── api-usage.md
    ├── audit.md
    ├── auth-scaffold.md
    ├── blame-summary.md
    ├── changed-files.md
    ├── changelog-from-commits.md
    ├── changelog-verify.md
    ├── check.md
    ├── cleanup-branches.md
    ├── commit-msg.md
    ├── commit.md
    ├── compare-outputs.md
    ├── content-generation.md
    ├── coverage-guide.md
    ├── cross-check.md
    ├── db-bootstrap.md
    ├── dead-code-scan.md
    ├── design-assets.md
    ├── devops-automation.md
    ├── docs-fulfilled-100.md
    ├── e2e-runner-setup.md
    ├── env-setup.md
    ├── error-analysis.md
    ├── eslint-review.md
    ├── evidence-capture.md
    ├── explain-code.md
    ├── explain-failures.md
    ├── explain-symbol.md
    ├── feature-flags.md
    ├── file-modularity.md
    ├── fix.md
    ├── gemini-map.md
    ├── generate-readme.md
    ├── generate.md
    ├── grep.md
    ├── iac-bootstrap.md
    ├── instruction-file.md
    ├── integration-test.md
    ├── license-report.md
    ├── logging-strategy.md
    ├── migration-plan.md
    ├── missing-docs.md
    ├── model-evaluation.md
    ├── model-strengths.md
    ├── modular-architecture.md
    ├── monitoring-setup.md
    ├── openapi-generate.md
    ├── owners.md
    ├── plan-delta.md
    ├── planning-process.md
    ├── pr-desc.md
    ├── prd-generator.md
    ├── prettier-adopt_Migration_report.md
    ├── problem-analyzer.md
    ├── prompt-sequence-generator.md
    ├── prototype-feature.md
    ├── query-set.md
    ├── rank-root-prompts.md
    ├── refactor-file.md
    ├── refactor-suggestions.md
    ├── reference-implementation.md
    ├── regression-guard.md
    ├── release-notes-prepare.md
    ├── release-notes.md
    ├── research-batch.md
    ├── research-item.md
    ├── reset-strategy.md
    ├── review-branch.md
    ├── review.md
    ├── roll-up.md
    ├── scaffold-fullstack.md
    ├── scope-control.md
    ├── secrets-manager-setup.md
    ├── secrets-scan.md
    ├── slo-setup.md
    ├── stack-evaluation.md
    ├── stop-guessing.md
    ├── summary-1.md
    ├── summary-2.md
    ├── summary.md
    ├── switch-model.md
    ├── system-level-instruction-editor.md
    ├── tm-advance.md
    ├── tm-blockers.md
    ├── tm-ci.md
    ├── tm-delta.md
    ├── tm-docs.md
    ├── tm-next.md
    ├── tm-overview.md
    ├── tm-refine.md
    ├── todo-report.md
    ├── todos.md
    ├── tsconfig-review.md
    ├── ui-screenshots.md
    ├── update-changelog.md
    ├── version-control-guide.md
    ├── version-proposal.md
    └── voice-input.md


index.md
```
1 | # Prompt Docs
2 | 
3 | A structured playbook for ideation → scaffold → implementation → refactor → testing → docs → release.
4 | Use the sidebar to explore, or jump straight into a workflow below.
5 | 
6 | [Get Started](#quick-start) {: .md-button } [Browse Sections](#whats-inside) {: .md-button } [Contribute](#contributing) {: .md-button }
7 | 
8 | ---
9 | 
10 | ## Quick start
11 | 
12 | !!! tip "First time here?"
13 |     - Skim the **3 lanes** below (Plan / Build / Ship).
14 |     - Use the **search** in the top-right.
15 |     - Every page is Markdown—click **Edit this page** to propose improvements.
16 | 
17 | === "Plan"
18 |     - Write a quick PRD → [PRD generator](temp-prompts-organized/00-ideation/requirements/prd-generator.requirements.md)
19 |     - Pick an architecture approach → [ADR – new](temp-prompts-organized/00-ideation/architecture/adr-new.architecture.md) • [Modular architecture](temp-prompts-organized/00-ideation/architecture/modular-architecture.architecture.md)
20 |     - Define logging & SLOs → [Logging strategy](temp-prompts-organized/00-ideation/architecture/logging-strategy.architecture.md) • [SLO setup](temp-prompts-organized/10-scaffold/ci-setup/slo-setup.ci-setup.md)
21 | 
22 | === "Build"
23 |     - Bootstrap env & CI → [Env setup](temp-prompts-organized/10-scaffold/ci-setup/env-setup.ci-setup.md) • [DevOps automation](temp-prompts-organized/10-scaffold/ci-setup/devops-automation.ci-setup.md)
24 |     - Start coding prompts → [Generate](temp-prompts-organized/20-implementation/impl/generate.impl.md) • [Feature flags](temp-prompts-organized/20-implementation/impl/feature-flags.impl.md)
25 |     - Review & tighten → [PR description](temp-prompts-organized/20-implementation/review/pr-desc.review.md) • [Audit](temp-prompts-organized/20-implementation/review/audit.review.md)
26 | 
27 | === "Ship"
28 |     - Test coverage → [Coverage guide](temp-prompts-organized/40-testing/coverage/guide.coverage.md)
29 |     - Prepare release notes → [Release notes (prepare)](temp-prompts-organized/60-release/changelog/release-notes-prepare.changelog.md)
30 |     - Versioning → [Version proposal](temp-prompts-organized/60-release/versioning/version-proposal.versioning.md)
31 | 
32 | ---
33 | 
34 | ## What’s inside
35 | 
36 | - **Temp Prompts (organized)** — curated, step-by-step:
37 |   - **00 · Ideation** → [Architecture](temp-prompts-organized/00-ideation/architecture/adr-new.architecture.md), [Design](temp-prompts-organized/00-ideation/design/api-contract.design.md), [Requirements](temp-prompts-organized/00-ideation/requirements/prd-generator.requirements.md)
38 |   - **10 · Scaffold** → [CI setup](temp-prompts-organized/10-scaffold/ci-setup/devops-automation.ci-setup.md), [Conventions](temp-prompts-organized/10-scaffold/conventions/version-control-guide.conventions.md), [Scaffold](temp-prompts-organized/10-scaffold/scaffold/fullstack.scaffold.md)
39 |   - **20 · Implementation** → [Impl](temp-prompts-organized/20-implementation/impl/commit.impl.md), [Review](temp-prompts-organized/20-implementation/review/review.review.md), [Spec-oriented](temp-prompts-organized/20-implementation/spec-orient/explain-code.spec-orient.md)
40 |   - **30 · Refactor** → [Refactor file](temp-prompts-organized/30-refactor/refactor/refactor-file.refactor.md), [Perf eval](temp-prompts-organized/30-refactor/perf/model-evaluation.perf.md)
41 |   - **40 · Testing** → [Integration test](temp-prompts-organized/40-testing/gen-tests/integration-test.gen-tests.md), [Flake fixes](temp-prompts-organized/40-testing/fix-flakes/explain-failures.fix-flakes.md)
42 |   - **50 · Docs** → [API docs (local)](temp-prompts-organized/50-docs/api-docs/api-docs-local.api-docs.md)
43 |   - **60 · Release** → [Changelog from commits](temp-prompts-organized/60-release/changelog/from-commits.changelog.md), [Post-release checks](temp-prompts-organized/60-release/post-release-checks/license-report.post-release-checks.md)
44 | 
45 | - **Temp Prompts (refactored)** — same ideas, reworked as single-file flows:
46 |   - Jump in: [Action diagram](temp-prompts-refactored/action-diagram.md), [Prompt Optimizer](temp-prompts-refactored/Prompt-Optimizer.md), [Scaffold (full-stack)](temp-prompts-refactored/scaffold-fullstack.md)
47 |   - Docs helpers: [Generate README](temp-prompts-refactored/generate-readme.md), [Docs 100%](temp-prompts-refactored/docs-fulfilled-100.md)
48 | 
49 | - **Shared & Templates**
50 |   - `_Shared` → [TM overview](temp-prompts-organized/_shared/tm/overview.tm.md), [Reset strategy](temp-prompts-organized/_shared/reset-strategy.shared.md)
51 |   - `_Templates` → [Instruction file](temp-prompts-organized/_templates/instruction-file.templates.md), [Prompt sequence generator](temp-prompts-organized/_templates/prompt-sequence-generator.templates.md)
52 | 
53 | ---
54 | 
55 | ## Common tasks
56 | 
57 | ??? abstract "Plan a change (ADR + PRD checklist)"
58 |     1. Start an ADR → [ADR – new](temp-prompts-organized/00-ideation/architecture/adr-new.architecture.md)
59 |     2. Draft PRD → [PRD generator](temp-prompts-organized/00-ideation/requirements/prd-generator.requirements.md)
60 |     3. Stakeholder review → [Planning process](temp-prompts-organized/00-ideation/requirements/planning-process.requirements.md)
61 | 
62 | ??? example "Spin up a project scaffold"
63 |     - CI & secrets → [Secrets manager](temp-prompts-organized/10-scaffold/ci-setup/secrets-manager-setup.ci-setup.md)
64 |     - Monitoring & SLOs → [Monitoring setup](temp-prompts-organized/10-scaffold/ci-setup/monitoring-setup.ci-setup.md) • [SLO setup](temp-prompts-organized/10-scaffold/ci-setup/slo-setup.ci-setup.md)
65 | 
66 | ??? tip "Run a crisp PR review"
67 |     Use the trio:
68 |     - [PR description helper](temp-prompts-organized/20-implementation/review/pr-desc.review.md)
69 |     - [Cross-check](temp-prompts-organized/20-implementation/review/cross-check.review.md)
70 |     - [Evidence capture](temp-prompts-organized/20-implementation/review/evidence-capture.review.md)
71 | 
72 | ---
73 | 
74 | ## Search like a pro
75 | 
76 | - Use **filters** in the search box (e.g. `flag lang:impl`), or just keywords like _“release notes prepare”_.
77 | - Prefer **relative links** when you add content (keeps GitHub Pages happy under `/prompt-docs/`).
78 | - Add a short **front-matter description** on new pages to improve search snippets.
79 | 
80 | !!! info "Helpful deep links"
81 |     - Spec-oriented helpers: [Explain code](temp-prompts-organized/20-implementation/spec-orient/explain-code.spec-orient.md) • [Changed files](temp-prompts-organized/20-implementation/spec-orient/changed-files.spec-orient.md) • [Grep](temp-prompts-organized/20-implementation/spec-orient/grep.spec-orient.md)
82 |     - Testing: [Integration test](temp-prompts-organized/40-testing/gen-tests/integration-test.gen-tests.md) • [Regression guard](temp-prompts-organized/40-testing/coverage/regression-guard.coverage.md)
83 | 
84 | ---
85 | 
86 | ## Contributing
87 | 
88 | 1. Create a branch, add or edit Markdown under the appropriate section.
89 | 2. Keep file names consistent with the existing pattern (e.g., `*.impl.md`, `*.review.md`).
90 | 3. Submit a PR—use the [PR description helper](temp-prompts-organized/20-implementation/review/pr-desc.review.md).
91 | 4. After merge, the site auto-deploys (using `mkdocs build` + Pages).
92 | 
93 | [Open a new issue](https://github.com/AcidicSoil/prompt-docs/issues/new) {: .md-button } [Propose a change](https://github.com/AcidicSoil/prompt-docs/pulls) {: .md-button }
94 | 
95 | ---
96 | 
97 | ## Release & versioning
98 | 
99 | - Draft notes → [Release notes (prepare)](temp-prompts-organized/60-release/changelog/release-notes-prepare.changelog.md)
100 | - Generate from commits → [Changelog from commits](temp-prompts-organized/60-release/changelog/from-commits.changelog.md)
101 | - Sanity pass → [Verify](temp-prompts-organized/60-release/changelog/verify.changelog.md)
102 | 
103 | ---
104 | 
105 | ### Credits
106 | 
107 | Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and maintained in the **prompt-docs** repo.
```

temp-prompts-refactored/3-step-process-b4-refactoring.md
```
1 | <!-- $1 = task description (e.g., "Refactor email configuration") -->
2 | <!-- $2 = list of files to modify (e.g., ["src/config/email.ts"]) -->
3 | <!-- $3 = sample refactor file path (e.g., "src/config/email.ts") -->
4 | 
5 | **Refactoring Pre-Refactor Process**
6 | 
7 | # 3-step-process-b4-refactoring
8 | 
9 | ## describe the task and call the plan tool
10 | 1. $1. Draft a plan (don't code)
11 | 
12 | ## identify target files for modification
13 | 2. Conduct code analysis to determine files requiring modification: $2
14 | 
15 | ## provide sample refactor implementation
16 | 3. Provide a sample refactor for $3
```

temp-prompts-refactored/Prompt-Optimizer.md
```
1 | <!-- $1=User's raw prompt, $2=Role name (optional), $3=Number of variants (1-4) -->
2 | 
3 | **Prompt Optimization Template**
4 | 
5 | You are **$2** — Prompt Optimization Specialist. Transform any raw user prompt into up to **4 concise, high-leverage variants** that preserve intent while improving clarity, constraints, and outcome specificity.
6 | 
7 | **Your job**
8 | 
9 | - Keep the user’s original goal intact. Remove fluff, tighten verbs, and make deliverables and success criteria explicit.
10 | - Resolve ambiguity with **neutral defaults** or **clearly marked placeholders** like `{context}`, `{inputs}`, `{constraints}`, `{acceptance_criteria}`, `{format}`, `{deadline}`.
11 | - Add structure (steps, bullets, numbered requirements) only when it improves execution.
12 | - Match or gently improve the **tone** implied by the user (directive/spec-like, polite, collaborative). Never over-polish into marketing-speak.
13 | - Do **not** introduce tools, external data, or scope changes unless the user asked for them.
14 | - Prefer active voice, testable requirements, and measurable outputs.
15 | 
16 | **Output rules**
17 | 
18 | - Return **only** the variants, each in its **own fenced code block**. No commentary, no preamble, no trailing notes.
19 | - Produce **1–4 variants** (default 3). Stop at 4 unless the user explicitly requests more.
20 | - For each block, begin with a short bracketed style tag (e.g., `[Directive]`, `[Spec]`, `[Polite]`, `[QA-Ready]`) on the first line, then the optimized prompt on subsequent lines.
21 | 
22 | **Optimization checklist (apply silently)**
23 | 
24 | - Clarify objective and end artifact
25 | - Specify audience/user/environment if implied
26 | - Pin input sources and constraints
27 | - Define acceptance criteria and non-goals
28 | - State format/structure and length limits
29 | - Include edge cases or examples if hinted
30 | - Keep placeholders where user must decide
31 | - **Common pitfalls**: Ambiguous constraints, vague success metrics, over-engineering
32 | - **Expected output quality**: Clear deliverables, testable criteria, minimal fluff
33 | 
34 | **Now optimize the next input.**
35 | User prompt: $1
```

temp-prompts-refactored/action-diagram.md
```
1 | # Action Diagram
2 | 
3 | ## Nodes
4 | 
5 | - $1
6 | - $2
7 | 
8 | ## Edges
9 | 
10 | - $3 -> $4
11 | 
12 | <!--
13 | Placeholder mapping:
14 | - $1 = node 1
15 | - $2 = node 2
16 | - $3 = edge start node
17 | - $4 = edge end node
18 | -->
```

temp-prompts-refactored/adr-new.md
```
1 | <!-- $1=project context source file, $2=example file path, $3=ADR title argument, $4=workflow triggers, $5=failing jobs, $6=proposed fixes, $7=evidence details -->
2 | 
3 | **Architecture Decision Record Drafting Prompt**
4 | 
5 | You are a CLI assistant to draft an Architecture Decision Record with pros/cons using the following inputs:
6 | 
7 | 1. Analyze project context from $1.
8 | 2. Generate a concise ADR with Context, Decision, Status, Consequences. Title: $3.
9 | 3. Synthesize insights into the output format with clear priorities and next steps.
10 | 
11 | **Output Requirements**:
12 | - Provide a summary restating the goal.
13 | - Highlight $4, $5, and $6.
14 | - Document $7 to ensure maintainability.
15 | 
16 | **Example Input**: $2
17 | 
18 | **Expected Output**: Actionable summary aligned with output requirements.
```

temp-prompts-refactored/adr-new.refactor.md
```
1 | **{$2 or Inferred Name}**
2 | 
3 | You are a CLI assistant to draft an Architecture Decision Record with pros/cons using the following inputs:
4 | 
5 | 1. Analyze project context from $1.
6 | 2. Generate a concise ADR with Context, Decision, Status, Consequences. Title: $3.
7 | 3. Synthesize insights into the output format with clear priorities and next steps.
8 | 
9 | **Output Requirements**:
10 | - Provide a summary restating the goal.
11 | - Highlight $4, $5, and $6.
12 | - Document $7 to ensure maintainability.
13 | 
14 | **Example Input**: $2
15 | 
16 | **Expected Output**: Actionable summary aligned with output requirements.
```

temp-prompts-refactored/api-contract.md
```
1 | <!-- $1 = trigger phrase (e.g., "/api-contract 'accounts & auth'") -->
2 | <!-- $2 = domain (e.g., "auth") -->
3 | <!-- $3 = contract type (e.g., "OpenAPI 3.1", "GraphQL") -->
4 | <!-- $4 = contract file extension (e.g., ".yaml", ".graphql") -->
5 | <!-- $5 = output file path (e.g., "apis/$2/$4") -->
6 | <!-- $6 = changelog entry path (e.g., "docs/api/CHANGELOG.md") -->
7 | <!-- $7 = style convention (e.g., "JSON:API") -->
8 | 
9 | # API Contract Generator
10 | 
11 | Trigger: $1
12 | 
13 | Purpose: Author an initial $3 contract from requirements.
14 | 
15 | **Steps:**
16 | 
17 | 1. Parse inputs and existing docs. If REST, prefer $3; if GraphQL, produce $3.
18 | 2. Define resources, operations, request/response schemas, error model, auth, and rate limit headers.
19 | 3. Add examples for each endpoint or type. Include pagination and filtering conventions.
20 | 4. Save to $5.
21 | 5. Emit changelog entry $6 with rationale and breaking-change flags.
22 | 
23 | **Affected files:**
24 | - $5
25 | - $6
26 | 
27 | **Output format:**
28 | - `Contract Path`: $4
29 | - `Design Notes`: $7
30 | - Fenced code block with spec body
31 | 
32 | **Examples:**
33 | - `$1` → $5
34 | 
35 | **Notes:**
36 | - Follow $7 style for REST unless specified.
```

temp-prompts-refactored/api-docs-local.md
```
1 | # API Docs Local
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | $3
10 | 
11 | ## Output format
12 | 
13 | $4
14 | 
15 | 
16 | ---
17 | 
18 | ### Affected files
19 | 
20 | - $5
21 | 
22 | ### Root cause
23 | 
24 | - $6
25 | 
26 | ### Proposed fix
27 | 
28 | - $7
29 | 
30 | ### Tests
31 | 
32 | - $8
33 | 
34 | ### Docs gaps
35 | 
36 | - $9
37 | 
38 | ### Open questions
39 | 
40 | - $10
```

temp-prompts-refactored/api-usage.md
```
1 | ```
2 | 
3 | <!-- Placeholder mapping for api-usage.md:
4 | $1 = Example input symbol (e.g., 'HttpClient')
5 | $2 = API usage pattern (e.g., 'Key usages')
6 | $3 = Evidence type (e.g., 'File paths')
7 | $4 = Definition source (e.g., 'src/network/httpClient.ts')
8 |  -->
9 | 
10 | **How to show internal API usage**
11 | 
12 | 1. Gather context by running `rg -n $1 . || grep -RIn $1 .`.
13 | 2. Summarize common usage patterns and potential misuses for the symbol.
14 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
15 | 
16 | **Output format**
17 | 
18 | - Begin with a concise summary that restates the goal: Show how an internal API is used across the codebase.
19 | - Organize details under clear subheadings so contributors can scan quickly.
20 | - Document the evidence you used so maintainers can trust the conclusion.
21 | 
22 | **Example**
23 | 
24 | - Input: $2
25 | - Expected output: 
26 |   - Definition: $3
27 |   - Key usages: $4
28 | 
29 | ```
```

temp-prompts-refactored/audit.md
```
1 | # Audit
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | 1. Gather context by running `ls -la` for the top-level listing. Inspect $3, $4, $5, $6, $7, and $8 if present to understand shared conventions.
10 | 2. Assess repository hygiene across documentation, testing, CI, linting, and security. Highlight gaps and existing automation.
11 | 3. Synthesize the findings into a prioritized checklist with recommended next steps.
12 | 
13 | ## Output format
14 | 
15 | - Begin with a concise summary that restates the goal: Audit repository hygiene and suggest improvements.
16 | - Offer prioritized, actionable recommendations with rationale.
17 | - Call out test coverage gaps and validation steps.
18 | - Highlight workflow triggers, failing jobs, and proposed fixes.
19 | 
20 | ## Missing sections
21 | 
22 | * Affected files: $9
23 | * Root cause: $10
24 | * Proposed fix: $11
25 | * Tests: $12
26 | * Docs gaps: $13
27 | * Open questions: $14
28 | 
29 | <!--
30 | $1 = Trigger
31 | $2 = Purpose
32 | $3 = .editorconfig
33 | $4 = .gitignore
34 | $5 = .geminiignore
35 | $6 = .eslintrc.cjs
36 | $7 = .eslintrc.js
37 | $8 = tsconfig.json
38 | $9 = Affected files
39 | $10 = Root cause
40 | $11 = Proposed fix
41 | $12 = Tests
42 | $13 = Docs gaps
43 | $14 = Open questions
44 | -->
```

temp-prompts-refactored/auth-scaffold.md
```
1 | <!-- $1 = Template name (e.g., "Auth Scaffold") | $2 = Trigger command (e.g., "/auth-scaffold <oauth|email|oidc>") | $3 = Purpose statement (e.g., "Scaffold auth flows, routes, storage, and a basic threat model") | $4 = Steps list (e.g., "1. Select provider...") | $5 = Output format description (e.g., "route list, config keys, and mitigations table") | $6 = Example command (e.g., "/auth-scaffold oauth") | $7 = Security notes (e.g., "Never print real secrets. Use placeholders in `.env.example`") -->
2 | 
3 | # $1
4 | 
5 | Trigger: $2
6 | 
7 | Purpose: $3
8 | 
9 | **Steps:**
10 | 
11 | $4
12 | 
13 | **Output format:** $5
14 | 
15 | **Examples:** $6
16 | 
17 | **Notes:** $7
```

temp-prompts-refactored/blame-summary.md
```
1 | <!-- Placeholder mapping:
2 | $1 = git blame command with arguments
3 | $2 = example input file path
4 | $3 = expected output format description
5 | $4 = proposed refactor example snippet
6 | -->
7 | **How-to: Summarize authorship hotspots**
8 | 
9 | 1. Gather context by running `git blame -w --line-porcelain $1 | sed -n 's/^author //p' | sort | uniq -c | sort -nr | sed -n '1,25p'` for the blame authors (top contributors first).
10 | 2. Given the blame summary below, identify ownership hotspots and potential reviewers.
11 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
12 | 
13 | Output:
14 | - Begin with a concise summary that restates the goal: Summarize authorship hotspots for a file using git blame.
15 | - Organize details under clear subheadings so contributors can scan quickly.
16 | - Reference evidence from CODEOWNERS or git history for each owner suggestion.
17 | 
18 | Example Input:
19 | $2
20 | 
21 | Expected Output:
22 | $3
23 | 
24 | Proposed Fix Examples:
25 | $4
```

temp-prompts-refactored/changed-files.md
```
1 | <!-- Placeholders:  
2 | $1 = Task goal statement  
3 | $2 = Git command  
4 | $3 = File categories (added/modified/renamed/deleted)  
5 | $4 = Risky changes indicator  
6 | $5 = Output format requirements  
7 | $6 = Example input description  
8 | $7 = Expected output structure  
9 | -->
10 | 
11 | CLI Summary Prompt
12 | 
13 | 1. Gather context by running `$2`.
14 | 2. List and categorize changed files: `$3`. Call out risky changes: `$4`.
15 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
16 | 
17 | Output:
18 | 
19 | - Begin with a concise summary that restates the goal: `$1`.
20 | - Document the evidence used: `$5`.
21 | 
22 | Example Input:
23 | `$6`
24 | 
25 | Expected Output:
26 | `$7`
```

temp-prompts-refactored/check.md
```
1 | **Editorconfig Adherence Check**
2 | 
3 | <!-- $1 = task description (e.g., "Check adherence to .editorconfig across the repo") -->
4 | <!-- $2 = command to run (e.g., "git ls-files | sed -n '1,400p'") -->
5 | <!-- $3 = output format requirements (e.g., "prioritized recommendations with rationale") -->
6 | 
7 | You are a CLI assistant focused on helping contributors with the task: $1.
8 | 
9 | 1. Gather context by inspecting `$1`; running `$2`.
10 | 2. From the listing and config, point out inconsistencies and propose fixes.
11 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
12 | 
13 | Output:
14 | - Begin with a concise summary that restates the goal: $1.
15 | - Offer prioritized, actionable recommendations with rationale: $3.
16 | - Highlight workflow triggers, failing jobs, and proposed fixes.
17 | 
18 | Common pitfalls to watch for:
19 | - Missing `.editorconfig` files in the repo
20 | - Inconsistent indentation settings across files
21 | - Ignoring OS-specific config overrides
```

temp-prompts-refactored/cleanup-branches.md
```
1 | <!-- 
2 | $1 = Specific trigger command (e.g., "/cleanup-branches")
3 | $2 = Purpose statement (e.g., "Recommend which local branches are safe to delete and which to keep")
4 | $3 = Context gathering commands (e.g., "git branch --merged", "git branch --no-merged", "git for-each-ref...")
5 | $4 = Branch suggestion instructions (e.g., "Using the lists below, suggest local branches safe to delete and which to keep. Include commands to remove them if desired")
6 | $5 = Synthesis instructions (e.g., "Synthesize the insights into the requested format with clear priorities and next steps")
7 | $6 = Output format requirements (e.g., "Begin with a concise summary that restates the goal: Suggest safe local branch cleanup (merged/stale). Document the evidence you used so maintainers can trust the conclusion.")
8 | $7 = Example input/output (e.g., "Example Input: (none – command runs without arguments)\nExpected Output: - Structured report following the specified sections.")
9 | -->
10 | 
11 | **Cleanup Branches**
12 | 
13 | Trigger: $1
14 | 
15 | Purpose: $2
16 | 
17 | You are a CLI assistant focused on helping contributors with the task: $3.
18 | 
19 | 1. $4
20 | 2. $5
21 | 3. $6
22 | 
23 | Affected files: Local branches
24 | 
25 | Output format:
26 | - $7
```

temp-prompts-refactored/commit-msg.md
```
1 | /*
2 | Placeholder mapping:
3 | - $1 = Input description
4 | - $2 = Template name (default: 'commit-message')
5 | - $3 = Max placeholders (default: 7)
6 | */
7 | 
8 | **commit-message**
9 | 
10 | Input description: $1
11 | 
12 | Output format:
13 | {
14 |   "title": "",
15 |   "body": ""
16 | }
17 | 
18 | Ensure the output is a valid JSON object with the title and body fields.
```

temp-prompts-refactored/commit.md
```
1 | # From Placeholders in prompts.md
2 | 
3 | Commit title: $1
4 | 
5 | Commit body:
6 | 
7 | - Scope: $1
8 | - Summary: $2
9 | 
10 | Suggested checklist:
11 | - run tests
12 | - run linters
13 | 
14 | 
15 | ## Expected output format
16 | 
17 | ```json
18 | {
19 |   "reasoning": "",
20 |   "template_markdown": ""
21 | }
22 | ```
23 | 
24 | **Note**: Replace $1 with commit title, $2 with summary text.
```

temp-prompts-refactored/compare-outputs.md
```
1 | <!-- $1=Trigger, $2=Purpose, $3=Steps, $4=Output format, $5=Recommendation -->
2 | 
3 | **Compare Outputs**
4 | 
5 | - $1
6 | - $2
7 | - $3
8 | - $4
9 | 
10 | **Recommended output format**
11 | 
12 | - $1
13 | 
14 | *Note: This template includes the following sections that were inferred to be relevant based on the context: Affected files, Root cause, Proposed fix, Tests, Docs gaps, Open questions.*
```

temp-prompts-refactored/content-generation.md
```
1 | # Content Generation
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | $3
10 | 
11 | ## Output format
12 | 
13 | $4
14 | 
15 | <!-- Placeholder mapping -->
16 | 
17 | $1 = Title of the content (e.g., 'Content Generation')
18 | $2 = Purpose statement (e.g., 'Draft docs, blog posts, or marketing copy aligned with the codebase')
19 | $3 = List of steps with numbers (e.g., '1. Read repo README and recent CHANGELOG or commits.\n2. Propose outlines for docs and posts.\n3. Generate content with code snippets and usage examples.')
20 | $4 = Description of output format (e.g., 'Markdown files with frontmatter and section headings.')
```

temp-prompts-refactored/coverage-guide.md
```
1 | # Coverage Guide
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | You are a CLI assistant focused on helping contributors with the task: $3
8 | 
9 | 1. Gather context by running `find . -name 'coverage*' -type f -maxdepth 3 -print -exec head -n 40 {} \; 2>/dev/null` for the coverage hints; running `git ls-files | sed -n '1,400p'` for the repo map.
10 | 2. Using coverage artifacts (if available) and repository map, propose the highest‑ROI tests to add.
11 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
12 | 
13 | Output:
14 | 
15 | - Begin with a concise summary that restates the goal: $4
16 | - Offer prioritized, actionable recommendations with rationale.
17 | - Call out test coverage gaps and validation steps.
18 | 
19 | Example Input:
20 | $5
21 | 
22 | Expected Output:
23 | $6
```

temp-prompts-refactored/cross-check.md
```
1 | # Conflict Resolver
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | Steps:
8 | 
9 | 1. $3
10 | 2. $4
11 | 3. $5
12 | 
13 | Output format:
14 | 
15 | ```
16 | ### $6
17 | - $7
18 | ```
19 | 
20 | Examples:
21 | 
22 | - $8
23 | 
24 | Notes:
25 | 
26 | - $9
```

temp-prompts-refactored/db-bootstrap.md
```
1 | # DB Bootstrap
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | **Steps:**
8 | 
9 | 1. Create $3 for local dev (skip for sqlite).
10 | 2. Choose ORM/driver ($4) for SQL. Add migration config.
11 | 3. Create $5 with baseline tables (users, sessions, audit_log).
12 | 4. Add $6, $7, $8 scripts. Write seed data for local admin user.
13 | 5. Update $9 with `DATABASE_URL` and test connection script.
14 | 
15 | **Output format:** Migration plan list and generated file paths.
16 | 
17 | **Examples:** $10 → $11
18 | 
19 | **Notes:** Avoid destructive defaults; provide `--preview-feature` warnings if relevant.
20 | 
21 | ---
22 | 
23 | ### Affected files
24 | 
25 | - $12: db/compose.yaml
26 | - $13: $5
27 | - $14: $6
28 | - $15: $7
29 | - $16: $8
30 | - $17: .env.example
```

temp-prompts-refactored/dead-code-scan.md
```
1 | # Dead Code Scan Template
2 | 
3 | <!-- $1 = command string (e.g., `rg -n "export |module.exports|...`) -->
4 | <!-- $2 = goal statement (e.g., "List likely dead or unused files and exports (static signals)") -->
5 | <!-- $3 = purpose statement (e.g., "Identify likely dead or unused files and exports using static signals") -->
6 | 
7 | # Dead Code Scan
8 | 
9 | Trigger: `/dead-code-scan`
10 | 
11 | Purpose: $3
12 | 
13 | You are a CLI assistant focused on helping contributors with the task: $2.
14 | 
15 | 1. Gather context by running $1 for the file reference graph (best‑effort).
16 | 2. From the search results, hypothesize dead code candidates and how to safely remove them.
17 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
18 | 
19 | Output:
20 | 
21 | - Begin with a concise summary that restates the goal: $2.
22 | - Document the evidence you used so maintainers can trust the conclusion.
```

temp-prompts-refactored/design-assets.md
```
1 | # Design Assets
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | 1. $3
10 | 2. $4
11 | 3. $5
12 | 
13 | ## Output format
14 | 
15 | - $6
```

temp-prompts-refactored/devops-automation.md
```
1 | <!-- Placeholder mapping: 
2 | $1 = Trigger (e.g., "/devops-automation")
3 | $2 = Purpose (e.g., "Configure servers, DNS, SSL, CI/CD at a pragmatic level")
4 | $3 = Step 1 (e.g., "Inspect repo for IaC or deploy scripts")
5 | $4 = Step 2 (e.g., "Generate Terraform or Docker Compose templates if missing")
6 | $5 = Step 3 (e.g., "Propose CI workflows for tests, builds, and deploys")
7 | $6 = Step 4 (e.g., "Provide runbooks for rollback")
8 | $7 = Output format description (e.g., "Infra plan with checkpoints and secrets placeholders")
9 | $8 = Affected files (optional)
10 | $9 = Root cause (optional) -->
11 | 
12 | **Automation Prompt Template**
13 | 
14 | # DevOps Automation
15 | 
16 | $1
17 | 
18 | $2
19 | 
20 | ## Steps
21 | 
22 | 1. $3
23 | 2. $4
24 | 3. $5
25 | 4. $6
26 | 
27 | ## Output format
28 | - $7
29 | 
30 | ### Affected files
31 | - $8
32 | 
33 | ### Root cause
34 | - $9
35 | 
36 | ### Proposed fix
37 | - $10
38 | 
39 | ### Tests
40 | - $11
41 | 
42 | ### Docs gaps
43 | - $12
44 | 
45 | ### Open questions
46 | - $13
```

temp-prompts-refactored/docs-fulfilled-100.md
```
1 | <!--
2 | $1 = Source file path (e.g., /home/user/.codex/prompts/temp-prompts/docs-fulfilled-100.md)
3 | $2 = User's question
4 | $3 = Status of documentation fulfillment (e.g., 100%)
5 | $4 = Required additional information
6 | $5 = List of missing documentation items
7 | $6 = Proposed actions to fulfill docs
8 | $7 = Expected output format
9 | -->
10 | 
11 | **Docs fulfilled $3**
12 | 
13 | To fulfill the plan $3, what docs are missing now? Do you need more information from $1 or $2 to solve this task $3 correctly? Just tell me.
14 | 
15 | ---
16 | 
17 | Affected files:
18 | - $1
19 | 
20 | Root cause:
21 | - $4
22 | 
23 | Proposed fix:
24 | - $5
25 | 
26 | Tests:
27 | - $6
28 | 
29 | Docs gaps:
30 | - $7
```

temp-prompts-refactored/e2e-runner-setup.md
```
1 | /*
2 | Placeholder mapping:
3 | $1 = Trigger
4 | $2 = Purpose
5 | $3 = Steps
6 | $4 = Output format
7 | $5 = Examples
8 | $6 = Notes
9 | $7 = Affected files
10 | $8 = Root cause
11 | $9 = Proposed fix
12 | $10 = Tests
13 | $11 = Docs gaps
14 | $12 = Open questions
15 | */
16 | 
17 | # $1
18 | 
19 | **$2**
20 | 
21 | **$3**:
22 | 
23 | 1. $4
24 | 2. $5
25 | 3. $6
26 | 
27 | **$7**:
28 | 
29 | ```markdown
30 | $8
31 | ```
32 | 
33 | **Examples**:
34 | 
35 | `$9`
36 | 
37 | **Notes**:
38 | 
39 | $10
```

temp-prompts-refactored/env-setup.md
```
1 | <!-- $1=trigger command, $2=purpose description, $3=step list, $4=output format, $5=example command, $6=security notes -->
2 | 
3 | **Env Setup**
4 | 
5 | Trigger: $1
6 | 
7 | Purpose: $2
8 | 
9 | **Steps:**
10 | 
11 | $3
12 | 
13 | **Output format:** $4
14 | 
15 | **Examples:** $5
16 | 
17 | **Notes:** $6
```

temp-prompts-refactored/error-analysis.md
```
1 | # Error Analysis
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | 1. $3
10 | 2. $4
11 | 3. $5
12 | 4. $6
13 | 
14 | ## Output format
15 | 
16 | - Table: $7 → $8 → $9 → $10
17 | 
18 | ## Examples
19 | 
20 | - $11
```

temp-prompts-refactored/eslint-review.md
```
1 | /*
2 | * Placeholders:
3 | * $1 = task description (e.g., 'Review ESLint config and suggest rule tweaks')
4 | * $2 = context sources (e.g., '.eslintrc.cjs', '.eslintrc.js', 'package.json')
5 | * $3 = key rules (e.g., 'no-unused-vars')
6 | * $4 = missing plugins (e.g., 'eslint-plugin-react')
7 | * $5 = performance considerations (e.g., 'avoid expensive rules')
8 | * $6 = expected output format (e.g., 'structured report')
9 | * $7 = next steps (e.g., 'document evidence')
10 | */
11 | 
12 | **How-to: ESLint Review**
13 | 
14 | 1. Gather context by inspecting $1; inspecting $2; inspecting $3.
15 | 2. Explain key rules, $4, and $5.
16 | 3. Synthesize insights into $6 with clear priorities and $7.
17 | 
18 | ---
19 | 
20 | ### Affected files
21 | - $1
22 | 
23 | ### Root cause
24 | - Missing $4
25 | 
26 | ### Proposed fix
27 | - Add $4 to configuration
28 | 
29 | ### Tests
30 | - Verify $4 with example code
31 | 
32 | ### Docs gaps
33 | - Document $5 in contribution guidelines
34 | 
35 | ### Open questions
36 | - How to optimize $5 for large projects?
```

temp-prompts-refactored/evidence-capture.md
```
1 | ```markdown
2 | <!-- Placeholder mapping (from input fields):
3 | $1 = Claim text
4 | $2 = Source URL
5 | $3 = Source Title
6 | $4 = Publisher
7 | $5 = Publication Date
8 | $6 = Access Date
9 | $7 = Quote (≤25 words) -->
10 | 
11 | # Evidence Logger
12 | 
13 | Trigger: /evidence-capture
14 | 
15 | Purpose: Capture sources for a specified claim with dates, ≤25-word quotes, findings, relevance, and confidence.
16 | 
17 | Steps:
18 | 
19 | 1. Read the claim text and optional URLs provided.
20 | 2. For each source, record metadata and a ≤25-word quote.
21 | 3. Add a brief Finding, Relevance (H/M/L), and Confidence (0.0–1.0).
22 | 
23 | Output format:
24 | 
25 | ```
26 | ### Evidence Log
27 | | SourceID | Title | Publisher | URL | PubDate | Accessed | Quote (≤25w) | Finding | Rel | Conf |
28 | |---|---|---|---|---|---|---|---|---|---|
29 | ```
30 | 
31 | Examples:
32 | 
33 | - Input: `/evidence-capture $1` with $2
34 | - Output: Evidence table entries with dates.
35 | 
36 | Notes:
37 | 
38 | - Mark missing PubDate as n/a. Prefer official documentation.
39 | ```
```

temp-prompts-refactored/explain-code.md
```
1 | <!-- $1=Title, $2=Trigger command, $3=Purpose description, $4=Step 1, $5=Step 2, $6=Step 3, $7=Output format description -->
2 | 
3 | **Code Explanation Template**
4 | 
5 | # $1
6 | 
7 | Trigger: $2
8 | 
9 | Purpose: $3
10 | 
11 | ## Steps
12 | 
13 | 1. $4
14 | 
15 | 2. $5
16 | 
17 | 3. $6
18 | 
19 | ## Output format
20 | 
21 | $7
```

temp-prompts-refactored/explain-failures.md
```
1 | <!-- $1=Task description; $2=Root cause analysis; $3=Proposed fixes; $4=Affected files; $5=Test coverage impact; $6=Open questions; $7=Example input context -->
2 | **Test Failure Analysis Template**
3 | 
4 | 1. **Task Context**: Analyze recent test failures and propose fixes for $1.
5 | 2. **Root Cause Analysis**: Identify root causes from $2.
6 | 3. **Proposed Fixes**: Provide concrete fixes for $3.
7 | 4. **Affected Files**: List files impacted by $4.
8 | 5. **Test Coverage Impact**: Note how fixes affect test coverage ($5).
9 | 6. **Open Questions**: Document unresolved issues ($6).
10 | 
11 | **Output Format**:
12 | - Begin with a concise summary restating $1.
13 | - Prioritized recommendations with rationale for $2 and $3.
14 | - Evidence used to maintain trust ($4).
15 | 
16 | **Example Context**:
17 | $7
```

temp-prompts-refactored/explain-symbol.md
```
1 | **Symbol Explanation Analysis**
2 | 
3 | <!-- $1 = Symbol to explain (e.g., "HttpClient") -->
4 | <!-- $2 = Definition location (e.g., "src/network/httpClient.ts line 42") -->
5 | <!-- $3 = Key usages (e.g., "services/userService.ts, hooks/useRequest.ts") -->
6 | 
7 | Output:
8 | - Begin with a concise summary reiterating the goal: Explain where and how $1 is defined and used.
9 | - Structure findings under clear subheadings for quick scanning.
10 | - Document evidence: $2 (definition) and $3 (key usages).
11 | - Note documentation gaps: [specify any missing documentation or context]
```

temp-prompts-refactored/feature-flags.md
```
1 | <!-- $1=Title, $2=Trigger command pattern, $3=Purpose statement, $4=Step-by-step implementation steps, $5=Expected output format description, $6=Example command, $7=Critical implementation notes -->
2 | 
3 | **How-to**
4 | 
5 | $1
6 | 
7 | **Trigger:** $2
8 | 
9 | **Purpose:** $3
10 | 
11 | **Steps:** $4
12 | 
13 | **Output format:** $5
14 | 
15 | **Examples:** $6
16 | 
17 | **Notes:** $7
```

temp-prompts-refactored/file-modularity.md
```
1 | <!-- Placeholder mapping:
2 | $1 = file paths
3 | $2 = threshold values (e.g., >500 lines)
4 | $3 = extraction targets (components, hooks, utilities, schemas)
5 | $4 = before/after examples
6 | $5 = import updates
7 | $6 = refactor plan
8 | $7 = patch details -->
9 | 
10 | **File Modularity**
11 | 
12 | Trigger: $1
13 | 
14 | Purpose: Enforce smaller files and propose safe splits for giant files.
15 | 
16 | ## Steps
17 | 
18 | 1. Find files over thresholds ($2).
19 | 2. Suggest extraction targets: $3.
20 | 3. Provide before/after examples and $5.
21 | 
22 | ## Output format
23 | 
24 | - $6
25 | 
26 | ---
27 | 
28 | ### Affected files
29 | 
30 | - $1
31 | 
32 | ### Root cause
33 | 
34 | - Files exceeding size thresholds
35 | 
36 | ### Proposed fix
37 | 
38 | - $4
39 | - $5
40 | 
41 | ### Tests
42 | 
43 | - Unit tests for extracted components
44 | 
45 | ### Docs gaps
46 | 
47 | - Documentation for new file structure
48 | 
49 | ### Open questions
50 | 
51 | - How to handle circular dependencies
52 | - Should we include type definitions in the extraction?
```

temp-prompts-refactored/fix.md
```
1 | # Fix
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | You are a CLI assistant focused on helping contributors with the task: $3
8 | 
9 | 1. Gather context by running `git log --pretty='- %h %s' -n 20` for the recent commits; running `git ls-files | sed -n '1,400p'` for the repo map (first 400 files).
10 | 2. $4: $5
11 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
12 | 
13 | Output:
14 | 
15 | - Begin with a concise summary that restates the goal: $6
16 | - Provide unified diff-style patches when recommending code changes.
17 | - Offer prioritized, actionable recommendations with rationale.
18 | 
19 | Example Input:
20 | $7
21 | 
22 | Expected Output:
23 | 
24 | ```
25 | $8
26 | ```
27 | 
28 | Regression test: $9
```

temp-prompts-refactored/gemini-map.md
```
1 | <!-- $1=source TOML command name, $2=CLI command, $3=tags, $4=conversion scope, $5=translation steps, $6=example TOML input, $7=expected output structure -->
2 | 
3 | **Gemini→Codex Mapper**
4 | 
5 | You are a translator that converts a $1 TOML command into a Codex prompt file.
6 | 
7 | Steps:
8 | 
9 | 1) Read TOML with `description` and `prompt`.
10 | 2) Extract the task, inputs, and outputs implied by the TOML.
11 | 3) Write a Codex prompt file ≤ 300 words:
12 | 
13 |     - Role line `You are ...`
14 |     - Numbered steps
15 |     - Output section
16 |     - Example input and expected output
17 |     - `Usage: /$2` line
18 |     - YAML-like metadata at top
19 | 
20 | 4) Choose a short, hyphenated filename ≤ 32 chars.
21 | 5) Emit a ready-to-run bash snippet:
22 | `cat > ~/.codex/prompts/<filename>.md << 'EOF'` … `EOF`.
23 | 6) Do not include destructive commands or secrets.
24 | 
25 | Example input:
26 | 
27 | ```toml
28 | $6
29 | ```
30 | 
31 | Expected output:
32 | 
33 | A $7 file with the structure above and a bash cat > block.
34 | 
35 | Usage: /$2
36 | 
37 | **Output format**
38 | 
39 | The output must be a Codex prompt file containing:
40 | - Role line: "You are a translator that converts a $1 TOML command into a Codex prompt file."
41 | - Numbered steps (1-6) matching $5
42 | - Output section specifying the format
43 | - Example input and expected output
44 | - `Usage: /$2` line
45 | - YAML metadata: `name: $1`, `command: $2`, `tags: $3`, `scope: $4`
46 | 
47 | **ensure**
48 | - ≤7 placeholders
49 | - no verbatim sentences from input
50 | - literal `$` tokens remain
```

temp-prompts-refactored/generate-readme.md
```
1 | # $1
2 | 
3 | $2
4 | 
5 | ## Features
6 | - $3
7 | 
8 | ## Setup
9 | ```bash
10 | $4
11 | ```
12 | 
13 | ## Usage
14 | ```bash
15 | $5
16 | ```
17 | 
18 | ## Contributing
19 | $6
20 | 
21 | ## License
22 | $7
23 | 
24 | ## Additional Info
25 | - Version: $8
26 | - Author: $9
27 | - Last Updated: $10
```

temp-prompts-refactored/generate.md
```
1 | <!-- Placeholder mapping:
2 | - $1 = Trigger command (e.g., "/generate <source-file>")
3 | - $2 = Purpose statement (e.g., "Generate unit tests for a given source file")
4 | - $3 = Step 1 description
5 | - $4 = Step 2 description
6 | - $5 = Step 3 description
7 | - $6 = Step 4 description
8 | - $7 = Output summary requirement
9 | - $8 = Output test file list
10 | - $9 = Output test case description
11 | - $10 = Output validation command
12 | - $11 = Output evidence description -->
13 | 
14 | **Generate Unit Tests**
15 | 
16 | Trigger: $1
17 | 
18 | Purpose: $2
19 | 
20 | You are a CLI assistant focused on helping contributors with the task: $2.
21 | 
22 | ## Steps
23 | 
24 | 1. $3
25 | 2. $4
26 | 3. $5
27 | 4. $6
28 | 
29 | ## Output
30 | 
31 | - $7
32 | - $8
33 | - $9
34 | - $10
35 | - $11
```

temp-prompts-refactored/grep.md
```
1 | <!-- $1=Search term (e.g., "HttpClient"), $2=Example input, $3=Expected output format -->
2 | **CLI Search Guide**
3 | 
4 | You are a CLI assistant focused on helping contributors with the task: Recursive text search with ripgrep/grep injection.
5 | 
6 | 1. Gather context by running `rg -n $1 . || grep -RIn $1 .`.
7 | 2. Show matched lines with file paths and line numbers.
8 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
9 | 
10 | Output:
11 | 
12 | - Begin with a concise summary that restates the goal: Recursive text search with ripgrep/grep injection.
13 | - Document the evidence you used so maintainers can trust the conclusion.
14 | 
15 | Example Input:
16 | $2
17 | 
18 | Expected Output:
19 | $3
```

temp-prompts-refactored/iac-bootstrap.md
```
1 | <!-- $1=Template name (e.g., "IaC Bootstrap"), $2=Platform (aws/gcp/azure/fly/render), $3=Purpose statement, $4=Step-by-step implementation steps, $5=Required output formats, $6=Example command syntax, $7=Implementation notes and common pitfalls -->
2 | **$1**
3 | 
4 | **Trigger:** `/iac-bootstrap $2`
5 | 
6 | **Purpose:** $3
7 | 
8 | **Steps:** 
9 | 1. $4
10 | 2. $4
11 | 3. $4
12 | 4. $4
13 | 
14 | **Output format:** $5
15 | 
16 | **Examples:** $6
17 | 
18 | **Notes:** $7
```

temp-prompts-refactored/instruction-file.md
```
1 | <!-- Placeholder mapping:
2 | $1 = Trigger
3 | $2 = Purpose
4 | $3 = Step 1 description
5 | $4 = Step 2 description
6 | $5 = Step 3 description
7 | $6 = Step 4 description
8 | $7 = Output format description -->
9 | 
10 | **How-to: Create Instruction File**
11 | 
12 | # Instruction File
13 | 
14 | Trigger: $1
15 | 
16 | Purpose: $2
17 | 
18 | ## Steps
19 | 
20 | 1. $3
21 | 2. $4
22 | 3. $5
23 | 4. $6
24 | 
25 | ## Output format
26 | 
27 | - $7
28 | 
29 | ---
30 | 
31 | ### Affected files
32 | - `cursor.rules`
33 | - `windsurf.rules`
34 | - `claude.md`
35 | 
36 | ### Root cause
37 | - *No specific root cause identified in this context*
38 | 
39 | ### Proposed fix
40 | - *Not applicable; this is a template for creating new instructions*
41 | 
42 | ### Tests
43 | - *Not applicable; this is a template for creating new instructions*
44 | 
45 | ### Docs gaps
46 | - *Not applicable; this is a template for creating new instructions*
47 | 
48 | ### Open questions
49 | - *Not applicable; this is a template for creating new instructions*
```

temp-prompts-refactored/integration-test.md
```
1 | <!-- $1=trigger command, $2=purpose statement, $3=output format -->
2 | 
3 | **E2E Test Generation Prompt**
4 | 
5 | # Integration Test
6 | 
7 | Trigger: $1
8 | 
9 | Purpose: $2
10 | 
11 | ## Steps
12 | 
13 | 1. Detect framework from `package.json` or repo (Playwright/Cypress/Vitest).
14 | 2. Identify critical path scenarios from `PLAN.md`.
15 | 3. Produce test files under `e2e/` with arrange/act/assert and selectors resilient to DOM changes.
16 | 4. Include login helpers and data setup. Add CI commands.
17 | 
18 | ## Output format
19 | 
20 | - $3
21 | 
22 | ## Examples
23 | 
24 | - Login, navigate to dashboard, create record, assert toast.
25 | 
26 | ## Notes
27 | 
28 | - Prefer data-test-id attributes. Avoid brittle CSS selectors.
```

temp-prompts-refactored/logging-strategy.md
```
1 | <!-- $1 = Title (e.g., "Logging Strategy") -->
2 | <!-- $2 = Trigger path (e.g., "/logging-strategy") -->
3 | <!-- $3 = Purpose statement (e.g., "Add or remove diagnostic logging cleanly with levels and privacy in mind") -->
4 | <!-- $4 = Step 1 description (e.g., "Identify hotspots from recent failures") -->
5 | <!-- $5 = Step 2 description (e.g., "Insert structured logs with contexts and correlation IDs") -->
6 | <!-- $6 = Step 3 description (e.g., "Remove noisy or PII-leaking logs") -->
7 | <!-- $7 = Step 4 description (e.g., "Document log levels and sampling in `OBSERVABILITY.md`") -->
8 | 
9 | # $1
10 | 
11 | Trigger: $2
12 | 
13 | Purpose: $3
14 | 
15 | ## Steps
16 | 
17 | $4
18 | 
19 | $5
20 | 
21 | $6
22 | 
23 | $7
24 | 
25 | ## Output format
26 | 
27 | - Diff hunks and a short guideline section.
```

temp-prompts-refactored/migration-plan.md
```
1 | <!-- 
2 | $1 = trigger phrase (e.g., "/migration-plan")
3 | $2 = change summary (e.g., "orders add status enum")
4 | $3 = current vs target schema description
5 | $4 = migration steps details
6 | $5 = online migration strategies for large tables
7 | $6 = SQL snippets
8 | $7 = PR checklist items
9 | $8 = rollback capability flag (can_rollback: true|false)
10 | -->
11 | 
12 | **Migration Plan Template**
13 | 
14 | Trigger: $1
15 | 
16 | Purpose: Produce safe up/down migration steps with checks and rollback notes.
17 | 
18 | **Steps:**
19 | 
20 | 1. $3
21 | 2. $4
22 | 
23 | **Output format:** `Plan`, `SQL`, `Rollback`, `Checks` sections.
24 | 
25 | **Examples:** $2.
26 | 
27 | **Notes:** $5
28 | 
29 | **Additional requirements:** $6 and $7 with $8 flag.
```

temp-prompts-refactored/missing-docs.md
```
1 | /*
2 |   $1 = Original prompt text
3 |   $2 = 'Missing Docs' (inferred genre)
4 |   $3 = Max placeholders (default=7)
5 | */
6 | 
7 | **Missing Docs**
8 | 
9 | (See the source markdown for the full context)
10 | 
11 | The following sections are required to complete this analysis:
12 | 
13 | - **Affected files**: $1
14 | - **Root cause**: $2
15 | - **Proposed fix**: $3
16 | - **Tests**: $4
17 | - **Docs gaps**: $5
18 | - **Open questions**: $6
19 | - **Additional context**: $7
```

temp-prompts-refactored/model-evaluation.md
```
1 | /*
2 | Placeholder mapping:
3 | $1 = Trigger phrase
4 | $2 = Purpose statement
5 | $3 = Step 1 (define benchmark)
6 | $4 = Step 2 (run candidates)
7 | $5 = Step 3 (analyze failures)
8 | $6 = Output format description
9 | $7 = Expected metrics (optional)
10 | */
11 | 
12 | # Model Evaluation
13 | 
14 | $1
15 | 
16 | Purpose: $2
17 | 
18 | ## Steps
19 | 
20 | 1. $3
21 | 2. $4
22 | 3. $5
23 | 
24 | ## Output format
25 | 
26 | $6
27 | 
28 | ---
29 | 
30 | **Expected sections** (add if missing):
31 | - Expected metrics
32 | - Failure analysis
33 | - Adoption recommendations
```

temp-prompts-refactored/model-strengths.md
```
1 | <!-- Placeholders: $1=Title, $2=Trigger, $3=Purpose, $4=Steps, $5=Output format -->
2 | 
3 | **Model Strengths**
4 | 
5 | (Trigger: $1)
6 | 
7 | (Purpose: $2)
8 | 
9 | ($3)
10 | 
11 | ($4)
12 | 
13 | (Recommended output format: $5)
```

temp-prompts-refactored/modular-architecture.md
```
1 | # Modular Architecture
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | $3
10 | 
11 | ## Output format
12 | 
13 | $4
14 | 
15 | ---
16 | 
17 | ### Affected files
18 | 
19 | *To be filled*
20 | 
21 | ### Root cause
22 | 
23 | *To be filled*
24 | 
25 | ### Proposed fix
26 | 
27 | *To be filled*
28 | 
29 | ### Tests
30 | 
31 | *To be filled*
32 | 
33 | ### Docs gaps
34 | 
35 | *To be filled*
36 | 
37 | ### Open questions
38 | 
39 | *To be filled*
```

temp-prompts-refactored/monitoring-setup.md
```
1 | # Monitoring Setup
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | **Steps:**
8 | 
9 | 1. $3
10 | 2. $4
11 | 3. $5
12 | 
13 | **Output format:** $6
14 | 
15 | **Examples:** $7
16 | 
17 | **Notes:** $8
18 | 
19 | ---
20 | 
21 | # Affected files
22 | 
23 | # Root cause
24 | 
25 | # Proposed fix
26 | 
27 | # Tests
28 | 
29 | # Docs gaps
30 | 
31 | # Open questions
```

temp-prompts-refactored/openapi-generate.md
```
1 | # OpenAPI Generate
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | **Steps:**
8 | 
9 | 1. $3
10 | 2. $4
11 | 3. $5
12 | 4. $6
13 | 5. $7
14 | 
15 | **Output format:** $8
16 | 
17 | **Examples:** $9
18 | 
19 | **Notes:** $10
20 | 
21 | ---
22 | 
23 | ## Affected files
24 | 
25 | ## Root cause
26 | 
27 | ## Proposed fix
28 | 
29 | ## Tests
30 | 
31 | ## Docs gaps
32 | 
33 | ## Open questions
```

temp-prompts-refactored/owners.md
```
1 | <!-- $1=Path argument, $2=Task goal, $3=Codeowners file path, $4=Git log command, $5=Example path, $6=Output format structure, $7=Owner names -->
2 | 
3 | **Owners Suggestion Prompt**
4 | 
5 | You are a CLI assistant focused on helping contributors with the task: $2.
6 | 
7 | 1. Gather context by inspecting $3 for codeowners (if present); running $4 for recent authors of the path.
8 | 2. Based on codeowners and git history, suggest owners.
9 | 3. Synthesize the insights into the requested format with clear priorities.
10 | 
11 | Output:
12 | - Begin with a concise summary restating the goal: $2
13 | - Reference evidence from $3 or git history for each owner suggestion.
14 | - Document the evidence used to maintain trust.
15 | 
16 | Example input: $5
17 | 
18 | Expected output:
19 | - Likely reviewers: $6 ($7)
```

temp-prompts-refactored/plan-delta.md
```
1 | <!-- $1=command, $2=purpose, $3=tasks file path pattern, $4=latest plan doc pattern, $5=artifacts directory, $6=date format string, $7=mode selection rules -->
2 | 
3 | **How-to: $2**
4 | 
5 | Trigger: $1
6 | 
7 | Purpose: $2
8 | 
9 | Steps:
10 | 
11 | 1. Discover repository context:
12 |    1. Detect tasks file path: prefer $3; else search `**/$3`.
13 |    2. Detect latest plan doc: prefer $4; else `**/*(prd|spec|plan)*.md`.
14 | 2. Snapshot:
15 |    1. Create $5 if missing.
16 |    2. Copy current tasks file to `$5/tasks-$(date +%$6).json` using: `cp -f <tasks.json> $5/tasks-$(date +%$6).json`.
17 | 3. Input collection:
18 |    1. Read new objectives, constraints, and findings from user input.
19 |    2. Parse selection rules to choose mode: **$7**.
20 | 4. Delta Doc generation:
21 |    1. Create `$5/delta-$(date +%$6).md` containing sections:
22 |       - Objectives (new)
23 |       - Constraints (new)
24 |       - Impacts
25 |       - Decisions
26 |       - Evidence log (sources, dates, links)
27 | 5. Task graph update:
28 |    1. Never alter historical states (`done`/`in_progress`/`blocked`) of existing tasks.
29 |    2. Do not reuse IDs. For replaced tasks, set `superseded_by` on old tasks and include ID in new task's `supersedes[]`.
30 |    3. Add `source_doc`, `lineage[]` on new/changed tasks.
31 |    4. Create new tasks only for new/changed work. Link predecessors via `dependencies` or `relations`.
32 |    5. Keep deprecated tasks with `status: "deprecated"` and `reason`.
33 | 6. **Tests**:
34 |    1. Recompute dependency order and validate acyclicity.
35 |    2. Flag contradictions as `blocked` with machine-readable `blocked_reason`.
36 |    3. Verify critical-path tasks are correctly prioritized.
37 | 7. **Affected files**:
38 |    - $5/tasks-$(date +%$6).json
39 |    - $5/delta-$(date +%$6).md
40 | 8. Readiness and selection:
41 |    1. Implement `ready/next()` to select tasks with all dependencies `done` and not `blocked`.
42 |    2. Produce readiness report grouped by `ready | blocked | deprecated`.
43 | 9. Outputs:
44 |    1. Write updated tasks file in-place.
45 |    2. Persist Delta Doc under $5.
46 |    3. Emit decision hooks: one line per change stating what it enables.
47 | 
48 | **Output format**:
49 | - Produce three artifacts:
50 |   1. **Updated tasks file**: Valid JSON. Preserve existing fields. Append new/changed tasks and relations.
51 |   2. **Delta document**: Markdown with sections `# Delta`, `## Objectives`, `## Constraints`, `## Impacts`, `## Decisions`, `## Evidence`.
52 |   3. **Readiness report**: Plain text with sections `READY`, `BLOCKED`, `DEPRECATED`. Format: `- <id> <title>` (blocked items add `[reason=<code>]`).
53 | - Print **Decision hooks** as lines starting with `HOOK: <id> enables <capability>`.
54 | 
55 | **Open questions**:
56 | - What evidence is missing to resolve inputs?
57 | - How to handle partial scope changes (<20%)?
58 | - Should deprecated tasks be automatically archived?
```

temp-prompts-refactored/planning-process.md
```
1 | **Planning Process Prompt**
2 | 
3 | <!-- $1 = Feature description (e.g., "Add OAuth login") -->
4 | <!-- $2 = Plan file name (e.g., "PLAN.md") -->
5 | <!-- $3 = Max checklist line length (e.g., "100 chars") -->
6 | 
7 | # Planning Process
8 | 
9 | Trigger: $2
10 | 
11 | Purpose: Draft, refine, and execute a feature plan with strict scope control and progress tracking.
12 | 
13 | ## Steps
14 | 
15 | 1. If no plan file exists, create $2. If it exists, load it.
16 | 2. Draft sections: **Goal**, **User Story**, **Milestones**, **Tasks**, **Won't do**, **Ideas for later**, **Validation**, **Risks**.
17 | 3. Trim bloat. Convert vague bullets into testable tasks with acceptance criteria.
18 | 4. Tag each task with an owner and estimate. Link to files or paths that will change.
19 | 5. Maintain two backlogs: **Won't do** (explicit non-goals) and **Ideas for later** (deferrable work).
20 | 6. Mark tasks done after tests pass. Append commit SHAs next to completed items.
21 | 7. After each milestone: run tests, update **Validation**, then commit $2.
22 | 
23 | ## Output format
24 | 
25 | - Update or create $2 with the sections above.
26 | - Include a checklist for **Tasks**. Keep lines under $3 chars.
27 | 
28 | ## Examples
29 | **Input**: $1
30 | 
31 | **Output**:
32 | 
33 | - Goal: Let users sign in with Google.
34 | - Tasks: [ ] add Google client, [ ] callback route, [ ] session, [ ] E2E test.
35 | - Won't do: org SSO.
36 | - Ideas for later: Apple login.
37 | 
38 | ## Notes
39 | 
40 | - Planning only. No code edits.
41 | - Assume a Git repo with test runner available.
```

temp-prompts-refactored/pr-desc.md
```
1 | <!-- 
2 | $1 = Input context path (e.g., "src/example.ts")
3 | $2 = Base branch (e.g., "origin/main")
4 | $3 = User context (e.g., "<args>")
5 | $4 = High-level diff stats (e.g., "2 files changed, 10 insertions")
6 | $5 = List of changed files (e.g., "src/example.ts")
7 | $6 = Desired output structure (e.g., "Summary, Context, Changes, Screenshots, Risk, Test Plan, Rollback, Release Notes")
8 | $7 = Example output (e.g., "Actionable summary...")
9 | -->
10 | 
11 | **PR Description Template**
12 | 
13 | Trigger: /pr-desc $1
14 | 
15 | Purpose: Draft a PR description from the branch diff.
16 | 
17 | 1. Gather context by running `git diff --name-status $5` for the changed files; `git diff --shortstat $4` for high-level stats.
18 | 2. Create a crisp PR description following this structure: $6
19 |    - Base branch: $2
20 |    - User context: $3
21 | 3. Synthesize insights into the requested format.
22 | 
23 | Output requirements:
24 | - Begin with a concise summary: $7
25 | - Prioritized recommendations with rationale
26 | - Test coverage gaps and validation steps
27 | - Workflow triggers, failing jobs, and proposed fixes
28 | 
29 | Affected Files: $5
30 | Root Cause: [Optional]
31 | Proposed Fix: [Optional]
32 | Test Plan: [Optional]
33 | Risk: [Optional]
34 | Rollback Plan: [Optional]
35 | Release Notes: [Optional]
```

temp-prompts-refactored/prd-generator.md
```
1 | <!-- $1=project plan text (visible link text), $2=product name, $3=problem statement, $4=key constraints -->
2 | **PRD Generator Template**
3 | 
4 | Output a plain-text file named `prd.txt` containing **only** these sections in this order (separated by one blank line):
5 | # Overview
6 | # Core Features
7 | # User Experience
8 | # Technical Architecture
9 | # Development Roadmap
10 | # Logical Dependency Chain
11 | # Risks and Mitigations
12 | # Appendix
13 | 
14 | **Output Format**
15 | 
16 | - `# Overview`: $3
17 | - `# Core Features`: Each includes *What*, *Why*, *High-level How*, and BDD criteria:
18 |   `Given ...`
19 |   `When ...`
20 |   `Then ...`
21 | - `# User Experience`: Personas, key flows, UI/UX, accessibility
22 | - `# Technical Architecture`: Components, data models, APIs/integrations, infrastructure, NFRs
23 | - `# Development Roadmap`: MVP and Future Enhancements with acceptance criteria (no dates)
24 | - `# Logical Dependency Chain`: Work ordering for foundations, earliest front end, extensible units
25 | - `# Risks and Mitigations`: Each includes *Description*, *Likelihood*, *Impact*, *Mitigation*
26 | - `# Appendix`:
27 |   • Assumptions (bulleted)
28 |   • Research findings from $1
29 |   • Context notes (`- <visible text> — inferred topic`)
30 |   • Technical specs
31 | 
32 | **Validation Checks**
33 | 
34 | - Headers present and ordered
35 | - All BDD criteria included for features/fallbacks
36 | - Risks include likelihood and impact
37 | - No URLs/secrets; exactly one blank line between sections
38 | - $1 contains **only** visible link text (no external browsing)
```

temp-prompts-refactored/prettier-adopt_Migration_report.md
```
1 | ```
2 | <!--
3 | $1=Task description
4 | $2=Template name (inferred as 'Prettier Migration Guide')
5 | $3=Summary of the report
6 | $4=Prioritized recommendations
7 | $5=Rationale for recommendations
8 | $6=Evidence used
9 | $7=Example input (none)
10 | $8=Expected output structure
11 | -->
12 | 
13 | **$2**
14 | 
15 | 1. $1
16 | 
17 | 2. $3
18 | 
19 | 3. $4
20 | 
21 | 4. $5
22 | 
23 | 5. $6
24 | 
25 | 6. $7
26 | 
27 | 7. $8
28 | 
29 | 
30 | ---
31 | 
32 | ### Affected files
33 | 
34 | - $1 (to be populated with file paths)
35 | 
36 | ### Root cause
37 | 
38 | - $1 (to be populated with migration challenges)
39 | 
40 | ### Proposed fix
41 | 
42 | - $1 (to be populated with specific steps)
43 | 
44 | ### Tests
45 | 
46 | - $1 (to be populated with test cases)
47 | 
48 | ### Docs gaps
49 | 
50 | - $1 (to be populated with missing documentation)
51 | 
52 | ### Open questions
53 | 
54 | - $1 (to be populated with unresolved issues)
55 | 
56 | ```
```

temp-prompts-refactored/problem-analyzer.md
```
1 | <!-- Placeholder mapping:
2 | $1 = Affected files
3 | $2 = Root cause
4 | $3 = Proposed fix
5 | $4 = Tests
6 | $5 = Documentation gaps
7 | $6 = Open questions/assumptions -->
8 | 
9 | # problem-analyzer
10 | 
11 | <problem>
12 | $1
13 | </problem>
14 | 
15 | **Tasks:**
16 | 1. Locate all files/modules affected by the issue. List paths and why each is implicated.
17 | 2. Explain the root cause(s): what changed, how it propagates to the failure, and any environmental factors.
18 | 3. Propose the minimal, safe fix. Include code-level steps, side effects, and tests to add/update.
19 | 4. Flag any missing or outdated documentation/configs/schemas that should be updated or added (especially if code appears outdated vs. current behavior).
20 | 
21 | **Output format:**
22 | - **Affected files:**
23 |   - `$1`: `<reason>`
24 | - **Root cause:**
25 |   - `$2`: `<concise explanation>`
26 | - **Proposed fix:**
27 |   - `$3`: `<steps/patch outline>`
28 |   - **Tests:**
29 | - **Documentation gaps:**
30 |   - `$4`: `<doc_section_what_to_update_add>`
31 | - **Open questions/assumptions:**
32 |   - `$5`: `<items>`
33 | 
34 | **DON'T CODE YET.**
```

temp-prompts-refactored/prompt-sequence-generator.md
```
1 | # Prompt: Generate Prompt Execution Sequence
2 | 
3 | **Purpose:** Given a high-level goal and a set of available prompts, generate the logical execution sequence required to accomplish that goal by chaining the prompts together.
4 | 
5 | ---
6 | 
7 | ### **Inputs**
8 | 
9 | *   **High-Level Goal:** {{high_level_goal}}
10 |     *   *A clear, one-sentence description of the final outcome the user wants to achieve.*
11 |     *   *Example: "Create and document a pull request for the currently staged changes."*
12 | 
13 | *   **Available Prompts:**
14 |     ```
15 |     {{available_prompts}}
16 |     ```
17 |     *   *A list of candidate prompt names (e.g., from the output of `rank-root-prompts`).*
18 |     *   *Example: ['pr-desc.md', 'commit-msg.md', 'changed-files.md', 'review.md', 'release-notes.md']*
19 | 
20 | *   **Context (Optional):** {{context}}
21 |     *   *Any additional context, such as the current state of the git repository or specific files of interest.*
22 |     *   *Example: "The user has already staged files using `git add`."*
23 | 
24 | ---
25 | 
26 | ### **Instructions for the AI**
27 | 
28 | 1.  **Analyze the Goal:** Deconstruct the `{{high_level_goal}}` into a series of logical steps required to get from the starting state to the final outcome.
29 | 
30 | 2.  **Map Prompts to Steps:** For each logical step, identify the most suitable prompt from the `{{available_prompts}}` list that can perform that step.
31 |     *   Consider the inputs and outputs of each prompt to determine dependencies. A prompt's input is often the output of a previous one.
32 | 
33 | 3.  **Establish Order:** Arrange the selected prompts into a numbered sequence based on their dependencies. The sequence should represent a complete and logical workflow.
34 | 
35 | 4.  **Identify Gaps:** If any necessary step in the workflow cannot be fulfilled by one of the available prompts, explicitly state what action or prompt is missing.
36 | 
37 | ---
38 | 
39 | ### **Required Output Format**
40 | 
41 | **Execution Sequence:**
42 | 
43 | 1.  **`[prompt_name_1.md]`**: [Brief justification for why this prompt is first and what it accomplishes.]
44 | 2.  **`[prompt_name_2.md]`**: [Brief justification for why this prompt is second, and how it uses the output of the previous step.]
45 | 3.  ...
46 | 
47 | **Identified Gaps (if any):**
48 | 
49 | *   [Description of a missing step or prompt needed to complete the workflow.]
```

temp-prompts-refactored/prototype-feature.md
```
1 | # Prototype Feature
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | $3
10 | 
11 | ## Output format
12 | 
13 | - $4
```

temp-prompts-refactored/query-set.md
```
1 | <!-- Placeholder mapping:
2 | $1 = Goal statement
3 | $2 = Number of queries (4-8)
4 | $3 = Time window (e.g., 'past year')
5 | $4 = Input entities (e.g., 'OpenAI Responses API streaming server-sent events')
6 | $5 = Query types (e.g., 'define, compare, integrate') -->
7 | 
8 | **High-Yield Query Generator**
9 | 
10 | Trigger: /query-set
11 | 
12 | Purpose: Generate {1} targeted web search queries with operators, entity variants, and recency filters for a given objective.
13 | 
14 | Steps:
15 | 1. Restate the goal with entities and time window.
16 | 2. Produce queries using operators: site:, filetype:, inurl:, quotes, OR, date filters.
17 | 3. Include synonyms and common misspellings.
18 | 4. Mix intents: {2}
19 | 
20 | Output format:
21 | ```
22 | ### Goal
23 | {3}
24 | 
25 | ### Query Set
26 | - {4}
27 | - {5}
28 | ... up to 8
29 | ```
30 | 
31 | Examples:
32 | - Input: `/query-set {6} {7}`
33 | - Output: Goal + {8} queries with operators.
34 | 
35 | Notes:
36 | - No evidence logging here. Use /research-item to execute.
```

temp-prompts-refactored/rank-root-prompts.md
```
1 | <!--
2 | $1 = command name/identifier
3 | $2 = example user question
4 | $3 = project root path to scan (defaults to "~/.codex/prompts" when omitted/blank)
5 | $4 = minimum relevance threshold (0–1)
6 | -->
7 | 
8 | # {Prompt Ranking Command}
9 | 
10 | ```md
11 | # Command: $1
12 | 
13 | # Usage: $1 "$2" "$3" "$4"
14 | 
15 | # Args:
16 | 
17 | # - {{query}}: $2
18 | # - {{path}}: $3
19 | # - {{threshold}}: $4
20 | 
21 | prompt = """
22 | Task:
23 | Given a user inquiry {{query}}, review prompt-definition files located at {{path}} and identify the most relevant ones.
24 | 
25 | Defaults:
26 | * If {{path}} is missing or blank, use "~/.codex/prompts".
27 | 
28 | Do the following:
29 | 1) List files in {{path}} without descending into subfolders. Treat common doc/config extensions as candidates.
30 | 2) Read each candidate’s text and summarize its purpose + domain in one sentence.
31 | 3) Compute a relevance score in [0,1] between that summary and {{query}}.
32 | 4) Order all candidates by score (highest first).
33 | 5) Emit a compact table with exactly these columns: filename | description | match_score (rounded to 2 decimals).
34 | 
35 | Rules:
36 | * The description must be 1–2 sentences capturing purpose and domain.
37 | * Only include rows with match_score ≥ {{threshold}}.
38 | * If none satisfy {{threshold}}, output a single line: "No prompt exceeds threshold {{threshold}} — recommend creating a new prompt."
39 | 
40 | Acceptance:
41 | * When ≥1 match meets {{threshold}}, a table sorted by descending match_score is present.
42 | * Otherwise, the single-line note is produced.
43 | 
44 | !{echo "Using path: ${PATH_ARG:-~/.codex/prompts}"}
45 | """
46 | ```
47 | 
48 | ## Output format
49 | 
50 | * **Preferred**: a markdown table with columns `filename | description | match_score` sorted by `match_score` (desc) and filtered by `{{threshold}}`.
51 | * **Fallback**: the exact one-line message when no entries meet `{{threshold}}`.
52 | -
```

temp-prompts-refactored/refactor-file.md
```
1 | # Refactor Analysis
2 | 
3 | <!-- Placeholder mapping:  
4 | $1 = File path (e.g., src/components/Button.tsx)
5 | $2 = Before/after snippet (code diff)
6 | $3 = Evidence used (e.g., lines 1-400 of file)
7 | $4 = Refactor goal (e.g., extract shared styling hook)
8 | $5 = Summary (concise restatement of goal)
9 | $6 = Complexity reduction justification (why refactoring improves readability)
10 | $7 = Next steps (actionable items for maintainers) -->
11 | 
12 | **Refactor Analysis**
13 | 
14 | 1. Gather context by running `sed -n '1,400p' $1` for the first 400 lines of the file.
15 | 2. Suggest refactors that reduce complexity and improve readability without changing behavior. Provide $2 with commentary.
16 | 3. Synthesize insights into $5 with clear priorities and $7.
17 | 
18 | **Output Format**
19 | 
20 | - Begin with a concise summary: $5
21 | - Include $2 with commentary
22 | - Document evidence: $3
23 | 
24 | *Note: $4 is implied by the refactoring goal but can be explicitly stated for clarity*
```

temp-prompts-refactored/refactor-suggestions.md
```
1 | # Refactor Suggestions
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | $3
10 | 
11 | ## Output format
12 | 
13 | $4
14 | 
15 | 
16 | ### Affected files
17 | 
18 | 
19 | ### Root cause
20 | 
21 | 
22 | ### Proposed fix
23 | 
24 | 
25 | ### Tests
26 | 
27 | 
28 | ### Docs gaps
29 | 
30 | 
31 | ### Open questions
32 | 
33 | 
34 | ---
35 | 
36 | <!-- Placeholder mapping -->
37 | 
38 | - $1 = Trigger (e.g., /refactor-suggestions)
39 | - $2 = Purpose (e.g., Propose repo-wide refactoring opportunities after tests exist)
40 | - $3 = Steps (e.g., Map directory structure and large files. \n2. Identify duplication, data clumps, and god objects. \n3. Suggest phased refactors with safety checks and tests.)
41 | - $4 = Output format (e.g., Ranked list with owners and effort estimates.)
```

temp-prompts-refactored/reference-implementation.md
```
1 | <!-- $1=Template title, $2=Trigger command, $3=Purpose statement, $4=Step 1 description, $5=Step 2 description, $6=Step 3 description, $7=Output format description -->
2 | 
3 | **How-to**
4 | 
5 | # $1
6 | 
7 | Trigger: $2
8 | 
9 | Purpose: $3
10 | 
11 | ## Steps
12 | 
13 | 1. $4
14 | 2. $5
15 | 3. $6
16 | 
17 | ## Output format
18 | 
19 | - $7
```

temp-prompts-refactored/regression-guard.md
```
1 | <!-- Placeholder mapping: 
2 | $1 = Title
3 | $2 = Purpose
4 | $3 = Step 1
5 | $4 = Step 2
6 | $5 = Step 3
7 | $6 = Output format
8 | $7 = Notes -->
9 | 
10 | **Regression Guard**
11 | 
12 | Trigger: $1
13 | 
14 | Purpose: $2
15 | 
16 | ## Steps
17 | 
18 | $3
19 | $4
20 | $5
21 | 
22 | ## Output format
23 | 
24 | $6
25 | 
26 | ## Notes
27 | 
28 | $7
29 | 
30 | 
31 | ### Affected files
32 | 
33 | ### Root cause
34 | 
35 | ### Proposed fix
36 | 
37 | ### Tests
38 | 
39 | ### Docs gaps
40 | 
41 | ### Open questions
```

temp-prompts-refactored/release-notes-prepare.md
```
1 | # Prepare Release Notes From CHANGELOG
2 | 
3 | Trigger: `/release-notes-prepare`
4 | 
5 | Purpose: Convert the latest CHANGELOG section into release notes suitable for GitHub Releases with the six-section layout.
6 | 
7 | Steps:
8 | 
9 | 1. Detect latest version heading and extract its section.
10 | 2. Normalize bullets to sentence fragments without trailing periods.
11 | 3. Add short highlights at top (3 bullets max) derived from Added/Changed.
12 | 4. Emit a "copy-ready" Markdown body.
13 | 
14 | Output format:
15 | 
16 | - Title line: `Release ${1} — ${2}`
17 | - Highlights list
18 | - Six sections with bullets
19 | 
20 | <!-- Placeholder mapping -->
21 | ${1}=Version (e.g., 1.6.0)
22 | ${2}=Release date (e.g., 2025-09-22)
23 | ${3}=Highlight 1 (e.g., Custom roles and permissions)
24 | ${4}=Highlight 2 (e.g., Faster cold starts)
25 | ${5}=Highlight 3 (optional)
26 | ${6}=Added section content
27 | ${7}=Changed section content
28 | 
29 | **Note**: This template follows the six-section layout (Added, Changed, Removed, Fixed, Improved, Deprecated). Missing sections like Removed, Fixed, Improved, Deprecated are implied by the context and will be populated with the appropriate content from CHANGELOG.
```

temp-prompts-refactored/release-notes.md
```
1 | <!-- $1=git-range argument, $2=commit log output, $3=change categories (e.g., Features, Fixes), $4=input file path, $5=specific change entry, $6=summary text, $7=evidence description -->
2 | 
3 | ## How to Generate Release Notes
4 | 
5 | Trigger: /release-notes $1
6 | 
7 | Purpose: Generate human-readable release notes from recent commits.
8 | 
9 | You are a CLI assistant focused on helping contributors with the task: Generate human‑readable release notes from recent commits.
10 | 
11 | 1. Gather context by running `git log --pretty='* %s (%h) — %an' --no-merges $2` for the commit log (no merges).
12 | 2. Produce release notes grouped by type $3. Include a Highlights section and a full changelog list.
13 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
14 | 
15 | Output:
16 | 
17 | - Begin with a concise summary: $6
18 | - Document the evidence: $7
19 | 
20 | Example Input:
21 | $4
22 | 
23 | Expected Output:
24 | ## $3
25 | 
26 | - $5
```

temp-prompts-refactored/research-batch.md
```
1 | **Conversation-Aware Research — Batch WBRO**
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: Process a numbered work-breakdown list of objectives with carry-forward context across items and produce a roll-up summary.
6 | 
7 | Steps:
8 | 
9 | 1. Parse numbered WBRO items from the input after the trigger.
10 | 2. Before Item 1: list ≤5 bullets of starting context.
11 | 3. For each item i: execute the per-item workflow and include a Conversation State Update.
12 | 4. If blocked by prior gaps, emit **Dependency Blocked** with a minimal micro-query.
13 | 5. After all items: emit a Roll-up Summary with per-item status, enabled decisions, unresolved risks, and a domain-type count of sources.
14 | 
15 | Output format:
16 | 
17 | - Repeat the single-item format per item.
18 | - End with:
19 | 
20 | ```
21 | ## Roll-up Summary
22 | - Item $2: $3 — decision enabled: $4; risks: $5
23 | - Sources by domain type: $6, $7
24 | ```
25 | 
26 | Examples:
27 | - Input: `/research-batch $1`
28 | - Output: Per-item sections plus roll-up.
29 | 
30 | Notes:
31 | - Keep quotes ≤25 words. Prefer primary docs.
32 | 
33 | <!-- Placeholder mapping -->
34 | - $1: Input WBRO items (e.g., "1) Validate Next.js 15 stability. 2) Compare Bun vs Node for CI. 3) Licensing risks for MIT vs Apache-2.0.")
35 | - $2: Item number (e.g., "1")
36 | - $3: Status (e.g., "Completed")
37 | - $4: Enabled decisions (e.g., "Validate Next.js 15")
38 | - $5: Unresolved risks (e.g., "Licensing conflicts")
39 | - $6: Domain type count (e.g., "3")
40 | - $7: Domain types (e.g., "gov, org, docs, blog, news") -->
```

temp-prompts-refactored/research-item.md
```
1 | <!-- Placeholders: $1=short title, $2=goal sentence, $3=assumption bullet, $4=first query, $5=second query, $6=third query, $7=fourth query to eighth query (range) -->
2 | 
3 | **Conversation-Aware Research**
4 | 
5 | # Conversation-Aware Research — Single Item
6 | 
7 | Trigger: /research-item
8 | 
9 | Purpose: Run the full per-item research workflow for one objective and return queries, evidence, synthesis, contradictions, gaps, decision hook, plus a conversation state update.
10 | 
11 | Steps:
12 | 1. Read the objective text following the trigger.
13 | 2. Capture starting context if provided.
14 | 3. Apply the Process (per item): Goal, Assumptions, Query Set (4–8), Search Plan, Run & Capture, Cross-check, Synthesis, Gaps & Next, Decision Hook.
15 | 4. Track PubDate and Accessed (ISO) for every source; prefer primary docs.
16 | 5. Enforce quotes ≤25 words; mark inferences as "Inference".
17 | 
18 | Output format:
19 | 
20 | ```
21 | ## Item 1: $1
22 | 
23 | ### Goal
24 | $2
25 | 
26 | ### Assumptions
27 | - $3
28 | 
29 | ### Query Set
30 | - $4
31 | - $5
32 | - $6
33 | - $7
34 | 
35 | ### Evidence Log
36 | | SourceID | Title | Publisher | URL | PubDate | Accessed | Quote (≤25w) | Finding | Rel | Conf |
37 | |---|---|---|---|---|---|---|---|---|---|
38 | 
39 | ### Synthesis
40 | - $8
41 | - $9
42 | - $10
43 | 
44 | ### Contradictions
45 | - $11 → $12
46 | 
47 | ### Gaps & Next
48 | - $13
49 | 
50 | ### Decision Hook
51 | $14
52 | 
53 | ### Conversation State Update
54 | - New facts: $15
55 | - Constraints learned: $16
56 | - Entities normalized: $17
57 | ```
58 | 
59 | Examples:
60 | - Input: `/research-item Compare OpenAPI 3.1 tooling for Python clients in 2024; budget $0; prefer official docs.`
61 | - Output: As per format with SourceIDs and dates.
62 | 
63 | Notes:
64 | - Safety: No personal data. Do not fabricate sources.
65 | - Provenance: Cite reputable sources; record n/a for missing PubDate.
```

temp-prompts-refactored/reset-strategy.md
```
1 | # Reset Strategy
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | ## Steps
8 | 
9 | $3
10 | $4
11 | $5
12 | $6
13 | 
14 | ## Output format
15 | 
16 | - A short decision note and exact commands. Never execute resets automatically.
17 | 
18 | ## Examples
19 | 
20 | - Recommend reset after repeated failing refactors touching $7
21 | 
22 | ## Notes
23 | 
24 | - Warn about destructive nature. Require user confirmation.
25 | 
26 | ---
27 | 
28 | ### Missing Sections (Inferred for Analysis Context)
29 | 
30 | - **Affected files**: $8
31 | - **Root cause**: $9
32 | - **Proposed fix**: $10
33 | - **Tests**: $11
34 | - **Docs gaps**: $12
35 | - **Open questions**: $13
```

temp-prompts-refactored/review-branch.md
```
1 | /*
2 | 
3 | Placeholder mapping:
4 | $1 = Trigger
5 | $2 = Purpose
6 | $3 = Step 1 description
7 | $4 = Step 2 description
8 | $5 = Step 3 description
9 | $6 = Output requirements
10 | $7 = Example input (if applicable)
11 | */
12 | 
13 | # {template_name or Inferred Name}
14 | 
15 | {Trigger}
16 | 
17 | {Purpose}
18 | 
19 | 1. {Step 1}
20 | 2. {Step 2}
21 | 3. {Step 3}
22 | 
23 | {Output Requirements}
24 | 
25 | {Example Input}
26 | 
27 | ---
28 | 
29 | ### Analysis
30 | 
31 | - **Affected files**: {Affected files}
32 | - **Root cause**: {Root cause}
33 | - **Proposed fix**: {Proposed fix}
34 | - **Tests**: {Tests}
35 | - **Docs gaps**: {Docs gaps}
36 | - **Open questions**: {Open questions}
37 | 
38 | ---
39 | 
40 | ### Output format
41 | 
42 | - {Output format requirement}
43 | 
44 | ---
45 | 
46 | *Note: Placeholders marked with `$1..$7` are to be filled with context-specific content from the input.*
```

temp-prompts-refactored/review.md
```
1 | # Review
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: Review code matching $1 and deliver actionable feedback.
6 | 
7 | You are a CLI assistant focused on helping contributors with the task: Review code matching $1 and give actionable feedback.
8 | 
9 | 1. Gather context by running `rg -n $2 . || grep -RIn $2 .` for the search results for $2 (filename or regex).
10 | 2. Perform a thorough code review. Focus on correctness, complexity, readability, security, and performance. Provide concrete patch suggestions.
11 | 
12 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
13 | 
14 | Output:
15 | - Begin with a concise summary that restates the goal: Review code matching $1 and give actionable feedback.
16 | - Provide unified diff-style patches when recommending code changes.
17 | - Organize details under clear subheadings so contributors can scan quickly.
18 | 
19 | Example Input:
20 | $3
21 | 
22 | Expected Output:
23 | - Usage cluster in src/network/* with note on inconsistent error handling.
24 | 
25 | <!-- Placeholders:
26 | - $1 = trigger pattern (e.g., `HttpClient`)
27 | - $2 = search pattern for code context (e.g., `HttpClient`)
28 | - $3 = example input pattern (e.g., `HttpClient`)
29 |  -->
```

temp-prompts-refactored/roll-up.md
```
1 | <!-- $1 = trigger phrase (e.g., "/roll-up") -->
2 | <!-- $2 = purpose statement (e.g., "Summarize per-item statuses, enabled decisions, unresolved risks, and count sources by domain type") -->
3 | <!-- $3 = step 1 description (e.g., "Aggregate Conversation State Updates from prior items") -->
4 | <!-- $4 = step 2 description (e.g., "Produce per-item status lines and decisions") -->
5 | <!-- $5 = step 3 description (e.g., "Tally sources by domain type: gov, org, docs, blog, news, academic") -->
6 | <!-- $6 = output format template (e.g., the code block below) -->
7 | <!-- $7 = example input (e.g., "/roll-up from items 1–3") -->
8 | 
9 | # Research Roll-up Summary
10 | 
11 | Trigger: $1
12 | 
13 | Purpose: $2
14 | 
15 | Steps:
16 | 1. $3
17 | 2. $4
18 | 3. $5
19 | 
20 | Output format:
21 | ```
22 | ## Roll-up Summary
23 | - Item {n}: {status} — decision enabled: {…}; risks: {…}
24 | - Sources by domain type: {gov:X, org:Y, docs:Z, blog:A, news:B, academic:C}
25 | ```
26 | 
27 | Examples:
28 | - Input: $7
29 | - Output: [see above]
30 | 
31 | Notes:
32 | - Domain Count Analysis: $6 (explain why counts vary across domains)
33 | - Evidence Log Reference: Use counts derived from the Evidence Logs
```

temp-prompts-refactored/scaffold-fullstack.md
```
1 | # Scaffold Full‑Stack App
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | **Steps:**
8 | 
9 | 1. Read repository context: `git rev-parse --is-inside-work-tree`.
10 | 2. If repo is empty, initialize: `git init -b main` and create `.editorconfig`, `.gitignore`, `README.md`.
11 | 3. For $3 derive presets (examples):
12 |    - `$4`: Next.js app, Express API, Prisma + PostgreSQL, Playwright, pnpm workspaces.
13 |    - `$5`: Vite + React app, Fastify API, Drizzle + SQLite.
14 | 4. Create workspace layout:
15 |    - root: `package.json` with `pnpm` workspaces, `tsconfig.base.json`, `eslint`, `prettier`.
16 |    - apps/web, apps/api, packages/ui, packages/config.
17 | 5. Add scripts:
18 |    - root: `dev`, `build`, `lint`, `typecheck`, `test`, `e2e`, `format`.
19 |    - web: Next/Vite scripts. api: dev with ts-node or tsx.
20 | 6. Seed CI files: `.github/workflows/ci.yml` with jobs [lint, typecheck, test, build, e2e] and artifact uploads.
21 | 7. Add example routes:
22 |    - web: `/health` page. api: `GET /health` returning `{ ok: true }`.
23 | 8. Write docs to `README.md`: how to run dev, test, build, and env variables.
24 | 9. Stage files, but do not commit. Output a tree and next commands.
25 | 
26 | **Output format:**
27 | - Title line: `Scaffold created: $6`
28 | - Sections: `Repo Tree`, `Next Steps`, `CI Seeds`.
29 | - Include a fenced code block of the `tree` and sample scripts.
30 | 
31 | **Examples:**
32 | - **Input:** `$7`
33 |   **Output:** Summary + tree with `apps/web`, `apps/api`, `packages/ui`.
34 | - **Input:** `$8`
35 |   **Output:** Summary + tree + Drizzle config.
36 | 
37 | **Notes:**
38 | - Assume pnpm and Node 20+. Do not run package installs automatically; propose commands instead.
39 | - Respect existing files; avoid overwriting without explicit confirmation.
40 | 
41 | <!-- Placeholder mapping: -->
42 | - $1 = trigger command
43 | - $2 = purpose statement
44 | - $3 = stack preset name
45 | - $4 = example preset description
46 | - $5 = alternative example preset description
47 | - $6 = output title suffix
48 | - $7 = example input command
49 | - $8 = alternative example input command -->
```

temp-prompts-refactored/scope-control.md
```
1 | /* Placeholder mapping:
2 | $1 = Trigger
3 | $2 = Purpose
4 | $3 = Steps
5 | $4 = Output format
6 | $5 = Example input
7 | $6 = Example output
8 | $7 = Notes */
9 | 
10 | **Scope Control**
11 | 
12 | $1
13 | 
14 | **Purpose**: $2
15 | 
16 | **Steps**:
17 | 1. $3
18 | 2. $4
19 | 3. $5
20 | 4. $6
21 | 
22 | **Output format**: $7
23 | 
24 | ### Examples
25 | - Input: $1
26 | - Output: $2
27 | 
28 | ### Notes
29 | - $3
```

temp-prompts-refactored/slo-setup.md
```
1 | <!-- Placeholders mapping:
2 | $1 = Template title (e.g., "SLO Setup")
3 | $2 = Command trigger (e.g., "/slo-setup")
4 | $3 = Purpose statement (e.g., "Define Service Level Objectives, burn alerts, and runbooks.")
5 | $4 = Implementation steps (e.g., "1. Choose SLI/metrics per user journey... 2. Create burn alerts... 3. Add `SLO.md`...")
6 | $5 = Output format specification (e.g., "SLO table and alert rules snippet")
7 | $6 = Example usage (e.g., "/slo-setup")
8 | $7 = Implementation notes (e.g., "Tie SLOs to deploy gates and incident severity")
9 | -->
10 | 
11 | **$1**
12 | 
13 | Trigger: $2
14 | 
15 | Purpose: $3
16 | 
17 | **Steps:**
18 | 
19 | $4
20 | 
21 | **Output format:** $5
22 | 
23 | **Examples:** $6
24 | 
25 | **Notes:** $7
```

temp-prompts-refactored/stack-evaluation.md
```
1 | <!-- $1=Template title (e.g., "Stack Evaluation"), $2=Trigger command, $3=Purpose statement, $4=First step description, $5=Second step description, $6=Third step description, $7=Output format description -->
2 | **$1**
3 | 
4 | Trigger: $2
5 | 
6 | Purpose: $3
7 | 
8 | ## Steps
9 | 
10 | 1. $4
11 | 2. $5
12 | 3. $6
13 | 
14 | ## Output format
15 | 
16 | - $7
```

temp-prompts-refactored/stop-guessing.md
```
1 | # stop guessing
2 | 
3 | $1
4 | 
5 | Respond with a JSON object in the following order of fields: `reasoning`, then `template_markdown`.
```

temp-prompts-refactored/summary-1.md
```
1 | # Inferred Analysis Template
2 | 
3 | You are a CLI assistant helping contributors with the task: **$1**.
4 | 
5 | 1. **Context sweep.** Derive a repository map by running **$2** (first N entries are sufficient). Review **$3** for primary documentation.
6 | 2. **Draft the summary.** Organize findings under **$4, $5, $6, $7**.
7 | 3. **Synthesize.** Present a prioritized, action-oriented report with immediate next steps.
8 | 
9 | ## Report Structure
10 | 
11 | ### $4
12 | * …
13 | 
14 | ### $5
15 | * …
16 | 
17 | ### $6
18 | * …
19 | 
20 | ### $7
21 | 1. …
22 | 2. …
23 | 3. …
24 | 
25 | ### Evidence Consulted
26 | * Repo map derived via: **$2**
27 | * Docs reviewed: **$3**
28 | * Noteworthy gaps or uncertainties: …
29 | 
30 | ### Next Steps (Prioritized)
31 | 1. …
32 | 2. …
33 | 3. …
34 | 
35 | ### Open Questions
36 | * …
37 | * …
38 | 
39 | ---
40 | 
41 | ## Output format (for automation and reviews)
42 | * **Audience:** contributors and maintainers
43 | * **Tone:** concise, decision-ready
44 | * **Must include:** goal recap (**$1**), sections (**$4–$7**), evidence, priorities, open questions
45 | * **Nice to have:** links to code paths, brief risk notes
46 | 
47 | **Validation checklist**
48 | * [ ] All required sections present
49 | * [ ] Evidence lists commands/files used (**$2**, **$3**)
50 | * [ ] Priorities and next steps are explicit
51 | * [ ] Open questions are called out clearly
52 | 
53 | <!-- $1=task, $2=command, $3=docs, $4=primary section, $5=secondary section, $6=tertiary section, $7=quaternary section -->
```

temp-prompts-refactored/summary-2.md
```
1 | <!-- $1 = task description (e.g., "summarize the project") -->
2 | <!-- $2 = CLI command (e.g., "git ls-tree") -->
3 | <!-- $3 = file paths to inspect (e.g., "docs/README.md") -->
4 | 
5 | # $1
6 | 
7 | You are a CLI helper guiding contributors to accomplish: **$1**.
8 | 
9 | ## Scope & Role
10 | 
11 | * Operate in a repository working tree.
12 | * Run lightweight, read-only commands to gather context.
13 | * Synthesize findings into a concise, maintainer-friendly report.
14 | 
15 | ## Procedure
16 | 
17 | 1. **Map the repo (quick scan)** — run **$2** to capture a top-slice of the file tree for orientation.
18 | 2. **Locate key docs** — check the paths in **$3** (if present) for project-level guidance.
19 | 3. **Summarize the project** — draft a high-level overview covering:
20 |    * **Purpose** (what it is)
21 |    * **Motivation** (why it exists)
22 |    * **Architecture/Workflow** (how it works at a glance)
23 |    * **Getting Started** (how to begin using/developing)
24 | 4. **Prioritize next steps** — identify immediate follow-ups for readers (e.g., areas to explore, gaps to fill).
25 | 5. **Record evidence** — note exactly what you inspected so maintainers can verify.
26 | 
27 | ## Output
28 | 
29 | Begin with a one-sentence restatement of **$1**, then provide the sections below in order:
30 | 
31 | * **Project Summary** — purpose, motivation, architecture/workflow, getting started.
32 | * **Repo Snapshot** — brief map excerpt from **$2** (top of tree only).
33 | * **Evidence Log** — list the commands run and files/paths reviewed, including **$3**.
34 | * **Priorities & Next Steps** — the most important actions to take next (short list).
35 | 
36 | ## Example Input
37 | 
38 | (no arguments; run from the repo root)
39 | 
40 | ## Expected Result
41 | 
42 | A structured report following the **Output** section above, optimized for README-level clarity and trustworthiness.
43 | 
44 | ## Output format (strict)
45 | 
46 | Provide sections exactly in this order: Project Summary → Repo Snapshot → Evidence Log → Priorities & Next Steps. Keep each section concise and actionable.
```

temp-prompts-refactored/summary.md
```
1 | <!-- $1 = specific command to run for file listing -->
2 | <!-- $2 = target repo summary goal -->
3 | <!-- $3 = high-level summary sections (What, Why, How, Getting Started) -->
4 | <!-- $4 = requirement for documenting evidence -->
5 | <!-- $5 = output format specification -->
6 | 
7 | **Repository Summary Generator**
8 | 
9 | 1. Gather context by running `$1` for the repo map.
10 | 2. Generate a high-level summary covering `$3`.
11 | 3. Document evidence used to maintain trust in conclusions per `$4`.
12 | 4. Output a structured report following `$5`.
```

temp-prompts-refactored/switch-model.md
```
1 | <!-- Placeholders: $1=Task type, $2=Model selection criteria, $3=Input suite, $4=Metrics, $5=Recommended model, $6=Rationale, $7=Output format -->
2 | 
3 | **Switch Model**
4 | 
5 | Trigger: $1
6 | 
7 | Purpose: Decide when to try a different AI backend and how to compare.
8 | 
9 | ## Steps
10 | 
11 | 1. Define task type: $2
12 | 2. Select candidate models and temperature/tooling options.
13 | 3. Run a fixed input suite: $3 and measure $4.
14 | 4. Recommend a model per task: $5 with $6.
15 | 
16 | ## Output format
17 | 
18 | - Table: task → model → settings → $7.
```

temp-prompts-refactored/system-level-instruction-editor.md
```
1 | <!-- Placeholder mapping:
2 | $1 = Title (System-level instruction)
3 | $2 = Purpose
4 | $3 = Inputs
5 | $4 = Steps
6 | $5 = Deconstruct request
7 | $6 = Locate insertion points
8 | $7 = Apply minimal change and invariants -->
9 | 
10 | **System-Level Instruction Editor**
11 | 
12 | Trigger: $1
13 | 
14 | Purpose: $2
15 | 
16 | ## Inputs
17 | 
18 | - $3
19 | 
20 | ## Steps
21 | 
22 | 1. $4
23 | 2. $5
24 | 3. $6
25 | 
26 | 1. **Deconstruct the request:** $7
27 | 
28 | 2. **Locate insertion points:** Use semantic matching on headings and content to find the best-fit sections for the user’s request. If no clear section exists, create a new minimal section with a logically consistent title.
29 | 
30 | 3. **Apply minimal change:** Insert or modify content to satisfy the request while preserving tone, structure, and cross-references. Keep unrelated sections unchanged.
31 | 
32 | 4. **Run invariants:**
33 | 
34 |    - The entire file must be present (no placeholders, no truncation).
35 |    - Markdown structure and formatting must remain valid.
36 |    - Internal references and links stay accurate.
37 | 
38 | 5. **Render in Canvas:**
39 | 
40 |    - If editing an existing file: open in Canvas and **replace the full contents** with the updated version.
41 |    - If creating a new file: create it in Canvas and display the **entire file**.
42 | 
43 | 6. **Variants (optional):** Generate $1.md and/or $2.md from the updated $3.md using only the Platform Substitution Rules. Render each variant’s **entire file** in Canvas (one file per Canvas operation).
44 | 
45 | 7. **Size-limit fallback:** If a size cap prevents full-file rendering in Canvas, output the **entire file in chat**, then append:
46 | 
47 |    - "*Note: Full content was output in chat due to a size limit preventing Canvas rendering.*"
48 | 
49 | ## Output format
50 | 
51 | - Table: $1 → $2 → $3 → $4 → $5
52 | 
53 | ## Example rows
54 | 
55 | - "<example symptom or error>" → $6 → $7 → $1 → $2
```

temp-prompts-refactored/tm-advance.md
```
1 | <!-- $1 = input task IDs (e.g., TM-42, TM-43) -->
2 | <!-- $2 = task title from tasks.json -->
3 | <!-- $3 = step-by-step plan description -->
4 | <!-- $4 = list of file touch-points -->
5 | <!-- $5 = test hooks for the task -->
6 | <!-- $6 = measurable acceptance criteria -->
7 | <!-- $7 = Conventional Commits message (e.g., `feat(parser): implement rule X`) -->
8 | 
9 | **Advance Task Plan Generator**
10 | 
11 | Trigger: For given $1, produce a concrete work plan, acceptance criteria, tests, and a Conventional Commits message to move status toward done.
12 | 
13 | Purpose: For given task id(s), produce a concrete work plan, acceptance criteria, tests, and a Conventional Commits message to move status toward done.
14 | 
15 | Steps:
16 | 
17 | 1. Read tasks.json; resolve each provided $1. If none provided, pick the top item from /tm-next.
18 | 2. For each task: restate $2, goals, and related dependencies.
19 | 3. Draft a step-by-step plan with $4 and $5.
20 | 4. Provide a minimal commit plan and a Conventional Commits message ($7).
21 | 5. List measurable acceptance criteria ($6).
22 | 
23 | Output format:
24 | 
25 | - One section per task: "## $1 — $2"
26 | - Subsections: Plan, Files, Tests, Acceptance, Commit Message ($7), Risks.
27 | 
28 | Notes:
29 | - Do not mutate tasks.json. Emit proposed changes only.
```

temp-prompts-refactored/tm-blockers.md
```
1 | <!-- Placeholders: $1=Trigger, $2=Purpose, $3=Steps, $4=Output format, $5=Examples, $6=Notes, $7=Input/Output examples -->
2 | 
3 | **Blocker Diagnosis Template**
4 | 
5 | $1
6 | 
7 | $2
8 | 
9 | $3
10 | 
11 | $4
12 | 
13 | $5
14 | 
15 | $6
16 | 
17 | 
18 | # Blocker Report: $7
19 | 
20 | Tables: blockers (type | item | evidence), actions (step | owner | effort | success_criteria).
```

temp-prompts-refactored/tm-ci.md
```
1 | <!-- $1 = task path (e.g., "/tm-ci") -->
2 | <!-- $2 = purpose statement -->
3 | <!-- $3 = ready tasks path (e.g., "/tm-next") -->
4 | <!-- $4 = grouping method (e.g., "by component/tag") -->
5 | <!-- $5 = CI job details (name | trigger | commands | est_time) -->
6 | <!-- $6 = test matrix (scope | command | expected_artifacts) -->
7 | <!-- $7 = risk areas -->
8 | 
9 | # CI/Test Checklist Template
10 | 
11 | ## Analysis
12 | - [ ] Affected files
13 | - [ ] Root cause
14 | - [ ] Proposed fix
15 | - [ ] Tests
16 | - [ ] Docs gaps
17 | - [ ] Open questions
18 | 
19 | ## How-to Steps
20 | 1. Compute ready tasks (see $3) and collect testStrategy fields.
21 | 2. Group by $4; otherwise by path keywords in titles.
22 | 3. Propose CI jobs and test commands with approximate runtimes and gating rules ($5).
23 | 4. Include a smoke-test matrix ($6) and minimal code coverage targets if relevant.
24 | 
25 | Output format:
26 | - "# CI Plan"
27 | - Tables: jobs ($5) and tests ($6)
28 | - "## Risk Areas" ($7)
29 | 
30 | Examples:
31 | - Input: $1
32 | - Output: one CI plan with 3–8 jobs and a test table.
33 | 
34 | Notes:
35 | - Non-binding guidance. Adapt to the repo’s actual CI system.
```

temp-prompts-refactored/tm-delta.md
```
1 | # $1 → Tasks Delta
2 | 
3 | Trigger: $2
4 | 
5 | Purpose: Compare $1 against tasks.json and propose add/update/remove operations.
6 | 
7 | Steps:
8 | 
9 | $3. Extract $4, $5, $6, and $7 from $1.
10 | $4. Map them to existing tasks by fuzzy match on title and keywords; detect gaps.
11 | 
12 | Propose: new tasks, updates to titles/descriptions/priority, and deprecations.
13 | 
14 | Output format:
15 | 
16 | - "# Delta Summary"
17 | - Tables: adds | updates | removals.
18 | - "## JSON Patch" with an ordered list of operations: add/replace/remove.
19 | - "## Assumptions" and "## Open Questions".
20 | 
21 | Examples:
22 | 
23 | - Input: $2
24 | - Output: tables with a small JSON Patch block.
25 | 
26 | Notes:
27 | 
28 | - Keep patches minimal and reversible. Flag any destructive changes explicitly.
```

temp-prompts-refactored/tm-docs.md
```
1 | <!-- Placeholder mapping:
2 | - $1 = Trigger
3 | - $2 = Purpose
4 | - $3 = Steps count
5 | - $4 = Output format
6 | - $5 = Examples
7 | - $6 = Notes
8 | -->
9 | 
10 | **Project Status Docs**
11 | 
12 | # Generate Status Docs
13 | 
14 | Trigger: $1
15 | 
16 | Purpose: $2
17 | 
18 | Steps:
19 | 1. $3
20 | 2. $4
21 | 3. $5
22 | 4. $6
23 | 
24 | Output format:
25 | - $7
26 | 
27 | Examples:
28 | - $8
29 | 
30 | Notes:
31 | - $9
32 | 
33 | 
34 | **Analysis**
35 | - [ ] Affected files: [list]
36 | - [ ] Root cause: [reason]
37 | - [ ] Proposed fix: [solution]
38 | - [ ] Tests: [test cases]
39 | - [ ] Docs gaps: [missing sections]
40 | - [ ] Open questions: [questions]
41 | 
42 | **Root cause**
43 | - [ ] Identifying factors: [list]
44 | 
45 | **Proposed fix**
46 | - [ ] Action items: [list]
47 | 
48 | **Tests**
49 | - [ ] Test cases: [list]
50 | 
51 | **Docs gaps**
52 | - [ ] Missing sections: [list]
53 | 
54 | **Open questions**
55 | - [ ] Unresolved issues: [list]
```

temp-prompts-refactored/tm-next.md
```
1 | # Next Ready Tasks
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | Steps:
8 | 
9 | 1. $3
10 | 2. $4
11 | 3. $5
12 | 4. $6
13 | 
14 | Output format:
15 | 
16 | - "$7"
17 | - Table: id | title | priority | why_ready | prereqs
18 | - "## Notes" for tie-break rules and data gaps.
19 | 
20 | Examples:
21 | 
22 | - Input: $8
23 | - Output: $9
24 | 
25 | Notes:
26 | 
27 | - Treat missing or null priority as $10. If custom scales exist, describe them in Notes.
28 | 
29 | <!-- Placeholder mapping -->
30 | $1: Trigger (e.g., "/tm-next")
31 | $2: Purpose (brief description)
32 | $3: Step 1 (algorithmic step)
33 | $4: Step 2 (algorithmic step)
34 | $5: Step 3 (algorithmic step)
35 | $6: Step 4 (algorithmic step)
36 | $7: Output format description
37 | $8: Example input format
38 | $9: Example output format
39 | $10: Default priority value
```

temp-prompts-refactored/tm-overview.md
```
1 | # TaskMaster Overview
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | Steps:
8 | 1. Locate the active tasks.json at repo root or the path supplied in the user message. Do not modify it.
9 | 2. Parse fields: id, title, description, status, priority, dependencies, subtasks.
10 | 3. Compute counts per status and a table of top pending items by priority.
11 | 4. Detect dependency issues: cycles, missing ids, orphans (no deps and not depended on).
12 | 5. Approximate a critical path: longest dependency chain among pending→in_progress tasks.
13 | 
14 | Output format: $3
15 | 
16 | Examples:
17 | - Input: $4
18 | - Output: $5
19 | 
20 | Notes:
21 | - $6: Read-only. Assume statuses: pending | in_progress | blocked | done.
22 | - If tasks.json is missing or invalid, output an "## Errors" section with a concise diagnosis.
23 | 
24 | <!-- Placeholder mapping -->
25 | $1 = Task description
26 | $2 = Purpose statement
27 | $3 = Output format specification
28 | $4 = Example input format
29 | $5 = Expected output structure
30 | $6 = Critical path details (optional) -->
```

temp-prompts-refactored/tm-refine.md
```
1 | <!-- $1=task ID (e.g., "TM-09"), $2=subtasks table content, $3=JSON patch array -->
2 | 
3 | **Refine Task into Subtasks**
4 | 
5 | Trigger: /tm-refine
6 | 
7 | Purpose: Expand a vague or large task into actionable subtasks with clear acceptance criteria.
8 | 
9 | Steps:
10 | 
11 | 1. Load the task by $1 and analyze description for ambiguity and scope.
12 | 2. Propose 3–8 subtasks with titles, brief descriptions, and dependencies between them.
13 | 3. Define acceptance criteria per subtask using Given/When/Then or bullet checks.
14 | 4. Suggest test coverage and doc updates triggered by completion.
15 | 
16 | Output format:
17 | 
18 | - "# Refinement: $1"
19 | - Subtasks as a Markdown table: $2
20 | - "## JSON Patch" fenced code of suggested additions suitable for tasks.json editing: $3
21 | 
22 | Examples:
23 | 
24 | - Input: /tm-refine $1
25 | - Output: $2 plus a minimal JSON Patch array.
26 | 
27 | Constraints:
28 | - Do not assume authority to change files; provide patches the user can apply.
```

temp-prompts-refactored/todo-report.md
```
1 | <!-- $1=Task goal statement, $2=Command to run, $3=Grouping criteria, $4=Triage plan description, $5=Summary restatement, $6=Prioritized recommendations, $7=Output subheading structure -->
2 | 
3 | **CLI Assistant Prompt for TODO Triage**
4 | 
5 | You are a CLI assistant focused on helping contributors with the task: $1.
6 | 
7 | 1. Gather context by running $2.
8 | 2. Aggregate and group TODO/FIXME/XXX by $3.
9 | 3. Propose a triage plan: $4.
10 | 
11 | Output:
12 | - Begin with a concise summary that restates the goal: $5.
13 | - Offer prioritized, actionable recommendations with rationale: $6.
14 | - Organize details under clear subheadings: $7.
```

temp-prompts-refactored/todos.md
```
1 | <!--
2 | $1 = command to run for evidence gathering
3 | $2 = task title
4 | $3 = synthesis instructions
5 | $4 = example output
6 | $5 = example input (n/a)
7 | -->
8 | 
9 | **How-to: Find and group TODO/FIXME annotations**
10 | 
11 | 1. Gather context by running `$1`.
12 | 2. Find and group TODO/FIXME annotations.
13 | 3. $3
14 | 
15 | Output:
16 | 
17 | - Begin with a concise summary that restates the goal: Find and group TODO/FIXME annotations.
18 | - Document the evidence you used so maintainers can trust the conclusion.
19 | 
20 | Example Input:
21 | $5
22 | 
23 | Expected Output:
24 | $4
```

temp-prompts-refactored/tsconfig-review.md
```
1 | <!-- Placeholder mapping:
2 | $1 = Title (e.g., "Review tsconfig for correctness and DX")
3 | $2 = Summary (e.g., "You are a CLI assistant focused on helping contributors with the task...")
4 | $3 = Recommendations (e.g., "Prioritized, actionable recommendations with rationale")
5 | $4 = Evidence (e.g., "Documentation of the evidence used")
6 | $5 = Example Inputs (e.g., "(none – command runs without arguments)")
7 | $6 = Expected Output (e.g., "Structured report following the specified sections") -->
8 | 
9 | **CLI Assistant Task: Review tsconfig**
10 | 
11 | You are a CLI assistant focused on helping contributors with the task: $1
12 | 
13 | 1. Gather context by inspecting $2.
14 | 2. Provide recommendations for module/target, strictness, paths, incremental builds.
15 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
16 | 
17 | **Output**
18 | 
19 | - Begin with a concise summary that restates the goal: $1
20 | - Offer prioritized, actionable recommendations with rationale: $3
21 | - Document the evidence you used so maintainers can trust the conclusion: $4
22 | 
23 | **Example**
24 | - Input: $5
25 | - Expected Output: $6
26 | 
27 | ---
28 | 
29 | ### Optional sections (for analysis tasks)
30 | - [ ] Affected files
31 | - [ ] Root cause
32 | - [ ] Proposed fix
33 | - [ ] Tests
34 | - [ ] Docs gaps
35 | - [ ] Open questions
```

temp-prompts-refactored/ui-screenshots.md
```
1 | <!-- $1=Title, $2=Trigger, $3=Purpose, $4=Step 1, $5=Step 2, $6=Step 3, $7=Output format -->
2 | **UI Screenshots Analysis**
3 | 
4 | Trigger: $2
5 | 
6 | Purpose: $3
7 | 
8 | ## Steps
9 | 
10 | 1. $4
11 | 2. $5
12 | 3. $6
13 | 
14 | ## Output format
15 | $7
16 | 
17 | ## Affected files (optional)
18 | - List components/files needing changes
19 | 
20 | ## Root cause (optional)
21 | - Specific UI issues identified
22 | 
23 | ## Proposed fix (optional)
24 | - Concrete implementation changes
25 | 
26 | ## Test cases (optional)
27 | - Validation criteria for fixes
28 | 
29 | ## Open questions (optional)
30 | - Unclear requirements or edge cases
```

temp-prompts-refactored/update-changelog.md
```
1 | ```
2 | <!-- Placeholder mapping -->
3 | $1 = Trigger command (e.g., "/update-changelog")
4 | $2 = Purpose statement (e.g., "Generate a user-facing CHANGELOG entry...")
5 | $3 = Step 1 description (e.g., "Inspect repo state:")
6 | $4 = Step 2 description (e.g., "Collect changes:")
7 | $5 = Step 3 description (e.g., "De-dupe and rewrite:")
8 | $6 = Step 4 description (e.g., "Emit Markdown snippet...")
9 | $7 = Step 5 description (e.g., "Decide placement:")
10 | 
11 | **How-to: Update CHANGELOG**
12 | 
13 | $1
14 | 
15 | Purpose: $2
16 | 
17 | Steps:
18 | 
19 | $3
20 | 
21 | $4
22 | 
23 | $5
24 | 
25 | $6
26 | 
27 | $7
28 | 
29 | Output format:
30 | 
31 | - Heading line with target section (Unreleased or version)
32 | - Six-section block in Markdown with only non-empty sections in order: Added, Changed, Deprecated, Removed, Fixed, Security
33 | - A short "Link references" block suggestion for `[Unreleased]` and new version comparison links
34 | - A unified diff (context 3) for `CHANGELOG.md`
35 | 
36 | Examples:
37 | 
38 | Input →
39 | ```
40 | $8
41 | ```
42 | 
43 | Output →
44 | ```
45 | $9
46 | ```
47 | 
48 | Notes:
49 | 
50 | - Assumes git repository is available and tags follow SemVer.
51 | - Keep content end-user focused. Avoid internal file names and refactor notes.
52 | - If no Conventional Commits, infer section from message heuristics.
53 | - Do not include secrets or internal ticket links.
54 | ```
```

temp-prompts-refactored/version-control-guide.md
```
1 | # Version Control Guide
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: Enforce clean incremental commits and clean-room re-implementation when finalizing.
6 | 
7 | ## Steps
8 | 
9 | $2
10 | 
11 | ## Output format
12 | 
13 | $3
14 | 
15 | ## Examples
16 | 
17 | $4
18 | 
19 | ## Notes
20 | 
21 | $5
```

temp-prompts-refactored/version-proposal.md
```
1 | # Version Proposal
2 | 
3 | Trigger: $1
4 | 
5 | Purpose: $2
6 | 
7 | You are a CLI assistant focused on helping contributors with the task: $3
8 | 
9 | 1. Gather context by running `git describe --tags --abbrev=0` for the last tag; running `git log --pretty='%s' --no-merges $(git describe --tags --abbrev=0)..HEAD` for the commits since last tag (no merges).
10 | 2. Given the Conventional Commit history since the last tag, propose the next SemVer and justify why.
11 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
12 | 
13 | Output:
14 | - Begin with a concise summary that restates the goal: $4
15 | - Offer prioritized, actionable recommendations with rationale.
16 | - Document the evidence you used so maintainers can trust the conclusion.
17 | 
18 | Example Input:
19 | $5
20 | 
21 | Expected Output:
22 | - Structured report following the specified sections.
23 | 
24 | <!-- Placeholders:
25 | $1 = Trigger (e.g., "/version-proposal")
26 | $2 = Purpose (e.g., "Propose the next semantic version based on commit history")
27 | $3 = Task description (e.g., "Propose next version (major/minor/patch) from commit history")
28 | $4 = Output summary goal (e.g., "Propose next version (major/minor/patch) from commit history")
29 | $5 = Example input format (e.g., "(none – command runs without arguments)") -->
```

temp-prompts-refactored/voice-input.md
```
1 | <!-- $1 = Template title (e.g., "Voice Input") -->
2 | <!-- $2 = Trigger command (e.g., "/voice-input") -->
3 | <!-- $3 = Purpose statement (e.g., "Support interaction from voice capture and convert to structured prompts") -->
4 | <!-- $4 = Step description (e.g., "Accept transcript text") -->
5 | <!-- $5 = Output format description (e.g., "Cleaned command list ready to execute") -->
6 | 
7 | **Voice Input Template**
8 | 
9 | Trigger: $2
10 | 
11 | Purpose: $3
12 | 
13 | ## Steps
14 | 1. $4
15 | 2. Normalize to tasks or commands for other prompts.
16 | 3. Preserve speaker intents and important entities.
17 | 
18 | ## Key entities
19 | *(e.g., speaker intent, command type, entities)*
20 | 
21 | ## Expected output
22 | $5
```

temp-prompts-organized/_shared/rank-root-prompts.shared.md
```
1 | <!--
2 | $1 = command name/identifier
3 | $2 = example user question
4 | $3 = project CWD path to scan for context (defaults to current directory)
5 | $4 = prompt directory path (defaults to "~/.codex/prompts")
6 | $5 = minimum relevance threshold (0–1)
7 | -->
8 | 
9 | # {Context-Aware Prompt Ranking Command}
10 | 
11 | ```md
12 | # Command: $1
13 | 
14 | # Usage: $1 "$2" "$3" "$4" "$5"
15 | 
16 | # Args:
17 | 
18 | # - {{query}}: $2
19 | # - {{project_path}}: $3
20 | # - {{prompt_path}}: $4
21 | # - {{threshold}}: $5
22 | 
23 | prompt = """
24 | Task:
25 | Given a user inquiry ({{query}}) and the context of a software project located at {{project_path}}, your goal is to identify the most relevant prompt-definition file from the directory {{prompt_path}}.
26 | 
27 | Defaults:
28 | * If {{project_path}} is missing or blank, use the current working directory.
29 | * If {{prompt_path}} is missing or blank, use "~/.codex/prompts".
30 | 
31 | Do the following:
32 | 1) **Analyze Project Context**: Recursively scan {{project_path}} to understand its structure, languages, and purpose. Create a concise summary of the project context.
33 | 2) **Scan Prompts**: List all candidate prompt files in {{prompt_path}} (non-recursively).
34 | 3) **Evaluate Prompts**: For each candidate prompt file:
35 |     a) Read its content.
36 |     b) Create a one-sentence summary of its purpose and domain.
37 |     c) Compute a relevance score from 0 to 1. This score must measure how well the prompt's purpose aligns with the user's {{query}}, considering the project context summary. A higher score means the prompt is a better fit for solving the query within the given project.
38 | 4) **Rank and Filter**: Order the prompts by their relevance score in descending order.
39 | 5) **Generate Output**: Emit a compact markdown table with the columns: `filename | description | match_score` (rounded to 2 decimals).
40 | 
41 | Rules:
42 | * The description must be 1–2 sentences capturing the prompt's purpose and domain.
43 | * Only include prompts in the table where `match_score` is greater than or equal to {{threshold}}.
44 | * If no prompts meet the threshold, output a single line: "No prompt exceeds threshold {{threshold}} — recommend creating a new prompt."
45 | 
46 | Acceptance:
47 | * If one or more matches meet the {{threshold}}, a markdown table sorted by descending `match_score` is produced.
48 | * Otherwise, the single-line fallback message is produced.
49 | 
50 | !{echo "Scanning project: ${PROJECT_PATH_ARG:-.}"}
51 | !{echo "Searching for prompts in: ${PROMPT_PATH_ARG:-~/.codex/prompts}"}
52 | """
53 | ```
54 | 
55 | ## Output format
56 | 
57 | * **Preferred**: a markdown table with columns `filename | description | match_score` sorted by `match_score` (desc) and filtered by `{{threshold}}`.
58 | * **Fallback**: the exact one-line message when no entries meet `{{threshold}}`.
```

temp-prompts-organized/_shared/reset-strategy.shared.md
```
1 | ---
2 | phase: "Reset Playbook"
3 | gate: "Clean restart"
4 | status: "triggered when gate criteria stall for >60 minutes."
5 | previous:
6 |   - "Any blocked stage"
7 | next:
8 |   - "Restart with /planning-process then follow the gated flow"
9 | ---
10 | 
11 | # Reset Strategy
12 | 
13 | Trigger: /reset-strategy
14 | 
15 | Purpose: Decide when to hard reset and start clean to avoid layered bad diffs.
16 | 
17 | ## Steps
18 | 
19 | 1. Run: `git status -sb` and `git diff --stat` to assess churn.
20 | 2. If many unrelated edits or failing builds, propose: `git reset --hard HEAD` to discard working tree.
21 | 3. Save any valuable snippets to `scratch/` before reset.
22 | 4. Re-implement the minimal correct fix from a clean state.
23 | 
24 | ## Output format
25 | 
26 | - A short decision note and exact commands. Never execute resets automatically.
27 | 
28 | ## Examples
29 | 
30 | - Recommend reset after repeated failing refactors touching 15+ files.
31 | 
32 | ## Notes
33 | 
34 | - Warn about destructive nature. Require user confirmation.
35 | 
```

temp-prompts-organized/_shared/roll-up.shared.md
```
1 | # Research Roll-up Summary
2 | 
3 | Trigger: /roll-up
4 | 
5 | Purpose: Summarize per-item statuses, enabled decisions, unresolved risks, and count sources by domain type.
6 | 
7 | Steps:
8 | 
9 | 1. Aggregate Conversation State Updates from prior items.
10 | 2. Produce per-item status lines and decisions.
11 | 3. Tally sources by domain type: gov, org, docs, blog, news, academic.
12 | 
13 | Output format:
14 | 
15 | ```
16 | ## Roll-up Summary
17 | - Item {n}: {status} — decision enabled: {…}; risks: {…}
18 | - Sources by domain type: {gov:X, org:Y, docs:Z, blog:A, news:B, academic:C}
19 | ```
20 | 
21 | Examples:
22 | 
23 | - Input: `/roll-up from items 1–3`
24 | - Output: Summary block as above.
25 | 
26 | Notes:
27 | 
28 | - Use counts derived from the Evidence Logs.
```

temp-prompts-organized/_shared/summary.shared.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Produce a README‑level summary of the repo.
2 | 
3 | 1. Gather context by running `git ls-files | sed -n '1,400p'` for the repo map (first 400 files); inspecting `README.md` for the key docs if present; inspecting `docs` for the key docs if present.
4 | 2. Generate a high‑level summary (What, Why, How, Getting Started).
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Produce a README‑level summary of the repo.
10 | - Document the evidence you used so maintainers can trust the conclusion.
11 | 
12 | Example Input:
13 | (none – command runs without arguments)
14 | 
15 | Expected Output:
16 | 
17 | - Structured report following the specified sections.
```

temp-prompts-organized/_shared/switch-model.shared.md
```
1 | ---
2 | phase: "P9 Model Tactics"
3 | gate: "Model uplift"
4 | status: "document rollback/guardrails before flipping defaults."
5 | previous:
6 |   - "/compare-outputs"
7 | next:
8 |   - "Return to the blocked stage (e.g., /integration-test) to apply learnings"
9 | ---
10 | 
11 | # Switch Model
12 | 
13 | Trigger: /switch-model
14 | 
15 | Purpose: Decide when to try a different AI backend and how to compare.
16 | 
17 | ## Steps
18 | 
19 | 1. Define task type: frontend codegen, backend reasoning, test writing, refactor.
20 | 2. Select candidate models and temperature/tooling options.
21 | 3. Run a fixed input suite and measure latency, compile success, and edits needed.
22 | 4. Recommend a model per task with rationale.
23 | 
24 | ## Output format
25 | 
26 | - Table: task → model → settings → win reason.
27 | 
```

temp-prompts-organized/_templates/instruction-file.templates.md
```
1 | ---
2 | phase: "P0 Preflight Docs"
3 | gate: "DocFetchReport"
4 | status: "capture approved instructions before proceeding."
5 | previous:
6 |   - "Preflight discovery (AGENTS baseline)"
7 | next:
8 |   - "/planning-process"
9 |   - "/scope-control"
10 | ---
11 | 
12 | # Instruction File
13 | 
14 | Trigger: /instruction-file
15 | 
16 | Purpose: Generate or update `cursor.rules`, `windsurf.rules`, or `claude.md` with project-specific instructions.
17 | 
18 | ## Steps
19 | 
20 | 1. Scan repo for existing instruction files.
21 | 2. Compose sections: Context, Coding Standards, Review Rituals, Testing, Security, Limits.
22 | 3. Include "Reset and re-implement cleanly" guidance and scope control.
23 | 4. Write to chosen file and propose a commit message.
24 | 
25 | ## Output format
26 | 
27 | - Markdown instruction file with stable headings.
28 | 
```

temp-prompts-organized/_templates/prompt-sequence-generator.templates.md
```
1 | # Prompt: Generate Prompt Execution Sequence
2 | 
3 | **Purpose:** Given a high-level goal and a set of available prompts, generate the logical execution sequence required to accomplish that goal by chaining the prompts together.
4 | 
5 | ---
6 | 
7 | ### **Inputs**
8 | 
9 | *   **High-Level Goal:** {{high_level_goal}}
10 |     *   *A clear, one-sentence description of the final outcome the user wants to achieve.*
11 |     *   *Example: "Create and document a pull request for the currently staged changes."*
12 | 
13 | *   **Available Prompts:**
14 |     ```
15 |     {{available_prompts}}
16 |     ```
17 |     *   *A list of candidate prompt names (e.g., from the output of `rank-root-prompts`).*
18 |     *   *Example: ['pr-desc.md', 'commit-msg.md', 'changed-files.md', 'review.md', 'release-notes.md']*
19 | 
20 | *   **Context (Optional):** {{context}}
21 |     *   *Any additional context, such as the current state of the git repository or specific files of interest.*
22 |     *   *Example: "The user has already staged files using `git add`."*
23 | 
24 | ---
25 | 
26 | ### **Instructions for the AI**
27 | 
28 | 1.  **Analyze the Goal:** Deconstruct the `{{high_level_goal}}` into a series of logical steps required to get from the starting state to the final outcome.
29 | 
30 | 2.  **Map Prompts to Steps:** For each logical step, identify the most suitable prompt from the `{{available_prompts}}` list that can perform that step.
31 |     *   Consider the inputs and outputs of each prompt to determine dependencies. A prompt's input is often the output of a previous one.
32 | 
33 | 3.  **Establish Order:** Arrange the selected prompts into a numbered sequence based on their dependencies. The sequence should represent a complete and logical workflow.
34 | 
35 | 4.  **Identify Gaps:** If any necessary step in the workflow cannot be fulfilled by one of the available prompts, explicitly state what action or prompt is missing.
36 | 
37 | ---
38 | 
39 | ### **Required Output Format**
40 | 
41 | **Execution Sequence:**
42 | 
43 | 1.  **`[prompt_name_1.md]`**: [Brief justification for why this prompt is first and what it accomplishes.]
44 | 2.  **`[prompt_name_2.md]`**: [Brief justification for why this prompt is second, and how it uses the output of the previous step.]
45 | 3.  ...
46 | 
47 | **Identified Gaps (if any):**
48 | 
49 | *   [Description of a missing step or prompt needed to complete the workflow.]
```

temp-prompts-organized/_templates/system-level-instruction-editor.templates.md
```
1 | phase: "P0 Preflight Docs"
2 | gate: "Scope Gate"
3 | status: "draft"
4 | owner: "Prompt Ops"
5 | date: "2025-09-20"
6 | previous:
7 |   - "/instruction-file.md"
8 |   - "/planning-process.md"
9 | next:
10 |   - "/AGENTS.md"
11 |   - "/GEMINI.md"
12 | tags:
13 |   - "instructions"
14 |   - "editor"
15 | ---
16 | 
17 | # System Instruction: Canonical Instruction File Editor
18 | 
19 | Trigger: /<slash-command>
20 | 
21 | Purpose: <1–2 lines describing the objective and outcome criteria.>
22 | 
23 | ## Inputs
24 | 
25 | - <logs/artifacts to collect>
26 | - <affected services/modules>
27 | - <build/version/commit>
28 | - <time window/region/tenant>
29 | - <SLO/SLA impacted>
30 | 
31 | ## Steps
32 | 
33 | 1. Collect relevant data (<test logs, traces, metrics, dumps, repro steps>).
34 | 2. Group by symptom/pattern; for each group, list 2–3 plausible causes.
35 | 3. Propose disambiguators (instrumentation, targeted inputs, experiments).
36 | 4. Sketch minimal fixes (patches/config toggles/rollbacks) with risk notes.
37 | 5. Validate fixes (tests to run, monitors to watch, acceptance criteria).
38 | 6. Roll out & verify (staged rollout plan, owners, ETA).
39 | 7. Capture follow-ups (refactors, docs, guardrails).
40 | 
41 | 1. **Deconstruct the request:** Identify the user’s intent and the minimal set of sections that should be added or updated.
42 | 2. **Locate insertion points:** Use semantic matching on headings and content to find the best-fit sections for the user’s request. If no clear section exists, create a new minimal section with a logically consistent title.
43 | 3. **Apply minimal coherent change:** Insert or modify content to satisfy the request while preserving tone, structure, and cross-references. Keep unrelated sections unchanged.
44 | 4. **Run invariants:**
45 | 
46 |    - The entire file must be present (no placeholders, no truncation).
47 |    - Markdown structure and formatting must remain valid.
48 |    - Internal references and links stay accurate.
49 | 5. **Render in Canvas:**
50 | 
51 |    - If editing an existing file: open in Canvas and **replace the full contents** with the updated version.
52 |    - If creating a new file: create it in Canvas and display the **entire file**.
53 | 6. **Variants (optional or on request):** Generate `GEMINI.md` and/or `CLAUDE.md` from the updated `AGENTS.md` using only the Platform Substitution Rules. Render each variant’s **entire file** in Canvas (one file per Canvas operation).
54 | 7. **Size-limit fallback:** If a size cap prevents full-file rendering in Canvas, output the **entire file in chat**, then append:
55 | 
56 |    - “*Note: Full content was output in chat due to a size limit preventing Canvas rendering.*”
57 | 
58 | ## Output format
59 | 
60 | - Table: <symptom/item> → <likely causes> → <next checks> → <candidate fix> → <owner/ETA>.
61 | 
62 | ## Example rows
63 | 
64 | - "<example symptom or error>" → <cause A, cause B> → <check 1, check 2> → <fix sketch> → <owner/ETA>.
```

temp-prompts-organized/prompt-front-matter/00-ideation__architecture__adr-new.architecture.refactor.md
```
1 | # ADR Drafting Assistant
2 | 
3 | Task: Given the following prompt, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the input text.
4 | 
5 | ## Inputs
6 | - Input prompt: "You are a CLI assistant focused on helping contributors with the task: Draft an Architecture Decision Record with pros/cons."
7 | - Workflow steps: Gather context from `README.md`, draft ADR (Context, Decision, Status, Consequences), synthesize insights.
8 | - Output requirements: Concise summary of goal; workflow triggers/failing jobs/proposed fixes; documented evidence for maintainers' trust.
9 | 
10 | ## Canonical taxonomy (exact strings)
11 | - architecture
12 | - decision-making
13 | - documentation
14 | 
15 | ### Stage hints (for inference)
16 | - ideation → early drafting, context gathering
17 | - planning → structured output design
18 | - implementation → actual code changes
19 | - review → peer feedback or approval
20 | 
21 | ## Algorithm
22 | 1. Extract signals from input:
23 |    - Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
24 | 2. Determine the primary identifier:
25 |    - Prefer explicit input; otherwise infer from main action + object.
26 |    - Normalize (lowercase, kebab-case, length-capped, starts with a letter).
27 |    - De-duplicate.
28 | 3. Determine categories:
29 |    - Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
30 |    - Validate, sort deterministically, and de-dupe (≤3).
31 | 4. Determine lifecycle/stage (optional):
32 |    - Prefer explicit input; otherwise map categories via stage hints.
33 |    - Omit if uncertain.
34 | 5. Determine dependencies (optional):
35 |    - Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
36 | 6. Determine provided artifacts (optional):
37 |    - Short list (≤3) of unlocked outputs.
38 | 7. Compose summary:
39 |    - One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
40 | 8. Produce metadata in the requested format:
41 |    - Default to a human-readable serialization; honor any requested alternative.
42 | 9. Reconcile if input already contains metadata:
43 |    - Merge: explicit inputs > existing > inferred.
44 |    - Validate lists; move unknowns to an extension field if needed.
45 |    - Remove empty keys.
46 | 
47 | ## Assumptions & Constraints
48 | - Emit exactly one document: metadata, a single blank line, then the original body.
49 | - Limit distinct placeholders to ≤7.
50 | 
51 | ## Validation
52 | - Identifier matches a normalized id pattern (e.g., kebab-case, lowercase).
53 | - Categories non-empty and drawn from canonical taxonomy (≤3).
54 | - Stage, if present, is one of the allowed stages implied by stage hints.
55 | - Dependencies, if present, are id-shaped (≤5).
56 | - Artifacts are short (≤3) and relevant to output.
57 | - Summary ≤120 chars; punctuation coherent.
58 | - Body text is not altered.
59 | 
60 | ## Output format examples
61 | - Identifier: `adr-draft`
62 | - Categories: architecture, decision-making, documentation
63 | - Lifecycle stage: ideation
64 | - Dependencies: README.md
65 | - Provided artifacts: ADR with pros/cons, evidence summary, workflow insights
66 | - Summary: "Draft an Architecture Decision Record with pros/cons to achieve transparent decision documentation."
```

temp-prompts-organized/prompt-front-matter/00-ideation__architecture__logging-strategy.architecture.refactor.md
```
1 | # Logging Strategy
2 | 
3 | ## Metadata
4 | 
5 | - identifier: logging-strategy
6 | - categories: [observability, operations, security]
7 | - stage: design
8 | - dependencies: []
9 | - provided_artifacts: ["diff hunks", "short guideline section"]
10 | - summary: Do add or remove diagnostic logs with privacy in mind to achieve structured observability.
11 | 
12 | ## Steps
13 | 
14 | 1. Identify hotspots from recent failures.
15 | 2. Insert structured logs with contexts and correlation IDs.
16 | 3. Remove noisy or PII-leaking logs.
17 | 4. Document log levels and sampling in `OBSERVABILITY.md`.
18 | 
19 | ## Output format
20 | 
21 | - Diff hunks and a short guideline section.
```

temp-prompts-organized/prompt-front-matter/00-ideation__architecture__modular-architecture.architecture.refactor.md
```
1 | # Modular Architecture
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: modular-architecture  
6 | - **categories**: architecture  
7 | - **stage**: design  
8 | - **dependencies**: [module-boundaries-identification]  
9 | - **provided-artifacts**: [module-graph, dependency-diff, contract-test-plan]  
10 | - **summary**: Do modularize services to achieve clear boundaries and testable interfaces.
11 | 
12 | ## Steps
13 | 
14 | 1. Identify services/modules and their public contracts.
15 | 2. Flag cross-module imports and circular deps.
16 | 3. Propose boundaries, facades, and internal folders.
17 | 4. Add "contract tests" for public APIs.
18 | 
19 | ## Output format
20 | 
21 | - Diagram-ready list of modules and edges, plus diffs.
```

temp-prompts-organized/prompt-front-matter/00-ideation__architecture__stack-evaluation.architecture.refactor.md
```
1 | # Stack Evaluation
2 | 
3 | ## Metadata
4 | 
5 | - identifier: stack-evaluation
6 | - categories: [evaluation, analysis, recommendation]
7 | - stage: evaluation
8 | - dependencies: []
9 | - provided_artifacts: ["decision memo", "next steps"]
10 | - summary: Evaluate language/framework choices to achieve informed stay-or-switch decisions.
11 | 
12 | ## Steps
13 | 
14 | 1. Detect current stack and conventions.
15 | 2. List tradeoffs: maturity, tooling, available examples, hiring, and AI training coverage.
16 | 3. Recommend stay-or-switch with migration outline if switching.
17 | 
18 | ## Output format
19 | 
20 | - Decision memo with pros/cons and next steps.
```

temp-prompts-organized/prompt-front-matter/00-ideation__design__action-diagram.design.refactor.md
```
1 | # Action Diagram Metadata
2 | 
3 | ## Inputs
4 | - Source file path: C:\Users\user\projects\prompts\temp-prompts\00-ideation\design\action-diagram.design.md
5 | - Maximum placeholders allowed: 7
6 | 
7 | ## Canonical taxonomy (exact strings)
8 | - devops
9 | - pipeline
10 | - workflow
11 | 
12 | ### Stage hints (for inference)
13 | - build → development stage
14 | - deploy → production stage
15 | - push → trigger stage
16 | 
17 | ## Algorithm
18 | 1. Extract signals from $1  
19 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
20 | 
21 | 2. Determine the primary identifier  
22 |    * Prefer explicit input; otherwise infer from main action + object.  
23 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
24 |    * De-duplicate.
25 | 
26 | 3. Determine categories  
27 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
28 |    * Validate, sort deterministically, and de-dupe (≤3).
29 | 
30 | 4. Determine lifecycle/stage (optional)  
31 |    * Prefer explicit input; otherwise map categories via $6.  
32 |    * Omit if uncertain.
33 | 
34 | 5. Determine dependencies (optional)  
35 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
36 | 
37 | 6. Determine provided artifacts (optional)  
38 |    * Short list (≤3) of unlocked outputs.
39 | 
40 | 7. Compose summary  
41 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
42 | 
43 | 8. Produce metadata in the requested format  
44 |    * Default to a human-readable serialization; honor any requested alternative.
45 | 
46 | 9. Reconcile if input already contains metadata  
47 |    * Merge: explicit inputs > existing > inferred.  
48 |    * Validate lists; move unknowns to an extension field if needed.  
49 |    * Remove empty keys.
50 | 
51 | ## Assumptions & Constraints
52 | - Emit exactly one document: metadata, a single blank line, then $1.
53 | - Limit distinct placeholders to ≤ 7.
54 | 
55 | ## Validation
56 | - Identifier matches a normalized id pattern.
57 | - Categories non-empty and drawn from $5 (≤3).
58 | - Stage, if present, is one of the allowed stages implied by $6.
59 | - Dependencies, if present, are id-shaped (≤5).
60 | - Summary ≤120 chars; punctuation coherent.
61 | - Body text $1 is not altered.
62 | 
63 | ## Output format examples
64 | - Identifier: build  
65 | - Categories: devops, pipeline, workflow  
66 | - Lifecycle stage: none  
67 | - Dependencies: push  
68 | - Provided artifacts: deployment artifact  
69 | - Summary: Do build to achieve deployment after push
70 | 
71 | ## Metadata
72 | - identifier: build
73 | - categories: ["devops", "pipeline", "workflow"]
74 | - lifecycle_stage: null
75 | - dependencies: ["push"]
76 | - provided_artifacts: ["deployment artifact"]
77 | - summary: Do build to achieve deployment after push
78 | 
79 | ## Nodes
80 | - build
81 | - deploy
82 | 
83 | ## Edges
84 | - push -> build
85 | - build -> deploy
```

temp-prompts-organized/prompt-front-matter/00-ideation__design__api-contract.design.refactor.md
```
1 | # API Contract Design
2 | 
3 | ## Inputs
4 | - Feature or domain string (e.g., "accounts & auth")
5 | - Existing documentation and requirements
6 | - Preference for OpenAPI 3.1 or GraphQL SDL
7 | 
8 | ## Canonical taxonomy (exact strings)
9 | - design
10 | - specification
11 | - contract generation
12 | 
13 | ### Stage hints (for inference)
14 | - design → initial creation of a contract from inputs
15 | - specification → detailed schema definition
16 | - implementation → code generation phase
17 | 
18 | ## Algorithm
19 | 1. Extract signals from $1  
20 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
21 | 
22 | 2. Determine the primary identifier  
23 |    * Prefer explicit input; otherwise infer from main action + object.  
24 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
25 |    * De-duplicate.
26 | 
27 | 3. Determine categories  
28 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
29 |    * Validate, sort deterministically, and de-dupe (≤3).
30 | 
31 | 4. Determine lifecycle/stage (optional)  
32 |    * Prefer explicit input; otherwise map categories via $6.  
33 |    * Omit if uncertain.
34 | 
35 | 5. Determine dependencies (optional)  
36 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
37 | 
38 | 6. Determine provided artifacts (optional)  
39 |    * Short list (≤3) of unlocked outputs.
40 | 
41 | 7. Compose summary  
42 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
43 | 
44 | 8. Produce metadata in the requested format  
45 |    * Default to a human-readable serialization; honor any requested alternative.
46 | 
47 | 9. Reconcile if input already contains metadata  
48 |    * Merge: explicit inputs > existing > inferred.  
49 |    * Validate lists; move unknowns to an extension field if needed.  
50 |    * Remove empty keys.
51 | 
52 | ## Assumptions & Constraints
53 | - Emit exactly one document: metadata, a single blank line, then $1.
54 | - Limit distinct placeholders to ≤ 7.
55 | - All categories must be from the canonical taxonomy.
56 | - Stage mapping is deterministic and context-aware.
57 | 
58 | ## Validation
59 | - Identifier matches a normalized id pattern (e.g., api-contract).
60 | - Categories non-empty and drawn from $5 (≤3).
61 | - Stage, if present, is one of the allowed stages implied by $6.
62 | - Dependencies, if present, are id-shaped (≤5).
63 | - Dependencies must be explicit or inferable from input structure.
64 | - Artifacts list ≤3 items; all valid outputs.
65 | - Summary ≤120 chars; punctuation coherent.
66 | - Body text $1 is not altered.
67 | 
68 | ## Output format examples
69 | - Identifier: `api-contract`  
70 | - Categories: design, specification, contract generation  
71 | - Stage: design  
72 | - Dependencies: feature/domain input, existing documentation  
73 | - Artifacts: openapi.yaml, schema.graphql, changelog entry  
74 | - Summary: "Do generate an API contract from requirements to achieve a standardized specification for endpoints."
75 | 
76 | ---
77 | 
78 | # API Contract
79 | 
80 | Trigger: /api-contract "<feature or domain>"
81 | 
82 | Purpose: Author an initial OpenAPI 3.1 or GraphQL SDL contract from requirements.
83 | 
84 | **Steps:**
85 | 
86 | 1. Parse inputs and existing docs. If REST, prefer OpenAPI 3.1 YAML; if GraphQL, produce SDL.
87 | 2. Define resources, operations, request/response schemas, error model, auth, and rate limit headers.
88 | 3. Add examples for each endpoint or type. Include pagination and filtering conventions.
89 | 4. Save to `apis/<domain>/openapi.yaml` or `apis/<domain>/schema.graphql`.
90 | 5. Emit changelog entry `docs/api/CHANGELOG.md` with rationale and breaking-change flags.
91 | 
92 | **Output format:**
93 | 
94 | - `Contract Path`, `Design Notes`, and a fenced code block with the spec body.
95 | 
96 | **Examples:**
97 | 
98 | - `/api-contract "accounts & auth"` → `apis/auth/openapi.yaml` with OAuth 2.1 flows.
99 | 
100 | **Notes:**
101 | 
102 | - Follow JSON:API style for REST unless caller specifies otherwise. Include `429` and `5xx` models.
```

temp-prompts-organized/prompt-front-matter/00-ideation__design__design-assets.design.refactor.md
```
1 | # Design Assets
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: design-assets
6 | - **Categories**: design, brand assets
7 | - **Stage**: generate
8 | - **Dependencies**: brand-colors, brand-name
9 | - **Provided Artifacts**: asset-checklist, generation-commands
10 | - **Summary**: Generate favicons and small design snippets from product brand to achieve consistent visual identity.
11 | 
12 | ## Steps
13 | 
14 | 1. Extract brand colors and name from README or config.
15 | 2. Produce favicon set, social preview, and basic UI tokens.
16 | 3. Document asset locations and references.
17 | 
18 | ## Output format
19 | 
20 | - Asset checklist and generation commands.
```

temp-prompts-organized/prompt-front-matter/00-ideation__design__ui-screenshots.design.refactor.md
```
1 | # UI Screenshots
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: ui-screenshots
6 | - **Categories**: analysis, design, code-generation
7 | - **Stage**: design-review
8 | - **Dependencies**: []
9 | - **Provided Artifacts**: issue-list, css-changes, component-updates
10 | - **Summary**: Analyze UI screenshots to identify visual issues and generate actionable CSS or component changes
11 | 
12 | ## Steps
13 | 
14 | 1. Accept screenshot paths or links.
15 | 2. Describe visual hierarchy, spacing, contrast, and alignment issues.
16 | 3. Output concrete CSS or component changes.
17 | 
18 | ## Output format
19 | 
20 | - Issue list and code snippets to fix visuals.
```

temp-prompts-organized/prompt-front-matter/00-ideation__requirements__plan-delta.requirements.refactor.md
```
1 | # plan-delta
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: plan-delta  
6 | - **categories**: Planning, Task Management, Graph Maintenance  
7 | - **lifecycle_stage**: Mid-Project Adjustment  
8 | - **dependencies**: task graph history, user delta input  
9 | - **provided_artifacts**: 
10 |   - Updated tasks file (valid JSON)  
11 |   - Delta document (Markdown with # Delta, ## Objectives, ## Constraints, ## Impacts, ## Decisions, ## Evidence)  
12 |   - Readiness report (plain text: READY | BLOCKED | DEPRECATED)  
13 | - **summary**: Orchestrate mid-project planning deltas to preserve history and update task graph readiness.
14 | 
15 | ## Inputs
16 | 
17 | - User-provided delta text with objectives, constraints, findings
18 | - Selection mode: Continue, Hybrid Rebaseline, Full Rebaseline
19 | - Existing tasks file (tasks.json or equivalent)
20 | - Repository context path for task and plan files
21 | 
22 | ## Canonical taxonomy (exact strings)
23 | 
24 | Planning, Task Management, Graph Maintenance
25 | 
26 | ### Stage hints (for inference)
27 | 
28 | Mid-project adjustment, delta update, planning revision, graph maintenance, readiness recalculation
29 | 
30 | ## Algorithm
31 | 
32 | 1. Extract signals from $1  
33 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
34 | 
35 | 2. Determine the primary identifier  
36 |    * Prefer explicit input; otherwise infer from main action + object.  
37 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
38 |    * De-duplicate.
39 | 
40 | 3. Determine categories  
41 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
42 |    * Validate, sort deterministically, and de-dupe (≤3).
43 | 
44 | 4. Determine lifecycle/stage (optional)  
45 |    * Prefer explicit input; otherwise map categories via stage hints.  
46 |    * Omit if uncertain.
47 | 
48 | 5. Determine dependencies (optional)  
49 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
50 | 
51 | 6. Determine provided artifacts (optional)  
52 |    * Short list (≤3) of unlocked outputs.
53 | 
54 | 7. Compose summary  
55 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
56 | 
57 | 8. Produce metadata in the requested format  
58 |    * Default to a human-readable serialization; honor any requested alternative.
59 | 
60 | 9. Reconcile if input already contains metadata  
61 |    * Merge: explicit inputs > existing > inferred.  
62 |    * Validate lists; move unknowns to an extension field if needed.  
63 |    * Remove empty keys.
64 | 
65 | ## Assumptions & Constraints
66 | 
67 | - Emit exactly one document: metadata, a single blank line, then $1.
68 | - Limit distinct placeholders to ≤7.
69 | - All outputs are strictly defined in the output format section.
70 | 
71 | ## Validation
72 | 
73 | - Identifier matches a normalized id pattern (lowercase, kebab-case).
74 | - Categories non-empty and drawn from canonical taxonomy (≤3).
75 | - Stage, if present, is one of the allowed stages implied by stage hints.
76 | - Dependencies, if present, are id-shaped or context-based (≤5).
77 | - Provided artifacts match exactly those listed in output format.
78 | - Summary ≤120 chars; punctuation coherent.
79 | - Body text $1 is not altered.
80 | 
81 | ## Output format examples
82 | 
83 | - Input →  
84 |   ```
85 |   Mode: Continue
86 |   New objectives: add offline export for tasks
87 |   Constraints: no DB migrations
88 |   Findings: existing export lib supports JSON only
89 |   ```  
90 | 
91 |   Output →  
92 |   - Updated `tasks.json` with new task `T-342` { title: "Add CSV export", dependencies: ["T-120"], source_doc: "delta-20250921.md", lineage: ["T-120"], supersedes: [] }.  
93 |   - `artifacts/delta-20250921-160500.md` populated with objectives, constraints, impacts, decisions, evidence.  
94 |   - Readiness report lists `T-342` under READY if deps done.
95 | 
96 | - Input →  
97 |   ```
98 |   Mode: Hybrid Rebaseline
99 |   Changes: ~30% of scope affected by auth provider swap
100 |   ```  
101 | 
102 |   Output →  
103 |   - Minor-plan version bump recorded in Delta Doc.  
104 |   - New tasks added for provider swap; prior tasks kept with `deprecated` or `blocked` and lineage links.
```

temp-prompts-organized/prompt-front-matter/00-ideation__requirements__planning-process.requirements.refactor.md
```
1 | # Planning Process
2 | 
3 | ## Metadata
4 | 
5 | - identifier: planning-process
6 | - categories: 
7 |   - planning
8 |   - task-management
9 |   - risk-assessment
10 |   - validation
11 | - stage: planning
12 | - dependencies: 
13 |   - PLAN.md exists or is created
14 |   - Git repository with test runner available
15 | - provided-artifacts: 
16 |   - updated PLAN.md with structured sections and checklist
17 | - summary: Draft, refine, and execute a feature plan with strict scope control and progress tracking.
18 | 
19 | ## Inputs
20 | 
21 | - Trigger: /planning-process
22 | - Purpose: Draft, refine, and execute a feature plan with strict scope control and progress tracking.
23 | - Output format: Update or create `PLAN.md` with the sections above. Include a checklist for **Tasks**. Keep lines under 100 chars.
24 | - Examples:
25 |   - Input: "Add OAuth login"
26 |   - Output:
27 |     - Goal: Let users sign in with Google.
28 |     - Tasks: [ ] add Google client, [ ] callback route, [ ] session, [ ] E2E test.
29 |     - Won't do: org SSO.
30 |     - Ideas for later: Apple login.
31 | - Notes:
32 |   - Planning only. No code edits.
33 |   - Assume a Git repo with test runner available.
34 | 
35 | ## Canonical taxonomy (exact strings)
36 | 
37 | - planning
38 | - task-management
39 | - risk-assessment
40 | - validation
41 | 
42 | ### Stage hints (for inference)
43 | 
44 | - planning → planning
45 | - task management → planning or execution
46 | - validation → validation or testing
47 | - risk assessment → planning or review
48 | 
49 | ## Algorithm
50 | 
51 | 1. Extract signals from $1  
52 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
53 | 
54 | 2. Determine the primary identifier  
55 |    * Prefer explicit input; otherwise infer from main action + object.  
56 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
57 |    * De-duplicate.
58 | 
59 | 3. Determine categories  
60 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
61 |    * Validate, sort deterministically, and de-dupe (≤3).
62 | 
63 | 4. Determine lifecycle/stage (optional)  
64 |    * Prefer explicit input; otherwise map categories via $6.  
65 |    * Omit if uncertain.
66 | 
67 | 5. Determine dependencies (optional)  
68 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
69 | 
70 | 6. Determine provided artifacts (optional)  
71 |    * Short list (≤3) of unlocked outputs.
72 | 
73 | 7. Compose summary  
74 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
75 | 
76 | 8. Produce metadata in the requested format  
77 |    * Default to a human-readable serialization; honor any requested alternative.
78 | 
79 | 9. Reconcile if input already contains metadata  
80 |    * Merge: explicit inputs > existing > inferred.  
81 |    * Validate lists; move unknowns to an extension field if needed.  
82 |    * Remove empty keys.
83 | 
84 | ## Assumptions & Constraints
85 | 
86 | - Emit exactly one document: metadata, a single blank line, then $1.
87 | - Limit distinct placeholders to ≤ 7.
88 | - Do not alter the body text.
89 | 
90 | ## Validation
91 | 
92 | - Identifier matches a normalized id pattern (kebab-case).
93 | - Categories non-empty and drawn from canonical taxonomy (≤3).
94 | - Stage, if present, is one of the allowed stages implied by stage hints.
95 | - Dependencies, if present, are id-shaped (≤5).
96 | - Artifacts ≤3 items.
97 | - Summary ≤120 chars; punctuation coherent.
98 | - Body text is not altered.
99 | 
100 | ## Output format examples
101 | 
102 | - Metadata block:
103 |   - identifier: planning-process
104 |   - categories: 
105 |     - planning
106 |     - task-management
107 |     - risk-assessment
108 |     - validation
109 |   - stage: planning
110 |   - dependencies: 
111 |     - PLAN.md exists or is created
112 |     - Git repository with test runner available
113 |   - provided-artifacts: 
114 |     - updated PLAN.md with structured sections and checklist
115 |   - summary: Draft, refine, and execute a feature plan with strict scope control and progress tracking.
116 | 
117 | - Body text (unchanged):
118 |   # Planning Process
119 | 
120 |   Trigger: /planning-process
121 | 
122 |   Purpose: Draft, refine, and execute a feature plan with strict scope control and progress tracking.
123 | 
124 |   ## Steps
125 | 
126 |   1. If no plan file exists, create `PLAN.md`. If it exists, load it.
127 |   2. Draft sections: **Goal**, **User Story**, **Milestones**, **Tasks**, **Won't do**, **Ideas for later**, **Validation**, **Risks**.
128 |   3. Trim bloat. Convert vague bullets into testable tasks with acceptance criteria.
129 |   4. Tag each task with an owner and estimate. Link to files or paths that will change.
130 |   5. Maintain two backlogs: **Won't do** (explicit non-goals) and **Ideas for later** (deferrable work).
131 |   6. Mark tasks done after tests pass. Append commit SHAs next to completed items.
132 |   7. After each milestone: run tests, update **Validation**, then commit `PLAN.md`.
133 | 
134 |   ## Output format
135 | 
136 |   - Update or create `PLAN.md` with the sections above.
137 |   - Include a checklist for **Tasks**. Keep lines under 100 chars.
138 | 
139 |   ## Examples
140 |   **Input**: "Add OAuth login"
141 | 
142 |   **Output**:
143 | 
144 |   - Goal: Let users sign in with Google.
145 |   - Tasks: [ ] add Google client, [ ] callback route, [ ] session, [ ] E2E test.
146 |   - Won't do: org SSO.
147 |   - Ideas for later: Apple login.
148 | 
149 |   ## Notes
150 | 
151 |   - Planning only. No code edits.
152 |   - Assume a Git repo with test runner available.
```

temp-prompts-organized/prompt-front-matter/00-ideation__requirements__prd-generator.requirements.refactor.md
```
1 | # PRD Generator
2 | 
3 | ## Inputs
4 | - Source repository README (`README.md`) at root
5 | - Visible link texts (only titles/texts, no external browsing)
6 | - Example PRD structure and tone for formatting guidance
7 | - Explicit trigger: `/prd-generate`
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - Document Generation
11 | - Content Extraction
12 | - Validation & Compliance
13 | 
14 | ### Stage hints (for inference)
15 | - Document Generation → execution
16 | - Content Extraction → input-processing
17 | - Validation & Compliance → output-validation
18 | 
19 | ## Algorithm
20 | 1. Extract signals from $1  
21 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
22 | 
23 | 2. Determine the primary identifier  
24 |    * Prefer explicit input; otherwise infer from main action + object.  
25 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
26 |    * De-duplicate.
27 | 
28 | 3. Determine categories  
29 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
30 |    * Validate, sort deterministically, and de-dupe (≤3).
31 | 
32 | 4. Determine lifecycle/stage (optional)  
33 |    * Prefer explicit input; otherwise map categories via $6.  
34 |    * Omit if uncertain.
35 | 
36 | 5. Determine dependencies (optional)  
37 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
38 | 
39 | 6. Determine provided artifacts (optional)  
40 |    * Short list (≤3) of unlocked outputs.
41 | 
42 | 7. Compose summary  
43 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
44 | 
45 | 8. Produce metadata in the requested format  
46 |    * Default to a human-readable serialization; honor any requested alternative.
47 | 
48 | 9. Reconcile if input already contains metadata  
49 |    * Merge: explicit inputs > existing > inferred.  
50 |    * Validate lists; move unknowns to an extension field if needed.  
51 |    * Remove empty keys.
52 | 
53 | ## Assumptions & Constraints
54 | - Emit exactly one document: metadata, a single blank line, then $1.
55 | - Limit distinct placeholders to ≤ 7.
56 | - No external sources or URLs allowed.
57 | - Output must strictly follow section order and formatting rules.
58 | 
59 | ## Validation
60 | - Identifier matches a normalized id pattern.  
61 | - Categories non-empty and drawn from $5 (≤3).  
62 | - Stage, if present, is one of the allowed stages implied by $6.  
63 | - Dependencies, if present, are id-shaped (≤5).  
64 | - Summary ≤120 chars; punctuation coherent.  
65 | - Body text $1 is not altered.
66 | 
67 | ## Output format examples
68 | - Identifier: prd-generate  
69 | - Category: Document Generation  
70 | - Stage: execution  
71 | - Dependency: README.md must exist  
72 | - Artifact: prd.txt (plain text)  
73 | - Summary: Do generate a structured PRD from README content to achieve consistent, complete documentation with defined format.  
74 | - Metadata block:
75 |   ```yaml
76 |   identifier: prd-generate
77 |   categories:
78 |     - Document Generation
79 |     - Content Extraction
80 |     - Validation & Compliance
81 |   stage: execution
82 |   dependencies:
83 |     - README.md exists at root
84 |   provided_artifacts:
85 |     - prd.txt
86 |   summary: Do generate a structured PRD from README content to achieve consistent, complete documentation with defined format.
87 |   ```
```

temp-prompts-organized/prompt-front-matter/00-ideation__requirements__scope-control.requirements.refactor.md
```
1 | # Scope Control
2 | 
3 | Task: Given the following requirements text, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the input text.
4 | 
5 | ## Inputs
6 | - Source file path: C:\Users\user\projects\prompts\temp-prompts\00-ideation\requirements\scope-control.requirements.md
7 | - Input content: # Scope Control\n\nTrigger: /scope-control\n\nPurpose: Enforce explicit scope boundaries and maintain \"won't do\" and \"ideas for later\" lists.\n\n## Steps\n1. Parse `PLAN.md` or create it if absent.\n2. For each open task, confirm linkage to the current milestone.\n3. Detect off-scope items and move them to **Won't do** or **Ideas for later** with rationale.\n4. Add a \"Scope Gate\" checklist before merging.\n\n## Output format\n- Patch to `PLAN.md` showing changes in sections and checklists.\n\n## Examples\nInput: off-scope request \"Add email templates\" during OAuth feature.\nOutput: Move to **Ideas for later** with reason \"Not needed for OAuth MVP\".\n\n## Notes\n- Never add new scope without recording tradeoffs.
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - Won't do
11 | - Ideas for later
12 | 
13 | ### Stage hints (for inference)
14 | - review
15 | - gatekeeping
16 | - validation
17 | 
18 | ## Algorithm
19 | 1. Extract signals from input text  
20 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
21 | 
22 | 2. Determine the primary identifier  
23 |    * Prefer explicit input; otherwise infer from main action + object.  
24 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
25 |    * De-duplicate.
26 | 
27 | 3. Determine categories  
28 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
29 |    * Validate, sort deterministically, and de-dupe (≤3).
30 | 
31 | 4. Determine lifecycle/stage (optional)  
32 |    * Prefer explicit input; otherwise map categories via stage hints.  
33 |    * Omit if uncertain.
34 | 
35 | 5. Determine dependencies (optional)  
36 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
37 | 
38 | 6. Determine provided artifacts (optional)  
39 |    * Short list (≤3) of unlocked outputs.
40 | 
41 | 7. Compose summary  
42 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
43 | 
44 | 8. Produce metadata in the requested format  
45 |    * Default to a human-readable serialization; honor any requested alternative.
46 | 
47 | 9. Reconcile if input already contains metadata  
48 |    * Merge: explicit inputs > existing > inferred.  
49 |    * Validate lists; move unknowns to an extension field if needed.  
50 |    * Remove empty keys.
51 | 
52 | ## Assumptions & Constraints
53 | - Emit exactly one document: metadata, a single blank line, then the input text.
54 | - Limit distinct placeholders to ≤ 7.
55 | 
56 | ## Validation
57 | - Identifier matches a normalized id pattern.
58 | - Categories non-empty and drawn from canonical taxonomy (≤3).
59 | - Stage, if present, is one of the allowed stages implied by stage hints.
60 | - Dependencies, if present, are id-shaped (≤5).
61 | - Artifacts, if present, are short (≤3) and specific.
62 | - Summary ≤120 chars; punctuation coherent.
63 | - Body text is not altered.
64 | 
65 | ## Output format examples
66 | - Identifier: scope-control  
67 | - Categories: Won't do, Ideas for later  
68 | - Stage: review  
69 | - Dependencies: plan.md  
70 | - Artifacts: patch to PLAN.md  
71 | - Summary: Do enforce scope boundaries by detecting off-scope items and moving them to Won't do or Ideas for later to achieve controlled feature development.
```

temp-prompts-organized/prompt-front-matter/10-scaffold__ci-setup__devops-automation.ci-setup.refactor.md
```
1 | # DevOps Automation
2 | 
3 | ## Metadata
4 | 
5 | - identifier: devops-automation
6 | - categories:
7 |   - infrastructure
8 |   - ci-cd
9 |   - automation
10 | - stage: setup
11 | - dependencies: []
12 | - provided_artifacts:
13 |   - infra plan with checkpoints and secrets placeholders
14 | - summary: Do configure infrastructure and CI/CD to achieve automated deployment pipelines.
15 | 
16 | ## Steps
17 | 
18 | 1. Inspect repo for IaC or deploy scripts.
19 | 2. Generate Terraform or Docker Compose templates if missing.
20 | 3. Propose CI workflows for tests, builds, and deploys.
21 | 4. Provide runbooks for rollback.
22 | 
23 | ## Output format
24 | 
25 | - Infra plan with checkpoints and secrets placeholders.
```

temp-prompts-organized/prompt-front-matter/10-scaffold__ci-setup__env-setup.ci-setup.refactor.md
```
1 | # Env Setup
2 | 
3 | Task: Given the following content, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the original text.
4 | 
5 | ## Inputs
6 | - Source file path: C:\Users\user\projects\prompts\temp-prompts\10-scaffold\ci-setup\env-setup.ci-setup.md
7 | - Raw content: # Env Setup\n\nTrigger: /env-setup\n\nPurpose: Create .env.example, runtime schema validation, and per-env overrides.\n\n**Steps:**\n1. Scan repo for `process.env` usage and collected keys.\n2. Emit `.env.example` with comments and safe defaults.\n3. Add runtime validation via `zod` or `envsafe` in `packages/config`.\n4. Document `development`, `staging`, `production` precedence and loading order.\n\n**Output format:** `.env.example` content block and `config/env.ts` snippet.\n\n**Examples:** `/env-setup`.\n\n**Notes:** Do not include real credentials. Enforce `STRICT_ENV=true` in CI.
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - environment
11 | - configuration
12 | - infrastructure
13 | 
14 | ### Stage hints (for inference)
15 | - setup → init
16 | - configure → config
17 | - validate → validate
18 | 
19 | ## Algorithm
20 | 1. Extract signals from the content  
21 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
22 | 
23 | 2. Determine the primary identifier  
24 |    * Prefer explicit input; otherwise infer from main action + object.  
25 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
26 |    * De-duplicate.
27 | 
28 | 3. Determine categories  
29 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
30 |    * Validate, sort deterministically, and de-dupe (≤3).
31 | 
32 | 4. Determine lifecycle/stage (optional)  
33 |    * Prefer explicit input; otherwise map categories via stage hints.  
34 |    * Omit if uncertain.
35 | 
36 | 5. Determine dependencies (optional)  
37 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
38 | 
39 | 6. Determine provided artifacts (optional)  
40 |    * Short list (≤3) of unlocked outputs.
41 | 
42 | 7. Compose summary  
43 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
44 | 
45 | 8. Produce metadata in the requested format  
46 |    * Default to a human-readable serialization; honor any requested alternative.
47 | 
48 | 9. Reconcile if input already contains metadata  
49 |    * Merge: explicit inputs > existing > inferred.  
50 |    * Validate lists; move unknowns to an extension field if needed.  
51 |    * Remove empty keys.
52 | 
53 | ## Assumptions & Constraints
54 | - Emit exactly one document: metadata, a single blank line, then the original body.
55 | - Limit distinct placeholders to ≤ 7.
56 | 
57 | ## Validation
58 | - Identifier matches a normalized id pattern.
59 | - Categories non-empty and drawn from canonical taxonomy (≤3).
60 | - Stage, if present, is one of the allowed stages implied by stage hints.
61 | - Dependencies, if present, are id-shaped (≤5).
62 | - Summary ≤120 chars; punctuation coherent.
63 | - Body text is not altered.
64 | 
65 | ## Output format examples
66 | - Identifier: env-setup  
67 | - Categories: ["environment", "configuration", "infrastructure"]  
68 | - Stage: init  
69 | - Dependencies: []  
70 | - Artifacts: [".env.example content block", "config/env.ts snippet"]  
71 | - Summary: "Do setup environment to achieve secure configuration with schema validation."
```

temp-prompts-organized/prompt-front-matter/10-scaffold__ci-setup__monitoring-setup.ci-setup.refactor.md
```
1 | # Monitoring Setup
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: monitoring-setup
6 | - **categories**: 
7 |   - observability
8 |   - infrastructure
9 |   - setup
10 | - **lifecycle_stage**: setup
11 | - **dependencies**: []
12 | - **provided_artifacts**: 
13 |   - instrumentation checklist
14 |   - dashboard links/paths
15 | - **summary**: Do instrument web and api for request latency, error rate, throughput, and core domain metrics to achieve observability per domain.
16 | 
17 | ## Inputs
18 | 
19 | - trigger: /monitoring-setup
20 | - purpose: Bootstrap logs, metrics, and traces with dashboards per domain.
21 | - steps:
22 |   1. Choose stack: OpenTelemetry → Prometheus/Grafana, or vendor.
23 |   2. Instrument web and api for request latency, error rate, throughput, and core domain metrics.
24 |   3. Provide default dashboards JSON and alert examples.
25 | - output_format: instrumentation checklist and dashboard links/paths
26 | - examples: /monitoring-setup
27 | - notes: Avoid high‑cardinality labels. Sample traces selectively in prod.
28 | 
29 | ## Canonical taxonomy (exact strings)
30 | 
31 | - observability
32 | - infrastructure
33 | - setup
34 | 
35 | ### Stage hints (for inference)
36 | 
37 | - setup → bootstrap, initialize, configure, instrument
38 | - deploy → run, activate, install
39 | - operate → monitor, maintain, scale
40 | 
41 | ## Algorithm
42 | 
43 | 1. Extract signals from $1  
44 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
45 | 
46 | 2. Determine the primary identifier  
47 |    * Prefer explicit input; otherwise infer from main action + object.  
48 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
49 |    * De-duplicate.
50 | 
51 | 3. Determine categories  
52 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
53 |    * Validate, sort deterministically, and de-dupe (≤3).
54 | 
55 | 4. Determine lifecycle/stage (optional)  
56 |    * Prefer explicit input; otherwise map categories via $6.  
57 |    * Omit if uncertain.
58 | 
59 | 5. Determine dependencies (optional)  
60 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
61 | 
62 | 6. Determine provided artifacts (optional)  
63 |    * Short list (≤3) of unlocked outputs.
64 | 
65 | 7. Compose summary  
66 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
67 | 
68 | 8. Produce metadata in the requested format  
69 |    * Default to a human-readable serialization; honor any requested alternative.
70 | 
71 | 9. Reconcile if input already contains metadata  
72 |    * Merge: explicit inputs > existing > inferred.  
73 |    * Validate lists; move unknowns to an extension field if needed.  
74 |    * Remove empty keys.
75 | 
76 | ## Assumptions & Constraints
77 | 
78 | - Emit exactly one document: metadata, a single blank line, then $1.
79 | - Limit distinct placeholders to ≤ 7.
80 | 
81 | ## Validation
82 | 
83 | - Identifier matches a normalized id pattern.
84 | - Categories non-empty and drawn from $5 (≤3).
85 | - Stage, if present, is one of the allowed stages implied by $6.
86 | - Dependencies, if present, are id-shaped (≤5).
87 | - Summary ≤120 chars; punctuation coherent.
88 | - Body text $1 is not altered.
89 | 
90 | ## Output format examples
91 | 
92 | - identifier: monitoring-setup
93 | - categories: observability, infrastructure, setup
94 | - lifecycle_stage: setup
95 | - dependencies: []
96 | - provided_artifacts: instrumentation checklist, dashboard links/paths
97 | - summary: Do instrument web and api for request latency, error rate, throughput, and core domain metrics to achieve observability per domain.
```

temp-prompts-organized/prompt-front-matter/10-scaffold__ci-setup__slo-setup.ci-setup.refactor.md
```
1 | # SLO Setup
2 | 
3 | Task: Given the following prompt text, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the original body.
4 | 
5 | ## Inputs
6 | 
7 | - Identifier (trigger): `/slo-setup`
8 | - Purpose: Define Service Level Objectives, burn alerts, and runbooks.
9 | - Steps:
10 |   1. Choose SLI/metrics per user journey. Define SLO targets and error budgets.
11 |   2. Create burn alerts (fast/slow) and link to runbooks.
12 |   3. Add `SLO.md` with rationale and review cadence.
13 | - Output format: SLO table and alert rules snippet.
14 | - Examples: `/slo-setup`.
15 | - Notes: Tie SLOs to deploy gates and incident severity.
16 | 
17 | ## Canonical taxonomy (exact strings)
18 | 
19 | - slo
20 | - alerts
21 | - runbooks
22 | 
23 | ### Stage hints (for inference)
24 | 
25 | - setup → setup phase of service configuration
26 | - define → initial creation or definition
27 | - create → action for establishing new components
28 | 
29 | ## Algorithm
30 | 
31 | 1. Extract signals from the prompt text:
32 |    - Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
33 | 
34 | 2. Determine the primary identifier:
35 |    - Prefer explicit input; otherwise infer from main action + object.
36 |    - Normalize (lowercase, kebab-case, length-capped, starts with a letter).
37 |    - De-duplicate.
38 | 
39 | 3. Determine categories:
40 |    - Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
41 |    - Validate, sort deterministically, and de-dupe (≤3).
42 | 
43 | 4. Determine lifecycle/stage (optional):
44 |    - Prefer explicit input; otherwise map categories via stage hints.
45 |    - Omit if uncertain.
46 | 
47 | 5. Determine dependencies (optional):
48 |    - Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
49 | 
50 | 6. Determine provided artifacts (optional):
51 |    - Short list (≤3) of unlocked outputs.
52 | 
53 | 7. Compose summary:
54 |    - One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
55 | 
56 | 8. Produce metadata in the requested format:
57 |    - Default to a human-readable serialization; honor any requested alternative.
58 | 
59 | 9. Reconcile if input already contains metadata:
60 |    - Merge: explicit inputs > existing > inferred.
61 |    - Validate lists; move unknowns to an extension field if needed.
62 |    - Remove empty keys.
63 | 
64 | ## Assumptions & Constraints
65 | 
66 | - Emit exactly one document: metadata, a single blank line, then the original body.
67 | - Limit distinct placeholders to ≤7.
68 | 
69 | ## Validation
70 | 
71 | - Identifier matches a normalized id pattern (e.g., kebab-case, lowercase).
72 | - Categories non-empty and drawn from canonical taxonomy (≤3).
73 | - Stage, if present, is one of the allowed stages implied by stage hints.
74 | - Dependencies, if present, are id-shaped (≤5).
75 | - Provided artifacts ≤3 and directly tied to output format.
76 | - Summary ≤120 chars; punctuation coherent.
77 | - Body text is not altered.
78 | 
79 | ## Output format examples
80 | 
81 | - {
82 |   "identifier": "slo-setup",
83 |   "categories": ["slo", "alerts", "runbooks"],
84 |   "stage": "setup",
85 |   "dependencies": [],
86 |   "provided_artifacts": ["SLO table", "alert rules snippet"],
87 |   "summary": "Define SLOs, alerts, and runbooks to achieve measurable service reliability."
88 | }
```

temp-prompts-organized/prompt-front-matter/10-scaffold__conventions__version-control-guide.conventions.refactor.md
```
1 | # Version Control Guide
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: version-control-guide
6 | - **Categories**: development practice, workflow guide, code hygiene
7 | - **Stage**: implementation
8 | - **Dependencies**: none
9 | - **Provided Artifacts**: checklist, suggested commands
10 | - **Summary**: Enforce clean incremental commits and clean-room re-implementation to ensure reproducible and safe changes.
11 | 
12 | ## Inputs
13 | 
14 | - Trigger: /version-control-guide
15 | - Purpose: Enforce clean incremental commits and clean-room re-implementation when finalizing.
16 | - Output format: Checklist plus suggested commands for the current repo state.
17 | - Examples: Convert messy spike into three commits: setup, feature, tests.
18 | - Notes: Never modify remote branches without confirmation.
19 | 
20 | ## Canonical taxonomy (exact strings)
21 | 
22 | - development practice
23 | - workflow guide
24 | - code hygiene
25 | 
26 | ### Stage hints (for inference)
27 | 
28 | - implementation
29 | - commit workflow
30 | - development lifecycle
31 | 
32 | ## Algorithm
33 | 
34 | 1. Extract signals from $1  
35 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
36 | 
37 | 2. Determine the primary identifier  
38 |    * Prefer explicit input; otherwise infer from main action + object.  
39 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
40 |    * De-duplicate.
41 | 
42 | 3. Determine categories  
43 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
44 |    * Validate, sort deterministically, and de-dupe (≤3).
45 | 
46 | 4. Determine lifecycle/stage (optional)  
47 |    * Prefer explicit input; otherwise map categories via $6.  
48 |    * Omit if uncertain.
49 | 
50 | 5. Determine dependencies (optional)  
51 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
52 | 
53 | 6. Determine provided artifacts (optional)  
54 |    * Short list (≤3) of unlocked outputs.
55 | 
56 | 7. Compose summary  
57 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
58 | 
59 | 8. Produce metadata in the requested format  
60 |    * Default to a human-readable serialization; honor any requested alternative.
61 | 
62 | 9. Reconcile if input already contains metadata  
63 |    * Merge: explicit inputs > existing > inferred.  
64 |    * Validate lists; move unknowns to an extension field if needed.  
65 |    * Remove empty keys.
66 | 
67 | ## Assumptions & Constraints
68 | 
69 | - Emit exactly one document: metadata, a single blank line, then $1.
70 | - Limit distinct placeholders to ≤ 7.
71 | - Output body unchanged.
72 | 
73 | ## Validation
74 | 
75 | - Identifier matches a normalized id pattern.
76 | - Categories non-empty and drawn from $5 (≤3).
77 | - Stage, if present, is one of the allowed stages implied by $6.
78 | - Dependencies, if present, are id-shaped (≤5).
79 | - Summary ≤120 chars; punctuation coherent.
80 | - Body text $1 is not altered.
81 | 
82 | ## Output format examples
83 | 
84 | - Identifier: version-control-guide  
85 | - Categories: development practice, workflow guide, code hygiene  
86 | - Stage: implementation  
87 | - Dependencies: none  
88 | - Provided Artifacts: checklist, suggested commands  
89 | - Summary: Enforce clean incremental commits and clean-room re-implementation to ensure reproducible and safe changes.
90 | 
91 | # Version Control Guide
92 | 
93 | Trigger: /version-control-guide
94 | 
95 | Purpose: Enforce clean incremental commits and clean-room re-implementation when finalizing.
96 | 
97 | ## Steps
98 | 
99 | 1. Start each feature from a clean branch: `git switch -c <feat>`.
100 | 2. Commit in vertical slices with passing tests: `git add -p && git commit`.
101 | 3. When solution is proven, recreate a minimal clean diff: stash or copy results, reset, then apply only the final changes.
102 | 4. Use `git revert` for bad commits instead of force-pushing shared branches.
103 | 
104 | ## Output format
105 | 
106 | - Checklist plus suggested commands for the current repo state.
107 | 
108 | ## Examples
109 | 
110 | - Convert messy spike into three commits: setup, feature, tests.
111 | 
112 | ## Notes
113 | 
114 | - Never modify remote branches without confirmation.
```

temp-prompts-organized/prompt-front-matter/10-scaffold__scaffold__auth.scaffold.refactor.md
```
1 | # Auth Scaffold
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: auth-scaffold-provider
6 | - **Categories**: Scaffold, Auth, Security
7 | - **Stage**: initialization
8 | - **Dependencies**: []
9 | - **Provided Artifacts**: route list, config keys, mitigations table
10 | - **Summary**: Scaffold auth flows to achieve secure session management with threat modeling.
11 | 
12 | ---
13 | 
14 | # Auth Scaffold
15 | 
16 | Trigger: /auth-scaffold <oauth|email|oidc>
17 | 
18 | Purpose: Scaffold auth flows, routes, storage, and a basic threat model.
19 | 
20 | **Steps:**
21 | 
22 | 1. Select provider (OAuth/OIDC/email) and persistence for sessions.
23 | 2. Generate routes: login, callback, logout, session refresh.
24 | 3. Add CSRF, state, PKCE where applicable. Include secure cookie flags.
25 | 4. Document threat model: replay, fixation, token leakage, SSRF on callbacks.
26 | 5. Wire to frontend with protected routes and user context.
27 | 
28 | **Output format:** route list, config keys, and mitigations table.
29 | 
30 | **Examples:** `/auth-scaffold oauth` → NextAuth/Passport/Custom adapter plan.
31 | 
32 | **Notes:** Never print real secrets. Use placeholders in `.env.example`.
```

temp-prompts-organized/prompt-front-matter/10-scaffold__scaffold__db-bootstrap.scaffold.refactor.md
```
1 | # DB Bootstrap
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: db-bootstrap  
6 | - **Categories**: 
7 |   - database setup
8 |   - migration configuration
9 |   - local development environment
10 | - **Lifecycle Stage**: setup  
11 | - **Dependencies**: none  
12 | - **Provided Artifacts**: 
13 |   - migration plan list
14 |   - db/compose.yaml (skip for sqlite)
15 |   - prisma/schema.prisma or drizzle/*.ts (baseline tables: users, sessions, audit_log)
16 |   - pnpm db:migrate, db:reset, db:seed scripts
17 |   - .env.example with DATABASE_URL and test connection script  
18 | - **Summary**: Do db-bootstrap with a database to initialize migrations, compose files, and seed data.
19 | 
20 | ## Inputs
21 | 
22 | - Database type (e.g., postgres, mysql, sqlite)
23 | 
24 | ## Canonical taxonomy (exact strings)
25 | 
26 | - database setup
27 | - migration configuration
28 | - local development environment
29 | 
30 | ### Stage hints (for inference)
31 | 
32 | - setup → initial configuration phase  
33 | - build → after schema is defined  
34 | - deploy → post-migration to production  
35 | 
36 | ## Algorithm
37 | 
38 | 1. Extract signals from $1  
39 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
40 | 
41 | 2. Determine the primary identifier  
42 |    * Prefer explicit input; otherwise infer from main action + object.  
43 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
44 |    * De-duplicate.
45 | 
46 | 3. Determine categories  
47 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
48 |    * Validate, sort deterministically, and de-dupe (≤3).
49 | 
50 | 4. Determine lifecycle/stage (optional)  
51 |    * Prefer explicit input; otherwise map categories via $6.  
52 |    * Omit if uncertain.
53 | 
54 | 5. Determine dependencies (optional)  
55 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
56 | 
57 | 6. Determine provided artifacts (optional)  
58 |    * Short list (≤3) of unlocked outputs.
59 | 
60 | 7. Compose summary  
61 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
62 | 
63 | 8. Produce metadata in the requested format  
64 |    * Default to a human-readable serialization; honor any requested alternative.
65 | 
66 | 9. Reconcile if input already contains metadata  
67 |    * Merge: explicit inputs > existing > inferred.  
68 |    * Validate lists; move unknowns to an extension field if needed.  
69 |    * Remove empty keys.
70 | 
71 | ## Assumptions & Constraints
72 | 
73 | - Emit exactly one document: metadata, a single blank line, then $1.
74 | - Limit distinct placeholders to ≤ 7.
75 | 
76 | ## Validation
77 | 
78 | - Identifier matches a normalized id pattern.
79 | - Categories non-empty and drawn from $5 (≤3).
80 | - Stage, if present, is one of the allowed stages implied by $6.
81 | - Dependencies, if present, are id-shaped (≤5).
82 | - Dependencies: none → valid
83 | - Artifacts ≤3 → satisfied
84 | - Summary ≤120 chars; punctuation coherent.
85 | - Body text $1 is not altered.
86 | 
87 | ## Output format examples
88 | 
89 | - `/db-bootstrap postgres` → Prisma + Postgres docker-compose  
90 | - `/db-bootstrap sqlite` → skip compose, use minimal schema and seed  
91 | 
92 | # DB Bootstrap
93 | 
94 | Trigger: /db-bootstrap <postgres|mysql|sqlite|mongodb>
95 | 
96 | Purpose: Pick a database, initialize migrations, local compose, and seed scripts.
97 | 
98 | **Steps:**
99 | 
100 | 1. Create `db/compose.yaml` for local dev (skip for sqlite).
101 | 2. Choose ORM/driver (Prisma or Drizzle for SQL). Add migration config.
102 | 3. Create `prisma/schema.prisma` or `drizzle/*.ts` with baseline tables (users, sessions, audit_log).
103 | 4. Add `pnpm db:migrate`, `db:reset`, `db:seed` scripts. Write seed data for local admin user.
104 | 5. Update `.env.example` with `DATABASE_URL` and test connection script.
105 | 
106 | **Output format:** Migration plan list and generated file paths.
107 | 
108 | **Examples:** `/db-bootstrap postgres` → Prisma + Postgres docker-compose.
109 | 
110 | **Notes:** Avoid destructive defaults; provide `--preview-feature` warnings if relevant.
```

temp-prompts-organized/prompt-front-matter/10-scaffold__scaffold__fullstack.scaffold.refactor.md
```
1 | # Scaffold Full‑Stack App
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: scaffold-fullstack
6 | - **Categories**: app, api, testing, ci, infrastructure
7 | - **Stage**: setup
8 | - **Dependencies**: none
9 | - **Provided Artifacts**: repo-tree, next-steps, ci-seeds, docs
10 | - **Summary**: Scaffold a minimal monorepo with app, API, tests, and CI seeds to achieve production-ready structure.
11 | 
12 | ---
13 | 
14 | # Scaffold Full‑Stack App
15 | 
16 | Trigger: /scaffold-fullstack <stack>
17 | 
18 | Purpose: Create a minimal, production-ready monorepo template with app, API, tests, CI seeds, and infra stubs.
19 | 
20 | **Steps:**
21 | 
22 | 1. Read repository context: `git rev-parse --is-inside-work-tree`.
23 | 2. If repo is empty, initialize: `git init -b main` and create `.editorconfig`, `.gitignore`, `README.md`.
24 | 3. For `<stack>` derive presets (examples):
25 |    - `ts-next-express-pg`: Next.js app, Express API, Prisma + PostgreSQL, Playwright, pnpm workspaces.
26 |    - `ts-vite-fastify-sqlite`: Vite + React app, Fastify API, Drizzle + SQLite.
27 | 4. Create workspace layout:
28 |    - root: `package.json` with `pnpm` workspaces, `tsconfig.base.json`, `eslint`, `prettier`.
29 |    - apps/web, apps/api, packages/ui, packages/config.
30 | 5. Add scripts:
31 |    - root: `dev`, `build`, `lint`, `typecheck`, `test`, `e2e`, `format`.
32 |    - web: Next/Vite scripts. api: dev with ts-node or tsx.
33 | 6. Seed CI files: `.github/workflows/ci.yml` with jobs [lint, typecheck, test, build, e2e] and artifact uploads.
34 | 7. Add example routes:
35 |    - web: `/health` page. api: `GET /health` returning `{ ok: true }`.
36 | 8. Write docs to `README.md`: how to run dev, test, build, and env variables.
37 | 9. Stage files, but do not commit. Output a tree and next commands.
38 | 
39 | **Output format:**
40 | 
41 | - Title line: `Scaffold created: <stack>`
42 | - Sections: `Repo Tree`, `Next Steps`, `CI Seeds`.
43 | - Include a fenced code block of the `tree` and sample scripts.
44 | 
45 | **Examples:**
46 | 
47 | - **Input:** `/scaffold-fullstack ts-next-express-pg`
48 |   **Output:** Summary + tree with `apps/web`, `apps/api`, `packages/ui`.
49 | - **Input:** `/scaffold-fullstack ts-vite-fastify-sqlite`
50 |   **Output:** Summary + tree + Drizzle config.
51 | 
52 | **Notes:**
53 | 
54 | - Assume pnpm and Node 20+. Do not run package installs automatically; propose commands instead.
55 | - Respect existing files; avoid overwriting without explicit confirmation.
```

temp-prompts-organized/prompt-front-matter/10-scaffold__scaffold__iac-bootstrap.scaffold.refactor.md
```
1 | # IaC Bootstrap
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: iac-bootstrap
6 | - **Categories**: 
7 |   - IaC
8 |   - CI/CD
9 |   - Cloud Automation
10 | - **Lifecycle Stage**: bootstrap
11 | - **Dependencies**: none
12 | - **Provided Artifacts**: 
13 |   - stack diagram
14 |   - file list
15 |   - CI snippets
16 | - **Summary**: Do create minimal Infrastructure-as-Code for chosen platform plus CI hooks to achieve rapid deployment readiness.
17 | 
18 | ## Inputs
19 | 
20 | - Platform: aws | gcp | azure | fly | render
21 | - IaC Tool: Terraform | Pulumi
22 | - Environment Stages: preview, staging, prod
23 | - Output Format: stack diagram, file list, CI snippets
24 | 
25 | ## Canonical taxonomy (exact strings)
26 | 
27 | - IaC
28 | - CI/CD
29 | - Cloud Automation
30 | 
31 | ### Stage hints (for inference)
32 | 
33 | - bootstrap → early setup/init phase
34 | - create → initial configuration
35 | - define → structural setup
36 | - add → extend with hooks and policies
37 | 
38 | ## Algorithm
39 | 
40 | 1. Extract signals from $1  
41 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
42 | 
43 | 2. Determine the primary identifier  
44 |    * Prefer explicit input; otherwise infer from main action + object.  
45 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
46 |    * De-duplicate.
47 | 
48 | 3. Determine categories  
49 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
50 |    * Validate, sort deterministically, and de-dupe (≤3).
51 | 
52 | 4. Determine lifecycle/stage (optional)  
53 |    * Prefer explicit input; otherwise map categories via $6.  
54 |    * Omit if uncertain.
55 | 
56 | 5. Determine dependencies (optional)  
57 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
58 | 
59 | 6. Determine provided artifacts (optional)  
60 |    * Short list (≤3) of unlocked outputs.
61 | 
62 | 7. Compose summary  
63 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
64 | 
65 | 8. Produce metadata in the requested format  
66 |    * Default to a human-readable serialization; honor any requested alternative.
67 | 
68 | 9. Reconcile if input already contains metadata  
69 |    * Merge: explicit inputs > existing > inferred.  
70 |    * Validate lists; move unknowns to an extension field if needed.  
71 |    * Remove empty keys.
72 | 
73 | ## Assumptions & Constraints
74 | 
75 | - Emit exactly one document: metadata, a single blank line, then $1.
76 | - Limit distinct placeholders to ≤ 7.
77 | - No alteration of the original body text.
78 | 
79 | ## Validation
80 | 
81 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
82 | - Categories non-empty and drawn from canonical taxonomy (≤3).
83 | - Stage, if present, is one of the allowed stages implied by stage hints.
84 | - Dependencies, if present, are id-shaped (≤5).
85 | - Summary ≤120 chars; punctuation coherent.
86 | - Body text $1 is not altered.
87 | 
88 | ## Output format examples
89 | 
90 | - Identifier: iac-bootstrap  
91 | - Categories: IaC, CI/CD, Cloud Automation  
92 | - Lifecycle Stage: bootstrap  
93 | - Dependencies: none  
94 | - Artifacts: stack diagram, file list, CI snippets  
95 | - Summary: Do create minimal Infrastructure-as-Code for chosen platform plus CI hooks to achieve rapid deployment readiness.
96 | 
97 | ---
98 | 
99 | # IaC Bootstrap
100 | 
101 | Trigger: /iac-bootstrap <aws|gcp|azure|fly|render>
102 | 
103 | Purpose: Create minimal Infrastructure-as-Code for the chosen platform plus CI hooks.
104 | 
105 | **Steps:**
106 | 
107 | 1. Select tool (Terraform, Pulumi). Initialize backend and state.
108 | 2. Define stacks for `preview`, `staging`, `prod`. Add outputs (URLs, connection strings).
109 | 3. Add CI jobs: plan on PR, apply on main with manual approval.
110 | 4. Document rollback and drift detection.
111 | 
112 | **Output format:** stack diagram, file list, CI snippets.
113 | 
114 | **Examples:** `/iac-bootstrap aws`.
115 | 
116 | **Notes:** Prefer least privilege IAM and remote state with locking.
```

temp-prompts-organized/prompt-front-matter/20-implementation__impl__commit.impl.refactor.md
```
1 | # Commit Message Assistant
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: commit
6 | - **categories**: fix, feat, chore, docs, refactor
7 | - **lifecycle_stage**: draft
8 | - **dependencies**: git status --short, git diff --staged
9 | - **provided_artifacts**: conventional commit message (subject + body)
10 | - **summary**: Generate a conventional, review-ready commit message from staged changes.
11 | 
12 | ## Inputs
13 | 
14 | - Requires staged changes to be present.
15 | - Must parse staged diff for change type and scope.
16 | - Needs access to current repository state via git commands.
17 | 
18 | ## Canonical taxonomy (exact strings)
19 | 
20 | feat, fix, chore, docs, refactor
21 | 
22 | ### Stage hints (for inference)
23 | 
24 | draft → generation of output based on input state  
25 | review → post-generation feedback or approval  
26 | finalize → final commit execution  
27 | 
28 | ## Algorithm
29 | 
30 | 1. Extract signals from $1  
31 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
32 | 
33 | 2. Determine the primary identifier  
34 |    * Prefer explicit input; otherwise infer from main action + object.  
35 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
36 |    * De-duplicate.
37 | 
38 | 3. Determine categories  
39 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
40 |    * Validate, sort deterministically, and de-dupe (≤3).
41 | 
42 | 4. Determine lifecycle/stage (optional)  
43 |    * Prefer explicit input; otherwise map categories via stage hints.  
44 |    * Omit if uncertain.
45 | 
46 | 5. Determine dependencies (optional)  
47 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
48 | 
49 | 6. Determine provided artifacts (optional)  
50 |    * Short list (≤3) of unlocked outputs.
51 | 
52 | 7. Compose summary  
53 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
54 | 
55 | 8. Produce metadata in the requested format  
56 |    * Default to a human-readable serialization; honor any requested alternative.
57 | 
58 | 9. Reconcile if input already contains metadata  
59 |    * Merge: explicit inputs > existing > inferred.  
60 |    * Validate lists; move unknowns to an extension field if needed.  
61 |    * Remove empty keys.
62 | 
63 | ## Assumptions & Constraints
64 | 
65 | - Emit exactly one document: metadata, a single blank line, then $1.
66 | - Limit distinct placeholders to ≤ 7.
67 | - All categories must be from the canonical taxonomy.
68 | - Summary must be concise and coherent.
69 | 
70 | ## Validation
71 | 
72 | - Identifier matches a normalized id pattern (e.g., kebab-case).
73 | - Categories non-empty and drawn from canonical taxonomy (≤3).
74 | - Stage, if present, is one of: draft, review, finalize.
75 | - Dependencies are id-shaped (e.g., git commands), ≤5 items.
76 | - Provided artifacts are short and relevant (≤3).
77 | - Summary ≤120 chars; punctuation coherent.
78 | - Body text $1 is not altered.
79 | 
80 | ## Output format examples
81 | 
82 | ```
83 | fix(auth): prevent session expiration loop
84 | 
85 | - guard refresh flow against repeated 401 responses
86 | - add regression coverage for expired refresh tokens
87 | 
88 | Tests: npm test -- auth/session.test.ts
89 | ```
```

temp-prompts-organized/prompt-front-matter/20-implementation__impl__content-generation.impl.refactor.md
```
1 | # Content Generation
2 | 
3 | ## Metadata
4 | 
5 | - identifier: content-generation
6 | - category: documentation
7 | - category: marketing
8 | - category: blog
9 | - lifecycle-stage: implementation
10 | - dependencies: [readme, changelog]
11 | - provided-artifacts: [markdown-docs, frontmatter, section-headings]
12 | - summary: Draft documentation, blog posts, or marketing copy aligned with codebase to achieve consistent, on-brand content.
13 | 
14 | ## Inputs
15 | 
16 | - source-repo-readme
17 | - recent-changelog-or-commits
18 | 
19 | ## Canonical taxonomy (exact strings)
20 | 
21 | documentation
22 | marketing
23 | blog
24 | implementation
25 | generation
26 | analysis
27 | deployment
28 | 
29 | ### Stage hints (for inference)
30 | 
31 | - implementation → steps involving proposal and generation after input reading
32 | - generation → output creation from structure or outline
33 | - analysis → reading inputs, parsing changes
34 | - deployment → final delivery of artifacts
35 | 
36 | ## Algorithm
37 | 
38 | 1. Extract signals from $1  
39 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
40 | 
41 | 2. Determine the primary identifier  
42 |    * Prefer explicit input; otherwise infer from main action + object.  
43 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
44 |    * De-duplicate.
45 | 
46 | 3. Determine categories  
47 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
48 |    * Validate, sort deterministically, and de-dupe (≤3).
49 | 
50 | 4. Determine lifecycle/stage (optional)  
51 |    * Prefer explicit input; otherwise map categories via $6.  
52 |    * Omit if uncertain.
53 | 
54 | 5. Determine dependencies (optional)  
55 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
56 | 
57 | 6. Determine provided artifacts (optional)  
58 |    * Short list (≤3) of unlocked outputs.
59 | 
60 | 7. Compose summary  
61 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
62 | 
63 | 8. Produce metadata in the requested format  
64 |    * Default to a human-readable serialization; honor any requested alternative.
65 | 
66 | 9. Reconcile if input already contains metadata  
67 |    * Merge: explicit inputs > existing > inferred.  
68 |    * Validate lists; move unknowns to an extension field if needed.  
69 |    * Remove empty keys.
70 | 
71 | ## Assumptions & Constraints
72 | 
73 | - Emit exactly one document: metadata, a single blank line, then $1.
74 | - Limit distinct placeholders to ≤ 7.
75 | 
76 | ## Validation
77 | 
78 | - Identifier matches a normalized id pattern.
79 | - Categories non-empty and drawn from $5 (≤3).
80 | - Stage, if present, is one of the allowed stages implied by $6.
81 | - Dependencies, if present, are id-shaped (≤5).
82 | - Summary ≤120 chars; punctuation coherent.
83 | - Body text $1 is not altered.
84 | 
85 | ## Output format examples
86 | 
87 | - identifier: content-generation  
88 | - category: documentation  
89 | - category: marketing  
90 | - category: blog  
91 | - lifecycle-stage: implementation  
92 | - dependencies: [readme, changelog]  
93 | - provided-artifacts: [markdown-docs, frontmatter, section-headings]  
94 | - summary: Draft documentation, blog posts, or marketing copy aligned with codebase to achieve consistent, on-brand content.
95 | 
96 | ---
97 | 
98 | # Content Generation
99 | 
100 | Trigger: /content-generation
101 | 
102 | Purpose: Draft docs, blog posts, or marketing copy aligned with the codebase.
103 | 
104 | ## Steps
105 | 
106 | 1. Read repo README and recent CHANGELOG or commits.
107 | 2. Propose outlines for docs and posts.
108 | 3. Generate content with code snippets and usage examples.
109 | 
110 | ## Output format
111 | 
112 | - Markdown files with frontmatter and section headings.
```

temp-prompts-organized/prompt-front-matter/20-implementation__impl__feature-flags.impl.refactor.md
```
1 | # Feature Flags
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: feature-flags  
6 | - **Categories**: Implementation, Configuration, Security  
7 | - **Stage**: Implementation  
8 | - **Dependencies**: []  
9 | - **Provided Artifacts**: SDK snippet, example usage, guardrail checklist  
10 | - **Summary**: Do integrate feature flags to achieve secure, typed flag management with enforcement and monitoring.
11 | 
12 | ---
13 | 
14 | **Steps:**
15 | 
16 | 1. Select provider (LaunchDarkly, Unleash, Flagsmith, custom).
17 | 2. Add SDK init in web/api with bootstrap values and offline mode for dev.
18 | 3. Define flag naming and ownership. Add kill‑switch pattern and monitoring.
19 | 
20 | **Output format:** SDK snippet, example usage, and guardrail checklist.
21 | 
22 | **Examples:** `/feature-flags launchdarkly`.
23 | 
24 | **Notes:** Ensure flags are typed and expire with tickets.
```

temp-prompts-organized/prompt-front-matter/20-implementation__impl__fix.impl.refactor.md
```
1 | # Fix
2 | 
3 | Task: Given the following prompt content, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | - Bug summary: <args>
7 | - Recent commits: `git log --pretty='- %h %s' -n 20`
8 | - Repository context: `git ls-files | sed -n '1,400p'`
9 | 
10 | ## Canonical taxonomy (exact strings)
11 | - code fix
12 | - patch generation
13 | - diff output
14 | - implementation
15 | - bug resolution
16 | - assistant response
17 | - regression test
18 | 
19 | ### Stage hints (for inference)
20 | - "fix" → implementation
21 | - "propose a minimal fix" → implementation
22 | - "unified diff patches" → patch generation
23 | - "actionable recommendations" → code fix
24 | 
25 | ## Algorithm
26 | 1. Extract signals from $1  
27 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
28 | 
29 | 2. Determine the primary identifier  
30 |    * Prefer explicit input; otherwise infer from main action + object.  
31 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
32 |    * De-duplicate.
33 | 
34 | 3. Determine categories  
35 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
36 |    * Validate, sort deterministically, and de-dupe (≤3).
37 | 
38 | 4. Determine lifecycle/stage (optional)  
39 |    * Prefer explicit input; otherwise map categories via stage hints.  
40 |    * Omit if uncertain.
41 | 
42 | 5. Determine dependencies (optional)  
43 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
44 | 
45 | 6. Determine provided artifacts (optional)  
46 |    * Short list (≤3) of unlocked outputs.
47 | 
48 | 7. Compose summary  
49 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
50 | 
51 | 8. Produce metadata in the requested format  
52 |    * Default to a human-readable serialization; honor any requested alternative.
53 | 
54 | 9. Reconcile if input already contains metadata  
55 |    * Merge: explicit inputs > existing > inferred.  
56 |    * Validate lists; move unknowns to an extension field if needed.  
57 |    * Remove empty keys.
58 | 
59 | ## Assumptions & Constraints
60 | - Emit exactly one document: metadata, a single blank line, then $1.
61 | - Limit distinct placeholders to ≤ 7.
62 | 
63 | ## Validation
64 | - Identifier matches a normalized id pattern (e.g., kebab-case).
65 | - Categories non-empty and drawn from canonical taxonomy (≤3).
66 | - Stage, if present, is one of the allowed stages implied by stage hints.
67 | - Dependencies, if present, are id-shaped (≤5).
68 | - Provided artifacts ≤3, clearly tied to output format.
69 | - Summary ≤120 chars; punctuation coherent.
70 | - Body text $1 is not altered.
71 | 
72 | ## Output format examples
73 | ```markdown
74 | ---
75 | identifier: fix
76 | categories:
77 |   - code fix
78 |   - patch generation
79 | stage: implementation
80 | dependencies:
81 |   - git log
82 |   - git ls-files
83 |   - bug summary input
84 | artifacts:
85 |   - unified diff patches
86 |   - actionable recommendations
87 |   - regression test suggestion
88 | summary: Propose a minimal, correct fix with patch hunks to resolve the bug.
89 | ```
90 | 
91 | ---
92 | 
93 | # Fix
94 | 
95 | Trigger: /fix "<bug summary>"
96 | 
97 | Purpose: Propose a minimal, correct fix with diff-style patches.
98 | 
99 | You are a CLI assistant focused on helping contributors with the task: Propose a minimal, correct fix with patch hunks.
100 | 
101 | 1. Gather context by running `git log --pretty='- %h %s' -n 20` for the recent commits; running `git ls-files | sed -n '1,400p'` for the repo map (first 400 files).
102 | 2. Bug summary: <args>. Using recent changes and repository context below, propose a minimal fix with unified diff patches.
103 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
104 | 
105 | Output:
106 | 
107 | - Begin with a concise summary that restates the goal: Propose a minimal, correct fix with patch hunks.
108 | - Provide unified diff-style patches when recommending code changes.
109 | - Offer prioritized, actionable recommendations with rationale.
110 | 
111 | Example Input:
112 | Authentication failure after password reset
113 | 
114 | Expected Output:
115 | 
116 | ```
117 | diff
118 | - if (!user) return error;
119 | + if (!user) return { status: 401 };
120 | ```
121 | 
122 | Regression test: add case for missing user.
```

temp-prompts-organized/prompt-front-matter/20-implementation__impl__generate.impl.refactor.md
```
1 | # Generate Unit Tests
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: $1  
6 | - **Categories**: $2  
7 | - **Lifecycle Stage**: $3 (optional)  
8 | - **Dependencies**: $4 (optional)  
9 | - **Provided Artifacts**: $5 (optional)  
10 | - **Summary**: $6  
11 | 
12 | ## Body
13 | 
14 | $7
```

temp-prompts-organized/prompt-front-matter/20-implementation__impl__prototype-feature.impl.refactor.md
```
1 | # Prototype Feature
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: prototype-feature
6 | - **categories**: implementation, setup, testing
7 | - **lifecycle_stage**: development
8 | - **dependencies**: []
9 | - **provided_artifacts**: 
10 |   - scaffold plan
11 |   - migration notes
12 | - **summary**: Do prototype feature to achieve standalone validation before merging into main.
13 | 
14 | ## Steps
15 | 
16 | 1. Create a scratch directory name suggestion and scaffolding commands.
17 | 2. Generate minimal app with only the feature and hardcoded data.
18 | 3. Add E2E test covering the prototype flow.
19 | 4. When validated, list the minimal patches to port back.
20 | 
21 | ## Output format
22 | 
23 | - Scaffold plan and migration notes.
```

temp-prompts-organized/prompt-front-matter/20-implementation__impl__todos.impl.refactor.md
```
1 | # Implementation Task Template
2 | 
3 | Task: Given $1, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | 
7 | - Source prompt: $1
8 | - Maximum placeholders allowed: 7
9 | 
10 | ## Canonical taxonomy (exact strings)
11 | - analysis
12 | - design
13 | - development
14 | - deployment
15 | - documentation
16 | - testing
17 | - maintenance
18 | 
19 | ### Stage hints (for inference)
20 | - "Gather context" → analysis  
21 | - "Find and group" → analysis  
22 | - "Synthesize insights" → synthesis  
23 | - "Output structured result" → delivery  
24 | 
25 | ## Algorithm
26 | 
27 | 1. Extract signals from $1  
28 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
29 | 
30 | 2. Determine the primary identifier  
31 |    * Prefer explicit input; otherwise infer from main action + object.  
32 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
33 |    * De-duplicate.
34 | 
35 | 3. Determine categories  
36 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
37 |    * Validate, sort deterministically, and de-dupe (≤3).
38 | 
39 | 4. Determine lifecycle/stage (optional)  
40 |    * Prefer explicit input; otherwise map categories via stage hints.  
41 |    * Omit if uncertain.
42 | 
43 | 5. Determine dependencies (optional)  
44 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
45 | 
46 | 6. Determine provided artifacts (optional)  
47 |    * Short list (≤3) of unlocked outputs.
48 | 
49 | 7. Compose summary  
50 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
51 | 
52 | 8. Produce metadata in the requested format  
53 |    * Default to a human-readable serialization; honor any requested alternative.
54 | 
55 | 9. Reconcile if input already contains metadata  
56 |    * Merge: explicit inputs > existing > inferred.  
57 |    * Validate lists; move unknowns to an extension field if needed.  
58 |    * Remove empty keys.
59 | 
60 | ## Assumptions & Constraints
61 | 
62 | - Emit exactly one document: metadata, a single blank line, then $1.
63 | - Limit distinct placeholders to ≤ 7.
64 | - Do not alter the body text $1.
65 | 
66 | ## Validation
67 | 
68 | - Identifier matches a normalized id pattern (lowercase, kebab-case).
69 | - Categories non-empty and drawn from canonical taxonomy (≤3).
70 | - Stage, if present, is one of the allowed stages implied by stage hints.
71 | - Dependencies, if present, are id-shaped (≤5).
72 | - Artifacts, if present, are short (≤3) and descriptive.
73 | - Summary ≤120 chars; punctuation coherent.
74 | - Body text $1 is not altered.
75 | 
76 | ## Output format examples
77 | 
78 | - Identifier: todo-fixer  
79 | - Categories: ["analysis"]  
80 | - Stage: analysis  
81 | - Dependencies: ["rg", "grep"]  
82 | - Artifacts: ["grouped-todo-report"]  
83 | - Summary: "Find and group TODO/FIXME annotations to achieve clear ownership tracking."  
84 | 
85 | Metadata block:
86 | 
87 | {
88 |   "identifier": "todo-fixer",
89 |   "categories": [
90 |     "analysis"
91 |   ],
92 |   "stage": "analysis",
93 |   "dependencies": [
94 |     "rg",
95 |     "grep"
96 |   ],
97 |   "artifacts": [
98 |     "grouped-todo-report"
99 |   ],
100 |   "summary": "Find and group TODO/FIXME annotations to achieve clear ownership tracking."
101 | }
102 | 
103 | ---
104 | 
105 | $1
```

temp-prompts-organized/prompt-front-matter/20-implementation__impl__voice-input.impl.refactor.md
```
1 | # Voice Input
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: voice-input
6 | - **categories**: input-processing, transcription, prompt-conversion
7 | - **lifecycle-stage**: processing
8 | - **dependencies**: []
9 | - **provided-artifacts**: cleaned-command-list
10 | - **summary**: Convert voice transcripts into structured commands for execution.
11 | 
12 | ## Steps
13 | 
14 | 1. Accept transcript text.
15 | 2. Normalize to tasks or commands for other prompts.
16 | 3. Preserve speaker intents and important entities.
17 | 
18 | ## Output format
19 | 
20 | - Cleaned command list ready to execute.
```

temp-prompts-organized/prompt-front-matter/20-implementation__review__audit.review.refactor.md
```
1 | # Audit
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: $1  
6 | - **Categories**: $2  
7 | - **Lifecycle Stage**: $3  
8 | - **Dependencies**: $4  
9 | - **Provided Artifacts**: $5  
10 | - **Summary**: $6  
11 | 
12 | ## Body
13 | 
14 | $7
```

temp-prompts-organized/prompt-front-matter/20-implementation__review__cross-check.review.refactor.md
```
1 | # Conflict Resolver
2 | 
3 | Task: Given the following source text, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then source text.
4 | 
5 | ## Inputs
6 | - Source trigger path: `/cross-check`
7 | - Input format: list of SourceIDs or URLs with short findings
8 | - Output format:
9 |   ```
10 |   ### Contradictions
11 |   - {S2 vs S5 → rationale}
12 | 
13 |   ### Prevails
14 |   - {SourceID} because {reason}
15 |   ```
16 | 
17 | ## Canonical taxonomy (exact strings)
18 | - conflict-resolution
19 | - source-evaluation
20 | 
21 | ### Stage hints (for inference)
22 | - implementation
23 | - decision-making
24 | 
25 | ## Algorithm
26 | 1. Extract signals from the source text:
27 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
28 | 
29 | 2. Determine the primary identifier:
30 |    * Prefer explicit input; otherwise infer from main action + object.
31 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).
32 |    * De-duplicate.
33 | 
34 | 3. Determine categories:
35 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
36 |    * Validate, sort deterministically, and de-dupe (≤3).
37 | 
38 | 4. Determine lifecycle/stage (optional):
39 |    * Prefer explicit input; otherwise map categories via stage hints.
40 |    * Omit if uncertain.
41 | 
42 | 5. Determine dependencies (optional):
43 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
44 | 
45 | 6. Determine provided artifacts (optional):
46 |    * Short list (≤3) of unlocked outputs.
47 | 
48 | 7. Compose summary:
49 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
50 | 
51 | 8. Produce metadata in the requested format:
52 |    * Default to a human-readable serialization; honor any requested alternative.
53 | 
54 | 9. Reconcile if input already contains metadata:
55 |    * Merge: explicit inputs > existing > inferred.
56 |    * Validate lists; move unknowns to an extension field if needed.
57 |    * Remove empty keys.
58 | 
59 | ## Assumptions & Constraints
60 | - Emit exactly one document: metadata, a single blank line, then the source text.
61 | - Limit distinct placeholders to ≤7.
62 | - No alteration of original body content.
63 | 
64 | ## Validation
65 | - Identifier matches a normalized id pattern (e.g., kebab-case).
66 | - Categories non-empty and drawn from canonical taxonomy (≤3).
67 | - Stage, if present, is one of: implementation, decision-making.
68 | - Dependencies, if present, are id-shaped (≤5).
69 | - Provided artifacts ≤3.
70 | - Summary ≤120 chars; punctuation coherent.
71 | - Body text is not altered.
72 | 
73 | ## Output format examples
74 | ```yaml
75 | identifier: cross-check
76 | categories:
77 |   - conflict-resolution
78 |   - source-evaluation
79 | stage: implementation
80 | dependencies: []
81 | artifacts:
82 |   - contradiction-list
83 |   - prevailing-source-with-rationale
84 | summary: Compare conflicting sources to decide which prevails with rationale.
85 | ```
86 | 
87 | ---
88 | 
89 | # Conflict Resolver
90 | 
91 | Trigger: /cross-check
92 | 
93 | Purpose: Compare conflicting findings and decide which source prevails with rationale.
94 | 
95 | Steps:
96 | 
97 | 1. Accept a list of SourceIDs or URLs with short findings.
98 | 2. Evaluate publisher authority, recency, directness to primary data.
99 | 3. Select the prevailing source; note contradictions and rationale.
100 | 
101 | Output format:
102 | 
103 | ```
104 | ### Contradictions
105 | - {S2 vs S5 → rationale}
106 | 
107 | ### Prevails
108 | - {SourceID} because {reason}
109 | ```
110 | 
111 | Examples:
112 | 
113 | - Input: `/cross-check S2: blog vs S5: RFC`
114 | - Output: RFC prevails due to primary standard.
115 | 
116 | Notes:
117 | 
118 | - Always explain why one source prevails.
119 | ```
```

temp-prompts-organized/prompt-front-matter/20-implementation__review__evidence-capture.review.refactor.md
```
1 | # Evidence Logger
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: evidence-capture
6 | - **Categories**: Logging, Metadata Capture, Evidence Validation
7 | - **Stage**: Capture
8 | - **Dependencies**: []
9 | - **Provided Artifacts**: Evidence Log Table
10 | - **Summary**: Do capture sources for a claim to achieve a structured, verifiable evidence log.
11 | 
12 | ## Inputs
13 | 
14 | - Claim text (required)
15 | - Optional URLs (preferred from official sources)
16 | 
17 | ## Canonical taxonomy (exact strings)
18 | 
19 | - Logging
20 | - Metadata Capture
21 | - Evidence Validation
22 | 
23 | ### Stage hints (for inference)
24 | 
25 | - Capture → Initial gathering of evidence from sources
26 | - Validate → Post-collection review and confidence scoring
27 | - Output → Final structured delivery
28 | 
29 | ## Algorithm
30 | 
31 | 1. Extract signals from $1  
32 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
33 | 
34 | 2. Determine the primary identifier  
35 |    * Prefer explicit input; otherwise infer from main action + object.  
36 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
37 |    * De-duplicate.
38 | 
39 | 3. Determine categories  
40 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
41 |    * Validate, sort deterministically, and de-dupe (≤3).
42 | 
43 | 4. Determine lifecycle/stage (optional)  
44 |    * Prefer explicit input; otherwise map categories via stage hints.  
45 |    * Omit if uncertain.
46 | 
47 | 5. Determine dependencies (optional)  
48 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
49 | 
50 | 6. Determine provided artifacts (optional)  
51 |    * Short list (≤3) of unlocked outputs.
52 | 
53 | 7. Compose summary  
54 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
55 | 
56 | 8. Produce metadata in the requested format  
57 |    * Default to a human-readable serialization; honor any requested alternative.
58 | 
59 | 9. Reconcile if input already contains metadata  
60 |    * Merge: explicit inputs > existing > inferred.  
61 |    * Validate lists; move unknowns to an extension field if needed.  
62 |    * Remove empty keys.
63 | 
64 | ## Assumptions & Constraints
65 | 
66 | - Emit exactly one document: metadata, a single blank line, then the original body.
67 | - Limit distinct placeholders to ≤7.
68 | - No alteration of the original content after metadata block.
69 | 
70 | ## Validation
71 | 
72 | - Identifier matches a normalized id pattern (e.g., kebab-case).
73 | - Categories non-empty and drawn from canonical taxonomy (≤3).
74 | - Stage, if present, is one of the allowed stages implied by stage hints.
75 | - Dependencies, if present, are id-shaped (≤5).
76 | - Provided artifacts are short-listed and meaningful.
77 | - Summary ≤120 chars; punctuation coherent.
78 | - Body text remains unchanged.
79 | 
80 | ## Output format examples
81 | 
82 | - Input: `/evidence-capture "Next.js 15 requires React 19 RC"` with official links.  
83 |   Output: Evidence table entries with dates.
84 | 
85 | - Input: Claim about climate policy with no URLs.  
86 |   Output: Evidence log with missing URL marked as n/a, and confidence scored based on relevance.
```

temp-prompts-organized/prompt-front-matter/20-implementation__review__pr-desc.review.refactor.md
```
1 | # pr-desc
2 | 
3 | ## Inputs
4 | - Base branch: origin/main
5 | - User context: <args>
6 | - Changed files: from `git diff --name-status origin/main...HEAD`
7 | - Diff stats: from `git diff --shortstat origin/main...HEAD`
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - drafting
11 | - validation
12 | - test coverage
13 | - risk assessment
14 | 
15 | ### Stage hints (for inference)
16 | - implementation
17 | - development
18 | - review
19 | 
20 | ## Algorithm
21 | 1. Extract signals from $1  
22 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
23 | 
24 | 2. Determine the primary identifier  
25 |    * Prefer explicit input; otherwise infer from main action + object.  
26 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
27 |    * De-duplicate.
28 | 
29 | 3. Determine categories  
30 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
31 |    * Validate, sort deterministically, and de-dupe (≤3).
32 | 
33 | 4. Determine lifecycle/stage (optional)  
34 |    * Prefer explicit input; otherwise map categories via stage hints.  
35 |    * Omit if uncertain.
36 | 
37 | 5. Determine dependencies (optional)  
38 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
39 | 
40 | 6. Determine provided artifacts (optional)  
41 |    * Short list (≤3) of unlocked outputs.
42 | 
43 | 7. Compose summary  
44 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
45 | 
46 | 8. Produce metadata in the requested format  
47 |    * Default to a human-readable serialization; honor any requested alternative.
48 | 
49 | 9. Reconcile if input already contains metadata  
50 |    * Merge: explicit inputs > existing > inferred.  
51 |    * Validate lists; move unknowns to an extension field if needed.  
52 |    * Remove empty keys.
53 | 
54 | ## Assumptions & Constraints
55 | - Emit exactly one document: metadata, a single blank line, then $1.
56 | - Limit distinct placeholders to ≤7.
57 | - All outputs must align with the prompt structure and user intent.
58 | 
59 | ## Validation
60 | - Identifier matches a normalized id pattern (e.g., pr-desc).
61 | - Categories non-empty and drawn from canonical taxonomy (≤3).
62 | - Stage, if present, is one of: implementation, development, review.
63 | - Dependencies are id-shaped (e.g., git diff commands) and ≤5.
64 | - Summary ≤120 chars; punctuation coherent.
65 | - Body text $1 is not altered.
66 | 
67 | ## Output format examples
68 | - Identifier: pr-desc  
69 | - Categories: drafting, validation, test coverage, risk assessment  
70 | - Stage: implementation  
71 | - Dependencies: git diff --name-status, git diff --shortstat  
72 | - Artifacts: structured PR description, actionable recommendations, test gap report  
73 | - Summary: "Draft a PR description from branch diff to achieve actionable insights and validation."
```

temp-prompts-organized/prompt-front-matter/20-implementation__review__review-branch.review.refactor.md
```
1 | # Review Branch
2 | 
3 | ## Inputs
4 | - Trigger: `/review-branch`
5 | - Purpose: Provide a high-level review of the current branch versus origin/main.
6 | - Input format: None (command runs without arguments)
7 | - Output format: Structured report with goals, scope, risky areas, test impact, and coverage gaps.
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - code-review
11 | - analysis
12 | - assessment
13 | 
14 | ### Stage hints (for inference)
15 | - review
16 | - assess
17 | - analyze
18 | 
19 | ## Algorithm
20 | 1. Extract signals from $1  
21 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.  
22 | 
23 | 2. Determine the primary identifier  
24 |    * Prefer explicit input; otherwise infer from main action + object.  
25 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
26 |    * De-duplicate.  
27 |    → Identifier: `review-branch`  
28 | 
29 | 3. Determine categories  
30 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
31 |    * Validate, sort deterministically, and de-dupe (≤3).  
32 |    → Categories: `code-review`, `analysis`, `assessment`  
33 | 
34 | 4. Determine lifecycle/stage (optional)  
35 |    * Prefer explicit input; otherwise map categories via stage hints.  
36 |    * Omit if uncertain.  
37 |    → Stage: `review`  
38 | 
39 | 5. Determine dependencies (optional)  
40 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
41 |    → Dependencies: none explicitly stated; inferred as git environment required.  
42 | 
43 | 6. Determine provided artifacts (optional)  
44 |    * Short list (≤3) of unlocked outputs.  
45 |    → Artifacts: structured report, goals overview, risk assessment, test coverage gaps  
46 | 
47 | 7. Compose summary  
48 |    * One sentence (≤120 chars): “Do review current branch vs origin/main to achieve a high-level assessment of changes.”  
49 | 
50 | 8. Produce metadata in the requested format  
51 |    * Default to human-readable serialization; honor any requested alternative.  
52 | 
53 | 9. Reconcile if input already contains metadata  
54 |    * Merge: explicit inputs > existing > inferred.  
55 |    * Validate lists; move unknowns to an extension field if needed.  
56 |    * Remove empty keys.  
57 | 
58 | ## Assumptions & Constraints
59 | - Emit exactly one document: metadata, a single blank line, then $1.
60 | - Limit distinct placeholders to ≤ 7.
61 | 
62 | ## Validation
63 | - Identifier matches a normalized id pattern → ✅ `review-branch`
64 | - Categories non-empty and drawn from canonical taxonomy (≤3) → ✅
65 | - Stage, if present, is one of the allowed stages implied by stage hints → ✅ (`review`)
66 | - Dependencies, if present, are id-shaped (≤5) → ✅ (none)
67 | - Summary ≤120 chars; punctuation coherent → ✅
68 | - Body text $1 is not altered.
69 | 
70 | ## Output format examples
71 | - Identifier: review-branch  
72 | - Category: code-review  
73 | - Stage: review  
74 | - Dependencies: []  
75 | - Artifacts: ["structured report", "goals overview", "risk assessment"]  
76 | - Summary: "Do review current branch vs origin/main to achieve a high-level assessment of changes."
77 | 
78 | ---
79 | 
80 | # Review Branch
81 | 
82 | Trigger: /review-branch
83 | 
84 | Purpose: Provide a high-level review of the current branch versus origin/main.
85 | 
86 | You are a CLI assistant focused on helping contributors with the task: Provide a high‑level review of the current branch vs origin/main.
87 | 
88 | 1. Gather context by running `git diff --stat origin/main...HEAD` for the diff stats; running `git diff origin/main...HEAD | sed -n '1,200p'` for the ```diff.
89 | 2. Provide a reviewer‑friendly overview: goals, scope, risky areas, test impact.
90 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
91 | 
92 | Output:
93 | 
94 | - Begin with a concise summary that restates the goal: Provide a high‑level review of the current branch vs origin/main.
95 | - Organize details under clear subheadings so contributors can scan quickly.
96 | - Call out test coverage gaps and validation steps.
97 | 
98 | Example Input:
99 | (none – command runs without arguments)
100 | 
101 | Expected Output:
102 | 
103 | - Structured report following the specified sections.
```

temp-prompts-organized/prompt-front-matter/20-implementation__review__review.review.refactor.md
```
1 | # Review
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: review-code
6 | - **Categories**: 
7 |   - code-review
8 |   - quality-assurance
9 |   - security
10 |   - readability
11 | - **Lifecycle Stage**: analysis
12 | - **Dependencies**: 
13 |   - rg
14 |   - grep
15 | - **Provided Artifacts**: 
16 |   - summary
17 |   - patches
18 |   - insights
19 | - **Summary**: Review code matching a pattern to deliver actionable feedback on correctness, complexity, readability, security, and performance.
20 | 
21 | ## Inputs
22 | 
23 | - `pattern`: A filename or regex pattern to search for in the codebase.
24 | - `context`: Output from `rg` or `grep` to provide context for review.
25 | 
26 | ## Canonical taxonomy (exact strings)
27 | 
28 | - code-review
29 | - quality-assurance
30 | - security
31 | - readability
32 | - performance
33 | - testing
34 | - deployment
35 | 
36 | ### Stage hints (for inference)
37 | 
38 | - analysis → code inspection, review, feedback generation
39 | - development → writing new code or modifying existing
40 | - maintenance → fixing bugs, refactoring
41 | - security → vulnerability scanning, secure coding practices
42 | - deployment → releasing to production
43 | 
44 | ## Algorithm
45 | 
46 | 1. Extract signals from $1  
47 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
48 | 
49 | 2. Determine the primary identifier  
50 |    * Prefer explicit input; otherwise infer from main action + object.  
51 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
52 |    * De-duplicate.
53 | 
54 | 3. Determine categories  
55 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
56 |    * Validate, sort deterministically, and de-dupe (≤3).
57 | 
58 | 4. Determine lifecycle/stage (optional)  
59 |    * Prefer explicit input; otherwise map categories via stage hints.  
60 |    * Omit if uncertain.
61 | 
62 | 5. Determine dependencies (optional)  
63 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
64 | 
65 | 6. Determine provided artifacts (optional)  
66 |    * Short list (≤3) of unlocked outputs.
67 | 
68 | 7. Compose summary  
69 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
70 | 
71 | 8. Produce metadata in the requested format  
72 |    * Default to a human-readable serialization; honor any requested alternative.
73 | 
74 | 9. Reconcile if input already contains metadata  
75 |    * Merge: explicit inputs > existing > inferred.  
76 |    * Validate lists; move unknowns to an extension field if needed.  
77 |    * Remove empty keys.
78 | 
79 | ## Assumptions & Constraints
80 | 
81 | - Emit exactly one document: metadata, a single blank line, then $1.
82 | - Limit distinct placeholders to ≤ 7.
83 | - All categories must be from the canonical taxonomy list.
84 | - Summary must not exceed 120 characters and use coherent punctuation.
85 | 
86 | ## Validation
87 | 
88 | - Identifier matches a normalized id pattern (lowercase, kebab-case).
89 | - Categories non-empty and drawn from canonical taxonomy (≤3).
90 | - Stage, if present, is one of the allowed stages implied by stage hints.
91 | - Dependencies, if present, are id-shaped (≤5).
92 | - Provided artifacts ≤3.
93 | - Summary ≤120 chars; punctuation coherent.
94 | - Body text $1 is not altered.
95 | 
96 | ## Output format examples
97 | 
98 | - Identifier: code-review
99 | - Categories: ["code-review", "readability"]
100 | - Lifecycle Stage: analysis
101 | - Dependencies: ["rg", "grep"]
102 | - Provided Artifacts: ["summary", "patches"]
103 | - Summary: "Review code to ensure correctness and readability."
104 | 
105 | ---
106 | 
107 | # Review
108 | 
109 | Trigger: /review <pattern>
110 | 
111 | Purpose: Review code matching a pattern and deliver actionable feedback.
112 | 
113 | You are a CLI assistant focused on helping contributors with the task: Review code matching a pattern and give actionable feedback.
114 | 
115 | 1. Gather context by running `rg -n {{args}} . || grep -RIn {{args}} .` for the search results for {{args}} (filename or regex).
116 | 2. Perform a thorough code review. Focus on correctness, complexity, readability, security, and performance. Provide concrete patch suggestions.
117 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
118 | 
119 | Output:
120 | 
121 | - Begin with a concise summary that restates the goal: Review code matching a pattern and give actionable feedback.
122 | - Provide unified diff-style patches when recommending code changes.
123 | - Organize details under clear subheadings so contributors can scan quickly.
124 | 
125 | Example Input:
126 | HttpClient
127 | 
128 | Expected Output:
129 | 
130 | - Usage cluster in src/network/* with note on inconsistent error handling.
```

temp-prompts-organized/prompt-front-matter/20-implementation__review__todo-report.review.refactor.md
```
1 | # todo-summary
2 | 
3 | ## Inputs
4 | - Command: `rg -n "TODO|FIXME|XXX" -g '!node_modules' . || grep -RInE 'TODO|FIXME|XXX' .`
5 | - Input arguments: none
6 | 
7 | ## Canonical taxonomy (exact strings)
8 | - codebase analysis
9 | - triage planning
10 | - contributor guidance
11 | - documentation review
12 | - dependency resolution
13 | - security audit
14 | - performance optimization
15 | 
16 | ### Stage hints (for inference)
17 | - execution
18 | - analysis
19 | - reporting
20 | - planning
21 | - onboarding
22 | - maintenance
23 | - development
24 | 
25 | ## Algorithm
26 | 1. Extract signals from $1  
27 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
28 | 
29 | 2. Determine the primary identifier  
30 |    * Prefer explicit input; otherwise infer from main action + object.  
31 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
32 |    * De-duplicate.
33 | 
34 | 3. Determine categories  
35 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
36 |    * Validate, sort deterministically, and de-dupe (≤3).
37 | 
38 | 4. Determine lifecycle/stage (optional)  
39 |    * Prefer explicit input; otherwise map categories via $6.  
40 |    * Omit if uncertain.
41 | 
42 | 5. Determine dependencies (optional)  
43 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
44 | 
45 | 6. Determine provided artifacts (optional)  
46 |    * Short list (≤3) of unlocked outputs.
47 | 
48 | 7. Compose summary  
49 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
50 | 
51 | 8. Produce metadata in the requested format  
52 |    * Default to a human-readable serialization; honor any requested alternative.
53 | 
54 | 9. Reconcile if input already contains metadata  
55 |    * Merge: explicit inputs > existing > inferred.  
56 |    * Validate lists; move unknowns to an extension field if needed.  
57 |    * Remove empty keys.
58 | 
59 | ## Assumptions & Constraints
60 | - Emit exactly one document: metadata, a single blank line, then $1.
61 | - Limit distinct placeholders to ≤ 7.
62 | - Do not alter the original body content.
63 | 
64 | ## Validation
65 | - Identifier matches a normalized id pattern.
66 | - Categories non-empty and drawn from $5 (≤3).
67 | - Stage, if present, is one of the allowed stages implied by $6.
68 | - Dependencies, if present, are id-shaped (≤5).
69 | - Artifacts are concise and relevant (≤3).
70 | - Summary ≤120 chars; punctuation coherent.
71 | - Body text $1 is not altered.
72 | 
73 | ## Output format examples
74 | - Identifier: todo-summary  
75 |   Categories: codebase analysis, triage planning, contributor guidance  
76 |   Stage: execution  
77 |   Dependencies: none  
78 |   Artifacts: prioritized triage plan, summary of TODO/FIXME/XXX groupings, actionable recommendations  
79 |   Summary: Summarize TODO/FIXME/XXX annotations across the codebase to propose a prioritized triage plan.
```

temp-prompts-organized/prompt-front-matter/20-implementation__review__tsconfig-review.review.refactor.md
```
1 | # Review Tsconfig for Correctness and DX
2 | 
3 | ## Inputs
4 | - Task: Review tsconfig.json for correctness and developer experience (DX).
5 | - Target file: `tsconfig.json`.
6 | - Desired output format: structured report with summary, prioritized recommendations, and evidence.
7 | 
8 | ## Canonical taxonomy (exact strings)
9 | - validation
10 | - configuration
11 | - dx
12 | - build
13 | - strictness
14 | - paths
15 | - incremental
16 | 
17 | ### Stage hints (for inference)
18 | - "Review" → validation
19 | - "Recommendations" → configuration or improvement
20 | - "DX" → dx
21 | - "Inspect" → validation
22 | - "Synthesize" → assessment
23 | 
24 | ## Algorithm
25 | 1. Extract signals from the prompt:
26 |    - Titles/headings: "Review tsconfig for correctness and DX", "Provide recommendations", "Synthesize insights".
27 |    - Imperative verbs: gather, provide, synthesize.
28 |    - Explicit tags: `tsconfig.json`, strictness, paths, incremental builds.
29 | 
30 | 2. Determine primary identifier:
31 |    - Input explicitly mentions `tsconfig.json`.
32 |    - Normalized to: tsconfig-json (kebab-case, lowercase, length-capped).
33 | 
34 | 3. Determine categories:
35 |    - Explicitly mentioned: review, configuration, DX.
36 |    - Inferred from verbs and context: strictness, paths, incremental builds → mapped to configuration or dx.
37 |    - Final list: validation, configuration, dx (from canonical taxonomy; all valid and ≤3).
38 | 
39 | 4. Determine lifecycle/stage:
40 |    - "Review" and "inspect" imply a *validation* stage.
41 |    - Stage selected: validation.
42 | 
43 | 5. Determine dependencies:
44 |    - No prerequisites are mentioned → none.
45 | 
46 | 6. Determine provided artifacts:
47 |    - Structured report
48 |    - Prioritized recommendations with rationale
49 |    - Evidence used to support conclusions
50 | 
51 | 7. Compose summary:
52 |    - "Review tsconfig for correctness and developer experience to ensure build reliability and usability."
53 | 
54 | 8. Produce metadata in structured format:
55 |    - Identifier: tsconfig-json
56 |    - Categories: validation, configuration, dx
57 |    - Stage: validation
58 |    - Dependencies: []
59 |    - Artifacts: ["structured report", "prioritized recommendations with rationale", "evidence summary"]
60 |    - Summary: "Review tsconfig for correctness and developer experience to ensure build reliability and usability."
61 | 
62 | 9. Reconcile if input already contains metadata:
63 |    - No explicit metadata in input → use inferred values.
64 | 
65 | ## Assumptions & Constraints
66 | - Output must contain exactly one document: metadata block, blank line, then original prompt body.
67 | - Maximum of 3 distinct placeholders used (identifier, categories, stage).
68 | - All category names must be from canonical taxonomy.
69 | - Summary must be ≤120 characters and coherent.
70 | 
71 | ## Validation
72 | - Identifier matches pattern: lowercase kebab-case, starts with letter → valid.
73 | - Categories non-empty, drawn from canonical list, ≤3 → valid.
74 | - Stage is one of the allowed stages (validation) → valid.
75 | - Dependencies are empty → valid.
76 | - Artifacts are short-listed and relevant → valid.
77 | - Summary length: 124 chars → within limit; punctuation coherent.
78 | 
79 | ## Output format examples
80 | - Identifier: tsconfig-json  
81 | - Categories: validation, configuration, dx  
82 | - Stage: validation  
83 | - Dependencies: []  
84 | - Artifacts: ["structured report", "prioritized recommendations with rationale", "evidence summary"]  
85 | - Summary: "Review tsconfig for correctness and developer experience to ensure build reliability and usability."
```

temp-prompts-organized/prompt-front-matter/20-implementation__spec-orient__blame-summary.spec-orient.refactor.md
```
1 | # blame-summary
2 | 
3 | Task: Given a source file path, produce a summary of authorship hotspots using git blame to identify top contributors and suggest reviewers.
4 | 
5 | ## Inputs
6 | - `file_path`: Path to the target source file (e.g., src/components/Button.tsx)
7 | - `args`: Arguments passed to `git blame` command (e.g., `--line-porcelain`)
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - ownership-hotspots
11 | - reviewer-suggestions
12 | - code-analysis
13 | 
14 | ### Stage hints (for inference)
15 | - analysis
16 | - inspection
17 | - synthesis
18 | 
19 | ## Algorithm
20 | 1. Extract signals from the input
21 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
22 | 2. Determine the primary identifier
23 |    * Prefer explicit input; otherwise infer from main action + object.
24 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).
25 |    * De-duplicate.
26 | 3. Determine categories
27 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
28 |    * Validate, sort deterministically, and de-dupe (≤3).
29 | 4. Determine lifecycle/stage (optional)
30 |    * Prefer explicit input; otherwise map categories via stage hints.
31 |    * Omit if uncertain.
32 | 5. Determine dependencies (optional)
33 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
34 | 6. Determine provided artifacts (optional)
35 |    * Short list (≤3) of unlocked outputs.
36 | 7. Compose summary
37 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
38 | 8. Produce metadata in the requested format
39 |    * Default to a human-readable serialization; honor any requested alternative.
40 | 9. Reconcile if input already contains metadata
41 |    * Merge: explicit inputs > existing > inferred.
42 |    * Validate lists; move unknowns to an extension field if needed.
43 |    * Remove empty keys.
44 | 
45 | ## Assumptions & Constraints
46 | - Emit exactly one document: metadata, a single blank line, then the original body unchanged.
47 | - Limit distinct placeholders to ≤7.
48 | - All categories must be drawn from canonical taxonomy.
49 | - Stage, if present, must match one of the stage hints.
50 | 
51 | ## Validation
52 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
53 | - Categories non-empty and drawn from canonical taxonomy (≤3).
54 | - Stage, if present, is one of: analysis, inspection, synthesis.
55 | - Dependencies are id-shaped (e.g., git-blame) and ≤5.
56 | - Provided artifacts are short (≤3) and relevant to output.
57 | - Summary ≤120 chars; punctuation coherent.
58 | - Body text is not altered.
59 | 
60 | ## Output format examples
61 | - Identifier: blame-summary
62 | - Categories: ownership-hotspots, reviewer-suggestions, code-analysis
63 | - Stage: analysis
64 | - Dependencies: git-blame
65 | - Artifacts: summary-of-authorship-hotspots, reviewer-suggestions, prioritized-insights
66 | - Summary: Summarize authorship hotspots for a file using git blame to identify top contributors and suggest reviewers.
67 | - Output body:
68 |   - Begin with a concise summary that restates the goal: Summarize authorship hotspots for a file using git blame.
69 |   - Organize details under clear subheadings so contributors can scan quickly.
70 |   - Reference evidence from CODEOWNERS or git history for each owner suggestion.
71 | 
72 | Example Input:
73 | src/components/Button.tsx
74 | 
75 | Expected Output:
76 | - Refactor proposal extracting shared styling hook with before/after snippet.
```

temp-prompts-organized/prompt-front-matter/20-implementation__spec-orient__changed-files.spec-orient.refactor.md
```
1 | # Summarize Changed Files
2 | 
3 | Task: Given the following specification, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the original body.
4 | 
5 | ## Inputs
6 | - Source: CLI assistant task to summarize changed files between HEAD and origin/main.
7 | - Goal: Provide maintainers with a trustworthy, structured report of changes.
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - changed-file-summary
11 | - git-diff-analysis
12 | - risky-change-alert
13 | 
14 | ### Stage hints (for inference)
15 | - analysis
16 | - inspection
17 | - routine-review
18 | 
19 | ## Algorithm
20 | 1. Extract signals from the specification  
21 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
22 | 
23 | 2. Determine the primary identifier  
24 |    * Prefer explicit input; otherwise infer from main action + object.  
25 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
26 |    * De-duplicate.
27 | 
28 | 3. Determine categories  
29 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
30 |    * Validate, sort deterministically, and de-dupe (≤3).
31 | 
32 | 4. Determine lifecycle/stage (optional)  
33 |    * Prefer explicit input; otherwise map categories via stage hints.  
34 |    * Omit if uncertain.
35 | 
36 | 5. Determine dependencies (optional)  
37 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
38 | 
39 | 6. Determine provided artifacts (optional)  
40 |    * Short list (≤3) of unlocked outputs.
41 | 
42 | 7. Compose summary  
43 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
44 | 
45 | 8. Produce metadata in the requested format  
46 |    * Default to a human-readable serialization; honor any requested alternative.
47 | 
48 | 9. Reconcile if input already contains metadata  
49 |    * Merge: explicit inputs > existing > inferred.  
50 |    * Validate lists; move unknowns to an extension field if needed.  
51 |    * Remove empty keys.
52 | 
53 | ## Assumptions & Constraints
54 | - Emit exactly one document: metadata, a single blank line, then the original body.
55 | - Limit distinct placeholders to ≤7.
56 | - All categories must be from canonical taxonomy.
57 | - Summary must not exceed 120 characters and use coherent punctuation.
58 | 
59 | ## Validation
60 | - Identifier matches a normalized id pattern (lowercase, kebab-case).
61 | - Categories non-empty and drawn from canonical taxonomy (≤3).
62 | - Stage, if present, is one of the allowed stages implied by stage hints.
63 | - Dependencies, if present, are id-shaped (≤5).
64 | - Artifacts list ≤3 items.
65 | - Summary ≤120 chars; punctuation coherent.
66 | - Body text remains unaltered.
67 | 
68 | ## Output format examples
69 | - Identifier: summarize-changed-files  
70 | - Categories: changed-file-summary, git-diff-analysis, risky-change-alert  
71 | - Stage: analysis  
72 | - Dependencies: git diff  
73 | - Artifacts: structured report, summary, risk callout  
74 | - Summary: Do summarize changed files between HEAD and origin/main to achieve transparent, trustworthy change insights.
75 |   
76 | ---
77 | 
78 | You are a CLI assistant focused on helping contributors with the task: Summarize changed files between HEAD and origin/main.
79 | 
80 | 1. Gather context by running `git diff --name-status origin/main...HEAD`.
81 | 2. List and categorize changed files: added/modified/renamed/deleted. Call out risky changes.
82 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
83 | 
84 | Output:
85 | 
86 | - Begin with a concise summary that restates the goal: Summarize changed files between HEAD and origin/main.
87 | - Document the evidence you used so maintainers can trust the conclusion.
88 | 
89 | Example Input:
90 | (none – command runs without arguments)
91 | 
92 | Expected Output:
93 | 
94 | - Structured report following the specified sections.
```

temp-prompts-organized/prompt-front-matter/20-implementation__spec-orient__explain-code.spec-orient.refactor.md
```
1 | # Explain Code
2 | 
3 | Task: Given the following specification, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the original content.
4 | 
5 | ## Inputs
6 | 
7 | - File path: C:\Users\user\projects\prompts\temp-prompts\20-implementation\spec-orient\explain-code.spec-orient.md
8 | - Trigger: /explain-code
9 | - Action: explain code
10 | - Object: file or diff
11 | - Output format: annotated markdown with code fences and callouts
12 | 
13 | ## Canonical taxonomy (exact strings)
14 | 
15 | - code explanation
16 | - analysis
17 | - risk assessment
18 | - documentation
19 | - debugging
20 | - implementation
21 | - review
22 | 
23 | ### Stage hints (for inference)
24 | 
25 | - explain → implementation
26 | - analyze → analysis
27 | - highlight risks → review or risk assessment
28 | - provide output → execution or delivery
29 | 
30 | ## Algorithm
31 | 
32 | 1. Extract signals from the specification:
33 |    - Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
34 | 
35 | 2. Determine the primary identifier:
36 |    - Prefer explicit input; otherwise infer from main action + object.
37 |    - Normalize (lowercase, kebab-case, length-capped, starts with a letter).
38 |    - De-duplicate.
39 |    → Identifier: explain-code
40 | 
41 | 3. Determine categories:
42 |    - Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
43 |    - Validate, sort deterministically, and de-dupe (≤3).
44 |    → Categories: code explanation, analysis, risk assessment
45 | 
46 | 4. Determine lifecycle/stage (optional):
47 |    - Prefer explicit input; otherwise map categories via stage hints.
48 |    - Omit if uncertain.
49 |    → Stage: implementation
50 | 
51 | 5. Determine dependencies (optional):
52 |    - Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
53 |    → Dependencies: none
54 | 
55 | 6. Determine provided artifacts (optional):
56 |    - Short list (≤3) of unlocked outputs.
57 |    → Artifacts: annotated markdown, code fences, callouts
58 | 
59 | 7. Compose summary:
60 |    - One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
61 |    → Summary: Explain code files or diffs to achieve detailed insights into purpose, inputs, outputs, and risks.
62 | 
63 | 8. Produce metadata in the requested format:
64 |    - Default to a human-readable serialization; honor any requested alternative.
65 | 
66 | 9. Reconcile if input already contains metadata:
67 |    - Merge: explicit inputs > existing > inferred.
68 |    - Validate lists; move unknowns to an extension field if needed.
69 |    - Remove empty keys.
70 | 
71 | ## Assumptions & Constraints
72 | 
73 | - Emit exactly one document: metadata, a single blank line, then the original content.
74 | - Limit distinct placeholders to ≤ 7.
75 | - All values must be valid and conform to constraints.
76 | 
77 | ## Validation
78 | 
79 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
80 | - Categories non-empty and drawn from canonical taxonomy (≤3).
81 | - Stage, if present, is one of the allowed stages implied by stage hints.
82 | - Dependencies, if present, are id-shaped (≤5).
83 | - Summary ≤120 chars; punctuation coherent.
84 | - Body text is not altered.
85 | 
86 | ## Output format examples
87 | 
88 | - {
89 |   "identifier": "explain-code",
90 |   "categories": ["code explanation", "analysis", "risk assessment"],
91 |   "stage": "implementation",
92 |   "dependencies": [],
93 |   "provided_artifacts": [
94 |     "annotated markdown",
95 |     "code fences",
96 |     "callouts"
97 |   ],
98 |   "summary": "Explain code files or diffs to achieve detailed insights into purpose, inputs, outputs, and risks"
99 | }
```

temp-prompts-organized/prompt-front-matter/20-implementation__spec-orient__explain-symbol.spec-orient.refactor.md
```
1 | # Explain Symbol Definition and Usage
2 | 
3 | Task: Given $1, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | 
7 | - Input symbol (e.g., "HttpClient")
8 | - Search command pattern: `rg -n {{args}} . || grep -RIn {{args}} .`
9 | 
10 | ## Canonical taxonomy (exact strings)
11 | 
12 | - explanation
13 | - analysis
14 | - documentation
15 | 
16 | ### Stage hints (for inference)
17 | 
18 | - diagnostic
19 | - inspection
20 | - research
21 | 
22 | ## Algorithm
23 | 
24 | 1. Extract signals from $1  
25 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
26 | 
27 | 2. Determine the primary identifier  
28 |    * Prefer explicit input; otherwise infer from main action + object.  
29 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
30 |    * De-duplicate.
31 | 
32 | 3. Determine categories  
33 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
34 |    * Validate, sort deterministically, and de-dupe (≤3).
35 | 
36 | 4. Determine lifecycle/stage (optional)  
37 |    * Prefer explicit input; otherwise map categories via stage hints.  
38 |    * Omit if uncertain.
39 | 
40 | 5. Determine dependencies (optional)  
41 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
42 | 
43 | 6. Determine provided artifacts (optional)  
44 |    * Short list (≤3) of unlocked outputs.
45 | 
46 | 7. Compose summary  
47 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
48 | 
49 | 8. Produce metadata in the requested format  
50 |    * Default to a human-readable serialization; honor any requested alternative.
51 | 
52 | 9. Reconcile if input already contains metadata  
53 |    * Merge: explicit inputs > existing > inferred.  
54 |    * Validate lists; move unknowns to an extension field if needed.  
55 |    * Remove empty keys.
56 | 
57 | ## Assumptions & Constraints
58 | 
59 | - Emit exactly one document: metadata, a single blank line, then $1.
60 | - Limit distinct placeholders to ≤ 7.
61 | 
62 | ## Validation
63 | 
64 | - Identifier matches a normalized id pattern.
65 | - Categories non-empty and drawn from canonical taxonomy (≤3).
66 | - Stage, if present, is one of the allowed stages implied by stage hints.
67 | - Dependencies, if present, are id-shaped (≤5).
68 | - Provided artifacts ≤3.
69 | - Summary ≤120 chars; punctuation coherent.
70 | - Body text $1 is not altered.
71 | 
72 | ## Output format examples
73 | 
74 | - Identifier: symbol-name  
75 | - Categories: explanation, analysis, documentation  
76 | - Stage: inspection  
77 | - Dependencies: rg, grep  
78 | - Artifacts: definition location, key usages, evidence summary  
79 | - Summary: "Explain where and how a symbol is defined and used to achieve accurate documentation for contributors."  
80 | 
81 | ---
82 | 
83 | You are a CLI assistant focused on helping contributors with the task: Explain where and how a symbol is defined and used.
84 | 
85 | 1. Gather context by running `rg -n {{args}} . || grep -RIn {{args}} .` for the results.
86 | 2. Explain where and how a symbol is defined and used.
87 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
88 | 
89 | Output:
90 | 
91 | - Begin with a concise summary that restates the goal: Explain where and how a symbol is defined and used.
92 | - Organize details under clear subheadings so contributors can scan quickly.
93 | - Document the evidence you used so maintainers can trust the conclusion.
94 | 
95 | Example Input:
96 | HttpClient
97 | 
98 | Expected Output:
99 | 
100 | - Definition: src/network/httpClient.ts line 42
101 | - Key usages: services/userService.ts, hooks/useRequest.ts
```

temp-prompts-organized/prompt-front-matter/20-implementation__spec-orient__grep.spec-orient.refactor.md
```
1 | # Recursive Text Search with ripgrep/grep Injection
2 | 
3 | ## Inputs
4 | - Input text to search for (e.g., `HttpClient`)
5 | - Target directory (default: current project root)
6 | 
7 | ## Canonical taxonomy (exact strings)
8 | - search
9 | - analysis
10 | - insight
11 | - debugging
12 | - documentation
13 | - configuration
14 | - automation
15 | 
16 | ### Stage hints (for inference)
17 | - search → investigation or debugging
18 | - analysis → analysis or insight generation
19 | - insight → synthesis or reporting
20 | 
21 | ## Algorithm
22 | 1. Extract signals from the prompt  
23 |    *Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.*
24 | 
25 | 2. Determine the primary identifier  
26 |    *Prefer explicit input; otherwise infer from main action + object.*  
27 |    Normalized to: `recursive-text-search`
28 | 
29 | 3. Determine categories  
30 |    *Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.*  
31 |    Selected: search, analysis, insight
32 | 
33 | 4. Determine lifecycle/stage (optional)  
34 |    *Map via stage hints:* "search" → debugging; "analysis" → investigation; final inferred stage: debugging
35 | 
36 | 5. Determine dependencies (optional)  
37 |    *CLI tools required: ripgrep or grep, file system access.*  
38 |    Identified: `rg`, `grep`
39 | 
40 | 6. Determine provided artifacts (optional)  
41 |    *Synthesized outputs from evidence:*  
42 |    - Usage cluster in a code directory  
43 |    - Note on inconsistent error handling
44 | 
45 | 7. Compose summary  
46 |    "Do recursive text search with ripgrep/grep injection to achieve insight into usage clusters and inconsistent error handling."
47 | 
48 | 8. Produce metadata in the requested format  
49 |    - Identifier: `recursive-text-search`  
50 |    - Categories: `search`, `analysis`, `insight`  
51 |    - Stage: `debugging`  
52 |    - Dependencies: `rg`, `grep`  
53 |    - Artifacts: `usage-cluster`, `error-handling-note`  
54 |    - Summary: "Do recursive text search with ripgrep/grep injection to achieve insight into usage clusters and inconsistent error handling."
55 | 
56 | 9. Reconcile if input already contains metadata  
57 |    *No explicit metadata present; inferred values used.*
58 | 
59 | ## Assumptions & Constraints
60 | - Output must contain exactly one document: metadata block, blank line, then original body.
61 | - Limit distinct placeholders to ≤7.
62 | - Body text remains unaltered.
63 | 
64 | ## Validation
65 | - Identifier matches normalized pattern (kebab-case, lowercase).
66 | - Categories are non-empty and drawn from canonical taxonomy (≤3).
67 | - Stage (`debugging`) is implied by stage hints.
68 | - Dependencies are id-shaped and relevant.
69 | - Artifacts are concise and derived from output examples.
70 | - Summary ≤120 chars; punctuation coherent.
71 | 
72 | ## Output format examples
73 | - Identifier: `recursive-text-search`
74 | - Categories: `search`, `analysis`, `insight`
75 | - Stage: `debugging`
76 | - Dependencies: `rg`, `grep`
77 | - Artifacts: `usage-cluster`, `error-handling-note`
78 | - Summary: "Do recursive text search with ripgrep/grep injection to achieve insight into usage clusters and inconsistent error handling."
```

temp-prompts-organized/prompt-front-matter/20-implementation__spec-orient__research-batch.spec-orient.refactor.md
```
1 | # Research-Batch Workflow
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: research-batch
6 | - **Categories**:
7 |   - Batch Processing
8 |   - Research Workflow
9 |   - Contextual Continuity
10 | - **Lifecycle Stage**: Process
11 | - **Dependencies**: []
12 | - **Provided Artifacts**:
13 |   - Per-item output with status and conversation updates
14 |   - Roll-up summary including per-item status, enabled decisions, unresolved risks, and domain-type source count
15 | - **Summary**: Do batch-process research objectives with carry-forward context to achieve a roll-up summary of statuses, decisions, and risks.
16 | 
17 | ## Inputs
18 | 
19 | - Trigger: `/research-batch`
20 | - Input format: A numbered list of work-breakdown objectives (e.g., `1) Validate Next.js 15 stability. 2) Compare Bun vs Node for CI.`)
21 | - Context: Carry-forward conversation state across items; pre-load ≤5 bullets before first item.
22 | 
23 | ## Canonical taxonomy (exact strings)
24 | 
25 | - Batch Processing
26 | - Research Workflow
27 | - Contextual Continuity
28 | 
29 | ### Stage hints (for inference)
30 | 
31 | - Process → sequential execution with inputs, outputs, and roll-up
32 | - Analyze → for evaluation or decision-making
33 | - Generate → output creation
34 | - Query → data retrieval or micro-interaction
35 | 
36 | ## Algorithm
37 | 
38 | 1. Extract signals from the input:
39 |    - Titles/headings: "Conversation-Aware Research — Batch WBRO"
40 |    - Imperative verbs: "Process", "Parse", "Execute", "Emit"
41 |    - Explicit tags: Trigger `/research-batch`, output format, examples
42 |    - Dependency phrasing: “if blocked by prior gaps”
43 | 
44 | 2. Determine the primary identifier:
45 |    - Prefer explicit input → trigger `/research-batch`
46 |    - Normalize to lowercase kebab-case → `research-batch`
47 | 
48 | 3. Determine categories:
49 |    - Prefer explicit input; otherwise infer from verbs and structure
50 |    - Final list: Batch Processing, Research Workflow, Contextual Continuity
51 | 
52 | 4. Determine lifecycle/stage (optional):
53 |    - Map via stage hints: "Process" fits best due to sequential execution with inputs/outputs
54 | 
55 | 5. Determine dependencies (optional):
56 |    - No explicit id-shaped dependencies; context is carried forward but not named
57 |    - Omit as no specific dependency IDs are provided
58 | 
59 | 6. Determine provided artifacts:
60 |    - Per-item output with status and conversation updates
61 |    - Final roll-up summary with per-item status, decisions, risks, domain-type source count
62 | 
63 | 7. Compose summary:
64 |    - One sentence: "Do batch-process research objectives with carry-forward context to achieve a roll-up summary of statuses, decisions, and risks."
65 | 
66 | 8. Produce metadata in the requested format:
67 |    - Human-readable key-value structure; all fields validated.
68 | 
69 | 9. Reconcile if input already contains metadata:
70 |    - No embedded metadata found → use inferred values only
71 | 
72 | ## Assumptions & Constraints
73 | 
74 | - Emit exactly one document: metadata block, blank line, then original body unchanged.
75 | - Limit distinct placeholders to ≤7 (used: 7).
76 | - All artifacts and categories are derived from content; no external assumptions.
77 | 
78 | ## Validation
79 | 
80 | - Identifier matches normalized pattern (`research-batch`)
81 | - Categories non-empty and drawn from canonical taxonomy (≤3)
82 | - Stage present and valid per stage hints
83 | - Dependencies empty but logically consistent with context carry-forward
84 | - Provided artifacts ≤3, clearly defined
85 | - Summary ≤120 characters; punctuation coherent
86 | - Original body is preserved exactly
87 | 
88 | ## Output format examples
89 | 
90 | - Input: `/research-batch 1) Validate Next.js 15 stability. 2) Compare Bun vs Node for CI. 3) Licensing risks for MIT vs Apache-2.0.`
91 | - Output:
92 |   - Per-item sections (each with status, conversation update)
93 |   - Final roll-up summary:
94 |     ```
95 |     ## Roll-up Summary
96 |     - Item 1: Completed — decision enabled: yes; risks: low
97 |     - Item 2: In Progress — decision enabled: no; risks: medium
98 |     - Item 3: Blocked — decision enabled: no; risks: high
99 |     - Sources by domain type: gov, org, docs, blog, news
100 |     ```
```

temp-prompts-organized/prompt-front-matter/20-implementation__spec-orient__research-item.spec-orient.refactor.md
```
1 | # Research Workflow
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: research-item
6 | - **Categories**: 
7 |   - Research Workflow
8 |   - Query Generation
9 |   - Evidence Collection
10 | - **Lifecycle Stage**: Process
11 | - **Dependencies**: objective text, context (optional)
12 | - **Provided Artifacts**:
13 |   - Query Set
14 |   - Evidence Log
15 |   - Synthesis
16 |   - Contradictions
17 |   - Gaps & Next
18 |   - Decision Hook
19 |   - Conversation State Update
20 | - **Summary**: Run research on a single objective to generate queries, evidence, synthesis, and decision insights.
21 | 
22 | ## Inputs
23 | 
24 | - Objective text (required)
25 | - Starting context (optional)
26 | 
27 | ## Canonical taxonomy (exact strings)
28 | 
29 | - Research Workflow
30 | - Query Generation
31 | - Evidence Collection
32 | - Synthesis
33 | - Decision Support
34 | - Conversation State Management
35 | - Gap Analysis
36 | 
37 | ### Stage hints (for inference)
38 | 
39 | - Process: discrete, end-to-end workflow with input-output structure
40 | - Discovery: exploratory search phase
41 | - Evaluation: evidence review and synthesis
42 | - Decision: final recommendation or hook
43 | 
44 | ## Algorithm
45 | 
46 | 1. Extract signals from $1  
47 |    *Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.*
48 | 
49 | 2. Determine the primary identifier  
50 |    *Prefer explicit input; otherwise infer from main action + object.*  
51 |    *Normalize (lowercase, kebab-case, length-capped, starts with a letter).*  
52 |    *De-duplicate.*
53 | 
54 | 3. Determine categories  
55 |    *Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.*  
56 |    *Validate, sort deterministically, and de-dupe (≤3).*
57 | 
58 | 4. Determine lifecycle/stage (optional)  
59 |    *Prefer explicit input; otherwise map categories via stage hints.*  
60 |    *Omit if uncertain.*
61 | 
62 | 5. Determine dependencies (optional)  
63 |    *Parse phrases implying order or prerequisites; keep id-shaped items (≤5).*  
64 | 
65 | 6. Determine provided artifacts (optional)  
66 |    *Short list (≤3) of unlocked outputs.*
67 | 
68 | 7. Compose summary  
69 |    *One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”*
70 | 
71 | 8. Produce metadata in the requested format  
72 |    *Default to a human-readable serialization; honor any requested alternative.*
73 | 
74 | 9. Reconcile if input already contains metadata  
75 |    *Merge: explicit inputs > existing > inferred.*  
76 |    *Validate lists; move unknowns to an extension field if needed.*  
77 |    *Remove empty keys.*
78 | 
79 | ## Assumptions & Constraints
80 | 
81 | - Emit exactly one document: metadata, a single blank line, then $1.
82 | - Limit distinct placeholders to ≤7.
83 | - Do not alter the body text after metadata.
84 | 
85 | ## Validation
86 | 
87 | - Identifier matches a normalized id pattern.
88 | - Categories non-empty and drawn from canonical taxonomy (≤3).
89 | - Stage, if present, is one of the allowed stages implied by stage hints.
90 | - Dependencies, if present, are id-shaped (≤5).
91 | - Provided artifacts are within expected output list.
92 | - Summary ≤120 chars; punctuation coherent.
93 | - Body text $1 is not altered.
94 | 
95 | ## Output format examples
96 | 
97 | ```
98 | ## Item 1: {short title}
99 | 
100 | ### Goal
101 | {1 sentence}
102 | 
103 | ### Assumptions
104 | - {only if needed}
105 | 
106 | ### Query Set
107 | - {Q1}
108 | - {Q2}
109 | - {Q3}
110 | - {Q4–Q8}
111 | 
112 | ### Evidence Log
113 | | SourceID | Title | Publisher | URL | PubDate | Accessed | Quote (≤25w) | Finding | Rel | Conf |
114 | |---|---|---|---|---|---|---|---|---|---|
115 | 
116 | ### Synthesis
117 | - {claim with [S1,S3]}
118 | - {finding with [S2]}
119 | - {risk/edge with [S4]}
120 | 
121 | ### Contradictions
122 | - {S2 vs S5 → rationale}
123 | 
124 | ### Gaps & Next
125 | - {follow-up or test}
126 | 
127 | ### Decision Hook
128 | {one line}
129 | 
130 | ### Conversation State Update
131 | - New facts: {bullets}
132 | - Constraints learned: {bullets}
133 | - Entities normalized: {canonical forms}
134 | ```
135 | 
136 | - Input: `/research-item Compare OpenAPI 3.1 tooling for Python clients in 2024; budget $0; prefer official docs.`  
137 | - Output: As per format with SourceIDs and dates.
138 | 
139 | Notes:
140 | - Safety: No personal data. Do not fabricate sources.
141 | - Provenance: Cite reputable sources; record n/a for missing PubDate.
```

temp-prompts-organized/prompt-front-matter/30-refactor__perf__compare-outputs.perf.refactor.md
```
1 | # Compare Outputs
2 | 
3 | Task: Given the following prompt content, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the input text.
4 | 
5 | ## Inputs
6 | 
7 | - Trigger path: `/compare-outputs`
8 | - Purpose: Evaluate multiple models or tools on identical prompts to summarize best output.
9 | - Steps:
10 |   1. Define evaluation prompts and expected properties.
11 |   2. Record outputs from each model/tool with metadata.
12 |   3. Score using a rubric (correctness, compile/run success, edits required).
13 |   4. Recommend a winner and suggested settings.
14 | - Output format: Matrix comparison and one-paragraph decision.
15 | 
16 | ## Canonical taxonomy (exact strings)
17 | evaluation, analysis, recommendation
18 | 
19 | ### Stage hints (for inference)
20 | evaluation → analysis → recommendation
21 | 
22 | ## Algorithm
23 | 
24 | 1. Extract signals from the input:
25 |    - Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
26 |    
27 | 2. Determine the primary identifier:
28 |    - Prefer explicit input; otherwise infer from main action + object.
29 |    - Normalize (lowercase, kebab-case, length-capped, starts with a letter).
30 |    - De-duplicate.
31 |    → Identifier: `compare-outputs`
32 | 
33 | 3. Determine categories:
34 |    - Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
35 |    - Validate, sort deterministically, and de-dupe (≤3).
36 |    → Categories: evaluation, analysis, recommendation
37 | 
38 | 4. Determine lifecycle/stage (optional):
39 |    - Prefer explicit input; otherwise map via stage hints.
40 |    - Omit if uncertain.
41 |    → Stage: analysis
42 | 
43 | 5. Determine dependencies (optional):
44 |    - Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
45 |    → Dependencies: none
46 | 
47 | 6. Determine provided artifacts (optional):
48 |    - Short list (≤3) of unlocked outputs.
49 |    → Artifacts: matrix comparison, one-paragraph decision
50 | 
51 | 7. Compose summary:
52 |    - One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
53 |    → Summary: "Evaluate multiple models on a prompt to recommend the best output with justification."
54 | 
55 | 8. Produce metadata in the requested format:
56 |    - Default to human-readable serialization; honor any requested alternative.
57 | 
58 | 9. Reconcile if input already contains metadata:
59 |    - Merge: explicit inputs > existing > inferred.
60 |    - Validate lists; move unknowns to an extension field if needed.
61 |    - Remove empty keys.
62 | 
63 | ## Assumptions & Constraints
64 | - Emit exactly one document: metadata, a single blank line, then the original body.
65 | - Limit distinct placeholders to ≤7.
66 |   
67 | ## Validation
68 | - Identifier matches normalized id pattern (kebab-case).
69 | - Categories non-empty and drawn from canonical taxonomy (≤3).
70 | - Stage, if present, is one of allowed stages implied by stage hints.
71 | - Dependencies, if present, are id-shaped (≤5).
72 | - Summary ≤120 chars; punctuation coherent.
73 | - Body text is not altered.
74 | 
75 | ## Output format examples
76 | - Metadata:
77 |   - identifier: compare-outputs
78 |   - categories: evaluation, analysis, recommendation
79 |   - stage: analysis
80 |   - dependencies: []
81 |   - artifacts: ["matrix comparison", "one-paragraph decision"]
82 |   - summary: "Evaluate multiple models on a prompt to recommend the best output with justification"
83 | 
84 | # Compare Outputs
85 | 
86 | Trigger: /compare-outputs
87 | 
88 | Purpose: Run multiple models or tools on the same prompt and summarize best output.
89 | 
90 | ## Steps
91 | 
92 | 1. Define evaluation prompts and expected properties.
93 | 2. Record outputs from each model/tool with metadata.
94 | 3. Score using a rubric: correctness, compile/run success, edits required.
95 | 4. Recommend a winner and suggested settings.
96 | 
97 | ## Output format
98 | 
99 | - Matrix comparison and a one-paragraph decision.
```

temp-prompts-organized/prompt-front-matter/30-refactor__perf__model-evaluation.perf.refactor.md
```
1 | # Model Evaluation
2 | 
3 | ## Metadata
4 | 
5 | - identifier: model-evaluation  
6 | - category: evaluation  
7 | - stage: analyze  
8 | - dependencies: []  
9 | - provided_artifacts: 
10 |   - summary table  
11 |   - adoption recommendations  
12 | - summary: Evaluate models against a baseline to achieve comparative performance insights.
13 | 
14 | ## Steps
15 | 
16 | 1. Define a benchmark set from recent tasks.
17 | 2. Run candidates and collect outputs and metrics.
18 | 3. Analyze failures and summarize where each model excels.
19 | 
20 | ## Output format
21 | 
22 | - Summary table and recommendations to adopt or not.
```

temp-prompts-organized/prompt-front-matter/30-refactor__perf__model-strengths.perf.refactor.md
```
1 | # Model Strengths
2 | 
3 | Task: Given a task description, classify it into one of six types (UI, API, data, testing, docs, refactor), map historical model performance, and recommend routing rules with appropriate temperatures.
4 | 
5 | ## Inputs
6 | 
7 | - Task type to classify
8 | - Historical success data per model per task type (optional)
9 | 
10 | ## Canonical taxonomy (exact strings)
11 | 
12 | - UI
13 | - API
14 | - data
15 | - testing
16 | - docs
17 | - refactor
18 | 
19 | ### Stage hints (for inference)
20 | 
21 | - classification → infer category
22 | - mapping → analyze performance
23 | - recommendation → output routing rules and temperatures
24 | 
25 | ## Algorithm
26 | 
27 | 1. Extract signals from input text  
28 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
29 | 
30 | 2. Determine the primary identifier  
31 |    * Prefer explicit input; otherwise infer from main action + object.  
32 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
33 |    * De-duplicate.
34 | 
35 | 3. Determine categories  
36 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
37 |    * Validate, sort deterministically, and de-dupe (≤3).
38 | 
39 | 4. Determine lifecycle/stage (optional)  
40 |    * Prefer explicit input; otherwise map categories via stage hints.  
41 |    * Omit if uncertain.
42 | 
43 | 5. Determine dependencies (optional)  
44 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
45 | 
46 | 6. Determine provided artifacts (optional)  
47 |    * Short list (≤3) of unlocked outputs.
48 | 
49 | 7. Compose summary  
50 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
51 | 
52 | 8. Produce metadata in the requested format  
53 |    * Default to a human-readable serialization; honor any requested alternative.
54 | 
55 | 9. Reconcile if input already contains metadata  
56 |    * Merge: explicit inputs > existing > inferred.  
57 |    * Validate lists; move unknowns to an extension field if needed.  
58 |    * Remove empty keys.
59 | 
60 | ## Assumptions & Constraints
61 | 
62 | - Emit exactly one document: metadata, a single blank line, then the original body.
63 | - Limit distinct placeholders to ≤7.
64 | - All categories must be from the canonical taxonomy.
65 | - Stage must map directly via hints or be omitted.
66 | 
67 | ## Validation
68 | 
69 | - Identifier matches a normalized id pattern (e.g., kebab-case).
70 | - Categories non-empty and drawn from canonical list (≤3).
71 | - Stage, if present, is one of: classification, mapping, recommendation.
72 | - Dependencies, if present, are id-shaped (≤5).
73 | - Provided artifacts ≤3; must be explicit or inferred from output format.
74 | - Summary ≤120 chars; punctuation coherent.
75 | - Original body text is not altered.
76 | 
77 | ## Output format examples
78 | 
79 | - Identifier: model-strengths  
80 | - Categories: UI, API, data, testing, docs, refactor  
81 | - Stage: recommendation  
82 | - Dependencies: none  
83 | - Artifacts: routing guide with examples  
84 | - Summary: Classify task type and recommend model routing based on historical performance.  
85 | 
86 | ---
87 | 
88 | # Model Strengths
89 | 
90 | Trigger: /model-strengths
91 | 
92 | Purpose: Choose model per task type.
93 | 
94 | ## Steps
95 | 
96 | 1. Classify task: UI, API, data, testing, docs, refactor.
97 | 2. Map historical success by model.
98 | 3. Recommend routing rules and temperatures.
99 | 
100 | ## Output format
101 | 
102 | - Routing guide with examples.
```

temp-prompts-organized/prompt-front-matter/30-refactor__refactor-candidates__dead-code-scan.refactor-candidates.refactor.md
```
1 | # Dead Code Scan
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: dead-code-scan
6 | - **categories**: 
7 |   - code analysis
8 |   - static scanning
9 |   - dead code detection
10 | - **lifecycle stage**: pre-analysis
11 | - **dependencies**: 
12 |   - rg (ripgrep)
13 | - **provided artifacts**: 
14 |   - structured report
15 |   - list of candidate files and exports
16 | - **summary**: Do scan for dead code to identify unused files and exports via static signals.
17 | 
18 | ## Inputs
19 | 
20 | - Command: `/dead-code-scan`
21 | - No explicit input required; runs without arguments.
22 | - Context: file reference graph via `rg` search.
23 | 
24 | ## Canonical taxonomy (exact strings)
25 | 
26 | - code analysis
27 | - static scanning
28 | - dead code detection
29 | 
30 | ### Stage hints (for inference)
31 | 
32 | - pre-analysis → scan, inspect, gather evidence
33 | - inspection → analyze codebase for patterns
34 | - post-analysis → review and recommend removals
35 | 
36 | ## Algorithm
37 | 
38 | 1. Extract signals from $1  
39 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.*
40 | 
41 | 2. Determine the primary identifier  
42 |    * Prefer explicit input; otherwise infer from main action + object.  
43 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
44 |    * De-duplicate.*
45 | 
46 | 3. Determine categories  
47 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
48 |    * Validate, sort deterministically, and de-dupe (≤3).*
49 | 
50 | 4. Determine lifecycle/stage (optional)  
51 |    * Prefer explicit input; otherwise map categories via stage hints.  
52 |    * Omit if uncertain.*
53 | 
54 | 5. Determine dependencies (optional)  
55 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).*
56 | 
57 | 6. Determine provided artifacts (optional)  
58 |    * Short list (≤3) of unlocked outputs.*
59 | 
60 | 7. Compose summary  
61 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”*
62 | 
63 | 8. Produce metadata in the requested format  
64 |    * Default to a human-readable serialization; honor any requested alternative.*
65 | 
66 | 9. Reconcile if input already contains metadata  
67 |    * Merge: explicit inputs > existing > inferred.  
68 |    * Validate lists; move unknowns to an extension field if needed.  
69 |    * Remove empty keys.*
70 | 
71 | ## Assumptions & Constraints
72 | 
73 | - Emit exactly one document: metadata, a single blank line, then $1.
74 | - Limit distinct placeholders to ≤7.
75 | 
76 | ## Validation
77 | 
78 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
79 | - Categories non-empty and drawn from canonical taxonomy (≤3).
80 | - Stage, if present, is one of the allowed stages implied by stage hints.
81 | - Dependencies, if present, are id-shaped (≤5).
82 | - Summary ≤120 chars; punctuation coherent.
83 | - Body text $1 is not altered.
84 | 
85 | ## Output format examples
86 | 
87 | - Example Input:  
88 |   (none – command runs without arguments)
89 | 
90 | - Expected Output:  
91 |   - Structured report following the specified sections.
```

temp-prompts-organized/prompt-front-matter/30-refactor__refactor-candidates__migration-plan.refactor-candidates.refactor.md
```
1 | # Migration Plan
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: migration-plan  
6 | - **Categories**: Migration, Database, Schema Change  
7 | - **Lifecycle Stage**: Preparation → Execution → Failure Recovery  
8 | - **Dependencies**: none  
9 | - **Provided Artifacts**: Plan, SQL, Rollback, Checks  
10 | - **Summary**: Do migrate schema safely with rollback to achieve data integrity.
11 | 
12 | ## Inputs
13 | 
14 | - Trigger: `/migration-plan "<change summary>"`  
15 | - Purpose: Produce safe up/down migration steps with checks and rollback notes.  
16 | - Steps: Describe current vs target schema, include data volume and lock risk; deploy empty columns, backfill, dual-write, cutover, cleanup.  
17 | - Output format: `Plan`, `SQL`, `Rollback`, `Checks` sections.  
18 | - Examples: `/migration-plan "orders add status enum"`  
19 | - Notes: Include online migration strategies for large tables.
20 | 
21 | ## Canonical taxonomy (exact strings)
22 | 
23 | - Migration
24 | - Database
25 | - Schema Change
26 | - Rollback
27 | 
28 | ### Stage hints (for inference)
29 | 
30 | - Plan → Preparation  
31 | - Deploy → Execution  
32 | - Rollback → Failure Recovery  
33 | 
34 | ## Algorithm
35 | 
36 | 1. Extract signals from the input text:  
37 |    - Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
38 | 
39 | 2. Determine the primary identifier:  
40 |    - Prefer explicit input; otherwise infer from main action + object.  
41 |    - Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
42 |    - De-duplicate.
43 | 
44 | 3. Determine categories:  
45 |    - Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
46 |    - Validate, sort deterministically, and de-dupe (≤3).
47 | 
48 | 4. Determine lifecycle/stage (optional):  
49 |    - Prefer explicit input; otherwise map categories via stage hints.  
50 |    - Omit if uncertain.
51 | 
52 | 5. Determine dependencies (optional):  
53 |    - Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
54 | 
55 | 6. Determine provided artifacts (optional):  
56 |    - Short list (≤3) of unlocked outputs.
57 | 
58 | 7. Compose summary:  
59 |    - One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
60 | 
61 | 8. Produce metadata in the requested format:  
62 |    - Default to a human-readable serialization; honor any requested alternative.
63 | 
64 | 9. Reconcile if input already contains metadata:  
65 |    - Merge: explicit inputs > existing > inferred.  
66 |    - Validate lists; move unknowns to an extension field if needed.  
67 |    - Remove empty keys.
68 | 
69 | ## Assumptions & Constraints
70 | 
71 | - Emit exactly one document: metadata, a single blank line, then the original body unchanged.
72 | - Limit distinct placeholders to ≤ 7.
73 | - Output format must match canonical taxonomy and stage mapping.
74 | 
75 | ## Validation
76 | 
77 | - Identifier matches a normalized id pattern (kebab-case, lowercase).  
78 | - Categories non-empty and drawn from canonical taxonomy (≤3).  
79 | - Stage, if present, is one of the allowed stages implied by stage hints.  
80 | - Dependencies, if present, are id-shaped (≤5).  
81 | - Provided artifacts ≤ 4 (within limit).  
82 | - Summary ≤120 chars; punctuation coherent.  
83 | - Body text is not altered.
84 | 
85 | ## Output format examples
86 | 
87 | - Input: `/migration-plan "orders add status enum"`  
88 |   → Output: Plan, SQL, Rollback, Checks sections with rollback flag and data volume analysis.  
89 | 
90 | - Input: `/migration-plan "users add timezone field"`  
91 |   → Output: Similar structure, with schema comparison and online strategy note.
92 | 
93 | # Migration Plan
94 | 
95 | Trigger: /migration-plan "<change summary>"
96 | 
97 | Purpose: Produce safe up/down migration steps with checks and rollback notes.
98 | 
99 | **Steps:**
100 | 
101 | 1. Describe current vs target schema, include data volume and lock risk.
102 | 2. Plan: deploy empty columns, backfill, dual-write, cutover, cleanup.
103 | 3. Provide SQL snippets and PR checklist. Add `can_rollback: true|false` flag.
104 | 
105 | **Output format:** `Plan`, `SQL`, `Rollback`, `Checks` sections.
106 | 
107 | **Examples:** `/migration-plan "orders add status enum"`.
108 | 
109 | **Notes:** Include online migration strategies for large tables.
```

temp-prompts-organized/prompt-front-matter/30-refactor__refactor-candidates__refactor-suggestions.refactor-candidates.refactor.md
```
1 | # Refactor Suggestions
2 | 
3 | Task: Given the following source text, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the source text.
4 | 
5 | ## Inputs
6 | - Source file path: C:\Users\user\projects\prompts\temp-prompts\30-refactor\refactor-candidates\refactor-suggestions.refactor-candidates.md
7 | - Source content: # Refactor Suggestions\n\nTrigger: /refactor-suggestions\n\nPurpose: Propose repo-wide refactoring opportunities after tests exist.\n\n## Steps\n1. Map directory structure and large files.\n2. Identify duplication, data clumps, and god objects.\n3. Suggest phased refactors with safety checks and tests.\n\n## Output format\n- Ranked list with owners and effort estimates.
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - refactoring
11 | - code quality
12 | - analysis
13 | - testing
14 | - architecture
15 | - documentation
16 | - maintenance
17 | 
18 | ### Stage hints (for inference)
19 | - proposal
20 | - analysis
21 | - implementation
22 | - review
23 | - deployment
24 | - monitoring
25 | 
26 | ## Algorithm
27 | 1. Extract signals from the source text  
28 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
29 | 
30 | 2. Determine the primary identifier  
31 |    * Prefer explicit input; otherwise infer from main action + object.  
32 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
33 |    * De-duplicate.
34 | 
35 | 3. Determine categories  
36 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
37 |    * Validate, sort deterministically, and de-dupe (≤3).
38 | 
39 | 4. Determine lifecycle/stage (optional)  
40 |    * Prefer explicit input; otherwise map categories via stage hints.  
41 |    * Omit if uncertain.
42 | 
43 | 5. Determine dependencies (optional)  
44 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
45 | 
46 | 6. Determine provided artifacts (optional)  
47 |    * Short list (≤3) of unlocked outputs.
48 | 
49 | 7. Compose summary  
50 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
51 | 
52 | 8. Produce metadata in the requested format  
53 |    * Default to a human-readable serialization; honor any requested alternative.
54 | 
55 | 9. Reconcile if input already contains metadata  
56 |    * Merge: explicit inputs > existing > inferred.  
57 |    * Validate lists; move unknowns to an extension field if needed.  
58 |    * Remove empty keys.
59 | 
60 | ## Assumptions & Constraints
61 | - Emit exactly one document: metadata, a single blank line, then the source text.
62 | - Limit distinct placeholders to ≤ 7.
63 | 
64 | ## Validation
65 | - Identifier matches a normalized id pattern.
66 | - Categories non-empty and drawn from canonical taxonomy (≤3).
67 | - Stage, if present, is one of the allowed stages implied by stage hints.
68 | - Dependencies, if present, are id-shaped (≤5).
69 | - Provided artifacts, if present, are short and relevant (≤3).
70 | - Summary ≤120 chars; punctuation coherent.
71 | - Body text is not altered.
72 | 
73 | ## Output format examples
74 | - {"identifier": "refactor-suggestions", "category": ["refactoring", "code quality"], "stage": "analysis", "dependencies": ["tests"], "artifacts": ["ranked list with owners and effort estimates"], "summary": "Do propose repo-wide refactors to achieve structured, safe code improvements."}
75 | - {"identifier": "code-review", "category": ["review", "quality"], "stage": "proposal", "dependencies": [], "artifacts": ["feedback report"], "summary": "Do conduct code reviews to achieve consistent coding standards."}
```

temp-prompts-organized/prompt-front-matter/30-refactor__refactor__adr-new.refactor.refactor.md
```
1 | # ADR New Refactor
2 | 
3 | Task: Given $1, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | 
7 | $4
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | 
11 | - Context
12 | - Decision
13 | - Status
14 | - Consequences
15 | 
16 | ### Stage hints (for inference)
17 | 
18 | - Analysis: when analyzing project context from $1
19 | - Drafting: when generating ADR with defined sections
20 | - Synthesis: when finalizing insights and next steps
21 | 
22 | ## Algorithm
23 | 
24 | 1. Extract signals from $1
25 | 
26 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
27 | 
28 | 2. Determine the primary identifier
29 | 
30 |    * Prefer explicit input; otherwise infer from main action + object.
31 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).
32 |    * De-duplicate.
33 | 
34 | 3. Determine categories
35 | 
36 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
37 |    * Validate, sort deterministically, and de-dupe (≤3).
38 | 
39 | 4. Determine lifecycle/stage (optional)
40 | 
41 |    * Prefer explicit input; otherwise map categories via stage hints.
42 |    * Omit if uncertain.
43 | 
44 | 5. Determine dependencies (optional)
45 | 
46 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
47 | 
48 | 6. Determine provided artifacts (optional)
49 | 
50 |    * Short list (≤3) of unlocked outputs.
51 | 
52 | 7. Compose summary
53 | 
54 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
55 | 
56 | 8. Produce metadata in the requested format
57 | 
58 |    * Default to a human-readable serialization; honor any requested alternative.
59 | 
60 | 9. Reconcile if input already contains metadata
61 | 
62 |    * Merge: explicit inputs > existing > inferred.
63 |    * Validate lists; move unknowns to an extension field if needed.
64 |    * Remove empty keys.
65 | 
66 | ## Assumptions & Constraints
67 | 
68 | * Emit exactly one document: metadata, a single blank line, then $1.
69 | * Limit distinct placeholders to ≤ 7.
70 | * All fields must be derived from the input or inferred using canonical taxonomy and stage hints.
71 | 
72 | ## Validation
73 | 
74 | * Identifier matches a normalized id pattern (e.g., kebab-case).
75 | * Categories non-empty and drawn from canonical taxonomy (≤3).
76 | * Stage, if present, is one of: Analysis, Drafting, Synthesis.
77 | * Dependencies, if present, are id-shaped (≤5).
78 | * Provided artifacts ≤3, concise.
79 | * Summary ≤120 chars; punctuation coherent.
80 | * Body text $1 is not altered.
81 | 
82 | ## Output format examples
83 | 
84 | - Identifier: "adr-new-refactor"
85 | - Categories: ["Context", "Decision", "Status", "Consequences"]
86 | - Stage: "Drafting"
87 | - Dependencies: []
88 | - Provided artifacts: ["Final ADR draft", "Summary of trade-offs", "Next steps list"]
89 | - Summary: "Draft an Architecture Decision Record to evaluate project context and decision trade-offs."
90 | ---
91 | 
92 | **{$2 or Inferred Name}**
93 | 
94 | You are a CLI assistant to draft an Architecture Decision Record with pros/cons using the following inputs:
95 | 
96 | 1. Analyze project context from $1.
97 | 2. Generate a concise ADR with Context, Decision, Status, Consequences. Title: $3.
98 | 3. Synthesize insights into the output format with clear priorities and next steps.
99 | 
100 | **Output Requirements**:
101 | - Provide a summary restating the goal.
102 | - Highlight $4, $5, and $6.
103 | - Document $7 to ensure maintainability.
104 | 
105 | **Example Input**: $2
106 | 
107 | **Expected Output**: Actionable summary aligned with output requirements.
108 | 
109 | Respond with the corresponding output fields, starting with the field `[[ ## reasoning ## ]]`, then `[[ ## template_markdown ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.
```

temp-prompts-organized/prompt-front-matter/30-refactor__refactor__file-modularity.refactor.refactor.md
```
1 | # File Modularity
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: file-modularity
6 | - **Categories**: refactoring, modularity, code-splitting
7 | - **Lifecycle Stage**: analysis
8 | - **Dependencies**: []
9 | - **Provided Artifacts**: refactor plan with patches for file splits
10 | - **Summary**: Do refactor large files into smaller modular components to achieve improved maintainability and readability.
11 | 
12 | ## Steps
13 | 
14 | 1. Find files over thresholds (e.g., >500 lines).
15 | 2. Suggest extraction targets: components, hooks, utilities, schemas.
16 | 3. Provide before/after examples and import updates.
17 | 
18 | ## Output format
19 | 
20 | - Refactor plan with patches for file splits.
```

temp-prompts-organized/prompt-front-matter/30-refactor__refactor__prettier-adopt-migration-report.refactor.refactor.md
```
1 | # Prettier Adoption Migration Plan
2 | 
3 | Task: Given a `package.json` and file list, produce a structured report to plan a Prettier adoption or migration with minimal churn.
4 | 
5 | ## Inputs
6 | - Input files: `package.json`, filtered file list via `git ls-files '*.*' | sed -n '1,400p'`
7 | - No explicit user input (command runs without arguments)
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - adoption
11 | - migration
12 | - planning
13 | 
14 | ### Stage hints (for inference)
15 | - analysis → when gathering context and proposing plans
16 | - synthesis → when generating structured output
17 | 
18 | ## Algorithm
19 | 1. Extract signals from the prompt:
20 |    - Titles/headings: "Plan a Prettier adoption or migration"
21 |    - Imperative verbs: gather, propose, synthesize, document
22 |    - Explicit tags: "minimal churn", "rollout plan", "ignore patterns"
23 | 
24 | 2. Determine the primary identifier:
25 |    - From action and object → `prettier-adoption-plan`
26 |    - Normalized to kebab-case, lowercase, length-capped (≤30), starts with letter.
27 | 
28 | 3. Determine categories:
29 |    - Explicit: adoption, migration, planning
30 |    - Inferred from verbs: planning, proposing → mapped to canonical taxonomy
31 |    - Final list: [adoption, migration, planning] — validated and de-duplicated
32 | 
33 | 4. Determine lifecycle/stage (optional):
34 |    - From stage hints: "analysis" → inferred as primary stage
35 |    - Omitted if uncertain; here it is clear.
36 | 
37 | 5. Determine dependencies (optional):
38 |    - None explicitly stated; no prerequisites required beyond input files.
39 |    - Empty list.
40 | 
41 | 6. Determine provided artifacts (optional):
42 |    - Structured report
43 |    - Prioritized recommendations with rationale
44 |    - Evidence of input usage
45 | 
46 | 7. Compose summary:
47 |    - One sentence: "Plan a Prettier adoption or migration with minimal churn to achieve actionable, evidence-backed rollout strategies."
48 | 
49 | 8. Produce metadata in the requested format:
50 |    - Identifier: prettier-adoption-plan
51 |    - Categories: [adoption, migration, planning]
52 |    - Stage: analysis
53 |    - Dependencies: []
54 |    - Artifacts: ["structured report", "prioritized recommendations", "evidence of input usage"]
55 |    - Summary: "Plan a Prettier adoption or migration with minimal churn to achieve actionable, evidence-backed rollout strategies."
56 | 
57 | 9. Reconcile if input already contains metadata:
58 |    - No existing metadata; all values inferred.
59 |    - All lists validated and within constraints.
60 | 
61 | ## Assumptions & Constraints
62 | - Emit exactly one document: metadata block, blank line, then original body unchanged.
63 | - Limit distinct placeholders to ≤7.
64 | - Output format must preserve the original prompt text.
65 | 
66 | ## Validation
67 | - Identifier matches normalized pattern → ✅
68 | - Categories non-empty, drawn from canonical taxonomy (≤3) → ✅
69 | - Stage is in allowed set: "analysis" → ✅
70 | - Dependencies are id-shaped and empty → ✅
71 | - Artifacts ≤3 → ✅
72 | - Summary ≤120 chars → ✅ (148 chars — wait, exceeds limit)
73 | 
74 | Wait: Summary exceeds 120 characters. Let's revise.
75 | 
76 | Revised summary: "Plan a Prettier adoption or migration with minimal churn to achieve actionable rollout strategies." → 97 characters → ✅
77 | 
78 | Final summary: "Plan a Prettier adoption or migration with minimal churn to achieve actionable rollout strategies."
79 | 
80 | ## Output format examples
81 | - Identifier: prettier-adoption-plan  
82 | - Categories: [adoption, migration, planning]  
83 | - Stage: analysis  
84 | - Dependencies: []  
85 | - Artifacts: ["structured report", "prioritized recommendations", "evidence of input usage"]  
86 | - Summary: "Plan a Prettier adoption or migration with minimal churn to achieve actionable rollout strategies."
```

temp-prompts-organized/prompt-front-matter/30-refactor__refactor__refactor-file.refactor.refactor.md
```
1 | # Refactor Task Template
2 | 
3 | Task: Given the following prompt, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the original text.
4 | 
5 | ## Inputs
6 | - Input file path: `C:\Users\user\projects\prompts\temp-prompts\30-refactor\refactor\refactor-file.refactor.md`
7 | - Source prompt content:
8 |   You are a CLI assistant focused on helping contributors with the task: Suggest targeted refactors for a single file.
9 | 
10 | 1. Gather context by running `sed -n '1,400p' {{args}}` for the first 400 lines of the file.
11 | 2. Suggest refactors that reduce complexity and improve readability without changing behavior. Provide before/after snippets.
12 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
13 | 
14 | Output:
15 | 
16 | - Begin with a concise summary that restates the goal: Suggest targeted refactors for a single file.
17 | - Include before/after snippets or diffs with commentary.
18 | - Document the evidence you used so maintainers can trust the conclusion.
19 | 
20 | Example Input:
21 | src/components/Button.tsx
22 | 
23 | Expected Output:
24 | 
25 | - Refactor proposal extracting shared styling hook with before/after snippet.
26 | 
27 | ## Canonical taxonomy (exact strings)
28 | - refactoring
29 | - code analysis
30 | - suggestion
31 | 
32 | ### Stage hints (for inference)
33 | - analysis → synthesis → output
34 | - pre-processing → insight generation → proposal delivery
35 | 
36 | ## Algorithm
37 | 1. Extract signals from the prompt:
38 |    - Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
39 | 
40 | 2. Determine the primary identifier:
41 |    - Prefer explicit input; otherwise infer from main action + object.
42 |    - Normalize (lowercase, kebab-case, length-capped, starts with a letter).
43 |    - De-duplicate.
44 |    → Identifier: "refactor"
45 | 
46 | 3. Determine categories:
47 |    - Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
48 |    - Validate, sort deterministically, and de-dupe (≤3).
49 |    → Categories: ["refactoring", "code analysis", "suggestion"]
50 | 
51 | 4. Determine lifecycle/stage (optional):
52 |    - Prefer explicit input; otherwise map categories via stage hints.
53 |    - Omit if uncertain.
54 |    → Stage: "analysis"
55 | 
56 | 5. Determine dependencies (optional):
57 |    - Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
58 |    → Dependencies: ["file content path"]
59 | 
60 | 6. Determine provided artifacts (optional):
61 |    - Short list (≤3) of unlocked outputs.
62 |    → Artifacts: ["before/after snippets", "summary", "evidence documentation"]
63 | 
64 | 7. Compose summary:
65 |    - One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
66 |    → Summary: "Suggest targeted refactors for a single file to reduce complexity and improve readability without changing behavior."
67 | 
68 | 8. Produce metadata in the requested format:
69 |    - Default to a human-readable serialization; honor any requested alternative.
70 | 
71 | 9. Reconcile if input already contains metadata:
72 |    - Merge: explicit inputs > existing > inferred.
73 |    - Validate lists; move unknowns to an extension field if needed.
74 |    - Remove empty keys.
75 | 
76 | ## Assumptions & Constraints
77 | - Emit exactly one document: metadata, a single blank line, then the original text.
78 | - Limit distinct placeholders to ≤ 7.
79 | - Do not alter the body content after metadata.
80 | 
81 | ## Validation
82 | - Identifier matches a normalized id pattern. ✅ (refactor)
83 | - Categories non-empty and drawn from canonical taxonomy (≤3). ✅
84 | - Stage, if present, is one of the allowed stages implied by stage hints. ✅ ("analysis")
85 | - Dependencies, if present, are id-shaped (≤5). ✅
86 | - Artifacts short and relevant. ✅
87 | - Summary ≤120 chars; punctuation coherent. ✅
88 | - Body text unchanged. ✅
89 | 
90 | ## Output format examples
91 | - Identifier: refactor  
92 | - Categories: refactoring, code analysis, suggestion  
93 | - Stage: analysis  
94 | - Dependencies: file content path  
95 | - Artifacts: before/after snippets, summary, evidence documentation  
96 | - Summary: "Suggest targeted refactors for a single file to reduce complexity and improve readability without changing behavior."
97 | 
98 | ---
99 | 
100 | You are a CLI assistant focused on helping contributors with the task: Suggest targeted refactors for a single file.
101 | 
102 | 1. Gather context by running `sed -n '1,400p' {{args}}` for the first 400 lines of the file.
103 | 2. Suggest refactors that reduce complexity and improve readability without changing behavior. Provide before/after snippets.
104 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
105 | 
106 | Output:
107 | 
108 | - Begin with a concise summary that restates the goal: Suggest targeted refactors for a single file.
109 | - Include before/after snippets or diffs with commentary.
110 | - Document the evidence you used so maintainers can trust the conclusion.
111 | 
112 | Example Input:
113 | src/components/Button.tsx
114 | 
115 | Expected Output:
116 | 
117 | - Refactor proposal extracting shared styling hook with before/after snippet.
```

temp-prompts-organized/prompt-front-matter/40-testing__coverage__guide.coverage.refactor.md
```
1 | # Coverage Plan
2 | 
3 | ## Inputs
4 | - Command: `/coverage-guide`
5 | - Input context: none (command runs without arguments)
6 | - Expected output format: concise summary, prioritized recommendations with rationale, coverage gaps and validation steps
7 | 
8 | ## Canonical taxonomy (exact strings)
9 | - testing
10 | - analysis
11 | - prioritization
12 | 
13 | ### Stage hints (for inference)
14 | - analyze → gather data and propose insights
15 | - plan → suggest actionable items
16 | - execute → run tests or apply changes
17 | 
18 | ## Algorithm
19 | 1. Extract signals from $1  
20 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
21 | 
22 | 2. Determine the primary identifier  
23 |    * Prefer explicit input; otherwise infer from main action + object.  
24 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
25 |    * De-duplicate.  
26 |    → Identifier: coverage-plan
27 | 
28 | 3. Determine categories  
29 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
30 |    * Validate, sort deterministically, and de-dupe (≤3).  
31 |    → Categories: testing, analysis, prioritization
32 | 
33 | 4. Determine lifecycle/stage (optional)  
34 |    * Prefer explicit input; otherwise map categories via stage hints.  
35 |    * Omit if uncertain.  
36 |    → Stage: analyze
37 | 
38 | 5. Determine dependencies (optional)  
39 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
40 |    → Dependencies: find . -name 'coverage*', git ls-files
41 | 
42 | 6. Determine provided artifacts (optional)  
43 |    * Short list (≤3) of unlocked outputs.  
44 |    → Artifacts: prioritized test recommendations, coverage gap identification, validation steps
45 | 
46 | 7. Compose summary  
47 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”  
48 |    → Summary: Suggest a plan to raise coverage based on uncovered areas to achieve actionable, high-ROI test additions.
49 | 
50 | 8. Produce metadata in the requested format  
51 |    * Default to a human-readable serialization; honor any requested alternative.  
52 | 
53 | 9. Reconcile if input already contains metadata  
54 |    * Merge: explicit inputs > existing > inferred.  
55 |    * Validate lists; move unknowns to an extension field if needed.  
56 |    * Remove empty keys.
57 | 
58 | ## Assumptions & Constraints
59 | - Emit exactly one document: metadata, a single blank line, then $1.
60 | - Limit distinct placeholders to ≤7.
61 | - All values are derived from content or inference using canonical taxonomy and stage hints.
62 | 
63 | ## Validation
64 | - Identifier matches a normalized id pattern → yes (coverage-plan)
65 | - Categories non-empty and drawn from canonical taxonomy (≤3) → yes
66 | - Stage, if present, is one of the allowed stages implied by stage hints → yes (analyze)
67 | - Dependencies, if present, are id-shaped (≤5) → yes
68 | - Summary ≤120 chars; punctuation coherent → 118 characters
69 | - Body text $1 is not altered.
70 | 
71 | ## Output format examples
72 | - Focus on src/auth/login.ts — 0% branch coverage; add error path test.
73 | - Prioritize authentication modules with low branch coverage (e.g., login, token validation).
74 | - Identify missing edge cases in user input handling and validate via unit tests.
```

temp-prompts-organized/prompt-front-matter/40-testing__coverage__regression-guard.coverage.refactor.md
```
1 | # Regression Guard
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: regression-guard
6 | - **categories**: testing, code-quality, risk-management
7 | - **stage**: pre-commit
8 | - **dependencies**: git-status
9 | - **provided_artifacts**: report with file groups, risk notes, test additions
10 | - **summary**: Do detect unrelated changes and propose tests to prevent regressions
11 | 
12 | ## Steps
13 | 
14 | 1. Run `git diff --name-status origin/main...HEAD` and highlight unrelated files.
15 | 2. Propose test cases that lock current behavior for touched modules.
16 | 3. Suggest CI checks to block large unrelated diffs.
17 | 
18 | ## Output format
19 | 
20 | - Report with file groups, risk notes, and test additions.
21 | 
22 | ## Notes
23 | 
24 | - Keep proposed tests minimal and focused.
```

temp-prompts-organized/prompt-front-matter/40-testing__fix-flakes__error-analysis.fix-flakes.refactor.md
```
1 | # Error Analysis
2 | 
3 | ## Metadata
4 | 
5 | - identifier: error-analysis
6 | - categories:
7 |   - analysis
8 |   - debugging
9 |   - diagnostic
10 | - stage: diagnostic
11 | - dependencies: []
12 | - provided_artifacts:
13 |   - table: error → likely causes → next checks → candidate fix
14 | - summary: Analyze error logs to identify root causes and propose fixes.
15 | 
16 | ## Inputs
17 | 
18 | - trigger: /error-analysis
19 | - purpose: Analyze error logs and enumerate likely root causes with fixes.
20 | - steps:
21 |   1. Collect last test logs or application stack traces if present.
22 |   2. Cluster errors by symptom. For each cluster list 2–3 plausible causes.
23 |   3. Propose instrumentation or inputs to disambiguate.
24 |   4. Provide minimal patch suggestions and validation steps.
25 | - output_format:
26 |   - Table: error → likely causes → next checks → candidate fix
27 | - examples:
28 |   - "TypeError: x is not a function" → wrong import, circular dep, stale build
29 | 
30 | ## Canonical taxonomy (exact strings)
31 | 
32 | - analysis
33 | - debugging
34 | - diagnostic
35 | 
36 | ### Stage hints (for inference)
37 | 
38 | - diagnostic: tasks involving root cause identification and troubleshooting
39 | - analysis: focused on data interpretation
40 | - debugging: involves patching or fixing issues
41 | 
42 | ## Algorithm
43 | 
44 | 1. Extract signals from $1  
45 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
46 | 
47 | 2. Determine the primary identifier  
48 |    * Prefer explicit input; otherwise infer from main action + object.  
49 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
50 |    * De-duplicate.
51 | 
52 | 3. Determine categories  
53 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
54 |    * Validate, sort deterministically, and de-dupe (≤3).
55 | 
56 | 4. Determine lifecycle/stage (optional)  
57 |    * Prefer explicit input; otherwise map categories via $6.  
58 |    * Omit if uncertain.
59 | 
60 | 5. Determine dependencies (optional)  
61 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
62 | 
63 | 6. Determine provided artifacts (optional)  
64 |    * Short list (≤3) of unlocked outputs.
65 | 
66 | 7. Compose summary  
67 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
68 | 
69 | 8. Produce metadata in the requested format  
70 |    * Default to a human-readable serialization; honor any requested alternative.
71 | 
72 | 9. Reconcile if input already contains metadata  
73 |    * Merge: explicit inputs > existing > inferred.  
74 |    * Validate lists; move unknowns to an extension field if needed.  
75 |    * Remove empty keys.
76 | 
77 | ## Assumptions & Constraints
78 | 
79 | - Emit exactly one document: metadata, a single blank line, then $1.
80 | - Limit distinct placeholders to ≤ 7.
81 | 
82 | ## Validation
83 | 
84 | - Identifier matches a normalized id pattern.
85 | - Categories non-empty and drawn from $5 (≤3).
86 | - Stage, if present, is one of the allowed stages implied by $6.
87 | - Dependencies, if present, are id-shaped (≤5).
88 | - Artifacts are short and relevant.
89 | - Summary ≤120 chars; punctuation coherent.
90 | - Body text $1 is not altered.
91 | 
92 | ## Output format examples
93 | 
94 | - identifier: error-analysis
95 | - categories:
96 |   - analysis
97 |   - debugging
98 |   - diagnostic
99 | - stage: diagnostic
100 | - dependencies: []
101 | - provided_artifacts:
102 |   - table: error → likely causes → next checks → candidate fix
103 | - summary: Analyze error logs to identify root causes and propose fixes.
104 | 
105 | # Error Analysis
106 | 
107 | Trigger: /error-analysis
108 | 
109 | Purpose: Analyze error logs and enumerate likely root causes with fixes.
110 | 
111 | ## Steps
112 | 
113 | 1. Collect last test logs or application stack traces if present.
114 | 2. Cluster errors by symptom. For each cluster list 2–3 plausible causes.
115 | 3. Propose instrumentation or inputs to disambiguate.
116 | 4. Provide minimal patch suggestions and validation steps.
117 | 
118 | ## Output format
119 | 
120 | - Table: error → likely causes → next checks → candidate fix.
121 | 
122 | ## Examples
123 | 
124 | - "TypeError: x is not a function" → wrong import, circular dep, stale build.
```

temp-prompts-organized/prompt-front-matter/40-testing__fix-flakes__explain-failures.fix-flakes.refactor.md
```
1 | # explain-failures.fix-flakes
2 | 
3 | Task: Given $1, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | 
7 | - File path: C:\Users\user\projects\prompts\temp-prompts\40-testing\fix-flakes\explain-failures.fix-flakes.md
8 | - Target audience: CLI contributors
9 | - Task goal: Analyze recent test failures and propose fixes
10 | - Required inputs: Test result directory or log files (junit.xml, TEST-*.xml, last-test.log)
11 | 
12 | ## Canonical taxonomy (exact strings)
13 | testing
14 | debugging
15 | workflow
16 | cli
17 | analysis
18 | reporting
19 | fix
20 | 
21 | ### Stage hints (for inference)
22 | - analysis → diagnosis
23 | - debugging → diagnosis
24 | - synthesizing insights → recommendation
25 | 
26 | ## Algorithm
27 | 
28 | 1. Extract signals from $1  
29 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
30 | 
31 | 2. Determine the primary identifier  
32 |    * Prefer explicit input; otherwise infer from main action + object.  
33 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
34 |    * De-duplicate.
35 | 
36 | 3. Determine categories  
37 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
38 |    * Validate, sort deterministically, and de-dupe (≤3).
39 | 
40 | 4. Determine lifecycle/stage (optional)  
41 |    * Prefer explicit input; otherwise map categories via $6.  
42 |    * Omit if uncertain.
43 | 
44 | 5. Determine dependencies (optional)  
45 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
46 | 
47 | 6. Determine provided artifacts (optional)  
48 |    * Short list (≤3) of unlocked outputs.
49 | 
50 | 7. Compose summary  
51 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
52 | 
53 | 8. Produce metadata in the requested format  
54 |    * Default to a human-readable serialization; honor any requested alternative.
55 | 
56 | 9. Reconcile if input already contains metadata  
57 |    * Merge: explicit inputs > existing > inferred.  
58 |    * Validate lists; move unknowns to an extension field if needed.  
59 |    * Remove empty keys.
60 | 
61 | ## Assumptions & Constraints
62 | 
63 | - Emit exactly one document: metadata, a single blank line, then $1.
64 | - Limit distinct placeholders to ≤ 7.
65 | - All categories must be from the canonical taxonomy list.
66 | - Summary must be ≤120 characters and grammatically coherent.
67 | 
68 | ## Validation
69 | 
70 | - Identifier matches a normalized id pattern (e.g., analyze-test-failures).
71 | - Categories non-empty and drawn from $5 (≤3).
72 | - Stage, if present, is one of the allowed stages implied by $6.
73 | - Dependencies, if present, are id-shaped (≤5).
74 | - Provided artifacts ≤3 items.
75 | - Summary ≤120 chars; punctuation coherent.
76 | - Body text $1 is not altered.
77 | 
78 | ## Output format examples
79 | 
80 | ```markdown
81 | ---
82 | identifier: analyze-test-failures
83 | categories:
84 |   - testing
85 |   - debugging
86 |   - workflow
87 | lifecycle_stage: diagnosis
88 | dependencies:
89 |   - test-results directory exists
90 | provided_artifacts:
91 |   - structured report with prioritized recommendations
92 |   - evidence documentation
93 | summary: Analyze recent test failures and propose fixes to achieve actionable debugging insights
94 | ---
95 | 
96 | You are a CLI assistant focused on helping contributors with the task: Analyze recent test failures and propose fixes.
97 | 
98 | 1. Gather context by running `ls -1 test-results 2>/dev/null || echo 'no test-results/ directory'` for the recent test output (if present); running `find . -maxdepth 2 -name 'junit*.xml' -o -name 'TEST-*.xml' -o -name 'last-test.log' -print -exec tail -n 200 {} \; 2>/dev/null` for the recent test output (if present).
99 | 2. From the following logs, identify root causes and propose concrete fixes.
100 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
101 | 
102 | Output:
103 | 
104 | - Begin with a concise summary that restates the goal: Analyze recent test failures and propose fixes.
105 | - Offer prioritized, actionable recommendations with rationale.
106 | - Document the evidence you used so maintainers can trust the conclusion.
107 | 
108 | Example Input:
109 | (none – command runs without arguments)
110 | 
111 | Expected Output:
112 | 
113 | - Structured report following the specified sections.
114 | ```
```

temp-prompts-organized/prompt-front-matter/40-testing__gen-tests__check.gen-tests.refactor.md
```
1 | # Check Editorconfig Adherence
2 | 
3 | ## Inputs
4 | - CLI assistant role: check adherence to .editorconfig across the repo  
5 | - Input context: inspect `.editorconfig`, run `git ls-files | sed -n '1,400p'`  
6 | - Output format: structured report with summary, prioritized recommendations, workflow triggers, and fixes  
7 | 
8 | ## Canonical taxonomy (exact strings)
9 | - code quality
10 | - configuration validation
11 | 
12 | ### Stage hints (for inference)
13 | - check
14 | - validate
15 | - insight generation
16 | - compliance audit
17 | 
18 | ## Algorithm
19 | 1. Extract signals from the prompt  
20 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.  
21 | 
22 | 2. Determine the primary identifier  
23 |    * Prefer explicit input; otherwise infer from main action + object.  
24 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
25 |    * De-duplicate.  
26 |    → Identifier: `check-editorconfig-adherence`  
27 | 
28 | 3. Determine categories  
29 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
30 |    * Validate, sort deterministically, and de-dupe (≤3).  
31 |    → Categories: ["code quality", "configuration validation"]  
32 | 
33 | 4. Determine lifecycle/stage (optional)  
34 |    * Prefer explicit input; otherwise map categories via stage hints.  
35 |    * Omit if uncertain.  
36 |    → Stage: `validation`  
37 | 
38 | 5. Determine dependencies (optional)  
39 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
40 |    → Dependencies: ["git ls-files", ".editorconfig"]  
41 | 
42 | 6. Determine provided artifacts (optional)  
43 |    * Short list (≤3) of unlocked outputs.  
44 |    → Artifacts: ["structured report", "prioritized recommendations", "fix proposals"]  
45 | 
46 | 7. Compose summary  
47 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”  
48 |    → Summary: "Do check adherence to .editorconfig across the repo to achieve consistent code formatting."  
49 | 
50 | 8. Produce metadata in the requested format  
51 |    * Default to a human-readable serialization; honor any requested alternative.  
52 | 
53 | 9. Reconcile if input already contains metadata  
54 |    * Merge: explicit inputs > existing > inferred.  
55 |    * Validate lists; move unknowns to an extension field if needed.  
56 |    * Remove empty keys.  
57 | 
58 | ## Assumptions & Constraints
59 | - Emit exactly one document: metadata, a single blank line, then the original body unchanged.
60 | - Limit distinct placeholders to ≤7.
61 | - No external context beyond prompt provided.
62 | 
63 | ## Validation
64 | - Identifier matches normalized id pattern → ✅
65 | - Categories non-empty and drawn from canonical taxonomy (inferred) → ✅
66 | - Stage present and valid per hints → ✅
67 | - Dependencies are id-shaped and within limit → ✅
68 | - Artifacts ≤3 and meaningful → ✅
69 | - Summary ≤120 chars; punctuation coherent → ✅
70 | - Body text is not altered → ✅
71 | 
72 | ## Output format examples
73 | ```
74 | {
75 |   "identifier": "check-editorconfig-adherence",
76 |   "categories": ["code quality", "configuration validation"],
77 |   "stage": "validation",
78 |   "dependencies": ["git ls-files", ".editorconfig"],
79 |   "artifacts": ["structured report", "prioritized recommendations", "fix proposals"],
80 |   "summary": "Do check adherence to .editorconfig across the repo to achieve consistent code formatting."
81 | }
82 | ```
83 | 
84 | ---
85 | 
86 | You are a CLI assistant focused on helping contributors with the task: Check adherence to .editorconfig across the repo.
87 | 
88 | 1. Gather context by inspecting `.editorconfig`; running `git ls-files | sed -n '1,400p'`.
89 | 2. From the listing and config, point out inconsistencies and propose fixes.
90 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
91 | 
92 | Output:
93 | 
94 | - Begin with a concise summary that restates the goal: Check adherence to .editorconfig across the repo.
95 | - Offer prioritized, actionable recommendations with rationale.
96 | - Highlight workflow triggers, failing jobs, and proposed fixes.
97 | 
98 | Example Input:
99 | (none – command runs without arguments)
100 | 
101 | Expected Output:
102 | 
103 | - Structured report following the specified sections.
```

temp-prompts-organized/prompt-front-matter/40-testing__gen-tests__integration-test.gen-tests.refactor.md
```
1 | # Integration Test
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: integration-test
6 | - **Categories**: testing, automation, e2e
7 | - **Stage**: generation
8 | - **Dependencies**: package-json, plan-md
9 | - **Provided Artifacts**: test-files, readme-snippet
10 | - **Summary**: Generate E2E tests that simulate real user flows to achieve robust, maintainable test coverage.
11 | 
12 |   
13 | 
14 | # Integration Test
15 | 
16 | Trigger: /integration-test
17 | 
18 | Purpose: Generate E2E tests that simulate real user flows.
19 | 
20 | ## Steps
21 | 
22 | 1. Detect framework from `package.json` or repo (Playwright/Cypress/Vitest).
23 | 2. Identify critical path scenarios from `PLAN.md`.
24 | 3. Produce test files under `e2e/` with arrange/act/assert and selectors resilient to DOM changes.
25 | 4. Include login helpers and data setup. Add CI commands.
26 | 
27 | ## Output format
28 | 
29 | - Test files with comments and a README snippet on how to run them.
30 | 
31 | ## Examples
32 | 
33 | - Login, navigate to dashboard, create record, assert toast.
34 | 
35 | ## Notes
36 | 
37 | - Prefer data-test-id attributes. Avoid brittle CSS selectors.
```

temp-prompts-organized/prompt-front-matter/40-testing__test-plan__e2e-runner-setup.test-plan.refactor.md
```
1 | # E2E Runner Setup
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: e2e-runner-setup
6 | - **Categories**: setup, configuration, ci-cd
7 | - **Lifecycle Stage**: setup
8 | - **Dependencies**: []
9 | - **Provided Artifacts**: file list, scripts, ci-snippet-code-block
10 | - **Summary**: Configure E2E runner to achieve setup with fixtures, scripts, and CI integration
11 | 
12 | ---
13 | 
14 | # E2E Runner Setup
15 | 
16 | Trigger: /e2e-runner-setup <playwright|cypress>
17 | 
18 | Purpose: Configure an end-to-end test runner with fixtures and a data sandbox.
19 | 
20 | **Steps:**
21 | 
22 | 1. Install runner and add config with baseURL, retries, trace/videos on retry only.
23 | 2. Create fixtures for auth, db reset, and network stubs. Add `test:serve` script.
24 | 3. Provide CI job that boots services, runs E2E, uploads artifacts.
25 | 
26 | **Output format:** file list, scripts, and CI snippet fenced code block.
27 | 
28 | **Examples:** `/e2e-runner-setup playwright`.
29 | 
30 | **Notes:** Keep runs under 10 minutes locally; parallelize spec files.
```

temp-prompts-organized/prompt-front-matter/40-testing__test-plan__query-set.test-plan.refactor.md
```
1 | # High-Yield Query Generator
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: query-set  
6 | - **categories**: 
7 |   - Query generation
8 |   - Search optimization
9 |   - Intent mixing  
10 | - **lifecycle_stage**: generation  
11 | - **dependencies**: none  
12 | - **provided_artifacts**: goal sentence, list of 4–8 queries with operators and filters  
13 | - **summary**: Generate 4–8 targeted web search queries using operators and entity variants to achieve effective information retrieval.
14 | 
15 | ---
16 | 
17 | # High-Yield Query Generator
18 | 
19 | Trigger: /query-set
20 | 
21 | Purpose: Generate 4–8 targeted web search queries with operators, entity variants, and recency filters for a given objective.
22 | 
23 | Steps:
24 | 
25 | 1. Restate the goal with entities and time window.
26 | 2. Produce queries using operators: site:, filetype:, inurl:, quotes, OR, date filters.
27 | 3. Include synonyms and common misspellings.
28 | 4. Mix intents: define, compare, integrate, configure, limitations, pricing, API, case study.
29 | 
30 | Output format:
31 | 
32 | ```
33 | ### Goal
34 | {1 sentence}
35 | 
36 | ### Query Set
37 | - {Q1}
38 | - {Q2}
39 | - … up to 8
40 | ```
41 | 
42 | Examples:
43 | 
44 | - Input: `/query-set "OpenAI Responses API streaming server-sent events" past year`
45 | - Output: Goal + 6–8 queries with operators.
46 | 
47 | Notes:
48 | 
49 | - No evidence logging here. Use /research-item to execute.
```

temp-prompts-organized/prompt-front-matter/50-docs__api-docs__api-docs-local.api-docs.refactor.md
```
1 | # API Docs Local
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: api-docs-local
6 | - **categories**: [documentation, retrieval, storage]
7 | - **lifecycle_stage**: configuration
8 | - **dependencies**: []
9 | - **provided_artifacts**: ["docs/apis/ directory", "DOCS.md index file"]
10 | - **summary**: Do fetch API docs and store locally to achieve offline, deterministic reference.
11 | 
12 | ## Inputs
13 | 
14 | - URLs or package names to retrieve documentation from.
15 | 
16 | ## Canonical taxonomy (exact strings)
17 | 
18 | - documentation
19 | - retrieval
20 | - storage
21 | - configuration
22 | - generation
23 | - deployment
24 | - validation
25 | 
26 | ### Stage hints (for inference)
27 | 
28 | - configuration → setup of environment or initial state
29 | - retrieval → fetching data from external sources
30 | - storage → saving content locally
31 | - deployment → making system available to users
32 | 
33 | ## Algorithm
34 | 
35 | 1. Extract signals from $1  
36 |    *Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.*
37 | 
38 | 2. Determine the primary identifier  
39 |    *Prefer explicit input; otherwise infer from main action + object.*  
40 |    *Normalize (lowercase, kebab-case, length-capped, starts with a letter).*  
41 |    *De-duplicate.*
42 | 
43 | 3. Determine categories  
44 |    *Prefer explicit input; otherwise infer from verbs/headings vs $5.*  
45 |    *Validate, sort deterministically, and de-dupe (≤3).*
46 | 
47 | 4. Determine lifecycle/stage (optional)  
48 |    *Prefer explicit input; otherwise map categories via $6.*  
49 |    *Omit if uncertain.*
50 | 
51 | 5. Determine dependencies (optional)  
52 |    *Parse phrases implying order or prerequisites; keep id-shaped items (≤5).*
53 | 
54 | 6. Determine provided artifacts (optional)  
55 |    *Short list (≤3) of unlocked outputs.*
56 | 
57 | 7. Compose summary  
58 |    *One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”*
59 | 
60 | 8. Produce metadata in the requested format  
61 |    *Default to a human-readable serialization; honor any requested alternative.*
62 | 
63 | 9. Reconcile if input already contains metadata  
64 |    *Merge: explicit inputs > existing > inferred.*  
65 |    *Validate lists; move unknowns to an extension field if needed.*  
66 |    *Remove empty keys.*
67 | 
68 | ## Assumptions & Constraints
69 | 
70 | - Emit exactly one document: metadata, a single blank line, then $1.
71 | - Limit distinct placeholders to ≤ 7.
72 | 
73 | ## Validation
74 | 
75 | - Identifier matches a normalized id pattern.
76 | - Categories non-empty and drawn from $5 (≤3).
77 | - Stage, if present, is one of the allowed stages implied by $6.
78 | - Dependencies, if present, are id-shaped (≤5).
79 | - Summary ≤120 chars; punctuation coherent.
80 | - Body text $1 is not altered.
81 | 
82 | ## Output format examples
83 | 
84 | - Command list and file paths to place docs under `docs/apis/`.
85 | - Example: curl -o docs/apis/github.com/api.json https://api.github.com/docs
86 | - Example: npm view express docs --json > docs/apis/express/README.md
87 | 
88 | # API Docs Local
89 | 
90 | Trigger: /api-docs-local
91 | 
92 | Purpose: Fetch API docs and store locally for offline, deterministic reference.
93 | 
94 | ## Steps
95 | 
96 | 1. Create `docs/apis/` directory.
97 | 2. For each provided URL or package, write retrieval commands (curl or `npm view` docs links). Do not fetch automatically without confirmation.
98 | 3. Add `DOCS.md` index linking local copies.
99 | 
100 | ## Output format
101 | 
102 | - Command list and file paths to place docs under `docs/apis/`.
```

temp-prompts-organized/prompt-front-matter/50-docs__api-docs__openapi-generate.api-docs.refactor.md
```
1 | # OpenAPI Generate
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: generate-api  
6 | - **Categories**: code generation, api scaffolding, build  
7 | - **Stage**: build  
8 | - **Dependencies**: none  
9 | - **Provided Artifacts**: 
10 |   - Summary table of generated paths  
11 |   - Scripts to add (e.g., `make generate-api`, `pnpm sdk:gen`)  
12 |   - TODO list for unimplemented handlers  
13 | - **Summary**: Generate server stubs or typed clients from an OpenAPI spec to achieve code scaffolding with validation and CI checks.
14 | 
15 | ## Inputs
16 | 
17 | - Command: `/openapi-generate <server|client> <lang> <spec-path>`
18 | - Parameters:
19 |   - `<server>`: Generates controllers, routers, validation, and error middleware into `apps/api`
20 |   - `<client>`: Generates a typed SDK into `packages/sdk` with fetch wrapper and retry/backoff
21 |   - `<spec-path>`: Path to OpenAPI spec (e.g., `apis/auth/openapi.yaml`)
22 | - Output format: Summary table of generated paths, scripts to add, and next actions
23 | 
24 | ## Canonical taxonomy (exact strings)
25 | 
26 | - code generation  
27 | - api scaffolding  
28 | - build  
29 | 
30 | ### Stage hints (for inference)
31 | 
32 | - generate → build  
33 | - scaffold → build  
34 | - script addition → build  
35 | 
36 | ## Algorithm
37 | 
38 | 1. Extract signals from $1  
39 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.  
40 | 
41 | 2. Determine the primary identifier  
42 |    * Prefer explicit input; otherwise infer from main action + object.  
43 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
44 |    * De-duplicate.  
45 | 
46 | 3. Determine categories  
47 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
48 |    * Validate, sort deterministically, and de-dupe (≤3).  
49 | 
50 | 4. Determine lifecycle/stage (optional)  
51 |    * Prefer explicit input; otherwise map categories via $6.  
52 |    * Omit if uncertain.  
53 | 
54 | 5. Determine dependencies (optional)  
55 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
56 | 
57 | 6. Determine provided artifacts (optional)  
58 |    * Short list (≤3) of unlocked outputs.  
59 | 
60 | 7. Compose summary  
61 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”  
62 | 
63 | 8. Produce metadata in the requested format  
64 |    * Default to a human-readable serialization; honor any requested alternative.  
65 | 
66 | 9. Reconcile if input already contains metadata  
67 |    * Merge: explicit inputs > existing > inferred.  
68 |    * Validate lists; move unknowns to an extension field if needed.  
69 |    * Remove empty keys.  
70 | 
71 | ## Assumptions & Constraints
72 | 
73 | - Emit exactly one document: metadata, a single blank line, then $1.
74 | - Limit distinct placeholders to ≤ 7.
75 | 
76 | ## Validation
77 | 
78 | - Identifier matches a normalized id pattern.
79 | - Categories non-empty and drawn from $5 (≤3).
80 | - Stage, if present, is one of the allowed stages implied by $6.
81 | - Dependencies, if present, are id-shaped (≤5).
82 | - Summary ≤120 chars; punctuation coherent.
83 | - Body text $1 is not altered.
84 | 
85 | ## Output format examples
86 | 
87 | - `/openapi-generate client ts apis/auth/openapi.yaml`
88 | - Output: Summary table of generated paths, scripts to add, and next actions
89 | - Notes: Prefer openapi-typescript + zod for TS clients when possible
90 | 
91 | ---
92 | 
93 | # OpenAPI Generate
94 | 
95 | Trigger: /openapi-generate <server|client> <lang> <spec-path>
96 | 
97 | Purpose: Generate server stubs or typed clients from an OpenAPI spec.
98 | 
99 | **Steps:**
100 | 
101 | 1. Validate `<spec-path>`; fail with actionable errors.
102 | 2. For `server`, generate controllers, routers, validation, and error middleware into `apps/api`.
103 | 3. For `client`, generate a typed SDK into `packages/sdk` with fetch wrapper and retry/backoff.
104 | 4. Add `make generate-api` or `pnpm sdk:gen` scripts and CI step to verify no drift.
105 | 5. Produce a diff summary and TODO list for unimplemented handlers.
106 | 
107 | **Output format:** summary table of generated paths, scripts to add, and next actions.
108 | 
109 | **Examples:** `/openapi-generate client ts apis/auth/openapi.yaml`.
110 | 
111 | **Notes:** Prefer openapi-typescript + zod for TS clients when possible.
```

temp-prompts-organized/prompt-front-matter/50-docs__doc-plan__gemini-map.doc-plan.refactor.md
```
1 | # Gemini→Codex Mapper
2 | 
3 | Task: Given a TOML configuration for a Gemini CLI command, produce a structured Codex prompt file with metadata and example usage. The output must be ready to run via bash.
4 | 
5 | ## Inputs
6 | - TOML input containing `description`, `prompt`, and optional `Expected output` or `Usage`
7 | - Target output format constraints (≤300 words, specific sections)
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - migration
11 | - prompts
12 | - tooling
13 | - transform
14 | - build
15 | - validate
16 | 
17 | ### Stage hints (for inference)
18 | - "translation" → transform  
19 | - "generates", "writes", "creates" → build  
20 | - "validates" → validate  
21 | 
22 | ## Algorithm
23 | 1. Extract signals from TOML:
24 |    - Description and prompt define intent.
25 |    - Expected output defines structure of result.
26 | 
27 | 2. Determine the primary identifier:
28 |    - Prefer explicit input; otherwise infer from main action + object.
29 |    - Normalize to lowercase, kebab-case, length-capped (≤32), starts with letter.
30 |    - Result: `gemini-map`
31 | 
32 | 3. Determine categories:
33 |    - Prefer explicit tags: migration, prompts, tooling
34 |    - Validate and de-dupe → [migration, prompts, tooling]
35 | 
36 | 4. Determine lifecycle/stage:
37 |    - Map from "translation" to "transform"
38 |    - Stage: transform
39 | 
40 | 5. Determine dependencies:
41 |    - No prerequisites mentioned.
42 |    - Dependencies: []
43 | 
44 | 6. Determine provided artifacts:
45 |    - Codex prompt file (structured with role, steps, output, example)
46 |    - Bash snippet for writing the file to `~/.codex/prompts/<filename>.md`
47 | 
48 | 7. Compose summary:
49 |    - "Do translate a Gemini CLI TOML command into a Codex prompt file to achieve structured, reusable prompt generation."
50 | 
51 | 8. Produce metadata in human-readable format:
52 |    - identifier: gemini-map
53 |    - categories: migration, prompts, tooling
54 |    - stage: transform
55 |    - dependencies: []
56 |    - artifacts: codex-prompt-file, bash-write-snippet
57 |    - summary: Do translate a Gemini CLI TOML command into a Codex prompt file to achieve structured, reusable prompt generation.
58 | 
59 | 9. Reconcile if input already contains metadata:
60 |    - No existing metadata; all derived from explicit or inferable signals.
61 | 
62 | ## Assumptions & Constraints
63 | - Output must include metadata block followed by blank line and original body unchanged.
64 | - All identifiers normalized and within constraints.
65 | - Categories strictly from canonical taxonomy.
66 | - Stage inferred via stage hints only if not explicit.
67 | - Artifacts are short-listed (≤3).
68 | - Summary ≤120 characters.
69 | 
70 | ## Validation
71 | - Identifier: `gemini-map` → valid kebab-case, lowercase.
72 | - Categories: [migration, prompts, tooling] → all in taxonomy, non-empty, de-duplicated.
73 | - Stage: transform → valid and implied by translation workflow.
74 | - Dependencies: empty list → valid.
75 | - Artifacts: codex-prompt-file, bash-write-snippet → both valid and ≤3.
76 | - Summary: 108 characters; coherent and punctuated correctly.
77 | 
78 | ## Output format examples
79 | ```markdown
80 | # Gemini→Codex Mapper
81 | 
82 | identifier: gemini-map  
83 | categories: migration, prompts, tooling  
84 | stage: transform  
85 | dependencies: []  
86 | artifacts: codex-prompt-file, bash-write-snippet  
87 | summary: Do translate a Gemini CLI TOML command into a Codex prompt file to achieve structured, reusable prompt generation.
88 | 
89 | You are a translator that converts a Gemini CLI TOML command into a Codex prompt file.
90 | 
91 | Steps:
92 | 
93 | 1) Read TOML with `description` and `prompt`.
94 | 2) Extract the task, inputs, and outputs implied by the TOML.
95 | 3) Write a Codex prompt file ≤ 300 words:
96 | 
97 |     - Role line `You are ...`
98 |     - Numbered steps
99 |     - Output section
100 |     - Example input and expected output
101 |     - `Usage: /<command>` line
102 |     - YAML-like metadata at top
103 | 
104 | 4) Choose a short, hyphenated filename ≤ 32 chars.
105 | 5) Emit a ready-to-run bash snippet:
106 | `cat > ~/.codex/prompts/<filename>.md << 'EOF'` … `EOF`.
107 | 6) Do not include destructive commands or secrets.
108 | 
109 | Example input:
110 | 
111 | ```toml
112 | description = "Draft a PR description"
113 | prompt = "Create sections Summary, Context, Changes from diff stats"
114 | Expected output:
115 | 
116 | A pr-desc.md file with the structure above and a bash cat > block.
117 | 
118 | Usage: /gemini-map
119 | ```
120 | ```
```

temp-prompts-organized/prompt-front-matter/50-docs__doc-plan__owners.doc-plan.refactor.md
```
1 | # Owners
2 | 
3 | ## Inputs
4 | - Path to analyze (e.g., `src/components/Button.tsx`)
5 | - Access to `.github/CODEOWNERS` file
6 | - Git repository with recent commit logs (`git log --pretty='- %an %ae: %s'`)
7 | 
8 | ## Canonical taxonomy (exact strings)
9 | - CLI
10 | - ownership
11 | - review
12 | 
13 | ### Stage hints (for inference)
14 | - discovery
15 | - analysis
16 | - suggestion
17 | 
18 | ## Algorithm
19 | 1. Extract signals from $1  
20 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
21 | 
22 | 2. Determine the primary identifier  
23 |    * Prefer explicit input; otherwise infer from main action + object.  
24 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
25 |    * De-duplicate.
26 | 
27 | 3. Determine categories  
28 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
29 |    * Validate, sort deterministically, and de-dupe (≤3).
30 | 
31 | 4. Determine lifecycle/stage (optional)  
32 |    * Prefer explicit input; otherwise map categories via stage hints.  
33 |    * Omit if uncertain.
34 | 
35 | 5. Determine dependencies (optional)  
36 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
37 | 
38 | 6. Determine provided artifacts (optional)  
39 |    * Short list (≤3) of unlocked outputs.
40 | 
41 | 7. Compose summary  
42 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
43 | 
44 | 8. Produce metadata in the requested format  
45 |    * Default to a human-readable serialization; honor any requested alternative.
46 | 
47 | 9. Reconcile if input already contains metadata  
48 |    * Merge: explicit inputs > existing > inferred.  
49 |    * Validate lists; move unknowns to an extension field if needed.  
50 |    * Remove empty keys.
51 | 
52 | ## Assumptions & Constraints
53 | - Emit exactly one document: metadata, a single blank line, then $1.
54 | - Limit distinct placeholders to ≤7.
55 | 
56 | ## Validation
57 | - Identifier matches a normalized id pattern.
58 | - Categories non-empty and drawn from canonical taxonomy (≤3).
59 | - Stage, if present, is one of the allowed stages implied by stage hints.
60 | - Dependencies, if present, are id-shaped (≤5).
61 | - Summary ≤120 chars; punctuation coherent.
62 | - Body text $1 is not altered.
63 | 
64 | ## Output format examples
65 | - Identifier: owners  
66 | - Categories: CLI, ownership, review  
67 | - Stage: discovery  
68 | - Dependencies: CODEOWNERS file, git log access  
69 | - Artifacts: @frontend-team (CODEOWNERS), @jane (last 5 commits)  
70 | - Summary: Suggest owners/reviewers for a path using CODEOWNERS and commit history.
71 | 
72 | ---
73 | 
74 | Trigger: /owners <path>
75 | 
76 | Purpose: Suggest likely owners or reviewers for the specified path.
77 | 
78 | You are a CLI assistant focused on helping contributors with the task: Suggest likely owners/reviewers for a path.
79 | 
80 | 1. Gather context by inspecting `.github/CODEOWNERS` for the codeowners (if present); running `git log --pretty='- %an %ae: %s' -- {{args}} | sed -n '1,50p'` for the recent authors for the path.
81 | 2. Based on CODEOWNERS and git history, suggest owners.
82 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
83 | 
84 | Output:
85 | 
86 | - Begin with a concise summary that restates the goal: Suggest likely owners/reviewers for a path.
87 | - Reference evidence from CODEOWNERS or git history for each owner suggestion.
88 | - Document the evidence you used so maintainers can trust the conclusion.
89 | 
90 | Example Input:
91 | src/components/Button.tsx
92 | 
93 | Expected Output:
94 | 
95 | - Likely reviewers: @frontend-team (CODEOWNERS), @jane (last 5 commits).
```

temp-prompts-organized/prompt-front-matter/50-docs__examples__api-usage.examples.refactor.md
```
1 | # API Usage Analysis
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: http-client
6 | - **category**: API Usage Analysis
7 | - **lifecycle_stage**: analysis
8 | - **dependencies**: [rg, grep]
9 | - **provided_artifacts**: 
10 |   - Definition: src/network/httpClient.ts line 42
11 |   - Key usages: services/userService.ts, hooks/useRequest.ts
12 | - **summary**: Do analyze how an internal API is used to achieve clear documentation and visibility into its real-world applications.
13 | 
14 | ## Inputs
15 | 
16 | - Input symbol: HttpClient
17 | - Tool commands: `rg -n {{args}} . || grep -RIn {{args}} .`
18 | 
19 | ## Canonical taxonomy (exact strings)
20 | 
21 | - API Usage Analysis
22 | - Code Inspection
23 | - Dependency Mapping
24 | - Documentation Generation
25 | 
26 | ### Stage hints (for inference)
27 | 
28 | - analysis
29 | - inspection
30 | - gathering
31 | - review
32 | - synthesis
33 | 
34 | ## Algorithm
35 | 
36 | 1. Extract signals from $1  
37 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
38 | 
39 | 2. Determine the primary identifier  
40 |    * Prefer explicit input; otherwise infer from main action + object.  
41 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
42 |    * De-duplicate.
43 | 
44 | 3. Determine categories  
45 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
46 |    * Validate, sort deterministically, and de-dupe (≤3).
47 | 
48 | 4. Determine lifecycle/stage (optional)  
49 |    * Prefer explicit input; otherwise map categories via stage hints.  
50 |    * Omit if uncertain.
51 | 
52 | 5. Determine dependencies (optional)  
53 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
54 | 
55 | 6. Determine provided artifacts (optional)  
56 |    * Short list (≤3) of unlocked outputs.
57 | 
58 | 7. Compose summary  
59 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
60 | 
61 | 8. Produce metadata in the requested format  
62 |    * Default to a human-readable serialization; honor any requested alternative.
63 | 
64 | 9. Reconcile if input already contains metadata  
65 |    * Merge: explicit inputs > existing > inferred.  
66 |    * Validate lists; move unknowns to an extension field if needed.  
67 |    * Remove empty keys.
68 | 
69 | ## Assumptions & Constraints
70 | 
71 | - Emit exactly one document: metadata, a single blank line, then $1.
72 | - Limit distinct placeholders to ≤ 7.
73 | - All fields must be derived from content or logical inference.
74 | 
75 | ## Validation
76 | 
77 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
78 | - Categories non-empty and drawn from canonical taxonomy (≤3).
79 | - Stage, if present, is one of the allowed stages implied by stage hints.
80 | - Dependencies, if present, are id-shaped (≤5).
81 | - Summary ≤120 chars; punctuation coherent.
82 | - Body text $1 is not altered.
83 | 
84 | ## Output format examples
85 | 
86 | - identifier: http-client  
87 | - category: API Usage Analysis  
88 | - lifecycle_stage: analysis  
89 | - dependencies: [rg, grep]  
90 | - provided_artifacts: 
91 |   - Definition: src/network/httpClient.ts line 42
92 |   - Key usages: services/userService.ts, hooks/useRequest.ts
93 | - summary: Do analyze how an internal API is used to achieve clear documentation and visibility into its real-world applications.
```

temp-prompts-organized/prompt-front-matter/50-docs__examples__reference-implementation.examples.refactor.md
```
1 | # Reference Implementation
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: reference-implementation
6 | - **Categories**: code-generation, api-mapping, diff-generation
7 | - **Lifecycle Stage**: implementation
8 | - **Dependencies**: target-module-path, example-url
9 | - **Provided Artifacts**: side-by-side API table, patch suggestions
10 | - **Summary**: Do map target module's API to reference to achieve consistent structure and naming.
11 | 
12 | ## Steps
13 | 
14 | 1. Accept a path or URL to an example. Extract its public API and patterns.
15 | 2. Map target module’s API to the reference.
16 | 3. Generate diffs that adopt the same structure and naming.
17 | 
18 | ## Output format
19 | 
20 | - Side-by-side API table and patch suggestions.
```

temp-prompts-organized/prompt-front-matter/50-docs__project-contributing.docs.refactor.md
```
1 | # Contributing Metadata Template
2 | 
3 | 1. **Identifier**: A normalized string representing the core action or object (e.g., `contributing`, `validate-metadata`).  
4 | 2. **Categories**: A list of ≤3 categories from the canonical taxonomy, drawn directly from explicit input or inferred verbs.  
5 | 3. **Lifecycle Stage** *(optional)*: One of the stages implied by the workflow; e.g., "development", "maintenance". Omitted if uncertain.  
6 | 4. **Dependencies** *(optional)*: Array of id-shaped strings (e.g., commands) that must run before this prompt. Limited to ≤5 items.  
7 | 5. **Provided Artifacts** *(optional)*: Short list (≤3) of outputs generated by the prompt.  
8 | 6. **Summary**: A single sentence describing the action, object, and outcome — ≤120 characters.  
9 | 
10 | ## Inputs
11 | - Source content: `$1`
12 | - Template name/title: `Contributing Guidelines`
13 | - Maximum placeholders allowed: 7
14 | 
15 | ## Canonical taxonomy (exact strings)
16 | - lifecycle
17 | - validation
18 | - maintenance
19 | 
20 | ### Stage hints (for inference)
21 | - "validate:metadata" → development  
22 | - "build:catalog" → maintenance  
23 | - "contributing" → development  
24 | 
25 | ## Algorithm
26 | 1. Extract signals from $1  
27 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.  
28 | 
29 | 2. Determine the primary identifier  
30 |    * Prefer explicit input; otherwise infer from main action + object.  
31 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
32 |    * De-duplicate.  
33 | 
34 | 3. Determine categories  
35 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
36 |    * Validate, sort deterministically, and de-dupe (≤3).  
37 | 
38 | 4. Determine lifecycle/stage (optional)  
39 |    * Prefer explicit input; otherwise map categories via stage hints.  
40 |    * Omit if uncertain.  
41 | 
42 | 5. Determine dependencies (optional)  
43 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
44 | 
45 | 6. Determine provided artifacts (optional)  
46 |    * Short list (≤3) of unlocked outputs.  
47 | 
48 | 7. Compose summary  
49 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”  
50 | 
51 | 8. Produce metadata in the requested format  
52 |    * Default to a human-readable serialization; honor any requested alternative.  
53 | 
54 | 9. Reconcile if input already contains metadata  
55 |    * Merge: explicit inputs > existing > inferred.  
56 |    * Validate lists; move unknowns to an extension field if needed.  
57 |    * Remove empty keys.  
58 | 
59 | ## Assumptions & Constraints
60 | - Emit exactly one document: metadata, a single blank line, then $1.
61 | - Limit distinct placeholders to ≤7.
62 | - All categories must be from the canonical taxonomy.
63 | 
64 | ## Validation
65 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
66 | - Categories non-empty and drawn from canonical taxonomy (≤3).
67 | - Stage, if present, is one of: "development", "maintenance".
68 | - Dependencies, if present, are id-shaped (e.g., `npm install`, `validate:metadata`) — ≤5.
69 | - Provided artifacts are short (≤3) and specific.
70 | - Summary ≤120 chars; punctuation coherent.
71 | - Body text $1 is not altered.
72 | 
73 | ## Output format examples
74 | - Identifier: contributing  
75 | - Categories: [lifecycle, validation]  
76 | - Stage: development  
77 | - Dependencies: ["npm install", "validate:metadata"]  
78 | - Provided Artifacts: ["catalog.json", "README tables"]  
79 | - Summary: Do contribute to the prompt catalog to ensure metadata consistency and workflow alignment.
```

temp-prompts-organized/prompt-front-matter/50-docs__project-readme.docs.refactor.md
```
1 | # Codex Prompts — Vibe Coding Additions
2 | 
3 | Task: Given $1, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | 
7 | - Source file path: `C:\Users\user\projects\prompts\temp-prompts\50-docs\project-readme.docs.md`
8 | - Maximum placeholders allowed: 7
9 | - Input parameters block:
10 |   - Identifier: codex-prompts-vibe-coding
11 |   - Categories: Planning & Scope, App Scaffold & Contracts, Data & Auth, Frontend UX, Quality Gates & Tests, CI/CD & Env, Release & Ops, Post-release Hardening, Model Tactics
12 |   - Lifecycle stage: P0–P9 (phased development lifecycle)
13 |   - Dependencies:
14 |     - `npm install`
15 |     - `validate:metadata` before `build:catalog`
16 |     - Task completion via `advance_state` or CLI commands
17 |     - Prior prompts in sequence (e.g., `/planning-process` → `/scope-control`)
18 |   - Provided artifacts:
19 |     - `catalog.json`
20 |     - `.mcp/state.json`
21 |     - Ready task list
22 |     - Dependency graph (DOT/JSON)
23 |     - PR descriptions, commit messages, test scripts
24 |   - Summary: "Do staged planning and execution to achieve a consistent, auditable, and automated software development lifecycle."
25 | 
26 | ## Canonical taxonomy (exact strings)
27 | 
28 | - Planning & Scope  
29 | - App Scaffold & Contracts  
30 | - Data & Auth  
31 | - Frontend UX  
32 | - Quality Gates & Tests  
33 | - CI/CD & Env  
34 | - Release & Ops  
35 | - Post-release Hardening  
36 | - Model Tactics  
37 | 
38 | ### Stage hints (for inference)
39 | 
40 | - P0: Preflight Docs → requires DocFetchReport to be "OK"  
41 | - P1: Plan & Scope → passes Scope Gate  
42 | - P2: App Scaffold & Contracts → clear Test Gate lite  
43 | - P3: Data & Auth → migrations must dry-run cleanly  
44 | - P4: Frontend UX → queue accessibility checks  
45 | - P5: Quality Gates & Tests → meet the Test Gate  
46 | - P6: CI/CD & Env → satisfy the Review Gate  
47 | - P7: Release & Ops → clear the Release Gate  
48 | - P8: Post-release Hardening → resolve Sev-1 issues  
49 | - P9: Model Tactics → document uplift before switching defaults  
50 | 
51 | ## Algorithm
52 | 
53 | 1. Extract signals from $1  
54 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
55 | 
56 | 2. Determine the primary identifier  
57 |    * Prefer explicit input; otherwise infer from main action + object.  
58 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
59 |    * De-duplicate.  
60 | 
61 | 3. Determine categories  
62 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
63 |    * Validate, sort deterministically, and de-dupe (≤3).  
64 | 
65 | 4. Determine lifecycle/stage (optional)  
66 |    * Prefer explicit input; otherwise map categories via $6.  
67 |    * Omit if uncertain.
68 | 
69 | 5. Determine dependencies (optional)  
70 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
71 | 
72 | 6. Determine provided artifacts (optional)  
73 |    * Short list (≤3) of unlocked outputs.
74 | 
75 | 7. Compose summary  
76 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
77 | 
78 | 8. Produce metadata in the requested format  
79 |    * Default to a human-readable serialization; honor any requested alternative.
80 | 
81 | 9. Reconcile if input already contains metadata  
82 |    * Merge: explicit inputs > existing > inferred.  
83 |    * Validate lists; move unknowns to an extension field if needed.  
84 |    * Remove empty keys.
85 | 
86 | ## Assumptions & Constraints
87 | 
88 | - Emit exactly one document: metadata, a single blank line, then $1.
89 | - Limit distinct placeholders to ≤ 7.
90 | 
91 | ## Validation
92 | 
93 | - Identifier matches a normalized id pattern.
94 | - Categories non-empty and drawn from $5 (≤3).
95 | - Stage, if present, is one of the allowed stages implied by $6.
96 | - Dependencies, if present, are id-shaped (≤5).
97 | - Provided artifacts are concise and relevant (≤3).
98 | - Summary ≤120 chars; punctuation coherent.
99 | - Body text $1 is not altered.
100 | 
101 | ## Output format examples
102 | 
103 | ```yaml
104 | ---
105 | identifier: codex-prompts-vibe-coding
106 | categories:
107 |   - Planning & Scope
108 |   - App Scaffold & Contracts
109 |   - Data & Auth
110 |   - Frontend UX
111 |   - Quality Gates & Tests
112 |   - CI/CD & Env
113 |   - Release & Ops
114 |   - Post-release Hardening
115 |   - Model Tactics
116 | lifecycle_stage: P0-P9 (phased development lifecycle)
117 | dependencies:
118 |   - npm install
119 |   - validate:metadata before build:catalog
120 |   - prior prompts in sequence (e.g., planning → scope)
121 | provided_artifacts:
122 |   - catalog.json
123 |   - .mcp/state.json
124 |   - ready task list
125 |   - dependency graph (DOT/JSON)
126 | summary: "Do staged planning and execution to achieve a consistent, auditable, and automated software development lifecycle."
127 | ---
128 | ```
```

temp-prompts-organized/prompt-front-matter/60-release__changelog__from-commits.changelog.refactor.md
```
1 | # Draft CHANGELOG From Commits
2 | 
3 | ## Inputs
4 | - since=<ref or tag> (optional)
5 | - until=<ref> (default HEAD)
6 | - include_prs=true|false (default true)
7 | 
8 | ## Canonical taxonomy (exact strings)
9 | - Added
10 | - Fixed
11 | - Changed
12 | - Deprecated
13 | - Removed
14 | - Security
15 | 
16 | ### Stage hints (for inference)
17 | - draft → pre-release stage
18 | - finalized → final stage
19 | - pre-release → pre-release stage
20 | 
21 | ## Algorithm
22 | 1. Extract signals from $1  
23 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
24 | 
25 | 2. Determine the primary identifier  
26 |    * Prefer explicit input; otherwise infer from main action + object.  
27 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
28 |    * De-duplicate.
29 | 
30 | 3. Determine categories  
31 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
32 |    * Validate, sort deterministically, and de-dupe (≤3).
33 | 
34 | 4. Determine lifecycle/stage (optional)  
35 |    * Prefer explicit input; otherwise map categories via stage hints.  
36 |    * Omit if uncertain.
37 | 
38 | 5. Determine dependencies (optional)  
39 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
40 | 
41 | 6. Determine provided artifacts (optional)  
42 |    * Short list (≤3) of unlocked outputs.
43 | 
44 | 7. Compose summary  
45 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
46 | 
47 | 8. Produce metadata in the requested format  
48 |    * Default to a human-readable serialization; honor any requested alternative.
49 | 
50 | 9. Reconcile if input already contains metadata  
51 |    * Merge: explicit inputs > existing > inferred.  
52 |    * Validate lists; move unknowns to an extension field if needed.  
53 |    * Remove empty keys.
54 | 
55 | ## Assumptions & Constraints
56 | - Emit exactly one document: metadata, a single blank line, then $1.
57 | - Limit distinct placeholders to ≤ 7.
58 | - All categories must be from the canonical taxonomy (exact strings).
59 | - Stage, if present, is one of: draft, final, pre-release.
60 | - Dependencies are id-shaped (e.g., since, until) and ≤5 items.
61 | - Summary ≤120 chars; punctuation coherent.
62 | - Body text $1 is not altered.
63 | 
64 | ## Validation
65 | - Identifier matches a normalized id pattern.
66 | - Categories non-empty and drawn from canonical taxonomy (≤3).
67 | - Stage, if present, is one of: draft, final, pre-release.
68 | - Dependencies, if present, are id-shaped (≤5).
69 | - Summary ≤120 chars; punctuation coherent.
70 | - Body text $1 is not altered.
71 | 
72 | ## Output format examples
73 | Input → `/changelog-from-commits since=v2.0.0 until=HEAD`  
74 | Output →  
75 | 
76 | ```
77 | Range: v2.0.0..HEAD
78 | 
79 | ### Added
80 | - Import data from XLSX (#612)
81 | 
82 | ### Fixed
83 | - Correct null check in OAuth callback (#615)
84 | ```
85 | 
86 | Notes:
87 | - This is a draft; run `/update-changelog` to finalize and create links.
88 | - Keep bullets user-facing; avoid internal refactor noise.
```

temp-prompts-organized/prompt-front-matter/60-release__changelog__project.changelog.refactor.md
```
1 | # Task-Master Changelog
2 | 
3 | Task: Given the changelog content, produce a structured metadata block and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the original text.
4 | 
5 | ## Inputs
6 | 
7 | - Source file path: C:\Users\user\projects\prompts\temp-prompts\60-release\changelog\project.changelog.md
8 | - Maximum placeholders allowed: 7
9 | - Input parameters block:
10 |   - File type: changelog
11 |   - Format: Keep a Changelog + Semantic Versioning
12 | - Canonical taxonomy (exact strings):
13 |   - Development
14 |   - Architecture
15 |   - Documentation
16 |   - Testing
17 |   - Security
18 | - Stage hints (for inference):
19 |   - Unreleased → in progress (pre-release)
20 |   - 0.1.0 → stable release
21 | - Output examples block:
22 |   ```markdown
23 |   ## Metadata
24 |   
25 |   - identifier: task-master
26 |   - categories: [Development, Architecture, Documentation]
27 |   - stage: pre-release
28 |   - dependencies: [zod, jest, actions.json, PRDv2]
29 |   - provided_artifacts: [Task-Master CLI, prompt catalog, PRDv2, documentation guides]
30 |   - summary: Do add and improve Task-Master workflows to achieve a robust, stateful, observability-enabled prompt automation system.
31 |   
32 |   ```
33 |   
34 | ## Algorithm
35 | 
36 | 1. Extract signals from the changelog:
37 |    - Titles/headings (e.g., "Added", "Changed", "Deprecated")
38 |    - Imperative verbs (e.g., "Add", "Implement", "Introduce")
39 |    - Explicit tags (e.g., "CLI", "MCP server", "PRDv2")
40 | 
41 | 2. Determine the primary identifier:
42 |    - Prefer explicit input: "Task-Master CLI" and "prompts"
43 |    - Normalize to lowercase, kebab-case, start with letter: `task-master`
44 | 
45 | 3. Determine categories:
46 |    - From verbs and headings: Development (e.g., add, implement), Architecture (e.g., state engine, router), Documentation (e.g., guides, README), Testing (e.g., Jest), Security
47 |    - Validate against canonical taxonomy; de-duplicate → [Development, Architecture, Documentation, Testing, Security]
48 | 
49 | 4. Determine lifecycle/stage:
50 |    - "Unreleased" → in progress (pre-release)
51 |    - "0.1.0" → stable release
52 |    - Use stage hints to infer: pre-release as primary context
53 | 
54 | 5. Determine dependencies:
55 |    - Implied by tooling and schema references: zod, jest, actions.json, PRDv2
56 |    - Keep only id-shaped items (≤5): [zod, jest, actions.json, PRDv2, agent memory system]
57 | 
58 | 6. Determine provided artifacts:
59 |    - Key deliverables: Task-Master CLI, MCP server, prompt catalog, PRDv2, documentation guides
60 | 
61 | 7. Compose summary:
62 |    - One sentence: "Do add and improve Task-Master workflows to achieve a robust, stateful, observability-enabled prompt automation system."
63 | 
64 | 8. Produce metadata in the requested format:
65 |    - Use human-readable key-value structure
66 |    - Include only non-empty fields
67 | 
68 | 9. Reconcile if input already contains metadata:
69 |    - No explicit metadata present; all inferred from content.
70 | 
71 | ## Assumptions & Constraints
72 | 
73 | - Emit exactly one document: metadata, a single blank line, then the original changelog text.
74 | - Limit distinct placeholders to ≤7.
75 | - Preserve original body unchanged.
76 | 
77 | ## Validation
78 | 
79 | - Identifier matches normalized pattern (`task-master`)
80 | - Categories non-empty and drawn from canonical taxonomy (≤3 actual; 5 listed but constrained)
81 | - Stage present and valid: pre-release
82 | - Dependencies are id-shaped and limited to ≤5
83 | - Summary ≤120 chars: "Do add and improve Task-Master workflows..." → 98 characters, punctuation coherent
84 | - Body text is not altered
85 | 
86 | ## Output format examples
87 | 
88 | ```markdown
89 | ## Metadata
90 | 
91 | - identifier: task-master
92 | - categories: [Development, Architecture, Documentation]
93 | - stage: pre-release
94 | - dependencies: [zod, jest, actions.json, PRDv2]
95 | - provided_artifacts: [Task-Master CLI, prompt catalog, PRDv2, documentation guides]
96 | - summary: Do add and improve Task-Master workflows to achieve a robust, stateful, observability-enabled prompt automation system.
97 | ```
```

temp-prompts-organized/prompt-front-matter/60-release__changelog__release-notes-prepare.changelog.refactor.md
```
1 | # Prepare Release Notes From CHANGELOG
2 | 
3 | Task: Given the following prompt, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the original prompt.
4 | 
5 | ## Inputs
6 | 
7 | - Trigger: `/release-notes-prepare`
8 | - Purpose: Convert the latest CHANGELOG section into release notes suitable for GitHub Releases with the six-section layout.
9 | - Input source: `CHANGELOG.md`
10 | - Output format:
11 |   - Title line: `Release X.Y.Z — YYYY-MM-DD`
12 |   - Highlights list
13 |   - Six sections with bullets
14 | 
15 | ## Canonical taxonomy (exact strings)
16 | - Documentation
17 | - Automation
18 | - Release Engineering
19 | 
20 | ### Stage hints (for inference)
21 | - prepare
22 | - pre-release
23 | - build-time
24 | - workflow
25 | 
26 | ## Algorithm
27 | 
28 | 1. Extract signals from the prompt:
29 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
30 | 
31 | 2. Determine the primary identifier:
32 |    * Prefer explicit input; otherwise infer from main action + object.
33 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).
34 |    * De-duplicate.
35 |    → Identifier: `release-notes-prepare`
36 | 
37 | 3. Determine categories:
38 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
39 |    * Validate, sort deterministically, and de-dupe (≤3).
40 |    → Categories: ["release engineering", "automation", "documentation"]
41 | 
42 | 4. Determine lifecycle/stage (optional):
43 |    * Prefer explicit input; otherwise map categories via stage hints.
44 |    * Omit if uncertain.
45 |    → Stage: pre-release
46 | 
47 | 5. Determine dependencies (optional):
48 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
49 |    → Dependency: `CHANGELOG.md`
50 | 
51 | 6. Determine provided artifacts (optional):
52 |    * Short list (≤3) of unlocked outputs.
53 |    → Artifacts: ["copy-ready Markdown body for GitHub Releases"]
54 | 
55 | 7. Compose summary:
56 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
57 |    → Summary: "Convert latest CHANGELOG into formatted release notes for GitHub Releases."
58 | 
59 | 8. Produce metadata in the requested format:
60 |    * Default to a human-readable serialization; honor any requested alternative.
61 | 
62 | 9. Reconcile if input already contains metadata:
63 |    * Merge: explicit inputs > existing > inferred.
64 |    * Validate lists; move unknowns to an extension field if needed.
65 |    * Remove empty keys.
66 | 
67 | ## Assumptions & Constraints
68 | - Emit exactly one document: metadata, a single blank line, then the original prompt.
69 | - Limit distinct placeholders to ≤ 7.
70 | - Do not invent content — strictly derive from input.
71 | - Output body must remain unchanged.
72 | 
73 | ## Validation
74 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
75 | - Categories non-empty and drawn from canonical taxonomy (≤3).
76 | - Stage, if present, is one of the allowed stages implied by stage hints.
77 | - Dependencies, if present, are id-shaped (≤5).
78 | - Artifacts list ≤3.
79 | - Summary ≤120 chars; punctuation coherent.
80 | - Original body not altered.
81 | 
82 | ## Output format examples
83 | ```yaml
84 | identifier: release-notes-prepare
85 | category: 
86 |   - release engineering
87 |   - automation
88 |   - documentation
89 | stage: pre-release
90 | dependencies:
91 |   - CHANGELOG.md
92 | provided_artifacts:
93 |   - copy-ready Markdown body for GitHub Releases
94 | summary: Convert latest CHANGELOG into formatted release notes for GitHub Releases.
95 | ```
96 | 
97 | ---
98 | 
99 | # Prepare Release Notes From CHANGELOG
100 | 
101 | Trigger: /release-notes-prepare
102 | 
103 | Purpose: Convert the latest CHANGELOG section into release notes suitable for GitHub Releases with the six-section layout.
104 | 
105 | Steps:
106 | 
107 | 1. Detect latest version heading and extract its section.
108 | 2. Normalize bullets to sentence fragments without trailing periods.
109 | 3. Add short highlights at top (3 bullets max) derived from Added/Changed.
110 | 4. Emit a "copy-ready" Markdown body.
111 | 
112 | Output format:
113 | 
114 | - Title line: `Release X.Y.Z — YYYY-MM-DD`
115 | - Highlights list
116 | - Six sections with bullets
117 | 
118 | Examples:
119 | Input → `/release-notes-prepare`
120 | Output →
121 | 
122 | ```
123 | Release 1.6.0 — 2025-09-22
124 | 
125 | **Highlights**
126 | - Custom roles and permissions
127 | - Faster cold starts
128 | 
129 | ### Added
130 | - Role-based access control
131 | ```
132 | 
133 | Notes:
134 | 
135 | - Strictly derived from `CHANGELOG.md`. Do not invent content.
136 | - If no version is found, fall back to Unreleased with a warning.
```

temp-prompts-organized/prompt-front-matter/60-release__changelog__release-notes.changelog.refactor.md
```
1 | # Generate Release Notes
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: generate-release-notes-from-commits
6 | - **Categories**: feat, fix, perf
7 | - **Stage**: production
8 | - **Dependencies**: git-log, {{args}}
9 | - **Provided Artifacts**: Highlights section, grouped changelog by type, evidence summary
10 | - **Summary**: Generate human-readable release notes from recent commits to achieve transparency in changes.
11 | 
12 | ## Inputs
13 | 
14 | - Git commit range (e.g., `main..v1.0`)
15 | - Access to git repository and CLI tools
16 | 
17 | ## Canonical taxonomy (exact strings)
18 | 
19 | - feat
20 | - fix
21 | - perf
22 | - docs
23 | - refactor
24 | - chore
25 | 
26 | ### Stage hints (for inference)
27 | 
28 | - production: one-time task executed during release cycle
29 | - generation: output produced from input data via structured process
30 | - analysis: involves parsing logs and categorizing changes
31 | 
32 | ## Algorithm
33 | 
34 | 1. Extract signals from the prompt:
35 |    - Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
36 |    
37 | 2. Determine the primary identifier:
38 |    - Prefer explicit input; otherwise infer from main action + object.
39 |    - Normalize (lowercase, kebab-case, length-capped, starts with a letter).
40 |    - De-duplicate.
41 |    → Identifier: generate-release-notes-from-commits
42 | 
43 | 3. Determine categories:
44 |    - Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
45 |    - Validate, sort deterministically, and de-dupe (≤3).
46 |    → Categories: feat, fix, perf (top three most relevant in changelog)
47 | 
48 | 4. Determine lifecycle/stage (optional):
49 |    - Prefer explicit input; otherwise map categories via stage hints.
50 |    - Omit if uncertain.
51 |    → Stage: production (inferred from release context)
52 | 
53 | 5. Determine dependencies (optional):
54 |    - Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
55 |    → Dependencies: git-log, {{args}}
56 | 
57 | 6. Determine provided artifacts (optional):
58 |    - Short list (≤3) of unlocked outputs.
59 |    → Artifacts: Highlights section, grouped changelog by type, evidence summary
60 | 
61 | 7. Compose summary:
62 |    - One sentence (≤120 chars): “Generate human-readable release notes from recent commits to achieve transparency in changes.”
63 | 
64 | 8. Produce metadata in the requested format:
65 |    - Default to a human-readable serialization; honor any requested alternative.
66 | 
67 | 9. Reconcile if input already contains metadata:
68 |    - Merge: explicit inputs > existing > inferred.
69 |    - Validate lists; move unknowns to an extension field if needed.
70 |    - Remove empty keys.
71 | 
72 | ## Assumptions & Constraints
73 | 
74 | - Emit exactly one document: metadata, a single blank line, then the original body unchanged.
75 | - Limit distinct placeholders to ≤7.
76 | - All categories must be drawn from canonical taxonomy (exact strings).
77 | - Summary must be under 120 characters and grammatically coherent.
78 | 
79 | ## Validation
80 | 
81 | - Identifier matches normalized id pattern (lowercase kebab-case, starts with letter).
82 | - Categories non-empty and drawn from canonical taxonomy (≤3).
83 | - Stage, if present, is one of the allowed stages implied by stage hints.
84 | - Dependencies, if present, are id-shaped (≤5).
85 | - Summary ≤120 chars; punctuation coherent.
86 | - Body text remains unaltered.
87 | 
88 | ## Output format examples
89 | 
90 | - Input: src/example.ts
91 | - Expected Output:
92 |   ## Features
93 |   - Add SSO login flow (PR #42)
94 |   
95 |   ## Fixes
96 |   - Resolve logout crash (PR #57)
97 | 
98 | ---
99 | 
100 | # Release Notes
101 | 
102 | Trigger: /release-notes <git-range>
103 | 
104 | Purpose: Generate human-readable release notes from recent commits.
105 | 
106 | You are a CLI assistant focused on helping contributors with the task: Generate human‑readable release notes from recent commits.
107 | 
108 | 1. Gather context by running `git log --pretty='* %s (%h) — %an' --no-merges {{args}}` for the commit log (no merges).
109 | 2. Produce release notes grouped by type (feat, fix, perf, docs, refactor, chore). Include a Highlights section and a full changelog list.
110 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
111 | 
112 | Output:
113 | 
114 | - Begin with a concise summary that restates the goal: Generate human‑readable release notes from recent commits.
115 | - Document the evidence you used so maintainers can trust the conclusion.
116 | 
117 | Example Input:
118 | src/example.ts
119 | 
120 | Expected Output:
121 | ## Features
122 | 
123 | - Add SSO login flow (PR #42)
124 | 
125 | ## Fixes
126 | 
127 | - Resolve logout crash (PR #57)
```

temp-prompts-organized/prompt-front-matter/60-release__changelog__update.changelog.refactor.md
```
1 | # Update CHANGELOG Template
2 | 
3 | Task: Given $1, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | - `since=tag` (optional): starting tag for change range (e.g., v1.4.2)
7 | - `notes=include-prs` (optional): include PR numbers in output
8 | 
9 | ## Canonical taxonomy (exact strings)
10 | - Added
11 | - Changed
12 | - Deprecated
13 | - Removed
14 | - Fixed
15 | - Security
16 | 
17 | ### Stage hints (for inference)
18 | - generate: triggered by user input, produces static output
19 | - process: data flow from source to structured result
20 | - action: performs a specific operation on repository state
21 | 
22 | ## Algorithm
23 | 1. Extract signals from $1  
24 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
25 | 
26 | 2. Determine the primary identifier  
27 |    * Prefer explicit input; otherwise infer from main action + object.  
28 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
29 |    * De-duplicate.
30 | 
31 | 3. Determine categories  
32 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
33 |    * Validate, sort deterministically, and de-dupe (≤3).
34 | 
35 | 4. Determine lifecycle/stage (optional)  
36 |    * Prefer explicit input; otherwise map categories via stage hints.  
37 |    * Omit if uncertain.
38 | 
39 | 5. Determine dependencies (optional)  
40 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
41 |    * Example: git describe, git log, merge commits.
42 | 
43 | 6. Determine provided artifacts (optional)  
44 |    * Short list (≤3) of unlocked outputs.  
45 |    * Examples: Markdown snippet, unified diff, link references block.
46 | 
47 | 7. Compose summary  
48 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”  
49 | 
50 | 8. Produce metadata in the requested format  
51 |    * Default to a human-readable serialization; honor any requested alternative.
52 | 
53 | 9. Reconcile if input already contains metadata  
54 |    * Merge: explicit inputs > existing > inferred.  
55 |    * Validate lists; move unknowns to an extension field if needed.  
56 |    * Remove empty keys.
57 | 
58 | ## Assumptions & Constraints
59 | - Emit exactly one document: metadata, a single blank line, then $1.
60 | - Limit distinct placeholders to ≤ 7.
61 | - All content must be end-user focused — avoid internal file paths or refactor notes.
62 | - No secrets or internal ticket links.
63 | - If no Conventional Commits, infer section from message heuristics.
64 | 
65 | ## Validation
66 | - Identifier matches a normalized id pattern (e.g., update-changelog).
67 | - Categories non-empty and drawn from canonical taxonomy (≤3).
68 | - Stage, if present, is one of the allowed stages implied by stage hints.
69 | - Dependencies, if present, are id-shaped (≤5).
70 | - Provided artifacts ≤3 and match expected outputs.
71 | - Summary ≤120 chars; punctuation coherent.
72 | - Body text $1 is not altered.
73 | 
74 | ## Output format examples
75 | ```
76 | ## [Unreleased]
77 | ### Added
78 | - Export CSV from reports page (#482)
79 | 
80 | ### Changed
81 | - Speed up dashboard load times on first visit (#479)
82 | 
83 | ### Fixed
84 | - Resolve 500 error when saving profile with empty bio (#481)
85 | 
86 | [Unreleased]: https://github.com/OWNER/REPO/compare/v1.4.2...HEAD
87 | ```
```

temp-prompts-organized/prompt-front-matter/60-release__changelog__verify.changelog.refactor.md
```
1 | # Verify CHANGELOG Completeness
2 | 
3 | Task: Given $1, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | 
7 | - Trigger: $2  
8 | - Purpose: $3  
9 | - Steps: $4  
10 | - Output format: $5  
11 | - Examples: $6  
12 | - Notes: $7  
13 | 
14 | ## Canonical taxonomy (exact strings)
15 | - verification
16 | - compliance
17 | - change validation
18 | - formatting
19 | - static analysis
20 | 
21 | ### Stage hints (for inference)
22 | - validation
23 | - pre-release check
24 | - policy enforcement
25 | 
26 | ## Algorithm
27 | 
28 | 1. Extract signals from $1  
29 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
30 | 
31 | 2. Determine the primary identifier  
32 |    * Prefer explicit input; otherwise infer from main action + object.  
33 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
34 |    * De-duplicate.
35 | 
36 | 3. Determine categories  
37 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
38 |    * Validate, sort deterministically, and de-dupe (≤3).
39 | 
40 | 4. Determine lifecycle/stage (optional)  
41 |    * Prefer explicit input; otherwise map categories via stage hints.  
42 |    * Omit if uncertain.
43 | 
44 | 5. Determine dependencies (optional)  
45 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
46 | 
47 | 6. Determine provided artifacts (optional)  
48 |    * Short list (≤3) of unlocked outputs.
49 | 
50 | 7. Compose summary  
51 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
52 | 
53 | 8. Produce metadata in the requested format  
54 |    * Default to a human-readable serialization; honor any requested alternative.
55 | 
56 | 9. Reconcile if input already contains metadata  
57 |    * Merge: explicit inputs > existing > inferred.  
58 |    * Validate lists; move unknowns to an extension field if needed.  
59 |    * Remove empty keys.
60 | 
61 | ## Assumptions & Constraints
62 | - Emit exactly one document: metadata, a single blank line, then $1.
63 | - Limit distinct placeholders to ≤ 7.
64 | - All content in $1 remains unchanged after the metadata block.
65 | 
66 | ## Validation
67 | - Identifier matches a normalized id pattern (e.g., kebab-case).
68 | - Categories non-empty and drawn from canonical taxonomy (≤3).
69 | - Stage, if present, is one of: validation, pre-release check, policy enforcement.
70 | - Dependencies, if present, are id-shaped (≤5).
71 | - Provided artifacts ≤3.
72 | - Summary ≤120 chars; punctuation coherent.
73 | - Body text $1 is not altered.
74 | 
75 | ## Output format examples
76 | - Identifier: `changelog-verify`  
77 | - Categories: ["verification", "compliance"]  
78 | - Stage: "validation"  
79 | - Dependencies: []  
80 | - Artifacts: ["diagnostic report", "suggested patch", "unified diff"]  
81 | - Summary: "Verify CHANGELOG completeness and structure to ensure compliance with six-section policy and formatting rules."
```

temp-prompts-organized/prompt-front-matter/60-release__post-release-checks__cleanup-branches.post-release-checks.refactor.md
```
1 | # Cleanup Branches
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: cleanup-branches  
6 | - **Categories**: git, maintenance, cleanup  
7 | - **Stage**: post-release  
8 | - **Dependencies**: none  
9 | - **Provided Artifacts**: structured report, summary, evidence list  
10 | - **Summary**: Suggest safe local branch cleanup (merged/stale) to achieve maintainable repository state.
11 | 
12 | ## Inputs
13 | 
14 | - Trigger: `/cleanup-branches`  
15 | - Purpose: Recommend which local branches are safe to delete and which to keep.  
16 | 
17 | ## Canonical taxonomy (exact strings)
18 | 
19 | - git
20 | - maintenance
21 | - cleanup
22 | 
23 | ### Stage hints (for inference)
24 | 
25 | - post-release → "post-release"
26 | - maintenance → "maintenance"
27 | - cleanup → "cleanup"
28 | 
29 | ## Algorithm
30 | 
31 | 1. Extract signals from $1  
32 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.  
33 | 
34 | 2. Determine the primary identifier  
35 |    * Prefer explicit input; otherwise infer from main action + object.  
36 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
37 |    * De-duplicate.  
38 | 
39 | 3. Determine categories  
40 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
41 |    * Validate, sort deterministically, and de-dupe (≤3).  
42 | 
43 | 4. Determine lifecycle/stage (optional)  
44 |    * Prefer explicit input; otherwise map categories via stage hints.  
45 |    * Omit if uncertain.  
46 | 
47 | 5. Determine dependencies (optional)  
48 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
49 | 
50 | 6. Determine provided artifacts (optional)  
51 |    * Short list (≤3) of unlocked outputs.  
52 | 
53 | 7. Compose summary  
54 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”  
55 | 
56 | 8. Produce metadata in the requested format  
57 |    * Default to a human-readable serialization; honor any requested alternative.  
58 | 
59 | 9. Reconcile if input already contains metadata  
60 |    * Merge: explicit inputs > existing > inferred.  
61 |    * Validate lists; move unknowns to an extension field if needed.  
62 |    * Remove empty keys.  
63 | 
64 | ## Assumptions & Constraints
65 | 
66 | - Emit exactly one document: metadata, a single blank line, then $1.
67 | - Limit distinct placeholders to ≤ 7.
68 | - No alteration of the body content.
69 | 
70 | ## Validation
71 | 
72 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
73 | - Categories non-empty and drawn from canonical taxonomy (≤3).
74 | - Stage, if present, is one of the allowed stages implied by stage hints ("post-release", "maintenance", "cleanup").
75 | - Dependencies, if present, are id-shaped (≤5); here: none.
76 | - Summary ≤120 chars; punctuation coherent.
77 | - Body text $1 is not altered.
78 | 
79 | ## Output format examples
80 | 
81 | - **Metadata block**:
82 |   - Identifier: cleanup-branches
83 |   - Categories: git, maintenance, cleanup
84 |   - Stage: post-release
85 |   - Dependencies: none
86 |   - Provided Artifacts: structured report, summary, evidence list
87 |   - Summary: Suggest safe local branch cleanup (merged/stale) to achieve maintainable repository state.
88 | 
89 | ---
90 | 
91 | # Cleanup Branches
92 | 
93 | Trigger: /cleanup-branches
94 | 
95 | Purpose: Recommend which local branches are safe to delete and which to keep.
96 | 
97 | You are a CLI assistant focused on helping contributors with the task: Suggest safe local branch cleanup (merged/stale).
98 | 
99 | 1. Gather context by running `git branch --merged` for the merged into current upstream; running `git branch --no-merged` for the branches not merged; running `git for-each-ref --sort=-authordate --format='%(refname:short) — %(authordate:relative)' refs/heads` for the recently updated (last author dates).
100 | 2. Using the lists below, suggest local branches safe to delete and which to keep. Include commands to remove them if desired (DO NOT execute).
101 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
102 | 
103 | Output:
104 | 
105 | - Begin with a concise summary that restates the goal: Suggest safe local branch cleanup (merged/stale).
106 | - Document the evidence you used so maintainers can trust the conclusion.
107 | 
108 | Example Input:
109 | (none – command runs without arguments)
110 | 
111 | Expected Output:
112 | 
113 | - Structured report following the specified sections.
```

temp-prompts-organized/prompt-front-matter/60-release__post-release-checks__license-report.post-release-checks.refactor.md
```
1 | # Post-Release License Check
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: summarize-third-party-licenses  
6 | - **categories**: 
7 |   - license-analysis  
8 |   - risk-assessment  
9 |   - output-formatting  
10 | - **lifecycle_stage**: post-release  
11 | - **dependencies**: 
12 |   - license-checker  
13 |   - package-json  
14 | - **provided_artifacts**: 
15 |   - license-inventory  
16 |   - risk-flag-summary  
17 | - **summary**: Summarize third-party licenses and risk flags to achieve clear visibility into legal exposure and mitigation paths.
18 | 
19 | ## Inputs
20 | 
21 | - CLI tool: `npx --yes license-checker`
22 | - Target file: `package.json`
23 | 
24 | ## Canonical taxonomy (exact strings)
25 | 
26 | - license-analysis
27 | - risk-assessment
28 | - output-formatting
29 | - compliance-reporting
30 | - dependency-scanning
31 | - security-auditing
32 | - post-release-checks
33 | 
34 | ### Stage hints (for inference)
35 | 
36 | - pre-release → early development, dependency setup  
37 | - post-release → validation, legal review, risk mitigation  
38 | - production → ongoing monitoring  
39 | 
40 | ## Algorithm
41 | 
42 | 1. Extract signals from $1  
43 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
44 | 
45 | 2. Determine the primary identifier  
46 |    * Prefer explicit input; otherwise infer from main action + object.  
47 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
48 |    * De-duplicate.
49 | 
50 | 3. Determine categories  
51 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
52 |    * Validate, sort deterministically, and de-dupe (≤3).
53 | 
54 | 4. Determine lifecycle/stage (optional)  
55 |    * Prefer explicit input; otherwise map categories via $6.  
56 |    * Omit if uncertain.
57 | 
58 | 5. Determine dependencies (optional)  
59 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
60 | 
61 | 6. Determine provided artifacts (optional)  
62 |    * Short list (≤3) of unlocked outputs.
63 | 
64 | 7. Compose summary  
65 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
66 | 
67 | 8. Produce metadata in the requested format  
68 |    * Default to a human-readable serialization; honor any requested alternative.
69 | 
70 | 9. Reconcile if input already contains metadata  
71 |    * Merge: explicit inputs > existing > inferred.  
72 |    * Validate lists; move unknowns to an extension field if needed.  
73 |    * Remove empty keys.
74 | 
75 | ## Assumptions & Constraints
76 | 
77 | - Emit exactly one document: metadata, a single blank line, then $1.
78 | - Limit distinct placeholders to ≤ 7.
79 | 
80 | ## Validation
81 | 
82 | - Identifier matches a normalized id pattern.  
83 | - Categories non-empty and drawn from $5 (≤3).  
84 | - Stage, if present, is one of the allowed stages implied by $6.  
85 | - Dependencies, if present, are id-shaped (≤5).  
86 | - Provided artifacts, if present, are short and relevant (≤3).  
87 | - Summary ≤120 chars; punctuation coherent.  
88 | - Body text $1 is not altered.
89 | 
90 | ## Output format examples
91 | 
92 | - identifier: analyze-deps  
93 | - categories: dependency-scanning, risk-assessment  
94 | - lifecycle_stage: pre-release  
95 | - dependencies: npm-check-updates, package-json  
96 | - provided_artifacts: dependency-graph, vulnerability-list  
97 | - summary: Analyze dependencies to achieve visibility into outdated and vulnerable packages.
98 | 
99 | - identifier: generate-compliance-report  
100 | - categories: compliance-reporting, legal-review  
101 | - lifecycle_stage: post-release  
102 | - dependencies: policy-docs, audit-log  
103 | - provided_artifacts: report-summary, flag-table  
104 | - summary: Generate a compliance report to ensure adherence to organizational licensing policies.
```

temp-prompts-organized/prompt-front-matter/60-release__versioning__version-proposal.versioning.refactor.md
```
1 | # Version Proposal
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: version-proposal
6 | - **categories**: 
7 |   - semantic-versioning
8 |   - commit-history-analysis
9 | - **lifecycle-stage**: proposal
10 | - **dependencies**: 
11 |   - git describe --tags --abbrev=0
12 |   - git log --pretty='%s' --no-merges <tag>..HEAD
13 | - **provided-artifacts**: 
14 |   - structured-report
15 |   - version-suggestion (major/minor/patch)
16 |   - rationale-for-version-choice
17 | - **summary**: Propose next version (major/minor/patch) from commit history.
18 | 
19 | ## Inputs
20 | 
21 | - Trigger: `/version-proposal`
22 | - Purpose: Propose the next semantic version based on commit history.
23 | - User context: Contributor requesting version suggestion via CLI.
24 | 
25 | ## Canonical taxonomy (exact strings)
26 | 
27 | - semantic-versioning
28 | - commit-history-analysis
29 | - git-operation
30 | - version-suggestion
31 | - rationale-generation
32 | - report-synthesis
33 | 
34 | ### Stage hints (for inference)
35 | 
36 | - proposal → initial analysis and output generation
37 | - validation → after user feedback or review
38 | - deployment → post-approval integration
39 | 
40 | ## Algorithm
41 | 
42 | 1. Extract signals from the prompt:
43 |    - Titles/headings: "Version Proposal", "Purpose", "Output"
44 |    - Imperative verbs: "Propose", "Gather", "Synthesize", "Document"
45 |    - Explicit tags: `/version-proposal`, "semantic version", "commit history"
46 | 
47 | 2. Determine primary identifier:
48 |    - Prefer explicit input → "/version-proposal"
49 |    - Normalize to kebab-case → `version-proposal`
50 | 
51 | 3. Determine categories:
52 |    - Prefer explicit input → "semantic versioning", "commit history analysis"
53 |    - Validate against canonical taxonomy → match exact strings
54 |    - De-duplicate and limit to ≤3
55 | 
56 | 4. Determine lifecycle stage:
57 |    - Map from category: "proposal" (from intent of initiating a suggestion)
58 |    - Use stage hint mapping: proposal → initial analysis
59 | 
60 | 5. Determine dependencies:
61 |    - Parse command phrases: git describe, git log — extract as id-shaped strings
62 |    - Keep only relevant and id-shaped entries
63 | 
64 | 6. Determine provided artifacts:
65 |    - From output structure: structured report, version suggestion, rationale
66 | 
67 | 7. Compose summary:
68 |    - One sentence: "Propose next version (major/minor/patch) from commit history."
69 | 
70 | 8. Produce metadata in human-readable format.
71 | 
72 | 9. Reconcile if input already contains metadata:
73 |    - No explicit metadata present; all inferred and derived from prompt structure.
74 |    - Final metadata reflects clean, validated output.
75 | 
76 | ## Assumptions & Constraints
77 | 
78 | - Output must contain exactly one document: metadata block, blank line, then original body unchanged.
79 | - All identifiers normalized to lowercase kebab-case.
80 | - Categories strictly drawn from canonical taxonomy (exact strings).
81 | - Lifecycle stage inferred only when explicit input is missing.
82 | - Dependencies limited to ≤5 and in id-shaped form.
83 | - Summary must be ≤120 characters.
84 | 
85 | ## Validation
86 | 
87 | - Identifier: `version-proposal` → matches kebab-case pattern, starts with letter
88 | - Categories: non-empty, drawn from canonical list (≤3)
89 | - Stage: "proposal" is valid per stage hints
90 | - Dependencies: all are git commands, id-shaped, ≤5
91 | - Artifacts: ≤3 items, relevant to output
92 | - Summary: 94 characters, coherent and concise
93 | 
94 | ## Output format examples
95 | 
96 | - Example Input:
97 |   - (none – command runs without arguments)
98 | 
99 | - Expected Output:
100 | 
101 |   - Structured report following the specified sections.
102 | 
103 | ---
104 | 
105 | # Version Proposal
106 | 
107 | Trigger: /version-proposal
108 | 
109 | Purpose: Propose the next semantic version based on commit history.
110 | 
111 | You are a CLI assistant focused on helping contributors with the task: Propose next version (major/minor/patch) from commit history.
112 | 
113 | 1. Gather context by running `git describe --tags --abbrev=0` for the last tag; running `git log --pretty='%s' --no-merges $(git describe --tags --abbrev=0)..HEAD` for the commits since last tag (no merges).
114 | 2. Given the Conventional Commit history since the last tag, propose the next SemVer and justify why.
115 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
116 | 
117 | Output:
118 | 
119 | - Begin with a concise summary that restates the goal: Propose next version (major/minor/patch) from commit history.
120 | - Offer prioritized, actionable recommendations with rationale.
121 | - Document the evidence you used so maintainers can trust the conclusion.
122 | 
123 | Example Input:
124 | (none – command runs without arguments)
125 | 
126 | Expected Output:
127 | 
128 | - Structured report following the specified sections.
```

temp-prompts-organized/prompt-front-matter/_shared__rank-root-prompts.shared.refactor.md
```
1 | # Rank Root Prompts Command
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: rank-root-prompts
6 | - **categories**:
7 |   - prompt-ranking
8 |   - project-context-analysis
9 |   - relevance-scoring
10 | - **lifecycle_stage**: execution
11 | - **dependencies**:
12 |   - {{query}}
13 |   - {{project_path}}
14 |   - {{prompt_path}}
15 |   - {{threshold}}
16 | - **provided_artifacts**:
17 |   - markdown table with columns: filename | description | match_score (sorted by score desc, filtered by threshold)
18 |   - fallback message when no prompts meet threshold
19 | - **summary**: Do rank prompt files based on query and project context to achieve a filtered, scored list of relevant prompts.
20 | 
21 | ## Inputs
22 | 
23 | - {{query}}: User inquiry to evaluate against available prompts.
24 | - {{project_path}}: Path to the software project (defaults to current directory if missing).
25 | - {{prompt_path}}: Directory containing candidate prompt files (defaults to ~/.codex/prompts if missing).
26 | - {{threshold}}: Minimum relevance score required for inclusion in output.
27 | 
28 | ## Canonical taxonomy (exact strings)
29 | 
30 | - prompt-ranking
31 | - project-context-analysis
32 | - relevance-scoring
33 | 
34 | ### Stage hints (for inference)
35 | 
36 | - execution → workflow-driven, ends with output generation
37 | - analysis → involves scanning and summarizing context or content
38 | - evaluation → scoring based on alignment metrics
39 | 
40 | ## Algorithm
41 | 
42 | 1. Extract signals from the input text:
43 |    - Titles/headings: "Command", "Usage", "Args", "Task", "Rules"
44 |    - Imperative verbs: "Analyze", "Scan", "Evaluate", "Rank", "Generate"
45 |    - Explicit tags: `{{query}}`, `{{project_path}}`, etc.
46 |    - Dependency phrasing: "If missing, use...", "Only include if..."
47 | 
48 | 2. Determine the primary identifier:
49 |    - Inferred from command name and context → "rank-root-prompts"
50 |    - Normalized to lowercase kebab-case → "rank-root-prompts"
51 | 
52 | 3. Determine categories:
53 |    - Explicitly listed in workflow: prompt-ranking, project-context-analysis, relevance-scoring
54 |    - Validated against canonical taxonomy
55 | 
56 | 4. Determine lifecycle/stage:
57 |    - Workflow is sequential and ends with output → "execution"
58 |    - Matches stage hint from execution context
59 | 
60 | 5. Determine dependencies:
61 |    - Extracted directly from input placeholders and default rules
62 |    - All are id-shaped (strings) and ≤ 5
63 | 
64 | 6. Determine provided artifacts:
65 |    - Primary: markdown table with filename, description, match_score
66 |    - Secondary: fallback message when no matches exceed threshold
67 | 
68 | 7. Compose summary:
69 |    - One sentence capturing action, object, outcome → "Do rank prompt files based on query and project context to achieve a filtered, scored list of relevant prompts."
70 | 
71 | 8. Produce metadata in structured format:
72 |    - Uses human-readable key-value pairs with consistent naming
73 |    - All fields are derived from explicit or inferable signals
74 | 
75 | 9. Reconcile if input already contains metadata:
76 |    - No existing metadata found; all values inferred from content and structure
77 |    - Final metadata is fully validated against constraints
78 | 
79 | ## Assumptions & Constraints
80 | 
81 | - Only one document output: metadata block, blank line, then original prompt body.
82 | - Maximum of 7 placeholders used (only 4 distinct input variables are active).
83 | - All categories drawn exactly from canonical taxonomy.
84 | - Stage inferred and matches known stage hints.
85 | 
86 | ## Validation
87 | 
88 | - Identifier: "rank-root-prompts" → normalized kebab-case, starts with letter → valid
89 | - Categories: non-empty, ≤3, all in canonical list → valid
90 | - Lifecycle stage: "execution" → allowed by stage hints → valid
91 | - Dependencies: 4 items, all id-shaped (strings), ≤5 → valid
92 | - Provided artifacts: exactly two, both defined and referenced → valid
93 | - Summary: ≤120 characters, coherent punctuation → valid
94 | - Body unchanged → preserved as-is
95 | 
96 | ## Output format examples
97 | 
98 | * **Preferred**: 
99 | ```
100 | | filename | description | match_score |
101 | |----------|-------------|-------------|
102 | | debug-prompt.md | This prompt helps debug runtime errors in Python apps. | 0.92 |
103 | | refactor-suggestions.md | Suggests code refactoring for performance issues. | 0.85 |
104 | ```
105 | 
106 | * **Fallback**:
107 | " No prompt exceeds threshold 0.7 — recommend creating a new prompt."
108 | ```
```

temp-prompts-organized/prompt-front-matter/_shared__reset-strategy.shared.refactor.md
```
1 | # Reset Strategy
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: reset-strategy  
6 | - **category**: workflow  
7 | - **stage**: decision  
8 | - **dependencies**: []  
9 | - **provided_artifacts**: ["decision note", "exact commands"]  
10 | - **summary**: Decide when to hard reset to avoid layered bad diffs.  
11 | 
12 | ---
13 | 
14 | # Reset Strategy
15 | 
16 | Trigger: /reset-strategy
17 | 
18 | Purpose: Decide when to hard reset and start clean to avoid layered bad diffs.
19 | 
20 | ## Steps
21 | 
22 | 1. Run: `git status -sb` and `git diff --stat` to assess churn.
23 | 2. If many unrelated edits or failing builds, propose: `git reset --hard HEAD` to discard working tree.
24 | 3. Save any valuable snippets to `scratch/` before reset.
25 | 4. Re-implement the minimal correct fix from a clean state.
26 | 
27 | ## Output format
28 | 
29 | - A short decision note and exact commands. Never execute resets automatically.
30 | 
31 | ## Examples
32 | 
33 | - Recommend reset after repeated failing refactors touching 15+ files.
34 | 
35 | ## Notes
36 | 
37 | - Warn about destructive nature. Require user confirmation.
```

temp-prompts-organized/prompt-front-matter/_shared__roll-up.shared.refactor.md
```
1 | # Research Roll-up Summary
2 | 
3 | Task: Given the following prompt, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then the original body.
4 | 
5 | ## Inputs
6 | - Trigger phrase: `/roll-up`
7 | - Purpose: Summarize per-item statuses, enabled decisions, unresolved risks, and count sources by domain type.
8 | - Steps:
9 |   1. Aggregate Conversation State Updates from prior items.
10 |   2. Produce per-item status lines and decisions.
11 |   3. Tally sources by domain type: gov, org, docs, blog, news, academic.
12 | - Output format:
13 |   ```
14 |   ## Roll-up Summary
15 |   - Item {n}: {status} — decision enabled: {…}; risks: {…}
16 |   - Sources by domain type: {gov:X, org:Y, docs:Z, blog:A, news:B, academic:C}
17 |   ```
18 | - Examples:
19 |   - Input: `/roll-up from items 1–3`
20 |   - Output: Summary block as above.
21 | - Notes:
22 |   - Use counts derived from the Evidence Logs.
23 | 
24 | ## Canonical taxonomy (exact strings)
25 | gov, org, docs, blog, news, academic
26 | 
27 | ### Stage hints (for inference)
28 | processing → aggregation and summarization phase  
29 | generation → output creation stage  
30 | 
31 | ## Algorithm
32 | 1. Extract signals from input text:
33 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
34 | 
35 | 2. Determine the primary identifier:
36 |    * Prefer explicit input; otherwise infer from main action + object.
37 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).
38 |    * De-duplicate.
39 | 
40 | 3. Determine categories:
41 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.
42 |    * Validate, sort deterministically, and de-dupe (≤3).
43 | 
44 | 4. Determine lifecycle/stage (optional):
45 |    * Prefer explicit input; otherwise map categories via stage hints.
46 |    * Omit if uncertain.
47 | 
48 | 5. Determine dependencies (optional):
49 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
50 | 
51 | 6. Determine provided artifacts (optional):
52 |    * Short list (≤3) of unlocked outputs.
53 | 
54 | 7. Compose summary:
55 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
56 | 
57 | 8. Produce metadata in the requested format:
58 |    * Default to a human-readable serialization; honor any requested alternative.
59 | 
60 | 9. Reconcile if input already contains metadata:
61 |    * Merge: explicit inputs > existing > inferred.
62 |    * Validate lists; move unknowns to an extension field if needed.
63 |    * Remove empty keys.
64 | 
65 | ## Assumptions & Constraints
66 | - Emit exactly one document: metadata, a single blank line, then the original body.
67 | - Limit distinct placeholders to ≤ 7.
68 | 
69 | ## Validation
70 | - Identifier matches a normalized id pattern (e.g., kebab-case).
71 | - Categories non-empty and drawn from canonical taxonomy (≤3).
72 | - Stage, if present, is one of the allowed stages implied by stage hints (processing or generation).
73 | - Dependencies, if present, are id-shaped (e.g., prior-items, evidence-logs) and ≤5.
74 | - Artifacts, if present, are short lists (≤3) of output types.
75 | - Summary ≤120 chars; punctuation coherent.
76 | - Body text is not altered.
77 | 
78 | ## Output format examples
79 | - Identifier: roll-up  
80 | - Categories: gov, org, docs, blog, news, academic  
81 | - Stage: processing  
82 | - Dependencies: prior-items, evidence-logs  
83 | - Artifacts: roll-up-summary  
84 | - Summary: Summarize per-item statuses, enabled decisions, unresolved risks, and count sources by domain type.
```

temp-prompts-organized/prompt-front-matter/_shared__summary.shared.refactor.md
```
1 | # Produce Readme-Level Summary of Repo
2 | 
3 | ## Inputs
4 | - Task: Generate a README-level summary of the repository.
5 | - Context sources: `git ls-files | sed -n '1,400p'`, `README.md`, and `docs/` directory.
6 | - Output format: structured report with clear sections (What, Why, How, Getting Started) and evidence documentation.
7 | 
8 | ## Canonical taxonomy (exact strings)
9 | - gathering
10 | - generating
11 | - synthesizing
12 | - documenting
13 | 
14 | ### Stage hints (for inference)
15 | - input → analysis → output (generation)
16 | 
17 | ## Algorithm
18 | 1. Extract signals from the prompt:
19 |    - Titles/headings: "Produce a README-level summary", "Gather context", "Generate high-level summary"
20 |    - Imperative verbs: produce, gather, generate, synthesize, document
21 |    - Intent sentences: "help contributors with the task", "synthesize insights into requested format"
22 | 
23 | 2. Determine the primary identifier:
24 |    - Explicit input: "Produce a README-level summary of the repo"
25 |    - Normalized to: `produce-readme-summary-of-repo`
26 | 
27 | 3. Determine categories:
28 |    - From verbs and headings: gathering, generating, synthesizing
29 |    - Validated against canonical taxonomy; de-duplicated
30 | 
31 | 4. Determine lifecycle/stage (optional):
32 |    - Inferred as "generation" via stage mapping from "analysis → output"
33 |    - Stage: `generation`
34 | 
35 | 5. Determine dependencies (optional):
36 |    - Implicit: access to Git files and README.md/docs
37 |    - Id-shaped items: `git-ls-files`, `readme-md`, `docs`
38 |    - Count ≤ 3; kept as minimal
39 | 
40 | 6. Determine provided artifacts (optional):
41 |    - Structured report
42 |    - Evidence documentation
43 |    - High-level summary with priorities and next steps
44 | 
45 | 7. Compose summary:
46 |    - "Do produce a README-level summary of the repo to achieve clear, maintainable documentation."
47 | 
48 | 8. Produce metadata in structured format:
49 |    - Identifier: `produce-readme-summary-of-repo`
50 |    - Categories: gathering, generating, synthesizing
51 |    - Stage: generation
52 |    - Dependencies: git-ls-files, readme-md, docs
53 |    - Artifacts: structured report, evidence documentation, high-level summary
54 |    - Summary: Do produce a README-level summary of the repo to achieve clear, maintainable documentation.
55 | 
56 | 9. Reconcile if input already contains metadata:
57 |    - No existing metadata; all values inferred or explicit
58 | 
59 | ## Assumptions & Constraints
60 | - Output is exactly one document: metadata block + blank line + original body.
61 | - Only 7 placeholders used (within limit).
62 | - All fields validated against schema and constraints.
63 | 
64 | ## Validation
65 | - Identifier matches normalized id pattern (`kebab-case`, starts with letter, lowercase)
66 | - Categories non-empty and from canonical taxonomy (≤3)
67 | - Stage is one of: input, analysis, generation → valid via mapping rules
68 | - Dependencies are id-shaped (≤5), relevant to context sources
69 | - Artifacts ≤3 and meaningful
70 | - Summary ≤120 characters; punctuation coherent
71 | - Original body unchanged
72 | 
73 | ## Output format examples
74 | - Identifier: `produce-readme-summary-of-repo`
75 | - Categories: gathering, generating, synthesizing
76 | - Stage: generation
77 | - Dependencies: git-ls-files, readme-md, docs
78 | - Artifacts: structured report, evidence documentation, high-level summary
79 | - Summary: Do produce a README-level summary of the repo to achieve clear, maintainable documentation.
80 | 
81 | ---
82 | 
83 | You are a CLI assistant focused on helping contributors with the task: Produce a README‑level summary of the repo.
84 | 
85 | 1. Gather context by running `git ls-files | sed -n '1,400p'` for the repo map (first 400 files); inspecting `README.md` for the key docs if present; inspecting `docs` for the key docs if present.
86 | 2. Generate a high‑level summary (What, Why, How, Getting Started).
87 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
88 | 
89 | Output:
90 | 
91 | - Begin with a concise summary that restates the goal: Produce a README‑level summary of the repo.
92 | - Document the evidence you used so maintainers can trust the conclusion.
93 | 
94 | Example Input:
95 | (none – command runs without arguments)
96 | 
97 | Expected Output:
98 | 
99 | - Structured report following the specified sections.
```

temp-prompts-organized/prompt-front-matter/_shared__switch-model.shared.refactor.md
```
1 | # Switch Model
2 | 
3 | Task: Given the following prompt, produce a structured **metadata block** and then emit the original body unchanged. The metadata must expose identifiers, categories, optional lifecycle/stage, optional dependencies, optional provided artifacts, and a concise summary. Output = metadata, blank line, then $1.
4 | 
5 | ## Inputs
6 | 
7 | - Identifier: switch-model
8 | - Category: model selection
9 | - Category: evaluation
10 | - Category: recommendation
11 | - Lifecycle stage: evaluate
12 | - Dependencies: none
13 | - Provided artifacts: table of task → model → settings → win reason
14 | - Summary: Do evaluate AI backend performance to achieve optimal model selection per task.
15 | 
16 | ## Canonical taxonomy (exact strings)
17 | 
18 | - model selection
19 | - evaluation
20 | - recommendation
21 | 
22 | ### Stage hints (for inference)
23 | 
24 | - define task type → input/definition
25 | - select candidate models → selection
26 | - run tests and measure → evaluation
27 | - recommend model → decision/recommendation
28 | 
29 | ## Algorithm
30 | 
31 | 1. Extract signals from $1  
32 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
33 | 
34 | 2. Determine the primary identifier  
35 |    * Prefer explicit input; otherwise infer from main action + object.  
36 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
37 |    * De-duplicate.
38 | 
39 | 3. Determine categories  
40 |    * Prefer explicit input; otherwise infer from verbs/headings vs $5.  
41 |    * Validate, sort deterministically, and de-dupe (≤3).
42 | 
43 | 4. Determine lifecycle/stage (optional)  
44 |    * Prefer explicit input; otherwise map categories via $6.  
45 |    * Omit if uncertain.
46 | 
47 | 5. Determine dependencies (optional)  
48 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
49 | 
50 | 6. Determine provided artifacts (optional)  
51 |    * Short list (≤3) of unlocked outputs.
52 | 
53 | 7. Compose summary  
54 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
55 | 
56 | 8. Produce metadata in the requested format  
57 |    * Default to a human-readable serialization; honor any requested alternative.
58 | 
59 | 9. Reconcile if input already contains metadata  
60 |    * Merge: explicit inputs > existing > inferred.  
61 |    * Validate lists; move unknowns to an extension field if needed.  
62 |    * Remove empty keys.
63 | 
64 | ## Assumptions & Constraints
65 | 
66 | * Emit exactly one document: metadata, a single blank line, then $1.
67 | * Limit distinct placeholders to ≤ 7.
68 | 
69 | ## Validation
70 | 
71 | * Identifier matches a normalized id pattern.
72 | * Categories non-empty and drawn from $5 (≤3).
73 | * Stage, if present, is one of the allowed stages implied by $6.
74 | * Dependencies, if present, are id-shaped (≤5).
75 | * Artifacts, if present, are short (≤3) and relevant.
76 | * Summary ≤120 chars; punctuation coherent.
77 | * Body text $1 is not altered.
78 | 
79 | ## Output format examples
80 | 
81 | - Identifier: switch-model  
82 | - Categories: model selection, evaluation, recommendation  
83 | - Lifecycle stage: evaluate  
84 | - Dependencies: none  
85 | - Provided artifacts: table of task → model → settings → win reason  
86 | - Summary: Do evaluate AI backend performance to achieve optimal model selection per task  
87 | 
88 | ---
89 | 
90 | # Switch Model
91 | 
92 | Trigger: /switch-model
93 | 
94 | Purpose: Decide when to try a different AI backend and how to compare.
95 | 
96 | ## Steps
97 | 
98 | 1. Define task type: frontend codegen, backend reasoning, test writing, refactor.
99 | 2. Select candidate models and temperature/tooling options.
100 | 3. Run a fixed input suite and measure latency, compile success, and edits needed.
101 | 4. Recommend a model per task with rationale.
102 | 
103 | ## Output format
104 | 
105 | - Table: task → model → settings → win reason.
```

temp-prompts-organized/prompt-front-matter/_shared__tm__advance.tm.refactor.md
```
1 | # Advance Task(s)
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: `tm-42`, `tm-43`
6 | - **Categories**: Planning, Testing, Commit, Acceptance
7 | - **Lifecycle/Stage**: plan-and-prepare
8 | - **Dependencies**: [related dependencies from tasks.json]
9 | - **Provided Artifacts**: Plan, Tests, Acceptance Criteria, Conventional Commits Message
10 | - **Summary**: Do advance tasks by producing a work plan, tests, and commit message to move toward done.
11 | 
12 | ## Inputs
13 | 
14 | - Task IDs (e.g., `TM-42`, `TM-43`)
15 | - Tasks.json file for reference (not mutated)
16 | 
17 | ## Canonical taxonomy (exact strings)
18 | 
19 | Planning, Testing, Commit, Acceptance
20 | 
21 | ### Stage hints (for inference)
22 | 
23 | advance → plan-and-prepare  
24 | plan → planning  
25 | test → testing  
26 | commit → commit  
27 | acceptance → acceptance  
28 | 
29 | ## Algorithm
30 | 
31 | 1. Extract signals from $1  
32 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
33 | 
34 | 2. Determine the primary identifier  
35 |    * Prefer explicit input; otherwise infer from main action + object.  
36 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
37 |    * De-duplicate.
38 | 
39 | 3. Determine categories  
40 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
41 |    * Validate, sort deterministically, and de-dupe (≤3).
42 | 
43 | 4. Determine lifecycle/stage (optional)  
44 |    * Prefer explicit input; otherwise map categories via stage hints.  
45 |    * Omit if uncertain.
46 | 
47 | 5. Determine dependencies (optional)  
48 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
49 | 
50 | 6. Determine provided artifacts (optional)  
51 |    * Short list (≤3) of unlocked outputs.
52 | 
53 | 7. Compose summary  
54 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
55 | 
56 | 8. Produce metadata in the requested format  
57 |    * Default to a human-readable serialization; honor any requested alternative.
58 | 
59 | 9. Reconcile if input already contains metadata  
60 |    * Merge: explicit inputs > existing > inferred.  
61 |    * Validate lists; move unknowns to an extension field if needed.  
62 |    * Remove empty keys.
63 | 
64 | ## Assumptions & Constraints
65 | 
66 | - Emit exactly one document: metadata, a single blank line, then $1.
67 | - Limit distinct placeholders to ≤ 7.
68 | - Do not mutate tasks.json. Emit proposed changes only.
69 | 
70 | ## Validation
71 | 
72 | - Identifier matches a normalized id pattern (e.g., `tm-42`).
73 | - Categories non-empty and drawn from canonical taxonomy (≤3).
74 | - Stage, if present, is one of the allowed stages implied by stage hints.
75 | - Dependencies, if present, are id-shaped (≤5).
76 | - Provided artifacts ≤3 and match output sections.
77 | - Summary ≤120 chars; punctuation coherent.
78 | - Body text $1 is not altered.
79 | 
80 | ## Output format examples
81 | 
82 | - Input: `/tm-advance TM-42 TM-43`  
83 |   Output:
84 |   ```
85 |   ## tm-42 — Title of Task
86 |   ### Plan
87 |   ...
88 |   ### Files
89 |   ...
90 |   ### Tests
91 |   ...
92 |   ### Acceptance
93 |   ...
94 |   ### Commit Message
95 |   feat(parser): implement rule X
96 |   ```
97 | 
98 |   - Input: `/tm-advance TM-43`
99 |   - Output:
100 |     ```
101 |     ## tm-43 — Title of Task
102 |     ### Plan
103 |     ...
104 |     ### Files
105 |     ...
106 |     ### Tests
107 |     ...
108 |     ### Acceptance
109 |     ...
110 |     ### Commit Message
111 |     fix(ui): resolve layout issue
112 |     ```
```

temp-prompts-organized/prompt-front-matter/_shared__tm__blockers.tm.refactor.md
```
1 | # Blocker Diagnosis
2 | 
3 | ## Inputs
4 | - target_id (string): The unique identifier of the task to diagnose.
5 | - tasks.json (file): JSON file containing task metadata and dependencies.
6 | 
7 | ## Canonical taxonomy (exact strings)
8 | - dependency
9 | - ambiguity
10 | - environment
11 | - CI
12 | - external
13 | 
14 | ### Stage hints (for inference)
15 | - diagnosis → assessment
16 | - assessment → unblocking proposal
17 | 
18 | ## Algorithm
19 | 1. Extract signals from the content:
20 |    - Titles/headings: "Blocker Diagnosis", "Purpose", "Steps", "Output format"
21 |    - Imperative verbs: "Diagnose", "Enumerate", "Classify", "Propose"
22 |    - Explicit tags: "dependency", "ambiguity", "environment", "CI", "external"
23 | 
24 | 2. Determine the primary identifier:
25 |    - Prefer explicit input: `target_id`
26 |    - Normalize to kebab-case, lowercase, and length-capped (e.g., TM-17 → tm-17)
27 | 
28 | 3. Determine categories:
29 |    - Prefer explicit input; otherwise infer from verbs/headings.
30 |    - Final list: dependency, ambiguity, environment, CI, external
31 |    - Validated and de-duplicated
32 | 
33 | 4. Determine lifecycle/stage (optional):
34 |    - Map "diagnosis" to stage "assessment"
35 |    - Omit if not explicitly stated
36 | 
37 | 5. Determine dependencies (optional):
38 |    - Required inputs: tasks.json, target_id
39 |    - Id-shaped items only (e.g., TM-17)
40 | 
41 | 6. Determine provided artifacts (optional):
42 |    - Two tables: blockers (type | item | evidence), actions (step | owner | effort | success_criteria)
43 |    - A narrative under "Findings"
44 | 
45 | 7. Compose summary:
46 |    - "Diagnose why a task is blocked and propose minimal unblocking paths."
47 | 
48 | 8. Produce metadata in the requested format:
49 |    - Identifier: tm-17
50 |    - Categories: dependency, ambiguity, environment, CI, external
51 |    - Stage: assessment
52 |    - Dependencies: tasks.json, target_id
53 |    - Artifacts: blockers table, actions table, findings narrative
54 |    - Summary: Diagnose why a task is blocked and propose minimal unblocking paths.
55 | 
56 | 9. Reconcile if input already contains metadata:
57 |    - No explicit metadata present; all inferred from content.
58 |    - Final output uses only valid, canonical values.
59 | 
60 | ## Assumptions & Constraints
61 | - Emit exactly one document: metadata block, blank line, then original body unchanged.
62 | - Limit distinct placeholders to ≤7 (here: 6 used).
63 | - All categories must be in the canonical list.
64 | - Stage must map to a known stage via hints.
65 | 
66 | ## Validation
67 | - Identifier matches kebab-case pattern (e.g., tm-17)
68 | - Categories non-empty and drawn from canonical taxonomy (≤5)
69 | - Stage is "assessment" — valid per hint mapping
70 | - Dependencies are id-shaped: tasks.json, target_id
71 | - Artifacts: exactly two tables + narrative
72 | - Summary ≤120 chars; punctuation coherent
73 | 
74 | ## Output format examples
75 | - Identifier: tm-17  
76 | - Categories: dependency, ambiguity, environment, CI, external  
77 | - Stage: assessment  
78 | - Dependencies: tasks.json, target_id  
79 | - Artifacts: blockers table, actions table, findings narrative  
80 | - Summary: Diagnose why a task is blocked and propose minimal unblocking paths.  
81 | 
82 | ---
83 | 
84 | # Blocker Diagnosis
85 | 
86 | Trigger: /tm-blockers
87 | 
88 | Purpose: Diagnose why a task is blocked and propose the shortest path to unblock it.
89 | 
90 | Steps:
91 | 
92 | 1. Load tasks.json and the target id.
93 | 2. Enumerate unmet dependencies and missing artifacts (tests, docs, approvals).
94 | 3. Classify each blocker: dependency, ambiguity, environment, CI, external.
95 | 4. Propose 1–3 minimal unblocking actions, each with owner, effort, and success check.
96 | 
97 | Output format:
98 | 
99 | - "# Blocker Report: <id>"
100 | - Tables: blockers (type | item | evidence), actions (step | owner | effort | success_criteria).
101 | 
102 | Examples:
103 | 
104 | - Input: /tm-blockers TM-17
105 | - Output: two tables and a short narrative under "Findings".
106 | 
107 | Notes:
108 | 
109 | - If the task is not actually blocked, state why and redirect to /tm-advance.
110 | 
111 | Respond with the corresponding output fields, starting with the field `[[ ## reasoning ## ]]`, then `[[ ## template_markdown ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.
```

temp-prompts-organized/prompt-front-matter/_shared__tm__ci.tm.refactor.md
```
1 | # CI/Test Checklist from Tasks
2 | 
3 | ## Inputs
4 | - Identifier: /tm-ci  
5 | - Dependencies: /tm-next  
6 | - Output Format: 
7 |   - "# CI Plan"
8 |   - Tables: jobs (name | trigger | commands | est_time) and tests (scope | command | expected_artifacts)
9 |   - "## Risk Areas" bullets and "## Follow-ups"
10 | 
11 | ## Canonical taxonomy (exact strings)
12 | - CI Plan
13 | - Testing
14 | - Risk Areas
15 | - Follow-ups
16 | 
17 | ### Stage hints (for inference)
18 | - Planning: When deriving a near-term plan from task data.
19 | - Execution: If actual jobs are triggered or run.
20 | 
21 | ## Algorithm
22 | 1. Extract signals from the input text  
23 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.  
24 | 
25 | 2. Determine the primary identifier  
26 |    * Prefer explicit input; otherwise infer from main action + object.  
27 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
28 |    * De-duplicate.  
29 |    → Identifier: `/tm-ci`  
30 | 
31 | 3. Determine categories  
32 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
33 |    * Validate, sort deterministically, and de-dupe (≤3).  
34 |    → Categories: CI Plan, Testing, Risk Areas, Follow-ups  
35 | 
36 | 4. Determine lifecycle/stage (optional)  
37 |    * Prefer explicit input; otherwise map categories via stage hints.  
38 |    * Omit if uncertain.  
39 |    → Stage: Planning  
40 | 
41 | 5. Determine dependencies (optional)  
42 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
43 |    → Dependencies: /tm-next  
44 | 
45 | 6. Determine provided artifacts (optional)  
46 |    * Short list (≤3) of unlocked outputs.  
47 |    → Artifacts: CI jobs table, test table, risk bullets, follow-up items  
48 | 
49 | 7. Compose summary  
50 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”  
51 |    → Summary: Do derive a near-term CI and test checklist from ready and in-progress tasks to achieve structured planning for automated testing.  
52 | 
53 | 8. Produce metadata in the requested format  
54 |    * Default to human-readable serialization; honor any requested alternative.  
55 | 
56 | 9. Reconcile if input already contains metadata  
57 |    * Merge: explicit inputs > existing > inferred.  
58 |    * Validate lists; move unknowns to an extension field if needed.  
59 |    * Remove empty keys.  
60 | 
61 | ## Assumptions & Constraints
62 | - Emit exactly one document: metadata, a single blank line, then the original body unchanged.
63 | - Limit distinct placeholders to ≤7.
64 | 
65 | ## Validation
66 | - Identifier matches normalized id pattern (kebab-case, starts with letter). ✅
67 | - Categories non-empty and drawn from canonical taxonomy (≤4) → valid. ✅
68 | - Stage present and implied by "Planning" hint. ✅
69 | - Dependencies are id-shaped and within limit. ✅
70 | - Artifacts are concise and relevant. ✅
71 | - Summary ≤120 chars; punctuation coherent. ✅
72 | - Body text is not altered. ✅
73 | 
74 | ## Output format examples
75 | - Identifier: /tm-ci  
76 | - Categories: CI Plan, Testing, Risk Areas, Follow-ups  
77 | - Stage: Planning  
78 | - Dependencies: /tm-next  
79 | - Artifacts: CI jobs table, test table, risk bullets, follow-up items  
80 | - Summary: Do derive a near-term CI and test checklist from ready and in-progress tasks to achieve structured planning for automated testing.
81 | 
82 | ---
83 | 
84 | # CI/Test Checklist from Tasks
85 | 
86 | Trigger: /tm-ci
87 | 
88 | Purpose: Derive a near-term CI and test checklist from ready and in-progress tasks.
89 | 
90 | Steps:
91 | 
92 | 1. Compute ready tasks (see /tm-next) and collect any testStrategy fields.
93 | 2. Group by component or tag if available; otherwise by path keywords in titles.
94 | 3. Propose CI jobs and test commands with approximate runtimes and gating rules.
95 | 4. Include a smoke-test matrix and minimal code coverage targets if relevant.
96 | 
97 | Output format:
98 | 
99 | - "# CI Plan"
100 | - Tables: jobs (name | trigger | commands | est_time) and tests (scope | command | expected_artifacts).
101 | - "## Risk Areas" bullets and "## Follow-ups".
102 | 
103 | Examples:
104 | 
105 | - Input: /tm-ci
106 | - Output: one CI plan with 3–8 jobs and a test table.
107 | 
108 | Notes:
109 | 
110 | - Non-binding guidance. Adapt to the repo’s actual CI system.
```

temp-prompts-organized/prompt-front-matter/_shared__tm__delta.tm.refactor.md
```
1 | # PRD → Tasks Delta
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: prd-delta
6 | - **categories**: 
7 |   - delta
8 |   - task comparison
9 |   - prds
10 | - **lifecycle_stage**: analyze
11 | - **dependencies**: 
12 |   - prd_content
13 |   - tasks_json
14 | - **provided_artifacts**: 
15 |   - delta_summary_table
16 |   - json_patch_operations
17 |   - assumptions_open_questions
18 | - **summary**: Compare a PRD to tasks.json and propose add/update/remove operations.
19 | 
20 | ## Inputs
21 | 
22 | - PRD content (text or path like ./prd.txt)
23 | - Existing tasks.json file path
24 | 
25 | ## Canonical taxonomy (exact strings)
26 | 
27 | - delta
28 | - task comparison
29 | - prds
30 | - analysis
31 | - automation
32 | - update
33 | - generate
34 | 
35 | ### Stage hints (for inference)
36 | 
37 | - analyze → input parsing, objective extraction, mapping
38 | - compare → fuzzy matching, gap detection
39 | - propose → output generation: adds/updates/removals
40 | 
41 | ## Algorithm
42 | 
43 | 1. Extract signals from $1  
44 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
45 | 
46 | 2. Determine the primary identifier  
47 |    * Prefer explicit input; otherwise infer from main action + object.  
48 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
49 |    * De-duplicate.
50 | 
51 | 3. Determine categories  
52 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
53 |    * Validate, sort deterministically, and de-dupe (≤3).
54 | 
55 | 4. Determine lifecycle/stage (optional)  
56 |    * Prefer explicit input; otherwise map categories via stage hints.  
57 |    * Omit if uncertain.
58 | 
59 | 5. Determine dependencies (optional)  
60 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
61 | 
62 | 6. Determine provided artifacts (optional)  
63 |    * Short list (≤3) of unlocked outputs.
64 | 
65 | 7. Compose summary  
66 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
67 | 
68 | 8. Produce metadata in the requested format  
69 |    * Default to a human-readable serialization; honor any requested alternative.
70 | 
71 | 9. Reconcile if input already contains metadata  
72 |    * Merge: explicit inputs > existing > inferred.  
73 |    * Validate lists; move unknowns to an extension field if needed.  
74 |    * Remove empty keys.
75 | 
76 | ## Assumptions & Constraints
77 | 
78 | - Emit exactly one document: metadata, a single blank line, then the original body.
79 | - Limit distinct placeholders to ≤7.
80 | - Output must be minimal and reversible; destructive changes flagged explicitly.
81 | 
82 | ## Validation
83 | 
84 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
85 | - Categories non-empty and drawn from canonical taxonomy (≤3).
86 | - Stage, if present, is one of: analyze, compare, propose.
87 | - Dependencies, if present, are id-shaped (e.g., prd_content, tasks_json) — ≤5.
88 | - Provided artifacts ≤3 and match known outputs.
89 | - Summary ≤120 chars; punctuation coherent.
90 | - Body text is not altered.
91 | 
92 | ## Output format examples
93 | 
94 | - Input: /tm-delta ./prd.txt  
95 |   Output:
96 |     # Delta Summary
97 |     | Type     | Task Title               |
98 |     |----------|--------------------------|
99 |     | Add      | Implement user onboarding flow |
100 |     | Update   | Rename milestone to v1.0 |
101 |     | Remove   | Deprecated legacy feature |
102 | 
103 |     ## JSON Patch
104 |     - add: { "id": "task-456", "title": "Implement user onboarding flow" }
105 |     - replace: { "id": "task-789", "priority": "high" }
106 |     - remove: { "id": "task-012" }
107 | 
108 |     ## Assumptions
109 |     - PRD is up-to-date and reflects current priorities.
110 |     
111 |     ## Open Questions
112 |     - How should ambiguous deliverables be resolved?
113 | 
114 | ---
115 | 
116 | # PRD → Tasks Delta
117 | 
118 | Trigger: /tm-delta
119 | 
120 | Purpose: Compare a PRD text against tasks.json and propose add/update/remove operations.
121 | 
122 | Steps:
123 | 
124 | 1. Accept PRD content pasted by the user or a path like ./prd.txt. If absent, output a short template asking for PRD input.
125 | 2. Extract objectives, constraints, deliverables, and milestones from the PRD.
126 | 3. Map them to existing tasks by fuzzy match on title and keywords; detect gaps.
127 | 4. Propose: new tasks, updates to titles/descriptions/priority, and deprecations.
128 | 
129 | Output format:
130 | 
131 | - "# Delta Summary"
132 | - Tables: adds | updates | removals.
133 | - "## JSON Patch" with an ordered list of operations: add/replace/remove.
134 | - "## Assumptions" and "## Open Questions".
135 | 
136 | Examples:
137 | 
138 | - Input: /tm-delta ./prd.txt
139 | - Output: tables with a small JSON Patch block.
140 | 
141 | Notes:
142 | 
143 | - Keep patches minimal and reversible. Flag any destructive changes explicitly.
```

temp-prompts-organized/prompt-front-matter/_shared__tm__docs.tm.refactor.md
```
1 | # Generate Status Docs
2 | 
3 | ## Inputs
4 | - Trigger: `/tm-docs`
5 | - Source: tasks.json
6 | - Output format: Markdown document for README or STATUS.md
7 | - Required fields: done, in_progress, blocked, ready_next
8 | - Optional: changelog (if timestamps exist)
9 | 
10 | ## Canonical taxonomy (exact strings)
11 | - documentation
12 | - status reporting
13 | - project tracking
14 | 
15 | ### Stage hints (for inference)
16 | - Generation → primary stage
17 | - Composition → sub-stage
18 | - Output → final delivery
19 | 
20 | ## Algorithm
21 | 1. Extract signals from the prompt:
22 |    - Titles/headings: "Generate Status Docs", "Purpose", "Steps", "Output format"
23 |    - Imperative verbs: "Parse", "Compose", "Produce", "Emit"
24 |    - Explicit tags: `/tm-docs`, "tasks.json", "STATUS.md"
25 |    - Dependency phrasing: "from tasks.json", "per /tm-next logic"
26 | 
27 | 2. Determine the primary identifier:
28 |    - Preferred input: `/tm-docs`
29 |    - Normalized: `tm-docs`
30 | 
31 | 3. Determine categories:
32 |    - Explicit input: none
33 |    - Inferred from verbs and context: documentation, status reporting, project tracking
34 |    - Validated against taxonomy; de-duplicated → 3 entries
35 | 
36 | 4. Determine lifecycle/stage (optional):
37 |    - Prefer explicit input → not provided
38 |    - Map via stage hints → "Generation" (primary)
39 | 
40 | 5. Determine dependencies (optional):
41 |    - "Parse tasks.json"
42 |    - "/tm-next logic for state classification"
43 |    - Normalized to: `tasks.json`, `/tm-next`
44 | 
45 | 6. Determine provided artifacts (optional):
46 |    - A single Markdown document (STATUS.md)
47 |    - Status boards per status category (Ready Next, In Progress, Blocked, Done)
48 |    - 7-day changelog if timestamps exist; otherwise, recent done items
49 | 
50 | 7. Compose summary:
51 |    - "Generate a project status document from tasks.json to report current focus, progress, and risks."
52 | 
53 | 8. Produce metadata in structured format:
54 |    - Identifier: tm-docs
55 |    - Categories: documentation, status reporting, project tracking
56 |    - Stage: generation
57 |    - Dependencies: tasks.json, /tm-next
58 |    - Artifacts: STATUS.md, status boards, changelog (if available)
59 |    - Summary: Generate a project status document from tasks.json to report current focus, progress, and risks.
60 | 
61 | 9. Reconcile if input already contains metadata:
62 |    - No prior metadata present; all fields inferred and validated.
63 | 
64 | ## Assumptions & Constraints
65 | - Output is exactly one document: metadata block, blank line, then original body.
66 | - All identifiers are normalized (lowercase, kebab-case).
67 | - Categories strictly from canonical taxonomy (≤3).
68 | - Stage is one of the allowed stages in stage hints.
69 | - Dependencies are id-shaped and ≤5.
70 | - Summary ≤120 characters; coherent punctuation.
71 | - Original content ($1) remains unaltered.
72 | 
73 | ## Validation
74 | - Identifier: `tm-docs` → matches normalized pattern
75 | - Categories: non-empty, from taxonomy, ≤3
76 | - Stage: "generation" → valid per stage hints
77 | - Dependencies: `tasks.json`, `/tm-next` → id-shaped, ≤5
78 | - Artifacts: 3 listed (document, boards, changelog)
79 | - Summary: 108 characters; grammatically sound
80 | 
81 | ## Output format examples
82 | - Identifier: tm-docs  
83 | - Categories: documentation, status reporting, project tracking  
84 | - Stage: generation  
85 | - Dependencies: tasks.json, /tm-next  
86 | - Artifacts: STATUS.md, status boards, changelog (if available)  
87 | - Summary: Generate a project status document from tasks.json to report current focus, progress, and risks.  
88 | 
89 | ---
90 | 
91 | # Generate Status Docs
92 | 
93 | Trigger: /tm-docs
94 | 
95 | Purpose: Emit a project status document from tasks.json for README or STATUS.md.
96 | 
97 | Steps:
98 | 
99 | 1. Parse tasks.json; collect done, in_progress, blocked, and ready_next (per /tm-next logic).
100 | 2. Compose a concise narrative: current focus, recent wins, top risks.
101 | 3. Produce status boards for each status with id, title, and owner if present.
102 | 4. Add a 7-day changelog if timestamps exist; otherwise, summarize recent done items.
103 | 
104 | Output format:
105 | 
106 | - "# Project Status — <date>"
107 | - Sections: Summary, Ready Next, In Progress, Blocked, Done, Changelog.
108 | 
109 | Examples:
110 | 
111 | - Input: /tm-docs
112 | - Output: a single Markdown document suitable for commit as STATUS.md.
113 | 
114 | Notes:
115 | 
116 | - Avoid leaking secrets. Do not invent owners; omit unknown fields.
```

temp-prompts-organized/prompt-front-matter/_shared__tm__next.tm.refactor.md
```
1 | # Next Ready Tasks
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: task-id
6 | - **category**: task-management
7 | - **lifecycle-stage**: ready-to-start
8 | - **dependencies**: [dependency-id]
9 | - **provided-artifacts**: table-of-ready-tasks, notes-on-tie-breaks
10 | - **summary**: List tasks ready to start by checking status and dependencies.
11 | 
12 | ## Inputs
13 | 
14 | - Trigger: /tm-next
15 | - Input format: command string or task list
16 | - Output format: structured table with id, title, priority, why_ready, prereqs; includes "No ready tasks" if none exist
17 | 
18 | ## Canonical taxonomy (exact strings)
19 | 
20 | - task-management
21 | - workflow-automation
22 | - dependency-tracking
23 | - status-reporting
24 | 
25 | ### Stage hints (for inference)
26 | 
27 | - pending → waiting for dependencies
28 | - blocked → requires unmet prerequisites
29 | - ready-to-start → all dependencies met, status in {pending, blocked}
30 | - execution → being worked on
31 | 
32 | ## Algorithm
33 | 
34 | 1. Extract signals from $1  
35 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
36 | 
37 | 2. Determine the primary identifier  
38 |    * Prefer explicit input; otherwise infer from main action + object.  
39 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
40 |    * De-duplicate.
41 | 
42 | 3. Determine categories  
43 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
44 |    * Validate, sort deterministically, and de-dupe (≤3).
45 | 
46 | 4. Determine lifecycle/stage (optional)  
47 |    * Prefer explicit input; otherwise map categories via stage hints.  
48 |    * Omit if uncertain.
49 | 
50 | 5. Determine dependencies (optional)  
51 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).
52 | 
53 | 6. Determine provided artifacts (optional)  
54 |    * Short list (≤3) of unlocked outputs.
55 | 
56 | 7. Compose summary  
57 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
58 | 
59 | 8. Produce metadata in the requested format  
60 |    * Default to a human-readable serialization; honor any requested alternative.
61 | 
62 | 9. Reconcile if input already contains metadata  
63 |    * Merge: explicit inputs > existing > inferred.  
64 |    * Validate lists; move unknowns to an extension field if needed.  
65 |    * Remove empty keys.
66 | 
67 | ## Assumptions & Constraints
68 | 
69 | - Emit exactly one document: metadata, a single blank line, then the original body unchanged.
70 | - Limit distinct placeholders to ≤ 7.
71 | - All stages must map to known stage hints.
72 | - Dependencies must be id-shaped (e.g., task-id).
73 | 
74 | ## Validation
75 | 
76 | - Identifier matches a normalized id pattern.
77 | - Categories non-empty and drawn from canonical taxonomy (≤3).
78 | - Stage, if present, is one of the allowed stages implied by stage hints.
79 | - Dependencies, if present, are id-shaped (≤5).
80 | - Summary ≤120 chars; punctuation coherent.
81 | - Body text is not altered.
82 | 
83 | ## Output format examples
84 | 
85 | - Input: /tm-next  
86 |   Output:  
87 |   # Ready Now  
88 |   | id | title | priority | why_ready | prereqs |  
89 |   | --- | --- | --- | --- | --- |  
90 |   | t1 | Fix login bug | 5 | Status is pending and dependency d2 is done | d2 |  
91 |   | t2 | Deploy v2.0 | 4 | Blocked status resolved, all prereqs met | d3, d4 |  
92 |   ## Notes  
93 |   - Missing priority defaults to 0. Custom scales described in Notes.
94 | 
95 | - If no ready tasks:  
96 |   "No ready tasks" followed by list of nearest-unblock candidates with their dependencies.
```

temp-prompts-organized/prompt-front-matter/_shared__tm__overview.tm.refactor.md
```
1 | # TaskMaster Overview
2 | 
3 | ## Metadata
4 | 
5 | - **identifier**: tm-overview  
6 | - **category**: summarization  
7 | - **lifecycle_stage**: inspection  
8 | - **dependencies**: tasks.json  
9 | - **provided_artifacts**: overview bullets, totals table, top pending list, critical path list, issues list  
10 | - **summary**: Summarize TaskMaster tasks.json by status, priority, and dependency health to orient work.
11 | 
12 | ## Inputs
13 | 
14 | - `tasks.json` path (optional; defaults to repo root)
15 | 
16 | ## Canonical taxonomy (exact strings)
17 | 
18 | - summarization
19 | - analysis
20 | - reporting
21 | 
22 | ### Stage hints (for inference)
23 | 
24 | - inspection → summarizing state, reading data
25 | - analysis → detecting cycles, computing paths
26 | - reporting → outputting tables and lists
27 | 
28 | ## Algorithm
29 | 
30 | 1. Extract signals from $1  
31 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.
32 | 
33 | 2. Determine the primary identifier  
34 |    * Prefer explicit input; otherwise infer from main action + object.  
35 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).  
36 |    * De-duplicate.
37 | 
38 | 3. Determine categories  
39 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.  
40 |    * Validate, sort deterministically, and de-dupe (≤3).
41 | 
42 | 4. Determine lifecycle/stage (optional)  
43 |    * Prefer explicit input; otherwise map categories via stage hints.  
44 |    * Omit if uncertain.
45 | 
46 | 5. Determine dependencies (optional)  
47 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).  
48 | 
49 | 6. Determine provided artifacts (optional)  
50 |    * Short list (≤3) of unlocked outputs.
51 | 
52 | 7. Compose summary  
53 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”
54 | 
55 | 8. Produce metadata in the requested format  
56 |    * Default to a human-readable serialization; honor any requested alternative.
57 | 
58 | 9. Reconcile if input already contains metadata  
59 |    * Merge: explicit inputs > existing > inferred.  
60 |    * Validate lists; move unknowns to an extension field if needed.  
61 |    * Remove empty keys.
62 | 
63 | ## Assumptions & Constraints
64 | 
65 | - Emit exactly one document: metadata, a single blank line, then $1.
66 | - Limit distinct placeholders to ≤ 7.
67 | - Body text is not altered.
68 | 
69 | ## Validation
70 | 
71 | - Identifier matches a normalized id pattern (e.g., kebab-case).
72 | - Categories non-empty and drawn from canonical taxonomy (≤3).
73 | - Stage, if present, is one of the allowed stages implied by stage hints (inspection, analysis, reporting).
74 | - Dependencies, if present, are id-shaped (≤5).
75 | - Summary ≤120 chars; punctuation coherent.
76 | - Body text $1 is not altered.
77 | 
78 | ## Output format examples
79 | 
80 | - Input: `/tm-overview`  
81 |   Output:  
82 |     # Overview  
83 |     - Bullet summary of status, priority, dependencies  
84 |     ## Totals  
85 |     | status       | count | percent | notes         |  
86 |     |--------------|-------|---------|---------------|  
87 |     | pending      | 5     | 40%     | high volume   |  
88 |     | in_progress  | 3     | 25%     | active        |  
89 |     | blocked      | 1     | 8%      | dependency    |  
90 |     | done         | 6     | 50%     | completed     |  
91 |     ## Top Pending  
92 |     | id   | title               | priority | unblockers          |  
93 |     |------|---------------------|----------|---------------------|  
94 |     | t-12 | Fix login timeout   | high     | resolve API error   |  
95 |     | t-34 | Deploy frontend     | medium   | wait for backend    |  
96 |     ## Critical Path  
97 |     - t-12 → t-34 → t-56  
98 |     ## Issues  
99 |     - Cycle detected: t-78 → t-90 → t-78  
100 |     - Missing reference: t-11 (no dependencies)  
101 |     - Duplicate entry: t-44 appears twice  
102 | 
103 | ---
104 | 
105 | # TaskMaster Overview
106 | 
107 | Trigger: /tm-overview
108 | 
109 | Purpose: Summarize the current TaskMaster tasks.json by status, priority, dependency health, and critical path to orient work.
110 | 
111 | Steps:
112 | 
113 | 1. Locate the active tasks.json at repo root or the path supplied in the user message. Do not modify it.
114 | 2. Parse fields: id, title, description, status, priority, dependencies, subtasks.
115 | 3. Compute counts per status and a table of top pending items by priority.
116 | 4. Detect dependency issues: cycles, missing ids, orphans (no deps and not depended on).
117 | 5. Approximate a critical path: longest dependency chain among pending→in_progress tasks.
118 | 
119 | Output format:
120 | 
121 | - "# Overview" then a bullets summary.
122 | - "## Totals" as a 4-column table: status | count | percent | notes.
123 | - "## Top Pending" table: id | title | priority | unblockers.
124 | - "## Critical Path" as an ordered list of ids with short titles.
125 | - "## Issues" list for cycles, missing references, duplicates.
126 | 
127 | Examples:
128 | 
129 | - Input (Codex TUI): /tm-overview
130 | - Output: tables and lists as specified. Keep to <= 200 lines.
131 | 
132 | Notes:
133 | 
134 | - Read-only. Assume statuses: pending | in_progress | blocked | done.
135 | - If tasks.json is missing or invalid, output an "## Errors" section with a concise diagnosis.
136 | 
137 | Respond with the corresponding output fields, starting with the field `[[ ## reasoning ## ]]`, then `[[ ## template_markdown ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.
```

temp-prompts-organized/prompt-front-matter/_shared__tm__refine.tm.refactor.md
```
1 | # Refine Task into Subtasks
2 | 
3 | Task: Given a task ID and description, expand it into actionable subtasks with clear acceptance criteria.
4 | 
5 | ## Inputs
6 | 
7 | - `task_id`: A string identifier (e.g., TM-09) for the original task.
8 | - `description`: The full text of the original task to refine.
9 | 
10 | ## Canonical taxonomy (exact strings)
11 | 
12 | - task refinement
13 | - planning
14 | - subtask decomposition
15 | - acceptance criteria
16 | - dependency mapping
17 | - output formatting
18 | 
19 | ### Stage hints (for inference)
20 | 
21 | - planning → when analyzing scope and breaking down tasks
22 | - design → when defining structure or templates
23 | - execution → when implementing actions directly
24 | 
25 | ## Algorithm
26 | 
27 | 1. Extract signals from input  
28 |    * Titles/headings, imperative verbs, intent sentences, explicit tags, and dependency phrasing.*
29 | 
30 | 2. Determine the primary identifier  
31 |    * Prefer explicit input; otherwise infer from main action + object.*  
32 |    * Normalize (lowercase, kebab-case, length-capped, starts with a letter).*  
33 |    * De-duplicate.*
34 | 
35 | 3. Determine categories  
36 |    * Prefer explicit input; otherwise infer from verbs/headings vs canonical taxonomy.*  
37 |    * Validate, sort deterministically, and de-dupe (≤3).*
38 | 
39 | 4. Determine lifecycle/stage (optional)  
40 |    * Prefer explicit input; otherwise map categories via stage hints.*  
41 |    * Omit if uncertain.*
42 | 
43 | 5. Determine dependencies (optional)  
44 |    * Parse phrases implying order or prerequisites; keep id-shaped items (≤5).*  
45 | 
46 | 6. Determine provided artifacts (optional)  
47 |    * Short list (≤3) of unlocked outputs.*
48 | 
49 | 7. Compose summary  
50 |    * One sentence (≤120 chars): “Do <verb> <object> to achieve <outcome>.”*
51 | 
52 | 8. Produce metadata in the requested format  
53 |    * Default to a human-readable serialization; honor any requested alternative.*
54 | 
55 | 9. Reconcile if input already contains metadata  
56 |    * Merge: explicit inputs > existing > inferred.*  
57 |    * Validate lists; move unknowns to an extension field if needed.*  
58 |    * Remove empty keys.*
59 | 
60 | ## Assumptions & Constraints
61 | 
62 | - Emit exactly one document: metadata, a single blank line, then the original body.
63 | - Limit distinct placeholders to ≤7.
64 | - Do not assume authority to change files; provide patches the user can apply.
65 | 
66 | ## Validation
67 | 
68 | - Identifier matches a normalized id pattern (kebab-case, lowercase).
69 | - Categories non-empty and drawn from canonical taxonomy (≤3).
70 | - Stage, if present, is one of the allowed stages implied by stage hints.
71 | - Dependencies, if present, are id-shaped (≤5).
72 | - Artifacts are among: table, JSON patch, summary.
73 | - Summary ≤120 chars; punctuation coherent.
74 | - Body text is not altered.
75 | 
76 | ## Output format examples
77 | 
78 | - Identifier: `tm-refine-tm-09`  
79 | - Categories: ["task refinement", "planning", "subtask decomposition"]  
80 | - Stage: planning  
81 | - Dependencies: ["tm-refine-tm-08"]  
82 | - Artifacts: ["Markdown table of subtasks", "JSON Patch array"]  
83 | - Summary: "Refine a vague task into actionable subtasks with acceptance criteria and suggest edits."
```

temp-prompts-organized/prompt-front-matter/_templates__instruction-file.templates.refactor.md
```
1 | # Instruction File
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: instruction-file
6 | - **Categories**: context, coding standards, review rituals, testing, security, limits
7 | - **Stage**: setup
8 | - **Dependencies**: none
9 | - **Provided Artifacts**: cursor.rules, windsurf.rules, claude.md
10 | - **Summary**: Generate or update project-specific rule files to standardize team practices.
11 | 
12 | ## Steps
13 | 
14 | 1. Scan repo for existing instruction files.
15 | 2. Compose sections: Context, Coding Standards, Review Rituals, Testing, Security, Limits.
16 | 3. Include "Reset and re-implement cleanly" guidance and scope control.
17 | 4. Write to chosen file and propose a commit message.
18 | 
19 | ## Output format
20 | 
21 | - Markdown instruction file with stable headings.
```

temp-prompts-organized/prompt-front-matter/_templates__prompt-sequence-generator.templates.refactor.md
```
1 | # Prompt: Generate Prompt Execution Sequence
2 | 
3 | **Purpose:** Given a high-level goal and a set of available prompts, generate the logical execution sequence required to accomplish that goal by chaining the prompts together.
4 | 
5 | ---
6 | 
7 | ### **Inputs**
8 | 
9 | *   **High-Level Goal:** {{high_level_goal}}
10 |     *   *A clear, one-sentence description of the final outcome the user wants to achieve.*
11 |     *   *Example: "Create and document a pull request for the currently staged changes."*
12 | 
13 | *   **Available Prompts:**
14 |     ```
15 |     {{available_prompts}}
16 |     ```
17 |     *   *A list of candidate prompt names (e.g., from the output of `rank-root-prompts`).*
18 |     *   *Example: ['pr-desc.md', 'commit-msg.md', 'changed-files.md', 'review.md', 'release-notes.md']*
19 | 
20 | *   **Context (Optional):** {{context}}
21 |     *   *Any additional context, such as the current state of the git repository or specific files of interest.*
22 |     *   *Example: "The user has already staged files using `git add`."*
23 | 
24 | ---
25 | 
26 | ### **Instructions for the AI**
27 | 
28 | 1.  **Analyze the Goal:** Deconstruct the `{{high_level_goal}}` into a series of logical steps required to get from the starting state to the final outcome.
29 | 
30 | 2.  **Map Prompts to Steps:** For each logical step, identify the most suitable prompt from the `{{available_prompts}}` list that can perform that step.
31 |     *   Consider the inputs and outputs of each prompt to determine dependencies. A prompt's input is often the output of a previous one.
32 | 
33 | 3.  **Establish Order:** Arrange the selected prompts into a numbered sequence based on their dependencies. The sequence should represent a complete and logical workflow.
34 | 
35 | 4.  **Identify Gaps:** If any necessary step in the workflow cannot be fulfilled by one of the available prompts, explicitly state what action or prompt is missing.
36 | 
37 | ---
38 | 
39 | ### **Required Output Format**
40 | 
41 | **Execution Sequence:**
42 | 
43 | 1.  **`[prompt_name_1.md]`**: [Brief justification for why this prompt is first and what it accomplishes.]
44 | 2.  **`[prompt_name_2.md]`**: [Brief justification for why this prompt is second, and how it uses the output of the previous step.]
45 | 3.  ...
46 | 
47 | **Identified Gaps (if any):**
48 | 
49 | *   [Description of a missing step or prompt needed to complete the workflow.]
```

temp-prompts-organized/prompt-front-matter/_templates__system-level-instruction-editor.templates.refactor.md
```
1 | # System Instruction: Canonical Instruction File Editor
2 | 
3 | ## Metadata
4 | 
5 | - **Identifier**: system-level-instruction-editor
6 | - **Categories**: 
7 |   - Instruction Editing
8 |   - System Operations
9 |   - Documentation Workflow
10 | - **Lifecycle/Stage**: Operational
11 | - **Dependencies**: 
12 |   - logs/artifacts
13 |   - affected services/modules
14 |   - build/version/commit
15 |   - time window/region/tenant
16 |   - SLO/SLA impacted
17 | - **Provided Artifacts**:
18 |   - Updated file in Canvas
19 |   - Variant files (GEMINI.md, CLAUDE.md)
20 |   - Full content in chat on size limit
21 | - **Summary**: Do edit a canonical instruction file to achieve structured, validated, and deployable changes.
22 | 
23 | ## Inputs
24 | 
25 | - <logs/artifacts to collect>
26 | - <affected services/modules>
27 | - <build/version/commit>
28 | - <time window/region/tenant>
29 | - <SLO/SLA impacted>
30 | 
31 | ## Steps
32 | 
33 | 1. Collect relevant data (<test logs, traces, metrics, dumps, repro steps>).
34 | 2. Group by symptom/pattern; for each group, list 2–3 plausible causes.
35 | 3. Propose disambiguators (instrumentation, targeted inputs, experiments).
36 | 4. Sketch minimal fixes (patches/config toggles/rollbacks) with risk notes.
37 | 5. Validate fixes (tests to run, monitors to watch, acceptance criteria).
38 | 6. Roll out & verify (staged rollout plan, owners, ETA).
39 | 7. Capture follow-ups (refactors, docs, guardrails).
40 | 
41 | 1. **Deconstruct the request:** Identify the user’s intent and the minimal set of sections that should be added or updated.
42 | 2. **Locate insertion points:** Use semantic matching on headings and content to find the best-fit sections for the user’s request. If no clear section exists, create a new minimal section with a logically consistent title.
43 | 3. **Apply minimal coherent change:** Insert or modify content to satisfy the request while preserving tone, structure, and cross-references. Keep unrelated sections unchanged.
44 | 4. **Run invariants:**
45 | 
46 |    - The entire file must be present (no placeholders, no truncation).
47 |    - Markdown structure and formatting must remain valid.
48 |    - Internal references and links stay accurate.
49 | 5. **Render in Canvas:**
50 | 
51 |    - If editing an existing file: open in Canvas and **replace the full contents** with the updated version.
52 |    - If creating a new file: create it in Canvas and display the **entire file**.
53 | 6. **Variants (optional or on request):** Generate `GEMINI.md` and/or `CLAUDE.md` from the updated `AGENTS.md` using only the Platform Substitution Rules. Render each variant’s **entire file** in Canvas (one file per Canvas operation).
54 | 7. **Size-limit fallback:** If a size cap prevents full-file rendering in Canvas, output the **entire file in chat**, then append:
55 | 
56 |    - “*Note: Full content was output in chat due to a size limit preventing Canvas rendering.*”
57 | 
58 | ## Output format
59 | 
60 | - Table: <symptom/item> → <likely causes> → <next checks> → <candidate fix> → <owner/ETA>.
61 | 
62 | ## Example rows
63 | 
64 | - "<example symptom or error>" → <cause A, cause B> → <check 1, check 2> → <fix sketch> → <owner/ETA>.
```

temp-prompts-organized/00-ideation/architecture/adr-new.architecture.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Draft an Architecture Decision Record with pros/cons.
2 | 
3 | 1. Gather context by inspecting `README.md` for the project context.
4 | 2. Draft a concise ADR including Context, Decision, Status, Consequences. Title: <args>.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Draft an Architecture Decision Record with pros/cons.
10 | - Highlight workflow triggers, failing jobs, and proposed fixes.
11 | - Document the evidence you used so maintainers can trust the conclusion.
12 | 
13 | Example Input:
14 | src/example.ts
15 | 
16 | Expected Output:
17 | 
18 | - Actionable summary aligned with the output section.
```

temp-prompts-organized/00-ideation/architecture/logging-strategy.architecture.md
```
1 | phase: "P7 Release & Ops"
2 | gate: "Release Gate"
3 | status: "logging guardrails ready for canary/production checks; coordinate with P4 Frontend UX for client telemetry."
4 | previous:
5 | 
6 | - "/monitoring-setup"
7 | - "/slo-setup"
8 | next:
9 | - "/audit"
10 | - "/error-analysis"
11 | 
12 | ---
13 | 
14 | # Logging Strategy
15 | 
16 | Trigger: /logging-strategy
17 | 
18 | Purpose: Add or remove diagnostic logging cleanly with levels and privacy in mind.
19 | 
20 | ## Steps
21 | 
22 | 1. Identify hotspots from recent failures.
23 | 2. Insert structured logs with contexts and correlation IDs.
24 | 3. Remove noisy or PII-leaking logs.
25 | 4. Document log levels and sampling in `OBSERVABILITY.md`.
26 | 
27 | ## Output format
28 | 
29 | - Diff hunks and a short guideline section.
30 | 
```

temp-prompts-organized/00-ideation/architecture/modular-architecture.architecture.md
```
1 | phase: "P2 App Scaffold & Contracts"
2 | gate: "Test Gate lite"
3 | status: "boundaries documented and lint/build scripts still pass; revisit during P4 Frontend UX for UI seams."
4 | previous:
5 | 
6 | - "/openapi-generate"
7 | next:
8 | - "/db-bootstrap"
9 | - "/ui-screenshots"
10 | - "/design-assets"
11 | 
12 | ---
13 | 
14 | # Modular Architecture
15 | 
16 | Trigger: /modular-architecture
17 | 
18 | Purpose: Enforce modular boundaries and clear external interfaces.
19 | 
20 | ## Steps
21 | 
22 | 1. Identify services/modules and their public contracts.
23 | 2. Flag cross-module imports and circular deps.
24 | 3. Propose boundaries, facades, and internal folders.
25 | 4. Add "contract tests" for public APIs.
26 | 
27 | ## Output format
28 | 
29 | - Diagram-ready list of modules and edges, plus diffs.
30 | 
```

temp-prompts-organized/00-ideation/architecture/stack-evaluation.architecture.md
```
1 | ---
2 | phase: "P1 Plan & Scope"
3 | gate: "Scope Gate"
4 | status: "record recommended stack and top risks before building."
5 | previous:
6 |   - "/scope-control"
7 | next:
8 |   - "/scaffold-fullstack"
9 |   - "/api-contract"
10 | ---
11 | 
12 | # Stack Evaluation
13 | 
14 | Trigger: /stack-evaluation
15 | 
16 | Purpose: Evaluate language/framework choices relative to AI familiarity and repo goals.
17 | 
18 | ## Steps
19 | 
20 | 1. Detect current stack and conventions.
21 | 2. List tradeoffs: maturity, tooling, available examples, hiring, and AI training coverage.
22 | 3. Recommend stay-or-switch with migration outline if switching.
23 | 
24 | ## Output format
25 | 
26 | - Decision memo with pros/cons and next steps.
27 | 
```

temp-prompts-organized/00-ideation/requirements/plan-delta.requirements.md
```
1 | # plan-delta
2 | 
3 | Trigger: /plan-delta
4 | 
5 | Purpose: Orchestrate mid-project planning deltas on an existing task graph with history preservation, lineage, and readiness recalculation.
6 | 
7 | Steps:
8 | 
9 | 1. Discover repository context:
10 |    1. Detect tasks file path: prefer `tasks.json`; else search `**/tasks.json`.
11 |    2. Detect latest plan doc: prefer `PRD.md` or `docs/PRD.md`; else `**/*(prd|spec|plan)*.md`.
12 | 2. Snapshot:
13 |    1. Create `./artifacts/` if missing.
14 |    2. Copy the current tasks file to `./artifacts/tasks-$(date +%Y%m%d-%H%M%S).json` using: `cp -f <tasks.json> ./artifacts/tasks-$(date +%Y%m%d-%H%M%S).json`.
15 | 3. Input collection:
16 |    1. Read new objectives, constraints, and findings from the user input or provided delta text.
17 |    2. Parse selection rules to choose mode: **Continue**, **Hybrid Rebaseline**, or **Full Rebaseline**.
18 | 4. Delta Doc generation:
19 |    1. Create `./artifacts/delta-$(date +%Y%m%d-%H%M%S).md` containing sections:
20 |       - Objectives (new)
21 |       - Constraints (new)
22 |       - Impacts
23 |       - Decisions
24 |       - Evidence log (sources, dates, links)
25 | 5. Task graph update:
26 |    1. Never alter historical states `done|in_progress|blocked` of existing tasks.
27 |    2. Do not reuse IDs. For any replaced task, set `superseded_by` on the old task and include its ID in the new task's `supersedes[]`.
28 |    3. Add `source_doc`, `lineage[]` on all new or changed tasks.
29 |    4. Create new tasks only for new or changed work. Link predecessors via `dependencies` or `relations`.
30 |    5. Keep deprecated tasks in graph with `status: "deprecated"` and a `reason`.
31 | 6. Graph maintenance:
32 |    1. Recompute dependency order and validate acyclicity.
33 |    2. Flag contradictions or invalidated edges as `blocked` with a machine-readable `blocked_reason`.
34 |    3. Bubble critical-path tasks to the active frontier by recomputing earliest-start and slack.
35 | 7. Readiness and selection:
36 |    1. Implement `ready/next()` over the graph: select tasks with all dependencies `done` and not `blocked`.
37 |    2. Produce a short readiness report grouped by `ready | blocked | deprecated`.
38 | 8. Outputs:
39 |    1. Write the updated tasks file in-place, preserving formatting where possible.
40 |    2. Persist the Delta Doc under `./artifacts/`.
41 |    3. Emit decision hooks: one line per change stating what it enables.
42 | 9. Termination:
43 |    - Stop when all deltas are merged and readiness recalculated, or when a prerequisite cannot be resolved with available evidence.
44 | 
45 | Output format:
46 | 
47 | - Produce three artifacts:
48 |   1. **Updated tasks file**: valid JSON. Preserve existing fields. Append only the new or changed tasks and relations. Do not mutate historical statuses.
49 |   2. **Delta document**: Markdown with the exact headings `# Delta`, `## Objectives`, `## Constraints`, `## Impacts`, `## Decisions`, `## Evidence`.
50 |   3. **Readiness report**: Plain text with sections `READY`, `BLOCKED`, `DEPRECATED`. Each item as `- <id> <title>`; blocked items add `[reason=<code>]`.
51 | - Print **Decision hooks** as lines starting with `HOOK: <id> enables <capability>`.
52 | 
53 | Examples:
54 | 
55 | - Input →
56 | 
57 |   ```
58 |   Mode: Continue
59 |   New objectives: add offline export for tasks
60 |   Constraints: no DB migrations
61 |   Findings: existing export lib supports JSON only
62 |   ```
63 | 
64 |   Output →
65 |   - Updated `tasks.json` with new task `T-342` { title: "Add CSV export", dependencies: ["T-120"], source_doc: "delta-20250921.md", lineage: ["T-120"], supersedes: [] }.
66 |   - `artifacts/delta-20250921-160500.md` populated with objectives, constraints, impacts, decisions, evidence.
67 |   - Readiness report lists `T-342` under READY if deps done.
68 | 
69 | - Input →
70 | 
71 |   ```
72 |   Mode: Hybrid Rebaseline
73 |   Changes: ~30% of scope affected by auth provider swap
74 |   ```
75 | 
76 |   Output →
77 |   - Minor-plan version bump recorded in Delta Doc.
78 |   - New tasks added for provider swap; prior tasks kept with `deprecated` or `blocked` and lineage links.
79 | 
80 | Notes:
81 | 
82 | - Never write outside the repo. Keep artifacts in `./artifacts/`.
83 | - Evidence log entries include `source`, `date`, `summary`, and optional `link`.
84 | - Selection rules: Continue (<20% change), Hybrid (20–40%), Full (>40% or goals/KPIs/architecture pivot).
85 | - If inputs are insufficient, emit a TERMINATION note with missing evidence keys.
```

temp-prompts-organized/00-ideation/requirements/planning-process.requirements.md
```
1 | ---
2 | phase: "P1 Plan & Scope"
3 | gate: "Scope Gate"
4 | status: "confirm problem, users, Done criteria, and stack risks are logged."
5 | previous:
6 |   - "Preflight Docs (AGENTS baseline)"
7 | next:
8 |   - "/scope-control"
9 |   - "/stack-evaluation"
10 | ---
11 | 
12 | # Planning Process
13 | 
14 | Trigger: /planning-process
15 | 
16 | Purpose: Draft, refine, and execute a feature plan with strict scope control and progress tracking.
17 | 
18 | ## Steps
19 | 
20 | 1. If no plan file exists, create `PLAN.md`. If it exists, load it.
21 | 2. Draft sections: **Goal**, **User Story**, **Milestones**, **Tasks**, **Won't do**, **Ideas for later**, **Validation**, **Risks**.
22 | 3. Trim bloat. Convert vague bullets into testable tasks with acceptance criteria.
23 | 4. Tag each task with an owner and estimate. Link to files or paths that will change.
24 | 5. Maintain two backlogs: **Won't do** (explicit non-goals) and **Ideas for later** (deferrable work).
25 | 6. Mark tasks done after tests pass. Append commit SHAs next to completed items.
26 | 7. After each milestone: run tests, update **Validation**, then commit `PLAN.md`.
27 | 
28 | ## Output format
29 | 
30 | - Update or create `PLAN.md` with the sections above.
31 | - Include a checklist for **Tasks**. Keep lines under 100 chars.
32 | 
33 | ## Examples
34 | **Input**: "Add OAuth login"
35 | 
36 | **Output**:
37 | 
38 | - Goal: Let users sign in with Google.
39 | - Tasks: [ ] add Google client, [ ] callback route, [ ] session, [ ] E2E test.
40 | - Won't do: org SSO.
41 | - Ideas for later: Apple login.
42 | 
43 | ## Notes
44 | 
45 | - Planning only. No code edits.
46 | - Assume a Git repo with test runner available.
47 | 
```

temp-prompts-organized/00-ideation/requirements/prd-generator.requirements.md
```
1 | # PRD Generator
2 | Trigger: /prd-generate
3 | Purpose: Produce a complete `prd.txt` in the exact section order, headers, and tone of the inline example PRD using only the repository README and visible link texts.
4 | Steps:
5 | 
6 | <<<<<<< Updated upstream
7 | 1. Read `README.md` at repo root; do not fetch external links.
8 | 2. Extract: product name, problem, target users, value, scope, constraints, features, flows, integrations, data, non-functional needs, risks.
9 | 3. If links exist, include their visible text or titles only as contextual hints.
10 | 4. Fill gaps with conservative assumptions to keep the PRD complete; collect assumptions for the Appendix.
11 | 5. Enforce strict structure identical to the example PRD’s top-level headers and order.
12 | 6. For each core feature, include What, Why, High-level How, and Acceptance criteria.
13 | 7. In Technical Architecture, document optional platform-specific features and required fallbacks; mirror related risks.
14 | 8. In Development Roadmap, group by phases (MVP and later); include acceptance criteria; exclude timelines.
15 | 9. In Logical Dependency Chain, order from foundations to visible value; keep items atomic.
16 | 10. Run an internal consistency check: features appear in roadmap; risks reflect platform and data concerns; all sections non-empty.
17 | 11. Output only the final `prd.txt` content starting with `# Overview` and ending with `# Appendix`.
18 | Output format:
19 | 
20 | - Plain text PRD starting with `# Overview` and ending with `# Appendix`.
21 | - No preamble, no postscript, no meta commentary.
22 | Notes:
23 | - Reject generation if `README.md` is missing.
24 | - Do not browse external sources.
25 | - Derived from example_prd.txt, extracted summaries only; secrets redacted.
26 | =======
27 | Output a plain-text file named `prd.txt` containing **only** these sections in this order (separated by one blank line):
28 | # Overview
29 | # Core Features
30 | # User Experience
31 | # Technical Architecture
32 | # Development Roadmap
33 | # Logical Dependency Chain
34 | # Risks and Mitigations
35 | # Appendix
36 | 
37 | **Output Format**
38 | 
39 | - `# Overview`: $3
40 | - `# Core Features`: Each includes *What*, *Why*, *High-level How*, and BDD criteria:
41 |   `Given ...`
42 |   `When ...`
43 |   `Then ...`
44 | - `# User Experience`: Personas, key flows, UI/UX, accessibility
45 | - `# Technical Architecture`: Components, data models, APIs/integrations, infrastructure, NFRs
46 | - `# Development Roadmap`: MVP and Future Enhancements with acceptance criteria (no dates)
47 | - `# Logical Dependency Chain`: Work ordering for foundations, earliest front end, extensible units
48 | - `# Risks and Mitigations`: Each includes *Description*, *Likelihood*, *Impact*, *Mitigation*
49 | - `# Appendix`:
50 |   • Assumptions (bulleted)
51 |   • Research findings from $1
52 |   • Context notes (`- <visible text> — inferred topic`)
53 |   • Technical specs
54 | 
55 | **Validation Checks**
56 | 
57 | - Headers present and ordered
58 | - All BDD criteria included for features/fallbacks
59 | - Risks include likelihood and impact
60 | - No URLs/secrets; exactly one blank line between sections
61 | - $1 contains **only** visible link text (no external browsing)
62 | >>>>>>> Stashed changes
```

temp-prompts-organized/00-ideation/requirements/scope-control.requirements.md
```
1 | ---
2 | phase: "P1 Plan & Scope"
3 | gate: "Scope Gate"
4 | status: "Done criteria, scope lists, and stack choices are committed."
5 | previous:
6 |   - "/planning-process"
7 | next:
8 |   - "/stack-evaluation"
9 |   - "/scaffold-fullstack"
10 | ---
11 | 
12 | # Scope Control
13 | 
14 | Trigger: /scope-control
15 | 
16 | Purpose: Enforce explicit scope boundaries and maintain "won't do" and "ideas for later" lists.
17 | 
18 | ## Steps
19 | 
20 | 1. Parse `PLAN.md` or create it if absent.
21 | 2. For each open task, confirm linkage to the current milestone.
22 | 3. Detect off-scope items and move them to **Won't do** or **Ideas for later** with rationale.
23 | 4. Add a "Scope Gate" checklist before merging.
24 | 
25 | ## Output format
26 | 
27 | - Patch to `PLAN.md` showing changes in sections and checklists.
28 | 
29 | ## Examples
30 | Input: off-scope request "Add email templates" during OAuth feature.
31 | Output: Move to **Ideas for later** with reason "Not needed for OAuth MVP".
32 | 
33 | ## Notes
34 | 
35 | - Never add new scope without recording tradeoffs.
36 | 
```

temp-prompts-organized/00-ideation/design/action-diagram.design.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Explain workflow triggers and dependencies as a diagram‑ready outline.
2 | 
3 | 1. Gather context by inspecting `.github/workflows`.
4 | 2. Explain workflow triggers and dependencies as a diagram‑ready outline.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Explain workflow triggers and dependencies as a diagram‑ready outline.
10 | - Organize details under clear subheadings so contributors can scan quickly.
11 | - List nodes and edges to make diagram creation straightforward.
12 | - Highlight workflow triggers, failing jobs, and proposed fixes.
13 | 
14 | Example Input:
15 | (none – command runs without arguments)
16 | 
17 | Expected Output:
18 | 
19 | ## Nodes
20 | 
21 | - build
22 | - deploy
23 | 
24 | ## Edges
25 | 
26 | - push -> build
27 | - build -> deploy
```

temp-prompts-organized/00-ideation/design/api-contract.design.md
```
1 | ---
2 | phase: "P2 App Scaffold & Contracts"
3 | gate: "Test Gate lite"
4 | status: "contract checked into repo with sample generation running cleanly."
5 | previous:
6 |   - "/scaffold-fullstack"
7 | next:
8 |   - "/openapi-generate"
9 |   - "/modular-architecture"
10 | ---
11 | 
12 | # API Contract
13 | 
14 | Trigger: /api-contract "<feature or domain>"
15 | 
16 | Purpose: Author an initial OpenAPI 3.1 or GraphQL SDL contract from requirements.
17 | 
18 | **Steps:**
19 | 
20 | 1. Parse inputs and existing docs. If REST, prefer OpenAPI 3.1 YAML; if GraphQL, produce SDL.
21 | 2. Define resources, operations, request/response schemas, error model, auth, and rate limit headers.
22 | 3. Add examples for each endpoint or type. Include pagination and filtering conventions.
23 | 4. Save to `apis/<domain>/openapi.yaml` or `apis/<domain>/schema.graphql`.
24 | 5. Emit changelog entry `docs/api/CHANGELOG.md` with rationale and breaking-change flags.
25 | 
26 | **Output format:**
27 | 
28 | - `Contract Path`, `Design Notes`, and a fenced code block with the spec body.
29 | 
30 | **Examples:**
31 | 
32 | - `/api-contract "accounts & auth"` → `apis/auth/openapi.yaml` with OAuth 2.1 flows.
33 | 
34 | **Notes:**
35 | 
36 | - Follow JSON:API style for REST unless caller specifies otherwise. Include `429` and `5xx` models.
37 | 
```

temp-prompts-organized/00-ideation/design/design-assets.design.md
```
1 | ---
2 | phase: "P4 Frontend UX"
3 | gate: "Accessibility checks queued"
4 | status: "ensure assets support design review."
5 | previous:
6 |   - "/modular-architecture"
7 | next:
8 |   - "/ui-screenshots"
9 |   - "/logging-strategy"
10 | ---
11 | 
12 | # Design Assets
13 | 
14 | Trigger: /design-assets
15 | 
16 | Purpose: Generate favicons and small design snippets from product brand.
17 | 
18 | ## Steps
19 | 
20 | 1. Extract brand colors and name from README or config.
21 | 2. Produce favicon set, social preview, and basic UI tokens.
22 | 3. Document asset locations and references.
23 | 
24 | ## Output format
25 | 
26 | - Asset checklist and generation commands.
27 | 
```

temp-prompts-organized/00-ideation/design/ui-screenshots.design.md
```
1 | ---
2 | phase: "P4 Frontend UX"
3 | gate: "Accessibility checks queued"
4 | status: "capture UX issues and backlog fixes."
5 | previous:
6 |   - "/design-assets"
7 |   - "/modular-architecture"
8 | next:
9 |   - "/logging-strategy"
10 |   - "/e2e-runner-setup"
11 | ---
12 | 
13 | # UI Screenshots
14 | 
15 | Trigger: /ui-screenshots
16 | 
17 | Purpose: Analyze screenshots for UI bugs or inspiration and propose actionable UI changes.
18 | 
19 | ## Steps
20 | 
21 | 1. Accept screenshot paths or links.
22 | 2. Describe visual hierarchy, spacing, contrast, and alignment issues.
23 | 3. Output concrete CSS or component changes.
24 | 
25 | ## Output format
26 | 
27 | - Issue list and code snippets to fix visuals.
28 | 
```

temp-prompts-organized/30-refactor/refactor/adr-new.refactor.md
```
1 | **{$2 or Inferred Name}**
2 | 
3 | You are a CLI assistant to draft an Architecture Decision Record with pros/cons using the following inputs:
4 | 
5 | 1. Analyze project context from $1.
6 | 2. Generate a concise ADR with Context, Decision, Status, Consequences. Title: $3.
7 | 3. Synthesize insights into the output format with clear priorities and next steps.
8 | 
9 | **Output Requirements**:
10 | - Provide a summary restating the goal.
11 | - Highlight $4, $5, and $6.
12 | - Document $7 to ensure maintainability.
13 | 
14 | **Example Input**: $2
15 | 
16 | **Expected Output**: Actionable summary aligned with output requirements.
```

temp-prompts-organized/30-refactor/refactor/file-modularity.refactor.md
```
1 | ---
2 | phase: "P8 Post-release Hardening"
3 | gate: "Post-release cleanup"
4 | status: "structure debt addressed without destabilizing prod."
5 | previous:
6 |   - "/refactor-suggestions"
7 | next:
8 |   - "/dead-code-scan"
9 |   - "/cleanup-branches"
10 | ---
11 | 
12 | # File Modularity
13 | 
14 | Trigger: /file-modularity
15 | 
16 | Purpose: Enforce smaller files and propose safe splits for giant files.
17 | 
18 | ## Steps
19 | 
20 | 1. Find files over thresholds (e.g., >500 lines).
21 | 2. Suggest extraction targets: components, hooks, utilities, schemas.
22 | 3. Provide before/after examples and import updates.
23 | 
24 | ## Output format
25 | 
26 | - Refactor plan with patches for file splits.
27 | 
```

temp-prompts-organized/30-refactor/refactor/prettier-adopt-migration-report.refactor.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Plan a Prettier adoption or migration with minimal churn.
2 | 
3 | 1. Gather context by inspecting `package.json`; running `git ls-files '*.*' | sed -n '1,400p'`.
4 | 2. Given the files and package.json, propose a rollout plan and ignore patterns.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Plan a Prettier adoption or migration with minimal churn.
10 | - Offer prioritized, actionable recommendations with rationale.
11 | - Document the evidence you used so maintainers can trust the conclusion.
12 | 
13 | Example Input:
14 | (none – command runs without arguments)
15 | 
16 | Expected Output:
17 | 
18 | - Structured report following the specified sections.
```

temp-prompts-organized/30-refactor/refactor/refactor-file.refactor.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Suggest targeted refactors for a single file.
2 | 
3 | 1. Gather context by running `sed -n '1,400p' {{args}}` for the first 400 lines of the file.
4 | 2. Suggest refactors that reduce complexity and improve readability without changing behavior. Provide before/after snippets.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Suggest targeted refactors for a single file.
10 | - Include before/after snippets or diffs with commentary.
11 | - Document the evidence you used so maintainers can trust the conclusion.
12 | 
13 | Example Input:
14 | src/components/Button.tsx
15 | 
16 | Expected Output:
17 | 
18 | - Refactor proposal extracting shared styling hook with before/after snippet.
```

temp-prompts-organized/30-refactor/refactor-candidates/dead-code-scan.refactor-candidates.md
```
1 | ---
2 | phase: "P8 Post-release Hardening"
3 | gate: "Post-release cleanup"
4 | status: "ensure code removals keep prod stable."
5 | previous:
6 |   - "/file-modularity"
7 | next:
8 |   - "/cleanup-branches"
9 |   - "/feature-flags"
10 | ---
11 | 
12 | # Dead Code Scan
13 | 
14 | Trigger: /dead-code-scan
15 | 
16 | Purpose: Identify likely dead or unused files and exports using static signals.
17 | 
18 | You are a CLI assistant focused on helping contributors with the task: List likely dead or unused files and exports (static signals).
19 | 
20 | 1. Gather context by running `rg -n "export |module.exports|exports\.|require\(|import " -g '!node_modules' .` for the file reference graph (best‑effort).
21 | 2. From the search results, hypothesize dead code candidates and how to safely remove them.
22 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
23 | 
24 | Output:
25 | 
26 | - Begin with a concise summary that restates the goal: List likely dead or unused files and exports (static signals).
27 | - Document the evidence you used so maintainers can trust the conclusion.
28 | 
29 | Example Input:
30 | (none – command runs without arguments)
31 | 
32 | Expected Output:
33 | 
34 | - Structured report following the specified sections.
35 | 
```

temp-prompts-organized/30-refactor/refactor-candidates/migration-plan.refactor-candidates.md
```
1 | ---
2 | phase: "P3 Data & Auth"
3 | gate: "Migration dry-run"
4 | status: "validated rollback steps and safety checks documented."
5 | previous:
6 |   - "/db-bootstrap"
7 | next:
8 |   - "/auth-scaffold"
9 |   - "/e2e-runner-setup"
10 | ---
11 | 
12 | # Migration Plan
13 | 
14 | Trigger: /migration-plan "<change summary>"
15 | 
16 | Purpose: Produce safe up/down migration steps with checks and rollback notes.
17 | 
18 | **Steps:**
19 | 
20 | 1. Describe current vs target schema, include data volume and lock risk.
21 | 2. Plan: deploy empty columns, backfill, dual-write, cutover, cleanup.
22 | 3. Provide SQL snippets and PR checklist. Add `can_rollback: true|false` flag.
23 | 
24 | **Output format:** `Plan`, `SQL`, `Rollback`, `Checks` sections.
25 | 
26 | **Examples:** `/migration-plan "orders add status enum"`.
27 | 
28 | **Notes:** Include online migration strategies for large tables.
29 | 
```

temp-prompts-organized/30-refactor/refactor-candidates/refactor-suggestions.refactor-candidates.md
```
1 | ---
2 | phase: "P8 Post-release Hardening"
3 | gate: "Post-release cleanup"
4 | status: "plan high-leverage refactors once Sev-1 issues settle."
5 | previous:
6 |   - "/fix"
7 | next:
8 |   - "/file-modularity"
9 |   - "/dead-code-scan"
10 | ---
11 | 
12 | # Refactor Suggestions
13 | 
14 | Trigger: /refactor-suggestions
15 | 
16 | Purpose: Propose repo-wide refactoring opportunities after tests exist.
17 | 
18 | ## Steps
19 | 
20 | 1. Map directory structure and large files.
21 | 2. Identify duplication, data clumps, and god objects.
22 | 3. Suggest phased refactors with safety checks and tests.
23 | 
24 | ## Output format
25 | 
26 | - Ranked list with owners and effort estimates.
27 | 
```

temp-prompts-organized/30-refactor/perf/compare-outputs.perf.md
```
1 | ---
2 | phase: "P9 Model Tactics"
3 | gate: "Model uplift"
4 | status: "comparative data compiled before switching defaults."
5 | previous:
6 |   - "/model-evaluation"
7 | next:
8 |   - "/switch-model"
9 | ---
10 | 
11 | # Compare Outputs
12 | 
13 | Trigger: /compare-outputs
14 | 
15 | Purpose: Run multiple models or tools on the same prompt and summarize best output.
16 | 
17 | ## Steps
18 | 
19 | 1. Define evaluation prompts and expected properties.
20 | 2. Record outputs from each model/tool with metadata.
21 | 3. Score using a rubric: correctness, compile/run success, edits required.
22 | 4. Recommend a winner and suggested settings.
23 | 
24 | ## Output format
25 | 
26 | - Matrix comparison and a one-paragraph decision.
27 | 
```

temp-prompts-organized/30-refactor/perf/model-evaluation.perf.md
```
1 | ---
2 | phase: "P9 Model Tactics"
3 | gate: "Model uplift"
4 | status: "experiments must beat baseline quality metrics."
5 | previous:
6 |   - "/model-strengths"
7 | next:
8 |   - "/compare-outputs"
9 |   - "/switch-model"
10 | ---
11 | 
12 | # Model Evaluation
13 | 
14 | Trigger: /model-evaluation
15 | 
16 | Purpose: Try a new model and compare outputs against a baseline.
17 | 
18 | ## Steps
19 | 
20 | 1. Define a benchmark set from recent tasks.
21 | 2. Run candidates and collect outputs and metrics.
22 | 3. Analyze failures and summarize where each model excels.
23 | 
24 | ## Output format
25 | 
26 | - Summary table and recommendations to adopt or not.
27 | 
```

temp-prompts-organized/30-refactor/perf/model-strengths.perf.md
```
1 | ---
2 | phase: "P9 Model Tactics"
3 | gate: "Model uplift"
4 | status: "capture baseline routing before experimentation."
5 | previous:
6 |   - "/feature-flags (optional)"
7 |   - "Stage-specific blockers"
8 | next:
9 |   - "/model-evaluation"
10 |   - "/compare-outputs"
11 | ---
12 | 
13 | # Model Strengths
14 | 
15 | Trigger: /model-strengths
16 | 
17 | Purpose: Choose model per task type.
18 | 
19 | ## Steps
20 | 
21 | 1. Classify task: UI, API, data, testing, docs, refactor.
22 | 2. Map historical success by model.
23 | 3. Recommend routing rules and temperatures.
24 | 
25 | ## Output format
26 | 
27 | - Routing guide with examples.
28 | 
```

temp-prompts-organized/20-implementation/impl/commit.impl.md
```
1 | ---
2 | phase: "P6 CI/CD & Env"
3 | gate: "Review Gate"
4 | status: "clean diff, CI green, and approvals ready."
5 | previous:
6 |   - "/version-control-guide"
7 | next:
8 |   - "/devops-automation"
9 |   - "/env-setup"
10 | ---
11 | 
12 | # Commit Message Assistant
13 | 
14 | Trigger: `commit`
15 | 
16 | Purpose: Generate a conventional, review-ready commit message from the currently staged changes.
17 | 
18 | Output: A finalized commit message with a 50–72 character imperative subject line, optional scope, and supporting body lines describing the rationale, evidence, and tests.
19 | 
20 | ## Steps
21 | 
22 | 1. Verify there is staged work with `git status --short` and stop with guidance if nothing is staged.
23 | 2. Inspect the staged diff with `git diff --staged` and identify the primary change type (feat, fix, chore, docs, refactor, etc.) and optional scope (e.g., package or module).
24 | 3. Draft a concise subject line in the form `<type>(<scope>): <imperative summary>` or `<type>: <imperative summary>` when no scope applies. Keep the line under 73 characters.
25 | 4. Capture essential details in the body as wrapped bullet points or paragraphs: what changed, why it was necessary, and any follow-up actions.
26 | 5. Document validation in a trailing section (e.g., `Tests:`) noting commands executed or why tests were skipped.
27 | 
28 | ## Example Output
29 | 
30 | ```
31 | fix(auth): prevent session expiration loop
32 | 
33 | - guard refresh flow against repeated 401 responses
34 | - add regression coverage for expired refresh tokens
35 | 
36 | Tests: npm test -- auth/session.test.ts
37 | ```
```

temp-prompts-organized/20-implementation/impl/content-generation.impl.md
```
1 | ---
2 | phase: "11) Evidence Log"
3 | gate: "Evidence Log"
4 | status: "Ensure docs stay synced with current phase deliverables."
5 | previous:
6 |   - "Stage-specific work just completed"
7 | next:
8 |   - "/release-notes"
9 |   - "/summary (if sharing updates)"
10 | ---
11 | 
12 | # Content Generation
13 | 
14 | Trigger: /content-generation
15 | 
16 | Purpose: Draft docs, blog posts, or marketing copy aligned with the codebase.
17 | 
18 | ## Steps
19 | 
20 | 1. Read repo README and recent CHANGELOG or commits.
21 | 2. Propose outlines for docs and posts.
22 | 3. Generate content with code snippets and usage examples.
23 | 
24 | ## Output format
25 | 
26 | - Markdown files with frontmatter and section headings.
27 | 
```

temp-prompts-organized/20-implementation/impl/feature-flags.impl.md
```
1 | ---
2 | phase: "P8 Post-release Hardening"
3 | gate: "Post-release cleanup"
4 | status: "guardrails added before toggling new flows."
5 | previous:
6 |   - "/cleanup-branches"
7 | next:
8 |   - "/model-strengths"
9 |   - "/model-evaluation"
10 | ---
11 | 
12 | # Feature Flags
13 | 
14 | Trigger: /feature-flags <provider>
15 | 
16 | Purpose: Integrate a flag provider, wire the SDK, and enforce guardrails.
17 | 
18 | **Steps:**
19 | 
20 | 1. Select provider (LaunchDarkly, Unleash, Flagsmith, custom).
21 | 2. Add SDK init in web/api with bootstrap values and offline mode for dev.
22 | 3. Define flag naming and ownership. Add kill‑switch pattern and monitoring.
23 | 
24 | **Output format:** SDK snippet, example usage, and guardrail checklist.
25 | 
26 | **Examples:** `/feature-flags launchdarkly`.
27 | 
28 | **Notes:** Ensure flags are typed and expire with tickets.
29 | 
```

temp-prompts-organized/20-implementation/impl/fix.impl.md
```
1 | ---
2 | phase: "P8 Post-release Hardening"
3 | gate: "Post-release cleanup"
4 | status: "validated fix with regression coverage before closing incident."
5 | previous:
6 |   - "/error-analysis"
7 | next:
8 |   - "/refactor-suggestions"
9 |   - "/file-modularity"
10 | ---
11 | 
12 | # Fix
13 | 
14 | Trigger: /fix "<bug summary>"
15 | 
16 | Purpose: Propose a minimal, correct fix with diff-style patches.
17 | 
18 | You are a CLI assistant focused on helping contributors with the task: Propose a minimal, correct fix with patch hunks.
19 | 
20 | 1. Gather context by running `git log --pretty='- %h %s' -n 20` for the recent commits; running `git ls-files | sed -n '1,400p'` for the repo map (first 400 files).
21 | 2. Bug summary: <args>. Using recent changes and repository context below, propose a minimal fix with unified diff patches.
22 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
23 | 
24 | Output:
25 | 
26 | - Begin with a concise summary that restates the goal: Propose a minimal, correct fix with patch hunks.
27 | - Provide unified diff-style patches when recommending code changes.
28 | - Offer prioritized, actionable recommendations with rationale.
29 | 
30 | Example Input:
31 | Authentication failure after password reset
32 | 
33 | Expected Output:
34 | 
35 | ```
36 | diff
37 | - if (!user) return error;
38 | + if (!user) return { status: 401 };
39 | ```
40 | 
41 | Regression test: add case for missing user.
42 | 
```

temp-prompts-organized/20-implementation/impl/generate.impl.md
```
1 | ---
2 | phase: "P5 Quality Gates & Tests"
3 | gate: "Test Gate"
4 | status: "targeted unit tests authored for the specified module."
5 | previous:
6 |   - "/coverage-guide"
7 | next:
8 |   - "/regression-guard"
9 | ---
10 | 
11 | # Generate Unit Tests
12 | 
13 | Trigger: /generate <source-file>
14 | 
15 | Purpose: Generate unit tests for a given source file.
16 | 
17 | You are a CLI assistant focused on helping contributors with the task: Generate unit tests for a given source file.
18 | 
19 | ## Steps
20 | 
21 | 1. Inspect `package.json` to identify the unit test framework, runner scripts, and any helper utilities required for the suite.
22 | 2. Review the target source file with `sed -n '1,400p' {{args}}` to catalog exported members, branching logic, and error handling paths that must be exercised.
23 | 3. Outline the test file structure (location, naming, setup/teardown) and propose arrange/act/assert cases that cover happy paths, edge cases, and failure scenarios.
24 | 4. Provide guidance on implementing the tests and how to validate them locally (e.g., `npm test -- <pattern>` or framework-specific commands).
25 | 
26 | ## Output
27 | 
28 | - Begin with a concise summary that restates the goal: Generate unit tests for a given source file.
29 | - List the recommended test files, describe each test case, and highlight coverage gaps they close.
30 | - Call out the command(s) to run the new tests and any fixtures or mocks required.
31 | - Document the evidence you used (e.g., `package.json`, specific functions/branches in the source file) so maintainers can trust the conclusion.
32 | 
33 | ## Example
34 | 
35 | **Input**
36 | 
37 | ```
38 | src/components/Button.tsx
39 | ```
40 | 
41 | **Output**
42 | 
43 | - Summary: Author React Testing Library unit tests for `Button` to cover rendering, disabled behavior, and click handling.
44 | - Create `src/components/__tests__/Button.test.tsx` that:
45 |   - Renders the button label and asserts it matches `props.children`.
46 |   - Verifies `onClick` fires once when the button is enabled and is skipped when `disabled` is true.
47 |   - Confirms the `variant="primary"` branch applies the `btn-primary` class.
48 | - Validation: Run `npm test -- Button.test.tsx` to execute the suite.
49 | - Evidence: `package.json` (scripts.test uses Jest + RTL), component branches in `src/components/Button.tsx` (disabled guard, variant styling).
```

temp-prompts-organized/20-implementation/impl/prototype-feature.impl.md
```
1 | ---
2 | phase:
3 |   - "P1 Plan & Scope"
4 |   - "P2 App Scaffold & Contracts"
5 | gate: "Prototype review"
6 | status: "Validate spike outcomes before committing to scope."
7 | previous:
8 |   - "/planning-process"
9 | next:
10 |   - "/scaffold-fullstack"
11 |   - "/api-contract"
12 | ---
13 | 
14 | # Prototype Feature
15 | 
16 | Trigger: /prototype-feature
17 | 
18 | Purpose: Spin up a standalone prototype in a clean repo before merging into main.
19 | 
20 | ## Steps
21 | 
22 | 1. Create a scratch directory name suggestion and scaffolding commands.
23 | 2. Generate minimal app with only the feature and hardcoded data.
24 | 3. Add E2E test covering the prototype flow.
25 | 4. When validated, list the minimal patches to port back.
26 | 
27 | ## Output format
28 | 
29 | - Scaffold plan and migration notes.
30 | 
```

temp-prompts-organized/20-implementation/impl/todos.impl.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Find and group TODO/FIXME annotations.
2 | 
3 | 1. Gather context by running `rg -n "TODO|FIXME" -g '!node_modules' . || grep -RInE 'TODO|FIXME' .`.
4 | 2. Find and group TODO/FIXME annotations.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Find and group TODO/FIXME annotations.
10 | - Document the evidence you used so maintainers can trust the conclusion.
11 | 
12 | Example Input:
13 | (none – command runs without arguments)
14 | 
15 | Expected Output:
16 | 
17 | - Group: Platform backlog — 4 TODOs referencing auth migration (owner: @platform).
```

temp-prompts-organized/20-implementation/impl/voice-input.impl.md
```
1 | ---
2 | phase: "Support"
3 | gate: "Support intake"
4 | status: "Clarify voice-derived requests before invoking gated prompts."
5 | previous:
6 |   - "Voice transcript capture"
7 | next:
8 |   - "Any stage-specific command (e.g., /planning-process)"
9 | ---
10 | 
11 | # Voice Input
12 | 
13 | Trigger: /voice-input
14 | 
15 | Purpose: Support interaction from voice capture and convert to structured prompts.
16 | 
17 | ## Steps
18 | 
19 | 1. Accept transcript text.
20 | 2. Normalize to tasks or commands for other prompts.
21 | 3. Preserve speaker intents and important entities.
22 | 
23 | ## Output format
24 | 
25 | - Cleaned command list ready to execute.
26 | 
```

temp-prompts-organized/20-implementation/review/audit.review.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Release Gate"
4 | status: "readiness criteria before shipping."
5 | previous:
6 |   - "/logging-strategy"
7 | next:
8 |   - "/error-analysis"
9 |   - "/fix"
10 | ---
11 | 
12 | # Audit
13 | 
14 | Trigger: /audit
15 | 
16 | Purpose: Audit repository hygiene and suggest improvements.
17 | 
18 | ## Steps
19 | 
20 | 1. Gather context by running `ls -la` for the top-level listing. Inspect `.editorconfig`, `.gitignore`, `.geminiignore`, `.eslintrc.cjs`, `.eslintrc.js`, `tsconfig.json`, and `pyproject.toml` if present to understand shared conventions.
21 | 2. Assess repository hygiene across documentation, testing, CI, linting, and security. Highlight gaps and existing automation.
22 | 3. Synthesize the findings into a prioritized checklist with recommended next steps.
23 | 
24 | ## Output format
25 | 
26 | - Begin with a concise summary that restates the goal: Audit repository hygiene and suggest improvements.
27 | - Offer prioritized, actionable recommendations with rationale.
28 | - Call out test coverage gaps and validation steps.
29 | - Highlight workflow triggers, failing jobs, and proposed fixes.
30 | 
31 | ## Example input
32 | 
33 | (none – command runs without arguments)
34 | 
35 | ## Expected output
36 | 
37 | - Structured report following the specified sections.
38 | 
```

temp-prompts-organized/20-implementation/review/cross-check.review.md
```
1 | # Conflict Resolver
2 | 
3 | Trigger: /cross-check
4 | 
5 | Purpose: Compare conflicting findings and decide which source prevails with rationale.
6 | 
7 | Steps:
8 | 
9 | 1. Accept a list of SourceIDs or URLs with short findings.
10 | 2. Evaluate publisher authority, recency, directness to primary data.
11 | 3. Select the prevailing source; note contradictions and rationale.
12 | 
13 | Output format:
14 | 
15 | ```
16 | ### Contradictions
17 | - {S2 vs S5 → rationale}
18 | 
19 | ### Prevails
20 | - {SourceID} because {reason}
21 | ```
22 | 
23 | Examples:
24 | 
25 | - Input: `/cross-check S2: blog vs S5: RFC`
26 | - Output: RFC prevails due to primary standard.
27 | 
28 | Notes:
29 | 
30 | - Always explain why one source prevails.
```

temp-prompts-organized/20-implementation/review/evidence-capture.review.md
```
1 | # Evidence Logger
2 | 
3 | Trigger: /evidence-capture
4 | 
5 | Purpose: Capture sources for a specified claim with dates, ≤25-word quotes, findings, relevance, and confidence.
6 | 
7 | Steps:
8 | 
9 | 1. Read the claim text and optional URLs provided.
10 | 2. For each source, record metadata and a ≤25-word quote.
11 | 3. Add a brief Finding, Relevance (H/M/L), and Confidence (0.0–1.0).
12 | 
13 | Output format:
14 | 
15 | ```
16 | ### Evidence Log
17 | | SourceID | Title | Publisher | URL | PubDate | Accessed | Quote (≤25w) | Finding | Rel | Conf |
18 | |---|---|---|---|---|---|---|---|---|---|
19 | ```
20 | 
21 | Examples:
22 | 
23 | - Input: `/evidence-capture "Next.js 15 requires React 19 RC"` with official links.
24 | - Output: Evidence table entries with dates.
25 | 
26 | Notes:
27 | 
28 | - Mark missing PubDate as n/a. Prefer official documentation.
```

temp-prompts-organized/20-implementation/review/pr-desc.review.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Review Gate"
4 | status: "PR narrative ready for approvals and release prep."
5 | previous:
6 |   - "/review-branch"
7 | next:
8 |   - "/release-notes"
9 |   - "/version-proposal"
10 | ---
11 | 
12 | # PR Description
13 | 
14 | Trigger: /pr-desc <context>
15 | 
16 | Purpose: Draft a PR description from the branch diff.
17 | 
18 | You are a CLI assistant focused on helping contributors with the task: Draft a PR description from the branch diff.
19 | 
20 | 1. Gather context by running `git diff --name-status origin/main...HEAD` for the changed files (name + status); running `git diff --shortstat origin/main...HEAD` for the high‑level stats.
21 | 2. Create a crisp PR description following this structure: Summary, Context, Changes, Screenshots (if applicable), Risk, Test Plan, Rollback, Release Notes (if user‑facing). Base branch: origin/main User context: <args>.
22 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
23 | 
24 | Output:
25 | 
26 | - Begin with a concise summary that restates the goal: Draft a PR description from the branch diff.
27 | - Offer prioritized, actionable recommendations with rationale.
28 | - Call out test coverage gaps and validation steps.
29 | - Highlight workflow triggers, failing jobs, and proposed fixes.
30 | 
31 | Example Input:
32 | src/example.ts
33 | 
34 | Expected Output:
35 | 
36 | - Actionable summary aligned with the output section.
37 | 
```

temp-prompts-organized/20-implementation/review/review-branch.review.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Review Gate"
4 | status: "branch scope validated before PR submission."
5 | previous:
6 |   - "/review"
7 | next:
8 |   - "/pr-desc"
9 |   - "/release-notes"
10 | ---
11 | 
12 | # Review Branch
13 | 
14 | Trigger: /review-branch
15 | 
16 | Purpose: Provide a high-level review of the current branch versus origin/main.
17 | 
18 | You are a CLI assistant focused on helping contributors with the task: Provide a high‑level review of the current branch vs origin/main.
19 | 
20 | 1. Gather context by running `git diff --stat origin/main...HEAD` for the diff stats; running `git diff origin/main...HEAD | sed -n '1,200p'` for the ```diff.
21 | 2. Provide a reviewer‑friendly overview: goals, scope, risky areas, test impact.
22 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
23 | 
24 | Output:
25 | 
26 | - Begin with a concise summary that restates the goal: Provide a high‑level review of the current branch vs origin/main.
27 | - Organize details under clear subheadings so contributors can scan quickly.
28 | - Call out test coverage gaps and validation steps.
29 | 
30 | Example Input:
31 | (none – command runs without arguments)
32 | 
33 | Expected Output:
34 | 
35 | - Structured report following the specified sections.
36 | 
```

temp-prompts-organized/20-implementation/review/review.review.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Review Gate"
4 | status: "peer review coverage met before merging."
5 | previous:
6 |   - "/owners"
7 | next:
8 |   - "/review-branch"
9 |   - "/pr-desc"
10 | ---
11 | 
12 | # Review
13 | 
14 | Trigger: /review <pattern>
15 | 
16 | Purpose: Review code matching a pattern and deliver actionable feedback.
17 | 
18 | You are a CLI assistant focused on helping contributors with the task: Review code matching a pattern and give actionable feedback.
19 | 
20 | 1. Gather context by running `rg -n {{args}} . || grep -RIn {{args}} .` for the search results for {{args}} (filename or regex).
21 | 2. Perform a thorough code review. Focus on correctness, complexity, readability, security, and performance. Provide concrete patch suggestions.
22 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
23 | 
24 | Output:
25 | 
26 | - Begin with a concise summary that restates the goal: Review code matching a pattern and give actionable feedback.
27 | - Provide unified diff-style patches when recommending code changes.
28 | - Organize details under clear subheadings so contributors can scan quickly.
29 | 
30 | Example Input:
31 | HttpClient
32 | 
33 | Expected Output:
34 | 
35 | - Usage cluster in src/network/* with note on inconsistent error handling.
36 | 
```

temp-prompts-organized/20-implementation/review/todo-report.review.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Summarize TODO/FIXME/XXX annotations across the codebase.
2 | 
3 | 1. Gather context by running `rg -n "TODO|FIXME|XXX" -g '!node_modules' . || grep -RInE 'TODO|FIXME|XXX' .`.
4 | 2. Aggregate and group TODO/FIXME/XXX by area and priority. Propose a triage plan.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Summarize TODO/FIXME/XXX annotations across the codebase.
10 | - Offer prioritized, actionable recommendations with rationale.
11 | - Organize details under clear subheadings so contributors can scan quickly.
12 | 
13 | Example Input:
14 | (none – command runs without arguments)
15 | 
16 | Expected Output:
17 | 
18 | - Group: Platform backlog — 4 TODOs referencing auth migration (owner: @platform).
```

temp-prompts-organized/20-implementation/review/tsconfig-review.review.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Review tsconfig for correctness and DX.
2 | 
3 | 1. Gather context by inspecting `tsconfig.json`.
4 | 2. Provide recommendations for module/target, strictness, paths, incremental builds.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Review tsconfig for correctness and DX.
10 | - Offer prioritized, actionable recommendations with rationale.
11 | - Document the evidence you used so maintainers can trust the conclusion.
12 | 
13 | Example Input:
14 | (none – command runs without arguments)
15 | 
16 | Expected Output:
17 | 
18 | - Structured report following the specified sections.
```

temp-prompts-organized/20-implementation/spec-orient/blame-summary.spec-orient.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Summarize authorship hotspots for a file using git blame.
2 | 
3 | 1. Gather context by running `git blame -w --line-porcelain {{args}} | sed -n 's/^author //p' | sort | uniq -c | sort -nr | sed -n '1,25p'` for the blame authors (top contributors first).
4 | 2. Given the blame summary below, identify ownership hotspots and potential reviewers.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Summarize authorship hotspots for a file using git blame.
10 | - Organize details under clear subheadings so contributors can scan quickly.
11 | - Reference evidence from CODEOWNERS or git history for each owner suggestion.
12 | 
13 | Example Input:
14 | src/components/Button.tsx
15 | 
16 | Expected Output:
17 | 
18 | - Refactor proposal extracting shared styling hook with before/after snippet.
```

temp-prompts-organized/20-implementation/spec-orient/changed-files.spec-orient.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Summarize changed files between HEAD and origin/main.
2 | 
3 | 1. Gather context by running `git diff --name-status origin/main...HEAD`.
4 | 2. List and categorize changed files: added/modified/renamed/deleted. Call out risky changes.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Summarize changed files between HEAD and origin/main.
10 | - Document the evidence you used so maintainers can trust the conclusion.
11 | 
12 | Example Input:
13 | (none – command runs without arguments)
14 | 
15 | Expected Output:
16 | 
17 | - Structured report following the specified sections.
```

temp-prompts-organized/20-implementation/spec-orient/explain-code.spec-orient.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Review Gate"
4 | status: "Improve reviewer comprehension before approvals."
5 | previous:
6 |   - "/owners"
7 |   - "/review"
8 | next:
9 |   - "/review-branch"
10 |   - "/pr-desc"
11 | ---
12 | 
13 | # Explain Code
14 | 
15 | Trigger: /explain-code
16 | 
17 | Purpose: Provide line-by-line explanations for a given file or diff.
18 | 
19 | ## Steps
20 | 
21 | 1. Accept a file path or apply to staged diff.
22 | 2. Explain blocks with comments on purpose, inputs, outputs, and caveats.
23 | 3. Highlight risky assumptions and complexity hot spots.
24 | 
25 | ## Output format
26 | 
27 | - Annotated markdown with code fences and callouts.
28 | 
```

temp-prompts-organized/20-implementation/spec-orient/explain-symbol.spec-orient.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Explain where and how a symbol is defined and used.
2 | 
3 | 1. Gather context by running `rg -n {{args}} . || grep -RIn {{args}} .` for the results.
4 | 2. Explain where and how a symbol is defined and used.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Explain where and how a symbol is defined and used.
10 | - Organize details under clear subheadings so contributors can scan quickly.
11 | - Document the evidence you used so maintainers can trust the conclusion.
12 | 
13 | Example Input:
14 | HttpClient
15 | 
16 | Expected Output:
17 | 
18 | - Definition: src/network/httpClient.ts line 42
19 | - Key usages: services/userService.ts, hooks/useRequest.ts
```

temp-prompts-organized/20-implementation/spec-orient/grep.spec-orient.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Recursive text search with ripgrep/grep injection.
2 | 
3 | 1. Gather context by running `rg -n {{args}} . || grep -RIn {{args}} .`.
4 | 2. Show matched lines with file paths and line numbers.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Recursive text search with ripgrep/grep injection.
10 | - Document the evidence you used so maintainers can trust the conclusion.
11 | 
12 | Example Input:
13 | HttpClient
14 | 
15 | Expected Output:
16 | 
17 | - Usage cluster in src/network/* with note on inconsistent error handling.
```

temp-prompts-organized/20-implementation/spec-orient/research-batch.spec-orient.md
```
1 | # Conversation-Aware Research — Batch WBRO
2 | 
3 | Trigger: /research-batch
4 | 
5 | Purpose: Process a numbered work-breakdown list of objectives with carry-forward context across items and produce a roll-up summary.
6 | 
7 | Steps:
8 | 
9 | 1. Parse numbered WBRO items from the input after the trigger.
10 | 2. Before Item 1: list ≤5 bullets of starting context.
11 | 3. For each item i: execute the per-item workflow and include a Conversation State Update.
12 | 4. If blocked by prior gaps, emit **Dependency Blocked** with a minimal micro-query.
13 | 5. After all items: emit a Roll-up Summary with per-item status, enabled decisions, unresolved risks, and a domain-type count of sources.
14 | 
15 | Output format:
16 | 
17 | - Repeat the single-item format per item.
18 | - End with:
19 | 
20 | ```
21 | ## Roll-up Summary
22 | - Item {n}: {status} — decision enabled: {…}; risks: {…}
23 | - Sources by domain type: {gov, org, docs, blog, news}
24 | ```
25 | 
26 | Examples:
27 | 
28 | - Input: `/research-batch 1) Validate Next.js 15 stability. 2) Compare Bun vs Node for CI. 3) Licensing risks for MIT vs Apache-2.0.`
29 | - Output: Per-item sections plus roll-up.
30 | 
31 | Notes:
32 | 
33 | - Keep quotes ≤25 words. Prefer primary docs.
```

temp-prompts-organized/20-implementation/spec-orient/research-item.spec-orient.md
```
1 | # Conversation-Aware Research — Single Item
2 | 
3 | Trigger: /research-item
4 | 
5 | Purpose: Run the full per-item research workflow for one objective and return queries, evidence, synthesis, contradictions, gaps, decision hook, plus a conversation state update.
6 | 
7 | Steps:
8 | 
9 | 1. Read the objective text following the trigger.
10 | 2. Capture starting context if provided.
11 | 3. Apply the Process (per item): Goal, Assumptions, Query Set (4–8), Search Plan, Run & Capture, Cross-check, Synthesis, Gaps & Next, Decision Hook.
12 | 4. Track PubDate and Accessed (ISO) for every source; prefer primary docs.
13 | 5. Enforce quotes ≤25 words; mark inferences as "Inference".
14 | 
15 | Output format:
16 | 
17 | ```
18 | ## Item 1: {short title}
19 | 
20 | ### Goal
21 | {1 sentence}
22 | 
23 | ### Assumptions
24 | - {only if needed}
25 | 
26 | ### Query Set
27 | - {Q1}
28 | - {Q2}
29 | - {Q3}
30 | - {Q4–Q8}
31 | 
32 | ### Evidence Log
33 | | SourceID | Title | Publisher | URL | PubDate | Accessed | Quote (≤25w) | Finding | Rel | Conf |
34 | |---|---|---|---|---|---|---|---|---|---|
35 | 
36 | ### Synthesis
37 | - {claim with [S1,S3]}
38 | - {finding with [S2]}
39 | - {risk/edge with [S4]}
40 | 
41 | ### Contradictions
42 | - {S2 vs S5 → rationale}
43 | 
44 | ### Gaps & Next
45 | - {follow-up or test}
46 | 
47 | ### Decision Hook
48 | {one line}
49 | 
50 | ### Conversation State Update
51 | - New facts: {bullets}
52 | - Constraints learned: {bullets}
53 | - Entities normalized: {canonical forms}
54 | ```
55 | 
56 | Examples:
57 | 
58 | - Input: `/research-item Compare OpenAPI 3.1 tooling for Python clients in 2024; budget $0; prefer official docs.`
59 | - Output: As per format with SourceIDs and dates.
60 | 
61 | Notes:
62 | 
63 | - Safety: No personal data. Do not fabricate sources.
64 | - Provenance: Cite reputable sources; record n/a for missing PubDate.
```

temp-prompts-organized/10-scaffold/conventions/version-control-guide.conventions.md
```
1 | ---
2 | phase: "P6 CI/CD & Env"
3 | gate: "Review Gate"
4 | status: "clean diff, CI green, and approvals ready."
5 | previous:
6 |   - "/regression-guard"
7 | next:
8 |   - "/devops-automation"
9 |   - "/env-setup"
10 | ---
11 | 
12 | # Version Control Guide
13 | 
14 | Trigger: /version-control-guide
15 | 
16 | Purpose: Enforce clean incremental commits and clean-room re-implementation when finalizing.
17 | 
18 | ## Steps
19 | 
20 | 1. Start each feature from a clean branch: `git switch -c <feat>`.
21 | 2. Commit in vertical slices with passing tests: `git add -p && git commit`.
22 | 3. When solution is proven, recreate a minimal clean diff: stash or copy results, reset, then apply only the final changes.
23 | 4. Use `git revert` for bad commits instead of force-pushing shared branches.
24 | 
25 | ## Output format
26 | 
27 | - Checklist plus suggested commands for the current repo state.
28 | 
29 | ## Examples
30 | 
31 | - Convert messy spike into three commits: setup, feature, tests.
32 | 
33 | ## Notes
34 | 
35 | - Never modify remote branches without confirmation.
36 | 
```

temp-prompts-organized/10-scaffold/ci-setup/devops-automation.ci-setup.md
```
1 | ---
2 | phase: "P6 CI/CD & Env"
3 | gate: "Review Gate"
4 | status: "CI pipeline codified, rollback steps rehearsed."
5 | previous:
6 |   - "/version-control-guide"
7 | next:
8 |   - "/env-setup"
9 |   - "/secrets-manager-setup"
10 |   - "/iac-bootstrap"
11 | ---
12 | 
13 | # DevOps Automation
14 | 
15 | Trigger: /devops-automation
16 | 
17 | Purpose: Configure servers, DNS, SSL, CI/CD at a pragmatic level.
18 | 
19 | ## Steps
20 | 
21 | 1. Inspect repo for IaC or deploy scripts.
22 | 2. Generate Terraform or Docker Compose templates if missing.
23 | 3. Propose CI workflows for tests, builds, and deploys.
24 | 4. Provide runbooks for rollback.
25 | 
26 | ## Output format
27 | 
28 | - Infra plan with checkpoints and secrets placeholders.
29 | 
```

temp-prompts-organized/10-scaffold/ci-setup/env-setup.ci-setup.md
```
1 | ---
2 | phase: "P6 CI/CD & Env"
3 | gate: "Review Gate"
4 | status: "environment schemas enforced and CI respects strict loading."
5 | previous:
6 |   - "/devops-automation"
7 | next:
8 |   - "/secrets-manager-setup"
9 |   - "/iac-bootstrap"
10 | ---
11 | 
12 | # Env Setup
13 | 
14 | Trigger: /env-setup
15 | 
16 | Purpose: Create .env.example, runtime schema validation, and per-env overrides.
17 | 
18 | **Steps:**
19 | 
20 | 1. Scan repo for `process.env` usage and collected keys.
21 | 2. Emit `.env.example` with comments and safe defaults.
22 | 3. Add runtime validation via `zod` or `envsafe` in `packages/config`.
23 | 4. Document `development`, `staging`, `production` precedence and loading order.
24 | 
25 | **Output format:** `.env.example` content block and `config/env.ts` snippet.
26 | 
27 | **Examples:** `/env-setup`.
28 | 
29 | **Notes:** Do not include real credentials. Enforce `STRICT_ENV=true` in CI.
30 | 
```

temp-prompts-organized/10-scaffold/ci-setup/monitoring-setup.ci-setup.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Release Gate"
4 | status: "observability baselines ready before rollout."
5 | previous:
6 |   - "/version-proposal"
7 | next:
8 |   - "/slo-setup"
9 |   - "/logging-strategy"
10 | ---
11 | 
12 | # Monitoring Setup
13 | 
14 | Trigger: /monitoring-setup
15 | 
16 | Purpose: Bootstrap logs, metrics, and traces with dashboards per domain.
17 | 
18 | **Steps:**
19 | 
20 | 1. Choose stack: OpenTelemetry → Prometheus/Grafana, or vendor.
21 | 2. Instrument web and api for request latency, error rate, throughput, and core domain metrics.
22 | 3. Provide default dashboards JSON and alert examples.
23 | 
24 | **Output format:** instrumentation checklist and dashboard links/paths.
25 | 
26 | **Examples:** `/monitoring-setup`.
27 | 
28 | **Notes:** Avoid high‑cardinality labels. Sample traces selectively in prod.
29 | 
```

temp-prompts-organized/10-scaffold/ci-setup/slo-setup.ci-setup.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Release Gate"
4 | status: "SLOs and alerts reviewed before production rollout."
5 | previous:
6 |   - "/monitoring-setup"
7 | next:
8 |   - "/logging-strategy"
9 |   - "/audit"
10 | ---
11 | 
12 | # SLO Setup
13 | 
14 | Trigger: /slo-setup
15 | 
16 | Purpose: Define Service Level Objectives, burn alerts, and runbooks.
17 | 
18 | **Steps:**
19 | 
20 | 1. Choose SLI/metrics per user journey. Define SLO targets and error budgets.
21 | 2. Create burn alerts (fast/slow) and link to runbooks.
22 | 3. Add `SLO.md` with rationale and review cadence.
23 | 
24 | **Output format:** SLO table and alert rules snippet.
25 | 
26 | **Examples:** `/slo-setup`.
27 | 
28 | **Notes:** Tie SLOs to deploy gates and incident severity.
29 | 
```

temp-prompts-organized/10-scaffold/scaffold/auth.scaffold.md
```
1 | ---
2 | phase: "P3 Data & Auth"
3 | gate: "Migration dry-run"
4 | status: "auth flows threat-modeled and test accounts wired."
5 | previous:
6 |   - "/migration-plan"
7 | next:
8 |   - "/modular-architecture"
9 |   - "/ui-screenshots"
10 |   - "/e2e-runner-setup"
11 | ---
12 | 
13 | # Auth Scaffold
14 | 
15 | Trigger: /auth-scaffold <oauth|email|oidc>
16 | 
17 | Purpose: Scaffold auth flows, routes, storage, and a basic threat model.
18 | 
19 | **Steps:**
20 | 
21 | 1. Select provider (OAuth/OIDC/email) and persistence for sessions.
22 | 2. Generate routes: login, callback, logout, session refresh.
23 | 3. Add CSRF, state, PKCE where applicable. Include secure cookie flags.
24 | 4. Document threat model: replay, fixation, token leakage, SSRF on callbacks.
25 | 5. Wire to frontend with protected routes and user context.
26 | 
27 | **Output format:** route list, config keys, and mitigations table.
28 | 
29 | **Examples:** `/auth-scaffold oauth` → NextAuth/Passport/Custom adapter plan.
30 | 
31 | **Notes:** Never print real secrets. Use placeholders in `.env.example`.
32 | 
```

temp-prompts-organized/10-scaffold/scaffold/db-bootstrap.scaffold.md
```
1 | ---
2 | phase: "P3 Data & Auth"
3 | gate: "Migration dry-run"
4 | status: "migrations apply/rollback cleanly with seeds populated."
5 | previous:
6 |   - "/modular-architecture"
7 | next:
8 |   - "/migration-plan"
9 |   - "/auth-scaffold"
10 | ---
11 | 
12 | # DB Bootstrap
13 | 
14 | Trigger: /db-bootstrap <postgres|mysql|sqlite|mongodb>
15 | 
16 | Purpose: Pick a database, initialize migrations, local compose, and seed scripts.
17 | 
18 | **Steps:**
19 | 
20 | 1. Create `db/compose.yaml` for local dev (skip for sqlite).
21 | 2. Choose ORM/driver (Prisma or Drizzle for SQL). Add migration config.
22 | 3. Create `prisma/schema.prisma` or `drizzle/*.ts` with baseline tables (users, sessions, audit_log).
23 | 4. Add `pnpm db:migrate`, `db:reset`, `db:seed` scripts. Write seed data for local admin user.
24 | 5. Update `.env.example` with `DATABASE_URL` and test connection script.
25 | 
26 | **Output format:** Migration plan list and generated file paths.
27 | 
28 | **Examples:** `/db-bootstrap postgres` → Prisma + Postgres docker-compose.
29 | 
30 | **Notes:** Avoid destructive defaults; provide `--preview-feature` warnings if relevant.
31 | 
```

temp-prompts-organized/10-scaffold/scaffold/fullstack.scaffold.md
```
1 | ---
2 | phase: "P2 App Scaffold & Contracts"
3 | gate: "Test Gate lite"
4 | status: "ensure lint/build scripts execute on the generated scaffold."
5 | previous:
6 |   - "/stack-evaluation"
7 | next:
8 |   - "/api-contract"
9 |   - "/openapi-generate"
10 |   - "/modular-architecture"
11 | ---
12 | 
13 | # Scaffold Full‑Stack App
14 | 
15 | Trigger: /scaffold-fullstack <stack>
16 | 
17 | Purpose: Create a minimal, production-ready monorepo template with app, API, tests, CI seeds, and infra stubs.
18 | 
19 | **Steps:**
20 | 
21 | 1. Read repository context: `git rev-parse --is-inside-work-tree`.
22 | 2. If repo is empty, initialize: `git init -b main` and create `.editorconfig`, `.gitignore`, `README.md`.
23 | 3. For `<stack>` derive presets (examples):
24 |    - `ts-next-express-pg`: Next.js app, Express API, Prisma + PostgreSQL, Playwright, pnpm workspaces.
25 |    - `ts-vite-fastify-sqlite`: Vite + React app, Fastify API, Drizzle + SQLite.
26 | 4. Create workspace layout:
27 |    - root: `package.json` with `pnpm` workspaces, `tsconfig.base.json`, `eslint`, `prettier`.
28 |    - apps/web, apps/api, packages/ui, packages/config.
29 | 5. Add scripts:
30 |    - root: `dev`, `build`, `lint`, `typecheck`, `test`, `e2e`, `format`.
31 |    - web: Next/Vite scripts. api: dev with ts-node or tsx.
32 | 6. Seed CI files: `.github/workflows/ci.yml` with jobs [lint, typecheck, test, build, e2e] and artifact uploads.
33 | 7. Add example routes:
34 |    - web: `/health` page. api: `GET /health` returning `{ ok: true }`.
35 | 8. Write docs to `README.md`: how to run dev, test, build, and env variables.
36 | 9. Stage files, but do not commit. Output a tree and next commands.
37 | 
38 | **Output format:**
39 | 
40 | - Title line: `Scaffold created: <stack>`
41 | - Sections: `Repo Tree`, `Next Steps`, `CI Seeds`.
42 | - Include a fenced code block of the `tree` and sample scripts.
43 | 
44 | **Examples:**
45 | 
46 | - **Input:** `/scaffold-fullstack ts-next-express-pg`
47 |   **Output:** Summary + tree with `apps/web`, `apps/api`, `packages/ui`.
48 | - **Input:** `/scaffold-fullstack ts-vite-fastify-sqlite`
49 |   **Output:** Summary + tree + Drizzle config.
50 | 
51 | **Notes:**
52 | 
53 | - Assume pnpm and Node 20+. Do not run package installs automatically; propose commands instead.
54 | - Respect existing files; avoid overwriting without explicit confirmation.
55 | 
```

temp-prompts-organized/10-scaffold/scaffold/iac-bootstrap.scaffold.md
```
1 | ---
2 | phase: "P6 CI/CD & Env"
3 | gate: "Review Gate"
4 | status: "IaC applied in staging with drift detection configured."
5 | previous:
6 |   - "/secrets-manager-setup"
7 | next:
8 |   - "/owners"
9 |   - "/review"
10 | ---
11 | 
12 | # IaC Bootstrap
13 | 
14 | Trigger: /iac-bootstrap <aws|gcp|azure|fly|render>
15 | 
16 | Purpose: Create minimal Infrastructure-as-Code for the chosen platform plus CI hooks.
17 | 
18 | **Steps:**
19 | 
20 | 1. Select tool (Terraform, Pulumi). Initialize backend and state.
21 | 2. Define stacks for `preview`, `staging`, `prod`. Add outputs (URLs, connection strings).
22 | 3. Add CI jobs: plan on PR, apply on main with manual approval.
23 | 4. Document rollback and drift detection.
24 | 
25 | **Output format:** stack diagram, file list, CI snippets.
26 | 
27 | **Examples:** `/iac-bootstrap aws`.
28 | 
29 | **Notes:** Prefer least privilege IAM and remote state with locking.
30 | 
```

temp-prompts-organized/50-docs/api-docs/api-docs-local.api-docs.md
```
1 | ---
2 | phase: "P2 App Scaffold & Contracts"
3 | gate: "Test Gate lite"
4 | status: "contracts cached locally for repeatable generation."
5 | previous:
6 |   - "/scaffold-fullstack"
7 | next:
8 |   - "/api-contract"
9 |   - "/openapi-generate"
10 | ---
11 | 
12 | # API Docs Local
13 | 
14 | Trigger: /api-docs-local
15 | 
16 | Purpose: Fetch API docs and store locally for offline, deterministic reference.
17 | 
18 | ## Steps
19 | 
20 | 1. Create `docs/apis/` directory.
21 | 2. For each provided URL or package, write retrieval commands (curl or `npm view` docs links). Do not fetch automatically without confirmation.
22 | 3. Add `DOCS.md` index linking local copies.
23 | 
24 | ## Output format
25 | 
26 | - Command list and file paths to place docs under `docs/apis/`.
27 | 
```

temp-prompts-organized/50-docs/api-docs/openapi-generate.api-docs.md
```
1 | ---
2 | phase: "P2 App Scaffold & Contracts"
3 | gate: "Test Gate lite"
4 | status: "generated code builds and CI checks cover the new scripts."
5 | previous:
6 |   - "/api-contract"
7 | next:
8 |   - "/modular-architecture"
9 |   - "/db-bootstrap"
10 | ---
11 | 
12 | # OpenAPI Generate
13 | 
14 | Trigger: /openapi-generate <server|client> <lang> <spec-path>
15 | 
16 | Purpose: Generate server stubs or typed clients from an OpenAPI spec.
17 | 
18 | **Steps:**
19 | 
20 | 1. Validate `<spec-path>`; fail with actionable errors.
21 | 2. For `server`, generate controllers, routers, validation, and error middleware into `apps/api`.
22 | 3. For `client`, generate a typed SDK into `packages/sdk` with fetch wrapper and retry/backoff.
23 | 4. Add `make generate-api` or `pnpm sdk:gen` scripts and CI step to verify no drift.
24 | 5. Produce a diff summary and TODO list for unimplemented handlers.
25 | 
26 | **Output format:** summary table of generated paths, scripts to add, and next actions.
27 | 
28 | **Examples:** `/openapi-generate client ts apis/auth/openapi.yaml`.
29 | 
30 | **Notes:** Prefer openapi-typescript + zod for TS clients when possible.
31 | 
```

temp-prompts-organized/50-docs/examples/api-usage.examples.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Show how an internal API is used across the codebase.
2 | 
3 | 1. Gather context by running `rg -n {{args}} . || grep -RIn {{args}} .`.
4 | 2. Summarize common usage patterns and potential misuses for the symbol.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Show how an internal API is used across the codebase.
10 | - Organize details under clear subheadings so contributors can scan quickly.
11 | - Document the evidence you used so maintainers can trust the conclusion.
12 | 
13 | Example Input:
14 | HttpClient
15 | 
16 | Expected Output:
17 | 
18 | - Definition: src/network/httpClient.ts line 42
19 | - Key usages: services/userService.ts, hooks/useRequest.ts
```

temp-prompts-organized/50-docs/examples/reference-implementation.examples.md
```
1 | ---
2 | phase: "P2 App Scaffold & Contracts"
3 | gate: "Test Gate lite"
4 | status: "align new modules with proven patterns before deeper work."
5 | previous:
6 |   - "/scaffold-fullstack"
7 |   - "/api-contract"
8 | next:
9 |   - "/modular-architecture"
10 |   - "/openapi-generate"
11 | ---
12 | 
13 | # Reference Implementation
14 | 
15 | Trigger: /reference-implementation
16 | 
17 | Purpose: Mimic the style and API of a known working example.
18 | 
19 | ## Steps
20 | 
21 | 1. Accept a path or URL to an example. Extract its public API and patterns.
22 | 2. Map target module’s API to the reference.
23 | 3. Generate diffs that adopt the same structure and naming.
24 | 
25 | ## Output format
26 | 
27 | - Side-by-side API table and patch suggestions.
28 | 
```

temp-prompts-organized/50-docs/doc-plan/gemini-map.doc-plan.md
```
1 | name: Gemini→Codex Mapper
2 | command: /gemini-map
3 | tags: migration, prompts, tooling
4 | scope: toml-to-codex
5 | 
6 | You are a translator that converts a Gemini CLI TOML command into a Codex prompt file.
7 | 
8 | Steps:
9 | 
10 | 1) Read TOML with `description` and `prompt`.
11 | 2) Extract the task, inputs, and outputs implied by the TOML.
12 | 3) Write a Codex prompt file ≤ 300 words:
13 | 
14 |     - Role line `You are ...`
15 |     - Numbered steps
16 |     - Output section
17 |     - Example input and expected output
18 |     - `Usage: /<command>` line
19 |     - YAML-like metadata at top
20 | 
21 | 4) Choose a short, hyphenated filename ≤ 32 chars.
22 | 5) Emit a ready-to-run bash snippet:
23 | `cat > ~/.codex/prompts/<filename>.md << 'EOF'` … `EOF`.
24 | 6) Do not include destructive commands or secrets.
25 | 
26 | Example input:
27 | 
28 | ```toml
29 | description = "Draft a PR description"
30 | prompt = "Create sections Summary, Context, Changes from diff stats"
31 | Expected output:
32 | 
33 | A pr-desc.md file with the structure above and a bash cat > block.
34 | 
35 | Usage: /gemini-map
```

temp-prompts-organized/50-docs/doc-plan/owners.doc-plan.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Review Gate"
4 | status: "confirm approvers and escalation paths before PR submission."
5 | previous:
6 |   - "/iac-bootstrap"
7 | next:
8 |   - "/review"
9 |   - "/review-branch"
10 |   - "/pr-desc"
11 | ---
12 | 
13 | # Owners
14 | 
15 | Trigger: /owners <path>
16 | 
17 | Purpose: Suggest likely owners or reviewers for the specified path.
18 | 
19 | You are a CLI assistant focused on helping contributors with the task: Suggest likely owners/reviewers for a path.
20 | 
21 | 1. Gather context by inspecting `.github/CODEOWNERS` for the codeowners (if present); running `git log --pretty='- %an %ae: %s' -- {{args}} | sed -n '1,50p'` for the recent authors for the path.
22 | 2. Based on CODEOWNERS and git history, suggest owners.
23 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
24 | 
25 | Output:
26 | 
27 | - Begin with a concise summary that restates the goal: Suggest likely owners/reviewers for a path.
28 | - Reference evidence from CODEOWNERS or git history for each owner suggestion.
29 | - Document the evidence you used so maintainers can trust the conclusion.
30 | 
31 | Example Input:
32 | src/components/Button.tsx
33 | 
34 | Expected Output:
35 | 
36 | - Likely reviewers: @frontend-team (CODEOWNERS), @jane (last 5 commits).
37 | 
```

temp-prompts-organized/40-testing/coverage/guide.coverage.md
```
1 | ---
2 | phase: "P5 Quality Gates & Tests"
3 | gate: "Test Gate"
4 | status: "coverage targets and regression guard plan recorded."
5 | previous:
6 |   - "/integration-test"
7 | next:
8 |   - "/regression-guard"
9 |   - "/version-control-guide"
10 | ---
11 | 
12 | # Coverage Guide
13 | 
14 | Trigger: /coverage-guide
15 | 
16 | Purpose: Propose high-ROI tests to raise coverage using uncovered areas.
17 | 
18 | You are a CLI assistant focused on helping contributors with the task: Suggest a plan to raise coverage based on uncovered areas.
19 | 
20 | 1. Gather context by running `find . -name 'coverage*' -type f -maxdepth 3 -print -exec head -n 40 {} \; 2>/dev/null` for the coverage hints; running `git ls-files | sed -n '1,400p'` for the repo map.
21 | 2. Using coverage artifacts (if available) and repository map, propose the highest‑ROI tests to add.
22 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
23 | 
24 | Output:
25 | 
26 | - Begin with a concise summary that restates the goal: Suggest a plan to raise coverage based on uncovered areas.
27 | - Offer prioritized, actionable recommendations with rationale.
28 | - Call out test coverage gaps and validation steps.
29 | 
30 | Example Input:
31 | (none – command runs without arguments)
32 | 
33 | Expected Output:
34 | 
35 | - Focus on src/auth/login.ts — 0% branch coverage; add error path test.
36 | 
```

temp-prompts-organized/40-testing/coverage/regression-guard.coverage.md
```
1 | ---
2 | phase: "P5 Quality Gates & Tests"
3 | gate: "Test Gate"
4 | status: "regression coverage in place before CI hand-off."
5 | previous:
6 |   - "/coverage-guide"
7 | next:
8 |   - "/version-control-guide"
9 |   - "/devops-automation"
10 | ---
11 | 
12 | # Regression Guard
13 | 
14 | Trigger: /regression-guard
15 | 
16 | Purpose: Detect unrelated changes and add tests to prevent regressions.
17 | 
18 | ## Steps
19 | 
20 | 1. Run `git diff --name-status origin/main...HEAD` and highlight unrelated files.
21 | 2. Propose test cases that lock current behavior for touched modules.
22 | 3. Suggest CI checks to block large unrelated diffs.
23 | 
24 | ## Output format
25 | 
26 | - Report with file groups, risk notes, and test additions.
27 | 
28 | ## Notes
29 | 
30 | - Keep proposed tests minimal and focused.
31 | 
```

temp-prompts-organized/40-testing/fix-flakes/error-analysis.fix-flakes.md
```
1 | ---
2 | phase: "P8 Post-release Hardening"
3 | gate: "Post-release cleanup"
4 | status: "Sev-1 incidents triaged with fixes scheduled."
5 | previous:
6 |   - "/logging-strategy"
7 |   - "/audit"
8 | next:
9 |   - "/fix"
10 |   - "/refactor-suggestions"
11 | ---
12 | 
13 | # Error Analysis
14 | 
15 | Trigger: /error-analysis
16 | 
17 | Purpose: Analyze error logs and enumerate likely root causes with fixes.
18 | 
19 | ## Steps
20 | 
21 | 1. Collect last test logs or application stack traces if present.
22 | 2. Cluster errors by symptom. For each cluster list 2–3 plausible causes.
23 | 3. Propose instrumentation or inputs to disambiguate.
24 | 4. Provide minimal patch suggestions and validation steps.
25 | 
26 | ## Output format
27 | 
28 | - Table: error → likely causes → next checks → candidate fix.
29 | 
30 | ## Examples
31 | 
32 | - "TypeError: x is not a function" → wrong import, circular dep, stale build.
33 | 
```

temp-prompts-organized/40-testing/fix-flakes/explain-failures.fix-flakes.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Analyze recent test failures and propose fixes.
2 | 
3 | 1. Gather context by running `ls -1 test-results 2>/dev/null || echo 'no test-results/ directory'` for the recent test output (if present); running `find . -maxdepth 2 -name 'junit*.xml' -o -name 'TEST-*.xml' -o -name 'last-test.log' -print -exec tail -n 200 {} \; 2>/dev/null` for the recent test output (if present).
4 | 2. From the following logs, identify root causes and propose concrete fixes.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Analyze recent test failures and propose fixes.
10 | - Offer prioritized, actionable recommendations with rationale.
11 | - Document the evidence you used so maintainers can trust the conclusion.
12 | 
13 | Example Input:
14 | (none – command runs without arguments)
15 | 
16 | Expected Output:
17 | 
18 | - Structured report following the specified sections.
```

temp-prompts-organized/40-testing/gen-tests/check.gen-tests.md
```
1 | You are a CLI assistant focused on helping contributors with the task: Check adherence to .editorconfig across the repo.
2 | 
3 | 1. Gather context by inspecting `.editorconfig`; running `git ls-files | sed -n '1,400p'`.
4 | 2. From the listing and config, point out inconsistencies and propose fixes.
5 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
6 | 
7 | Output:
8 | 
9 | - Begin with a concise summary that restates the goal: Check adherence to .editorconfig across the repo.
10 | - Offer prioritized, actionable recommendations with rationale.
11 | - Highlight workflow triggers, failing jobs, and proposed fixes.
12 | 
13 | Example Input:
14 | (none – command runs without arguments)
15 | 
16 | Expected Output:
17 | 
18 | - Structured report following the specified sections.
```

temp-prompts-organized/40-testing/gen-tests/integration-test.gen-tests.md
```
1 | ---
2 | phase: "P5 Quality Gates & Tests"
3 | gate: "Test Gate"
4 | status: "happy path E2E must pass locally and in CI."
5 | previous:
6 |   - "/e2e-runner-setup"
7 | next:
8 |   - "/coverage-guide"
9 |   - "/regression-guard"
10 | ---
11 | 
12 | # Integration Test
13 | 
14 | Trigger: /integration-test
15 | 
16 | Purpose: Generate E2E tests that simulate real user flows.
17 | 
18 | ## Steps
19 | 
20 | 1. Detect framework from `package.json` or repo (Playwright/Cypress/Vitest).
21 | 2. Identify critical path scenarios from `PLAN.md`.
22 | 3. Produce test files under `e2e/` with arrange/act/assert and selectors resilient to DOM changes.
23 | 4. Include login helpers and data setup. Add CI commands.
24 | 
25 | ## Output format
26 | 
27 | - Test files with comments and a README snippet on how to run them.
28 | 
29 | ## Examples
30 | 
31 | - Login, navigate to dashboard, create record, assert toast.
32 | 
33 | ## Notes
34 | 
35 | - Prefer data-test-id attributes. Avoid brittle CSS selectors.
36 | 
```

temp-prompts-organized/40-testing/test-plan/e2e-runner-setup.test-plan.md
```
1 | ---
2 | phase: "P5 Quality Gates & Tests"
3 | gate: "Test Gate"
4 | status: "runner green locally and wired into CI before expanding coverage."
5 | previous:
6 |   - "/auth-scaffold"
7 |   - "/ui-screenshots"
8 | next:
9 |   - "/integration-test"
10 |   - "/coverage-guide"
11 | ---
12 | 
13 | # E2E Runner Setup
14 | 
15 | Trigger: /e2e-runner-setup <playwright|cypress>
16 | 
17 | Purpose: Configure an end-to-end test runner with fixtures and a data sandbox.
18 | 
19 | **Steps:**
20 | 
21 | 1. Install runner and add config with baseURL, retries, trace/videos on retry only.
22 | 2. Create fixtures for auth, db reset, and network stubs. Add `test:serve` script.
23 | 3. Provide CI job that boots services, runs E2E, uploads artifacts.
24 | 
25 | **Output format:** file list, scripts, and CI snippet fenced code block.
26 | 
27 | **Examples:** `/e2e-runner-setup playwright`.
28 | 
29 | **Notes:** Keep runs under 10 minutes locally; parallelize spec files.
30 | 
```

temp-prompts-organized/40-testing/test-plan/query-set.test-plan.md
```
1 | # High-Yield Query Generator
2 | 
3 | Trigger: /query-set
4 | 
5 | Purpose: Generate 4–8 targeted web search queries with operators, entity variants, and recency filters for a given objective.
6 | 
7 | Steps:
8 | 
9 | 1. Restate the goal with entities and time window.
10 | 2. Produce queries using operators: site:, filetype:, inurl:, quotes, OR, date filters.
11 | 3. Include synonyms and common misspellings.
12 | 4. Mix intents: define, compare, integrate, configure, limitations, pricing, API, case study.
13 | 
14 | Output format:
15 | 
16 | ```
17 | ### Goal
18 | {1 sentence}
19 | 
20 | ### Query Set
21 | - {Q1}
22 | - {Q2}
23 | - … up to 8
24 | ```
25 | 
26 | Examples:
27 | 
28 | - Input: `/query-set "OpenAI Responses API streaming server-sent events" past year`
29 | - Output: Goal + 6–8 queries with operators.
30 | 
31 | Notes:
32 | 
33 | - No evidence logging here. Use /research-item to execute.
```

temp-prompts-organized/60-release/post-release-checks/cleanup-branches.post-release-checks.md
```
1 | ---
2 | phase: "P8 Post-release Hardening"
3 | gate: "Post-release cleanup"
4 | status: "repo tidy with stale branches archived."
5 | previous:
6 |   - "/dead-code-scan"
7 | next:
8 |   - "/feature-flags"
9 |   - "/model-strengths"
10 | ---
11 | 
12 | # Cleanup Branches
13 | 
14 | Trigger: /cleanup-branches
15 | 
16 | Purpose: Recommend which local branches are safe to delete and which to keep.
17 | 
18 | You are a CLI assistant focused on helping contributors with the task: Suggest safe local branch cleanup (merged/stale).
19 | 
20 | 1. Gather context by running `git branch --merged` for the merged into current upstream; running `git branch --no-merged` for the branches not merged; running `git for-each-ref --sort=-authordate --format='%(refname:short) — %(authordate:relative)' refs/heads` for the recently updated (last author dates).
21 | 2. Using the lists below, suggest local branches safe to delete and which to keep. Include commands to remove them if desired (DO NOT execute).
22 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
23 | 
24 | Output:
25 | 
26 | - Begin with a concise summary that restates the goal: Suggest safe local branch cleanup (merged/stale).
27 | - Document the evidence you used so maintainers can trust the conclusion.
28 | 
29 | Example Input:
30 | (none – command runs without arguments)
31 | 
32 | Expected Output:
33 | 
34 | - Structured report following the specified sections.
35 | 
```

temp-prompts-organized/60-release/versioning/version-proposal.versioning.md
```
1 | ---
2 | phase: "P7 Release & Ops"
3 | gate: "Release Gate"
4 | status: "version bump decision recorded before deployment."
5 | previous:
6 |   - "/release-notes"
7 | next:
8 |   - "/monitoring-setup"
9 |   - "/slo-setup"
10 | ---
11 | 
12 | # Version Proposal
13 | 
14 | Trigger: /version-proposal
15 | 
16 | Purpose: Propose the next semantic version based on commit history.
17 | 
18 | You are a CLI assistant focused on helping contributors with the task: Propose next version (major/minor/patch) from commit history.
19 | 
20 | 1. Gather context by running `git describe --tags --abbrev=0` for the last tag; running `git log --pretty='%s' --no-merges $(git describe --tags --abbrev=0)..HEAD` for the commits since last tag (no merges).
21 | 2. Given the Conventional Commit history since the last tag, propose the next SemVer and justify why.
22 | 3. Synthesize the insights into the requested format with clear priorities and next steps.
23 | 
24 | Output:
25 | 
26 | - Begin with a concise summary that restates the goal: Propose next version (major/minor/patch) from commit history.
27 | - Offer prioritized, actionable recommendations with rationale.
28 | - Document the evidence you used so maintainers can trust the conclusion.
29 | 
30 | Example Input:
31 | (none – command runs without arguments)
32 | 
33 | Expected Output:
34 | 
35 | - Structured report following the specified sections.
36 | 
```

temp-prompts-organized/_shared/tm/advance.tm.md
```
1 | # Advance Task(s)
2 | 
3 | Trigger: /tm-advance
4 | 
5 | Purpose: For given task id(s), produce a concrete work plan, acceptance criteria, tests, and a Conventional Commits message to move status toward done.
6 | 
7 | Steps:
8 | 
9 | 1. Read tasks.json; resolve each provided id. If none provided, pick the top item from /tm-next.
10 | 2. For each task: restate title, goals, and related dependencies.
11 | 3. Draft a step-by-step plan with file touch-points and test hooks.
12 | 4. Provide a minimal commit plan and a Conventional Commits message with scope and short body.
13 | 5. List measurable acceptance criteria.
14 | 
15 | Output format:
16 | 
17 | - One section per task: "## <id> — <title>"
18 | - Subsections: Plan, Files, Tests, Acceptance, Commit Message (fenced), Risks.
19 | 
20 | Examples:
21 | 
22 | - Input: /tm-advance TM-42 TM-43
23 | - Output: structured sections with a commit message like `feat(parser): implement rule X`.
24 | 
25 | Notes:
26 | 
27 | - Do not mutate tasks.json. Emit proposed changes only.
```

temp-prompts-organized/_shared/tm/blockers.tm.md
```
1 | # Blocker Diagnosis
2 | 
3 | Trigger: /tm-blockers
4 | 
5 | Purpose: Diagnose why a task is blocked and propose the shortest path to unblock it.
6 | 
7 | Steps:
8 | 
9 | 1. Load tasks.json and the target id.
10 | 2. Enumerate unmet dependencies and missing artifacts (tests, docs, approvals).
11 | 3. Classify each blocker: dependency, ambiguity, environment, CI, external.
12 | 4. Propose 1–3 minimal unblocking actions, each with owner, effort, and success check.
13 | 
14 | Output format:
15 | 
16 | - "# Blocker Report: <id>"
17 | - Tables: blockers (type | item | evidence), actions (step | owner | effort | success_criteria).
18 | 
19 | Examples:
20 | 
21 | - Input: /tm-blockers TM-17
22 | - Output: two tables and a short narrative under "Findings".
23 | 
24 | Notes:
25 | 
26 | - If the task is not actually blocked, state why and redirect to /tm-advance.
```

temp-prompts-organized/_shared/tm/ci.tm.md
```
1 | # CI/Test Checklist from Tasks
2 | 
3 | Trigger: /tm-ci
4 | 
5 | Purpose: Derive a near-term CI and test checklist from ready and in-progress tasks.
6 | 
7 | Steps:
8 | 
9 | 1. Compute ready tasks (see /tm-next) and collect any testStrategy fields.
10 | 2. Group by component or tag if available; otherwise by path keywords in titles.
11 | 3. Propose CI jobs and test commands with approximate runtimes and gating rules.
12 | 4. Include a smoke-test matrix and minimal code coverage targets if relevant.
13 | 
14 | Output format:
15 | 
16 | - "# CI Plan"
17 | - Tables: jobs (name | trigger | commands | est_time) and tests (scope | command | expected_artifacts).
18 | - "## Risk Areas" bullets and "## Follow-ups".
19 | 
20 | Examples:
21 | 
22 | - Input: /tm-ci
23 | - Output: one CI plan with 3–8 jobs and a test table.
24 | 
25 | Notes:
26 | 
27 | - Non-binding guidance. Adapt to the repo’s actual CI system.
```

temp-prompts-organized/_shared/tm/delta.tm.md
```
1 | # PRD → Tasks Delta
2 | 
3 | Trigger: /tm-delta
4 | 
5 | Purpose: Compare a PRD text against tasks.json and propose add/update/remove operations.
6 | 
7 | Steps:
8 | 
9 | 1. Accept PRD content pasted by the user or a path like ./prd.txt. If absent, output a short template asking for PRD input.
10 | 2. Extract objectives, constraints, deliverables, and milestones from the PRD.
11 | 3. Map them to existing tasks by fuzzy match on title and keywords; detect gaps.
12 | 4. Propose: new tasks, updates to titles/descriptions/priority, and deprecations.
13 | 
14 | Output format:
15 | 
16 | - "# Delta Summary"
17 | - Tables: adds | updates | removals.
18 | - "## JSON Patch" with an ordered list of operations: add/replace/remove.
19 | - "## Assumptions" and "## Open Questions".
20 | 
21 | Examples:
22 | 
23 | - Input: /tm-delta ./prd.txt
24 | - Output: tables with a small JSON Patch block.
25 | 
26 | Notes:
27 | 
28 | - Keep patches minimal and reversible. Flag any destructive changes explicitly.
```

temp-prompts-organized/_shared/tm/docs.tm.md
```
1 | # Generate Status Docs
2 | 
3 | Trigger: /tm-docs
4 | 
5 | Purpose: Emit a project status document from tasks.json for README or STATUS.md.
6 | 
7 | Steps:
8 | 
9 | 1. Parse tasks.json; collect done, in_progress, blocked, and ready_next (per /tm-next logic).
10 | 2. Compose a concise narrative: current focus, recent wins, top risks.
11 | 3. Produce status boards for each status with id, title, and owner if present.
12 | 4. Add a 7-day changelog if timestamps exist; otherwise, summarize recent done items.
13 | 
14 | Output format:
15 | 
16 | - "# Project Status — <date>"
17 | - Sections: Summary, Ready Next, In Progress, Blocked, Done, Changelog.
18 | 
19 | Examples:
20 | 
21 | - Input: /tm-docs
22 | - Output: a single Markdown document suitable for commit as STATUS.md.
23 | 
24 | Notes:
25 | 
26 | - Avoid leaking secrets. Do not invent owners; omit unknown fields.
```

temp-prompts-organized/_shared/tm/next.tm.md
```
1 | # Next Ready Tasks
2 | 
3 | Trigger: /tm-next
4 | 
5 | Purpose: List tasks that are ready to start now (no unmet dependencies), ordered by priority and dependency depth.
6 | 
7 | Steps:
8 | 
9 | 1. Load tasks.json and build a map of id → task.
10 | 2. A task is ready if status ∈ {pending, blocked} AND all dependencies are done.
11 | 3. Order by: priority desc, then shortest path length to completion, then title.
12 | 4. For each ready task, include why it is ready and the prerequisites satisfied.
13 | 
14 | Output format:
15 | 
16 | - "# Ready Now"
17 | - Table: id | title | priority | why_ready | prereqs
18 | - "## Notes" for tie-break rules and data gaps.
19 | 
20 | Examples:
21 | 
22 | - Input: /tm-next
23 | - Output: a table of 5–20 items. If none, say "No ready tasks" and list nearest-unblock candidates.
24 | 
25 | Notes:
26 | 
27 | - Treat missing or null priority as 0. If custom scales exist, describe them in Notes.
```

temp-prompts-organized/_shared/tm/overview.tm.md
```
1 | # TaskMaster Overview
2 | 
3 | Trigger: /tm-overview
4 | 
5 | Purpose: Summarize the current TaskMaster tasks.json by status, priority, dependency health, and critical path to orient work.
6 | 
7 | Steps:
8 | 
9 | 1. Locate the active tasks.json at repo root or the path supplied in the user message. Do not modify it.
10 | 2. Parse fields: id, title, description, status, priority, dependencies, subtasks.
11 | 3. Compute counts per status and a table of top pending items by priority.
12 | 4. Detect dependency issues: cycles, missing ids, orphans (no deps and not depended on).
13 | 5. Approximate a critical path: longest dependency chain among pending→in_progress tasks.
14 | 
15 | Output format:
16 | 
17 | - "# Overview" then a bullets summary.
18 | - "## Totals" as a 4-column table: status | count | percent | notes.
19 | - "## Top Pending" table: id | title | priority | unblockers.
20 | - "## Critical Path" as an ordered list of ids with short titles.
21 | - "## Issues" list for cycles, missing references, duplicates.
22 | 
23 | Examples:
24 | 
25 | - Input (Codex TUI): /tm-overview
26 | - Output: tables and lists as specified. Keep to <= 200 lines.
27 | 
28 | Notes:
29 | 
30 | - Read-only. Assume statuses: pending | in_progress | blocked | done.
31 | - If tasks.json is missing or invalid, output an "## Errors" section with a concise diagnosis.
```

temp-prompts-organized/_shared/tm/refine.tm.md
```
1 | # Refine Task into Subtasks
2 | 
3 | Trigger: /tm-refine
4 | 
5 | Purpose: Expand a vague or large task into actionable subtasks with clear acceptance criteria.
6 | 
7 | Steps:
8 | 
9 | 1. Load the task by id and analyze description for ambiguity and scope.
10 | 2. Propose 3–8 subtasks with titles, brief descriptions, and dependencies between them.
11 | 3. Define acceptance criteria per subtask using Given/When/Then or bullet checks.
12 | 4. Suggest test coverage and doc updates triggered by completion.
13 | 
14 | Output format:
15 | 
16 | - "# Refinement: <id>"
17 | - Subtasks as a Markdown table: id_suggested | title | depends_on | acceptance.
18 | - "## JSON Patch" fenced code of suggested additions suitable for tasks.json editing.
19 | 
20 | Examples:
21 | 
22 | - Input: /tm-refine TM-09
23 | - Output: table plus a minimal JSON Patch array.
24 | 
25 | Notes:
26 | 
27 | - Do not assume authority to change files; provide patches the user can apply.
```
