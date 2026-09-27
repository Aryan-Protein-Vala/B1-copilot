# ARYAN SHARMA
**LLM / Generative AI Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Generative AI engineer who ships production LLM systems end to end — agent runtimes, RAG pipelines, multi-model orchestration, and the guardrails that keep them reliable. 10+ LLM-powered systems built across Python, Rust, and TypeScript; measured 0.8 ms P50 retrieval latency in a voice RAG system and a 60-question E2E accuracy harness on an enterprise SAP copilot. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- LLM Systems: OpenAI, Anthropic (Claude), Groq, OpenRouter, Vercel AI SDK · prompt & tool design · function calling · structured outputs · streaming · token-budget & cost governance
- RAG: FAISS · hybrid graph+vector retrieval · hierarchical chunking · embeddings (TF-IDF, BGE, sqlite-vec) · citation grounding
- Agents: tool-use loops · multi-agent orchestration · background workers · deterministic routing · guardrails & jailbreak defense
- Languages: Python · Rust · TypeScript · Go · SQL
- Infra: FastAPI · WebSockets · Docker · PostgreSQL/Supabase · Redis · gRPC · Vercel/Cloudflare edge

## PROJECTS

**CORTEX — Local-First Graph-Vector AI Memory Engine (Rust)**
- Built a Rust memory core (5,700+ LOC) whose background "shadow kernel" intercepts conversations from any LLM, extracts JSON-LD triplets, and writes relationships to SurrealDB with Qdrant as the fast vector lookup — one shared memory layer across ChatGPT, Claude, Gemini, and Cursor.
- Implemented an Ebbinghaus forgetting-curve decay engine so low-salience memories are pruned and identity facts persist, collapsing context injection from 100k+ token dumps to a flat, hyper-dense packet (flat token cost).
- Shipped a Tauri desktop client with a live 3D WebGL memory graph, an MCP server for any MCP-capable host, and a gRPC (tonic) sync API.
- Tech: Rust, SurrealDB, Qdrant, Redis, Tauri, gRPC, OpenRouter, Docker — github.com/Aryan-Protein-Vala/CORTEX

**Oblivion AI — Autonomous Desktop Agent & Multi-Model Council**
- Built the agent engine (TypeScript, ~67k LOC): LLM brain with tool use and subagent orchestration, persistent sqlite-vec vector memory with hybrid search, plugin loader with hooks, and a WebSocket + HTTP gateway with session auth.
- Designed a 3-layer intent router for multi-model "council" debates — deterministic regex parser (~90% of traffic at zero LLM cost) → nano-model classifier → hard backend router — plus @mention-directed parallel model review and single-shot synthesis mode.
- Routed across 30+ providers (OpenAI, Anthropic, Gemini, Bedrock, Ollama) with tool-use policies, secret detection, and a full audit trail.
- Tech: TypeScript, Tauri v2 (Rust), sqlite-vec, WebSocket, Vercel AI SDK — github.com/Aryan-Protein-Vala/Oblivion-AI

**B1 Copilot — SAP Business One AI Copilot SaaS**
- Built a 4-tool LLM agent layer (schema search, table describe, structured query builder, guarded raw SQL) with ~80 business aliases that lets users query an entire SAP HANA ERP in plain English and get tables, charts, and executive summaries.
- Enforced model-output safety: SELECT/WITH-only SQL guard, parameter binding, auto-injected row caps, and per-table preferred-column mapping to keep prompts small.
- Validated generation quality with a 60-question end-to-end LLM accuracy harness (scorecard + CI gate) plus 40+ unit tests running with zero ERP, network, or API key required.
- Tech: Python, FastAPI, Next.js 16, React 19, SAP HANA, OpenRouter, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**VĀYU — Ultra-Low-Latency Voice RAG System**
- Built a voice-first RAG pipeline (Sarvam STT/TTS → speculative retrieval → FAISS over 9,000+ in-RAM vectors → Groq Llama 3 → TTS) answering in 0.8 ms P50 WebSocket round-trips against a 50–100 ms requirement.
- Engineered deterministic input guardrails (compiled regex, <1 ms) and an output grounding validator that rejects any claim or citation tag not present in retrieved context.
- Tech: Python, FastAPI, WebSockets, FAISS, Groq LPU, Sarvam AI, Next.js 16 — github.com/Aryan-Protein-Vala/vayu-voice-rag

**Council — Multi-Model Decision Platform**
- Built dual-mode LLM products: "God mode" (one prompt → one synthesized decision from parallel model passes) and "Council mode" (parallel frontier models with selective cross-review).
- Designed cost governance: integer-credit prepaid wallet, tier gating, and Razorpay UPI top-ups with webhook-verified ledger entries.
- Tech: Next.js 15, Vercel AI SDK, Supabase, Clerk, Razorpay — github.com/Aryan-Protein-Vala/multi-model

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Data Structures & Algorithms, Databases, Operating Systems, Computer Networks, Machine Learning, Linear Algebra & Probability
