document.addEventListener('DOMContentLoaded', function () {
    const scene = new THREE.Scene();
    
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 0, 5);
    
    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('three-canvas'), antialias: true });

    // Set initial size of the renderer
    const footerHeight = 100; // Adjust based on your footer height
    renderer.setSize(window.innerWidth, window.innerHeight - footerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);

    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    
    camera.lookAt(cube.position);

    let isAnimating = true; // Flag to control animation
    const card = document.createElement('div');
    card.classList.add('card'); // Add card class for styling
    card.innerText = "You clicked the cube!";
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
                card.classList.remove('show');
            } else {
                card.classList.add('show'); 
            }
        }
    }

    window.addEventListener('resize', onWindowResize);
    window.addEventListener('click', onCubeClick);
    animate();
});