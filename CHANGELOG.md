# Changelog

All notable changes to **Qwen Skills** will be documented in this file.

---

## [2.0.0] — 2026-04-09

### Complete Repository Rebuild

Migrated from Gemini CLI skills to Qwen Code skills with full reorganization and cleanup.

### Added
- **155 skills** across 8 professional categories
- **492 source files** totaling 124,184 lines of skill definitions, references, and evaluations
- **llm-wiki-compiler**: Automated knowledge compilation with `check_new_files.py` and `update_state.py` (22 directory watchers, 6,007 files indexed)
- **60+ skills with reference libraries**: Playbooks, templates, and examples
- **30+ skills with eval suites**: Automated evaluation test cases

### New Categories
- **Marketing & Growth** (25): SEO, content, ads, email, CRO
- **Product Management** (20): PRD, user stories, prioritization, roadmaps
- **Development** (15): Code review, TDD, debugging, Git workflows
- **Design & Presentations** (10): PPT, PDF, XLSX, DOCX generation
- **Data & Analytics** (10): Cohort analysis, sentiment, SQL, dashboards
- **AI & LLM** (8): Wiki compiler, AI SEO, model routing
- **Business & Strategy** (15): Competitive analysis, pricing, monetization
- **Communication & Writing** (12): Copywriting, editing, meeting summaries

### Updated
- **LLM Wiki App v2.1**: Complete graph rebuild with 1,810 wikilinks extracted (Karpathy pattern), 1,616 graph links across 1,343 nodes
- **Dashboard v2.1**: Changelog feed, directory navigation, knowledge density metrics, isolated node detection
- **Skill consolidation**: Merged 32 overlapping skills into 9 unified skills (19% redundancy reduction)

### Fixed
- `update_state.py` path sync with `check_new_files.py` (22 directories)
- TypeScript compilation errors in frontend components
- Circular dependency in graph data parser
- Vite connectivity issues with node_modules corruption

### Removed
- Legacy Gemini-specific configurations
- Duplicate skills: `brainstorm-experiments-existing/new`, `brainstorm-ideas-existing/new` → unified `brainstorm`
- Outdated OpenClaw/ZeroClaw dependencies

---

## [1.5.0] — 2026-04-07

### LLM Knowledge Engine
- `llm-wiki-compiler`: Karpathy-inspired knowledge compilation
- `obsidan`: Obsidian vault management
- Strategy skills infusion: `product-strategy`, `swot-analysis`, `startup-canvas`, `market-sizing`
- Mass sync: 120+ skills from local workspace

---

## [1.0.0] — 2026-03-24

### Initial Release
- 40+ skills covering SEO, CRO, and productivity
- Core framework: skill definitions, evals, references structure
