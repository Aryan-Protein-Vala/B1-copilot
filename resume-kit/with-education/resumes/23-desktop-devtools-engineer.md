# ARYAN SHARMA
**Desktop & Developer Tools Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Desktop and developer-tools engineer: a Tauri 2/Rust desktop AI that operates the OS via a ghost cursor, an offline Rust TUI system cleaner distributed with a one-line curl installer and enterprise fleet console, a native macOS widget with hardware-bound licensing, and a 15-tool zero-trust browser WASM toolkit. I build tools people install on their own machines — and the distribution, licensing, and ops around them. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Desktop: Tauri 2 (Rust plugins: hotkeys, screen capture, input injection, secure storage) · Windows Graphics Capture · macOS Core Graphics · Python/PyQt6 · PyInstaller · native-feel UI patterns
- CLIs & TUIs: Rust TUIs · terminal UX · one-line curl/PowerShell installers · HWID-bound licensing · fleet management consoles
- Performance: zero-latency capture paths · ~35 MB RSS budgets · multi-threaded WebAssembly (COOP/COEP + SharedArrayBuffer) · ffmpeg.wasm · tesseract.js
- Dev Tools: Chrome extensions (MV3) · MCP servers · plugin systems with hooks · secret detection · audit trails
- Languages: Rust · TypeScript · Python · Go · SQL · Docker, GitHub Actions

## PROJECTS

**MYLO OS — Desktop AI Operator (Tauri 2 / Rust)**
- Built a Tauri 2 desktop agent that overlays a transparent control layer above any running application (IDE, Blender, Excel, terminal) using zero-latency Windows Graphics Capture + macOS Core Graphics, and executes spoken tasks with a ghost cursor — holding ~35 MB RSS.
- Wrote the Rust plugin suite: global hotkeys (hotkey.rs), screen capture (screen_capture.rs), human-paced input injection (input_injector.rs), secure credential storage (storage.rs), PII masking, and tier gating; OS-level stealth (WDA_EXCLUDEFROMCAPTURE / NSWindow.sharingType) hides the overlay from screen capture, share, and recording.
- Built the background-agent orchestrator: headless Chrome worker pool for long tasks (scrape 200+ competitors, post content, pull leads) with completion pings — the desktop app as a control plane for background automation.
- Tech: Rust, Tauri 2, WGC, Core Graphics, Cloudflare Workers, Next.js — github.com/Aryan-Protein-Vala/MyloOS · mylo-frontend.vercel.app

**Prometheus — Offline OS Cleaner + Fleet Console (live)**
- Built a 100% offline, zero-telemetry Rust TUI: deep-flush scans finding hidden caches, phantom duplicates, and ad-trackers across thousands of files in milliseconds; HWID-bound license keys; a centralized Enterprise Fleet Command Center for org-wide management; one-line curl installer for macOS/Linux — live at prometheus-cleaner.vercel.app.
- Tech: Rust, TUI, Next.js, GitHub Actions — github.com/Aryan-Protein-Vala/Prometheus

**Snag — macOS Floating Productivity Widget**
- Built a native macOS widget in Python + PyQt6 (PyInstaller-packaged): global-hotkey summon, 10-most-recent screenshots hub, real-time downloads tracker, rolling 15-item clipboard history, pinned snippets, and drag-and-drop of files/text directly into Finder, Chrome, or Slack.
- Shipped the full distribution + monetization stack: curl one-liner installer (installs to /Applications, safe Gatekeeper handling), Next.js + Supabase backend, Razorpay/PayPal webhook billing, and hardware-UUID license activation.
- Tech: Python, PyQt6, PyInstaller, Next.js, Supabase — github.com/Aryan-Protein-Vala/Snag

**CORTEX — Desktop Memory App + MCP Server**
- Built the desktop surface for an AI memory engine: Tauri client with a live 3D WebGL memory graph (nodes pulse on access, dim as they decay), plus an MCP server so any MCP-capable editor/agent can read the same memory — Docker Compose distribution for the SurrealDB/Qdrant/Redis stack.
- Tech: Rust, Tauri, SurrealDB, Qdrant, Docker — github.com/Aryan-Protein-Vala/CORTEX

**ToolGrid — 15-Tool Browser WASM Toolkit**
- Built a zero-trust toolkit of 15 pro tools that run 100% client-side: multi-threaded ffmpeg.wasm video compression, in-browser AI background removal, Tesseract OCR, 4K device-mockup canvas engine, batch SVG vectorizer, lamejs audio encoding, Manifest V3 ad-blocker generator, ATS resume matcher — behind COOP/COEP + SharedArrayBuffer so WASM is multi-threaded, with zero server uploads.
- Tech: Astro, WebAssembly, Canvas, JSZip — github.com/Aryan-Protein-Vala/Micro-Tools

**CommentLysis — Chrome Extension (MV3)**
- Built a Manifest V3 Chrome extension that runs the full analysis pipeline (sentiment, questions, video ideas) in-page while browsing YouTube — content-script capture, popup UX, and secure API bridging.
- Tech: Chrome Extension MV3, Next.js, GPT-4o — github.com/Aryan-Protein-Vala/CommentLysis

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Operating Systems, Data Structures & Algorithms, Databases, Computer Networks
