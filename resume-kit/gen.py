#!/usr/bin/env python3
"""Generate one-page PDFs + standalone .tex files from the v2 markdown resumes."""
import os, re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

ACCENT = HexColor("#1a1a2e")
GREY = HexColor("#444444")
ROOT = os.path.dirname(__file__)

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(t):
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t

STYLES = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=18, leading=20, textColor=ACCENT, spaceAfter=0),
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=10.5, leading=12.5, textColor=black, spaceAfter=1),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8, leading=10, textColor=GREY, spaceAfter=0.5),
    "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=9.5, leading=11.5, textColor=ACCENT, spaceBefore=1, spaceAfter=1.5),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=8.3, leading=10.2, textColor=black, spaceAfter=1),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.3, leading=10.1, textColor=black, leftIndent=10, bulletIndent=1, spaceAfter=1),
}

def parse(md_text):
    lines = md_text.splitlines()
    items = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            items.append(("name", line[2:]))
            i += 1
            while i < n and not lines[i].strip():
                i += 1
            if i < n and lines[i].strip().startswith("**"):
                items.append(("title", lines[i].strip().strip("*")))
                i += 1
                while i < n and not lines[i].strip():
                    i += 1
                while i < n and lines[i].strip() and not lines[i].startswith("#"):
                    items.append(("contact", lines[i].strip()))
                    i += 1
            continue
        if line.startswith("## "):
            items.append(("section", line[3:].strip()))
            i += 1
            continue
        if line.startswith("- "):
            items.append(("bullet", line[2:]))
            i += 1
            continue
        items.append(("body", line))
        i += 1
    return items

def to_pdf(items, pdf_path):
    flow = []
    for kind, text in items:
        if kind == "name":
            flow.append(Paragraph(inline(text), STYLES["name"]))
            flow.append(Spacer(1, 2))
        elif kind == "title":
            flow.append(Paragraph(inline(text), STYLES["title"]))
        elif kind == "contact":
            flow.append(Paragraph(inline(text), STYLES["contact"]))
        elif kind == "section":
            flow.append(HRFlowable(width="100%", thickness=0.7, color=ACCENT, spaceBefore=3.5, spaceAfter=0))
            flow.append(Paragraph(inline(text), STYLES["section"]))
        elif kind == "body":
            flow.append(Paragraph(inline(text), STYLES["body"]))
        elif kind == "bullet":
            flow.append(Paragraph(inline(text), STYLES["bullet"], bulletText="•"))
    doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                            leftMargin=0.55*inch, rightMargin=0.55*inch,
                            topMargin=0.45*inch, bottomMargin=0.4*inch,
                            title=os.path.basename(pdf_path)[:-4], author="Aryan Sharma")
    doc.build(flow)
    with open(pdf_path, "rb") as f:
        data = f.read()
    return len(re.findall(rb"/Type\s*/Page[^s]", data))

def tex_escape(t):
    for a, b in [("\\", r"\\"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
                 ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"),
                 ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        t = t.replace(a, b)
    return t

def tex_inline(t):
    t = tex_escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
    t = t.replace("·", "\\,·\\,")
    t = t.replace("—", " --- ")
    return t

TEX_HEADER = r"""\documentclass[9pt]{article}
\usepackage[a4paper,margin=0.55in,top=0.5in,bottom=0.45in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[scaled=0.92]{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage[hidelinks]{hyperref}
\definecolor{accent}{HTML}{1A1A2E}
\definecolor{greyc}{HTML}{444444}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\titleformat{\section}{\normalfont\normalsize\bfseries\color{accent}}{}{0em}{}[{\color{accent}\titlerule[0.7pt]}]
\titlespacing*{\section}{0pt}{7pt}{2.5pt}
\begin{document}
"""

def to_tex(items, tex_path):
    out = [TEX_HEADER]
    in_items = False
    for kind, text in items:
        t = tex_inline(text)
        def close_items():
            nonlocal in_items
            if in_items:
                out.append("\\end{itemize}")
                in_items = False
        if kind == "name":
            close_items()
            out.append(f"\\noindent{{\\LARGE\\bfseries\\color{{accent}} {t}}}\\\\[3pt]")
        elif kind == "title":
            close_items()
            out.append(f"{{\\large\\bfseries {t}}}\\\\[3pt]")
        elif kind == "contact":
            close_items()
            out.append(f"{{\\small\\color{{greyc}} {t}}}\\vspace{{-2pt}}")
        elif kind == "section":
            close_items()
            out.append(f"\\section*{{{t}}}")
        elif kind == "body":
            close_items()
            out.append(t)
            out.append("\\vspace{1pt}")
        elif kind == "bullet":
            if not in_items:
                out.append("\\begin{itemize}[leftmargin=11pt,itemsep=0pt,topsep=1pt,parsep=0pt]")
                in_items = True
            out.append(f"\\item {t}")
    close_items()
    out.append("\\end{document}")
    open(tex_path, "w", encoding="utf-8").write("\n".join(out) + "\n")

def main():
    src = os.path.join(ROOT, "resumes")
    pdfd = os.path.join(ROOT, "pdf")
    texd = os.path.join(ROOT, "latex")
    os.makedirs(pdfd, exist_ok=True)
    os.makedirs(texd, exist_ok=True)
    bad = []
    for fn in sorted(os.listdir(src)):
        if not fn.endswith(".md"):
            continue
        items = parse(open(os.path.join(src, fn), encoding="utf-8").read())
        pdf_path = os.path.join(pdfd, fn[:-3] + ".pdf")
        pages = to_pdf(items, pdf_path)
        to_tex(items, os.path.join(texd, fn[:-3] + ".tex"))
        flag = "" if pages == 1 else f"  <-- {pages} PAGES"
        print(f"{fn:45s} {pages} page{flag}")
        if pages != 1:
            bad.append(fn)
    print("NEEDS TRIMMING:", bad if bad else "none")

if __name__ == "__main__":
    main()
