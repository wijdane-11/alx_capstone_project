document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact-form');
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(contactForm);
        const requestData = Object.fromEntries(formData);

        fetch('/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            contactForm.reset();
        })
        .catch(error => console.error('Error:', error));
    });
});
