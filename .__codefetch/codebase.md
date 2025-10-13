```md
Project Structure:
├── README.md
├── codefetch
│   ├── codebase.md
│   └── prompts
│       └── default.md
├── codefetch.config.mjs
├── docs
│   ├── index.md
│   ├── temp-prompts-organized
│   │   ├── 00-ideation
│   │   │   ├── architecture
│   │   │   │   ├── adr-new.architecture.md
│   │   │   │   ├── logging-strategy.architecture.md
│   │   │   │   ├── modular-architecture.architecture.md
│   │   │   │   └── stack-evaluation.architecture.md
│   │   │   ├── design
│   │   │   │   ├── action-diagram.design.md
│   │   │   │   ├── api-contract.design.md
│   │   │   │   ├── design-assets.design.md
│   │   │   │   └── ui-screenshots.design.md
│   │   │   └── requirements
│   │   │       ├── plan-delta.requirements.md
│   │   │       ├── planning-process.requirements.md
│   │   │       ├── prd-generator.requirements.md
│   │   │       └── scope-control.requirements.md
│   │   ├── 10-scaffold
│   │   │   ├── ci-setup
│   │   │   │   ├── devops-automation.ci-setup.md
│   │   │   │   ├── env-setup.ci-setup.md
│   │   │   │   ├── monitoring-setup.ci-setup.md
│   │   │   │   ├── secrets-manager-setup.ci-setup.md
│   │   │   │   └── slo-setup.ci-setup.md
│   │   │   ├── conventions
│   │   │   │   └── version-control-guide.conventions.md
│   │   │   └── scaffold
│   │   │       ├── auth.scaffold.md
│   │   │       ├── db-bootstrap.scaffold.md
│   │   │       ├── fullstack.scaffold.md
│   │   │       └── iac-bootstrap.scaffold.md
│   │   ├── 20-implementation
│   │   │   ├── impl
│   │   │   │   ├── commit.impl.md
│   │   │   │   ├── content-generation.impl.md
│   │   │   │   ├── feature-flags.impl.md
│   │   │   │   ├── fix.impl.md
│   │   │   │   ├── generate.impl.md
│   │   │   │   ├── prototype-feature.impl.md
│   │   │   │   ├── todos.impl.md
│   │   │   │   └── voice-input.impl.md
│   │   │   ├── review
│   │   │   │   ├── audit.review.md
│   │   │   │   ├── cross-check.review.md
│   │   │   │   ├── evidence-capture.review.md
│   │   │   │   ├── pr-desc.review.md
│   │   │   │   ├── review-branch.review.md
│   │   │   │   ├── review.review.md
│   │   │   │   ├── todo-report.review.md
│   │   │   │   └── tsconfig-review.review.md
│   │   │   └── spec-orient
│   │   │       ├── blame-summary.spec-orient.md
│   │   │       ├── changed-files.spec-orient.md
│   │   │       ├── explain-code.spec-orient.md
│   │   │       ├── explain-symbol.spec-orient.md
│   │   │       ├── grep.spec-orient.md
│   │   │       ├── research-batch.spec-orient.md
│   │   │       └── research-item.spec-orient.md
│   │   ├── 30-refactor
│   │   │   ├── perf
│   │   │   │   ├── compare-outputs.perf.md
│   │   │   │   ├── model-evaluation.perf.md
│   │   │   │   └── model-strengths.perf.md
│   │   │   ├── refactor
│   │   │   │   ├── adr-new.refactor.md
│   │   │   │   ├── file-modularity.refactor.md
│   │   │   │   ├── prettier-adopt-migration-report.refactor.md
│   │   │   │   └── refactor-file.refactor.md
│   │   │   └── refactor-candidates
│   │   │       ├── dead-code-scan.refactor-candidates.md
│   │   │       ├── migration-plan.refactor-candidates.md
│   │   │       └── refactor-suggestions.refactor-candidates.md
│   │   ├── 40-testing
│   │   │   ├── coverage
│   │   │   │   ├── guide.coverage.md
│   │   │   │   └── regression-guard.coverage.md
│   │   │   ├── fix-flakes
│   │   │   │   ├── error-analysis.fix-flakes.md
│   │   │   │   └── explain-failures.fix-flakes.md
│   │   │   ├── gen-tests
│   │   │   │   ├── check.gen-tests.md
│   │   │   │   └── integration-test.gen-tests.md
│   │   │   └── test-plan
│   │   │       ├── e2e-runner-setup.test-plan.md
│   │   │       ├── query-set.test-plan.md
│   │   │       └── secrets-scan.test-plan.md
│   │   ├── 50-docs
│   │   │   ├── api-docs
│   │   │   │   ├── api-docs-local.api-docs.md
│   │   │   │   └── openapi-generate.api-docs.md
│   │   │   ├── doc-plan
│   │   │   │   ├── gemini-map.doc-plan.md
│   │   │   │   └── owners.doc-plan.md
│   │   │   ├── examples
│   │   │   │   ├── api-usage.examples.md
│   │   │   │   └── reference-implementation.examples.md
│   │   │   ├── project-contributing.docs.md
│   │   │   ├── project-readme.docs.md
│   │   │   └── site-sync
│   │   ├── 60-release
│   │   │   ├── changelog
│   │   │   │   ├── from-commits.changelog.md
│   │   │   │   ├── project.changelog.md
│   │   │   │   ├── release-notes-prepare.changelog.md
│   │   │   │   ├── release-notes.changelog.md
│   │   │   │   ├── update.changelog.md
│   │   │   │   └── verify.changelog.md
│   │   │   ├── pack-publish
│   │   │   ├── post-release-checks
│   │   │   │   ├── cleanup-branches.post-release-checks.md
│   │   │   │   └── license-report.post-release-checks.md
│   │   │   └── versioning
│   │   │       └── version-proposal.versioning.md
│   │   ├── _archive
│   │   ├── _experimental
│   │   ├── _shared
│   │   │   ├── rank-root-prompts.shared.md
│   │   │   ├── reset-strategy.shared.md
│   │   │   ├── roll-up.shared.md
│   │   │   ├── summary.shared.md
│   │   │   ├── switch-model.shared.md
│   │   │   └── tm
│   │   │       ├── advance.tm.md
│   │   │       ├── blockers.tm.md
│   │   │       ├── ci.tm.md
│   │   │       ├── delta.tm.md
│   │   │       ├── docs.tm.md
│   │   │       ├── next.tm.md
│   │   │       ├── overview.tm.md
│   │   │       └── refine.tm.md
│   │   ├── _templates
│   │   │   ├── instruction-file.templates.md
│   │   │   ├── prompt-sequence-generator.templates.md
│   │   │   └── system-level-instruction-editor.templates.md
│   │   ├── codefetch
│   │   │   └── codebase.md
│   │   ├── prompt-front-matter
│   │   │   ├── 00-ideation__architecture__adr-new.architecture.refactor.md
│   │   │   ├── 00-ideation__architecture__logging-strategy.architecture.refactor.md
│   │   │   ├── 00-ideation__architecture__modular-architecture.architecture.refactor.md
│   │   │   ├── 00-ideation__architecture__stack-evaluation.architecture.refactor.md
│   │   │   ├── 00-ideation__design__action-diagram.design.refactor.md
│   │   │   ├── 00-ideation__design__api-contract.design.refactor.md
│   │   │   ├── 00-ideation__design__design-assets.design.refactor.md
│   │   │   ├── 00-ideation__design__ui-screenshots.design.refactor.md
│   │   │   ├── 00-ideation__requirements__plan-delta.requirements.refactor.md
│   │   │   ├── 00-ideation__requirements__planning-process.requirements.refactor.md
│   │   │   ├── 00-ideation__requirements__prd-generator.requirements.refactor.md
│   │   │   ├── 00-ideation__requirements__scope-control.requirements.refactor.md
│   │   │   ├── 10-scaffold__ci-setup__devops-automation.ci-setup.refactor.md
│   │   │   ├── 10-scaffold__ci-setup__env-setup.ci-setup.refactor.md
│   │   │   ├── 10-scaffold__ci-setup__monitoring-setup.ci-setup.refactor.md
│   │   │   ├── 10-scaffold__ci-setup__secrets-manager-setup.ci-setup.refactor.md
│   │   │   ├── 10-scaffold__ci-setup__slo-setup.ci-setup.refactor.md
│   │   │   ├── 10-scaffold__conventions__version-control-guide.conventions.refactor.md
│   │   │   ├── 10-scaffold__scaffold__auth.scaffold.refactor.md
│   │   │   ├── 10-scaffold__scaffold__db-bootstrap.scaffold.refactor.md
│   │   │   ├── 10-scaffold__scaffold__fullstack.scaffold.refactor.md
│   │   │   ├── 10-scaffold__scaffold__iac-bootstrap.scaffold.refactor.md
│   │   │   ├── 20-implementation__impl__commit.impl.refactor.md
│   │   │   ├── 20-implementation__impl__content-generation.impl.refactor.md
│   │   │   ├── 20-implementation__impl__feature-flags.impl.refactor.md
│   │   │   ├── 20-implementation__impl__fix.impl.refactor.md
│   │   │   ├── 20-implementation__impl__generate.impl.refactor.md
│   │   │   ├── 20-implementation__impl__prototype-feature.impl.refactor.md
│   │   │   ├── 20-implementation__impl__todos.impl.refactor.md
│   │   │   ├── 20-implementation__impl__voice-input.impl.refactor.md
│   │   │   ├── 20-implementation__review__audit.review.refactor.md
│   │   │   ├── 20-implementation__review__cross-check.review.refactor.md
│   │   │   ├── 20-implementation__review__evidence-capture.review.refactor.md
│   │   │   ├── 20-implementation__review__pr-desc.review.refactor.md
│   │   │   ├── 20-implementation__review__review-branch.review.refactor.md
│   │   │   ├── 20-implementation__review__review.review.refactor.md
│   │   │   ├── 20-implementation__review__todo-report.review.refactor.md
│   │   │   ├── 20-implementation__review__tsconfig-review.review.refactor.md
│   │   │   ├── 20-implementation__spec-orient__blame-summary.spec-orient.refactor.md
│   │   │   ├── 20-implementation__spec-orient__changed-files.spec-orient.refactor.md
│   │   │   ├── 20-implementation__spec-orient__explain-code.spec-orient.refactor.md
│   │   │   ├── 20-implementation__spec-orient__explain-symbol.spec-orient.refactor.md
│   │   │   ├── 20-implementation__spec-orient__grep.spec-orient.refactor.md
│   │   │   ├── 20-implementation__spec-orient__research-batch.spec-orient.refactor.md
│   │   │   ├── 20-implementation__spec-orient__research-item.spec-orient.refactor.md
│   │   │   ├── 30-refactor__perf__compare-outputs.perf.refactor.md
│   │   │   ├── 30-refactor__perf__model-evaluation.perf.refactor.md
│   │   │   ├── 30-refactor__perf__model-strengths.perf.refactor.md
│   │   │   ├── 30-refactor__refactor-candidates__dead-code-scan.refactor-candidates.refactor.md
│   │   │   ├── 30-refactor__refactor-candidates__migration-plan.refactor-candidates.refactor.md
│   │   │   ├── 30-refactor__refactor-candidates__refactor-suggestions.refactor-candidates.refactor.md
│   │   │   ├── 30-refactor__refactor__adr-new.refactor.refactor.md
│   │   │   ├── 30-refactor__refactor__file-modularity.refactor.refactor.md
│   │   │   ├── 30-refactor__refactor__prettier-adopt-migration-report.refactor.refactor.md
│   │   │   ├── 30-refactor__refactor__refactor-file.refactor.refactor.md
│   │   │   ├── 40-testing__coverage__guide.coverage.refactor.md
│   │   │   ├── 40-testing__coverage__regression-guard.coverage.refactor.md
│   │   │   ├── 40-testing__fix-flakes__error-analysis.fix-flakes.refactor.md
│   │   │   ├── 40-testing__fix-flakes__explain-failures.fix-flakes.refactor.md
│   │   │   ├── 40-testing__gen-tests__check.gen-tests.refactor.md
│   │   │   ├── 40-testing__gen-tests__integration-test.gen-tests.refactor.md
│   │   │   ├── 40-testing__test-plan__e2e-runner-setup.test-plan.refactor.md
│   │   │   ├── 40-testing__test-plan__query-set.test-plan.refactor.md
│   │   │   ├── 40-testing__test-plan__secrets-scan.test-plan.refactor.md
│   │   │   ├── 50-docs__api-docs__api-docs-local.api-docs.refactor.md
│   │   │   ├── 50-docs__api-docs__openapi-generate.api-docs.refactor.md
│   │   │   ├── 50-docs__doc-plan__gemini-map.doc-plan.refactor.md
│   │   │   ├── 50-docs__doc-plan__owners.doc-plan.refactor.md
│   │   │   ├── 50-docs__examples__api-usage.examples.refactor.md
│   │   │   ├── 50-docs__examples__reference-implementation.examples.refactor.md
│   │   │   ├── 50-docs__project-contributing.docs.refactor.md
│   │   │   ├── 50-docs__project-readme.docs.refactor.md
│   │   │   ├── 60-release__changelog__from-commits.changelog.refactor.md
│   │   │   ├── 60-release__changelog__project.changelog.refactor.md
│   │   │   ├── 60-release__changelog__release-notes-prepare.changelog.refactor.md
│   │   │   ├── 60-release__changelog__release-notes.changelog.refactor.md
│   │   │   ├── 60-release__changelog__update.changelog.refactor.md
│   │   │   ├── 60-release__changelog__verify.changelog.refactor.md
│   │   │   ├── 60-release__post-release-checks__cleanup-branches.post-release-checks.refactor.md
│   │   │   ├── 60-release__post-release-checks__license-report.post-release-checks.refactor.md
│   │   │   ├── 60-release__versioning__version-proposal.versioning.refactor.md
│   │   │   ├── _shared__rank-root-prompts.shared.refactor.md
│   │   │   ├── _shared__reset-strategy.shared.refactor.md
│   │   │   ├── _shared__roll-up.shared.refactor.md
│   │   │   ├── _shared__summary.shared.refactor.md
│   │   │   ├── _shared__switch-model.shared.refactor.md
│   │   │   ├── _shared__tm__advance.tm.refactor.md
│   │   │   ├── _shared__tm__blockers.tm.refactor.md
│   │   │   ├── _shared__tm__ci.tm.refactor.md
│   │   │   ├── _shared__tm__delta.tm.refactor.md
│   │   │   ├── _shared__tm__docs.tm.refactor.md
│   │   │   ├── _shared__tm__next.tm.refactor.md
│   │   │   ├── _shared__tm__overview.tm.refactor.md
│   │   │   ├── _shared__tm__refine.tm.refactor.md
│   │   │   ├── _templates__instruction-file.templates.refactor.md
│   │   │   ├── _templates__prompt-sequence-generator.templates.refactor.md
│   │   │   └── _templates__system-level-instruction-editor.templates.refactor.md
│   │   └── temp-prompt-worklist.md
│   └── temp-prompts-refactored
│       ├── 3-step-process-b4-refactoring.md
│       ├── Prompt-Optimizer.md
│       ├── action-diagram.md
│       ├── adr-new.md
│       ├── adr-new.refactor.md
│       ├── api-contract.md
│       ├── api-docs-local.md
│       ├── api-usage.md
│       ├── audit.md
│       ├── auth-scaffold.md
│       ├── blame-summary.md
│       ├── changed-files.md
│       ├── changelog-from-commits.md
│       ├── changelog-verify.md
│       ├── check.md
│       ├── cleanup-branches.md
│       ├── commit-msg.md
│       ├── commit.md
│       ├── compare-outputs.md
│       ├── content-generation.md
│       ├── coverage-guide.md
│       ├── cross-check.md
│       ├── db-bootstrap.md
│       ├── dead-code-scan.md
│       ├── design-assets.md
│       ├── devops-automation.md
│       ├── docs-fulfilled-100.md
│       ├── e2e-runner-setup.md
│       ├── env-setup.md
│       ├── error-analysis.md
│       ├── eslint-review.md
│       ├── evidence-capture.md
│       ├── explain-code.md
│       ├── explain-failures.md
│       ├── explain-symbol.md
│       ├── feature-flags.md
│       ├── file-modularity.md
│       ├── fix.md
│       ├── gemini-map.md
│       ├── generate-readme.md
│       ├── generate.md
│       ├── grep.md
│       ├── iac-bootstrap.md
│       ├── instruction-file.md
│       ├── integration-test.md
│       ├── license-report.md
│       ├── logging-strategy.md
│       ├── migration-plan.md
│       ├── missing-docs.md
│       ├── model-evaluation.md
│       ├── model-strengths.md
│       ├── modular-architecture.md
│       ├── monitoring-setup.md
│       ├── openapi-generate.md
│       ├── owners.md
│       ├── plan-delta.md
│       ├── planning-process.md
│       ├── pr-desc.md
│       ├── prd-generator.md
│       ├── prettier-adopt_Migration_report.md
│       ├── problem-analyzer.md
│       ├── prompt-sequence-generator.md
│       ├── prototype-feature.md
│       ├── query-set.md
│       ├── rank-root-prompts.md
│       ├── refactor-file.md
│       ├── refactor-suggestions.md
│       ├── reference-implementation.md
│       ├── regression-guard.md
│       ├── release-notes-prepare.md
│       ├── release-notes.md
│       ├── research-batch.md
│       ├── research-item.md
│       ├── reset-strategy.md
│       ├── review-branch.md
│       ├── review.md
│       ├── roll-up.md
│       ├── scaffold-fullstack.md
│       ├── scope-control.md
│       ├── secrets-manager-setup.md
│       ├── secrets-scan.md
│       ├── slo-setup.md
│       ├── stack-evaluation.md
│       ├── stop-guessing.md
│       ├── summary-1.md
│       ├── summary-2.md
│       ├── summary.md
│       ├── switch-model.md
│       ├── system-level-instruction-editor.md
│       ├── tm-advance.md
│       ├── tm-blockers.md
│       ├── tm-ci.md
│       ├── tm-delta.md
│       ├── tm-docs.md
│       ├── tm-next.md
│       ├── tm-overview.md
│       ├── tm-refine.md
│       ├── todo-report.md
│       ├── todos.md
│       ├── tsconfig-review.md
│       ├── ui-screenshots.md
│       ├── update-changelog.md
│       ├── version-control-guide.md
│       ├── version-proposal.md
│       └── voice-input.md
├── index.html
├── mkdocs.yml
├── pyproject.toml
└── uv.lock
```