(function () {
  "use strict";
  var MODE = document.body.getAttribute("data-mode"); // notes | mcqs
  var ROMAN = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",11:"XI",12:"XII"};
  var BOOKS = [];
  var state = { board: "Sindh Textbook Board", medium: "", cls: "", q: "" };
  function $(s) { return document.querySelector(s); }
  function esc(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }

  /* ---------- catalogue (same design as Solved Books) ---------- */
  function cardHTML(b) {
    var live = b.status === "live";
    var pub = (ROMAN[b.cls] || ("Class " + b.cls)) + (live ? (b.pages ? " • " + b.pages + " pages" : "") : " • Coming Soon");
    var label = MODE === "notes" ? "Read Notes &rarr;" : "Practice MCQs &rarr;";
    var inner = '<div class="book-cover-wrap"><img class="book-img" src="/' + esc(b.cover) + '" alt="' + esc(b.title) + ' — official book cover" loading="lazy"><span class="book-medium-badge">' + esc(b.medium) + '</span></div>' +
      '<div class="book-info"><div class="book-title">' + esc(b.title) + '</div><div class="book-pub">' + pub + '</div>' +
      '<div class="book-actions"><span class="ba-open">' + label + '</span></div></div>';
    return '<a class="card card-link book-card" data-id="' + b.id + '" data-class="' + b.cls + '" href="/' + MODE + '.html?book=' + encodeURIComponent(b.id) + '">' + inner + '</a>';
  }
  function syncPills() {
    [["board-pills", "data-board", state.board], ["medium-pills", "data-medium", state.medium], ["class-pills", "data-cls", state.cls]].forEach(function (cfg) {
      var w = document.getElementById(cfg[0]); if (!w) return;
      Array.prototype.forEach.call(w.querySelectorAll(".feat-pill"), function (p) {
        p.classList.toggle("active", (p.getAttribute(cfg[1]) || "") === String(cfg[2]));
      });
    });
  }
  function renderGrid() {
    var grid = $("#learn-grid"); if (!grid) return;
    var list = BOOKS.filter(function (b) {
      if (state.board && b.board !== state.board) return false;
      if (state.medium && b.medium !== state.medium) return false;
      if (state.cls && String(b.cls) !== String(state.cls)) return false;
      if (state.q) {
        var hay = (b.title + " " + b.subject + " " + b.medium + " " + b.board + " Class " + b.cls).toLowerCase();
        if (hay.indexOf(state.q.toLowerCase()) < 0) return false;
      }
      return true;
    });
    grid.innerHTML = list.length ? list.map(cardHTML).join("") : '<p class="empty-note">No books match these filters.</p>';
    var c = $("#learn-count"); if (c) c.textContent = list.length + " books";
    var t = $("#learn-title");
    if (t) t.textContent = state.cls ? ("Class " + (ROMAN[state.cls] || state.cls) + (MODE === "notes" ? " Notes" : " MCQs")) : (MODE === "notes" ? "Easy Notes" : "MCQs Practice");
  }
  function pillWire(id, key, attr) {
    var wrap = document.getElementById(id); if (!wrap) return;
    wrap.addEventListener("click", function (e) {
      var btn = e.target.closest("[" + attr + "]"); if (!btn) return;
      e.preventDefault();
      state[key] = btn.getAttribute(attr) || "";
      syncPills(); renderGrid();
    });
  }
  function initCatalogue() {
    fetch("/assets/data/books.json").then(function (r) { return r.json(); }).then(function (data) {
      BOOKS = data || [];
      pillWire("board-pills", "board", "data-board");
      pillWire("medium-pills", "medium", "data-medium");
      pillWire("class-pills", "cls", "data-cls");
      var q = $("#q");
      if (q) q.addEventListener("input", function () { state.q = q.value; renderGrid(); });
      var clear = $("#clear-filters");
      if (clear) clear.addEventListener("click", function () {
        state = { board: "Sindh Textbook Board", medium: "", cls: "", q: "" };
        if (q) q.value = "";
        syncPills(); renderGrid();
      });
      syncPills(); renderGrid();
    }).catch(function () {
      var grid = $("#learn-grid");
      if (grid) grid.innerHTML = '<p class="empty-note">Books could not load. Please refresh the page.</p>';
    });
  }

  /* ---------- book view: chapters + notes / mcq practice ---------- */
  var quiz = null;
  function chapterButtons(book, learn, activeIdx) {
    var chapters = (learn && learn.chapters && learn.chapters.length) ? learn.chapters : (book.chapters || []).map(function (t) { return { title: t, notes_html: "", mcqs: [] }; });
    if (!chapters.length) return { html: '<p class="empty-note">Chapters for this book are coming soon.</p>', chapters: [] };
    var html = '<div class="chapter-list">' + chapters.map(function (ch, i) {
      var has = MODE === "notes" ? !!ch.notes_html : (ch.mcqs && ch.mcqs.length > 0);
      return '<button type="button" class="chapter-btn' + (i === activeIdx ? " active" : "") + '" data-ch="' + i + '"><span class="chapter-num">' + (i + 1) + '</span><span class="chapter-name">' + esc(ch.title) + '</span>' + (has ? '' : '<span class="chapter-soon">Coming soon</span>') + '</button>';
    }).join("") + '</div>';
    return { html: html, chapters: chapters };
  }
  function openChapter(book, chapters, idx) {
    var ch = chapters[idx]; if (!ch) return;
    Array.prototype.forEach.call(document.querySelectorAll(".chapter-btn"), function (b) {
      b.classList.toggle("active", Number(b.getAttribute("data-ch")) === idx);
    });
    var url = new URL(location.href); url.searchParams.set("ch", idx + 1);
    history.replaceState(null, "", url);
    var box = $("#learn-content");
    if (MODE === "notes") {
      box.innerHTML = ch.notes_html
        ? '<article class="easy-notes" dir="auto">' + ch.notes_html + '</article>'
        : '<p class="empty-note">Easy Notes for this chapter are coming soon.</p>';
    } else {
      if (ch.mcqs && ch.mcqs.length) { startQuiz(ch); }
      else { quiz = null; box.innerHTML = '<p class="empty-note">MCQs for this chapter are coming soon.</p>'; }
    }
    box.scrollIntoView({ behavior: "smooth", block: "start" });
  }
  function startQuiz(ch) {
    quiz = { list: ch.mcqs, i: 0, score: 0, locked: false, title: ch.title };
    renderQuestion();
  }
  function renderQuestion() {
    var box = $("#learn-content");
    var q = quiz.list[quiz.i]; quiz.locked = false;
    var html = '<div class="mcq-head"><span>Question ' + (quiz.i + 1) + ' of ' + quiz.list.length + '</span><span>Score: ' + quiz.score + '</span></div>' +
      '<div class="mcq-q" dir="auto">' + esc(q.q) + '</div><div class="mcq-opts">' +
      q.options.map(function (o, i) { return '<button type="button" class="mcq-opt" data-opt="' + i + '" dir="auto">' + esc(o) + '</button>'; }).join("") +
      '</div><div class="mcq-why" style="display:none" dir="auto"></div><div class="mcq-nav"></div>';
    box.innerHTML = html;
    Array.prototype.forEach.call(box.querySelectorAll(".mcq-opt"), function (btn) {
      btn.addEventListener("click", function () { answerQuestion(btn, q); });
    });
  }
  function answerQuestion(btn, q) {
    if (!quiz || quiz.locked) return;
    quiz.locked = true;
    var picked = Number(btn.getAttribute("data-opt"));
    var box = $("#learn-content");
    Array.prototype.forEach.call(box.querySelectorAll(".mcq-opt"), function (b) {
      var i = Number(b.getAttribute("data-opt"));
      if (i === q.answer) b.classList.add("correct");
      else if (i === picked) b.classList.add("wrong");
      b.disabled = true;
    });
    if (picked === q.answer) quiz.score++;
    var why = box.querySelector(".mcq-why");
    why.style.display = "";
    why.innerHTML = (picked === q.answer ? '<strong>Correct.</strong> ' : '<strong>Not correct.</strong> ') + esc(q.why || "");
    var nav = box.querySelector(".mcq-nav");
    var last = quiz.i === quiz.list.length - 1;
    nav.innerHTML = '<button type="button" class="btn btn-primary" id="mcq-next">' + (last ? "See Result" : "Next Question") + '</button>';
    document.getElementById("mcq-next").addEventListener("click", function () {
      quiz.i++;
      if (quiz.i < quiz.list.length) renderQuestion(); else renderResult();
    });
  }
  function renderResult() {
    var box = $("#learn-content");
    box.innerHTML = '<div class="mcq-result"><div class="mcq-score">' + quiz.score + ' / ' + quiz.list.length + '</div>' +
      '<p>Practice finished for this chapter. Practice again to remember it better.</p>' +
      '<button type="button" class="btn btn-primary" id="mcq-again">Practice Again</button></div>';
    document.getElementById("mcq-again").addEventListener("click", function () {
      quiz.i = 0; quiz.score = 0; renderQuestion();
    });
  }
  function initBook(bookId) {
    var cat = $("#catalogue-sec"); if (cat) cat.style.display = "none";
    var view = $("#learn-view"); if (view) view.style.display = "";
    Promise.all([
      fetch("/assets/data/books.json").then(function (r) { return r.json(); }),
      fetch("/assets/data/learn/" + encodeURIComponent(bookId) + ".json").then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })
    ]).then(function (res) {
      var book = (res[0] || []).filter(function (b) { return b.id === bookId; })[0];
      var learn = res[1];
      var head = $("#learn-head"), listBox = $("#chapter-list"), content = $("#learn-content");
      if (!book) { head.innerHTML = '<p class="empty-note">Book not found.</p>'; return; }
      document.title = book.title + (MODE === "notes" ? " — Easy Notes" : " — MCQs Practice") + " | SolvedBooks.pk";
      head.innerHTML = '<nav class="crumbs"><a href="/">Home</a> › <a href="/' + MODE + '.html">' + (MODE === "notes" ? "Easy Notes" : "MCQs") + '</a> › <span>' + esc(book.subject) + '</span></nav>' +
        '<div class="learn-head"><img class="learn-cover" src="/' + esc(book.cover) + '" alt="' + esc(book.title) + ' — official book cover">' +
        '<div><h1 class="learn-book-title">' + esc(book.title) + '</h1>' +
        '<div class="learn-chips"><span class="chip">' + esc(book.board) + '</span><span class="chip">Class ' + (ROMAN[book.cls] || book.cls) + '</span><span class="chip">' + esc(book.medium) + ' Medium</span></div>' +
        '<p class="learn-sub">' + (MODE === "notes" ? "Select a chapter to read its Easy Notes." : "Select a chapter to practice its MCQs.") + '</p></div></div>';
      var built = chapterButtons(book, learn, -1);
      listBox.innerHTML = built.html;
      listBox.addEventListener("click", function (e) {
        var btn = e.target.closest(".chapter-btn"); if (!btn) return;
        openChapter(book, built.chapters, Number(btn.getAttribute("data-ch")));
      });
      var chParam = Number(new URLSearchParams(location.search).get("ch"));
      if (chParam >= 1 && chParam <= built.chapters.length) openChapter(book, built.chapters, chParam - 1);
      else if (content) content.innerHTML = "";
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var bookId = new URLSearchParams(location.search).get("book");
    if (bookId) initBook(bookId); else initCatalogue();
  });
})();
