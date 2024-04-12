document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contactForm");
    const responseMessage = document.getElementById("responseMessage");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(form);

        // Submit form data via AJAX
        fetch("submit.php", {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            if (data.trim() === "success") {
                responseMessage.textContent = "Submitted successfully!";
                responseMessage.style.color = "green";
                form.reset(); // Reset form after successful submission
            } else {
                responseMessage.textContent = "An error occurred. Please try again later.";
                responseMessage.style.color = "red";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            responseMessage.textContent = "An error occurred. Please try again later.";
            responseMessage.style.color = "red";
        });
    });
});