# ARYAN SHARMA
**AI Infrastructure & MLOps Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
AI infrastructure engineer who builds the plumbing LLM products run on — Rust memory cores behind Docker Compose stacks, edge proxies that keep model keys off the client, multi-provider LLM routers across 30+ vendors, deterministic offline sandboxes that let LLM CI run with zero network or API cost, and cost-governed wallet systems for prepaid AI credits. a deterministic offline SAP sandbox that runs LLM CI with zero network or API cost (40+ unit tests + 60-question accuracy harness, all CI-gated).

## TECHNICAL SKILLS
- AI Infra: multi-provider LLM routing (30+ providers) · OpenRouter/Anthropic/OpenAI/Bedrock/Groq adapters · token budgets & cost governance · streaming · BYOK vs managed-key architectures
- Serving & Edge: Cloudflare Workers edge proxies · Vercel serverless · FastAPI/Uvicorn · gRPC (tonic) · WebSockets · Docker & Docker Compose · GitHub Actions CI
- Models & Data: FAISS in-RAM vector stores · sqlite-vec · embeddings pipelines · deterministic offline simulators/sandboxes for LLM apps · telemetry & benchmarking
- Languages: Rust · Python · TypeScript · Go · SQL · Linux, bash
- Observability: per-stage latency telemetry · P50/P70/P100 tracking · benchmark harnesses · audit logging

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

**MYLO OS — Managed-Tier AI Platform (Edge + Desktop)**
- Built the Cloudflare edge proxy that makes a managed AI tier secure: license keys validated at the edge, Anthropic master API keys injected server-side per request — client-side key theft is structurally impossible.
- Designed a 3-tier pricing architecture (BYOK Free → $14.99 Pro → $49.99 Elite) with model gating (Claude Sonnet 4.5 / Haiku 4.5), token budgets, and tier-gated feature access enforced in Rust on the desktop side.
- Tech: Rust, Tauri 2, Cloudflare Workers, Wrangler, Next.js — github.com/Aryan-Protein-Vala/MyloOS

**CORTEX — Rust Memory Core as AI Infra (Docker Compose)**
- Built and containerized a Rust memory service (axum + gRPC/tonic + SurrealDB + Qdrant + Redis) deployed via Docker Compose — the shared "memory database" that any AI client reads/writes, with O(1) injection endpoints and decay cron inside the engine.
- Profiled the hot path to keep memory injection flat-cost and sub-millisecond at the index layer (Qdrant as lookup pre-filter into the SurrealDB graph).
- Tech: Rust, axum, tonic/prost, SurrealDB, Qdrant, Redis, Docker Compose — github.com/Aryan-Protein-Vala/CORTEX

**Oblivion AI — Multi-Provider LLM Gateway**
- Built the LLM router and gateway: 30+ provider adapters (OpenAI, Anthropic, Gemini, Bedrock, Ollama) behind one interface, WebSocket + HTTP gateway with session auth, plugin loader with hooks, and config system (YAML + env resolution).
- Implemented the 3-layer routing stack that cuts LLM spend — deterministic parser (~90% of traffic, zero cost) → nano-model classifier → hard router — with per-tier cost governance and an integer-credit wallet ledger.
- Tech: TypeScript, Vercel AI SDK, Supabase, Clerk, Razorpay — github.com/Aryan-Protein-Vala/Oblivion-AI · github.com/Aryan-Protein-Vala/multi-model

**B1 Copilot — Deterministic Offline Sandbox for LLM CI**
- Built a deterministic offline SAP B1 sandbox with a deterministic SQL planner so the entire LLM app boots, serves, and is tested with no HANA server, no LLM key, and no network — responses clearly labelled SIMULATED; this is what lets 40+ unit tests and the 60-question accuracy harness run in CI in seconds.
- Added a data-source auto-fallback chain (HANA → Service Layer → sandbox) and Dockerized the backend for one-command deployment.
- Tech: Python, FastAPI, Docker, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
