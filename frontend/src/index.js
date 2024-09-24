// index.js
import './index.css';

document.addEventListener("DOMContentLoaded", function() {
    // Load header
    fetch('/header.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('header-container').innerHTML = data;
            updateNavbar(); // Call updateNavbar after header is loaded
        })
        .catch(error => console.error('Error loading header:', error));

    // Load footer
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
    console.log('updateNavbar called'); // Debug log
    try {
        const response = await fetch('/api/user-status/', {
            credentials: 'include', // Include cookies for session management
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('User status data:', data); // Debug log

        const authLinks = document.getElementById('auth-links');

        // Ensure authLinks is not null
        if (!authLinks) {
            console.error('Element with ID "auth-links" not found');
            return; // Exit the function early
        }

        // Update navbar based on user status
        if (data.logged_in) {
            authLinks.innerHTML = `
                <a href="/profile" class="nav-link">${data.username}</a> <!-- Add existing class here -->
                <a href="/logout" class="nav-link">Logout</a> <!-- Add existing class here -->
            `;
        } else {
            authLinks.innerHTML = `
                <a href="/login" class="nav-link">Login</a> <!-- Add existing class here -->
                <a href="/register" class="nav-link">Register</a> <!-- Add existing class here -->
            `;
        }
    } catch (error) {
        console.error('Error fetching user status:', error);
    }
}