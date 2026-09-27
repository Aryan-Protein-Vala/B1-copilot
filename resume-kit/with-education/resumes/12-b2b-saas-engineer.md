# ARYAN SHARMA
**B2B SaaS Product Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
B2B SaaS engineer who builds the unglamorous middle of enterprise products — multi-tenant RBAC, white-labeling, tiered plans, per-tenant quotas, admin consoles, data migration, and compliance-grade reporting — on top of impressive user-facing AI. Shipped a white-labeled SAP Business One copilot SaaS with 3 admin tiers, a GST compliance suite for CAs, and an enterprise fleet product. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- SaaS Architecture: multi-tenancy (tenant-scoped RBAC, per-tenant quotas & feature flags) · white-label theming · tiered plans (Pilot/Read-Only/Read-Write/Migration) · partner/reseller models · admin consoles
- Enterprise: SAP Business One (HANA, OData Service Layer) · data migration & fuzzy field mapping · audit trails · read-only technical users · guarded SQL
- Compliance & Reporting: GST (CGST/SGST/IGST, HSN codes) · GSTR-1/3B exports · P&L/balance sheet · signed PDFs
- Product: Next.js/React · FastAPI · Supabase (RLS, cron) · Razorpay/Stripe (B2B billing, security deposits) · Docker · Vercel/Render
- Languages: TypeScript · Python · Go · SQL

## PROJECTS

**B1 Copilot — White-Label Multi-Tenant SAP Copilot SaaS**
- Upgraded an AI analytics copilot into a tiered B2B SaaS: Super Admin provisions Reseller Partners (plans: Pilot, Read Only, Read/Write Full, Migration), sets tenant quotas, and manages white-label brand names; Partner Admins connect and manage their clients' SAP B1 databases with per-tenant write_enabled toggles; End Users get the chat copilot.
- Built the partner data-migration tool: Excel/CSV upload → difflib fuzzy header mapping (irregular client headers like "Vendor Name" → strict SAP fields like CardName) → validation against the B1 Service Layer → batch push — the boring step that makes enterprise onboarding possible.
- Safety architecture for enterprise data: read-only technical HANA user, SELECT-only guarded SQL with parameter binding and row caps, per-employee session scoping, tampered/expired token rejection; 40+ unit tests + 60-question E2E accuracy harness with CI scorecard.
- Tech: FastAPI, Next.js 16, SAP HANA, OData, Docker — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**GSTGenius — Compliance SaaS for Indian Businesses & CAs (live)**
- Built the CA-facing product: a dedicated portal where one Chartered Accountant manages unlimited clients with shared access, while each client self-serves invoicing, inventory, and compliance reports.
- Shipped the compliance surface: GST-compliant invoicing (CGST/SGST/IGST from HSN + location), one-click GSTR-1 / GSTR-3B exports, real-time P&L and balance sheets, recurring billing with automated dunning, and gateway auto-reconciliation; live at gstgenius-6f0d0.web.app.
- Tech: Next.js 15, Firebase, Razorpay — github.com/Aryan-Protein-Vala/GSTGenius

**Black Index — Founder-Side B2B Marketplace Platform**
- Built the SaaS vendor side of a distribution marketplace: product listings with hybrid commission config (upfront % + recurring % + max months), payment/webhook integration setup per provider, featured-listing payments, security deposits, and a founder dashboard with analytics, wallet, and product management.
- Tech: Next.js, Supabase, Razorpay/Stripe — github.com/Aryan-Protein-Vala/Black-Index

**Prometheus — Enterprise Fleet Security Product (live)**
- Built a B2B-distributable OS cleaner: 100% offline Rust TUI (zero telemetry as the selling point), HWID-bound license keys to prevent license burnout, a centralized Enterprise Fleet Command Center for organizational management, and a one-line curl installer across macOS/Linux — live at prometheus-cleaner.vercel.app.
- Tech: Rust, TUI, Next.js, GitHub Actions — github.com/Aryan-Protein-Vala/Prometheus

**B1 Copilot (continued) — Migration & Diagnostics Ops Surfaces**
- Built partner ops surfaces: SAP connectivity diagnostics endpoints, migration progress tracking, and per-tenant connection health — the "does it work in the customer's environment" layer that determines enterprise renewal.
- Tech: FastAPI, SAP B1 Service Layer — github.com/Aryan-Protein-Vala/Cira-RAG-agent

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Databases, Data Structures & Algorithms, Operating Systems, Computer Networks
