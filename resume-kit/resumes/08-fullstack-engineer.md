# ARYAN SHARMA
**Full-Stack Software Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Full-stack engineer who has shipped 10+ complete products solo — from Next.js frontends to FastAPI/Go/Rust backends, Postgres schemas with RLS, payment integrations (Razorpay, Stripe, PayPal), and Vercel/Render/Firebase production deploys. 6 live applications including a multi-tenant SAP SaaS, a two-sided affiliate marketplace (31k+ LOC), and a real-time multiplayer engine over 25M cells.

## TECHNICAL SKILLS
- Frontend: React 19 · Next.js 14–16 (App Router, Server Actions, RSC) · TypeScript · Tailwind CSS · shadcn/ui · Framer Motion · Astro · HTML5 Canvas
- Backend: Node.js · FastAPI (Python) · Go · Rust · Supabase/PostgreSQL · Prisma · Firebase (Firestore, Functions, Auth) · Redis · WebSockets
- Payments & Auth: Razorpay (orders, webhooks, UPI) · Stripe · PayPal · Clerk · NextAuth · Supabase Auth (SSR, RLS)
- Deployment: Vercel (Edge, Blob, KV) · Render · Firebase Hosting · GitHub Actions · Docker
- Practices: REST + webhook design · idempotency · rate limiting · unit/E2E testing · performance (95+ Lighthouse)

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

**B1 Copilot — Multi-Tenant SAP Copilot SaaS (full stack)**
- Built the full product: Next.js 16 / React 19 frontend → FastAPI backend → SAP HANA / B1 Service Layer, with streaming tables + charts + executive summaries from plain-English queries.
- Shipped 3-tier RBAC (Super Admin → Partner Admin → Client) with white-label branding, per-tenant quotas, and an Excel/CSV data-migration tool with fuzzy header mapping (difflib) and Service-Layer batch push.
- Quality bar: 40+ unit tests + 60-question E2E accuracy harness with CI scorecard; Dockerized backend; boots into a deterministic offline sandbox with zero external dependencies.
- Tech: Next.js 16, FastAPI, SAP HANA, Docker, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**Black Index — Two-Sided SaaS Affiliate Marketplace (31k+ LOC)**
- Built the full marketplace in Next.js + Supabase (RLS on every table): founder product listings with hybrid commission config, seller ("Warlord") referral-link generation, tracked attribution, earnings dashboards, and an admin console for fraud/blacklist/disputes.
- Implemented the money path end to end: HMAC-verified webhooks from 14 payment providers (Razorpay, Stripe, Gumroad, Lemon Squeezy, PayPal, Cashfree, PhonePe, PayU, Instamojo, CCAvenue, Shopify, Cal.com, +custom) → atomic record_conversion RPC (customer upsert, recurring count, idempotent insert, founder debit, seller escrow credit, platform fee) → 30-day escrow release via cron.
- Tech: Next.js, TypeScript, Supabase, Razorpay/Stripe, Zod, cron webhooks — github.com/Aryan-Protein-Vala/Black-Index

**GSTGenius — GST Invoicing & Business Suite (live)**
- Built a 26k+ LOC business suite: GST-compliant invoicing (CGST/SGST/IGST auto-computed from HSN + location), digitally signed PDF invoices, inventory integration, recurring billing via Firebase Cloud Functions, WhatsApp/email payment reminders, GSTR-1 / GSTR-3B exports, P&L + balance sheet, and a CA portal managing unlimited clients.
- Auto-reconciliation: invoices marked Paid on Razorpay/UPI gateway confirmation; live at gstgenius-6f0d0.web.app.
- Tech: Next.js 15, React 19, Firebase, Razorpay, Chart.js — github.com/Aryan-Protein-Vala/GSTGenius

**CLAIM/05 — Real-Time Multiplayer Game (live)**
- Built the full loop: Next.js 16 canvas client (5,000×5,000 grid, pan/zoom, minimap) ↔ Go WebSocket engine (hub pattern) ↔ Redis (SETNX atomic cell locks + Pub/Sub delta fan-out) with sub-millisecond sync and reload-safe reconnection; 24/7 with zero cold starts via GitHub Actions keep-alive.
- Tech: Next.js 16, Go, Gorilla WebSockets, Redis — github.com/Aryan-Protein-Vala/Grid-Game · live: multiplayer-grid-game-theta.vercel.app
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
