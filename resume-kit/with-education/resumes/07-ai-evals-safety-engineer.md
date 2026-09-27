# ARYAN SHARMA
**AI Evals, Safety & Reliability Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
AI reliability engineer who treats LLM quality as a measurable engineering problem: built a 60-question E2E accuracy harness with CI scorecards, a SQL guard layer that rejects injection-shaped input by construction, deterministic input guardrails + output grounding validators in a production RAG system, and an adversarial red-team engine that tests guardrails the way an attacker would. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Evals: E2E accuracy harnesses · CI-gated scorecards · deterministic sandboxes for reproducible LLM tests · unit test suites for LLM apps (40+ tests, zero network/key deps) · per-stage latency telemetry
- Guardrails: deterministic regex injection/jailbreak filters · output grounding & citation validation · SQL injection prevention (SELECT-only, parameter binding, row caps, identifier allowlists) · secret detection · tool-use policies
- Adversarial: WAF-bypass payload mutation (hex-quoting, case-swap, XSS obfuscation) · timing-based blind extraction · traffic mimicry (UA rotation, jitter) — built to test, not attack
- Monitoring: audit trails · webhook log verification · idempotency & replay-attack defense (Bloom filters) · tampered/expired token rejection tests
- Languages: Python · Rust · TypeScript · Go · SQL · FastAPI, pytest, Docker

## PROJECTS

**B1 Copilot — LLM Safety Rails for an Enterprise ERP Copilot**
- Built the SQL guard layer: single-statement enforcement, SELECT/WITH only, DDL/DML/CALL rejected even inside sub-queries, identifiers validated against the live catalog, all values parameter-bound, row cap auto-injected when missing — the model literally cannot write to the customer's ERP.
- Auth & integrity test suite: forged-unsigned token rejected, tampered signature rejected, expired token rejected, cross-employee session hijack blocked, sessions scoped per employee — 40+ unit tests with no ERP, network, or API key required.
- Built the 60-question E2E accuracy harness: every question executed against a deterministic offline sandbox, scored into a CI gate scorecard so regressions in generation accuracy block merges.
- Tech: Python, FastAPI, pytest, SAP HANA, Next.js 16 — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**VĀYU — Deterministic Guardrails + Grounding in Production RAG**
- Built input guardrails as compiled deterministic regex running concurrently with vector search (<1 ms) — intercepting prompt injection, jailbreaks, and off-topic queries before they cost an LLM call.
- Built the output grounding validator: every claim and citation tag (e.g., [ID: 12345]) is checked against retrieved context IDs and rejected if ungrounded — hallucination becomes a measured, unit-testable failure mode, not a vibes metric.
- Measured reliability with a live 10-query audit harness and in-process per-stage benchmarks standing as regression gates.
- Tech: Python, FastAPI, WebSockets, FAISS — github.com/Aryan-Protein-Vala/vayu-voice-rag

**GhostStrike — Adversarial Engine for Testing Defenses**
- Built an autonomous CTEM engine that stress-tests enterprise surfaces the way an APT would: AI-driven payload mutation (hex-quoted literals, SQL keyword case swaps, XSS tag obfuscation) to defeat static rule sets, and a sub-millisecond temporal observer for timing-based blind SQLi — validating exactly where WAFs and apps break.
- Hard safety doctrine baked into the architecture: a strict authorization/scope gate means no scope file, no execution; three severity tiers (Phantom Recon → Tactical Strike → Swarm Overdrive) for authorized engagements only.
- Tech: Rust, MPSC concurrency, Parquet/mmap — github.com/Aryan-Protein-Vala/GhostStrike (demo; full engine licensed privately)

**Oblivion AI — Agent Runtime Security**
- Built the security layer for an autonomous agent that can execute tools: tool-use policy engine, secret detection in memory and transit, a full audit trail of agent actions, and a plugin loader that isolates untrusted extensions.
- Tech: TypeScript, Tauri v2, sqlite-vec — github.com/Aryan-Protein-Vala/Oblivion-AI

**Black Index — Money-Path Integrity**
- Built verification for a payment-adjacent marketplace: HMAC webhook signature verification with timing-safe secret comparison, idempotent external transaction IDs, self-referral + velocity checks, replay-safe dedup, and RLS on every table — with unit-tested rejection paths for forged webhooks and double-settled conversions.
- Tech: Next.js, Supabase/Postgres, Razorpay/Stripe, Zod — github.com/Aryan-Protein-Vala/Black-Index

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Data Structures & Algorithms, Operating Systems, Databases, Machine Learning, Computer Networks
