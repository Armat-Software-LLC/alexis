// This is a sample JavaScript file served by Flask

console.log('JavaScript file loaded successfully!');

// Function to demonstrate interactivity
document.addEventListener('DOMContentLoaded', function() {
    const image = document.getElementById('displayed-image');
    if (image) {
        image.addEventListener('click', function() {
            alert('Image clicked! JavaScript is working.');
        });
        
        console.log('Image found and click handler attached');
    }
});

// Sample function that can be called from HTML
function showMessage() {
    alert('Hello from Flask-served JavaScript!');
}

console.log('JavaScript initialized');

