# ARYAN SHARMA
**Voice AI & Real-Time Systems Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Voice AI and real-time systems engineer. Built VĀYU, a production-grade voice-first RAG system that answers in 0.8 ms P50 WebSocket round-trips against a 50–100 ms requirement — with speculative retrieval while the user is still speaking, barge-in cancellation, and per-stage latency telemetry on every hop. Deep experience with STT/TTS pipelines (Sarvam), LPU-accelerated LLM streaming, and the network-level fixes (TCP_NODELAY, Nagle, delayed ACK) that make voice feel instant. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Speech: Sarvam AI (saaras:v2 STT, bulbul:v2 TTS) · Web Speech API · buffered mic capture · partial transcripts · TTS streaming (WebSocket WAV)
- Real-Time: WebSockets · TCP_NODELAY/Nagle profiling · P50/P70/P100 latency telemetry · speculative retrieval · barge-in / generation cancellation · LRU caches
- RAG: FAISS (IndexFlatIP) · 9,000+ in-RAM vectors · TF-IDF (512-dim) · parent-child chunking · citation grounding
- LLM Serving: Groq LPU (llama3-8b) streaming · token-budget control · deterministic guardrails (<1 ms regex)
- Languages: Python · TypeScript · Rust · Go · SQL · Infra: FastAPI, Uvicorn, Next.js, Docker

## PROJECTS

**VĀYU — Ultra-Low-Latency Voice-Enabled RAG System**
- Beat a strict 50–100 ms end-to-end voice-answer requirement by ~99%: measured P50 0.8 ms, P70 1.5 ms, worst-case 1.6 ms client↔server WebSocket round-trips via a live 10-query audit harness.
- Root-caused and fixed a Nagle + delayed-ACK pathology — uvicorn's websockets path never set TCP_NODELAY, adding ~42 ms to every round trip — cutting WS latency from ~44 ms to ~1.5 ms (96% reduction); added per-stage telemetry (guardrail 0.005 ms → embed 0.51 ms → FAISS 0.017 ms → parent 0.009 ms → grounding 0.005 ms; 0.67 ms P50 retrieval).
- Designed the voice UX pipeline: Sarvam STT on buffered mic audio with browser partials for live transcripts, speculative background retrieval triggered by partials (candidates in RAM before speech ends), Groq Llama 3 streaming tokens, Sarvam TTS (speaker-selectable) streaming WAV back over WebSocket — with engine attribution (SARVAM vs BROWSER voice) in the answer meta.
- Built the robustness layer: barge-in (user speaks → backend cancels the in-flight generation task and resets state), compiled-regex injection/jailbreak guardrails executing concurrently with vector search, and an output grounding validator rejecting any citation not in retrieved context.
- Tech: Python, FastAPI, WebSockets, FAISS, Groq LPU, Sarvam AI, Next.js 16 — github.com/Aryan-Protein-Vala/vayu-voice-rag

**MYLO OS — Voice-First Desktop Operator (Tauri 2 / Rust)**
- Built the voice-trigger layer for a desktop OS agent: hold a global hotkey, speak the task, and a ghost cursor executes it across the OS — screen understanding via zero-latency Windows Graphics Capture / macOS Core Graphics at ~35 MB RSS.
- Engineered OS-level stealth (WDA_EXCLUDEFROMCAPTURE / NSWindow sharingType) so the agent's overlay is invisible during live calls and streams.
- Tech: Rust, Tauri 2, Windows Graphics Capture, Core Graphics — github.com/Aryan-Protein-Vala/MyloOS

**CLAIM/05 — Real-Time Multiplayer Sync Engine (Go + Redis)**
- Built a Go WebSocket engine (hub pattern, concurrent channel hubs) syncing a 5,000×5,000 (25M-cell) live battlefield: Redis SETNX atomic cell locks guarantee conflict-free ownership, and Pub/Sub delta fan-out reaches every connected client in sub-millisecond — the same real-time fabric voice UIs need.
- Added persistent player tokens (reload-safe reconnection) and a GitHub Actions 10-minute keep-alive keeping the 24/7 engine at zero cold starts.
- Tech: Go, Gorilla WebSockets, Redis Pub/Sub, Next.js 16 — github.com/Aryan-Protein-Vala/Grid-Game · live: multiplayer-grid-game-theta.vercel.app

**B1 Copilot — Streaming Analytics Copilot (SAP)**
- Built streaming token delivery from LLM-generated SQL answers over WebSockets, interleaved with live table and chart rendering as each query stage completes — partial results visible before generation finishes.
- Tech: Python, FastAPI, WebSockets, Next.js 16, SAP HANA — github.com/Aryan-Protein-Vala/Cira-RAG-agent

**CORTEX — Low-Latency Memory Injection (Rust)**
- Built the O(1) memory-packet injection path for voice/text AI sessions: graph+vector hybrid retrieval in Rust (SurrealDB + Qdrant) returning a hyper-dense context packet with flat token cost, plus gRPC (tonic) sync for multi-device memory continuity.
- Tech: Rust, SurrealDB, Qdrant, tonic/gRPC — github.com/Aryan-Protein-Vala/CORTEX

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Computer Networks, Operating Systems, Databases, Machine Learning, Data Structures & Algorithms
