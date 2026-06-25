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
  // Helper function to get CSRF token
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  // Toast Notification Helper
  function showToast(message, isError = false) {
    let container = document.getElementById("toast-container");
    if (!container) {
      container = document.createElement("div");
      container.id = "toast-container";
      container.style.position = "fixed";
      container.style.bottom = "24px";
      container.style.right = "24px";
      container.style.zIndex = "1000";
      container.style.display = "flex";
      container.style.flexDirection = "column";
      container.style.gap = "10px";
      document.body.appendChild(container);
    }
    
    const toast = document.createElement("div");
    toast.className = `toast-message ${isError ? "error" : "success"}`;
    toast.style.background = isError ? "rgba(220, 53, 69, 0.95)" : "rgba(27, 28, 28, 0.95)";
    toast.style.color = "#fff";
    toast.style.padding = "14px 24px";
    toast.style.borderRadius = "8px";
    toast.style.boxShadow = "0 8px 30px rgba(0,0,0,0.15)";
    toast.style.fontFamily = "Outfit, sans-serif";
    toast.style.fontWeight = "500";
    toast.style.fontSize = "14px";
    toast.style.minWidth = "280px";
    toast.style.display = "flex";
    toast.style.alignItems = "center";
    toast.style.justifyContent = "space-between";
    toast.style.opacity = "0";
    toast.style.transform = "translateY(20px)";
    toast.style.transition = "all 0.3s cubic-bezier(0.16, 1, 0.3, 1)";
    
    const icon = isError 
      ? '<i class="fa-solid fa-circle-exclamation" style="margin-right:10px;color:#ff4d4d;font-size:16px;"></i>' 
      : '<i class="fa-solid fa-circle-check" style="margin-right:10px;color:#4caf50;font-size:16px;"></i>';
      
    toast.innerHTML = `
      <div style="display:flex;align-items:center;">
        ${icon}
        <span>${message}</span>
      </div>
      <button style="background:none;border:none;color:#fff;cursor:pointer;margin-left:15px;font-size:16px;line-height:1;">&times;</button>
    `;
    
    container.appendChild(toast);
    
    setTimeout(() => {
      toast.style.opacity = "1";
      toast.style.transform = "translateY(0)";
    }, 10);
    
    const removeTimeout = setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transform = "translateY(-20px)";
      setTimeout(() => {
        toast.remove();
      }, 300);
    }, 4000);
    
    toast.querySelector("button").addEventListener("click", () => {
      clearTimeout(removeTimeout);
      toast.style.opacity = "0";
      toast.style.transform = "translateY(-20px)";
      setTimeout(() => {
        toast.remove();
      }, 300);
    });
  }

  // Handle Add to Cart Click
  const btnAddToCart = document.getElementById("btn-add-to-cart");
  if (btnAddToCart) {
    btnAddToCart.addEventListener("click", function () {
      const productId = this.getAttribute("data-product-id");
      const activeColorSpan = document.getElementById("active-color-name");
      const color = activeColorSpan ? activeColorSpan.textContent.trim() : "";
      
      const selectedSizeBtn = document.querySelector(".size-btn.active");
      if (!selectedSizeBtn) {
        showToast("Please select a size before adding to cart.", true);
        return;
      }
      
      const size = selectedSizeBtn.textContent.trim();
      
      this.disabled = true;
      const originalText = this.textContent;
      this.textContent = "Adding...";
      
      fetch("/cart/add/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
          product_id: productId,
          color: color,
          size: size,
          quantity: 1
        })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        if (data.success) {
          showToast("Successfully added to your shopping cart!");
          const cartBadge = document.getElementById("nav-cart-count");
          if (cartBadge) {
            cartBadge.textContent = data.cart_count;
            // Add a little pop animation to the badge
            cartBadge.style.transform = "scale(1.3)";
            setTimeout(() => {
              cartBadge.style.transform = "scale(1)";
            }, 200);
          }
        } else {
          showToast(data.error || "Failed to add item.", true);
        }
      })
      .catch(error => {
        console.error("Error adding to cart:", error);
        showToast("An error occurred. Please try again.", true);
      })
      .finally(() => {
        this.disabled = false;
        this.textContent = originalText;
      });
    });
  }
});
