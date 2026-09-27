# ARYAN SHARMA
**RAG & AI Search Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
RAG and AI search specialist who has shipped retrieval pipelines where every millisecond is measured. Built a voice RAG system answering in 0.8 ms P50 retrieval (99% under its latency budget), an enterprise SAP copilot with a 60-question E2E accuracy harness, and a 1,300+-product RAG recommendation engine. Deep in chunking strategy, hybrid vector+graph retrieval, grounding, and hallucination defense.

## TECHNICAL SKILLS
- Retrieval: FAISS (IndexFlatIP/IVF) · hybrid vector+graph search · parent-child hierarchical chunking · overlapping semantic splits · LRU query caches · speculative/pre-fetch retrieval
- Embeddings: TF-IDF (sklearn) · BGE-small · sqlite-vec · semantic vs fixed-size chunking · metadata faceting
- Grounding & Quality: citation validation · hallucination defense · deterministic guardrails · E2E accuracy harnesses · RAGAS-style evaluation
- Data: PostgreSQL/Supabase · SurrealDB (graph) · Qdrant · Redis · Parquet · Excel/CSV ingestion & fuzzy schema mapping
- Languages: Python · TypeScript · Rust · Go · SQL

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

**VĀYU — Ultra-Low-Latency Voice RAG System**
- Engineered a complete RAG pipeline with per-stage telemetry: compiled-regex guardrails 0.005 ms → 512-dim TF-IDF embedding 0.51 ms → FAISS IndexFlatIP over 9,000+ in-RAM vectors 0.017 ms → O(1) parent-chunk lookup 0.009 ms → citation-grounding validator 0.005 ms (0.67 ms P50 total retrieval).
- Designed the chunking strategy: parent-child hierarchy (full passages as parents, 1–2 sentence children) with 1-sentence overlap and semantic-then-fixed-size hybrid splitting, so no concept is orphaned at a boundary; every child carries language/category/provenance metadata for faceted retrieval.
- Added a sub-0.2 ms LRU cache for repeated/similar queries and speculative retrieval triggered by live speech partials — candidates are in RAM before the user finishes the sentence.
- Tech: Python, FastAPI, WebSockets, FAISS, sklearn, Groq LPU, Sarvam AI — github.com/Aryan-Protein-Vala/vayu-voice-rag

**B1 Copilot — SAP Business One AI Copilot SaaS**
- Built retrieval over an entire ERP schema: `sap_search_schema` indexes table names, comments, column names, and column comments (SYS.TABLE_COLUMNS) so the agent finds fields it was never told about; friendly-name resolution maps ~80 business terms (invoices→OINV, vendors→OCRD) with status-word → B1 code translation in both directions.
- Added a policy RAG side-channel that searches real policy documents (travel, finance, data security, procurement) and grounds answers with citations; guarded SQL layer (SELECT/WITH-only, parameter-bound, row-capped) as the structured-retrieval fallback.
- Tech: Python, FastAPI, SAP HANA SQL, Next.js 16, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**CORTEX — Graph-Vector Hybrid Memory Engine (Rust)**
- Built a local-first memory store using graph (SurrealDB) + vector (Qdrant) hybrid indexing: relationship triples for structural recall, embeddings for semantic lookup, with the vector index acting as a fast pre-filter into the graph.
- Tech: Rust, SurrealDB, Qdrant, Redis, gRPC — github.com/Aryan-Protein-Vala/CORTEX

**DermaOS — AI Skin Analysis & Product RAG Marketplace**
- Built the RAG recommendation head ranking 1,300+ catalog products against a 6-dimension skin profile by skin type, concern, and ingredient compatibility, with a personalized grade per product card.
- Tech: Next.js 16, TypeScript, Supabase, Prisma, OpenRouter (GPT-4o-mini) — github.com/Aryan-Protein-Vala/DermaOS · live: dermaos.vercel.app
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
