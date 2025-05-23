const toggle = document.getElementById("mode-toggle"),
   body = document.body;
let currentTheme = localStorage.getItem("theme") || "custom";

function applyTheme(e) {
   body.classList.remove("light-mode", "dark-mode", "custom-mode"),  
   "dark" === e ? (body.classList.add("dark-mode"), toggle.innerHTML = '<span class="fa-solid fa-moon fa-lg"></span>') : "custom" === e ? (body.classList.add("custom-mode"), 
   toggle.innerHTML = '<span class="fa-solid fa-robot fa-lg" style="color: #789fe3;"></span>') : toggle.innerHTML = '<span class="fa-solid fa-cloud-sun fa-lg"></span>', localStorage.setItem("theme", e)
}
applyTheme(currentTheme), toggle.addEventListener("click", (() => {
   currentTheme = "light" === currentTheme ? "dark" : "dark" === currentTheme ? "custom" : "light", applyTheme(currentTheme)
}));
const scrollToTopButton = document.getElementById("scrollToTop");
window.addEventListener("scroll", (() => {
   const e = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight) * 100;
   scrollToTopButton.style.display = e > 37 ? "block" : "none"
})), scrollToTopButton.addEventListener("click", (() => {
   window.scrollTo({
      top: 0,
      behavior: "smooth"
   })
}));
const svg = document.getElementById("svg-eye"),
   pupil = svg.querySelector("circle[fill='#111']"),
   iris = svg.querySelector("circle[fill^='url(#irisGradient)']"),
   outerskin = svg.querySelector("circle[fill='url(#lid3D)']"),
   sclera = svg.querySelector("circle[fill='url(#sclera3D)']"),
   centerX = 100,
   centerY = 100,
   maxOffset = 10;

function typeText(e, t, o) {
   const l = document.getElementById(e);
   if (!l) return;
   const n = l.getAttribute("data-text") || "";
   l.textContent = "", l.classList.add("typing");
   let r = 0;
   ! function e() {
      r < n.length ? (l.textContent += n.charAt(r), r++, setTimeout(e, t)) : (l.classList.remove("typing"), o && o())
   }()
}
document.addEventListener("mousemove", (e => {
   const t = svg.getBoundingClientRect(),
      o = e.clientX - (t.left + t.width / 2),
      l = e.clientY - (t.top + t.height / 2),
      n = Math.min(10, Math.sqrt(o * o + l * l)),
      r = Math.atan2(l, o),
      c = Math.cos(r) * n,
      s = Math.sin(r) * n;
   pupil.setAttribute("cx", 100 + 1.18 * c), pupil.setAttribute("cy", 100 + 1.18 * s), iris.setAttribute("cx", 100 + c / 2), iris.setAttribute("cy", 100 + s / 2), outerskin.setAttribute("cx", 100 - .5 * c), outerskin.setAttribute("cy", 100 - .5 * s), sclera.setAttribute("cx", 100 - c / 4), sclera.setAttribute("cy", 100 - s / 4)
})), typeText("hero-name", 110, (() => {
   typeText("hero-title", 100, (() => {
      typeText("hero-tagline", 90, (() => {}))
   }))
}));


 
