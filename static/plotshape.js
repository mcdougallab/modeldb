var neuron_section_data = undefined;
var _shape_plots_mapping = {};
var id_map = {};
var mouse = new THREE.Vector2();

function set_neuron_section_data(new_data) {
    neuron_section_data = new_data;
    for(sp of _shape_plots) {
        sp.update();
    }
}

function ShapePlot(container) {
    this.diam_scale = 1;
    this.tc = new ThreeContainer(container);
    this.container = container;
    this.section_data = undefined;
    this.vmin = -100;
    this.vmax = 100;
    this.container.on( 'click', clickEvent);
    _shape_plots_mapping[this.container.attr('id')] = this;
}

function clickEvent(event) {
    //TODO: try only-one-pixel option again
    var plot = _shape_plots_mapping[$(this).attr('id')];
    mouse.x = event.clientX;
    mouse.y = plot.tc.height - event.clientY;

    // virtual buffer read 
    var pixelBuffer = new Uint8Array(3);
    render = plot.tc.renderer;
    render.render(plot.tc.pickingScene, plot.tc.camera, plot.tc.pickingTexture);
    render.readRenderTargetPixels(plot.tc.pickingTexture, mouse.x, mouse.y, 1, 1, pixelBuffer);

    const id = (pixelBuffer[0] << 16) | (pixelBuffer[1] << 8) | (pixelBuffer[2]);
    o = id_map[id];
    if (o) {
        console.log('intersected!');
        _section_intersected(browser_id, id);
    } 

}

ShapePlot.prototype.update = function() {
    if (this.section_data !== neuron_section_data[0]) {
        this.section_data = neuron_section_data[0];
        this.camera_dist = neuron_section_data[1]*2.5;
        this.tc.camera.position.set(0,0,this.camera_dist);
        this.tc.onContainerResize();
        this.tc.clearLines();
        var my_mode = this.container.attr('data-mode');
        if (my_mode == undefined) {
            my_mode = 1;
        }
        function const_function(val) {
            return function(p) {return val};
        }
        function sp_interpolater(arc3d, ys, diam_scale) {
            var my_arc3d = [];
            var lo = arc3d[0];
            var hi = arc3d[arc3d.length - 1];
            var delta = hi - lo;
            for (var i = 0; i < arc3d.length; i++) {
                my_arc3d.push((arc3d[i] - lo) / delta);
            }
            return function(p) {
                for(var i = 1; i < my_arc3d.length; i++) {
                    var me = my_arc3d[i];
                    if (p < me) {
                        var last = my_arc3d[i - 1];
                        var x = (p - last) / (me - last);
                        return diam_scale * (x * ys[i] + (1 - x) * ys[i - 1]);
                    }
                }
                return ys[my_arc3d.length - 1] * diam_scale;
            }
        }
        var const_diam_f = const_function(4 * this.diam_scale);
        var my_width_rule;
        for(var i = 0; i < this.section_data.length; i++) {
            var my_segment = this.section_data[i];
            var xs = my_segment[0];
            var ys = my_segment[1];
            var zs = my_segment[2];
            var ds = my_segment[3];
            var arcs = my_segment[4];
            var geo = new THREE.Geometry();
            for(var j = 0 ; j < xs.length; j++) {
                geo.vertices.push(new THREE.Vector3(xs[j], ys[j], zs[j]));
            }
            if (my_mode == 0) {
                my_width_rule = sp_interpolater(arcs, ds, 4 * this.diam_scale);
            } else {
                my_width_rule = const_diam_f;
            }
            this.tc.makeLine(geo, my_width_rule);
        }
    }
}

ShapePlot.prototype.force_update = function() {
    this.section_data = undefined;
    this.update();
}


ShapePlot.prototype.set_diam_scale = function(diam) {
    this.diam_scale = diam;
    this.force_update();
}

ShapePlot.prototype.update_colors = function(data) {
    var vmin = this.vmin;
    var vmax = this.vmax;
    var vdelta = vmax - vmin;
    for (var i = 0; i < this.section_data.length; i++) {
        var v = data[i];
        var r, g, b;
        if (v == null) {
            r = 0;
            g = 0;
            b = 0;
        } else {
            v = (data[i] - vmin) / vdelta;
            if (v < 0) {v = 0;}
            if (v > 1) {v = 1;}
            r = v;
            b = 1 - v;
            g = 0;
        }
        var cv = this.tc.lines[i].material.uniforms.color.value;
        cv.r = r;
        cv.g = g;
        cv.b = b;
    }
}