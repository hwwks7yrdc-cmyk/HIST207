/* Duplicate Sample — small behaviours, no dependencies.
   1. the four-field label reveal
   2. the depth marker
   Everything degrades: with JS off, hidden fields are shown by the <noscript> rule. */
(function () {
  "use strict";

  /* ---- 1. label reveal ------------------------------------------------ */
  document.querySelectorAll(".field--hidden").forEach(function (field) {
    var btn = field.querySelector(".reveal");
    var val = field.querySelector(".field__v");
    if (!btn || !val) return;
    field.setAttribute("data-open", "false");
    btn.setAttribute("aria-expanded", "false");
    btn.addEventListener("click", function () {
      var open = field.getAttribute("data-open") === "true";
      field.setAttribute("data-open", open ? "false" : "true");
      btn.setAttribute("aria-expanded", open ? "false" : "true");
      btn.textContent = open ? "reveal" : "hide";
    });
  });

  /* ---- 2. depth marker ------------------------------------------------ */
  var fill = document.querySelector(".depth__fill");
  if (fill) {
    var tick = function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? Math.min(1, Math.max(0, window.scrollY / h)) : 0;
      fill.style.height = (p * 100) + "%";
    };
    tick();
    window.addEventListener("scroll", tick, { passive: true });
    window.addEventListener("resize", tick);
  }

  /* ---- 3. flag dark pages so the depth marker keeps its contrast ------- */
  if (document.body.dataset.tone === "dark") {
    document.documentElement.classList.add("dark-page");
  }
})();

/* ===================================================================== */
/* Added behaviours. Each guards its own elements, so every page loads    */
/* the same file and runs only what it has.                              */
/* ===================================================================== */
(function () {
  "use strict";

  var STORE = "ds.opened.v1";

  /* ---- shared: the record of which closed fields were opened --------- */
  function load() {
    try {
      var raw = window.localStorage.getItem(STORE);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }
  function save(o) {
    try { window.localStorage.setItem(STORE, JSON.stringify(o)); } catch (e) {}
  }
  function count(o) { return Object.keys(o).length; }

  var TOTAL = 18;   /* nine works, two closed fields each */
  var opened = load();

  function paint() {
    var n = count(opened);
    var box = document.querySelector("[data-seen]");
    if (box) {
      box.hidden = n === 0;
      var b = box.querySelector("b");
      if (b) b.textContent = String(n);
    }
    document.querySelectorAll("[data-progress]").forEach(function (p) {
      p.hidden = n === 0;
      if (n === 0) return;
      p.innerHTML = n >= TOTAL
        ? "You opened every one of the eighteen closed fields. Whatever else the collection "
          + "withholds, it is not withholding it from you."
        : "So far you have opened <b>" + n + "</b> of the exhibition’s <b>" + TOTAL
          + "</b> closed fields. The rest are still shut.";
    });
    document.querySelectorAll(".pl-slot").forEach(function (a) {
      var slug = (a.getAttribute("href") || "").split("#")[1];
      if (!slug) return;
      var any = Object.keys(opened).some(function (k) { return k.indexOf(slug + "-") === 0; });
      if (any) a.setAttribute("data-seen", "true");
    });
  }

  /* record an opening; the reveal itself is handled further up this file */
  document.querySelectorAll(".field--hidden[data-key]").forEach(function (field) {
    var btn = field.querySelector(".reveal");
    if (!btn) return;
    btn.addEventListener("click", function () {
      if (field.getAttribute("data-open") === "true") {
        opened[field.getAttribute("data-key")] = 1;
        save(opened);
        paint();
      }
    });
  });
  paint();

  /* ---- the register: two independent filters ------------------------- */
  var table = document.querySelector(".reg");
  if (table) {
    var state = { room: "all", access: "all" };
    var rows = Array.prototype.slice.call(table.querySelectorAll("tbody tr"));
    var countEl = document.querySelector("[data-count]");
    var emptyEl = document.querySelector("[data-empty]");
    var WORDS = ["None", "One", "Two", "Three", "Four", "Five",
                 "Six", "Seven", "Eight", "Nine"];

    function apply() {
      var shown = 0;
      rows.forEach(function (tr) {
        var ok = (state.room === "all" || tr.dataset.room === state.room)
              && (state.access === "all" || tr.dataset.access === state.access);
        tr.hidden = !ok;
        if (ok) shown++;
      });
      if (countEl) countEl.textContent = WORDS[shown] + " of nine";
      if (emptyEl) emptyEl.hidden = shown !== 0;
    }

    document.querySelectorAll(".chip").forEach(function (chip) {
      chip.addEventListener("click", function () {
        var kind = chip.dataset.filter;
        state[kind] = chip.dataset.value;
        document.querySelectorAll('.chip[data-filter="' + kind + '"]').forEach(function (c) {
          c.setAttribute("aria-pressed", String(c === chip));
        });
        apply();
      });
    });
    apply();
  }

  /* ---- the withdrawal slip ------------------------------------------- */
  var form = document.getElementById("slipform");
  var slip = document.getElementById("slip");
  if (form && slip) {
    var sel = document.getElementById("f-work");
    var printBtn = document.querySelector("[data-print]");
    var dlBtn = document.querySelector("[data-download]");

    function put(key, value) {
      var el = slip.querySelector('[data-s="' + key + '"]');
      if (el) el.textContent = value;
    }

    /* a work can be pre-selected from a label: withdrawal.html?work=sansour */
    try {
      var want = new URLSearchParams(window.location.search).get("work");
      if (want && sel.querySelector('option[value="' + CSS.escape(want) + '"]')) {
        sel.value = want;
      }
    } catch (e) {}

    function preview() {
      var o = sel.options[sel.selectedIndex];
      put("code", o.dataset.code);
      put("title", o.textContent.split("·").slice(1).join("·").trim());
      put("room", o.dataset.room.replace("&middot;", "·"));
      put("kept", o.dataset.kept);
      put("rule", o.dataset.rule);
    }
    sel.addEventListener("change", preview);
    preview();

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var name = form.name.value.trim();
      var why = form.why.value.trim();
      if (!name || !why) {
        (name ? form.why : form.name).focus();
        return;
      }
      preview();
      put("name", name);
      put("aff", form.aff.value.trim() || "Nobody. The request is personal.");
      put("why", why);
      put("ack", form.ack.checked
        ? "Accepted. A refusal needs no reason."
        : "Not accepted.");
      put("when", new Date().toLocaleDateString(undefined,
        { year: "numeric", month: "long", day: "numeric" }));
      slip.setAttribute("data-ready", "true");
      if (printBtn) printBtn.disabled = false;
      if (dlBtn) dlBtn.disabled = false;
      slip.scrollIntoView({ behavior: "smooth", block: "nearest" });
    });

    form.addEventListener("reset", function () {
      window.setTimeout(function () {
        ["name", "aff", "why"].forEach(function (k) { put(k, "—"); });
        put("ack", "Not accepted");
        put("when", "—");
        slip.removeAttribute("data-ready");
        if (printBtn) printBtn.disabled = true;
        if (dlBtn) dlBtn.disabled = true;
        preview();
      }, 0);
    });

    if (printBtn) printBtn.addEventListener("click", function () { window.print(); });

    if (dlBtn) dlBtn.addEventListener("click", function () {
      var lines = ["DUPLICATE SAMPLE", "Withdrawal request", ""];
      slip.querySelectorAll(".slip__fields div").forEach(function (d) {
        lines.push(d.querySelector("dt").textContent + ": "
                 + d.querySelector("dd").textContent);
      });
      lines.push("", slip.querySelector('[data-s="code"]').textContent + "  "
               + slip.querySelector('[data-s="title"]').textContent);
      lines.push("", "No record of this request is held by the exhibition.");
      var blob = new Blob([lines.join("\n")], { type: "text/plain;charset=utf-8" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "withdrawal-request.txt";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
    });
  }

  /* ---- the wall: let a vertical wheel move it sideways ---------------- */
  var track = document.querySelector(".wall__track");
  if (track) {
    track.addEventListener("wheel", function (ev) {
      if (Math.abs(ev.deltaY) <= Math.abs(ev.deltaX)) return;
      var max = track.scrollWidth - track.clientWidth;
      var at = track.scrollLeft;
      /* hand the page back the scroll once the wall has run out */
      if ((ev.deltaY > 0 && at >= max - 1) || (ev.deltaY < 0 && at <= 1)) return;
      ev.preventDefault();
      track.scrollLeft = at + ev.deltaY;
    }, { passive: false });
  }
})();

/* ===================================================================== */
/* The descent: the entry sequence on the entrance page.                  */
/*                                                                        */
/* It is an overlay over a page that is already fully rendered beneath,   */
/* so nothing here is load-bearing. With scripting off the markup keeps   */
/* its `hidden` attribute and the entrance behaves exactly as it always   */
/* did. The flight itself is declared in CSS and starts the moment the    */
/* element is laid out; this file only decides whether to show it, and    */
/* when to take it away.                                                  */
/* ===================================================================== */
(function () {
  "use strict";

  var tun = document.getElementById("descent");
  if (!tun) return;

  var HOLD = 1.5;
  var FLY = parseFloat(tun.style.getPropertyValue("--dur-fly")) || 7;
  var root = document.documentElement;
  var still = window.matchMedia &&
              window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var timer = null, running = false;

  function onKey(ev) {
    if (ev.key === "Escape" || ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); end(); }
  }
  function onSkip() { end(); }
  function onBackdrop(ev) { if (ev.target === tun) end(); }

  function end() {
    if (!running) return;
    running = false;
    window.clearTimeout(timer);
    tun.classList.add("tun--out");
    root.classList.remove("tun-lock");
    document.removeEventListener("keydown", onKey);
    tun.removeEventListener("click", onBackdrop);
    var skip = tun.querySelector(".tun__skip");
    if (skip) skip.removeEventListener("click", onSkip);
    window.setTimeout(function () {
      tun.hidden = true;
      tun.classList.remove("tun--out");
    }, 900);
    if (window.location.hash === "#descend" && window.history.replaceState) {
      window.history.replaceState(null, "", window.location.pathname);
    }
  }

  function play() {
    if (running) return;
    running = true;
    /* hiding and showing restarts the CSS animations, which is what makes a
       replay possible without reloading the page */
    tun.hidden = true;
    void tun.offsetWidth;
    root.classList.add("tun-lock");
    window.scrollTo(0, 0);
    tun.hidden = false;
    document.addEventListener("keydown", onKey);
    tun.addEventListener("click", onBackdrop);
    var skip = tun.querySelector(".tun__skip");
    if (skip) skip.addEventListener("click", onSkip);
    /* No autofocus: a focus ring on the skip button would be the loudest
       thing on screen for the whole sequence. Escape is handled on the
       document, and Tab reaches the button first. */
    timer = window.setTimeout(end, (still ? 3.4 : FLY + HOLD) * 1000);
  }

  /* Wait for the plates, but never for long: a slow connection must not be
     able to hold up the entrance. Whatever has arrived at the cap is what
     flies. */
  function whenReady(run) {
    var imgs = [].slice.call(tun.querySelectorAll("img"));
    var left = imgs.length;
    var went = false;
    function go() { if (!went) { went = true; run(); } }
    if (!left || still) { go(); return; }
    imgs.forEach(function (im) {
      if (im.complete) { if (--left === 0) go(); return; }
      im.addEventListener("load", function () { if (--left === 0) go(); });
      im.addEventListener("error", function () { if (--left === 0) go(); });
    });
    window.setTimeout(go, 1400);
  }

  /* A replay asked for from inside the page changes only the fragment, so the
     document is never reloaded and nothing below would ever run again. */
  window.addEventListener("hashchange", function () {
    if (window.location.hash === "#descend") whenReady(play);
  });

  /* The sequence plays on every arrival at the entrance. It used to play once
     per browser, remembered under ds.descent.v1; that key is no longer read or
     written, and any value left in a visitor's browser from before is ignored.
     The one exception stays: somebody who deep-links to a section of this page
     knows where they are going and is not held up. */
  var asked = window.location.hash === "#descend";
  if (!asked && window.location.hash && window.location.hash !== "#") return;
  whenReady(play);
})();

/* ===================================================================== */
/* The depth marker is page chrome and floats over everything at the      */
/* middle of the right edge. Several bands run edge to edge — the preview */
/* wall, the wall in Room II, and every work's opening photograph — so    */
/* the marker lands 40px inside the image and reads as a line drawn       */
/* across the artwork. On dark pictures nobody notices; on a white        */
/* gallery wall it is plainly wrong. It yields while such a band crosses  */
/* the middle of the viewport, and comes back after. The entrance is      */
/* deliberately not in the list: there the marker sits in the dark scrim  */
/* at the right of the vault photograph, where it belongs.                */
/* ===================================================================== */
(function () {
  "use strict";
  var depth = document.querySelector(".depth");
  var bands = document.querySelectorAll(".tiles, .wall__track, .work__fig");
  if (!depth || !bands.length || !("IntersectionObserver" in window)) return;

  var on = [];
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      var i = on.indexOf(e.target);
      if (e.isIntersecting && i < 0) on.push(e.target);
      else if (!e.isIntersecting && i > -1) on.splice(i, 1);
    });
    document.documentElement.classList.toggle("depth-off", on.length > 0);
  }, { rootMargin: "-46% 0px -46% 0px" });

  Array.prototype.forEach.call(bands, function (el) { io.observe(el); });
})();
