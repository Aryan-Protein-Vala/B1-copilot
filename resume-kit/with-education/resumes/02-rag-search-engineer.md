# ARYAN SHARMA
**RAG & AI Search Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
RAG and AI search specialist who has shipped retrieval pipelines where every millisecond is measured. Built a voice RAG system answering in 0.8 ms P50 retrieval (99% under its latency budget), an enterprise SAP copilot with a 60-question E2E accuracy harness, and a 1,300+-product RAG recommendation engine. Deep in chunking strategy, hybrid vector+graph retrieval, grounding, and hallucination defense. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Retrieval: FAISS (IndexFlatIP/IVF) · hybrid vector+graph search · parent-child hierarchical chunking · overlapping semantic splits · LRU query caches · speculative/pre-fetch retrieval
- Embeddings: TF-IDF (sklearn) · BGE-small · sqlite-vec · semantic vs fixed-size chunking · metadata faceting
- Grounding & Quality: citation validation · hallucination defense · deterministic guardrails · E2E accuracy harnesses · RAGAS-style evaluation
- Data: PostgreSQL/Supabase · SurrealDB (graph) · Qdrant · Redis · Parquet · Excel/CSV ingestion & fuzzy schema mapping
- Languages: Python · TypeScript · Rust · Go · SQL

## PROJECTS

**VĀYU — Ultra-Low-Latency Voice RAG System**
- Engineered a complete RAG pipeline with per-stage telemetry: compiled-regex guardrails 0.005 ms → 512-dim TF-IDF embedding 0.51 ms → FAISS IndexFlatIP over 9,000+ in-RAM vectors 0.017 ms → O(1) parent-chunk lookup 0.009 ms → citation-grounding validator 0.005 ms (0.67 ms P50 total retrieval).
- Designed the chunking strategy: parent-child hierarchy (full passages as parents, 1–2 sentence children) with 1-sentence overlap and semantic-then-fixed-size hybrid splitting, so no concept is orphaned at a boundary; every child carries language/category/provenance metadata for faceted retrieval.
- Added a sub-0.2 ms LRU cache for repeated/similar queries and speculative retrieval triggered by live speech partials — candidates are in RAM before the user finishes the sentence.
- Built the ingestion pipeline for MSMARCO-XI (query/passage/answer-tagged schema) with SQuAD fallback; measured end-to-end P50 0.8 ms WebSocket round-trips vs a 50–100 ms requirement.
- Tech: Python, FastAPI, WebSockets, FAISS, sklearn, Groq LPU, Sarvam AI — github.com/Aryan-Protein-Vala/vayu-voice-rag

**B1 Copilot — SAP Business One AI Copilot SaaS**
- Built retrieval over an entire ERP schema: `sap_search_schema` indexes table names, comments, column names, and column comments (SYS.TABLE_COLUMNS) so the agent finds fields it was never told about; friendly-name resolution maps ~80 business terms (invoices→OINV, vendors→OCRD) with status-word → B1 code translation in both directions.
- Added a policy RAG side-channel that searches real policy documents (travel, finance, data security, procurement) and grounds answers with citations; guarded SQL layer (SELECT/WITH-only, parameter-bound, row-capped) as the structured-retrieval fallback.
- Verified retrieval + generation quality with a 60-question E2E accuracy harness and 40+ unit tests, including "schema search finds columns anywhere", "unknown column rejected with suggestion", and "row cap is enforced" gates.
- Tech: Python, FastAPI, SAP HANA SQL, Next.js 16, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**CORTEX — Graph-Vector Hybrid Memory Engine (Rust)**
- Built a local-first memory store using graph (SurrealDB) + vector (Qdrant) hybrid indexing: relationship triples for structural recall, embeddings for semantic lookup, with the vector index acting as a fast pre-filter into the graph.
- Implemented Ebbinghaus decay at the index layer — decay scores drive pruning so retrieval quality improves over time instead of degrading under stale documents.
- Tech: Rust, SurrealDB, Qdrant, Redis, gRPC — github.com/Aryan-Protein-Vala/CORTEX

**DermaOS — AI Skin Analysis & Product RAG Marketplace**
- Built a RAG recommendation engine ranking 1,300+ catalog products against a user's 6-dimension skin profile (oiliness, hydration, acne, texture, elasticity, pigmentation) by skin type, concern, and ingredient compatibility — with a personalized grade per product.
- Tech: Next.js 16, TypeScript, Supabase, Prisma, OpenRouter (GPT-4o-mini) — github.com/Aryan-Protein-Vala/DermaOS · live: dermaos.vercel.app

**CommentLysis — Creator Intelligence Platform**
- Built a retrieval + LLM pipeline over YouTube/Instagram comment corpora: sentiment classification, question extraction and categorization, and content-idea generation grounded in extracted viewer questions; 3 exportable PDF report types.
- Tech: Next.js 15, Firebase, GPT-4o, Chrome Extension — github.com/Aryan-Protein-Vala/CommentLysis

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Data Structures & Algorithms, Databases, Machine Learning, Operating Systems, Linear Algebra & Probability
