# ARYAN SHARMA
**Desktop & Developer Tools Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Desktop and developer-tools engineer: a Tauri 2/Rust desktop AI that operates the OS via a ghost cursor, an offline Rust TUI system cleaner distributed with a one-line curl installer and enterprise fleet console, a native macOS widget with hardware-bound licensing, and a 15-tool zero-trust browser WASM toolkit. I build tools people install on their own machines — and the distribution, licensing, and ops around them.

## TECHNICAL SKILLS
- Desktop: Tauri 2 (Rust plugins: hotkeys, screen capture, input injection, secure storage) · Windows Graphics Capture · macOS Core Graphics · Python/PyQt6 · PyInstaller · native-feel UI patterns
- CLIs & TUIs: Rust TUIs · terminal UX · one-line curl/PowerShell installers · HWID-bound licensing · fleet management consoles
- Performance: zero-latency capture paths · ~35 MB RSS budgets · multi-threaded WebAssembly (COOP/COEP + SharedArrayBuffer) · ffmpeg.wasm · tesseract.js
- Dev Tools: Chrome extensions (MV3) · MCP servers · plugin systems with hooks · secret detection · audit trails
- Languages: Rust · TypeScript · Python · Go · SQL · Docker, GitHub Actions

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

**MYLO OS — Desktop AI Operator (Tauri 2 / Rust)**
- Built a Tauri 2 desktop agent that overlays a transparent control layer above any running application (IDE, Blender, Excel, terminal) using zero-latency Windows Graphics Capture + macOS Core Graphics, and executes spoken tasks with a ghost cursor — holding ~35 MB RSS.
- Wrote the Rust plugin suite: global hotkeys (hotkey.rs), screen capture (screen_capture.rs), human-paced input injection (input_injector.rs), secure credential storage (storage.rs), PII masking, and tier gating; OS-level stealth (WDA_EXCLUDEFROMCAPTURE / NSWindow.sharingType) hides the overlay from screen capture, share, and recording.
- Tech: Rust, Tauri 2, WGC, Core Graphics, Cloudflare Workers, Next.js — github.com/Aryan-Protein-Vala/MyloOS · mylo-frontend.vercel.app

**Prometheus — Offline OS Cleaner + Fleet Console (live)**
- Built a 100% offline, zero-telemetry Rust TUI: deep-flush scans finding hidden caches, phantom duplicates, and ad-trackers across thousands of files in milliseconds; HWID-bound licensing; centralized Enterprise Fleet Command Center; one-line curl installer — live at prometheus-cleaner.vercel.app.
- Tech: Rust, TUI, Next.js, GitHub Actions — github.com/Aryan-Protein-Vala/Prometheus

**Snag — macOS Floating Productivity Widget**
- Built a native macOS widget in Python + PyQt6 (PyInstaller-packaged): global-hotkey summon, 10-most-recent screenshots hub, real-time downloads tracker, rolling 15-item clipboard history, pinned snippets, and drag-and-drop of files/text directly into Finder, Chrome, or Slack.
- Tech: Python, PyQt6, PyInstaller, Next.js, Supabase — github.com/Aryan-Protein-Vala/Snag

**CORTEX — Desktop Memory App + MCP Server**
- Built the Tauri desktop surface: live 3D WebGL memory graph (nodes pulse on access, dim as they decay) plus an MCP server so any MCP-capable editor/agent reads the same memory — Docker Compose distribution for the SurrealDB/Qdrant/Redis stack.
- Tech: Rust, Tauri, SurrealDB, Qdrant, Docker — github.com/Aryan-Protein-Vala/CORTEX

**ToolGrid — 15-Tool Browser WASM Toolkit**
- Built 15 pro tools that run 100% client-side with zero uploads: multi-threaded ffmpeg.wasm video compression, in-browser AI background removal, Tesseract OCR, 4K mockup canvas, batch SVG vectorizer, and a Manifest V3 ad-blocker generator — behind COOP/COEP + SharedArrayBuffer.
- Tech: Astro, WebAssembly, Canvas, JSZip — github.com/Aryan-Protein-Vala/Micro-Tools
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
