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
function cardHTML(b){
  const live = b.status==='live';
  const slug = subjSlug(b.subject);
  const cover = subjectCover(b);
  const badge = live ? '<span class="live-badge"><i></i>Free</span>' : '<span class="live-badge soon"><i></i>Coming Soon</span>';
  const btn = live ? `<span class="btn-open">${BOOK_IC} Open &rarr;</span>` : `<button class="btn-open">Notify me</button>`;
  const coverEl = live
    ? `<div class="book-stage"><div class="book3d"><div class="book3d-back"></div><div class="book3d-spine"></div><img class="book3d-front" src="/${cover}" alt="${b.title} — official book cover" loading="lazy"><div class="book3d-pages"></div><div class="book3d-shade"></div></div>${badge}</div>`
    : `<div class="card-cover"><img src="/${cover}" alt="${b.title} — illustrated cover" loading="lazy">${badge}</div>`;
  const inner = `${coverEl}<div class="card-body"><span class="subj-tag ${slug}">${BOOK_IC} ${b.subject}</span><h3>${b.title}</h3><p class="card-meta"><span class="chip">Class ${b.cls}</span> <span class="chip">${b.subject}</span> <span class="chip">${b.medium} Medium</span></p><p class="card-desc">${b.desc}</p><div class="actions">${btn}</div></div>`;
  if(live) return `<a class="card card-link" data-id="${b.id}" data-class="${b.cls}" href="/preview.html?id=${b.id}">${inner}</a>`;
  return `<article class="card" data-id="${b.id}" data-class="${b.cls}" onclick="openBook('${b.id}')">${inner}</article>`;
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
