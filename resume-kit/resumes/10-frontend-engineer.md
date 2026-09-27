# ARYAN SHARMA
**Frontend Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Frontend engineer with a performance and interaction obsession: 95+ Lighthouse performance on shipped Next.js products, a 25,000,000-cell real-time canvas that pans/zooms at 60fps, client-side WebAssembly tooling (ffmpeg, Tesseract, AI background removal) running with zero server round-trips, and edge-optimized viral share loops (Vercel Blob/KV + Satori OG images).

## TECHNICAL SKILLS
- Core: React 19 · Next.js 14–16 (App Router, RSC, Server Actions) · TypeScript · Tailwind CSS · shadcn/ui · Radix · Framer Motion · Astro
- Canvas & Media: HTML5 Canvas (high-perf rendering math) · Rough.js · react-easy-crop · HEIC decode · ffmpeg.wasm (multi-threaded WASM) · tesseract.js · @imgly background-removal
- Real-Time: WebSockets (streaming LLM tokens, live game state) · optimistic UI · persistent reconnection patterns
- Edge & Performance: Vercel (Blob, KV, OG/Satori) · CDN immutable caching · COOP/COEP + SharedArrayBuffer for multi-threaded WASM · Lighthouse 95+ · client-side image compression (2 MB → 30 KB)
- Data: Supabase/Postgres, Prisma, Firebase, Zod

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

**CLAIM/05 — 25M-Cell Real-Time Canvas (live)**
- Built the canvas layer for a 5,000×5,000 (25,000,000-cell) multiplayer battlefield: custom pan/zoom camera math (two-finger/drag, pinch/CTRL+scroll), rough.js stroke rendering, a full-screen satellite minimap with live heat indicators, and identity hashing (crypto seed → deterministic HSL palette + spawn).
- Wired the WebSocket client for sub-millisecond state sync with reload-safe re-attachment (persistent tokens) — the UI never re-renders the full grid, only deltas.
- Tech: Next.js 16, React 19, HTML5 Canvas, WebSockets, Framer Motion — github.com/Aryan-Protein-Vala/Grid-Game · live: multiplayer-grid-game-theta.vercel.app

**DermaOS — AI Skincare Product Experience (live)**
- Built a polished consumer UI: AI scanner modal (photo upload → 6-metric score cards → 4-week forecast charts), onboarding flow, marketplace with ingredient-level product cards and personalized grades, PDF report viewer, glassmorphism modals, and INR/USD regional UI — 95+ Lighthouse, live at dermaos.vercel.app.
- Tech: Next.js 16, TypeScript, Tailwind, shadcn/ui, Recharts — github.com/Aryan-Protein-Vala/DermaOS

**B1 Copilot — Streaming Analytics UI**
- Built the chat interface that renders an enterprise copilot's output as it arrives: streamed markdown, live tables, auto-typed charts (aggregate detection drives chart type), and a two-line executive summary per query — plus Super Admin / Partner Admin / Client portals and a drag-in Excel/CSV migration wizard.
- Tech: Next.js 16, React 19, TypeScript — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**ToolGrid — Zero-Trust WASM Tool Suite**
- Built 15 client-side tools with zero server uploads: multi-threaded ffmpeg.wasm video compression, in-browser AI background removal, Tesseract OCR, a 4K device-mockup canvas engine, batch SVG vectorizer, lamejs audio encoding, and a Manifest V3 ad-blocker generator — all behind COOP/COEP + SharedArrayBuffer headers so WASM runs multi-threaded in the browser.
- Tech: Astro, Tailwind, WebAssembly, Canvas — github.com/Aryan-Protein-Vala/Micro-Tools

**FrameInGoa — Viral Edge Share Loop**
- Built the client-side generation pipeline: react-easy-crop 1:1 framing, HEIC decode, and canvas composition compressing generated avatars to ~30 KB WebP before any upload; then an edge share engine — Vercel Blob + KV at the edge, Satori-composed dynamic OG cards cached immutable on the CDN (zero compute after the first crawler hit) — with a "Generate Your ID" CTA under every shared card closing the viral loop.
- Tech: Next.js, Canvas API, Vercel Blob/KV, @vercel/og — github.com/Aryan-Protein-Vala/FrameInGoa
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
