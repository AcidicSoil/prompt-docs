Project Structure:
├── 00-ideation
│   ├── architecture
│   │   ├── adr-new.architecture.md
│   │   ├── logging-strategy.architecture.md
│   │   ├── modular-architecture.architecture.md
│   │   └── stack-evaluation.architecture.md
│   ├── design
│   │   ├── action-diagram.design.md
│   │   ├── api-contract.design.md
│   │   ├── design-assets.design.md
│   │   └── ui-screenshots.design.md
│   └── requirements
│       ├── plan-delta.requirements.md
│       ├── planning-process.requirements.md
│       ├── prd-generator.requirements.md
│       └── scope-control.requirements.md
├── 10-scaffold
│   ├── ci-setup
│   │   ├── devops-automation.ci-setup.md
│   │   ├── env-setup.ci-setup.md
│   │   ├── monitoring-setup.ci-setup.md
│   │   ├── secrets-manager-setup.ci-setup.md
│   │   └── slo-setup.ci-setup.md
│   ├── conventions
│   │   └── version-control-guide.conventions.md
│   └── scaffold
│       ├── auth.scaffold.md
│       ├── db-bootstrap.scaffold.md
│       ├── fullstack.scaffold.md
│       └── iac-bootstrap.scaffold.md
├── 20-implementation
│   ├── impl
│   │   ├── commit.impl.md
│   │   ├── content-generation.impl.md
│   │   ├── feature-flags.impl.md
│   │   ├── fix.impl.md
│   │   ├── generate.impl.md
│   │   ├── prototype-feature.impl.md
│   │   ├── todos.impl.md
│   │   └── voice-input.impl.md
│   ├── review
│   │   ├── audit.review.md
│   │   ├── cross-check.review.md
│   │   ├── evidence-capture.review.md
│   │   ├── pr-desc.review.md
│   │   ├── review-branch.review.md
│   │   ├── review.review.md
│   │   ├── todo-report.review.md
│   │   └── tsconfig-review.review.md
│   └── spec-orient
│       ├── blame-summary.spec-orient.md
│       ├── changed-files.spec-orient.md
│       ├── explain-code.spec-orient.md
│       ├── explain-symbol.spec-orient.md
│       ├── grep.spec-orient.md
│       ├── research-batch.spec-orient.md
│       └── research-item.spec-orient.md
├── 30-refactor
│   ├── perf
│   │   ├── compare-outputs.perf.md
│   │   ├── model-evaluation.perf.md
│   │   └── model-strengths.perf.md
│   ├── refactor
│   │   ├── adr-new.refactor.md
│   │   ├── file-modularity.refactor.md
│   │   ├── prettier-adopt-migration-report.refactor.md
│   │   └── refactor-file.refactor.md
│   └── refactor-candidates
│       ├── dead-code-scan.refactor-candidates.md
│       ├── migration-plan.refactor-candidates.md
│       └── refactor-suggestions.refactor-candidates.md
├── 40-testing
│   ├── coverage
│   │   ├── guide.coverage.md
│   │   └── regression-guard.coverage.md
│   ├── fix-flakes
│   │   ├── error-analysis.fix-flakes.md
│   │   └── explain-failures.fix-flakes.md
│   ├── gen-tests
│   │   ├── check.gen-tests.md
│   │   └── integration-test.gen-tests.md
│   └── test-plan
│       ├── e2e-runner-setup.test-plan.md
│       ├── query-set.test-plan.md
│       └── secrets-scan.test-plan.md
├── 50-docs
│   ├── api-docs
│   │   ├── api-docs-local.api-docs.md
│   │   └── openapi-generate.api-docs.md
│   ├── doc-plan
│   │   ├── gemini-map.doc-plan.md
│   │   └── owners.doc-plan.md
│   ├── examples
│   │   ├── api-usage.examples.md
│   │   └── reference-implementation.examples.md
│   └── site-sync
├── 60-release
│   ├── changelog
│   │   ├── from-commits.changelog.md
│   │   ├── project.changelog.md
│   │   ├── release-notes-prepare.changelog.md
│   │   ├── release-notes.changelog.md
│   │   ├── update.changelog.md
│   │   └── verify.changelog.md
│   ├── pack-publish
│   ├── post-release-checks
│   │   ├── cleanup-branches.post-release-checks.md
│   │   └── license-report.post-release-checks.md
│   └── versioning
│       └── version-proposal.versioning.md
├── _archive
├── _experimental
├── _shared
│   ├── rank-root-prompts.shared.md
│   ├── reset-strategy.shared.md
│   ├── roll-up.shared.md
│   ├── summary.shared.md
│   ├── switch-model.shared.md
│   └── tm
│       ├── advance.tm.md
│       ├── blockers.tm.md
│       ├── ci.tm.md
│       ├── delta.tm.md
│       ├── docs.tm.md
│       ├── next.tm.md
│       ├── overview.tm.md
│       └── refine.tm.md
└── _templates
    ├── instruction-file.templates.md
    ├── prompt-sequence-generator.templates.md
    └── system-level-instruction-editor.templates.md


_shared/rank-root-prompts.shared.md
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

_shared/reset-strategy.shared.md
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

_shared/roll-up.shared.md
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

_shared/summary.shared.md
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

_shared/switch-model.shared.md
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

_templates/instruction-file.templates.md
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

_templates/prompt-sequence-generator.templates.md
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

_templates/system-level-instruction-editor.templates.md
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

00-ideation/architecture/adr-new.architecture.md
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

00-ideation/architecture/logging-strategy.architecture.md
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

00-ideation/architecture/modular-architecture.architecture.md
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

00-ideation/architecture/stack-evaluation.architecture.md
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

00-ideation/design/action-diagram.design.md
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

00-ideation/design/api-contract.design.md
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

00-ideation/design/design-assets.design.md
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

00-ideation/design/ui-screenshots.design.md
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

00-ideation/requirements/plan-delta.requirements.md
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

00-ideation/requirements/planning-process.requirements.md
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

00-ideation/requirements/prd-generator.requirements.md
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

00-ideation/requirements/scope-control.requirements.md
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

10-scaffold/conventions/version-control-guide.conventions.md
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

10-scaffold/scaffold/auth.scaffold.md
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

10-scaffold/scaffold/db-bootstrap.scaffold.md
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

10-scaffold/scaffold/fullstack.scaffold.md
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

10-scaffold/scaffold/iac-bootstrap.scaffold.md
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

10-scaffold/ci-setup/devops-automation.ci-setup.md
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

10-scaffold/ci-setup/env-setup.ci-setup.md
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

10-scaffold/ci-setup/monitoring-setup.ci-setup.md
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

10-scaffold/ci-setup/slo-setup.ci-setup.md
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

20-implementation/review/audit.review.md
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

20-implementation/review/cross-check.review.md
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

20-implementation/review/evidence-capture.review.md
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

20-implementation/review/pr-desc.review.md
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

20-implementation/review/review-branch.review.md
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

20-implementation/review/review.review.md
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

20-implementation/review/todo-report.review.md
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

20-implementation/review/tsconfig-review.review.md
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

20-implementation/spec-orient/blame-summary.spec-orient.md
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

20-implementation/spec-orient/changed-files.spec-orient.md
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

20-implementation/spec-orient/explain-code.spec-orient.md
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

20-implementation/spec-orient/explain-symbol.spec-orient.md
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

20-implementation/spec-orient/grep.spec-orient.md
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

20-implementation/spec-orient/research-batch.spec-orient.md
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

20-implementation/spec-orient/research-item.spec-orient.md
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

40-testing/coverage/guide.coverage.md
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

40-testing/coverage/regression-guard.coverage.md
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

20-implementation/impl/commit.impl.md
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

20-implementation/impl/content-generation.impl.md
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

20-implementation/impl/feature-flags.impl.md
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

20-implementation/impl/fix.impl.md
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

20-implementation/impl/generate.impl.md
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

20-implementation/impl/prototype-feature.impl.md
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

20-implementation/impl/todos.impl.md
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

20-implementation/impl/voice-input.impl.md
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

40-testing/gen-tests/check.gen-tests.md
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

40-testing/gen-tests/integration-test.gen-tests.md
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

40-testing/fix-flakes/error-analysis.fix-flakes.md
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

40-testing/fix-flakes/explain-failures.fix-flakes.md
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

40-testing/test-plan/e2e-runner-setup.test-plan.md
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

40-testing/test-plan/query-set.test-plan.md
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

30-refactor/refactor/adr-new.refactor.md
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

30-refactor/refactor/file-modularity.refactor.md
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

30-refactor/refactor/prettier-adopt-migration-report.refactor.md
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

30-refactor/refactor/refactor-file.refactor.md
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

30-refactor/refactor-candidates/dead-code-scan.refactor-candidates.md
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

30-refactor/refactor-candidates/migration-plan.refactor-candidates.md
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

30-refactor/refactor-candidates/refactor-suggestions.refactor-candidates.md
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

30-refactor/perf/compare-outputs.perf.md
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

30-refactor/perf/model-evaluation.perf.md
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

30-refactor/perf/model-strengths.perf.md
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

50-docs/api-docs/api-docs-local.api-docs.md
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

50-docs/api-docs/openapi-generate.api-docs.md
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

50-docs/doc-plan/gemini-map.doc-plan.md
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

50-docs/doc-plan/owners.doc-plan.md
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

50-docs/examples/api-usage.examples.md
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

50-docs/examples/reference-implementation.examples.md
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

60-release/post-release-checks/cleanup-branches.post-release-checks.md
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

60-release/versioning/version-proposal.versioning.md
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

_shared/tm/advance.tm.md
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

_shared/tm/blockers.tm.md
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

_shared/tm/ci.tm.md
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

_shared/tm/delta.tm.md
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

_shared/tm/docs.tm.md
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

_shared/tm/next.tm.md
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

_shared/tm/overview.tm.md
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

_shared/tm/refine.tm.md
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
