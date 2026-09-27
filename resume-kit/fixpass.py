#!/usr/bin/env python3
"""Targeted quality fixes after mechanical trimming."""
import os, re

DST = os.path.join(os.path.dirname(__file__), "resumes")

def fix(fn, old, new):
    path = os.path.join(DST, fn)
    text = open(path, encoding="utf-8").read()
    assert old in text, f"{fn}: pattern not found: {old[:60]}..."
    open(path, "w", encoding="utf-8").write(text.replace(old, new, 1))
    print(f"fixed {fn}: {old[:45]}...")

def block(fn, header):
    text = open(os.path.join(DST, fn), encoding="utf-8").read()
    m = re.search(r"^\*\*" + re.escape(header) + r".*?(?=^\*\*|^## )", text, flags=re.M | re.S)
    assert m, f"{fn}: header not found: {header}"
    return m.group(0)

# 1. double periods from summary rewrite (all files)
for fn in sorted(os.listdir(DST)):
    if not fn.endswith(".md"):
        continue
    path = os.path.join(DST, fn)
    text = open(path, encoding="utf-8").read()
    if ".." in text:
        open(path, "w", encoding="utf-8").write(text.replace("..", "."))
        print(f"double-period fixed: {fn}")

# 2. stale badge claims
fix("09-backend-engineer.md",
    "5,000+ concurrent AI requests served across self-hosted systems; 96% WebSocket latency reduction from a single root-caused fix.",
    "Production systems handling 5,000+ monthly transactions; 96% WebSocket latency reduction from a single root-caused fix.")

fix("05-ai-infra-mlops-engineer.md",
    "5,000+ concurrent AI requests served across self-hosted systems; 80% of test pipeline automated.",
    "a deterministic offline SAP sandbox that runs LLM CI with zero network or API cost (40+ unit tests + 60-question accuracy harness, all CI-gated).")

# 3. restore one real bullet to key Tech-only projects
fix("02-rag-search-engineer.md",
    "**DermaOS — AI Skin Analysis & Product RAG Marketplace**\n- Tech:",
    "**DermaOS — AI Skin Analysis & Product RAG Marketplace**\n- Built the RAG recommendation head ranking 1,300+ catalog products against a 6-dimension skin profile by skin type, concern, and ingredient compatibility, with a personalized grade per product card.\n- Tech:")

fix("04-voice-ai-engineer.md",
    "**B1 Copilot — Streaming Analytics Copilot (SAP)**\n- Tech:",
    "**B1 Copilot — Streaming Analytics Copilot (SAP)**\n- Built streaming token delivery of LLM-generated SQL answers over WebSockets, interleaved with live table and chart rendering as each query stage completes — partial results visible before generation finishes.\n- Tech:")

fix("09-backend-engineer.md",
    "**GSTGenius — Serverless Billing & Compliance Backend**\n- Tech:",
    "**GSTGenius — Serverless Billing & Compliance Backend**\n- Built the Firebase Cloud Functions backend: recurring invoices (daily/weekly/monthly), automated WhatsApp + email payment reminders, GST tax computation (CGST/SGST/IGST from HSN + location), GSTR-1/GSTR-3B report generation, and gateway auto-reconciliation marking invoices Paid on confirmation.\n- Tech:")
fix("09-backend-engineer.md", block("09-backend-engineer.md", "Council — Prepaid Credit Wallet Backend"), "")

fix("11-fintech-payments-engineer.md",
    "**Council — Prepaid Credit Wallet for AI**\n- Tech:",
    "**Council — Prepaid Credit Wallet for AI**\n- Built the wallet backend: integer-credit ledger with typed transactions (deposit/usage/refund/bonus), Razorpay UPI top-ups with webhook-verified settlement, and tier gating that controls limits without recurring billing.\n- Tech:")

fix("18-network-protocol-engineer.md",
    "**VĀYU — WebSocket Latency Protocol Tuning**\n- Tech:",
    "**VĀYU — WebSocket Latency Protocol Tuning**\n- Profiled a production WebSocket path and found the protocol-level bug: missing TCP_NODELAY on uvicorn's websockets path let Nagle + delayed ACK add ~42 ms per round trip — fixed at the socket layer and verified 44 ms → 1.5 ms (96% reduction) with a scripted 10-query audit harness.\n- Tech:")

fix("20-offensive-security-red-team.md",
    "**B1 Copilot — Injection-Proof Data Access (Defensive Test Suite)**\n- Tech:",
    "**B1 Copilot — Injection-Proof Data Access (Defensive Test Suite)**\n- Built the guard layer an attacker's tests target: SELECT/WITH-only enforcement, DDL/DML/CALL rejection inside sub-queries, live-catalog identifier validation, parameter binding — with adversarial unit tests (raw SQL write blocked, forged/tampered/expired token rejected, cross-employee session hijack blocked).\n- Tech:")
fix("20-offensive-security-red-team.md", block("20-offensive-security-red-team.md", "VĀYU — LLM Guardrail Validation in Production"), "")
fix("20-offensive-security-red-team.md", block("20-offensive-security-red-team.md", "Black Index — Money-Path Adversarial Tests"), "")

fix("21-cryptography-secure-systems.md",
    "**B1 Copilot — Auth & Integrity for an Enterprise Copilot**\n- Tech:",
    "**B1 Copilot — Auth & Integrity for an Enterprise Copilot**\n- Built the security test matrix for an app holding customer ERP access: forged-unsigned, tampered, and expired token rejection; cross-employee session-hijack blocking; read-only technical DB user and SELECT-only guarded SQL as defense-in-depth.\n- Tech:")
fix("21-cryptography-secure-systems.md", block("21-cryptography-secure-systems.md", "MYLO OS — Keys That Never Touch the Client"), "")
fix("21-cryptography-secure-systems.md", block("21-cryptography-secure-systems.md", "Prometheus — Air-Gapped by Design (live)"), "")

# 4. restore 23's trimmed bullets
for header, bullet in [
    ("CORTEX — Desktop Memory App + MCP Server",
     "- Built the Tauri desktop surface: live 3D WebGL memory graph (nodes pulse on access, dim as they decay) plus an MCP server so any MCP-capable editor/agent reads the same memory — Docker Compose distribution for the SurrealDB/Qdrant/Redis stack.\n- Tech:"),
    ("ToolGrid — 15-Tool Browser WASM Toolkit",
     "- Built 15 pro tools that run 100% client-side with zero uploads: multi-threaded ffmpeg.wasm video compression, in-browser AI background removal, Tesseract OCR, 4K mockup canvas, batch SVG vectorizer, and a Manifest V3 ad-blocker generator — behind COOP/COEP + SharedArrayBuffer.\n- Tech:"),
    ("Prometheus — Offline OS Cleaner + Fleet Console (live)",
     "- Built a 100% offline, zero-telemetry Rust TUI: deep-flush scans finding hidden caches, phantom duplicates, and ad-trackers across thousands of files in milliseconds; HWID-bound licensing; centralized Enterprise Fleet Command Center; one-line curl installer — live at prometheus-cleaner.vercel.app.\n- Tech:"),
]:
    path = os.path.join(DST, "23-desktop-devtools-engineer.md")
    text = open(path, encoding="utf-8").read()
    pat = "**" + header + "**\n- Tech:"
    if pat in text:
        text = text.replace(pat, "**" + header + "**\n" + bullet, 1)
        open(path, "w", encoding="utf-8").write(text)
        print(f"23: restored bullet for {header}")

print("ALL DONE")
