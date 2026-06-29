/* Account Dashboard Interactivity */
document.addEventListener("DOMContentLoaded", function () {
  // ================= TAB NAVIGATION =================
  const tabBtns = document.querySelectorAll(".sidebar-tab-btn");
  const panels = document.querySelectorAll(".content-panel");

  tabBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      const targetId = this.getAttribute("data-target");
      const targetPanel = document.getElementById(targetId);

      if (!targetPanel) return;

      // Update active nav button
      tabBtns.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");

      // Switch active content panel with subtle transitions
      panels.forEach((p) => {
        p.classList.remove("active");
      });
      targetPanel.classList.add("active");
    });
  });

  // ================= EDIT PROFILE MODE =================
  const editToggleBtn = document.getElementById("edit-profile-toggle");
  const editCancelBtn = document.getElementById("edit-profile-cancel");
  const profileForm = document.getElementById("profile-details-form");
  const formActions = document.getElementById("form-edit-actions");

  if (profileForm && editToggleBtn && editCancelBtn) {
    const editableInputs = profileForm.querySelectorAll(
      "input:not([type='hidden'])",
    );

    // Store original values to restore on cancel
    let originalValues = {};

    editToggleBtn.addEventListener("click", function () {
      // Enter Edit Mode
      editToggleBtn.style.display = "none";
      formActions.style.display = "flex";

      editableInputs.forEach((input) => {
        // Store current value
        originalValues[input.id] = input.value;

        // Remove readonly except for email address (usually locked in storefronts)
        if (input.id !== "profile-email") {
          input.removeAttribute("readonly");
        }
      });
    });

    editCancelBtn.addEventListener("click", function () {
      // Exit Edit Mode and Restore Values
      editToggleBtn.style.display = "block";
      formActions.style.display = "none";

      editableInputs.forEach((input) => {
        input.setAttribute("readonly", true);
        if (originalValues[input.id] !== undefined) {
          input.value = originalValues[input.id];
        }
      });
    });

    profileForm.addEventListener("submit", function (e) {
      e.preventDefault();

      // Simulate saving changes
      editableInputs.forEach((input) => {
        input.setAttribute("readonly", true);
      });

      editToggleBtn.style.display = "block";
      formActions.style.display = "none";

      // Display success alert
      const successToast = document.createElement("div");
      successToast.style.position = "fixed";
      successToast.style.bottom = "20px";
      successToast.style.right = "20px";
      successToast.style.backgroundColor = "#10B981";
      successToast.style.color = "#FFFFFF";
      successToast.style.padding = "14px 24px";
      successToast.style.borderRadius = "4px";
      successToast.style.fontFamily = "'Outfit', sans-serif";
      successToast.style.fontSize = "13px";
      successToast.style.fontWeight = "700";
      successToast.style.letterSpacing = "0.5px";
      successToast.style.boxShadow = "0 4px 12px rgba(0,0,0,0.15)";
      successToast.style.zIndex = "1000";
      successToast.style.textTransform = "uppercase";
      successToast.textContent = "Profile updated successfully";

      document.body.appendChild(successToast);

      setTimeout(() => {
        successToast.style.opacity = "0";
        successToast.style.transition = "opacity 0.5s ease";
        setTimeout(() => successToast.remove(), 500);
      }, 3000);
    });
  }

  // ================= WISHLIST DELETION =================
  const wishlistGrid = document.getElementById("wishlist-items-grid");
  const statsWishlistBadge = document.getElementById("stats-wishlist-count");

  if (wishlistGrid) {
    wishlistGrid.addEventListener("click", function (e) {
      const removeBtn = e.target.closest(".btn-remove-wishlist");
      if (!removeBtn) return;

      const card = removeBtn.closest(".wishlist-card");
      if (!card) return;

      // Apply fade out animation
      card.style.opacity = "0";
      card.style.transform = "scale(0.95)";
      card.style.transition = "all 0.3s cubic-bezier(0.16, 1, 0.3, 1)";

      setTimeout(() => {
        card.remove();

        // Update wishlist count in header stats
        const remainingCards = wishlistGrid.querySelectorAll(".wishlist-card");
        if (statsWishlistBadge) {
          statsWishlistBadge.textContent = remainingCards.length;
        }

        // Show empty state if all cards are removed
        if (remainingCards.length === 0) {
          const emptyState = document.createElement("div");
          emptyState.className = "empty-state";
          emptyState.id = "wishlist-empty-state";
          emptyState.innerHTML = `
            <i class="fa-regular fa-heart"></i>
            <p>Your wishlist is currently empty.</p>
            <a href="/product/" class="btn-primary">Browse Collection</a>
          `;
          wishlistGrid.replaceWith(emptyState);
        }
      }, 300);
    });
  }

  // ================= LOGOUT =================
  const logoutBtn = document.getElementById("btn-logout");
  const logoutForm = document.getElementById("logout-form");
  if (logoutBtn && logoutForm) {
    logoutBtn.addEventListener("click", function (e) {
      e.preventDefault();
      logoutForm.submit();
    });
  }
});
