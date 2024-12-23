        
        const params = new URLSearchParams(window.location.search);
        const imagePath = params.get('image_path');

        if (imagePath) {
            const imageElement = document.getElementById('display-image');
            imageElement.src = imagePath;
            
            
            imageElement.onerror = function() {
                document.getElementById('image-container').innerHTML = 
                    "<p>Error loading image. Please try again.</p>";
            };
        } else {
            document.getElementById('image-container').innerHTML = 
                "<p>Image path not provided!</p>";
        }