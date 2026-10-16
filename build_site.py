#!/usr/bin/env python3
"""Build core pages for Solved Sindh Textbook Board Books (index, books, solved, about, contact, legal, SEO files).
Run: python3 build_site.py  (then python3 build_blog.py for the 50 blog posts)
Data source: assets/data/books.json is generated here from BOOKS below.
To add a book: add an entry to BOOKS (or edit assets/data/books.json) + drop the PDF in assets/pdfs/.
"""
import json, os
from datetime import date

SITE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://solved-stbb-books.vercel.app"
TODAY = date.today().isoformat()

# ---------------- Book catalogue ----------------
REAL = [
 {"id":"isl-6-sd","cover":"assets/images/covers/isl-6-sd.jpg","title":"Class 6 Islamiat — Solved Exercises (Sindhi Medium)","cls":6,"subject":"Islamiat","medium":"Sindhi","type":"solved-notes","status":"live","pdf":"assets/pdfs/Class6-Islamiat-SolvedExercises-Sindhi.pdf","pages":28,"desc":"Complete solved exercises for Sindh Textbook Board Class 6 Islamiat, Sindhi medium — handwritten-style notes in the book's own format.","chapters":["Quran Majeed — Nazra, Hifz, Duaein","Imaniyat & Ibadat — Tauheed, Azan, Namaz, Hajj","Seerat Tayyaba — Sulah Hudaibiya se Ghazwa Khyber","Akhlaq & Adab — Taharat, Sadaqat, Amanat, Huqooq-ul-Ibad","Mashahir-e-Islam — Khadija, Ali, Data Ganj Bakhsh, Tariq bin Ziyad"]},
 {"id":"isl-6-ur","cover":"assets/images/covers/isl-6-ur.jpg","title":"Class 6 Islamiat — Solved Exercises (Urdu Medium)","cls":6,"subject":"Islamiat","medium":"Urdu","type":"solved-notes","status":"live","pdf":"assets/pdfs/Class6-Islamiat-SolvedExercises-Urdu.pdf","pages":28,"desc":"Complete solved exercises for Sindh Textbook Board Class 6 Islamiat, Urdu medium — clear answers in exam format.","chapters":["Quran Majeed — Nazra, Hifz, Duaein","Imaniyat & Ibadat — Tauheed, Azan, Namaz, Hajj","Seerat Tayyaba — Sulah Hudaibiya se Ghazwa Khyber","Akhlaq & Adab — Taharat, Sadaqat, Amanat, Huqooq-ul-Ibad","Mashahir-e-Islam — Khadija, Ali, Data Ganj Bakhsh, Tariq bin Ziyad"]},
 {"id":"isl-8-sd","cover":"assets/images/covers/isl-8-sd.jpg","title":"Class 8 Islamiat — Solved Exercises (Sindhi Medium)","cls":8,"subject":"Islamiat","medium":"Sindhi","type":"solved-notes","status":"live","pdf":"assets/pdfs/Class8-Islamiat-SolvedExercises-Sindhi.pdf","pages":32,"desc":"Complete solved exercises for Sindh Textbook Board Class 8 Islamiat, Sindhi medium — Aakhirat, Roza, Seerat, Akhlaq solved.","chapters":["Quran Majeed — Nazra, Hifz, Ayat-ul-Kursi","Imaniyat & Ibadat — Aakhirat, Roza, Hajj","Seerat Tayyaba — Khulq-e-Azeem, Sabr, Adl, Husn-e-Muashrat","Akhlaq & Adab — Halal Kamai, Itehad-e-Milli, Huqooq-ul-Ibad","Mashahir-e-Islam — Fatima-tuz-Zahra, Muhammad bin Qasim, Ibn-e-Sina, Shah Waliullah"]},
 {"id":"isl-8-ur","cover":"assets/images/covers/isl-8-ur.jpg","title":"Class 8 Islamiat — Solved Exercises (Urdu Medium)","cls":8,"subject":"Islamiat","medium":"Urdu","type":"solved-notes","status":"live","pdf":"assets/pdfs/Class8-Islamiat-SolvedExercises-Urdu.pdf","pages":32,"desc":"Complete solved exercises for Sindh Textbook Board Class 8 Islamiat, Urdu medium — exam-ready answers.","chapters":["Quran Majeed — Nazra, Hifz, Ayat-ul-Kursi","Imaniyat & Ibadat — Aakhirat, Roza, Hajj","Seerat Tayyaba — Khulq-e-Azeem, Sabr, Adl, Husn-e-Muashrat","Akhlaq & Adab — Halal Kamai, Itehad-e-Milli, Huqooq-ul-Ibad","Mashahir-e-Islam — Fatima-tuz-Zahra, Muhammad bin Qasim, Ibn-e-Sina, Shah Waliullah"]},
 {"id":"isl-9-sd","cover":"assets/images/covers/isl-9-sd.jpg","title":"Class 9 Islamiat — Solved Exercises (Sindhi Medium)","cls":9,"subject":"Islamiat","medium":"Sindhi","type":"solved-notes","status":"live","pdf":"assets/pdfs/Class9-Islamiat-SolvedExercises-Sindhi.pdf","pages":40,"desc":"Complete solved exercises for Sindh Textbook Board Class 9 Islamiat (IX–X volume), Sindhi medium — Quran, Hadith, Tauheed, Seerat.","chapters":["Quran Majeed — Taaruf, Fazilat, Chuninda Ayaat","Hadith Sharif — Taaruf, Sunnat, Chuninda Ahadith","Imaniyat — Tauheed, Risalat","Ibadat — Ahmiyat, Jihad","Seerat Tayyaba — Baasat, Dawat, Hijrat, Ghazwat, Shamail","Akhlaq — Ilm, Khandan, Ehtram-e-Insaniyat, Adl, Haya","Mashahir — Imam Hussain, Abu Ubaidah, Jabir bin Hayyan"]},
 {"id":"isl-9-ur","cover":"assets/images/covers/isl-9-ur.jpg","title":"Class 9 Islamiat — Solved Exercises (Urdu Medium)","cls":9,"subject":"Islamiat","medium":"Urdu","type":"solved-notes","status":"live","pdf":"assets/pdfs/Class9-Islamiat-SolvedExercises-Urdu.pdf","pages":40,"desc":"Complete solved exercises for Sindh Textbook Board Class 9 Islamiat (IX–X volume), Urdu medium — board-exam-ready answers.","chapters":["Quran Majeed — Taaruf, Fazilat, Chuninda Ayaat","Hadith Sharif — Taaruf, Sunnat, Chuninda Ahadith","Imaniyat — Tauheed, Risalat","Ibadat — Ahmiyat, Jihad","Seerat Tayyaba — Baasat, Dawat, Hijrat, Ghazwat, Shamail","Akhlaq — Ilm, Khandan, Ehtram-e-Insaniyat, Adl, Haya","Mashahir — Imam Hussain, Abu Ubaidah, Jabir bin Hayyan"]},
]
SUBJECTS_BY_CLASS = {
 1:["Sindhi","Urdu","English","Math","Islamiat"], 2:["Sindhi","Urdu","English","Math","Islamiat"],
 3:["Sindhi","Urdu","English","Math","Science"], 4:["Sindhi","Urdu","English","Math","Science"],
 5:["Sindhi","Urdu","English","Math","Science"], 6:["Sindhi","Urdu","English","Math","Science","Social Studies"],
 7:["Sindhi","Urdu","English","Math","Science","Islamiat"], 8:["Sindhi","Urdu","English","Math","Science","Social Studies"],
 9:["Urdu","English","Math","Physics","Chemistry","Biology","Pakistan Studies"],
 10:["Urdu","English","Math","Physics","Chemistry","Biology","Pakistan Studies"],
}
MEDIUMS = ["Sindhi","Urdu","English"]
BOOKS = list(REAL)
for cls, subjects in SUBJECTS_BY_CLASS.items():
    for j, subj in enumerate(subjects):
        med = MEDIUMS[(cls + j) % 3]
        if subj == "Islamiat" and cls in (6,8,9) and med in ("Sindhi","Urdu"):
            continue  # already live above
        BOOKS.append({"id":f"{subj.lower().replace(' ','-')}-{cls}-{med.lower()[:2]}","title":f"Class {cls} {subj} — Solved Exercises ({med} Medium)","cls":cls,"subject":subj,"medium":med,"type":"solved-notes","status":"coming-soon","pdf":None,"pages":None,"desc":f"Sindh Textbook Board Class {cls} {subj} solved exercises, {med} medium — coming soon. Check the live Islamiat notes for Classes 6, 8 and 9 while this one is prepared.","chapters":[]})
for subj in ["Physics","Chemistry","Biology","Mathematics","Urdu","English"]:
    BOOKS.append({"id":f"{subj.lower()}-11-en","title":f"Class 11 {subj} — Solved Exercises (English Medium)","cls":11,"subject":subj,"medium":"English","type":"solved-notes","status":"coming-soon","pdf":None,"pages":None,"desc":f"Sindh Textbook Board Class 11 {subj} solved exercises, English medium — coming soon.","chapters":[]})
for subj in ["Physics","Chemistry","Biology","Mathematics","Urdu","English"]:
    BOOKS.append({"id":f"{subj.lower()}-12-en","title":f"Class 12 {subj} — Solved Exercises (English Medium)","cls":12,"subject":subj,"medium":"English","type":"solved-notes","status":"coming-soon","pdf":None,"pages":None,"desc":f"Sindh Textbook Board Class 12 {subj} solved exercises, English medium — coming soon.","chapters":[]})

def w(path, content):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return full


CSS = r"""
:root{--green:#0B6B4A;--green2:#0E8A5F;--teal:#0E7C7B;--dark:#14201B;--muted:#5A6B62;--bg:#F7FAF8;--card:#fff;--line:#DCE8E0;--amber:#E8A020;--radius:14px}
*{box-sizing:border-box}html{scroll-behavior:smooth}html,body{width:100%}body{overflow-x:clip;margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--dark);background:var(--bg);line-height:1.65}
a{color:var(--green)}a:hover{color:var(--green2)}.container{width:100%;max-width:1140px;margin:0 auto;padding:0 18px}
.skip-link{position:absolute;left:-9999px}.skip-link:focus{position:static;background:var(--green);color:#fff;padding:8px 14px;display:block}
.site-header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50}.header-inner{display:flex;align-items:center;gap:16px;min-height:64px}
.logo{display:flex;align-items:center;gap:9px;font-weight:800;font-size:19px;color:var(--dark);text-decoration:none}.logo-mark{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:9px;background:var(--green);color:#fff;font-size:20px}
.main-nav{margin-left:auto;display:flex;align-items:center;gap:4px;flex-wrap:wrap}.main-nav a{padding:8px 11px;border-radius:8px;text-decoration:none;color:var(--dark);font-weight:600;font-size:15px}.main-nav a.active,.main-nav a:hover{background:#EAF4EF;color:var(--green)}
.btn{display:inline-block;background:var(--green);color:#fff!important;text-decoration:none;padding:12px 22px;border-radius:10px;font-weight:700;border:2px solid var(--green);cursor:pointer}.btn:hover{background:var(--green2);border-color:var(--green2)}.btn.small{padding:8px 15px;font-size:14px}.btn .ic{vertical-align:-2px;margin-right:5px}.btn.outline{background:#fff;color:var(--green)!important}.btn.light{background:#fff;color:var(--green)!important;border-color:#fff}.btn.amber{background:var(--amber);border-color:var(--amber);color:#222!important}
.nav-toggle{display:none;margin-left:auto;background:none;border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:18px;cursor:pointer}
.hero{background:var(--green);color:#fff;padding:52px 0 46px;text-align:center}.hero h1{font-size:clamp(30px,5vw,48px);line-height:1.15;margin:10px 0 14px}.hero p.lead{font-size:18px;max-width:720px;opacity:.95;margin:0 auto}.eyebrow{display:inline-block;background:rgba(255,255,255,.16);padding:6px 12px;border-radius:999px;font-size:13px;font-weight:700}
.search-box{display:flex;gap:10px;max-width:680px;margin:22px auto 10px}.search-box input{flex:1;padding:14px 16px;border-radius:10px;border:0;font-size:16px}.search-box .btn{background:#fff;color:var(--green)!important;border-color:#fff}

.section{padding:48px 0}.section h2{font-size:30px;margin:0 0 8px}.section .sub{color:var(--muted);max-width:760px;margin:0 0 26px}
.filters{display:flex;gap:12px;flex-wrap:wrap;background:#fff;border:1px solid var(--line);padding:16px;border-radius:var(--radius);margin-bottom:26px}.filters label{font-weight:700;font-size:14px;display:flex;flex-direction:column;gap:6px;flex:1;min-width:170px}.filters input,.filters select{padding:11px 12px;border:1px solid var(--line);border-radius:9px;font-size:15px;background:#fff}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;display:flex;flex-direction:column}.card-cover.has-img{background:#fff;padding:10px;min-height:0}.card-cover.has-img img{width:100%;height:140px;object-fit:contain;display:block}.card-meta{display:flex;gap:6px;flex-wrap:wrap;margin:0}.modal-cover{width:100%;max-height:260px;object-fit:contain;background:#fff;border-radius:8px;margin-bottom:12px}.card-cover{background:var(--green);color:#fff;padding:22px;min-height:120px;display:flex;flex-direction:column;justify-content:flex-end;gap:4px}.card-cover small{opacity:.85}.card-cover b{font-size:20px;line-height:1.25}.card-body{padding:18px;display:flex;flex-direction:column;gap:10px;flex:1}.card-body h3{margin:0;font-size:18px;line-height:1.35}.card-body p{margin:0;color:var(--muted);font-size:14.5px}.card-body .actions{margin-top:auto;display:flex;gap:8px;flex-wrap:wrap}
.chip{display:inline-block;background:#EAF4EF;color:var(--green);padding:4px 10px;border-radius:999px;font-size:12.5px;font-weight:700}.chip.soon{background:#FFF4DE;color:#8A5A00}.chip.live{background:#E3F7EC;color:#0B6B4A}
.steps-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}.step{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px}.step .num{width:44px;height:44px;border-radius:50%;background:var(--green);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:20px;margin-bottom:12px}
.subject-strip{display:flex;gap:10px;flex-wrap:wrap}.subject-strip a{background:#fff;border:1px solid var(--line);padding:9px 16px;border-radius:999px;text-decoration:none;color:var(--dark);font-weight:600}
.testimonials{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}.testi{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:22px}.testi p{font-style:italic}.testi b{display:block;margin-top:10px}
.faq details{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin-bottom:10px}.faq summary{cursor:pointer;font-weight:700}
.newsletter{background:var(--dark);color:#fff;border-radius:18px;padding:34px;text-align:center}.newsletter h2{color:#fff}.newsletter input{padding:13px 16px;border-radius:10px;border:0;min-width:260px;font-size:15px}.newsletter form{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:16px}
.post{max-width:820px;margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:16px;padding:32px}.post h1{font-size:32px;line-height:1.25}.post h2{font-size:24px;margin-top:34px}.post-meta{color:var(--muted)}.post-hero{background:var(--green);color:#fff;border-radius:12px;padding:34px 26px;display:flex;justify-content:space-between;align-items:flex-end;margin:20px 0}.post-hero-num{font-size:52px;font-weight:800}.lead{font-size:18px}
.post-thumb{width:100%;height:auto;border-radius:12px;margin:20px 0;display:block}
figure.diagram{margin:22px 0 8px;border:1px solid var(--line);border-radius:12px;padding:14px;background:#F7FAF8}figure.diagram img{width:100%;height:auto;display:block;border-radius:8px}figure.diagram figcaption{font-size:14px;color:var(--muted);text-align:center;margin-top:10px}
.key-points li{margin-bottom:10px}.steps li{margin-bottom:12px}.related{background:#F7FAF8;border:1px solid var(--line);border-radius:12px;padding:20px;margin-top:30px}
.crumbs{padding:18px 0 6px;color:var(--muted);font-size:14px}.crumbs a{color:var(--muted)}
.modal-backdrop{position:fixed;inset:0;background:rgba(0,0,0,.55);display:none;align-items:center;justify-content:center;z-index:100;padding:16px}.modal-backdrop.open{display:flex}.modal{background:#fff;border-radius:16px;max-width:640px;width:100%;max-height:88vh;overflow:auto;padding:26px}.modal .close{float:right;background:none;border:0;font-size:24px;cursor:pointer}
.site-footer{background:#fff;border-top:1px solid var(--line);margin-top:50px;padding:36px 0 20px}.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:24px}.site-footer ul{list-style:none;padding:0}.site-footer li{margin-bottom:8px}.site-footer a{text-decoration:none;color:var(--muted)}.copyright{text-align:center;color:var(--muted);font-size:13.5px;border-top:1px solid var(--line);padding-top:16px}
.pagination{display:flex;gap:12px;align-items:center;justify-content:center;margin:30px 0}.form-box{max-width:640px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:26px}.form-box label{display:block;font-weight:700;margin:14px 0 6px}.form-box input,.form-box textarea,.form-box select{width:100%;padding:12px;border:1px solid var(--line);border-radius:9px;font-size:15px}
.notice{background:#FFF4DE;border:1px solid #F2D492;border-radius:10px;padding:14px 18px}
@media(max-width:760px){.main-nav{display:none;width:100%;flex-direction:column;align-items:stretch}.main-nav.open{display:flex}.nav-toggle{display:block}.footer-grid{grid-template-columns:1fr}.post{padding:20px}.search-box{flex-direction:column}.hero{padding:36px 0 30px}.section{padding:32px 0}}
.pdf-frame{width:100%;height:78vh;border:1px solid var(--line);border-radius:12px;background:#fff}.btn.whatsapp{background:#25D366;border-color:#25D366;color:#fff!important}.btn.whatsapp:hover{background:#1FB857;border-color:#1FB857}.preview-meta{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
@media(max-width:760px){.pdf-frame{height:68vh}}
"""

JS = r"""
// Solved Sindh Textbook Board Books — search, filters, FAQ, detail modal
// NOTE: website is English-only. No language switcher, no RTL: the whole
// document always stays LTR so English content is always left-sided.
document.addEventListener('DOMContentLoaded', ()=>{
  const navBtn = document.getElementById('nav-toggle');
  const nav = document.getElementById('main-nav');
  if(navBtn && nav){ navBtn.addEventListener('click', ()=>{ nav.classList.toggle('open'); navBtn.setAttribute('aria-expanded', nav.classList.contains('open')); }); }
  // Catalogue render
  const grid = document.getElementById('books-grid');
  if(grid){ renderBooks(); ['q','f-class','f-medium','f-subject','f-status'].forEach(id=>{ const el=document.getElementById(id); if(el) el.addEventListener('input', renderBooks); }); }
  const blogSearch = document.getElementById('blog-search');
  if(blogSearch){ const cat=document.getElementById('blog-cat'); const fn=()=>{ const q=blogSearch.value.toLowerCase(); const c=cat?cat.value:''; document.querySelectorAll('#blog-grid .blog-card').forEach(card=>{ const txt=card.textContent.toLowerCase(); const okQ=!q||txt.includes(q); const okC=!c||txt.includes(c.toLowerCase()); card.style.display=(okQ&&okC)?'':'none'; }); }; blogSearch.addEventListener('input',fn); if(cat) cat.addEventListener('change',fn); }
  // Hero search -> books page
  const heroForm = document.getElementById('hero-search-form');
  if(heroForm){ heroForm.addEventListener('submit', e=>{ e.preventDefault(); const q=document.getElementById('hero-search').value; window.location.href='/books.html?q='+encodeURIComponent(q); }); }
  // Newsletter (no backend — mailto fallback + success message)
  document.querySelectorAll('.newsletter form').forEach(f=>f.addEventListener('submit', e=>{ e.preventDefault(); const msg=f.parentElement.querySelector('.nl-msg'); if(msg){ msg.textContent='Thanks! You are on the list. New solved notes will be shared here first.'; } f.reset(); }));
});
let BOOKS = [];
async function loadBooks(){
  if(BOOKS.length) return BOOKS;
  try{ const r = await fetch('/assets/data/books.json'); BOOKS = await r.json(); }catch(e){ BOOKS = []; }
  return BOOKS;
}
function cardHTML(b){
  const live = b.status==='live';
  const badge = live ? '<span class="chip live">● Live — Preview Free</span>' : '<span class="chip soon">Coming Soon</span>';
  const btn = live ? `<a class="btn small" href="/preview.html?id=${b.id}"><svg class="ic" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg> Open</a>` : `<button class="btn small outline" onclick="openBook('${b.id}')">Notify me</button>`;
  const cover = b.cover ? `<div class="card-cover has-img"><img src="/${b.cover}" alt="${b.title} — official book cover" loading="lazy"></div>` : `<div class="card-cover"><small>Class ${b.cls} · ${b.medium} Medium</small><b>${b.title.replace(' — Solved Exercises ('+b.medium+' Medium)','')}</b><small>${b.subject}</small></div>`;
  const titleRow = b.cover ? `<h3>${b.title}</h3><p class="card-meta"><span class="chip">Class ${b.cls}</span> <span class="chip">${b.subject}</span> <span class="chip">${b.medium} Medium</span></p>` : '';
  return `<article class="card" data-id="${b.id}">${cover}<div class="card-body">${badge}${titleRow}<p>${b.desc}</p><div class="actions">${btn}</div></div></article>`;
}
async function renderBooks(){
  const grid = document.getElementById('books-grid'); if(!grid) return;
  const books = await loadBooks();
  const params = new URLSearchParams(location.search);
  const q = (document.getElementById('q')?.value || params.get('q') || '').toLowerCase();
  const qc = document.getElementById('q'); if(qc && !qc.value && q) qc.value = q;
  const fcEl = document.getElementById('f-class'); if(fcEl && !fcEl.value && params.get('f-class')) fcEl.value = params.get('f-class');
  const fmEl = document.getElementById('f-medium'); if(fmEl && !fmEl.value && params.get('f-medium')) fmEl.value = params.get('f-medium');
  const fsEl = document.getElementById('f-subject'); if(fsEl && !fsEl.value && params.get('f-subject')) fsEl.value = params.get('f-subject');
  const fc = fcEl?.value || '';
  const fm = fmEl?.value || '';
  const fs = fsEl?.value || '';
  const fst = document.getElementById('f-status')?.value || '';
  const filtered = books.filter(b=>{
    if(fc && String(b.cls)!==fc) return false;
    if(fm && b.medium!==fm) return false;
    if(fs && b.subject!==fs) return false;
    if(fst && b.status!==fst) return false;
    if(q && !(b.title+' '+b.subject+' '+b.medium+' Class '+b.cls).toLowerCase().includes(q)) return false;
    return true;
  });
  const count = document.getElementById('books-count'); if(count) count.textContent = filtered.length + ' books found';
  grid.innerHTML = filtered.length ? filtered.map(cardHTML).join('') : '<p>No books match your filters. Try clearing the search or choose another class/medium.</p>';
}
async function openBook(id){
  const books = await loadBooks();
  const b = books.find(x=>x.id===id); if(!b) return;
  const modal = document.getElementById('book-modal'); const body = document.getElementById('modal-body');
  const chapters = (b.chapters||[]).length ? '<h3>Chapters covered</h3><ul>'+b.chapters.map(c=>'<li>'+c+'</li>').join('')+'</ul>' : '<p>This book is being prepared. Join the list below and we will share it as soon as it is ready.</p>';
  const dl = b.pdf ? `<p><a class="btn" href="/preview.html?id=${b.id}"><svg class="ic" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg> Open Preview</a></p>` : '<p><a class="btn outline" href="/contact.html">Request this book</a></p>';
  const coverImg = b.cover ? `<img class="modal-cover" src="/${b.cover}" alt="${b.title} — official book cover">` : '';
  body.innerHTML = `${coverImg}<h2>${b.title}</h2><p><span class="chip">Class ${b.cls}</span> <span class="chip">${b.subject}</span> <span class="chip">${b.medium} Medium</span> ${b.status==='live'?'<span class="chip live">Live</span>':'<span class="chip soon">Coming Soon</span>'}</p><p>${b.desc}</p>${chapters}${dl}<p><a href="/books.html">← Back to all books</a></p>`;
  modal.classList.add('open');
}
function closeModal(){ document.getElementById('book-modal')?.classList.remove('open'); }
document.addEventListener('click', e=>{ if(e.target && e.target.id==='book-modal') closeModal(); });
document.addEventListener('keydown', e=>{ if(e.key==='Escape') closeModal(); });
"""


# ---------------- Templates ----------------
def head(title, desc, path, keywords="", extra=""):
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">
<meta name="robots" content="index, follow">
{f'<meta name="keywords" content="{keywords}">' if keywords else ''}
<meta property="og:type" content="website"><meta property="og:site_name" content="Solved Sindh Textbook Board Books">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{BASE}/assets/images/og.svg">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{BASE}/assets/images/og.svg">
<link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#0B6B4A"><link rel="stylesheet" href="/assets/css/style.css?v=2">
{extra}</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
"""

def header(active=""):
    def a(href, label):
        return f'<a href="{href}" class="{"active" if href==active else ""}">{label}</a>'
    return f"""<header class="site-header"><div class="container header-inner">
<a class="logo" href="/"><span class="logo-mark">S</span> Solved Sindh Textbook Board Books</a>
<button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu" aria-expanded="false">☰</button>
<nav class="main-nav" id="main-nav" aria-label="Main navigation">
{a('/', 'Home')}{a('/books.html', 'Books')}{a('/solved.html', 'Solved Notes')}{a('/blog/', 'Blog')}{a('/about.html', 'About')}{a('/contact.html', 'Contact')}<a href="/books.html" class="btn small">Browse Books</a>
</nav></div></header>
"""

FOOTER = """<footer class="site-footer"><div class="container footer-grid">
<div><a class="logo" href="/"><span class="logo-mark">S</span> Solved Sindh Textbook Board Books</a><p>Preview solved Sindh Textbook Board books and exercises free on this website — Sindhi, Urdu and English medium. Full PDFs Rs.100 on WhatsApp. Prepared by teachers, for students.</p></div>
<div><h3>Explore</h3><ul><li><a href="/books.html">All Books</a></li><li><a href="/solved.html">Solved Notes</a></li><li><a href="/blog/">Blog</a></li><li><a href="/about.html">About</a></li></ul></div>
<div><h3>Help</h3><ul><li><a href="/contact.html">Contact</a></li><li><a href="/privacy.html">Privacy Policy</a></li><li><a href="/terms.html">Terms</a></li></ul></div>
</div><p class="copyright">© 2026 Solved Sindh Textbook Board Books. Preview free on this website. Textbooks are the property of the Sindh Textbook Board.</p></footer>
<script src="/assets/js/main.js"></script>
</body></html>"""

MODAL = """<div class="modal-backdrop" id="book-modal" role="dialog" aria-modal="true" aria-label="Book details"><div class="modal"><button class="close" onclick="closeModal()" aria-label="Close">×</button><div id="modal-body"></div></div></div>"""

ORG_LD = json.dumps({"@context":"https://schema.org","@type":"Organization","name":"Solved Sindh Textbook Board Books","url":BASE,"logo":BASE+"/assets/images/og.svg","description":"Free solved Sindh Textbook Board books and exercises for Sindh Board students in Sindhi, Urdu and English medium."}, ensure_ascii=False)
SITE_LD = json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"Solved Sindh Textbook Board Books","url":BASE,"inLanguage":["en","sd","ur"],"publisher":{"@type":"Organization","name":"Solved Sindh Textbook Board Books"},"potentialAction":{"@type":"SearchAction","target":BASE+"/books.html?q={search_term_string}","query-input":"required name=search_term_string"}}, ensure_ascii=False)

def featured_cards():
    out = ""
    for b in REAL:
        cover = f"""<div class="card-cover has-img"><img src="/{b['cover']}" alt="Class {b['cls']} Islamiat — official book cover" loading="lazy"></div>""" if b.get('cover') else f"""<div class="card-cover"><small>Class {b['cls']} · {b['medium']} Medium</small><b>Class {b['cls']} Islamiat</b><small>Solved Exercises</small></div>"""
        out += f"""<article class="card">{cover}<div class="card-body"><span class="chip live">● Live — Preview Free</span><h3>{b['title']}</h3><p class="card-meta"><span class="chip">Class {b['cls']}</span> <span class="chip">{b['subject']}</span> <span class="chip">{b['medium']} Medium</span></p><p>{b['desc']}</p><div class="actions"><a class="btn small" href="/preview.html?id={b['id']}"><svg class="ic" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg> Open</a></div></div></article>\n"""
    return out

# ---------------- Pages ----------------
def build():
    os.makedirs(os.path.join(SITE, "assets/data"), exist_ok=True)
    with open(os.path.join(SITE, "assets/data/books.json"), "w", encoding="utf-8") as f:
        json.dump(BOOKS, f, ensure_ascii=False, indent=2)
    w("assets/css/style.css", CSS.strip() + "\n")
    w("assets/js/main.js", JS.strip() + "\n")

    # INDEX
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"Are the solved notes really free?","acceptedAnswer":{"@type":"Answer","text":"Preview is free on this website. The full PDF costs Rs.100 — open the preview, tap Download, and order on WhatsApp."}},
        {"@type":"Question","name":"Which mediums are available?","acceptedAnswer":{"@type":"Answer","text":"Solved notes are available in Sindhi, Urdu and English medium. Islamiat for Classes 6, 8 and 9 is live in Sindhi and Urdu; more books are being added."}},
        {"@type":"Question","name":"Do the solved notes follow the Sindh Textbook Board textbook?","acceptedAnswer":{"@type":"Answer","text":"Yes. Every solved exercise follows the official Sindh Textbook Board textbook chapter by chapter, in the book's own format."}},
        {"@type":"Question","name":"Can I request a book that is not listed?","acceptedAnswer":{"@type":"Answer","text":"Yes. Use the contact page to request any Sindh Textbook Board class, subject or medium. Requested books are prepared first."}},
    ]}
    index = head("Solved Sindh Textbook Board Books — Solved Exercises Sindhi, Urdu & English Medium, Free Preview | Sindh Board",
        "Preview solved Sindh Textbook Board books & exercises free on this website. Class 6, 8, 9 Islamiat solved notes live in Sindhi & Urdu medium. Full PDF Rs.100 on WhatsApp.",
        "/", "Sindh Textbook Board solved books, Sindh Textbook Board solved exercises, Class 9 Islamiat solved Sindhi",
        f'<script type="application/ld+json">{ORG_LD}</script><script type="application/ld+json">{SITE_LD}</script><script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>')
    index += header("/") + f"""
<main id="main">
<section class="hero"><div class="container">
<span class="eyebrow">Free Preview · Sindh Textbook Board</span>
<h1 id="hero-title">Free Solved Sindh Textbook Board Books — Sindhi, Urdu &amp; English Medium</h1>
<p class="lead" id="hero-sub">Preview solved exercises for Sindh Textbook Board books. Class 6, 8 and 9 Islamiat notes are live now — free preview on this website. Full PDF Rs.100 on WhatsApp.</p>
<form class="search-box" id="hero-search-form" role="search"><label class="sr-only" for="hero-search" style="position:absolute;left:-9999px">Search books</label><input type="search" id="hero-search" placeholder="Search by class, subject or medium… e.g. Class 9 Islamiat Sindhi"><button class="btn" type="submit">Search</button></form>
<div><a class="btn light" href="/books.html">Browse All Books</a> <a class="btn amber" href="/solved.html">Solved Notes</a></div>

</div></section>
<section class="section container"><h2>Featured solved notes — free preview</h2><p class="sub">Real solved exercises, prepared from the Sindh Textbook Board textbook. Click Open to preview free on this website. Full PDF Rs.100 on WhatsApp.</p><div class="grid">{featured_cards()}</div></section>
<section class="section container"><h2>How it works</h2><div class="steps-grid">
<div class="step"><div class="num">1</div><h3>Find your book</h3><p>Search by class, subject or medium — or browse the catalogue.</p></div>
<div class="step"><div class="num">2</div><h3>Preview free</h3><p>Open the preview on this website. Free to preview — full PDF Rs.100 on WhatsApp.</p></div>
<div class="step"><div class="num">3</div><h3>Learn &amp; write</h3><p>Study the solved answers, then write them from memory. That is how marks are made.</p></div></div></section>
<section class="section container"><h2>Browse by subject</h2><div class="subject-strip">
<a href="/books.html?f-subject=Islamiat">Islamiat</a><a href="/books.html?f-subject=Urdu">Urdu</a><a href="/books.html?f-subject=Sindhi">Sindhi</a><a href="/books.html?f-subject=English">English</a><a href="/books.html?f-subject=Math">Math</a><a href="/books.html?f-subject=Science">Science</a><a href="/books.html?f-subject=Physics">Physics</a><a href="/books.html?f-subject=Chemistry">Chemistry</a><a href="/books.html?f-subject=Biology">Biology</a><a href="/books.html?f-subject=Pakistan Studies">Pakistan Studies</a><a href="/books.html?f-subject=Social Studies">Social Studies</a></div></section>
<section class="section container"><h2>Why students love it</h2><div class="steps-grid">
<div class="step"><h3>📖 Follows the textbook</h3><p>Every answer follows the Sindh Textbook Board book chapter by chapter — nothing extra, nothing missing.</p></div>
<div class="step"><h3>✍️ Exam-ready answers</h3><p>Answers are written the way examiners want: translation, explanation, example.</p></div>
<div class="step"><h3>🌍 Three mediums</h3><p>Sindhi, Urdu and English — study in the medium you write your exam in.</p></div>
<div class="step"><h3>📱 Works on any phone</h3><p>Fast, mobile-first pages and PDFs that open on any phone.</p></div></div></section>
<section class="section container"><h2>What students say</h2><div class="testimonials">
<div class="testi"><p>“Class 9 Islamiat ke solved notes ne meri tayyari aasan kar di. Har jawab kitab ke mutabiq hai.”</p><b>— Class 9 Student, Hyderabad</b></div>
<div class="testi"><p>“Sindhi medium notes milna mushkil tha. Yahan sab kuch free aur saaf likha hua mila.”</p><b>— Class 8 Student, Larkana</b></div>
<div class="testi"><p>“Main apni class ko isi se parhata hoon. Solved exercises ka format board ke liye behtareen hai.”</p><b>— School Teacher, Sukkur</b></div></div></section>
<section class="section container"><h2>Frequently asked questions</h2><div class="faq">
<details open><summary>Are the solved notes really free?</summary><p>Preview is free on this website. The full PDF costs Rs.100 — open the preview, tap Download, and order on WhatsApp.</p></details>
<details><summary>Which mediums are available?</summary><p>Sindhi, Urdu and English. Islamiat for Classes 6, 8 and 9 is live in Sindhi and Urdu; more books are being added.</p></details>
<details><summary>Do the solved notes follow the Sindh Textbook Board textbook?</summary><p>Yes. Every solved exercise follows the official Sindh Textbook Board textbook chapter by chapter.</p></details>
<details><summary>Can I request a book that is not listed?</summary><p>Yes — use the <a href="/contact.html">contact page</a>. Requested books are prepared first.</p></details>
</div></section>
<section class="section container"><div class="newsletter"><h2>Get new solved notes first</h2><p>One email when a new book is added. No spam, unsubscribe anytime.</p><form><label class="sr-only" for="nl-email" style="position:absolute;left:-9999px">Email</label><input id="nl-email" type="email" required placeholder="Your email address"><button class="btn amber" type="submit">Join free</button></form><p class="nl-msg"></p><p>Or join on WhatsApp: <a href="https://wa.me/923018981055" style="color:#fff">+92 301 8981055</a></p></div></section>
</main>
""" + MODAL + FOOTER
    w("index.html", index)

    # BOOKS
    books_page = head("All Books — Sindh Textbook Board Solved Exercises by Class, Subject & Medium | Solved Sindh Textbook Board Books",
        "Browse all Sindh Textbook Board solved books by class (1-12), subject and medium (Sindhi, Urdu, English). Free PDF downloads, live search and filters.",
        "/books.html", "Sindh Textbook Board books catalogue, solved exercises by class, Sindh Board books")
    books_page += header("/books.html") + """
<main id="main" class="container"><h1>All Books — Sindh Textbook Board Solved Exercises</h1>
<p class="lead">Search and filter the full catalogue. Live books have a free preview; full PDF Rs.100 on WhatsApp. Coming-soon books can be requested.</p>
<div class="filters">
<label>Search <input type="search" id="q" placeholder="e.g. Class 9 Islamiat Sindhi"></label>
<label>Class <select id="f-class"><option value="">All classes</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7</option><option>8</option><option>9</option><option>10</option><option>11</option><option>12</option></select></label>
<label>Medium <select id="f-medium"><option value="">All mediums</option><option>Sindhi</option><option>Urdu</option><option>English</option></select></label>
<label>Subject <select id="f-subject"><option value="">All subjects</option><option>Islamiat</option><option>Urdu</option><option>Sindhi</option><option>English</option><option>Math</option><option>Science</option><option>Social Studies</option><option>Physics</option><option>Chemistry</option><option>Biology</option><option>Pakistan Studies</option><option>Mathematics</option></select></label>
<label>Status <select id="f-status"><option value="">All</option><option value="live">Live — Free PDF</option><option value="coming-soon">Coming Soon</option></select></label>
</div><p id="books-count"></p><div class="grid" id="books-grid"><p>Loading books…</p></div>
<p class="notice">Tip: click <strong>Open</strong> on any card to preview it free on this website. Cannot find your book? <a href="/contact.html">Request it here</a>.</p>
</main>
""" + MODAL + FOOTER
    w("books.html", books_page)

    # SOLVED
    solved = head("Solved Notes — Free Preview of Sindh Textbook Board Solved Exercises",
        "Preview solved notes free: Class 6, 8, 9 Islamiat solved exercises in Sindhi & Urdu medium. Full PDF Rs.100 on WhatsApp.",
        "/solved.html", "Sindh Textbook Board solved notes, solved exercises PDF, Islamiat solved notes")
    solved += header("/solved.html") + f"""
<main id="main" class="container"><h1>Solved Notes — Free Preview</h1>
<p class="lead">Six solved-notes PDFs are live now — preview them free on this website. Full PDF Rs.100 on WhatsApp. More classes, subjects and mediums are being added — request yours on the contact page.</p>
<div class="grid">{featured_cards()}</div>
<h2 style="margin-top:36px">How to use solved notes (so they become marks)</h2>
<ol class="steps"><li>Read the solved answer with your Sindh Textbook Board book open.</li><li>Close the book and write the answer from memory.</li><li>Compare, fix the missing line, and revise after 2 days.</li></ol>
<p><a class="btn" href="/books.html">Browse all books →</a></p></main>
""" + MODAL + FOOTER
    w("solved.html", solved)

    # ABOUT / CONTACT / LEGAL
    about = head("About — Solved Sindh Textbook Board Books", "About Solved Sindh Textbook Board Books: free solved Sindh Textbook Board exercises for Sindh Board students in Sindhi, Urdu and English medium, prepared by teachers.", "/about.html")
    about += header("/about.html") + """<main id="main" class="container"><h1>About Solved Sindh Textbook Board Books</h1><p class="lead">We are teachers from Sindh. We saw students struggling to find solved exercises in their own medium — especially Sindhi medium — so we started preparing them, chapter by chapter, from the official Sindh Textbook Board textbooks.</p><h2>What we do</h2><ul><li>Solve every exercise from the Sindh Textbook Board textbook in the book's own format.</li><li>Write answers the way board examiners want: translation, explanation, example.</li><li>Publish everything for preview — free on this website; full PDFs Rs.100 on WhatsApp.</li></ul><h2>What we do not do</h2><p>We do not replace the textbook. Solved notes are for learning and revision — always study with your Sindh Textbook Board book open. Textbooks are the property of the Sindh Textbook Board; solved notes here are original explanations of those exercises.</p><p><a class="btn" href="/books.html">Browse books →</a></p></main>""" + FOOTER
    w("about.html", about)
    contact = head("Contact — Request a Book | Solved Sindh Textbook Board Books", "Contact Solved Sindh Textbook Board Books to request a solved book, report an error, or suggest a new guide.", "/contact.html")
    contact += header("/contact.html") + """<main id="main" class="container"><h1>Contact &amp; Request a Book</h1><p class="lead">Tell us which book you need — class, subject and medium — and we will prepare it first.</p><div class="form-box"><form action="mailto:hello@stbbsolved.pk" method="post" enctype="text/plain"><label>Your name <input name="name" required></label><label>Email <input name="email" type="email" required></label><label>Request <select name="type"><option>Request a solved book</option><option>Report an error</option><option>Suggest a guide</option><option>Other</option></select></label><label>Class <input name="class" placeholder="e.g. Class 10"></label><label>Subject &amp; Medium <input name="subject" placeholder="e.g. Physics, English medium"></label><label>Message <textarea name="message" rows="5" required placeholder="Which book do you need?"></textarea></label><button class="btn" type="submit">Send request</button></form></div><p>WhatsApp: <a href="https://wa.me/923018981055">+92 301 8981055</a></p></main>""" + FOOTER
    w("contact.html", contact)
    privacy = head("Privacy Policy | Solved Sindh Textbook Board Books", "Privacy policy for Solved Sindh Textbook Board Books. No accounts, no tracking beyond basic analytics.", "/privacy.html")
    privacy += header("") + """<main id="main" class="container"><h1>Privacy Policy</h1><p>This site does not require accounts. We do not sell personal data. If you email us, we use your message only to reply. Preview uses the on-page viewer; full PDFs are sent on WhatsApp after payment. No personal data is needed to preview.</p><p>Basic anonymous visit counts may be used to see which books students need most. No advertising profiles are built from this site.</p></main>""" + FOOTER
    w("privacy.html", privacy)
    terms = head("Terms | Solved Sindh Textbook Board Books", "Terms of use for Solved Sindh Textbook Board Books. Free solved notes for study; always verify against your Sindh Textbook Board textbook.", "/terms.html")
    terms += header("") + """<main id="main" class="container"><h1>Terms of Use</h1><p>Solved-note previews are free for study and revision. Full PDFs cost Rs.100 via WhatsApp. Always verify answers against your official Sindh Textbook Board textbook and your teacher. We aim for accuracy but accept no liability for exam outcomes. Textbooks remain the property of the Sindh Textbook Board.</p></main>""" + FOOTER
    w("terms.html", terms)

    # PREVIEW — PDF viewer page. Users preview free on this website; the
    # Download button is locked and opens the Rs.100 WhatsApp buy popup.
    preview = head("Preview Solved PDF | Solved Sindh Textbook Board Books",
        "Preview a solved Sindh Textbook Board PDF free on this website. Full PDF Rs.100 on WhatsApp.",
        "/preview.html", "preview solved PDF, Sindh Textbook Board solved notes preview")
    preview += header("") + """<main id="main" class="container">
<p id="preview-loading">Loading book…</p>
<div id="preview-content" style="display:none">
<h1 id="preview-title"></h1>
<div class="preview-meta" id="preview-chips"></div>
<p class="lead" id="preview-desc"></p>
<p>Preview free on this website. Full PDF Rs.100 — tap Download below to order on WhatsApp.</p>
<div oncontextmenu="return false"><iframe id="pdf-frame" class="pdf-frame" title="Solved PDF preview" src=""></iframe></div>
<p style="margin-top:18px"><button class="btn" id="buy-btn">⬇ Download PDF</button> <a class="btn outline" href="/books.html">← Back to all books</a></p>
<p class="muted" style="font-size:14px;color:var(--muted)">Preview is free on this website. Download is locked — the full PDF is Rs.100 on WhatsApp.</p>
</div>
<div id="preview-notfound" style="display:none"><h1>Book not found</h1><p>This book is not live yet. Browse the catalogue or request it on the contact page.</p><p><a class="btn" href="/books.html">Browse all books →</a> <a class="btn outline" href="/contact.html">Request this book</a></p></div>
</main>
<div class="modal-backdrop" id="buy-modal" role="dialog" aria-modal="true" aria-label="Buy this solved PDF"><div class="modal"><button class="close" onclick="closeBuy()" aria-label="Close">×</button><h2>Buy this solved PDF</h2><p><strong>Buy this solved PDF in Rs.100 only.</strong></p><p>Message us on WhatsApp with your book details and we will send you the PDF.</p><p><a class="btn whatsapp" id="wa-btn" href="https://wa.me/923018981055" target="_blank" rel="noopener">💬 Order on WhatsApp — Rs.100</a></p><p class="muted" style="font-size:14px;color:var(--muted)">Your book details are already filled in the WhatsApp message.</p></div></div>
<script>
async function initPreview(){
  const id = new URLSearchParams(location.search).get('id');
  let books = [];
  try{ books = await (await fetch('/assets/data/books.json')).json(); }catch(e){}
  const b = books.find(x=>x.id===id);
  document.getElementById('preview-loading').style.display = 'none';
  if(!b || !b.pdf){
    document.getElementById('preview-notfound').style.display = 'block';
    return;
  }
  document.getElementById('preview-content').style.display = 'block';
  document.getElementById('preview-title').textContent = b.title;
  document.title = 'Preview — ' + b.title + ' | Solved Sindh Textbook Board Books';
  document.getElementById('preview-chips').innerHTML = '<span class="chip">Class ' + b.cls + '</span> <span class="chip">' + b.subject + '</span> <span class="chip">' + b.medium + ' Medium</span> <span class="chip live">Preview Free</span>';
  document.getElementById('preview-desc').textContent = b.desc || '';
  document.getElementById('pdf-frame').src = '/' + b.pdf + '#toolbar=0&navpanes=0&scrollbar=0';
  const msg = 'Hi! I want to buy this solved PDF (Rs.100): ' + b.title + ' — Class ' + b.cls + ', ' + b.subject + ', ' + b.medium + ' Medium. Please send me the PDF.';
  document.getElementById('wa-btn').href = 'https://wa.me/923018981055?text=' + encodeURIComponent(msg);
  document.getElementById('buy-btn').addEventListener('click', ()=>{ document.getElementById('buy-modal').classList.add('open'); });
}
function closeBuy(){ document.getElementById('buy-modal')?.classList.remove('open'); }
document.addEventListener('click', e=>{ if(e.target && e.target.id==='buy-modal') closeBuy(); });
document.addEventListener('keydown', e=>{ if(e.key==='Escape') closeBuy(); });
document.addEventListener('DOMContentLoaded', initPreview);
</script>
""" + FOOTER
    w("preview.html", preview)

    # SEO files
    import sys
    sys.path.insert(0, SITE)
    from build_blog import POSTS
    urls = ["", "/books.html", "/solved.html", "/about.html", "/contact.html", "/privacy.html", "/terms.html", "/preview.html", "/blog/"]
    urls += [f"/blog/{p['slug']}.html" for p in POSTS]
    import math as _math
    _total_pages = max(1, _math.ceil(len(POSTS) / 30))
    urls += [f"/blog/page-{n}.html" for n in range(2, _total_pages + 1)]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sm += f'  <url><loc>{BASE}{u if u else "/"}</loc><lastmod>{TODAY}</lastmod></url>\n'
    sm += "</urlset>\n"
    w("sitemap.xml", sm)
    w("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    w("manifest.webmanifest", json.dumps({"name":"Solved Sindh Textbook Board Books","short_name":"Sindh Textbook Board Solved","start_url":"/","display":"standalone","background_color":"#ffffff","theme_color":"#0B6B4A","icons":[{"src":"/favicon.svg","sizes":"512x512","type":"image/svg+xml"}]}, indent=2))
    w("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0B6B4A"/><text x="32" y="44" font-family="Arial" font-size="34" font-weight="bold" fill="#fff" text-anchor="middle">S</text></svg>\n')
    w("assets/images/og.svg", '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630"><rect width="1200" height="630" fill="#0B6B4A"/><text x="60" y="200" font-family="Arial" font-size="64" font-weight="bold" fill="#fff">Solved Sindh Textbook Board Books</text><text x="60" y="280" font-family="Arial" font-size="32" fill="#DCE8E0">Preview solved exercises free — Sindhi · Urdu · English</text><text x="60" y="340" font-family="Arial" font-size="28" fill="#fff">Class 6 · 8 · 9 Islamiat notes live now</text></svg>\n')
    # README
    readme = f"""# Solved Sindh Textbook Board Books — Static Website

Free solved Sindh Textbook Board books & exercises for Sindh Board students (Sindhi, Urdu, English medium).
Pure static HTML/CSS/JS — no backend, no build step. Deploy anywhere (Vercel, GitHub Pages, Netlify).

## Live content
- **6 solved-notes PDFs live**: Class 6 / 8 / 9 Islamiat × Sindhi / Urdu (in `assets/pdfs/`).
- **{len(BOOKS)} catalogue entries** in `assets/data/books.json` (6 live + rest coming-soon).
- **{len(POSTS)} SEO blog posts** in `blog/` (generated by `build_blog.py`; daily engine in `gen/`).

## Preview locally
```bash
cd stbb-solved-website
python3 -m http.server 8000
# open http://localhost:8000
```

## Add a new book
1. Drop the PDF into `assets/pdfs/` (e.g. `Class10-Physics-SolvedExercises-English.pdf`).
2. Edit `assets/data/books.json` — copy a live entry, set `status: "live"`, `pdf: "assets/pdfs/<file>.pdf"`, `pages`, `desc`, `chapters`.
3. Or: add the entry to `BOOKS` in `build_site.py` and re-run `python3 build_site.py`.
4. The book appears automatically on Home, Books and Solved pages (JS renders from books.json).

## Add a blog post
Daily engine (15/day, from 2026-10-16): write a `gen/batch_XXX.py` batch file, run `python3 gen/build_batch.py batch_XXX BATCH_XXX` (validates, appends to `gen/extra_posts.json`, rebuilds blog + sitemap), then `python3 gen/push_batch.py "Day N" <files>` to push.
Manual single post: append a dict to `POSTS` in `build_blog.py` (slug, title, cat, desc, kw, intro, points).
2. Run `python3 build_blog.py` — it regenerates `blog/*.html`, `blog/index.html`, `blog/page-N.html`.
3. Run `python3 build_site.py` to refresh `sitemap.xml`.

## Deploy to Vercel
1. Push this folder to a GitHub repo (e.g. `stbb-solved-website`).
2. Vercel → New Project → import repo → Framework: **Other** → Deploy. No build command needed.
3. After deploy, replace `{BASE}` with your real domain in `build_site.py` / `build_blog.py`, re-run both scripts, and re-deploy.
4. Submit `https://YOUR-DOMAIN/sitemap.xml` in Google Search Console.

## Files
- `index.html`, `books.html`, `solved.html`, `about.html`, `contact.html`, `privacy.html`, `terms.html`
- `blog/` — 50 posts + index + page-2
- `assets/css/style.css`, `assets/js/main.js`, `assets/data/books.json`, `assets/pdfs/`
- `sitemap.xml`, `robots.txt`, `manifest.webmanifest`, `favicon.svg`
- `build_site.py`, `build_blog.py` — generators (source of truth for pages/blogs)

## Domain suggestions (check availability before buying)
1. **stbbsolved.pk** — exact-match, best for SEO in Pakistan
2. **solvedstbb.com** — global, easy to say
3. **stbbnotes.pk** — short, memorable, brandable
"""
    w("README.md", readme)
    print(f"Built core site: {len(BOOKS)} books ({len(REAL)} live), sitemap {len(urls)} URLs")

if __name__ == "__main__":
    build()
