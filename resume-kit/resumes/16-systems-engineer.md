# ARYAN SHARMA
**Systems Software Engineer (Rust · Go)**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Systems engineer writing performance-critical software in Rust and Go: a zero-copy P2P transfer engine (mmap, raw TCP multiplexing, hardware SHA-256), a delay-tolerant mesh networking core bridged to iOS/Android via FFI, a graph-vector AI memory engine on gRPC, and a Tauri desktop OS agent holding ~35 MB RSS. 20+ systems shipped across 8 languages, with the hard parts always in the systems layer.

## TECHNICAL SKILLS
- Systems Languages: Rust (tokio, axum, tonic/prost, unsafe-by-avoidance) · Go (goroutines, channels, mmap via syscall) · C/C++ interop · FFI (Mozilla UniFFI, JNI, XCFramework)
- OS & Performance: mmap zero-copy I/O · zero-heap-allocation hot paths · raw TCP (TCP_NODELAY, 8 MB socket buffers) · MPSC channels · thread pools · latency profiling (per-stage telemetry)
- Networking: TCP/IP · QUIC · WebSockets · mDNS/ZeroConf · BLE GATT · Delay-Tolerant Networking (DTN) · spray-and-wait routing
- Crypto (applied): P-256/ECDH · ChaCha20-Poly1305 · AES-256-GCM · PBKDF2 · ECDSA · HKDF · Noise Protocol
- Platforms: Linux · macOS (Core Graphics, WGC on Windows) · Docker · GitHub Actions · C++ (background)

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

**Aether — Zero-Copy P2P File Transfer Engine (Go)**
- Wrote the data path to hit physical NIC limits: syscall.Mmap pre-allocation + io.ReadFull straight from NIC buffers into memory-mapped file pointers — zero heap allocations and zero copy() operations in the hot path, bypassing the garbage collector entirely.
- Built a raw TCP multiplexer: pool of persistent TCP_NODELAY sockets with 8 MB OS socket buffers, files sliced into 16 MB parallel chunks over a [lengthPrefix][binaryFrame] protocol that skips per-chunk handshake latency; modeled 110–115 MB/s on Gigabit and 700–1,100 MB/s on 10G, with 71 MB/s peak measured sync throughput.
- Tech: Go, syscall/mmap, raw TCP, QUIC, mDNS, AES-256-GCM — github.com/Aryan-Protein-Vala/AetherNet

**Astral — Delay-Tolerant Mesh Networking Core (Rust ↔ iOS/Android)**
- Wrote astral-core in Rust: all cryptography, MTU slicing, and spray-and-wait opportunistic routing for a DTN mesh where every phone is a roaming router — messages hop device-to-device over Bluetooth until they reach their destination's vicinity.
- Built the FFI layer with Mozilla UniFFI: one Rust engine exposed as a Swift XCFramework (iOS) and Kotlin via JNI (Android) with byte-identical behavior — 10,700+ LOC across the stack.
- Tech: Rust, Swift, Kotlin, UniFFI, BLE/GATT, P-256, ChaCha20-Poly1305 — github.com/Aryan-Protein-Vala/Astral-Offline

**CORTEX — AI Memory Engine (Rust, gRPC)**
- Built the core in Rust (5,700+ LOC): tokio async runtime, axum + gRPC (tonic/prost) APIs, SurrealDB graph writes, Qdrant vector lookups, and a background "shadow kernel" extracting JSON-LD triplets — with Ebbinghaus decay executed in the engine itself.
- Tech: Rust, tokio, axum, tonic, SurrealDB, Qdrant, Docker — github.com/Aryan-Protein-Vala/CORTEX

**MYLO OS — Tauri 2 Desktop OS Agent (Rust)**
- Wrote the Rust core of a desktop OS operator: custom Tauri plugins for global hotkeys (hotkey.rs), zero-latency screen capture (Windows Graphics Capture / macOS Core Graphics), human-paced input injection (ghost cursor), secure credential storage, PII masking, and tier gating — holding ~35 MB RSS while overlaying live applications.
- Tech: Rust, Tauri 2, WGC, Core Graphics — github.com/Aryan-Protein-Vala/MyloOS
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
