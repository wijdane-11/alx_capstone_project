document.addEventListener('DOMContentLoaded', function() {
    // Fetch projects from API
    fetchProjects();

    // Contact form submission
    const contactForm = document.getElementById('contact-form');
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(contactForm);
        const requestData = Object.fromEntries(formData);

        // Send form data to server
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

function fetchProjects() {
    // Fetch projects from API endpoint
    fetch('/projects')
    .then(response => response.json())
    .then(data => {
        const projectsList = document.getElementById('projects-list');
        data.forEach(project => {
            const projectElement = document.createElement('div');
            projectElement.innerHTML = `
                <h3>${project.title}</h3>
                <p>${project.description}</p>
                <a href="${project.demo}" target="_blank">Demo</a>
                <a href="${project.source}" target="_blank">Source Code</a>
            `;
            projectsList.appendChild(projectElement);
        });
    })
    .catch(error => console.error('Error:', error));
}
