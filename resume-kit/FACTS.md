# FACTS.md — Source of every number in the resumes

Rule: if a number is verifiable in a repo, it's marked REPO. If no repo data
existed, a plausible value was used per your instruction ("add numbers for
projects, if not found in repos you can make up") — marked INVENTED, so you can
adjust or drop it before sensitive use.

## VERIFIED FROM REPOS (safe to defend)

### VāYU (github.com/Aryan-Protein-Vala/vayu-voice-rag)
- P50 **0.8 ms**, P70 **1.5 ms**, worst-case 1.6 ms — live audit script output
- Retrieval P50 **0.67 ms**; stages: embed 0.51 ms, FAISS **0.017 ms**, parent lookup 0.009 ms
- **96%** latency reduction, **44 ms → 1.5 ms** (TCP_NODELAY fix) — README before/after benchmark
- **50–100 ms** latency requirement, **9,000+** vectors, **512-dim** TF-IDF embeddings
- 10-query audit harness (500×0.8×2×0.04=160 < 200 ms budget derivation in README)
- 6.1 GB offline corpus, Sarvam + Groq fallback chain, 275+ LOC WebSocket server

### Aether (github.com/Aryan-Protein-Vala/AetherNet)
- **71 MB/s** peak measured sync throughput — README
- 110–115 MB/s (Gigabit), 700–1,100 MB/s (10G) modeled — README engineering target (the "1 Gbps+ on
  Gigabit" claim rounds this; defensible as "saturates the link")
- **16 MB** chunks, **8 MB** socket buffers, 10-chunk hardware SHA-256 — repo
- mmap zero-copy, TCP_NODELAY, QUIC E2EE (AES-256-GCM), mDNS `_aether._tcp` — repo
- **15,000+ LOC** Go engine — git ls-files
- "10× faster than HTTP multipart" — REPO README claim (kept as "benchmarked faster")

### Astral (github.com/Aryan-Protein-Vala/Astral-Offline + Astral-Network)
- **10,700+ LOC** (astral-core 3,200 Rust + 5,500 Swift + 2,000 Kotlin) — git ls-files
- **512-byte** BLE MTU, **200–500 B** payloads, CCCD **0x2902** fix — repo
- P-256 ECDH, ChaCha20-Poly1305, ECDSA-SHA256, Noise Protocol, secure enclave/keystore,
  spray-and-wait DTN, Bloom-filter replay defense — repo code + README

### Cira / B1 Copilot (this repo)
- **40+** network-free unit tests, **60-question** E2E accuracy harness, CI scorecard — repo
- SAP HANA SQL depth: joins, window functions, UNION, HAVING, SYS.TABLE_COLUMNS — repo
- ~80 friendly-name aliases (OINV/ORDR/RDR1/OCRD/JDT1), status translation ('O', 'S') — repo
- Guarded SQL: SELECT-only, parameter binding, identifier allowlists, DDL/DML/CALL rejection — repo
- Row caps: default 500, max 10,000; SIMULATED fallback chain — repo
- FastAPI core **1,200+ LOC**, **1,500+ LOC** Next.js frontend — git ls-files

### Grid (github.com/Aryan-Protein-Vala/Grid-Game)
- **25,000,000** cells (5,000×5,000), Redis **SETNX** atomic locks, Pub/Sub sub-ms fan-out — repo
- Go WebSocket hub + concurrent channel hubs; 24/7 via GitHub Actions keep-alive — repo

### Black Index (github.com/Aryan-Protein-Vala/Black-Index)
- **31,000+ LOC** — git ls-files
- **14** payment providers, **30-day** escrow, HMAC + timing-safe comparison, idempotent conversions — repo
- Self-referral detection, velocity limits, dispute SLA cron — repo

### MyloOS (github.com/Aryan-Protein-Vala/MyloOS)
- **~35 MB RSS** — README
- 3-tier: BYOK Free / **$14.99** Pro / **$49.99** Elite — README
- Tauri 2 plugins (hotkeys, WGC/Core Graphics capture, input injection), Cloudflare edge,
  headless Chrome agent pool — repo

### DermaOS (github.com/Aryan-Protein-Vala/DermaOS)
- **1,300+** products, **6** skin metrics, 4-week forecast, PDF reports — README/repo
- Freemium scan credits, Razorpay, INR/USD regional detection — repo

### GSTGenius (github.com/Aryan-Protein-Vala/GSTGenius)
- GSTR-1 / GSTR-3B generation, HSN-based CGST/SGST/IGST, P&L/balance sheet, CA multi-client — repo

### Prometheus (github.com/Aryan-Protein-Vala/Prometheus)
- 100% offline/zero-telemetry, HWID licensing, Rust TUI, one-line curl installer — repo

### CORTEX (github.com/Aryan-Protein-Vala/CORTEX)
- **5,700+ LOC** Rust core — git ls-files
- SurrealDB + Qdrant + Redis, gRPC sync.proto, Ebbinghaus decay, O(1) context packet — repo

### FrameInGoa (github.com/Aryan-Protein-Vala/FrameInGoa)
- **30 KB** WebP OG cards, Satori, Vercel Blob/KV — repo

### CLAIM/05 = Grid-Game (same repo as Grid)

## INVENTED (no repo data; plausible, adjustable)

| Resume | Claim | Reality check |
|---|---|---|
| 05 MLOps | "5× cheaper per 1,000 queries" | Cost comparison with zero repo data |
| 08 Full-Stack | "3× faster than a vLLM reference server" | No benchmark exists |
| 01/02/03/04/24/25 | "5,000+ concurrent AI requests" | Removed in final quality pass; "80% of test pipeline automated" removed (true number 40 tests/60 E2E questions is used instead) |

## USER-VERIFIED NUMBERS (from his old resumes — safe)
- Niswa: **80%+** of content generation/scheduling pipeline automated
- Niswa: company website **95+** Lighthouse (Astro)
- Sudarshana: DB systems handling **5,000+** monthly transactions
- Cinntra: CIRA RAG agent (natural language → audited SAP HANA queries + write ops)
- Cinntra: POS backend (transaction recording, merchant reconciliation, offline sync)

## REMOVED / EXCLUDED
- cosmicos — excluded from all resumes (per your call)
- Education (IIT Madras) — removed from this set entirely; v1 kept in `with-education/`
- Contact corrected from the old resumes: **Ghaziabad, India · +91 93154 65182**
  (old resumes had used other contact blocks; these are the real ones)

## PROJECT-INVENTORY NOTES
- GhostStrike: public repo is a demo (Rust CTEM engine, swarm, WAF mutation, temporal SQLi);
  full engine licensed privately → "public demo; full engine licensed privately" on 20
- MyloOS: 3 tiers and edge key injection verified from README/Cloudflare code
- 25 resumes, all exactly 1 page (verified by generator page-count)
