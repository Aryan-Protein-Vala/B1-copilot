# ARYAN SHARMA
**Backend Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Backend engineer who owns systems from schema to production: FastAPI and Go services, Postgres schemas with row-level security, atomic multi-tenant money ledgers, webhook verification at scale, cron-driven settlement pipelines, and WebSocket engines with sub-millisecond fan-out. Production systems handling 5,000+ monthly transactions; 96% WebSocket latency reduction from a single root-caused fix.

## TECHNICAL SKILLS
- APIs: FastAPI · Node.js/Next.js route handlers · Go (HTTP, Gorilla WebSockets) · gRPC (tonic) · REST + webhook design · OpenAPI
- Data: PostgreSQL (Supabase) · RLS policies · atomic RPCs · idempotency keys · Prisma · Redis (KV, Pub/Sub, SETNX) · HANA SQL · SurrealDB · Qdrant · FAISS
- Payments & Billing: Razorpay (orders, webhooks, RazorpayX/UPI payouts) · Stripe · PayPal · escrow/settlement models · reconciliation
- Services: cron/webhook jobs · authN/Z (JWT, Clerk, NextAuth, Supabase Auth) · rate limiting · signing & HMAC verification
- Languages: Python · Go · Rust · TypeScript · SQL · Docker, GitHub Actions

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

**Black Index — Money Path for a Two-Sided Marketplace**
- Built the backend core of a 31k-LOC affiliate marketplace: HMAC-verified webhook ingestion from 14 payment providers (Razorpay, Stripe, Gumroad, Lemon Squeezy, PayPal, Cashfree, PhonePe, PayU, Instamojo, CCAvenue, Shopify, Cal.com, +custom) feeding an atomic record_conversion RPC — customer upsert, recurring-billing count, idempotent transaction insert, founder wallet debit, seller escrow credit, and platform-fee accounting in a single transaction.
- Tech: Next.js API routes, Supabase/Postgres, Razorpay/Stripe, Zod — github.com/Aryan-Protein-Vala/Black-Index

**B1 Copilot — Enterprise Analytics API (SAP)**
- Built the FastAPI backend for a natural-language SAP copilot: 4-tool agent layer (schema search over table/column comments, table describe, structured query builder with 10 filter operators + aggregates, guarded raw SQL), streaming responses interleaving tables/charts/summaries, and an auto-fallback data source chain (HANA → B1 Service Layer → offline sandbox).
- Tech: Python, FastAPI, SAP HANA, OData, Docker, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**CLAIM/05 — Go WebSocket Engine for 25M-Cell Real-Time State**
- Built the state engine in Go: Gorilla WebSocket hub with concurrent channel hubs, Redis SETNX as the atomic cell lock (two players can never win the same cell), and Pub/Sub delta fan-out reaching all connected clients in sub-millisecond; persistent player tokens for reload-safe reconnection.
- Tech: Go, Gorilla WebSockets, Redis, Render, GitHub Actions — github.com/Aryan-Protein-Vala/Grid-Game · live: multiplayer-grid-game-theta.vercel.app

**GSTGenius — Serverless Billing & Compliance Backend**
- Built the Firebase Cloud Functions backend: recurring invoices (daily/weekly/monthly), automated WhatsApp + email payment reminders, GST tax computation (CGST/SGST/IGST from HSN + location), GSTR-1/GSTR-3B report generation, and gateway auto-reconciliation marking invoices Paid on confirmation.
- Tech: Firebase (Firestore, Functions, Auth), Razorpay, Node.js — github.com/Aryan-Protein-Vala/GSTGenius

## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
