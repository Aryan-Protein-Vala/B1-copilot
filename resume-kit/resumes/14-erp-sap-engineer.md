# ARYAN SHARMA
**Enterprise ERP & SAP Integration Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
ERP integration engineer who has built production software directly on SAP Business One — HANA SQL at full depth (joins, window functions, UNION, HAVING), the OData Service Layer, schema discovery across tables/views/user fields, and the business-semantic layer that turns "invoices" into OINV and "Open" into 'O'. Shipped a multi-tenant, white-labeled SAP copilot SaaS with migration tooling, compliance-grade guarded SQL, and a 60-question E2E accuracy harness.

## TECHNICAL SKILLS
- SAP: SAP Business One · SAP HANA (SQL, system ports, tenant schemas, SYS.TABLE_COLUMNS metadata) · B1 Service Layer (OData) · company-schema objects (OINV/ORDR/RDR1/OCRD/JDT1, @user tables, U_ fields) · read-only technical users
- Data Engineering: schema discovery & cataloging · fuzzy field mapping (difflib) · Excel/CSV ingestion · batch push with validation · row-cap governance · dialect translation (HANA→SQLite for sandboxing)
- Safety: guarded SQL (SELECT-only, parameter binding, identifier allowlists, DDL/DML/CALL rejection) · RBAC (3-tier) · audit · per-tenant scoping
- Compliance Data: GST tax logic (HSN-based CGST/SGST/IGST) · GSTR-1/3B · financial statement computation (P&L, balance sheet)
- Languages: Python (FastAPI) · TypeScript (Next.js) · SQL · Go · Rust

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

**B1 Copilot — Natural-Language SAP Business One Copilot (multi-tenant SaaS)**
- Built the full-depth SAP access layer: 4 tools reaching any table, view, user table (@…), or user field (U_…) in a company schema — schema search across table/column names AND comments (SYS.TABLE_COLUMNS), table describe with row counts + samples, a structured query builder (10 filter operators, group_by, 6 aggregates, date windows), and guarded raw SQL for joins/sub-queries/window functions/UNION/HAVING.
- Encoded the B1 business-semantic layer as data: ~80 friendly-name aliases (invoices→OINV, vendors→OCRD, journal lines→JDT1), status-word ↔ B1 code translation on the way in and out (Open → 'O', vendor → 'S'), per-table preferred columns so 150-column headers don't drown the UI, and known date/amount/party column typing for automatic charting.
- Hardened for enterprise: single-statement SELECT/WITH-only guard with DDL/DML/CALL rejection even inside sub-queries, live-catalog identifier validation, parameter-bound values, auto-injected row caps (default 500, max 10,000), and a data-source auto-fallback chain (HANA → Service Layer → deterministic offline sandbox labelled SIMULATED).
- Wrapped it as a tiered white-label SaaS: Super Admin → Partner Admin → Client with per-tenant write enablement, plus a partner data-migration tool (Excel/CSV → difflib fuzzy mapping of irregular headers to strict SAP fields → Service-Layer batch push with validation).
- Verified with 40+ network-free unit tests (including "unknown column rejected with suggestion", "row cap enforced", "HANA→SQLite translation") and a 60-question E2E accuracy harness with CI scorecard.
- Tech: Python, FastAPI, SAP HANA, B1 Service Layer/OData, Next.js 16, Docker, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**GSTGenius — Regulatory Data & Compliance Reporting (live)**
- Built the compliance data layer for Indian tax: HSN-code + location-driven CGST/SGST/IGST computation, GST-compliant signed PDF invoices, and one-click GSTR-1 / GSTR-3B report generation from transactional ledgers; real-time P&L, balance sheet, and revenue trend computation; CA portal with unlimited-client shared access — live at gstgenius-6f0d0.web.app.
- Tech: Next.js 15, Firebase, Razorpay, jsPDF — github.com/Aryan-Protein-Vala/GSTGenius

**Black Index — Multi-System Reconciliation Engine**
- Built the integration + reconciliation pattern every ERP environment needs: 14 external provider webhook adapters normalized into one conversion processor, idempotent external transaction IDs, cron reconciliation against canonical records, and wallet/ledger drift detection — the same pattern as ERP↔bank reconciliation.
- Tech: Next.js, Supabase/Postgres, Razorpay/Stripe — github.com/Aryan-Protein-Vala/Black-Index
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
