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
  // Featured class-filter pills (index featured grid + solved page)
  document.querySelectorAll('.feat-pills').forEach(pills=>{
    pills.addEventListener('click', e=>{
      const btn = e.target.closest('.feat-pill'); if(!btn) return;
      pills.querySelectorAll('.feat-pill').forEach(p=>p.classList.remove('active'));
      btn.classList.add('active');
      const grid = document.getElementById(pills.dataset.grid); if(!grid) return;
      const f = btn.dataset.filter;
      grid.querySelectorAll('.card').forEach(card=>{ card.style.display = (f==='all' || card.dataset.class===f) ? '' : 'none'; });
    });
  });
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
function subjSlug(subject){
  const map = {'Sindhi':'sindhi','Urdu':'urdu','English':'english','Arabic':'arabic','Math':'math','Science':'science','Social Studies':'social-studies','Islamiat':'islamiat','Mazhabi Taleemat':'mazhabi-taleemat','Computer':'computer','Physics':'physics','Chemistry':'chemistry','Biology':'biology','Pakistan Studies':'pakistan-studies','Mathematics':'math'};
  return map[subject] || 'science';
}
function subjectCover(b){
  if(b.cover) return b.cover;
  return 'assets/images/covers/subjects/' + subjSlug(b.subject) + '.svg';
}
const BOOK_IC = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 4h6a4 4 0 0 1 4 4v12a3 3 0 0 0-3-3H2z"/><path d="M22 4h-6a4 4 0 0 0-4 4v12a3 3 0 0 1 3-3h7z"/></svg>';
const CAP_IC = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12.4V16c0 1.66 2.69 3 6 3s6-1.34 6-3v-3.6"/><path d="M22 10v6"/></svg>';
const STAR_IC = '<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.6l2.9 5.87 6.48.94-4.69 4.57 1.11 6.45L12 17.47l-5.8 2.96 1.11-6.45L2.62 9.41l6.48-.94z"/></svg>';
const SPROUT_IC = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21v-7"/><path d="M12 14c0-3.2-2.6-5.4-6.5-5.4 0 3.9 2.6 5.4 6.5 5.4z"/><path d="M12 12.5c0-3.2 2.6-5.4 6.5-5.4 0 3.9-2.6 5.4-6.5 5.4z"/></svg>';
function cardHTML(b){
  const live = b.status==='live';
  const slug = subjSlug(b.subject);
  const cover = subjectCover(b);
  const btn = live ? `<span class="btn-open">${BOOK_IC} Open &rarr;</span>` : `<button class="btn-open" type="button">Notify me</button>`;
  // Hero = user's thumbnail theme image (CSS background, shown in full);
  // the book's own real cover is seated on the scene book's front face.
  const hero = `<div class="bk-hero"><img class="bk-cover" src="/${cover}" alt="${b.title} — official book cover" loading="lazy" onerror="this.style.display='none'"></div>`;
  const inner = `${hero}<div class="card-body"><span class="subj-tag ${slug}">${BOOK_IC} ${b.subject}</span><h3>${b.title}</h3><p class="bk-tags"><span class="bk-tag t-class">${CAP_IC} Class ${b.cls}</span><span class="bk-tag t-subj">${BOOK_IC} ${b.subject}</span><span class="bk-tag t-med">${STAR_IC} ${b.medium} Medium</span></p><p class="card-desc">${b.desc}</p><div class="actions">${btn}<span class="bk-better">${SPROUT_IC}<span>Better<br>Learning</span></span></div></div>`;
  if(live) return `<a class="card card-link book-card" data-id="${b.id}" data-class="${b.cls}" href="/preview.html?id=${b.id}">${inner}</a>`;
  return `<article class="card book-card" data-id="${b.id}" data-class="${b.cls}" onclick="openBook('${b.id}')">${inner}</article>`;
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
  const count = document.getElementById('books-count'); if(count) count.textContent = filtered.length + ' solved notes found';
  grid.innerHTML = filtered.length ? filtered.map(cardHTML).join('') : '<p>No solved notes match your filters. Try clearing the search or choose another class/medium.</p>';
}
// PDF.js inline viewer — renders PDF pages as canvases (works on mobile, no browser PDF plugin).
const _pdfState = {};
async function renderPDF(url, containerId){
  const el = document.getElementById(containerId); if(!el) return;
  el.innerHTML = '<p>Loading PDF…</p>';
  try{
    pdfjsLib.GlobalWorkerOptions.workerSrc = '/assets/js/pdf.worker.min.js';
    const pdf = await pdfjsLib.getDocument(url).promise;
    _pdfState[containerId] = {pdf, scale: 1, container: el};
    await _drawPDF(_pdfState[containerId]);
  }catch(e){ el.innerHTML = '<p>Could not load this PDF. Please try again.</p>'; }
}
async function _drawPDF(st){
  const el = st.container; el.innerHTML = '';
  const n = st.pdf.numPages;
  const first = await st.pdf.getPage(1);
  const w = el.clientWidth || 800;
  const base = w / first.getViewport({scale:1}).width;
  const scale = base * st.scale;
  for(let i=1;i<=n;i++){
    const p = await st.pdf.getPage(i);
    const vp = p.getViewport({scale});
    const cv = document.createElement('canvas');
    cv.width = Math.floor(vp.width); cv.height = Math.floor(vp.height);
    el.appendChild(cv);
    await p.render({canvasContext: cv.getContext('2d'), viewport: vp}).promise;
  }
}
function zoomPDF(containerId, dir){
  const st = _pdfState[containerId]; if(!st) return;
  st.scale = Math.max(0.5, Math.min(3, st.scale + dir*0.25));
  _drawPDF(st);
}
async function openBook(id){
  const books = await loadBooks();
  const b = books.find(x=>x.id===id); if(!b) return;
  const modal = document.getElementById('book-modal'); const body = document.getElementById('modal-body');
  const chapters = (b.chapters||[]).length ? '<h3>Chapters covered</h3><ul>'+b.chapters.map(c=>'<li>'+c+'</li>').join('')+'</ul>' : '<p>This book is being prepared. Join the list below and we will share it as soon as it is ready.</p>';
  const coverImg = b.cover ? `<div class="book-stage modal-book"><div class="book3d"><div class="book3d-back"></div><div class="book3d-spine"></div><img class="book3d-front" src="/${b.cover}" alt="${b.title} — official book cover"><div class="book3d-pages"></div><div class="book3d-shade"></div></div></div>` : '';
  if(b.pdf){
    // Live books open on their own preview page (full-page viewer), not in the modal.
    location.href = '/preview.html?id=' + b.id;
    return;
  }
  modal.querySelector('.modal').classList.remove('pdf-modal');
  body.innerHTML = `${coverImg}<h2>${b.title}</h2><p><span class="chip">Class ${b.cls}</span> <span class="chip">${b.subject}</span> <span class="chip">${b.medium} Medium</span> <span class="chip soon">Coming Soon</span></p><p>${b.desc}</p>${chapters}<p><a class="btn outline" href="/contact.html">Request this book</a></p><p><a href="/books.html">← Back to solved notes</a></p>`;
  modal.classList.add('open');
}
function closeModal(){ document.getElementById('book-modal')?.classList.remove('open'); }
document.addEventListener('click', e=>{ if(e.target && e.target.id==='book-modal') closeModal(); });
document.addEventListener('keydown', e=>{ if(e.key==='Escape') closeModal(); });

/* Google Analytics 4 (gtag.js) — G-6N54Z7LQTB. Loaded here because every
   page on Solved STBB Books includes this shared script. */
(function () {
  if (window.__ga4Loaded) return;
  window.__ga4Loaded = true;
  if (document.querySelector('script[src*="googletagmanager.com/gtag/js"]')) return;
  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  window.gtag = gtag;
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=G-6N54Z7LQTB';
  document.head.appendChild(s);
  gtag('js', new Date());
  gtag('config', 'G-6N54Z7LQTB');
})();
