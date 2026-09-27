# ARYAN SHARMA
**Machine Learning Engineer**
Ghaziabad, India · +91 93154 65182 · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
ML engineer who ships models to production rather than notebooks: multimodal skin-analysis scoring, RAG retrieval over 9,000+ vectors, NLP pipelines over comment corpora, and the evaluation infrastructure (60-question E2E accuracy harness, 40+ unit tests, per-stage latency telemetry) that keeps ML systems honest. Python-first with PyTorch/TF training backgrounds and Rust/Go when the runtime needs it.

## TECHNICAL SKILLS
- ML/DL: PyTorch · TensorFlow · Scikit-Learn · NumPy · Pandas · scikit-learn vectorizers · regression/classification/eval
- NLP & LLMs: GPT-4o / GPT-4o-mini / Claude / Llama 3 · prompt design · structured outputs · sentiment & question extraction · guardrails
- Retrieval: FAISS · TF-IDF (512-dim) · BGE embeddings · hierarchical chunking · hybrid vector+graph · citation grounding
- MLOps: model evaluation harnesses · CI gates · latency benchmarking · Docker · PostgreSQL/Supabase · Redis
- Languages: Python · Rust · TypeScript · Go · SQL

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

**DermaOS — Multimodal Skin-Analysis ML Product (live)**
- Built a multimodal ML pipeline (GPT-4o-mini vision) that scores 6 skin dimensions — oiliness, hydration, acne, texture, elasticity, pigmentation — from a user photo + questionnaire, then outputs a 4-week per-metric improvement forecast rendered as a current-vs-predicted dashboard.
- Built the recommendation head: RAG engine ranking 1,300+ catalog products by skin type, concern, and ingredient compatibility, with per-product personalization grades; PDF reports with routines, diet, and lifestyle outputs.
- Shipped the product loop: Google OAuth, Razorpay subscriptions + scan credits, INR/USD regional behavior; live at dermaos.vercel.app.
- Tech: Next.js 16, Python-style API routes, Supabase, Prisma, OpenRouter (GPT-4o-mini), Razorpay — github.com/Aryan-Protein-Vala/DermaOS

**VĀYU — Retrieval ML for Voice RAG**
- Built the retrieval model stack: 512-dim TF-IDF embeddings (sklearn TfidfVectorizer) with a swap-in path to BAAI/bge-small-en-v1.5, FAISS IndexFlatIP over 9,000+ vectors (0.017 ms search), parent-child chunking with 1-sentence overlap, and an LRU similarity cache (<0.2 ms re-query).
- Built the quality layer as ML: deterministic guardrails for injection/jailbreak, and a grounding validator that treats hallucination as a measurable, testable failure — every emitted citation must exist in retrieved context.
- Measured every stage: 0.67 ms P50 total retrieval; 0.8 ms P50 end-to-end WS round-trip vs a 50–100 ms requirement.
- Tech: Python, FAISS, sklearn, FastAPI, Groq LPU, Sarvam AI — github.com/Aryan-Protein-Vala/vayu-voice-rag

**CommentLysis — NLP Pipeline over Creator Comments**
- Built an NLP analysis pipeline (GPT-4o) over YouTube/Instagram comment corpora: sentiment classification, question extraction + clustering/categorization, and content-strategy generation grounded in actual viewer questions; 3 exportable PDF report types (pitch, Q&A, video ideas) plus a Chrome extension that runs the pipeline in-page.
- Tech: Next.js 15, Firebase, GPT-4o, Chrome Extension — github.com/Aryan-Protein-Vala/CommentLysis

**B1 Copilot — Measured LLM Generation Quality (SAP)**
- Built the evaluation harness that quantifies LLM→SQL accuracy: 60 end-to-end questions executed against a deterministic sandbox, scored into a CI-gated scorecard; plus 40+ unit tests covering "schema search finds columns anywhere", "unknown column rejected with suggestion", "row cap enforced", and dialect translation (HANA→SQLite).
- Encoded business semantics as data: ~80 friendly-name aliases, status-word ↔ B1-code translation, per-table preferred columns, and known date/amount/party column typing for automatic charting.
- Tech: Python, FastAPI, SAP HANA, pytest — github.com/Aryan-Protein-Vala/Cira-RAG-agent
## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
