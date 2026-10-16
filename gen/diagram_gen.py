"""In-article SVG diagram generator for Solved Sindh Textbook Board Books blog articles.

Diagram specs (from batch files) look like:
  {"kind": "flowchart", "title": "...", "items": [{"label": "...", "sub": "..."}, ...]}
  {"kind": "timeline",  "title": "...", "items": [{"label": "...", "text": "..."}, ...]}
  {"kind": "concept",   "title": "...", "center": "...", "branches": [{"label": "...", "text": "..."}, ...]}
  {"kind": "compare",   "title": "...", "left": "...", "right": "...",
   "rows": [{"left": "...", "right": "..."}, ...]}
  {"kind": "labelled",  "title": "...", "center": "...", "parts": [{"label": "...", "text": "..."}, ...]}

All diagrams visualise the article's OWN method/structure/process — never
fabricated statistics, exam dates, or board data. Numbers appear only if the
article itself states them (e.g. step counts, revision-day counts).
"""
import html as htmlmod
import os
import textwrap

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAG_DIR = os.path.join(SITE_DIR, "assets", "images", "blog", "diagrams")

GREEN = "#0B6B4A"
GREEN_LT = "#E7F4EC"
AMBER = "#F59E0B"
INK = "#1F2937"
MUTED = "#6B7280"
LINE = "#D1D5DB"
W = 1000


def _esc(s):
    return htmlmod.escape(str(s or ""))


def _wrap(text, width, size=22):
    return textwrap.wrap(str(text or ""), width=width) or [""]


def _text_lines(lines, x, y, size=22, fill=INK, anchor="start", weight="normal"):
    out = []
    for ln in lines:
        out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" '
                   f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{_esc(ln)}</text>')
        y += size + 8
    return "\n".join(out), y


def _title_block(title, width=W):
    lines = _wrap(title, 52, 28)
    els, y = _text_lines(lines, 40, 58, size=28, weight="bold", fill=GREEN)
    return els, y + 14


def _svg(body, height):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" '
            f'viewBox="0 0 {W} {height}">\n<rect width="{W}" height="{height}" rx="16" fill="#FFFFFF" '
            f'stroke="{LINE}"/>\n{body}\n</svg>\n')


def _flowchart(spec):
    title_els, y = _title_block(spec["title"])
    parts = [title_els]
    cy = y
    for i, it in enumerate(spec["items"]):
        box_h = 30 + 30 * max(1, len(_wrap(it.get("sub", ""), 62)))
        parts.append(f'<rect x="140" y="{cy}" width="720" height="{box_h + 34}" rx="12" '
                     f'fill="{GREEN_LT}" stroke="{GREEN}" stroke-width="2"/>')
        label, cy2 = _text_lines(_wrap(it["label"], 58), 500, cy + 32, size=24, weight="bold",
                                 fill=GREEN, anchor="middle")
        parts.append(label)
        if it.get("sub"):
            sub, _ = _text_lines(_wrap(it["sub"], 62), 500, cy2 + 2, size=20, fill=MUTED,
                                 anchor="middle")
            parts.append(sub)
        cy += box_h + 34
        if i < len(spec["items"]) - 1:
            parts.append(f'<polygon points="500,{cy + 4} 486,{cy + 26} 514,{cy + 26}" fill="{AMBER}"/>')
            cy += 34
    return _svg("\n".join(parts), cy + 30)


def _timeline(spec):
    title_els, y = _title_block(spec["title"])
    parts = [title_els]
    parts.append(f'<line x1="70" y1="{y}" x2="70" y2="{y + len(spec["items"]) * 92}" stroke="{GREEN}" stroke-width="4"/>')
    cy = y + 10
    for it in spec["items"]:
        parts.append(f'<circle cx="70" cy="{cy + 12}" r="11" fill="{AMBER}" stroke="{GREEN}" stroke-width="2"/>')
        label, _ = _text_lines(_wrap(it["label"], 40), 110, cy + 20, size=24, weight="bold", fill=INK)
        parts.append(label)
        if it.get("text"):
            sub, _ = _text_lines(_wrap(it["text"], 62), 110, cy + 48, size=20, fill=MUTED)
            parts.append(sub)
        cy += 92
    return _svg("\n".join(parts), cy + 24)


def _concept(spec):
    title_els, y = _title_block(spec["title"])
    parts = [title_els]
    branches = spec["branches"]
    # Center box
    parts.append(f'<rect x="350" y="{y + 120}" width="300" height="76" rx="14" fill="{GREEN}"/>')
    center, _ = _text_lines(_wrap(spec["center"], 24), 500, y + 156, size=24, weight="bold",
                            fill="#FFFFFF", anchor="middle")
    parts.append(center)
    # Branch boxes: 2 columns around the center
    positions = [(60, y + 20), (700, y + 20), (60, y + 240), (700, y + 240),
                 (60, y + 460), (700, y + 460)]
    for i, b in enumerate(branches[:6]):
        bx, by = positions[i]
        lines = _wrap(b.get("text", ""), 26)
        bh = 52 + 28 * len(lines)
        parts.append(f'<line x1="{bx + 120}" y1="{by + bh}" x2="500" y2="{y + 158}" stroke="{LINE}" stroke-width="2"/>')
        parts.append(f'<rect x="{bx}" y="{by}" width="240" height="{bh}" rx="12" fill="{GREEN_LT}" stroke="{GREEN}"/>')
        lab, _ = _text_lines(_wrap(b["label"], 26), bx + 120, by + 30, size=22, weight="bold",
                             fill=GREEN, anchor="middle")
        parts.append(lab)
        if lines:
            sub, _ = _text_lines(lines, bx + 120, by + 58, size=19, fill=MUTED, anchor="middle")
            parts.append(sub)
    height = y + 460 + 130
    return _svg("\n".join(parts), height)


def _compare(spec):
    title_els, y = _title_block(spec["title"])
    parts = [title_els]
    # Header row
    parts.append(f'<rect x="40" y="{y}" width="440" height="52" rx="8" fill="{GREEN}"/>')
    parts.append(f'<rect x="520" y="{y}" width="440" height="52" rx="8" fill="{AMBER}"/>')
    lh, _ = _text_lines(_wrap(spec["left"], 30), 260, y + 34, size=22, weight="bold",
                        fill="#FFFFFF", anchor="middle")
    rh, _ = _text_lines(_wrap(spec["right"], 30), 740, y + 34, size=22, weight="bold",
                        fill=INK, anchor="middle")
    parts += [lh, rh]
    cy = y + 52
    for i, row in enumerate(spec["rows"]):
        llen = max(1, len(_wrap(row["left"], 34)))
        rlen = max(1, len(_wrap(row["right"], 34)))
        rhgt = 26 + 28 * max(llen, rlen)
        bg = "#F7FAF8" if i % 2 == 0 else "#FFFFFF"
        parts.append(f'<rect x="40" y="{cy}" width="920" height="{rhgt}" fill="{bg}" stroke="{LINE}"/>')
        lt, _ = _text_lines(_wrap(row["left"], 34), 60, cy + 30, size=20)
        rt, _ = _text_lines(_wrap(row["right"], 34), 540, cy + 30, size=20)
        parts += [lt, rt]
        cy += rhgt
    return _svg("\n".join(parts), cy + 20)


def _labelled(spec):
    title_els, y = _title_block(spec["title"])
    parts = [title_els]
    # Center circle
    parts.append(f'<circle cx="500" cy="{y + 130}" r="95" fill="{GREEN_LT}" stroke="{GREEN}" stroke-width="3"/>')
    center, _ = _text_lines(_wrap(spec["center"], 14), 500, y + 124, size=24, weight="bold",
                            fill=GREEN, anchor="middle")
    parts.append(center)
    n = len(spec["parts"])
    for i, p in enumerate(spec["parts"]):
        # alternate left / right callouts
        side_left = (i % 2 == 0)
        bx = 60 if side_left else 640
        by = y + 20 + (i // 2) * 150
        lines = _wrap(p.get("text", ""), 30)
        bh = 52 + 28 * len(lines)
        parts.append(f'<line x1="{bx + 300 if side_left else bx}" y1="{by + bh // 2}" '
                     f'x2="{405 if side_left else 595}" y2="{y + 130}" stroke="{LINE}" stroke-width="2"/>')
        parts.append(f'<rect x="{bx}" y="{by}" width="300" height="{bh}" rx="12" fill="#FFFFFF" stroke="{AMBER}" stroke-width="2"/>')
        lab, _ = _text_lines(_wrap(p["label"], 30), bx + 20, by + 30, size=22, weight="bold", fill=INK)
        parts.append(lab)
        if lines:
            sub, _ = _text_lines(lines, bx + 20, by + 58, size=19, fill=MUTED)
            parts.append(sub)
    height = y + 20 + ((n + 1) // 2) * 150 + 40
    return _svg("\n".join(parts), max(height, y + 300))


RENDERERS = {
    "flowchart": _flowchart,
    "timeline": _timeline,
    "concept": _concept,
    "compare": _compare,
    "labelled": _labelled,
}

REQUIRED = {
    "flowchart": ["title", "items"],
    "timeline": ["title", "items"],
    "concept": ["title", "center", "branches"],
    "compare": ["title", "left", "right", "rows"],
    "labelled": ["title", "center", "parts"],
}


def render_diagram(spec, slug, index):
    """Render one diagram spec to SVG. Returns web path."""
    kind = spec.get("kind")
    if kind not in RENDERERS:
        raise ValueError(f"Unknown diagram kind: {kind!r}")
    for key in REQUIRED[kind]:
        if key not in spec:
            raise ValueError(f"Diagram kind {kind} missing key: {key}")
    os.makedirs(DIAG_DIR, exist_ok=True)
    fname = f"{slug}-{index}.svg"
    with open(os.path.join(DIAG_DIR, fname), "w", encoding="utf-8") as f:
        f.write(RENDERERS[kind](spec))
    return f"/assets/images/blog/diagrams/{fname}"
