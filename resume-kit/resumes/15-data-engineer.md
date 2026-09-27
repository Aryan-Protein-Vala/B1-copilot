# ARYAN SHARMA
**Data & Analytics Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Data engineer who builds pipelines from messy real-world sources to trustworthy answers: SAP HANA schema discovery and cataloging, Excel/CSV ingestion with fuzzy field mapping, 9,000+ vector ingestion with faceted metadata, ledger reconciliation across 14 external systems, and the testing discipline (60-question E2E accuracy harness, 40+ unit tests) that proves the data is right.

## TECHNICAL SKILLS
- Data Engineering: schema discovery & cataloging (SYS.TABLE_COLUMNS) · Excel/CSV ingestion · fuzzy field mapping (difflib) · batch ETL push with validation · dialect translation (HANA→SQLite) · metadata design (language/category/provenance facets)
- Vector & Search Data: FAISS (IndexFlatIP) · TF-IDF (512-dim) · BGE embeddings · parent-child chunking pipelines · MSMARCO-XI/SQuAD ingestion schemas · LRU caches
- Databases: PostgreSQL/Supabase (RLS, atomic RPCs) · SAP HANA SQL (joins, window functions, UNION, HAVING) · SurrealDB (graph) · Redis · sqlite-vec
- Quality: E2E accuracy harnesses · CI scorecards · idempotency keys · reconciliation & drift detection · parameterized queries
- Languages: Python (pandas, NumPy, sklearn) · TypeScript · Go · Rust · SQL

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

**B1 Copilot — ERP Data Layer (SAP HANA)**
- Built the schema-discovery pipeline: index and search table names, table comments, column names, and column comments across an entire SAP HANA company schema (SYS.TABLE_COLUMNS), plus friendly-name resolution (~80 aliases) and status-code translation — the semantic layer that makes raw ERP tables queryable.
- Built the ingestion/migration pipeline: Excel/CSV upload → difflib fuzzy mapping of irregular client headers ("Vendor Name" → CardName) → validation against the B1 Service Layer → batch push, with progress tracking and per-tenant scoping.
- Built the governance layer: parameterized query builder (10 filter operators, 6 aggregates), auto-injected row caps, dialect translation (HANA→SQLite) powering a deterministic offline sandbox, and 40+ tests asserting data behavior ("unknown column rejected with suggestion", "decimal/date/bytes JSON-safe", "char padding stripped").
- Validated end to end with a 60-question accuracy harness executed against sandbox data and scored into a CI gate.
- Tech: Python, FastAPI, SAP HANA, OData, difflib, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**VĀYU — Vector Data Pipeline (9,000+ Vectors)**
- Built the ingestion pipeline: multi-strategy chunking (parent-child hierarchy, 1-sentence overlap, semantic-then-fixed-size hybrid), metadata enrichment (Language | Category | ID | Title | Content) for faceted retrieval, and MSMARCO-XI-ready schemas (query/passage/is_selected) with SQuAD offline fallback.
- Built the serving path: 9,000+ vectors embedded (512-dim TF-IDF, BGE swap-in path) into in-RAM FAISS with an LRU similarity cache (<0.2 ms) — measured 0.017 ms search, 0.67 ms P50 full retrieval.
- Tech: Python, FAISS, sklearn, FastAPI — github.com/Aryan-Protein-Vala/vayu-voice-rag

**Black Index — Cross-System Ledger Reconciliation**
- Built the reconciliation data path for a marketplace: 14 external provider webhook streams normalized into one processor, idempotent transaction IDs, atomic ledger updates (founder debit / seller escrow credit / platform fee), and cron jobs (reconcile, wallet-check, dispute SLA) that detect drift between provider records and the canonical ledger.
- Tech: Next.js, Supabase/Postgres, Razorpay/Stripe — github.com/Aryan-Protein-Vala/Black-Index

**GSTGenius — Financial Data & Reporting (live)**
- Built the analytics pipeline: transactional ledgers → real-time P&L, balance sheet, and revenue trend computation; HSN + location → CGST/SGST/IGST; GSTR-1 / GSTR-3B report generation in CSV/Excel; auto-reconciliation marking invoices Paid on gateway events — live at gstgenius-6f0d0.web.app.
- Tech: Next.js 15, Firebase, Chart.js — github.com/Aryan-Protein-Vala/GSTGenius
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
