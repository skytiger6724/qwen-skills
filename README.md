# 🧠 Qwen Skills — AI Agent Skill Collection

> **155 specialized skills** that turn Qwen Code into a multi-disciplinary expert team.

A comprehensive collection of AI agent skills covering marketing, product management, development, design, data analysis, and business strategy. Inspired by Karpathy's LLM Wiki philosophy — persistent, compounding knowledge that gets smarter with every interaction.

![Skills](https://img.shields.io/badge/Skills-155-blue.svg)
![Files](https://img.shields.io/badge/Files-492-green.svg)
![Lines](https://img.shields.io/badge/Lines-124K-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## Why This Exists

Most AI agents redis knowledge from scratch on every task. This collection takes a different approach: each skill is a self-contained expert that brings its own framework, templates, references, and evaluation criteria. They don't just answer — they execute structured workflows with measurable outcomes.

Think of it as a team of 155 specialists, each with their own playbook, ready to deploy on demand.

---

## 📂 Skill Categories

### 📈 Marketing & Growth (25 skills)
SEO, content strategy, paid ads, email marketing, CRO, and conversion optimization.
- `seo-audit` — Technical SEO health check
- `ai-seo` — Optimize for AI search engines (AEO/LLMO)
- `programmatic-seo` — Scale SEO with data-driven pages
- `cold-email` — B2B cold outreach sequences
- `onboarding-cro` / `signup-flow-cro` / `paywall-upgrade-cro` — Conversion rate optimization
- `churn-prevention` — Retention and save offers

### 🛠️ Product Management (20 skills)
PRD creation, user research, prioritization, roadmaps, and strategy.
- `create-prd` — Product Requirements Documents
- `user-stories` / `job-stories` / `wwas` — Backitem formats
- `prioritize-features` — Impact/effort/risk scoring
- `product-strategy` — 9-section strategy canvas
- `north-star-metric` — Define and validate your North Star
- `brainstorm` — Multi-perspective ideation

### 💻 Development (15 skills)
Code review, testing, debugging, and Git workflows.
- `review` — Code review with correctness/security/performance checks
- `systematic-debugging` — Root cause analysis framework
- `test-driven-development` — TDD methodology
- `using-git-worktrees` — Isolated Git worktrees
- `finishing-a-development-branch` — PR/merge completion workflow

### 🎨 Design & Presentations (10 skills)
PPT templates, PDF/XLSX processing, document generation.
- `pptx` — Professional slide deck creation
- `pdf` — PDF manipulation (merge, extract, fill forms, OCR)
- `xlsx` — Spreadsheet automation with formulas and charts
- `docx` — Word document generation
- `ppt-generator-pro` — AI-generated PPT with images/video

### 📊 Data & Analytics (10 skills)
Cohort analysis, sentiment, dashboards, and SQL.
- `cohort-analysis` — User retention by cohort
- `sentiment-analysis` — Feedback sentiment scoring
- `metrics-dashboard` — Product metrics definition
- `sql-queries` — Natural language → SQL
- `data-visualization` — Insight-driven chart generation

### 🤖 AI & LLM (8 skills)
Wiki compilation, knowledge management, and AI optimization.
- `llm-wiki-compiler` — Automated knowledge ingestion (Karpathy pattern)
- `ai-seo` — AI search engine optimization
- `zeroapi` — Intelligent model routing (Gemini/GPT/Claude)
- `context-compression` — Fit within token limits

### 💼 Business & Strategy (15 skills)
Competitive analysis, pricing, monetization, and growth.
- `competitive-analysis` — Strengths/weaknesses mapping
- `pricing-strategy` — Tier structure and willingness-to-pay
- `monetization-strategy` — Revenue model brainstorming
- `growth-loops` — Viral/usage/collaboration loops
- `gtm-strategy` — Go-to-market planning

### 📝 Communication & Writing (12 skills)
Copywriting, editing, internal comms, and meeting summaries.
- `copywriting` — Marketing copy for any page
- `humanizer` — De-AI-fy text, inject personality
- `summarize-meeting` / `summarize-interview` — Structured summaries
- `internal-comms` — Status reports, newsletters, FAQs

### 🔧 Specialized (40+ skills)
Niche tools for specific domains and workflows.
- `career-ops` — AI-powered job search command center
- `pua` — High-agency problem solver (pressure mode)
- `notebooklm` — Google NotebookLM integration
- `gog` — Google Workspace automation
- `revops` — Revenue operations and lead lifecycle

---

## 🚀 Quick Start

### Install as Local Skills
```bash
# Clone to your agent skills directory
git clone https://github.com/skytiger6724/qwen-skills.git ~/.qwen/skills

# Skills auto-load on next Qwen Code session
```

### Use Individual Skills
Reference skills by name in your prompts:
```
Use the seo-audit skill to analyze my site.
Use the create-prd skill to write a PRD for feature X.
```

---

## 📊 Stats

| Metric | Value |
|:------:|:-----:|
| Total Skills | 155 |
| Source Files | 492 |
| Code Lines | 124,184 |
| Categories | 8 |
| With References | 60+ |
| With Evals | 30+ |

---

## 🏗️ Structure

Each skill follows a consistent layout:
```
skill-name/
├── SKILL.md              # Core skill definition + trigger words
├── evals/                # Evaluation test cases (optional)
│   └── evals.json
└── references/           # Playbooks, templates, examples (optional)
    └── *.md
```

---

## 📄 License
MIT. *Built from real-world usage, not theoretical design.*
