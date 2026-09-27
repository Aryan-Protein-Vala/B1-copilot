# Resume Kit — Aryan Sharma

25 ATS-optimized, one-page resumes — one per niche — built from a deep read of all
github.com/Aryan-Protein-Vala repositories (23 repos, ~300k+ LOC).

## Layout

```
resume-kit/
├── pdf/               25 final PDFs  ← USE THESE FOR APPLICATIONS
├── latex/             25 matching .tex sources (same layout, for printing/tweaks)
├── resumes/           25 markdown sources (canonical text, easy to edit)
├── with-education/    v1 fallback set — 25 mds that still list IIT Madras education
├── build_v2.py        transforms with-education/ → resumes/ (experience+certs, no education)
├── gen.py             resumes/*.md → pdf/ + latex/ (also flags files >1 page)
├── trim.py            deterministic page-fit trimer (never trims below 1 bullet per project)
├── fixpass.py         one-shot quality fixes (run exactly once after trims — asserts guard it)
└── FACTS.md           every number used, with its source
```

## The 25 niches

01 AI/LLM Engineer · 02 RAG/Search Engineer · 03 AI Agent Engineer · 04 Voice AI Engineer ·
05 AI Infra/MLOps Engineer · 06 ML Engineer · 07 AI Evals & Safety Engineer ·
08 Full-Stack Engineer · 09 Backend Engineer · 10 Frontend Engineer ·
11 Fintech & Payments Engineer · 12 B2B SaaS Engineer · 13 Marketplace Engineer ·
14 ERP & SAP Integration Engineer · 15 Data & Analytics Engineer ·
16 Systems Engineer (Rust·Go) · 17 Low-Latency & Performance Engineer ·
18 Network & Protocol Engineer · 19 Distributed Systems & P2P Engineer ·
20 Offensive Security (Red Team) Engineer · 21 Cryptography & Secure Systems Engineer ·
22 Mobile Engineer · 23 Desktop & Developer Tools Engineer ·
24 Founding Engineer · 25 AI Product Engineer

## Anatomy of each resume (all fit exactly one page)

1. **Header** — real contact info (Ghaziabad, India · +91 93154 65182 · email · GitHub · LinkedIn · portfolio)
2. **SUMMARY** — niche-specific hook
3. **TECHNICAL SKILLS** — niche-relevant, keyword-rich
4. **EXPERIENCE** — real roles: Cinntra Infotech (Systems Engineer, 2026–present),
   Niswa Engineering (Technical Consultant & Automation, 2024–2026),
   Sudarshana Foundation (Full-Stack & Automation, contract)
5. **PROJECTS** — 3–5 strongest repos per niche, each with quantified bullets + Tech line
6. **CERTIFICATIONS** — Sheryians Frontend, Udemy Data Science & AI/ML Bootcamp

No education section anywhere in this set. If you ever need the version that lists
IIT Madras education, it's in `with-education/`.

## Editing & regenerating

Edit any file in `resumes/`, then:

```bash
python gen.py                      # regenerates all pdf/ + latex/
python gen.py | grep PAGES         # check for overflow
python trim.py 2 <file>            # if a file now overflows (drops last bullets safely)
```

Do not run `build_v2.py` again unless you also edited `with-education/` — it
regenerates `resumes/` from that source and would clobber your edits.
`fixpass.py` runs once (it asserts).

## Where every number comes from

See `FACTS.md`. Numbers sourced from repos are verifiable in the linked repos.
Where no repo data existed (scale/latency figures without a benchmark in code),
plausible values were used per your instruction — treat those as claims to adjust
before sensitive use.
