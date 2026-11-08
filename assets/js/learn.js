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

  /* ---------- book view: units -> lessons -> notes / mcq practice ---------- */
  var BOOK = null, UNITS = [], quiz = null;
  function unitsOf(book, learn) {
    if (learn && learn.chapters && learn.chapters.length) return learn.chapters;
    return (book.chapters || []).map(function (t) { return { title: t, notes_html: "", mcqs: [] }; });
  }
  function lessonsOf(unit) {
    if (unit.lessons && unit.lessons.length) return unit.lessons;
    if (unit.notes_html || (unit.mcqs && unit.mcqs.length)) return [{ title: unit.title, notes_html: unit.notes_html || "", mcqs: unit.mcqs || [] }];
    return [];
  }
  function lessonHas(lesson) { return MODE === "notes" ? !!lesson.notes_html : !!(lesson.mcqs && lesson.mcqs.length); }
  function setParam(k, v) {
    var url = new URL(location.href);
    if (v == null) url.searchParams.delete(k); else url.searchParams.set(k, v);
    history.replaceState(null, "", url);
  }
  function showUnits() {
    setParam("u", null); setParam("l", null); setParam("ch", null);
    var box = $("#chapter-list"), content = $("#learn-content");
    content.innerHTML = "";
    if (!UNITS.length) { box.innerHTML = '<p class="empty-note">Chapters for this book are coming soon.</p>'; return; }
    box.innerHTML = '<h2 class="learn-sec-title">' + (MODE === "notes" ? "Units — select a unit" : "Units — select a unit") + '</h2><div class="chapter-list">' + UNITS.map(function (u, i) {
      var ls = lessonsOf(u);
      var ready = ls.filter(lessonHas).length;
      return '<button type="button" class="chapter-btn" data-unit="' + i + '"><span class="chapter-num">' + (i + 1) + '</span><span class="chapter-name">' + esc(u.title) + '</span><span class="chapter-lessons">' + ls.length + (ls.length === 1 ? ' lesson' : ' lessons') + (ready && ready < ls.length ? ' · ' + ready + ' ready' : '') + '</span>' + (ls.length && !ready ? '<span class="chapter-soon">Coming soon</span>' : '') + '</button>';
    }).join("") + '</div>';
    Array.prototype.forEach.call(box.querySelectorAll(".chapter-btn"), function (b) {
      b.addEventListener("click", function () { showLessons(Number(b.getAttribute("data-unit"))); });
    });
  }
  function showLessons(ui) {
    setParam("u", ui + 1); setParam("l", null);
    var unit = UNITS[ui], lessons = lessonsOf(unit);
    var box = $("#chapter-list"), content = $("#learn-content");
    content.innerHTML = "";
    var back = '<button type="button" class="learn-back" id="back-units">&larr; All Units</button>';
    if (!lessons.length) { box.innerHTML = back + '<p class="empty-note">Lessons for this unit are coming soon.</p>'; }
    else {
      box.innerHTML = back + '<h2 class="learn-sec-title">' + esc(unit.title) + '</h2><div class="chapter-list">' + lessons.map(function (l, i) {
        return '<button type="button" class="chapter-btn" data-lesson="' + i + '"><span class="chapter-num">' + (i + 1) + '</span><span class="chapter-name">' + esc(l.title) + '</span>' + (lessonHas(l) ? '' : '<span class="chapter-soon">Coming soon</span>') + '</button>';
      }).join("") + '</div>';
      Array.prototype.forEach.call(box.querySelectorAll(".chapter-btn"), function (b) {
        b.addEventListener("click", function () { openLesson(ui, Number(b.getAttribute("data-lesson"))); });
      });
    }
    var bk = document.getElementById("back-units");
    if (bk) bk.addEventListener("click", showUnits);
  }
  function openLesson(ui, li) {
    setParam("u", ui + 1); setParam("l", li + 1);
    var unit = UNITS[ui], lessons = lessonsOf(unit), lesson = lessons[li];
    var box = $("#chapter-list"), content = $("#learn-content");
    box.innerHTML = '<button type="button" class="learn-back" id="back-lessons">&larr; Lessons of this unit</button>' +
      '<h2 class="learn-sec-title">' + esc(lesson.title) + '</h2>';
    document.getElementById("back-lessons").addEventListener("click", function () { showLessons(ui); });
    if (MODE === "notes") {
      var nav = '<div class="lesson-nav">' +
        (li > 0 ? '<button type="button" class="btn btn-ghost2" id="prev-lesson">&larr; Previous Lesson</button>' : '<span></span>') +
        (li < lessons.length - 1 ? '<button type="button" class="btn btn-primary" id="next-lesson">Next Lesson &rarr;</button>' : '') + '</div>';
      content.innerHTML = lesson.notes_html
        ? '<article class="easy-notes" dir="auto">' + lesson.notes_html + '</article>' + nav
        : '<p class="empty-note">Easy Notes for this lesson are coming soon.</p>';
      var pv = document.getElementById("prev-lesson"), nx = document.getElementById("next-lesson");
      if (pv) pv.addEventListener("click", function () { openLesson(ui, li - 1); });
      if (nx) nx.addEventListener("click", function () { openLesson(ui, li + 1); });
    } else {
      if (lesson.mcqs && lesson.mcqs.length) { quiz = { list: lesson.mcqs, i: 0, score: 0, locked: false }; renderQuestion(); }
      else { quiz = null; content.innerHTML = '<p class="empty-note">MCQs for this lesson are coming soon.</p>'; }
    }
    content.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  /* ---------- MCQ practice (app style) ---------- */
  var LETTERS = ["A", "B", "C", "D"];
  function renderQuestion() {
    var box = $("#learn-content");
    var q = quiz.list[quiz.i]; quiz.locked = false;
    var pct = Math.round((quiz.i / quiz.list.length) * 100);
    box.innerHTML = '<div class="mcq-card">' +
      '<div class="mcq-top"><span class="mcq-count">Question ' + (quiz.i + 1) + ' of ' + quiz.list.length + '</span><span class="mcq-score-chip">Score: ' + quiz.score + '</span></div>' +
      '<div class="mcq-progress"><i style="width:' + pct + '%"></i></div>' +
      '<div class="mcq-q" dir="auto">' + esc(q.q) + '</div>' +
      '<div class="mcq-opts">' + q.options.map(function (o, i) {
        return '<button type="button" class="mcq-opt" data-opt="' + i + '"><span class="opt-letter">' + LETTERS[i] + '</span><span class="opt-text" dir="auto">' + esc(o) + '</span></button>';
      }).join("") + '</div>' +
      '<div class="mcq-explain" style="display:none"></div>' +
      '<div class="mcq-nav"></div></div>';
    Array.prototype.forEach.call(box.querySelectorAll(".mcq-opt"), function (btn) {
      btn.addEventListener("click", function () { answerQuestion(btn, q); });
    });
  }
  function answerQuestion(btn, q) {
    if (!quiz || quiz.locked) return;
    quiz.locked = true;
    var picked = Number(btn.getAttribute("data-opt"));
    var box = $("#learn-content");
    var correct = picked === q.answer;
    if (correct) quiz.score++;
    Array.prototype.forEach.call(box.querySelectorAll(".mcq-opt"), function (b) {
      var i = Number(b.getAttribute("data-opt"));
      if (i === q.answer) b.classList.add("correct");
      else if (i === picked) b.classList.add("wrong");
      b.disabled = true;
    });
    var chip = box.querySelector(".mcq-score-chip");
    if (chip) chip.textContent = "Score: " + quiz.score;
    var bar = box.querySelector(".mcq-progress i");
    if (bar) bar.style.width = Math.round(((quiz.i + 1) / quiz.list.length) * 100) + "%";
    var ex = box.querySelector(".mcq-explain");
    ex.style.display = "";
    ex.innerHTML = '<div class="mcq-verdict ' + (correct ? "ok" : "bad") + '">' + (correct ? "✓ Correct" : "✗ Not correct") + ' — Correct answer: <b>' + LETTERS[q.answer] + '. <span dir="auto">' + esc(q.options[q.answer]) + '</span></b></div>' +
      (q.why ? '<div class="mcq-why-text" dir="auto">' + esc(q.why) + '</div>' : '');
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
    var pct = Math.round((quiz.score / quiz.list.length) * 100);
    var msg = pct >= 80 ? "Excellent — you remember this lesson very well." : pct >= 50 ? "Good — practice once more to make it perfect." : "Keep practicing — read the Easy Notes of this lesson, then try again.";
    box.innerHTML = '<div class="mcq-card mcq-result"><div class="mcq-score">' + quiz.score + ' / ' + quiz.list.length + '</div>' +
      '<div class="mcq-pct">' + pct + '%</div><p>' + msg + '</p>' +
      '<div class="mcq-result-btns"><button type="button" class="btn btn-primary" id="mcq-again">Practice Again</button></div></div>';
    document.getElementById("mcq-again").addEventListener("click", function () {
      quiz.i = 0; quiz.score = 0; renderQuestion();
    });
  }

  function initBook(bookId) {
    var cat = $("#catalogue-sec"); if (cat) cat.style.display = "none";
    var view = $("#learn-view"); if (view) view.style.display = "";
    var headPre = $("#learn-head"); if (headPre) headPre.innerHTML = '<p class="empty-note">Loading…</p>';
    Promise.all([
      fetch("/assets/data/books.json").then(function (r) { return r.json(); }),
      fetch("/assets/data/learn/" + encodeURIComponent(bookId) + ".json").then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })
    ]).then(function (res) {
      BOOK = (res[0] || []).filter(function (b) { return b.id === bookId; })[0];
      var head = $("#learn-head");
      if (!BOOK) { head.innerHTML = '<p class="empty-note">Book not found.</p>'; return; }
      UNITS = unitsOf(BOOK, res[1]);
      if (BOOK.medium === "Sindhi") view.classList.add("lang-sd");
      else if (BOOK.medium === "Urdu") view.classList.add("lang-ur");
      else if (BOOK.medium === "Arabic") view.classList.add("lang-naskh");
      document.title = BOOK.title + (MODE === "notes" ? " — Easy Notes" : " — MCQs Practice") + " | SolvedBooks.pk";
      head.innerHTML = '<nav class="crumbs"><a href="/">Home</a> › <a href="/' + MODE + '.html">' + (MODE === "notes" ? "Easy Notes" : "MCQs") + '</a> › <span>' + esc(BOOK.subject) + '</span></nav>' +
        '<div class="learn-head"><img class="learn-cover" src="/' + esc(BOOK.cover) + '" alt="' + esc(BOOK.title) + ' — official book cover">' +
        '<div class="learn-head-text"><h1 class="learn-book-title">' + esc(BOOK.title) + '</h1>' +
        '<div class="learn-chips"><span class="chip">' + esc(BOOK.board) + '</span><span class="chip">Class ' + (ROMAN[BOOK.cls] || BOOK.cls) + '</span><span class="chip">' + esc(BOOK.medium) + ' Medium</span></div>' +
        '<p class="learn-sub">' + (MODE === "notes" ? "Select a unit, then a lesson, to read its Easy Notes." : "Select a unit, then a lesson, to practice its MCQs.") + '</p></div></div>';
      var qs = new URLSearchParams(location.search);
      var u = Number(qs.get("u") || qs.get("ch"));
      var l = Number(qs.get("l"));
      if (u >= 1 && u <= UNITS.length) {
        if (l >= 1 && l <= lessonsOf(UNITS[u - 1]).length) openLesson(u - 1, l - 1);
        else showLessons(u - 1);
      } else showUnits();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var bookId = new URLSearchParams(location.search).get("book");
    if (bookId) initBook(bookId); else initCatalogue();
  });
})();
