document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contact-form");
  const successModal = document.getElementById("success-modal");
  const closeModalBtn = document.getElementById("close-modal");

  if (form && successModal) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();

      const nameInput = document.getElementById("form-name");
      const emailInput = document.getElementById("form-email");
      const subjectInput = document.getElementById("form-subject");
      const messageInput = document.getElementById("form-message");

      let isValid = true;

      // Simple visual validation function
      const validateField = (input, condition) => {
        if (condition) {
          input.style.borderColor = "";
          return true;
        } else {
          input.style.borderColor = "#ff3333";
          // Add temporary shake animation or outline
          input.animate(
            [
              { transform: "translateX(0)" },
              { transform: "translateX(-4px)" },
              { transform: "translateX(4px)" },
              { transform: "translateX(0)" }
            ],
            { duration: 200, iterations: 1 }
          );
          return false;
        }
      };

      // Validate inputs
      if (!validateField(nameInput, nameInput.value.trim() !== "")) isValid = false;
      
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!validateField(emailInput, emailRegex.test(emailInput.value.trim()))) isValid = false;

      if (!validateField(subjectInput, subjectInput.value.trim() !== "")) isValid = false;
      if (!validateField(messageInput, messageInput.value.trim() !== "")) isValid = false;

      // If valid, show custom success state
      if (isValid) {
        successModal.classList.add("is-visible");
      }
    });
  }

  if (closeModalBtn && successModal && form) {
    closeModalBtn.addEventListener("click", () => {
      successModal.classList.remove("is-visible");
      form.reset();
      
      // Reset any error border colors
      form.querySelectorAll("input, textarea").forEach((field) => {
        field.style.borderColor = "";
      });
    });
  }
});
