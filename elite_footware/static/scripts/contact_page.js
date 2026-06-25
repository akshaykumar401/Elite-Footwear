document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contact-form");
  const successModal = document.getElementById("success-modal");
  const closeModalBtn = document.getElementById("close-modal");

  if (form) {
    form.addEventListener("submit", (e) => {
      const nameInput = document.getElementById("id_full_name");
      const emailInput = document.getElementById("id_email");
      const subjectInput = document.getElementById("id_subject");
      const messageInput = document.getElementById("id_message");

      let isValid = true;

      // Simple visual validation function
      const validateField = (input, condition) => {
        if (!input) return true;
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
      if (nameInput && !validateField(nameInput, nameInput.value.trim() !== "")) isValid = false;
      
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (emailInput && !validateField(emailInput, emailRegex.test(emailInput.value.trim()))) isValid = false;

      if (subjectInput && !validateField(subjectInput, subjectInput.value.trim() !== "")) isValid = false;
      if (messageInput && !validateField(messageInput, messageInput.value.trim() !== "")) isValid = false;

      // If NOT valid, prevent submission
      if (!isValid) {
        e.preventDefault();
      }
    });
  }

  if (closeModalBtn && successModal) {
    closeModalBtn.addEventListener("click", () => {
      successModal.classList.remove("is-visible");
      if (form) {
        form.reset();
        
        // Reset any error border colors
        form.querySelectorAll("input, textarea").forEach((field) => {
          field.style.borderColor = "";
        });
      }
    });
  }
});
