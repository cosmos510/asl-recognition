document.addEventListener('DOMContentLoaded', function () {
    const scene = new THREE.Scene();

    // Create the camera with an initial aspect ratio based on the window size
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 0, 5); // Set the camera 5 units away from the cube (along the z-axis)

    // Set up the renderer
    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('three-canvas'), antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);

    // Create a cube and add it to the scene
    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    // Make sure the camera is looking at the cube's position
    camera.lookAt(cube.position);

    function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    }

    // Resize handler to adjust the camera and renderer when the window is resized
    function onWindowResize() {
        const width = window.innerWidth;
        const height = window.innerHeight;

        console.log('Window resized:', width, height);

        // Update the renderer size
        renderer.setSize(width, height);

        // Update the camera's aspect ratio
        camera.aspect = width / height;

        // Update the camera's projection matrix (this is crucial to keeping the view updated)
        camera.updateProjectionMatrix();
    }

    // Add event listener for window resize
    window.addEventListener('resize', onWindowResize);

    // Start the animation loop
    animate();
});