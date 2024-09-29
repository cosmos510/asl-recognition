import './index2.css';

document.addEventListener("DOMContentLoaded", function() {
    fetch('/header.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('header-container').innerHTML = data;
            updateNavbar();
        })
        .catch(error => console.error('Error loading header:', error));
    fetch('/footer.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('footer-container').innerHTML = data;
        })
        .catch(error => console.error('Error loading footer:', error));
});

async function updateNavbar() {
    try {
        const response = await fetch('/api/user-status/', {
            credentials: 'include',
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        const authLinks = document.getElementById('auth-links');
        if (!authLinks) {
            console.error('Element with ID "auth-links" not found');
            return;
        }
        if (data.logged_in) {
            authLinks.innerHTML = `
                <a href="/logout" class="nav-link">Logout</a>
            `;
        } else {
            authLinks.innerHTML = `
                <a href="/login" class="nav-link">Login</a>
                <a href="/register" class="nav-link">Register</a>
            `;
        }
    } catch (error) {
        console.error('Error fetching user status:', error);
    }
}