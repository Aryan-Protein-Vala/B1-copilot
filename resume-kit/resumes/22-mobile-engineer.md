# ARYAN SHARMA
**Mobile Engineer (iOS · Android · Cross-Platform)**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Mobile engineer with real cross-platform native work: a single Rust engine bridged to iOS (Swift XCFramework) and Android (Kotlin JNI) via UniFFI, a BLE GATT protocol design that works around the quirks of both CoreBluetooth and BluetoothGattServer, and native-feel desktop/mobile products (Tauri, PyQt) with one-line distribution. 10,700+ LOC of mobile systems code, including fixes only possible on the platform side.

## TECHNICAL SKILLS
- iOS: Swift · CoreBluetooth (Peripheral + Central) · CryptoKit · Secure Enclave · XCFramework · App Intents · Tauri on macOS (Core Graphics)
- Android: Kotlin · BluetoothGattServer/GattClient · Android Keystore · java.security · JNI · XCFramework/JNI interop · Gradle
- Cross-Platform: Mozilla UniFFI (Rust→Swift/Kotlin FFI) · byte-identical cipher parity across stacks · shared protocol design · BLE (MTU negotiation, CCCD, fragmentation)
- Product: mobile-first React/Next.js · WebView-free native capture paths · one-line installers (curl) · PyInstaller/gradle packaging · App Store–adjacent licensing (HWID/UUID binding)
- Languages: Swift · Kotlin · Rust · TypeScript · Python

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

**Astral — Cross-Platform BLE Mesh SDK (Rust core → iOS + Android)**
- Built one Rust engine (astral-core: cryptography, MTU slicing, spray-and-wait routing) and bridged it to both mobile stacks with Mozilla UniFFI — Swift XCFramework for iOS, Kotlin via JNI for Android — so the mesh protocol is byte-identical on every device (10,700+ LOC total).
- Solved the iOS↔Android BLE interop problems platform by platform: manual CCCD descriptor (0x2902) writes on Android Centrals to correctly subscribe to iOS Peripheral ACKs (the "merchant did not respond" bug), sequential onCharacteristicWrite queues replacing racy timer-based writes, and dynamic MTU negotiation to 512 B with fragmentation for 200–500 B payloads.
- Implemented hardware-backed identity on both platforms: iOS Secure Enclave and Android Hardware Keystore P-256 keypairs, with ChaCha20-Poly1305 AEAD parity between Apple CryptoKit and java.security down to the byte.
- Shipped demo apps on both platforms (Android wallet + QR scanner screens, iOS app) plus a Next.js/Supabase reconciliation backend for when devices reconnect.
- Tech: Rust, Swift, Kotlin, UniFFI, BLE GATT, Noise Protocol — github.com/Aryan-Protein-Vala/Astral-Offline · github.com/Aryan-Protein-Vala/Astral-Network

**MYLO OS — Native Desktop Agent (macOS + Windows)**
- Built a Tauri 2 (Rust) agent with first-class native integrations on both desktop OSes: zero-latency screen capture (macOS Core Graphics / Windows Graphics Capture), human-paced input injection, global hotkeys, and OS-level stealth (NSWindow.sharingType / WDA_EXCLUDEFROMCAPTURE) so the overlay is invisible to screen share — ~35 MB RSS.
- Tech: Rust, Tauri 2, Swift (macOS surface), TypeScript — github.com/Aryan-Protein-Vala/MyloOS

**Snag — Native macOS App with One-Line Distribution**
- Built a native-feel macOS utility in Python + PyQt6, packaged with PyInstaller: global-hotkey floating widget (frameless, matte dark mode), screenshot hub, real-time downloads tracker, 15-slot clipboard history, and drag-and-drop out into any app — with a curl one-liner installer that installs to /Applications and handles Gatekeeper safely.
- Tech: Python, PyQt6, PyInstaller, Next.js, Supabase — github.com/Aryan-Protein-Vala/Snag

**DermaOS — Mobile-First Consumer Product (live)**
- Built the mobile-first product experience for an AI skincare app: scan-to-report flow, onboarding, modals, and marketplace UI tuned for small screens and Indian market context (INR pricing, UPI via Razorpay); live at dermaos.vercel.app.
- Tech: Next.js 16, Tailwind, shadcn/ui — github.com/Aryan-Protein-Vala/DermaOS
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
