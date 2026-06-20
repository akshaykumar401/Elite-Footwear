document.addEventListener("DOMContentLoaded", () => {
  const filterToggle = document.querySelector(".catalog-filter");
  const filterDrawer = document.getElementById("filter-drawer");
  const filterButtons = document.querySelectorAll(".filter-btn");
  const productGrid = document.querySelector(".product-grid");
  const productCards = document.querySelectorAll(".product-card");
  const countText = document.querySelector(".count-text");
  const countShowing = document.querySelector(".count-showing");

  let selectedCategory = "All";
  let selectedGender = "All";
  let selectedSort = "newest";

  // Toggle filter drawer
  if (filterToggle && filterDrawer) {
    filterToggle.addEventListener("click", () => {
      const isOpen = filterDrawer.classList.toggle("is-open");
      filterToggle.classList.toggle("is-active", isOpen);
    });
  }

  // Handle filter/sort updates
  function updateGallery() {
    // 1. Filter matching items
    let visibleCount = 0;
    
    productCards.forEach((card) => {
      const category = card.getAttribute("data-category");
      const gender = card.getAttribute("data-gender");

      const categoryMatch = selectedCategory === "All" || category === selectedCategory;
      const genderMatch = selectedGender === "All" || gender === selectedGender;
      const isVisible = categoryMatch && genderMatch;

      if (isVisible) {
        visibleCount++;
        card.classList.remove("hidden-card");
        void card.offsetHeight; // force layout recalculation for transition
        card.classList.remove("fade-out");
      } else {
        card.classList.add("fade-out");
        // Hide after animation finishes (350ms)
        setTimeout(() => {
          if (card.classList.contains("fade-out")) {
            card.classList.add("hidden-card");
          }
        }, 350);
      }
    });

    // 2. Sort items in DOM
    const sortedCards = Array.from(productCards);
    sortedCards.sort((a, b) => {
      if (selectedSort === "newest") {
        return parseInt(b.getAttribute("data-newest")) - parseInt(a.getAttribute("data-newest"));
      } else if (selectedSort === "price-low-high") {
        return parseFloat(a.getAttribute("data-price")) - parseFloat(b.getAttribute("data-price"));
      } else if (selectedSort === "price-high-low") {
        return parseFloat(b.getAttribute("data-price")) - parseFloat(a.getAttribute("data-price"));
      }
      return 0;
    });

    // Re-append sorted cards to DOM in order
    sortedCards.forEach((card) => {
      productGrid.appendChild(card);
    });

    // 3. Update count texts
    if (countText) {
      countText.textContent = `${visibleCount} Product${visibleCount === 1 ? "" : "s"} Found`;
    }
    if (countShowing) {
      countShowing.textContent = `Showing ${visibleCount} of 6 Products`;
    }
  }

  // Hook event listeners to filter buttons
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const parentList = btn.closest(".filter-list");
      const filterGroup = parentList.getAttribute("data-filter-group");
      const value = btn.getAttribute("data-value");

      // Reset active state for buttons in the same filter column
      parentList.querySelectorAll(".filter-btn").forEach((b) => {
        b.classList.remove("active");
      });
      btn.classList.add("active");

      // Update state based on filter group
      if (filterGroup === "category") {
        selectedCategory = value;
      } else if (filterGroup === "gender") {
        selectedGender = value;
      } else if (filterGroup === "sort") {
        selectedSort = value;
      }

      updateGallery();
    });
  });
});