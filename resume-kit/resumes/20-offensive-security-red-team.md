# ARYAN SHARMA
**Offensive Security (Red Team) Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Offensive security engineer who builds automation for authorized engagements: an autonomous CTEM swarm engine that mimics APT behavior at machine speed (WAF-defeating payload mutation, temporal blind SQLi, lateral trust mapping), the adversarial testing layer for LLM applications (injection/jailbreak guardrail validation), and the defensive test suites that prove money paths survive forged webhooks. Every tool I ship has a hard authorization gate — no scope file, no execution.

## TECHNICAL SKILLS
- Offensive: SQLi (blind/temporal, UNION extraction) · XSS (tag obfuscation) · SSRF · WAF evasion (payload mutation, hex-quoted literals, keyword case swaps) · traffic mimicry (per-worker RNG, UA rotation, packet jitter) · lateral trust mapping · APT simulation
- Automation: Rust swarm orchestration (MPSC channels, priority pools) · AI-driven payload generation · memory-mapped harvesting (Parquet) · sub-millisecond timing engines · scope-gated engagement modes
- LLM Security: prompt-injection & jailbreak validation · guardrail red-teaming · grounding/hallucination testing · secret detection · tool-use policy testing
- AppSec Testing: webhook signature forgery tests · timing-safe comparison validation · replay-attack tests · session hijack tests · RLS bypass tests
- Languages: Rust · Python · TypeScript · Go · SQL · bash

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

**GhostStrike — Autonomous CTEM / Red-Team Swarm Engine (Rust)**
- Built the swarm orchestrator: multi-threaded execution over MPSC channels with high/low-priority pools distributing work across the target surface, plus the "ghost protocol" — per-worker RNG, user-agent rotation, packet jitter, session persistence — making autonomous traffic indistinguishable from organic users and defeating rate-limiting.
- Engineered the AI Bridge: a real-time payload mutation engine applying hex-quoted literals, SQL keyword case swapping, and XSS tag obfuscation on the fly to defeat static WAF rule sets.
- Built the Harvester and Temporal Observer: Parquet memory-mapped data harvesting with an infinite iterator streaming blind UNION-extraction results into local databases, and a sub-millisecond timing engine for timing-based blind SQLi with absolute precision.
- Tech: Rust, MPSC concurrency, Parquet/mmap, CTEM — github.com/Aryan-Protein-Vala/GhostStrike (public demo; full engine licensed privately)

**B1 Copilot — Injection-Proof Data Access (Defensive Test Suite)**
- Built the guard layer an attacker's tests target: SELECT/WITH-only enforcement, DDL/DML/CALL rejection inside sub-queries, live-catalog identifier validation, parameter binding — with adversarial unit tests (raw SQL write blocked, forged/tampered/expired token rejected, cross-employee session hijack blocked).
- Tech: Python, FastAPI, pytest, SAP HANA — github.com/Aryan-Protein-Vala/Cira-RAG-agent

## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
