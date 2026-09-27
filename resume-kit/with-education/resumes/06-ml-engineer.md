# ARYAN SHARMA
**Machine Learning Engineer**
Chennai, India · +91 98XXX XXXXX · aryansharma24112003@gmail.com
github.com/Aryan-Protein-Vala · linkedin.com/in/aryannnn · aryannnn-portfolio.vercel.app

## SUMMARY
ML engineer (IIT Madras, BSc Data Science & Programming) who ships models to production rather than notebooks: multimodal skin-analysis scoring, RAG retrieval over 9,000+ vectors, NLP pipelines over comment corpora, and the evaluation infrastructure (60-question E2E accuracy harness, 40+ unit tests, per-stage latency telemetry) that keeps ML systems honest. Python-first with PyTorch/TF training backgrounds and Rust/Go when the runtime needs it.

## TECHNICAL SKILLS
- ML/DL: PyTorch · TensorFlow · Scikit-Learn · NumPy · Pandas · scikit-learn vectorizers · regression/classification/eval
- NLP & LLMs: GPT-4o / GPT-4o-mini / Claude / Llama 3 · prompt design · structured outputs · sentiment & question extraction · guardrails
- Retrieval: FAISS · TF-IDF (512-dim) · BGE embeddings · hierarchical chunking · hybrid vector+graph · citation grounding
- MLOps: model evaluation harnesses · CI gates · latency benchmarking · Docker · PostgreSQL/Supabase · Redis
- Languages: Python · Rust · TypeScript · Go · SQL

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

**GSTGenius — Financial Analytics & Compliance Engine (live)**
- Built the analytics layer: real-time P&L and balance-sheet computation, revenue trend analysis, and one-click GSTR-1 / GSTR-3B report generation from transactional data; GST tax logic computing CGST/SGST/IGST from HSN codes + location.
- Tech: Next.js 15, Firebase, Chart.js, Recharts — github.com/Aryan-Protein-Vala/GSTGenius · live: gstgenius-6f0d0.web.app

## EDUCATION
**Indian Institute of Technology Madras (IITM)**
BSc Data Science & Programming · 2023 – Present (expected 2027)
Core coursework: Machine Learning, Data Structures & Algorithms, Databases, Linear Algebra, Probability & Statistics
