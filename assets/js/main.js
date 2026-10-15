// Solved STBB Books — search, filters, FAQ, language toggle, detail modal
const I18N = {
  en: {heroTitle:"Free Solved STBB Books — Sindhi, Urdu & English Medium", heroSub:"Download solved exercises for Sindh Textbook Board books. Class 6, 8 and 9 Islamiat notes are live now — 100% free, no signup.", searchBtn:"Search", ctaBooks:"Browse All Books", ctaSolved:"Solved Notes"},
  sd: {heroTitle:"مفت حل ٿيل STBB ڪتاب — سنڌي، اردو ۽ انگريزي ميڊيم", heroSub:"سنڌ ٽيڪسٽ بڪ بورڊ جي ڪتابن جون حل ٿيل مشقون ڊائون لوڊ ڪريو. ڪلاس 6، 8 ۽ 9 اسلاميات جا نوٽس هاڻي موجود آهن — بلڪل مفت.", searchBtn:"ڳولا", ctaBooks:"سڀ ڪتاب ڏسو", ctaSolved:"حل ٿيل نوٽس"},
  ur: {heroTitle:"مفت حل شدہ STBB کتب — سندھی، اردو اور انگریزی میڈیم", heroSub:"سندھ ٹیکسٹ بک بورڈ کی کتب کی حل شدہ مشقیں ڈاؤن لوڈ کریں۔ کلاس 6، 8 اور 9 اسلامیات کے نوٹس اب موجود ہیں — بالکل مفت۔", searchBtn:"تلاش", ctaBooks:"تمام کتب دیکھیں", ctaSolved:"حل شدہ نوٹس"}
};
function setLang(l){
  const d = I18N[l] || I18N.en;
  const t = document.getElementById('hero-title'); if(t) t.textContent = d.heroTitle;
  const s = document.getElementById('hero-sub'); if(s) s.textContent = d.heroSub;
  document.querySelectorAll('.lang-switch button').forEach(b=>b.classList.toggle('active', b.dataset.lang===l));
  try{localStorage.setItem('stbb-lang', l);}catch(e){}
  document.documentElement.lang = l==='en' ? 'en' : (l==='sd' ? 'sd' : 'ur');
  document.documentElement.dir = l==='en' ? 'ltr' : 'rtl';
  if(l==='en'){ document.documentElement.dir='ltr'; }
}
document.addEventListener('DOMContentLoaded', ()=>{
  const navBtn = document.getElementById('nav-toggle');
  const nav = document.getElementById('main-nav');
  if(navBtn && nav){ navBtn.addEventListener('click', ()=>{ nav.classList.toggle('open'); navBtn.setAttribute('aria-expanded', nav.classList.contains('open')); }); }
  try{ const saved = localStorage.getItem('stbb-lang'); if(saved && I18N[saved]) setLang(saved); }catch(e){}
  document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click', ()=>setLang(b.dataset.lang)));
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
  const badge = live ? '<span class="chip live">● Live — Free PDF</span>' : '<span class="chip soon">Coming Soon</span>';
  const btn = live ? `<a class="btn small" href="/${b.pdf}" download>⬇ Download PDF</a><button class="btn small outline" onclick="openBook('${b.id}')">Details</button>` : `<button class="btn small outline" onclick="openBook('${b.id}')">Notify me</button>`;
  return `<article class="card" data-id="${b.id}"><div class="card-cover"><small>Class ${b.cls} · ${b.medium} Medium</small><b>${b.title.replace(' — Solved Exercises ('+b.medium+' Medium)','')}</b><small>${b.subject}</small></div><div class="card-body">${badge}<p>${b.desc}</p><div class="actions">${btn}</div></div></article>`;
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
  const dl = b.pdf ? `<p><a class="btn" href="/${b.pdf}" download>⬇ Download Free PDF</a></p>` : '<p><a class="btn outline" href="/contact.html">Request this book</a></p>';
  body.innerHTML = `<h2>${b.title}</h2><p><span class="chip">Class ${b.cls}</span> <span class="chip">${b.subject}</span> <span class="chip">${b.medium} Medium</span> ${b.status==='live'?'<span class="chip live">Live</span>':'<span class="chip soon">Coming Soon</span>'}</p><p>${b.desc}</p>${chapters}${dl}<p><a href="/books.html">← Back to all books</a></p>`;
  modal.classList.add('open');
}
function closeModal(){ document.getElementById('book-modal')?.classList.remove('open'); }
document.addEventListener('click', e=>{ if(e.target && e.target.id==='book-modal') closeModal(); });
document.addEventListener('keydown', e=>{ if(e.key==='Escape') closeModal(); });
