"""SVG thumbnail generator for Sindh Textbook Board blog articles.
Produces catchy 1200x630 thumbnails with article title, category, branding.
SVG is text -> pushes cleanly via GitHub API (no binary issues).
"""
import html as htmlmod
import os
import textwrap

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THUMB_DIR = os.path.join(SITE_DIR, "assets", "images", "blog")

CAT_COLORS = {
    "Solved Notes": ("#0B6B4A", "#14A06B"),
    "Study Tips": ("#1D4ED8", "#38BDF8"),
    "Board & Syllabus": ("#B45309", "#F59E0B"),
    "Subject Guides": ("#6D28D9", "#A78BFA"),
}
DEFAULT_COLORS = ("#0B6B4A", "#14A06B")


def make_thumbnail(p):
    """p: post dict with title, cat, slug. Returns SVG text."""
    c1, c2 = CAT_COLORS.get(p.get("cat", ""), DEFAULT_COLORS)
    title = htmlmod.unescape(p["title"])
    lines = textwrap.wrap(title, width=26)[:4]
    cat = htmlmod.escape(p.get("cat", "Guide"))
    title_els = ""
    y = 250
    for ln in lines:
        title_els += (f'<text x="70" y="{y}" font-family="Arial, sans-serif" font-size="58" '
                      f'font-weight="bold" fill="#ffffff">{htmlmod.escape(ln)}</text>\n')
        y += 72
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/>
</linearGradient></defs>
<rect width="1200" height="630" fill="url(#g)"/>
<circle cx="1080" cy="90" r="190" fill="#ffffff" opacity="0.12"/>
<circle cx="1050" cy="560" r="150" fill="#ffffff" opacity="0.10"/>
<rect x="70" y="70" width="220" height="46" rx="23" fill="#F59E0B"/>
<text x="180" y="101" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#1F2937" text-anchor="middle">{cat}</text>
{title_els}<text x="70" y="560" font-family="Arial, sans-serif" font-size="30" font-weight="bold" fill="#ffffff">Sindh Textbook Board</text>
<text x="70" y="595" font-family="Arial, sans-serif" font-size="22" fill="#DCE8E0">Free solved exercises - Sindhi - Urdu - English</text>
<rect x="980" y="470" width="150" height="90" rx="10" fill="#ffffff" opacity="0.95"/>
<text x="1055" y="510" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="{c1}" text-anchor="middle">S</text>
<text x="1055" y="540" font-family="Arial, sans-serif" font-size="16" fill="#1F2937" text-anchor="middle">SINDH</text>
</svg>'''


def save_thumbnail(p):
    """Write thumbnail SVG for post p. Returns web path for the thumb."""
    os.makedirs(THUMB_DIR, exist_ok=True)
    path = os.path.join(THUMB_DIR, p["slug"] + ".svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(make_thumbnail(p))
    return f"/assets/images/blog/{p['slug']}.svg"
