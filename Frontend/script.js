async function createAndRedirect() {
    try {
        const response = await fetch('http://127.0.0.1:8000/upload-image/', { 
            method: 'POST',
            credentials: 'include'  
        });

        if (response.ok) {
            const data = await response.json();
            window.location.href = `displayTelescope.html?image_path=${encodeURIComponent(data.image_path)}`;
        } else {
            console.error('Error creating image:', response.statusText);
            alert('Failed to create the image.');
        }
    } catch (error) {
        console.error('Error creating image:', error);
        alert('An error occurred while creating the image.');
    }
}

function toggleDropdown() {
    const dropdown = document.getElementById('dropdownMenu');
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
}