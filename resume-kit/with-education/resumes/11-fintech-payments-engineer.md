# ARYAN SHARMA
**Fintech & Payments Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Payments and fintech systems engineer: built the full money path for a two-sided SaaS marketplace (14 provider webhooks → atomic settlement RPC → 30-day escrow → UPI payouts), a prepaid-credit wallet for an AI platform, GST-compliant invoicing with gateway auto-reconciliation, and an offline P2P payment mesh where every transaction is E2E-encrypted and non-repudiable over Bluetooth. Obsessed with idempotency, replay defense, and reconciliation. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Payments: Razorpay (orders, webhooks, RazorpayX/UPI payouts, security deposits) · Stripe · PayPal · Gumroad · Cashfree · PhonePe · PayU · Instamojo · CCAvenue · Shopify · Lemon Squeezy · webhooks & provider event modeling
- Ledger & Settlement: atomic conversion/settlement RPCs · idempotent transaction keys · escrow & pending/withdrawable balances · recurring commission accounting · 30-day settlement holds · reconciliation crons · refund/chargeback handling
- Security: HMAC webhook verification · timing-safe comparisons · self-referral & velocity checks · replay defense (Bloom filters) · RLS · signed transactions (ECDSA)
- Fintech Domains: GST/HSN tax logic · GSTR-1/3B reporting · invoicing & dunning · wallet accounting · KYC-adjacent onboarding
- Languages: TypeScript · Python · Rust · Swift/Kotlin (payments SDKs) · PostgreSQL/Supabase, Firebase

## PROJECTS

**Black Index — Marketplace Money Path (31k+ LOC)**
- Built the settlement engine: HMAC-verified webhooks from 14 payment providers (Razorpay, Stripe, Gumroad, Lemon Squeezy, PayPal, Cashfree, PhonePe, PayU, Instamojo, CCAvenue, Shopify, Cal.com, +custom) feed an atomic record_conversion RPC — customer upsert, recurring-billing count, idempotent transaction insert, founder wallet debit, seller escrow credit, and platform-fee accounting (2–5% model) in one transaction.
- Implemented the risk controls: 30-day escrow hold, cron-driven release after refund/chargeback/dispute windows, reconciliation + wallet-check crons, self-referral detection, velocity limits, timing-safe secret comparison, server-side-only money operations, and RLS on every table; seller payouts via RazorpayX/UPI.
- Built founder-side money flows: security deposits, prepaid wallets, featured-listing payments, and upgrade verification — each with a separate verify endpoint.
- Tech: Next.js, Supabase/Postgres, Razorpay/Stripe, Zod — github.com/Aryan-Protein-Vala/Black-Index

**Astral — Offline P2P Payment Mesh over BLE**
- Built a payment mesh that works with zero connectivity: encrypted payment packets (200–500 B) exchange over BLE between phones and reconcile to a backend ledger when either device reconnects.
- Implemented the crypto that makes it non-repudiable: P-256 keypairs in iOS Secure Enclave / Android Keystore, Noise-protocol ECDH + HKDF-SHA256 key derivation, ChaCha20-Poly1305 AEAD payloads, ECDSA-SHA256 signature per transaction, and Bloom-filter deduplication of transaction hashes (not ciphertext) that blocks offline replay attacks.
- Solved the transport: dynamic GATT MTU negotiation to 512 B and sequential onCharacteristicWrite fragmentation with zero packet loss, plus cross-platform cipher parity between Apple CryptoKit and java.security.
- Tech: Rust, Swift, Kotlin, UniFFI, BLE/GATT, Noise Protocol — github.com/Aryan-Protein-Vala/Astral-Offline · github.com/Aryan-Protein-Vala/Astral-Network

**GSTGenius — GST-Compliant Billing Suite (live)**
- Built the tax engine: automatic CGST/SGST/IGST computation from HSN codes + transaction location, GST-compliant invoices with digital signatures and brand logos, and one-click GSTR-1 / GSTR-3B exports in CSV/Excel.
- Built the reconciliation loop: Razorpay/UPI/NetBanking payments auto-mark invoices Paid on gateway confirmation; recurring invoices (daily/weekly/monthly) with WhatsApp + email dunning via Cloud Functions; CA portal managing unlimited clients with shared access — live at gstgenius-6f0d0.web.app.
- Tech: Next.js 15, Firebase, Razorpay, jsPDF — github.com/Aryan-Protein-Vala/GSTGenius

**Council — Prepaid Credit Wallet for AI**
- Built the wallet backend: integer-credit ledger with typed transactions (deposit/usage/refund/bonus), Razorpay UPI top-ups with webhook-verified settlement, balance/transaction APIs, and tier gating that controls limits without recurring billing.
- Tech: Next.js, Supabase, Clerk, Razorpay — github.com/Aryan-Protein-Vala/multi-model

**Snag — Desktop App Billing & Licensing**
- Built the monetization stack for a native macOS app: Next.js + Supabase backend, Razorpay & PayPal webhook billing, hardware-UUID license binding with a 16-character key activation flow, and a one-line curl installer.
- Tech: Python (PyQt6), Next.js, Supabase, Razorpay/PayPal — github.com/Aryan-Protein-Vala/Snag

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Data Structures & Algorithms, Databases, Operating Systems, Computer Networks
