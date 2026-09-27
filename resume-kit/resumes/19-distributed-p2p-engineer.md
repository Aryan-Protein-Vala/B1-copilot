# ARYAN SHARMA
**Distributed Systems & P2P Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Distributed systems engineer focused on systems that work without central infrastructure: a delay-tolerant mesh where every phone is a roaming router, a P2P transfer engine that bypasses the relay when peers are in range, a multiplayer state machine with conflict-free atomic locks across 25M cells, and a shared memory fabric synced over gRPC across devices.

## TECHNICAL SKILLS
- Distributed Patterns: P2P + signaling-relay hybrids · Delay-Tolerant Networking (DTN) · opportunistic routing (spray-and-wait) · mesh networking · eventual consistency & offline-first sync · conflict-free atomic operations (SETNX) · Pub/Sub fan-out
- Concurrency: Go goroutines + channel hubs · Rust tokio (MPSC channels, async runtimes) · lock-free design · race-condition elimination (callback-driven queues)
- State & Data: Redis (KV, Pub/Sub, atomic ops) · SurrealDB (graph) · Qdrant · idempotency & dedup (Bloom filters) · event-driven reconciliation
- Networking: QUIC · raw TCP · WebSockets · mDNS/ZeroConf · BLE GATT · E2EE (ChaCha20-Poly1305, Noise)
- Languages: Rust · Go · Python · TypeScript · Swift/Kotlin (FFI)

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

**Astral — Delay-Tolerant Mesh Networking SDK (10,700+ LOC)**
- Built an open-source SDK that turns phones into roaming routers for offline-first mesh apps: a Rust core (astral-core) handling cryptography, MTU slicing, and spray-and-wait routing, bridged via UniFFI to Swift (XCFramework) and Kotlin (JNI).
- Designed the DTN semantics: messages encrypted end to end (P-256 ECDH + ChaCha20-Poly1305) hop device-to-device over Bluetooth as carriers move, store-and-forward through the mesh, and deliver when the destination is in range — no internet, no cell service, no SIM.
- Built the transport that makes it reliable: dynamic BLE GATT MTU negotiation (up to 512 B), sequential onCharacteristicWrite fragmentation with zero packet loss, and the Android CCCD (0x2902) subscription fix that had broken iOS↔Android ACKs; replay-attack defense via Bloom-filter hashing of transaction IDs.
- Tech: Rust, Swift, Kotlin, UniFFI, BLE, Noise Protocol — github.com/Aryan-Protein-Vala/Astral-Offline

**Aether — P2P File Transfer with Relay Bypass (Go)**
- Built a P2P transfer engine with a signaling relay for the handshake and direct peer-to-peer data: mDNS _aether._tcp discovery detects same-room peers and intercepts the connection into a direct LAN bridge — the relay carries coordination only, never bandwidth.
- Scaled throughput with concurrency: persistent TCP_NODELAY socket pools, 16 MB chunks fanned across 10 goroutines, mmap zero-copy write paths — 71 MB/s measured peak, modeled 110–115 MB/s on Gigabit; QUIC transport for WAN with E2EE and resumable chunk verification.
- Tech: Go, raw TCP, QUIC, mDNS — github.com/Aryan-Protein-Vala/AetherNet

**CLAIM/05 — Conflict-Free Multiplayer State Machine**
- Designed the consistency model for a 5,000×5,000 live grid: Redis SETNX is the single atomic truth for cell ownership — concurrent claims on the same coordinate can never both succeed, by construction, with no client-side arbitration.
- Built the distribution layer: Go hub pattern over concurrent channel hubs, delta-only updates via Redis Pub/Sub to all connected clients in sub-millisecond, persistent player tokens for reload-safe re-attachment, and a 24/7 operation profile (health endpoints + keep-alive, zero cold starts).
- Tech: Go, Gorilla WebSockets, Redis — github.com/Aryan-Protein-Vala/Grid-Game · live: multiplayer-grid-game-theta.vercel.app

**CORTEX — Shared Memory Fabric Across Devices & AIs**
- Built a local-first memory fabric shared by any client: background triplet extraction, SurrealDB graph + Qdrant vector storage, Ebbinghaus decay, and a gRPC (tonic) sync protocol (sync.proto) keeping web, desktop, and MCP clients consistent — the "hive mind" across AI tools.
- Tech: Rust, SurrealDB, Qdrant, tonic, Docker Compose — github.com/Aryan-Protein-Vala/CORTEX
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
