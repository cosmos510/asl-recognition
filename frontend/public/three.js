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
    
    function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    }

    function onWindowResize() {
        const width = window.innerWidth;
        const height = window.innerHeight;
        renderer.setSize(width, height - footerHeight);
        camera.aspect = width / (height - footerHeight);
        camera.updateProjectionMatrix();
    }

    window.addEventListener('resize', onWindowResize);
    animate();
});