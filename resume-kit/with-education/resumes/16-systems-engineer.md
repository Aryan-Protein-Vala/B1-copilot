# ARYAN SHARMA
**Systems Software Engineer (Rust · Go)**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Systems engineer writing performance-critical software in Rust and Go: a zero-copy P2P transfer engine (mmap, raw TCP multiplexing, hardware SHA-256), a delay-tolerant mesh networking core bridged to iOS/Android via FFI, a graph-vector AI memory engine on gRPC, and a Tauri desktop OS agent holding ~35 MB RSS. 20+ systems shipped across 8 languages, with the hard parts always in the systems layer. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Systems Languages: Rust (tokio, axum, tonic/prost, unsafe-by-avoidance) · Go (goroutines, channels, mmap via syscall) · C/C++ interop · FFI (Mozilla UniFFI, JNI, XCFramework)
- OS & Performance: mmap zero-copy I/O · zero-heap-allocation hot paths · raw TCP (TCP_NODELAY, 8 MB socket buffers) · MPSC channels · thread pools · latency profiling (per-stage telemetry)
- Networking: TCP/IP · QUIC · WebSockets · mDNS/ZeroConf · BLE GATT · Delay-Tolerant Networking (DTN) · spray-and-wait routing
- Crypto (applied): P-256/ECDH · ChaCha20-Poly1305 · AES-256-GCM · PBKDF2 · ECDSA · HKDF · Noise Protocol
- Platforms: Linux · macOS (Core Graphics, WGC on Windows) · Docker · GitHub Actions · C++ (background)

## PROJECTS

**Aether — Zero-Copy P2P File Transfer Engine (Go)**
- Wrote the data path to hit physical NIC limits: syscall.Mmap pre-allocation + io.ReadFull straight from NIC buffers into memory-mapped file pointers — zero heap allocations and zero copy() operations in the hot path, bypassing the garbage collector entirely.
- Built a raw TCP multiplexer: pool of persistent TCP_NODELAY sockets with 8 MB OS socket buffers, files sliced into 16 MB parallel chunks over a [lengthPrefix][binaryFrame] protocol that skips per-chunk handshake latency; modeled 110–115 MB/s on Gigabit and 700–1,100 MB/s on 10G, with 71 MB/s peak measured sync throughput.
- Pushed 10 chunks through hardware SHA-256 (Intel SHA-NI / Apple crypto) on 10 goroutines; added mDNS (_aether._tcp) zeroconf discovery that auto-bridges LAN transfers above ISP ceilings, and a QUIC WAN transport with PBKDF2→AES-256-GCM E2EE (per-chunk independence for resumable, verified transfers).
- Tech: Go, syscall/mmap, raw TCP, QUIC, mDNS, AES-256-GCM — github.com/Aryan-Protein-Vala/AetherNet

**Astral — Delay-Tolerant Mesh Networking Core (Rust ↔ iOS/Android)**
- Wrote astral-core in Rust: all cryptography, MTU slicing, and spray-and-wait opportunistic routing for a DTN mesh where every phone is a roaming router — messages hop device-to-device over Bluetooth until they reach their destination's vicinity.
- Built the FFI layer with Mozilla UniFFI: one Rust engine exposed as a Swift XCFramework (iOS) and Kotlin via JNI (Android) with byte-identical behavior — 10,700+ LOC across the stack.
- Implemented the BLE transport: dynamic GATT MTU negotiation to 512 B and sequential onCharacteristicWrite fragmentation for zero-loss delivery of 200–500 B encrypted payloads across iOS CoreBluetooth ↔ Android BluetoothGattServer, including a fix for the Android CCCD (0x2902) write bug that broke iOS peripheral ACKs.
- Tech: Rust, Swift, Kotlin, UniFFI, BLE/GATT, P-256, ChaCha20-Poly1305 — github.com/Aryan-Protein-Vala/Astral-Offline

**CORTEX — AI Memory Engine (Rust, gRPC)**
- Built the core in Rust (5,700+ LOC): tokio async runtime, axum + gRPC (tonic/prost) APIs, SurrealDB graph writes, Qdrant vector lookups, and a background "shadow kernel" extracting JSON-LD triplets — with Ebbinghaus decay executed in the engine itself.
- Containerized the full stack (engine + SurrealDB + Qdrant + Redis) via Docker Compose; O(1) memory-injection endpoints keep token cost flat regardless of memory size.
- Tech: Rust, tokio, axum, tonic, SurrealDB, Qdrant, Docker — github.com/Aryan-Protein-Vala/CORTEX

**MYLO OS — Tauri 2 Desktop OS Agent (Rust)**
- Wrote the Rust core of a desktop OS operator: custom Tauri plugins for global hotkeys (hotkey.rs), zero-latency screen capture (Windows Graphics Capture / macOS Core Graphics), human-paced input injection (ghost cursor), secure credential storage, PII masking, and tier gating — holding ~35 MB RSS while overlaying live applications.
- Built OS-level stealth (WDA_EXCLUDEFROMCAPTURE / NSWindow sharingType) so the overlay is excluded from screen capture at the kernel boundary, plus a background-agent orchestrator spawning headless Chrome workers.
- Tech: Rust, Tauri 2, WGC, Core Graphics — github.com/Aryan-Protein-Vala/MyloOS

**Prometheus — Offline OS Cleaner (Rust TUI)**
- Built a 100% offline, zero-telemetry Rust TUI: deep-scan engines for hidden caches, phantom duplicates, and ad-trackers that walk thousands of files in milliseconds; HWID-bound licensing and an enterprise fleet command center; one-line curl distribution.
- Tech: Rust, TUI, Next.js — github.com/Aryan-Protein-Vala/Prometheus

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Operating Systems, Computer Networks, Data Structures & Algorithms, Databases, Linux
