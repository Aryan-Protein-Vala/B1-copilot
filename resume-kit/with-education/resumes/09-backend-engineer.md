# ARYAN SHARMA
**Backend Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Backend engineer who owns systems from schema to production: FastAPI and Go services, Postgres schemas with row-level security, atomic multi-tenant money ledgers, webhook verification at scale, cron-driven settlement pipelines, and WebSocket engines with sub-millisecond fan-out. 5,000+ concurrent AI requests served across self-hosted systems; 96% WebSocket latency reduction from a single root-caused fix. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- APIs: FastAPI · Node.js/Next.js route handlers · Go (HTTP, Gorilla WebSockets) · gRPC (tonic) · REST + webhook design · OpenAPI
- Data: PostgreSQL (Supabase) · RLS policies · atomic RPCs · idempotency keys · Prisma · Redis (KV, Pub/Sub, SETNX) · HANA SQL · SurrealDB · Qdrant · FAISS
- Payments & Billing: Razorpay (orders, webhooks, RazorpayX/UPI payouts) · Stripe · PayPal · escrow/settlement models · reconciliation
- Services: cron/webhook jobs · authN/Z (JWT, Clerk, NextAuth, Supabase Auth) · rate limiting · signing & HMAC verification
- Languages: Python · Go · Rust · TypeScript · SQL · Docker, GitHub Actions

## PROJECTS

**Black Index — Money Path for a Two-Sided Marketplace**
- Built the backend core of a 31k-LOC affiliate marketplace: HMAC-verified webhook ingestion from 14 payment providers (Razorpay, Stripe, Gumroad, Lemon Squeezy, PayPal, Cashfree, PhonePe, PayU, Instamojo, CCAvenue, Shopify, Cal.com, +custom) feeding an atomic record_conversion RPC — customer upsert, recurring-billing count, idempotent transaction insert, founder wallet debit, seller escrow credit, and platform-fee accounting in a single transaction.
- Designed the settlement pipeline: 30-day escrow hold with cron jobs for escrow release, reconciliation, wallet checks, and a dispute SLA ("guillotine"); self-referral detection, velocity limits, timing-safe secret comparison, and RLS on every table; admin APIs for users, products, transactions, disputes, and blacklist data.
- Tech: Next.js API routes, Supabase/Postgres, Razorpay/Stripe, Zod — github.com/Aryan-Protein-Vala/Black-Index

**B1 Copilot — Enterprise Analytics API (SAP)**
- Built the FastAPI backend for a natural-language SAP copilot: 4-tool agent layer (schema search over table/column comments, table describe, structured query builder with 10 filter operators + aggregates, guarded raw SQL), streaming responses interleaving tables/charts/summaries, and an auto-fallback data source chain (HANA → B1 Service Layer → offline sandbox).
- Hardened every path: SELECT/WITH-only guard, parameter binding, auto row caps, per-employee session scoping, tampered/expired token rejection — covered by 40+ network-free unit tests and a 60-question E2E accuracy harness with CI scorecard.
- Tech: Python, FastAPI, SAP HANA, OData, Docker, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**CLAIM/05 — Go WebSocket Engine for 25M-Cell Real-Time State**
- Built the state engine in Go: Gorilla WebSocket hub with concurrent channel hubs, Redis SETNX as the atomic cell lock (two players can never win the same cell), and Pub/Sub delta fan-out reaching all connected clients in sub-millisecond; persistent player tokens for reload-safe reconnection.
- Operated it 24/7 on Render with automated health endpoints and a GitHub Actions 10-minute keep-alive → zero cold starts.
- Tech: Go, Gorilla WebSockets, Redis, Render, GitHub Actions — github.com/Aryan-Protein-Vala/Grid-Game · live: multiplayer-grid-game-theta.vercel.app

**GSTGenius — Serverless Billing & Compliance Backend**
- Built the Firebase Cloud Functions backend: recurring invoices (daily/weekly/monthly), automated WhatsApp + email payment reminders, GST tax computation (CGST/SGST/IGST from HSN + location), GSTR-1/GSTR-3B report generation, and gateway auto-reconciliation marking invoices Paid on confirmation.
- Tech: Firebase (Firestore, Functions, Auth), Razorpay, Node.js — github.com/Aryan-Protein-Vala/GSTGenius

**Council — Prepaid Credit Wallet Backend**
- Built the wallet service for a multi-model AI platform: integer-credit ledger with typed transactions (deposit/usage/refund/bonus), Razorpay UPI top-ups with webhook-verified settlement, balance/transaction APIs, and tier-based gating; Clerk auth with Supabase RLS scoping every query to the owner.
- Tech: Next.js API routes, Supabase, Clerk, Razorpay — github.com/Aryan-Protein-Vala/multi-model

**VĀYU — WebSocket Backend Root-Cause Victory**
- Built a FastAPI + WebSocket RAG backend, then audited it with a scripted 10-query harness that exposed a missing TCP_NODELAY in uvicorn's websockets path (Nagle + delayed ACK adding ~42 ms per round trip) — fixed and verified 44 ms → 1.5 ms (96% reduction).
- Tech: Python, FastAPI, Uvicorn, FAISS — github.com/Aryan-Protein-Vala/vayu-voice-rag

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Data Structures & Algorithms, Databases, Operating Systems, Computer Networks
