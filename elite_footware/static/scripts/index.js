document.addEventListener("DOMContentLoaded", () => {
  const filterButtons = document.querySelectorAll(".filter-btn");
  const productCards = document.querySelectorAll(".product-card");
  const countText = document.getElementById("product-count-text");

  function updateGallery(selectedCategory) {
    let visibleCount = 0;

    productCards.forEach((card) => {
      const category = card.getAttribute("category");
      const isVisible = selectedCategory === "All" || category === selectedCategory;

      if (isVisible) {
        visibleCount++;
        card.classList.remove("hidden");
      } else {
        card.classList.add("hidden");
      }
    });

    if (countText) {
      countText.textContent = `${visibleCount} Product${visibleCount === 1 ? "" : "s"} Found`;
    }
  }

  // Hook event listeners to filter buttons
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      // Reset active state for all filter buttons
      filterButtons.forEach((b) => {
        b.classList.remove("active");
      });
      btn.classList.add("active");

      const value = btn.getAttribute("data-value");
      updateGallery(value);
    });
  });

  // Initial call to set the count correctly
  updateGallery("All");
});
