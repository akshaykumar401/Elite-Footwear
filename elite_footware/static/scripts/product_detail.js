document.addEventListener("DOMContentLoaded", function () {
  const thumbnailsContainer = document.getElementById("gallery-thumbnails");
  const mainImg = document.getElementById("main-product-img");

  // Set up click listeners for the thumbnails
  function setupThumbnailListeners() {
    const thumbs = thumbnailsContainer.querySelectorAll(".thumbnail-box");
    thumbs.forEach((thumb) => {
      thumb.addEventListener("click", function () {
        // Remove active state
        thumbs.forEach((t) => t.classList.remove("active"));
        // Set active state on current
        this.classList.add("active");

        // Switch main image with subtle fade transition
        mainImg.style.opacity = "0";
        setTimeout(() => {
          mainImg.src = this.getAttribute("data-img-url");
          mainImg.style.opacity = "1";
        }, 150);
      });
    });
  }

  setupThumbnailListeners();

  // Set up click listeners for the color swatch buttons
  const swatches = document.querySelectorAll(".swatch-btn");
  const activeColorSpan = document.getElementById("active-color-name");

  swatches.forEach((swatch) => {
    swatch.addEventListener("click", function () {
      if (this.classList.contains("active")) return;

      swatches.forEach((s) => s.classList.remove("active"));
      this.classList.add("active");

      // Update color name text indicator
      if (activeColorSpan) {
        activeColorSpan.textContent = this.getAttribute("data-color-name");
      }

      // Load swatch specific main image with a smooth crossfade effect
      const newMainImgSrc = this.getAttribute("data-main-img");
      mainImg.style.opacity = "0";
      setTimeout(() => {
        mainImg.src = newMainImgSrc;
        mainImg.style.opacity = "1";
      }, 150);

      // Re-populate thumbnail boxes based on selected swatch data
      const thumbsData = JSON.parse(this.getAttribute("data-thumbs"));
      thumbnailsContainer.innerHTML = "";
      thumbsData.forEach((thumbUrl, index) => {
        const thumbBox = document.createElement("div");
        thumbBox.className = `thumbnail-box ${index === 0 ? "active" : ""}`;
        thumbBox.setAttribute("data-img-url", thumbUrl);
        thumbBox.innerHTML = `<img src="${thumbUrl}" alt="Thumbnail angle view" />`;
        thumbnailsContainer.appendChild(thumbBox);
      });

      // Re-attach listeners to the fresh thumbnail boxes
      setupThumbnailListeners();
    });
  });

  // Set up size selection logic
  const sizeBtns = document.querySelectorAll(".size-btn");
  sizeBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      sizeBtns.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");
    });
  });

  // Set up specifications accordion expand/collapse logic
  const accordionToggle = document.getElementById("specs-accordion-toggle");
  const accordionContent = document.getElementById("specs-accordion-content");

  accordionToggle.addEventListener("click", function () {
    const isActive = this.classList.toggle("active");
    if (isActive) {
      accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
    } else {
      accordionContent.style.maxHeight = "0";
    }
  });
});
