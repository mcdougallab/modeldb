function ThreeContainer(container) {
    // NOTE: this assumes only one entry in container
    this.container = container[0];
    this.width = this.container.clientWidth;
    this.height = this.container.clientHeight;
    this.scene = new THREE.Scene();
    this.pickingScene = new THREE.Scene();
    this.pickingScene.background = new THREE.Color(0);
    this.pickingTexture = new THREE.WebGLRenderTarget(this.width, this.height, {format: THREE.RGBFormat});

    this.camera = new THREE.PerspectiveCamera(60, this.width / this.height, .01, 10000); //OrthographicCamera(this.width / -2, this.width / 2, this.height / -2, this.height / 2, 1, 1000) // 
    this.camera.position.set(0, 0, 500);

    this.renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
    this.renderer.setSize(this.width, this.height);
    this.renderer.setPixelRatio(window.devicePixelRatio);
    this.container.appendChild(this.renderer.domElement);

    this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);

    this.lines = [];
    container.resize(this.onContainerResize);
    console.log('ThreeContainer', this);
    this.init();
    return this;
}


ThreeContainer.prototype.onContainerResize = function() {
    var w = this.container.clientWidth;
    var h = this.container.clientHeight;
    console.log(w,h);

    this.camera.aspect = w / h;
    this.camera.updateProjectionMatrix();

    this.renderer.setSize(w, h);
    this.pickingTexture.setSize(w, h);
    this.width = w;
    this.height = h;
    console.log('onContainerResize', w, h);
}


ThreeContainer.prototype.makeLine = function (geo, width_rule) {
    var g = new MeshLine();
    g.setGeometry(geo, width_rule);

    var material = new MeshLineMaterial({
        color: new THREE.Color(0x000000),
        lineWidth: 0.25,
        side: THREE.DoubleSide
    });
    var mesh = new THREE.Mesh(g.geometry, material);
    this.scene.add(mesh);
    // virtual buffer id as color
    const id = this.lines.length + 1;
    id_map[id] = mesh;

    var pick_material = new MeshLineMaterial({
        color: new THREE.Color(id),
        lineWidth: 0.25,
        side: THREE.DoubleSide
    })
    var pick_mesh = new THREE.Mesh(g.geometry, pick_material);

    this.pickingScene.add(pick_mesh);
    this.lines.push(mesh);
}

ThreeContainer.prototype.init = function() {
    this.onContainerResize();
    this.render();
}

ThreeContainer.prototype.render = function() {
    this.renderer.render(this.scene, this.camera);
    requestAnimationFrame(this.render.bind(this));
}

ThreeContainer.prototype.clearLines = function() {
    console.log('clearLines');
    this.scene.remove.apply(this.scene, this.scene.children);
    this.pickingScene.remove.apply(this.pickingScene, this.pickingScene.children);
    this.lines = [];
}


function neuron_javascript_embedder(js) {
    try {
        eval(js);
    } catch (err) {
        console.log(err.message);
    }
}
