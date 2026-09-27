# ARYAN SHARMA
**AI Agent Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
AI agent engineer building autonomous systems that act, not just answer — desktop agents that operate an OS with a ghost cursor, multi-agent orchestrators, background headless-browser workers, and swarm-based execution engines. Shipped 6+ agent systems in Rust, TypeScript, and Python with real tool-use, persistent memory, security policies, and measured reliability (60-question E2E harness, 40+ unit tests).

## TECHNICAL SKILLS
- Agent Design: tool-use/function calling · subagent orchestration · multi-agent debate (council patterns) · planner-executor loops · background worker pools · long-task session management
- Autonomy: screen understanding (WGC/Core Graphics) · input injection · headless browser control · file-system & git-repo awareness · global hotkey triggers
- Memory: sqlite-vec vector stores · graph+vector hybrid (SurrealDB/Qdrant) · Ebbinghaus decay · JSON-LD triple extraction
- Safety: tool-use policies · secret detection · audit logs · deterministic guardrails · scoped execution · license/tier gating
- Languages: Rust · TypeScript · Python · Go · SQL · Infra: Tauri, FastAPI, WebSockets, Docker, PostgreSQL/Supabase, Cloudflare

## EXPERIENCE
**Cinntra Infotech — Systems Engineer** · 2026 – Present
- Built CIRA, a RAG agent translating natural-language requests into audited SAP HANA queries and write operations, giving non-technical users direct access to enterprise data
- Built the point-of-sale system backend: transaction recording, merchant reconciliation, and offline synchronization

**Niswa Engineering — Technical Consultant & Automation Engineer** · 2024 – 2026
- Built asynchronous AI agents (TypeScript) that automated 80%+ of a content generation and scheduling pipeline
- Built the company website in Astro (95+ Google Lighthouse score); set up cloud infrastructure, API integrations, and event-driven automation workflows

**Sudarshana Foundation — Full-Stack & Automation Engineer** · Contract
- Designed and built the organization's first centralized web platform, digitizing paper-based workflows into software
- Built database systems handling 5,000+ monthly transactions

## PROJECTS

**MYLO OS — Autonomous Desktop AI Operator (Tauri 2 / Rust)**
- Built a Tauri 2 + Rust desktop agent that takes a spoken task and executes it on the live OS with a ghost cursor — overlaying a transparent control layer above any app (IDE, Blender, Excel) via zero-latency Windows Graphics Capture + macOS Core Graphics at ~35 MB RSS.
- Wrote the autonomy stack as custom Rust plugins: global hotkeys, screen capture, human-paced input injection, secure credential storage, PII masking, and tier gating; OS-level stealth mode (WDA_EXCLUDEFROMCAPTURE / NSWindow sharingType) hides the overlay from screen share and recording.
- Built the background-agent orchestrator: headless Chrome worker pool for long tasks (scraping 200+ competitors, content posting, lead pulls) that runs quietly and pings on completion.
- Tech: Rust, Tauri 2, Windows Graphics Capture, Core Graphics, Cloudflare Workers, Headless Chrome, Claude — github.com/Aryan-Protein-Vala/MyloOS · mylo-frontend.vercel.app

**Oblivion AI — Autonomous Desktop Agent Platform**
- Built the engine (TypeScript, ~67k LOC): agent brain with tool use and subagent orchestration, persistent structured project memory (goals, sprints, tech stack) in sqlite-vec with hybrid search, file-system/git watching, and a plugin loader with hooks.
- Designed multi-model council orchestration — parallel frontier models with @mention-directed cross-review — behind a 3-layer intent router (deterministic regex parser handling ~90% of traffic at zero LLM cost → nano-model classifier → hard router).
- Tech: TypeScript, Tauri v2 (Rust), sqlite-vec, WebSocket, React — github.com/Aryan-Protein-Vala/Oblivion-AI

**GhostStrike — Autonomous CTEM / Red-Team Swarm Engine (Rust)**
- Built a swarm orchestrator on MPSC channels with high/low-priority execution pools that plans and executes attack chains at machine speed: recon → exploitation → lateral-trust mapping, all gated by a hard authorization/scope check.
- Tech: Rust, MPSC concurrency, Parquet/mmap, CTEM — github.com/Aryan-Protein-Vala/GhostStrike (demo; full engine licensed privately)

**B1 Copilot — SAP Business One AI Copilot SaaS**
- Built an agent with 4 data tools (schema search, table describe, structured query builder, guarded SQL) that plans and executes multi-step ERP analytics in plain English — including joins and window functions — then renders tables, charts, and a two-line executive summary.
- Tech: Python, FastAPI, Next.js 16, SAP HANA, OpenRouter — github.com/Aryan-Protein-Vala/Cira-RAG-agent
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
