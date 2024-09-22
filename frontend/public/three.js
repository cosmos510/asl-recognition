document.addEventListener('DOMContentLoaded', function () {
    const scene = new THREE.Scene();
    
    // Set a solid color background
    scene.background = new THREE.Color(0x87CEEB); // Light blue color

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 0, 5);
    
    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('three-canvas'), antialias: true });
    
    // Set initial size of the renderer
    const footerHeight = 100; // Adjust based on your footer height
    renderer.setSize(window.innerWidth, window.innerHeight - footerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);

    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 }); // Use MeshStandardMaterial for lighting
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    
    // Add ambient light
    const ambientLight = new THREE.AmbientLight(0x404040, 1); // Soft white light
    scene.add(ambientLight);

    // Add directional light
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // White light
    directionalLight.position.set(5, 5, 5); // Position the light
    scene.add(directionalLight);
    
    camera.lookAt(cube.position);

    let isAnimating = true; // Flag to control animation
    const card = document.createElement('div');
    card.classList.add('card'); // Add card class for styling
    card.innerText = "You clicked the cube!";
    card.style.display = 'none'; // Initially hide the card
    document.body.appendChild(card);

    function animate() {
        requestAnimationFrame(animate);
        if (isAnimating) {
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
        }
        renderer.render(scene, camera);
    }

    function onWindowResize() {
        const width = window.innerWidth;
        const height = window.innerHeight;
        renderer.setSize(width, height - footerHeight);
        camera.aspect = width / (height - footerHeight);
        camera.updateProjectionMatrix();
    }

    function onCubeClick(event) {
        const mouse = new THREE.Vector2(
            (event.clientX / window.innerWidth) * 2 - 1,
            - (event.clientY / window.innerHeight) * 2 + 1
        );

        const raycaster = new THREE.Raycaster();
        raycaster.setFromCamera(mouse, camera);

        const intersects = raycaster.intersectObjects([cube]);

        if (intersects.length > 0) {
            isAnimating = !isAnimating;
            if (isAnimating) {
                card.style.display = 'none'; // Hide card
            } else {
                card.style.display = 'block'; // Show card
            }
        }
    }

    window.addEventListener('resize', onWindowResize);
    window.addEventListener('click', onCubeClick);
    animate();
});