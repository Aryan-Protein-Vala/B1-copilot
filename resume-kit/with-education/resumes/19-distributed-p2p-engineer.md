# ARYAN SHARMA
**Distributed Systems & P2P Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Distributed systems engineer focused on systems that work without central infrastructure: a delay-tolerant mesh where every phone is a roaming router, a P2P transfer engine that bypasses the relay when peers are in range, a multiplayer state machine with conflict-free atomic locks across 25M cells, and a shared memory fabric synced over gRPC across devices. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Distributed Patterns: P2P + signaling-relay hybrids · Delay-Tolerant Networking (DTN) · opportunistic routing (spray-and-wait) · mesh networking · eventual consistency & offline-first sync · conflict-free atomic operations (SETNX) · Pub/Sub fan-out
- Concurrency: Go goroutines + channel hubs · Rust tokio (MPSC channels, async runtimes) · lock-free design · race-condition elimination (callback-driven queues)
- State & Data: Redis (KV, Pub/Sub, atomic ops) · SurrealDB (graph) · Qdrant · idempotency & dedup (Bloom filters) · event-driven reconciliation
- Networking: QUIC · raw TCP · WebSockets · mDNS/ZeroConf · BLE GATT · E2EE (ChaCha20-Poly1305, Noise)
- Languages: Rust · Go · Python · TypeScript · Swift/Kotlin (FFI)

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

**Black Index — Event-Driven Offline Tolerance**
- Built the offline-tolerant settlement pattern for a marketplace: provider webhooks may arrive late, duplicated, or out of order — idempotent transaction keys, atomic settlement RPCs, and reconciliation crons keep the distributed ledger consistent across 14 external systems.
- Tech: Next.js, Supabase/Postgres, Razorpay/Stripe — github.com/Aryan-Protein-Vala/Black-Index

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Computer Networks, Operating Systems, Data Structures & Algorithms, Databases
