#!/usr/bin/env python3
"""One-shot: transform v1 (with-education) resumes into v2 (experience-first, no education, +certs)."""
import os, re

SRC = os.path.join(os.path.dirname(__file__), "with-education", "resumes")
DST = os.path.join(os.path.dirname(__file__), "resumes")
os.makedirs(DST, exist_ok=True)

EXPERIENCE = """## EXPERIENCE
**Cinntra Infotech — Systems Engineer** · 2026 – Present
- Built CIRA, a RAG agent translating natural-language requests into audited SAP HANA queries and write operations, giving non-technical users direct access to enterprise data
- Built the point-of-sale system backend: transaction recording, merchant reconciliation, and offline synchronization

**Niswa Engineering — Technical Consultant & Automation Engineer** · 2024 – 2026
- Built asynchronous AI agents (TypeScript) that automated 80%+ of a content generation and scheduling pipeline
- Built the company website in Astro (95+ Google Lighthouse score); set up cloud infrastructure, API integrations, and event-driven automation workflows

**Sudarshana Foundation — Full-Stack & Automation Engineer** · Contract
- Designed and built the organization's first centralized web platform, digitizing paper-based workflows into software
- Built database systems handling 5,000+ monthly transactions

"""

CERTS = """## CERTIFICATIONS
- Frontend Development Certification — Sheryians Coding School
- Data Science & AI/ML Bootcamp Certification — Udemy
"""

def transform(md: str) -> str:
    md = md.replace("Chennai, India · +91 98XXX XXXXX", "Ghaziabad, India · +91 93154 65182")
    md = md.replace(" IIT Madras, BSc Data Science & Programming.", ".")
    md = md.replace("(IIT Madras, BSc Data Science & Programming) ", "")
    m = re.search(r"^## (PROJECTS|SELECTED SHIPPED PRODUCTS)\s*$", md, flags=re.M)
    if not m:
        raise ValueError("no projects section found")
    idx = m.start()
    md = md[:idx] + EXPERIENCE + md[idx:]
    md = re.sub(r"## EDUCATION\n.*", "", md, flags=re.S).rstrip()
    md = md + "\n\n" + CERTS
    return md

for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".md"):
        continue
    text = open(os.path.join(SRC, fn), encoding="utf-8").read()
    out = transform(text)
    assert "IIT" not in out, f"IIT still present in {fn}"
    assert "Ghaziabad" in out and "93154" in out, f"header not updated in {fn}"
    assert "## EXPERIENCE" in out and "## CERTIFICATIONS" in out, f"sections missing in {fn}"
    open(os.path.join(DST, fn), "w", encoding="utf-8").write(out)
    print(f"transformed {fn}")
print("done")
