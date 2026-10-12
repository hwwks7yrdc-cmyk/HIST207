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
