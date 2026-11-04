"""Daily batch builder for the Solved Sindh Textbook Board Books blog engine.

Usage:
    python3 build_batch.py batch_XXX BATCH_XXX     # validate + build + verify
    python3 build_batch.py --mark-done slug1 slug2 # mark topics done in topics_300.py

Batch files (gen/batch_XXX.py) hold BATCH_XXX = [post dicts]. Required keys:
  slug, title, cat, desc, kw, intro, sections, points, faqs
  sections: 5+ entries {h2, paras:[...], bullets?[...], diagram_spec?{...}}
  faqs: 4+ {q, a}. points: 4+ key-point strings.
  1-2 sections total carry a diagram_spec (rendered to SVG by diagram_gen).

Validation is strict: word count 700+, FAQs 4+, diagrams 1-2, internal links
only to pages that exist, no duplicate slugs. NEVER push if validation fails.
"""
import importlib
import html as htmlmod
import json
import os
import re
import subprocess
import sys

GEN_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(GEN_DIR)
EXTRA_PATH = os.path.join(GEN_DIR, "extra_posts.json")

sys.path.insert(0, SITE_DIR)
sys.path.insert(0, GEN_DIR)
import build_blog  # noqa: E402
from thumb_gen import save_thumbnail  # noqa: E402
from diagram_gen import render_diagram  # noqa: E402

CATS = {"Solved Notes", "Study Tips", "Board & Syllabus", "Subject Guides"}
STATIC_PAGES = {"/", "/books.html", "/solved.html", "/about.html", "/contact.html",
                "/privacy.html", "/terms.html", "/blog/"}


def _texts(p):
    out = [p.get("intro", ""), p.get("desc", "")]
    for s in p.get("sections", []):
        out.append(s.get("h2", ""))
        out.extend(s.get("paras", []))
        out.extend(s.get("bullets", []))
    out.extend(p.get("points", []))
    for f in p.get("faqs", []):
        out += [f.get("q", ""), f.get("a", "")]
    return out


def _strip_boilerplate(post):
    """Engine guard (2026-11-04): silently remove any section that carries the
    Muse invite-code boilerplate (LTGSWD / 'AI Help: Muse AI') from an
    incoming post before it can reach extra_posts.json. Returns count removed."""
    secs = post.get("sections", [])
    if not secs:
        return 0
    kept = []
    removed = 0
    for s in secs:
        blob = json.dumps(s, ensure_ascii=False)
        if "LTGSWD" in blob or "AI Help: Muse AI" in blob:
            removed += 1
            continue
        kept.append(s)
    if removed:
        post["sections"] = kept
    return removed


def validate(posts):
    errors = []
    seen = set()
    base_slugs = {p["slug"] for p in build_blog.BASE_POSTS}
    extra_slugs = set()
    try:
        with open(EXTRA_PATH, encoding="utf-8") as f:
            extra_slugs = {p["slug"] for p in json.load(f)}
    except FileNotFoundError:
        pass
    known_slugs = base_slugs | extra_slugs
    allowed_links = STATIC_PAGES | {f"/blog/{s}.html" for s in known_slugs}
    allowed_links |= {f"/blog/{p['slug']}.html" for p in posts}
    for pg in range(2, 10):
        allowed_links.add(f"/blog/page-{pg}.html")

    for p in posts:
        tag = p.get("slug", "?")
        for key in ("slug", "title", "cat", "desc", "kw", "intro", "sections", "points", "faqs"):
            if not p.get(key):
                errors.append(f"{tag}: missing/empty key {key}")
        if p.get("cat") not in CATS:
            errors.append(f"{tag}: bad cat {p.get('cat')!r}")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", p.get("slug", "")):
            errors.append(f"{tag}: bad slug format")
        if p.get("slug") in seen:
            errors.append(f"{tag}: duplicate slug inside batch")
        seen.add(p.get("slug"))
        if p.get("slug") in base_slugs:
            errors.append(f"{tag}: slug collides with an original-50 post")
        if p.get("slug") in extra_slugs:
            print(f"NOTE {tag}: already in extra_posts.json — will skip on build")
        if not (100 <= len(p.get("desc", "")) <= 200):
            errors.append(f"{tag}: desc must be 100-200 chars (got {len(p.get('desc', ''))})")
        secs = p.get("sections", [])
        if len(secs) < 5:
            errors.append(f"{tag}: need 5+ sections (got {len(secs)})")
        for s in secs:
            if not s.get("h2") or not (s.get("paras") or s.get("bullets")):
                errors.append(f"{tag}: section needs h2 + paras/bullets: {s.get('h2')!r}")
        if len(p.get("points", [])) < 4:
            errors.append(f"{tag}: need 4+ key points")
        if len(p.get("faqs", [])) < 4:
            errors.append(f"{tag}: need 4+ FAQs")
        for f in p.get("faqs", []):
            if not f.get("q") or not f.get("a"):
                errors.append(f"{tag}: FAQ needs q + a")
        n_diagrams = sum(1 for s in secs if s.get("diagram_spec"))
        if not (1 <= n_diagrams <= 2):
            errors.append(f"{tag}: need 1-2 diagram specs (got {n_diagrams})")
        words = build_blog._count_words(p)
        if words < 700:
            errors.append(f"{tag}: need 700+ words (got {words})")
        for t in _texts(p):
            for m in re.finditer(r"\[([^\]]+)\]\(([^)\s]+)\)", t):
                url = m.group(2)
                if url.startswith("/") and url not in allowed_links and not url.startswith("/assets/"):
                    errors.append(f"{tag}: internal link to missing page: {url}")
    return errors


def build(posts):
    """Render thumbs + diagrams, append to extra_posts.json, rebuild site."""
    existing = []
    if os.path.exists(EXTRA_PATH):
        with open(EXTRA_PATH, encoding="utf-8") as f:
            existing = json.load(f)
    have = {p["slug"] for p in existing}
    new_posts = []
    for p in posts:
        if p["slug"] in have:
            print(f"SKIP {p['slug']}: already in extra_posts.json")
            continue
        p = dict(p)
        _removed = _strip_boilerplate(p)
        if _removed:
            print(f"WARNING {p['slug']}: stripped {_removed} boilerplate section(s) containing LTGSWD/AI Help: Muse AI (engine guard)")
        p["thumb"] = save_thumbnail(p)
        di = 0
        for s in p["sections"]:
            spec = s.pop("diagram_spec", None)
            if spec:
                di += 1
                src = render_diagram(spec, p["slug"], di)
                s["diagram"] = {"src": src, "alt": spec.get("title", p["title"]),
                                "caption": spec.get("caption", spec.get("title", ""))}
        new_posts.append(p)
    if new_posts:
        existing.extend(new_posts)
        with open(EXTRA_PATH, "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
        print(f"Appended {len(new_posts)} posts to extra_posts.json")
    for script in ("build_blog.py",):
        r = subprocess.run([sys.executable, script], cwd=SITE_DIR,
                           capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode != 0:
            print(r.stderr[:2000])
            raise SystemExit(f"{script} FAILED")
    return [p["slug"] for p in posts]


def verify(slugs):
    ok = True
    with open(os.path.join(SITE_DIR, "sitemap-blog.xml"), encoding="utf-8") as f:
        sitemap = f.read()
    with open(os.path.join(SITE_DIR, "blog", "index.html"), encoding="utf-8") as f:
        listing = f.read()
    for slug in slugs:
        path = os.path.join(SITE_DIR, "blog", slug + ".html")
        if not os.path.exists(path):
            print(f"FAIL {slug}: HTML missing"); ok = False; continue
        with open(path, encoding="utf-8") as f:
            html = f.read()
        checks = [
            (f"/blog/{slug}.html" in sitemap, "sitemap"),
            (".svg" in html, "thumbnail/diagram refs"),
        ]
        for passed, name in checks:
            print(f"{'PASS' if passed else 'FAIL'} {slug}: {name}")
            ok = ok and passed
    return ok


def mark_done(slugs):
    import topics_300
    import pprint
    changed = 0
    for t in topics_300.TOPICS:
        if t["slug"] in slugs and t["status"] != "done":
            t["status"] = "done"
            changed += 1
    path = os.path.join(GEN_DIR, "topics_300.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write("TOPICS = " + pprint.pformat(topics_300.TOPICS, width=120) + "\n")
    print(f"Marked {changed} topics done in topics_300.py")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--mark-done":
        mark_done(sys.argv[2:])
        sys.exit(0)
    if len(sys.argv) < 3:
        print("usage: build_batch.py batch_XXX BATCH_XXX | build_batch.py --mark-done slug...")
        sys.exit(2)
    mod = importlib.import_module(sys.argv[1])
    batch = getattr(mod, sys.argv[2])
    errs = validate(batch)
    if errs:
        print("VALIDATION FAILED:")
        for e in errs:
            print(" -", e)
        sys.exit(1)
    print(f"Validation OK: {len(batch)} posts")
    slugs = build(batch)
    if not verify(slugs):
        print("VERIFY FAILED")
        sys.exit(1)
    print("BUILD + VERIFY OK")
