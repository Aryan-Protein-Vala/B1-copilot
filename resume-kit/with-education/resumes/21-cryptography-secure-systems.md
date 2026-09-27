# ARYAN SHARMA
**Cryptography & Secure Systems Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Applied cryptography and secure-systems engineer: designed the full crypto pipeline for an offline P2P payment mesh (Secure Enclave/Keystore P-256 keys, Noise-protocol ECDH, ChaCha20-Poly1305 AEAD, ECDSA non-repudiation, Bloom-filter replay defense), hardware-accelerated E2EE file transfer (PBKDF2 → AES-256-GCM over QUIC), and local-first systems where the security model is "nothing leaves the device." IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Cryptography: P-256 (secp256r1) ECDH · ChaCha20-Poly1305 AEAD · AES-256-GCM · PBKDF2 KDF · HKDF-SHA256 · ECDSA-SHA256 signatures · Noise Protocol Framework · hardware SHA-256 (SHA-NI) · Bloom filters (replay defense)
- Key Management: iOS Secure Enclave · Android Hardware Keystore · hardware-UUID license binding · edge-side key injection (keys never reach the client)
- Secure Architecture: E2EE designs · non-repudiation · replay-attack prevention · timing-safe comparisons · HMAC webhook verification · RLS · secret detection · tamper/expired token rejection · air-gapped (zero-telemetry) products
- Platforms: Rust · Go · Swift · Kotlin · Python · BLE GATT (secure transport) · QUIC

## PROJECTS

**Astral — Offline P2P Payment Mesh Crypto Pipeline**
- Designed the complete on-device crypto pipeline for a payment mesh with zero connectivity: P-256 keypair generation and storage in iOS Secure Enclave / Android Hardware Keystore, Noise-protocol handshake (ephemeral P-256 ECDH + HKDF-SHA256 key derivation), ChaCha20-Poly1305 AEAD payload encryption, and ECDSA-SHA256 sender signatures giving every transaction non-repudiation.
- Solved the replay-attack problem unique to delayed delivery: Bloom-filter/hash tracking dedupes on the transaction ID hash (not ciphertext — which differs per ephemeral key), so offline replay attempts are rejected at reconciliation.
- Achieved byte-for-byte cipher parity between Apple CryptoKit and Android java.security — the hard requirement for cross-platform decryption — and fixed the BLE-layer bug (CCCD 0x2902) that had broken ACK security sequencing.
- Tech: Rust, Swift, Kotlin, UniFFI, BLE GATT, Noise Protocol, P-256, ChaCha20-Poly1305 — github.com/Aryan-Protein-Vala/Astral-Offline · github.com/Aryan-Protein-Vala/Astral-Network

**Aether — E2EE Transfer Engine with Hardware Crypto (Go)**
- Built the encryption layer for WAN transfers: PBKDF2 key derivation from a user passphrase into AES-256-GCM, with authentication tagging (a single flipped bit is detected and dropped) and per-16MB-chunk key independence — any chunk can be re-verified or resumed without restarting the transfer.
- Moved hashing off the ALU: hardware SHA-256 (Intel SHA-NI / Apple M-series crypto) across 10 parallel goroutines, so integrity checking never becomes the throughput bottleneck on a saturated link.
- Tech: Go, AES-256-GCM, PBKDF2, QUIC — github.com/Aryan-Protein-Vala/AetherNet

**B1 Copilot — Auth & Integrity for an Enterprise Copilot**
- Built the security test matrix for an app holding customer ERP access: forged-unsigned token rejected, tampered signature rejected, expired token rejected, cross-employee session hijack blocked, sessions scoped per employee — plus read-only technical DB user, SELECT-only guarded SQL, and parameter binding as defense-in-depth.
- Tech: Python, FastAPI, pytest, JWT — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**MYLO OS — Keys That Never Touch the Client**
- Designed the key architecture for a managed AI tier: license keys validated at the Cloudflare edge, Anthropic master API keys injected server-side per request — the client physically cannot exfiltrate provider keys; desktop-side secure credential storage (Rust) + PII masking + tier gating complete the model.
- Tech: Rust, Tauri 2, Cloudflare Workers — github.com/Aryan-Protein-Vala/MyloOS

**Prometheus — Air-Gapped by Design (live)**
- Built a system cleaner whose security model is absence: 100% offline, zero telemetry, air-gapped logic — with HWID-bound licensing (persistent hardware identification) to prevent license burnout in enterprise fleets.
- Tech: Rust, TUI — github.com/Aryan-Protein-Vala/Prometheus

**Snag — Hardware-Bound Licensing**
- Built the activation protocol for a native macOS app: on first launch the app binds to the macOS Hardware UUID, validates a 16-character license key against the Next.js + Supabase backend, and activates the machine — plus Razorpay/PayPal webhook-verified billing.
- Tech: Python (PyQt6), Next.js, Supabase — github.com/Aryan-Protein-Vala/Snag

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Computer Networks, Operating Systems, Data Structures & Algorithms, Cryptography & Security
