# ARYAN SHARMA
**Marketplace & Two-Sided Platform Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
Two-sided platform engineer: built the matching, attribution, trust, and settlement layers for a SaaS affiliate marketplace (founders ↔ sellers), a verified social-activity marketplace with trust scores, and a skincare marketplace where an AI RAG engine is the matching engine over 1,300+ products. Deep in referral attribution, anti-fraud rails, escrow, and liquidity-side UX. IIT Madras, BSc Data Science & Programming.

## TECHNICAL SKILLS
- Marketplace Mechanics: two-sided matching · referral-link attribution & tracking · commission models (upfront + recurring) · escrow & settlement · payouts · demand/supply dashboards
- Trust & Safety: ID + trust-score verification · self-referral detection · velocity/fraud checks · content moderation · dispute workflows with SLAs
- Payments: Razorpay/RazorpayX/UPI · Stripe · PayPal · 14-provider webhook ingestion · idempotent settlement
- Product: Next.js (App Router, Server Actions) · Supabase (Postgres, RLS, realtime) · Tailwind · Framer Motion · Vercel Edge (ap-south-1)
- Languages: TypeScript · Python · SQL · Rust (engine work)

## PROJECTS

**Black Index — Affiliate Marketplace for Indian SaaS (31k+ LOC)**
- Designed the full two-sided flow: founders list products with hybrid commission config (upfront % + recurring % + max recurring months); sellers ("Warlords") browse the marketplace, generate product-specific tracked referral links, and earn on webhook-verified conversions.
- Built the attribution + settlement engine: referral endpoints associating traffic with seller+product, HMAC-verified provider webhooks from 14 payment providers feeding an atomic record_conversion RPC (customer upsert, recurring count, idempotent insert, founder debit, seller escrow credit, platform fee), and a 30-day escrow hold → withdrawable → RazorpayX/UPI payout pipeline.
- Built the trust layer: self-referral detection, velocity limits, fraud-report API with dispute evidence upload, blacklist admin tooling, and a dispute SLA cron; seller dashboards for links, transactions, earnings, and pending/withdrawable balances.
- Tech: Next.js, Supabase (RLS), Razorpay/Stripe, Zod — github.com/Aryan-Protein-Vala/Black-Index

**PlusOne — Verified Social-Activity Marketplace (live)**
- Built the marketplace loop for real-life activities: post a plan with an optional reward, or host an offer at your own ₹/hour rate; instant real-time chat opens on booking confirmation; city + category discovery (Mumbai, Delhi, Bangalore; coffee, movies, study, gaming, travel).
- Designed the trust system: ID verification + trust-score badges, automated prohibited-content moderation, and public-venue-only safety policies — the difference between a demo and something people meet up on.
- Deployed edge-serverless in ap-south-1 (Mumbai) for India-first latency; live at findyour-plusone.vercel.app.
- Tech: Next.js 15, Supabase (Auth SSR, RLS), Tailwind v4 — github.com/Aryan-Protein-Vala/PlusOne

**DermaOS — AI-Matched Product Marketplace (live)**
- Built the matching engine for a consumer goods marketplace: an RAG recommendation layer ranking 1,300+ products by skin type, concern, and ingredient compatibility, with personalized grades per product card, marketplace filters, and a 4-week outcome forecast that de-risks first purchase.
- Built the monetization loop: freemium scan credits, Razorpay subscriptions, INR/USD regional availability — live at dermaos.vercel.app.
- Tech: Next.js 16, Supabase, Prisma, OpenRouter, Razorpay — github.com/Aryan-Protein-Vala/DermaOS

**GSTGenius — CA-Client Marketplace of Services (live)**
- Built the CA portal: one Chartered Accountant onboards and manages unlimited client businesses with shared access and per-client workspaces — a service marketplace where the CA is the seller and compliance automation is the product.
- Tech: Next.js 15, Firebase, Razorpay — github.com/Aryan-Protein-Vala/GSTGenius

**FrameInGoa — Supply-Side Viral Acquisition**
- Designed a viral loop as a growth engine for a community platform: client-side ID generation → 30 KB WebP upload → Satori-composed OG cards with a "Generate Your ID" CTA under every shared card — turning every share into an acquisition funnel at near-zero infra cost.
- Tech: Next.js, Vercel Blob/KV, Satori — github.com/Aryan-Protein-Vala/FrameInGoa

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Data Structures & Algorithms, Databases, Operating Systems, Computer Networks
