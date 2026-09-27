# ARYAN SHARMA
**Cryptography & Secure Systems Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Applied cryptography and secure-systems engineer: designed the full crypto pipeline for an offline P2P payment mesh (Secure Enclave/Keystore P-256 keys, Noise-protocol ECDH, ChaCha20-Poly1305 AEAD, ECDSA non-repudiation, Bloom-filter replay defense), hardware-accelerated E2EE file transfer (PBKDF2 → AES-256-GCM over QUIC), and local-first systems where the security model is "nothing leaves the device.".

## TECHNICAL SKILLS
- Cryptography: P-256 (secp256r1) ECDH · ChaCha20-Poly1305 AEAD · AES-256-GCM · PBKDF2 KDF · HKDF-SHA256 · ECDSA-SHA256 signatures · Noise Protocol Framework · hardware SHA-256 (SHA-NI) · Bloom filters (replay defense)
- Key Management: iOS Secure Enclave · Android Hardware Keystore · hardware-UUID license binding · edge-side key injection (keys never reach the client)
- Secure Architecture: E2EE designs · non-repudiation · replay-attack prevention · timing-safe comparisons · HMAC webhook verification · RLS · secret detection · tamper/expired token rejection · air-gapped (zero-telemetry) products
- Platforms: Rust · Go · Swift · Kotlin · Python · BLE GATT (secure transport) · QUIC

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

**Astral — Offline P2P Payment Mesh Crypto Pipeline**
- Designed the complete on-device crypto pipeline for a payment mesh with zero connectivity: P-256 keypair generation and storage in iOS Secure Enclave / Android Hardware Keystore, Noise-protocol handshake (ephemeral P-256 ECDH + HKDF-SHA256 key derivation), ChaCha20-Poly1305 AEAD payload encryption, and ECDSA-SHA256 sender signatures giving every transaction non-repudiation.
- Solved the replay-attack problem unique to delayed delivery: Bloom-filter/hash tracking dedupes on the transaction ID hash (not ciphertext — which differs per ephemeral key), so offline replay attempts are rejected at reconciliation.
- Tech: Rust, Swift, Kotlin, UniFFI, BLE GATT, Noise Protocol, P-256, ChaCha20-Poly1305 — github.com/Aryan-Protein-Vala/Astral-Offline · github.com/Aryan-Protein-Vala/Astral-Network

**Aether — E2EE Transfer Engine with Hardware Crypto (Go)**
- Built the encryption layer for WAN transfers: PBKDF2 key derivation from a user passphrase into AES-256-GCM, with authentication tagging (a single flipped bit is detected and dropped) and per-16MB-chunk key independence — any chunk can be re-verified or resumed without restarting the transfer.
- Tech: Go, AES-256-GCM, PBKDF2, QUIC — github.com/Aryan-Protein-Vala/AetherNet

**B1 Copilot — Auth & Integrity for an Enterprise Copilot**
- Built the security test matrix for an app holding customer ERP access: forged-unsigned, tampered, and expired token rejection; cross-employee session-hijack blocking; read-only technical DB user and SELECT-only guarded SQL as defense-in-depth.
- Tech: Python, FastAPI, pytest, JWT — github.com/Aryan-Protein-Vala/Cira-RAG-agent

## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
