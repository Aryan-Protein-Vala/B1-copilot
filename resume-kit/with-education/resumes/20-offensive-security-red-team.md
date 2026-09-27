# ARYAN SHARMA
**Offensive Security (Red Team) Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Offensive security engineer who builds automation for authorized engagements: an autonomous CTEM swarm engine that mimics APT behavior at machine speed (WAF-defeating payload mutation, temporal blind SQLi, lateral trust mapping), the adversarial testing layer for LLM applications (injection/jailbreak guardrail validation), and the defensive test suites that prove money paths survive forged webhooks. Every tool I ship has a hard authorization gate — no scope file, no execution. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Offensive: SQLi (blind/temporal, UNION extraction) · XSS (tag obfuscation) · SSRF · WAF evasion (payload mutation, hex-quoted literals, keyword case swaps) · traffic mimicry (per-worker RNG, UA rotation, packet jitter) · lateral trust mapping · APT simulation
- Automation: Rust swarm orchestration (MPSC channels, priority pools) · AI-driven payload generation · memory-mapped harvesting (Parquet) · sub-millisecond timing engines · scope-gated engagement modes
- LLM Security: prompt-injection & jailbreak validation · guardrail red-teaming · grounding/hallucination testing · secret detection · tool-use policy testing
- AppSec Testing: webhook signature forgery tests · timing-safe comparison validation · replay-attack tests · session hijack tests · RLS bypass tests
- Languages: Rust · Python · TypeScript · Go · SQL · bash

## PROJECTS

**GhostStrike — Autonomous CTEM / Red-Team Swarm Engine (Rust)**
- Built the swarm orchestrator: multi-threaded execution over MPSC channels with high/low-priority pools distributing work across the target surface, plus the "ghost protocol" — per-worker RNG, user-agent rotation, packet jitter, session persistence — making autonomous traffic indistinguishable from organic users and defeating rate-limiting.
- Engineered the AI Bridge: a real-time payload mutation engine applying hex-quoted literals, SQL keyword case swapping, and XSS tag obfuscation on the fly to defeat static WAF rule sets.
- Built the Harvester and Temporal Observer: Parquet memory-mapped data harvesting with an infinite iterator streaming blind UNION-extraction results into local databases, and a sub-millisecond timing engine for timing-based blind SQLi with absolute precision.
- Designed a 3-tier engagement model (Phantom Recon: zero-signature passive mapping → Tactical Strike: surgical XSS/SQLi/SSRF → Swarm Overdrive: APT-hot simulation with lateral trust mapping) gated by a strict authorization check: no scope file, no execution — built exclusively for sanctioned operations.
- Tech: Rust, MPSC concurrency, Parquet/mmap, CTEM — github.com/Aryan-Protein-Vala/GhostStrike (public demo; full engine licensed privately)

**VĀYU — LLM Guardrail Validation in Production**
- Built the deterministic guardrail layer for a production RAG system (compiled regex, <1 ms, running concurrently with retrieval) and adversarially validated it: prompt-injection, jailbreak, and off-topic interception paths, plus the output grounding validator that rejects ungrounded citations — the measurable hallucination gate.
- Tech: Python, FastAPI, FAISS — github.com/Aryan-Protein-Vala/vayu-voice-rag

**B1 Copilot — Injection-Proof Data Access (Defensive Test Suite)**
- Built the guard layer that an attacker's tests target: SELECT/WITH-only enforcement, DDL/DML/CALL rejection even inside sub-queries, identifier validation against the live catalog, parameter binding, and auto row caps — with adversarial unit tests ("raw SQL write is blocked", "unknown column rejected with suggestion", "forged/tampered/expired token rejected", "cross-employee session hijack blocked").
- Tech: Python, FastAPI, pytest, SAP HANA — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**Black Index — Money-Path Adversarial Tests**
- Built the verification for a payment-adjacent system against realistic attack paths: forged webhook signatures, replayed events, double-settled conversions, self-referral fraud, and velocity abuse — each with a tested rejection path (HMAC verification, timing-safe comparison, idempotency keys, RLS).
- Tech: Next.js, Supabase, Razorpay/Stripe — github.com/Aryan-Protein-Vala/Black-Index

**Oblivion AI — Agent Runtime Security Testing Surface**
- Built the security layer of an autonomous agent (tool-use policies, secret detection, audit trail) — and the adversarial case it's tested against: an agent with shell access must be as hard to subvert as the app around it.
- Tech: TypeScript, Tauri v2 — github.com/Aryan-Protein-Vala/Oblivion-AI

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Computer Networks, Operating Systems, Data Structures & Algorithms, Computer Security
