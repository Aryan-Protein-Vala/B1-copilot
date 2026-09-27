#!/usr/bin/env python3
"""Trim v2 resumes to one page.
mode 1: drop the LAST project block (least relevant for that niche)
mode 2: drop the last bullet of each remaining project (at most 1 per project; keeps the Tech line)
"""
import os, re, sys

ROOT = os.path.dirname(__file__)
DST = os.path.join(ROOT, "resumes")

def projects_range(lines):
    start = None
    for i, ln in enumerate(lines):
        if re.match(r"^## (PROJECTS|SELECTED SHIPPED PRODUCTS)\s*$", ln):
            start = i + 1
    end = None
    for i, ln in enumerate(lines):
        if ln.startswith("## CERTIFICATIONS"):
            end = i
    return start, end

def drop_last_project(lines):
    s, e = projects_range(lines)
    headers = [i for i in range(s, e) if lines[i].startswith("**") and not lines[i].startswith("- ")]
    if not headers:
        return lines, False
    last = headers[-1]
    cut = last
    while cut > s and not lines[cut-1].strip():
        cut -= 1
    new = lines[:cut] + lines[e:]
    while len(new) > 2 and not new[-2].strip() and not new[-3].strip():
        new = new[:-2] + new[-1:]
    return new, True

def drop_last_bullets(lines):
    s, e = projects_range(lines)
    headers = [i for i in range(s, e) if lines[i].startswith("**") and not lines[i].startswith("- ")]
    headers.append(e)
    removed = 0
    for a, b in list(zip(headers, headers[1:]))[::-1]:
        bullets = [i for i in range(a + 1, b) if lines[i].startswith("- ")]
        if bullets and len(bullets) > 1:
            i = bullets[-1]
            if "Tech:" in lines[i]:
                i = bullets[-2]
            del lines[i]
            removed += 1
    return lines, removed

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "1"
    files = sys.argv[2:] if len(sys.argv) > 2 else None
    for fn in sorted(os.listdir(DST)):
        if not fn.endswith(".md"):
            continue
        if files and fn not in files:
            continue
        path = os.path.join(DST, fn)
        lines = open(path, encoding="utf-8").read().splitlines()
        if mode == "1":
            new, changed = drop_last_project(lines)
            if changed:
                open(path, "w", encoding="utf-8").write("\n".join(new) + "\n")
                print(f"{fn}: dropped last project")
        else:
            new, removed = drop_last_bullets(lines)
            if removed:
                open(path, "w", encoding="utf-8").write("\n".join(new) + "\n")
                print(f"{fn}: dropped {removed} bullets")

if __name__ == "__main__":
    main()
