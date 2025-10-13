Output: Agent-ready summary | Constraints: stage-first layout; deterministic order; minimal but actionable | Acceptance criteria: an agent can create/validate the tree, place files correctly from category/stage, and compute include/exclude globs

**Goal**
Organize `prompts/` so stage inference → deterministic execution order.

**Parent dirs (lexical order = lifecycle)**

- `00-ideation/`
- `10-scaffold/`
- `20-implementation/`
- `30-refactor/`
- `40-testing/`
- `50-docs/`
- `60-release/`
- `_shared/` (cross-stage utilities), `_templates/` (authoring), `_experimental/` (WIP), `_archive/` (retired)

**Optional subfolders by category**

- ideation → `requirements/`, `design/`, `architecture/`
- scaffold → `scaffold/`, `conventions/`, `ci-setup/`
- implementation → `spec-orient/`, `impl/`, `review/`
- refactor → `refactor-candidates/`, `refactor/`, `perf/`
- testing → `test-plan/`, `gen-tests/`, `fix-flakes/`, `coverage/`
- docs → `doc-plan/`, `examples/`, `api-docs/`, `site-sync/`
- release → `versioning/`, `changelog/`, `pack-publish/`, `post-release-checks/`

**File naming rule**

- `{slug}.{category}.md` (multi: `{slug}.{cat1}+{cat2}.md`)
  Examples: `implement-endpoint.impl.md`, `prepare-release.versioning+changelog.md`

**Placement logic**

1. Read front-matter: `categories` (or `category`) and optional `stage`.
2. Map `stage` → parent dir; if missing, infer from `categories`.
3. If multi-category, choose parent by primary stage; keep all categories in filename and front-matter.
4. Keep `id` in front-matter (kebab-case); directory location does not change `id`.

**Include/Exclude for ranking/sequencing**

- Include: `prompts/{00-ideation,10-scaffold,20-implementation,30-refactor,40-testing,50-docs,60-release}/**/*.md`
- Exclude: `prompts/_archive/**`, `prompts/_experimental/**`, `prompts/_templates/**` (optionally exclude `_shared/**` from sequencing but include for linting)

**Agent tasks checklist**

- Ensure all parent dirs exist (create if missing).
- Validate filenames match `{slug}.{category}.md`; fix if not.
- Verify front-matter has `id` and `categories`; add/normalize if missing.
- Move files into stage parent (and optional category subfolder) per rules above.
- Produce a report of moves/renames and any files excluded from sequencing.
