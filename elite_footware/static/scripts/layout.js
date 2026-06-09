const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
const menuIcon = document.querySelector(".menu-icon");

if ("scrollRestoration" in history) {
  history.scrollRestoration = "manual";
}

window.addEventListener("pageshow", () => {
  if (!window.location.hash) {
    window.scrollTo(0, 0);
  }
});

if (menuToggle && navLinks) {
  const setMenuIcon = (isOpen) => {
    if (!menuIcon) {
      return;
    }

    menuIcon.classList.toggle("fa-bars", !isOpen);
    menuIcon.classList.toggle("fa-xmark", isOpen);
  };

  const closeMenu = () => {
    menuToggle.classList.remove("active");
    navLinks.classList.remove("active");
    menuToggle.setAttribute("aria-expanded", "false");
    setMenuIcon(false);
  };

  menuToggle.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("active");

    menuToggle.classList.toggle("active", isOpen);
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    setMenuIcon(isOpen);
  });

  navLinks.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
      closeMenu();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 768) {
      closeMenu();
    }
  });
}
