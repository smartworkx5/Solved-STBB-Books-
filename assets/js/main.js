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
