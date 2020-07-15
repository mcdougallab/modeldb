// from https://github.com/spite/THREE.MeshLine/blob/master/LICENSE
/*
MIT License

Copyright (c) 2016 Jaume Sanchez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

// from THREE.MeshLine/demo/js/OrbitControls.js 
/**
 * @author qiao / https://github.com/qiao
 * @author mrdoob / http://mrdoob.com
 * @author alteredq / http://alteredqualia.com/
 * @author WestLangley / http://github.com/WestLangley
 * @author erich666 / http://erichaines.com
 */
/*global THREE, console */

( function () {

	function OrbitConstraint ( object ) {

		this.object = object;

		// "target" sets the location of focus, where the object orbits around
		// and where it pans with respect to.
		this.target = new THREE.Vector3();

		// Limits to how far you can dolly in and out ( PerspectiveCamera only )
		this.minDistance = 0;
		this.maxDistance = Infinity;

		// Limits to how far you can zoom in and out ( OrthographicCamera only )
		this.minZoom = 0;
		this.maxZoom = Infinity;

		// How far you can orbit vertically, upper and lower limits.
		// Range is 0 to Math.PI radians.
		this.minPolarAngle = 0; // radians
		this.maxPolarAngle = Math.PI; // radians

		// How far you can orbit horizontally, upper and lower limits.
		// If set, must be a sub-interval of the interval [ - Math.PI, Math.PI ].
		this.minAzimuthAngle = - Infinity; // radians
		this.maxAzimuthAngle = Infinity; // radians

		// Set to true to enable damping (inertia)
		// If damping is enabled, you must call controls.update() in your animation loop
		this.enableDamping = false;
		this.dampingFactor = 0.25;

		////////////
		// internals

		var scope = this;

		var EPS = 0.000001;

		// Current position in spherical coordinate system.
		var theta;
		var phi;

		// Pending changes
		var phiDelta = 0;
		var thetaDelta = 0;
		var scale = 1;
		var panOffset = new THREE.Vector3();
		var zoomChanged = false;

		// API

		this.getPolarAngle = function () {

			return phi;

		};

		this.getAzimuthalAngle = function () {

			return theta;

		};

		this.rotateLeft = function ( angle ) {

			thetaDelta -= angle;

		};

		this.rotateUp = function ( angle ) {

			phiDelta -= angle;

		};

		// pass in distance in world space to move left
		this.panLeft = function() {

			var v = new THREE.Vector3();

			return function panLeft ( distance ) {

				var te = this.object.matrix.elements;

				// get X column of matrix
				v.set( te[ 0 ], te[ 1 ], te[ 2 ] );
				v.multiplyScalar( - distance );

				panOffset.add( v );

			};

		}();

		// pass in distance in world space to move up
		this.panUp = function() {

			var v = new THREE.Vector3();

			return function panUp ( distance ) {

				var te = this.object.matrix.elements;

				// get Y column of matrix
				v.set( te[ 4 ], te[ 5 ], te[ 6 ] );
				v.multiplyScalar( distance );

				panOffset.add( v );

			};

		}();

		// pass in x,y of change desired in pixel space,
		// right and down are positive
		this.pan = function ( deltaX, deltaY, screenWidth, screenHeight ) {

			if ( scope.object instanceof THREE.PerspectiveCamera ) {

				// perspective
				var position = scope.object.position;
				var offset = position.clone().sub( scope.target );
				var targetDistance = offset.length();

				// half of the fov is center to top of screen
				targetDistance *= Math.tan( ( scope.object.fov / 2 ) * Math.PI / 180.0 );

				// we actually don't use screenWidth, since perspective camera is fixed to screen height
				scope.panLeft( 2 * deltaX * targetDistance / screenHeight );
				scope.panUp( 2 * deltaY * targetDistance / screenHeight );

			} else if ( scope.object instanceof THREE.OrthographicCamera ) {

				// orthographic
				scope.panLeft( deltaX * ( scope.object.right - scope.object.left ) / screenWidth );
				scope.panUp( deltaY * ( scope.object.top - scope.object.bottom ) / screenHeight );

			} else {

				// camera neither orthographic or perspective
				console.warn( 'WARNING: OrbitControls.js encountered an unknown camera type - pan disabled.' );

			}

		};

		this.dollyIn = function ( dollyScale ) {

			if ( scope.object instanceof THREE.PerspectiveCamera ) {

				scale /= dollyScale;

			} else if ( scope.object instanceof THREE.OrthographicCamera ) {

				scope.object.zoom = Math.max( this.minZoom, Math.min( this.maxZoom, this.object.zoom * dollyScale ) );
				scope.object.updateProjectionMatrix();
				zoomChanged = true;

			} else {

				console.warn( 'WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled.' );

			}

		};

		this.dollyOut = function ( dollyScale ) {

			if ( scope.object instanceof THREE.PerspectiveCamera ) {

				scale *= dollyScale;

			} else if ( scope.object instanceof THREE.OrthographicCamera ) {

				scope.object.zoom = Math.max( this.minZoom, Math.min( this.maxZoom, this.object.zoom / dollyScale ) );
				scope.object.updateProjectionMatrix();
				zoomChanged = true;

			} else {

				console.warn( 'WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled.' );

			}

		};

		this.update = function() {

			var offset = new THREE.Vector3();

			// so camera.up is the orbit axis
			var quat = new THREE.Quaternion().setFromUnitVectors( object.up, new THREE.Vector3( 0, 1, 0 ) );
			var quatInverse = quat.clone().inverse();

			var lastPosition = new THREE.Vector3();
			var lastQuaternion = new THREE.Quaternion();

			return function () {

				var position = this.object.position;

				offset.copy( position ).sub( this.target );

				// rotate offset to "y-axis-is-up" space
				offset.applyQuaternion( quat );

				// angle from z-axis around y-axis

				theta = Math.atan2( offset.x, offset.z );

				// angle from y-axis

				phi = Math.atan2( Math.sqrt( offset.x * offset.x + offset.z * offset.z ), offset.y );

				theta += thetaDelta;
				phi += phiDelta;

				// restrict theta to be between desired limits
				theta = Math.max( this.minAzimuthAngle, Math.min( this.maxAzimuthAngle, theta ) );

				// restrict phi to be between desired limits
				phi = Math.max( this.minPolarAngle, Math.min( this.maxPolarAngle, phi ) );

				// restrict phi to be betwee EPS and PI-EPS
				phi = Math.max( EPS, Math.min( Math.PI - EPS, phi ) );

				var radius = offset.length() * scale;

				// restrict radius to be between desired limits
				radius = Math.max( this.minDistance, Math.min( this.maxDistance, radius ) );

				// move target to panned location
				this.target.add( panOffset );

				offset.x = radius * Math.sin( phi ) * Math.sin( theta );
				offset.y = radius * Math.cos( phi );
				offset.z = radius * Math.sin( phi ) * Math.cos( theta );

				// rotate offset back to "camera-up-vector-is-up" space
				offset.applyQuaternion( quatInverse );

				position.copy( this.target ).add( offset );

				this.object.lookAt( this.target );

				if ( this.enableDamping === true ) {

					thetaDelta *= ( 1 - this.dampingFactor );
					phiDelta *= ( 1 - this.dampingFactor );

				} else {

					thetaDelta = 0;
					phiDelta = 0;

				}

				scale = 1;
				panOffset.set( 0, 0, 0 );

				// update condition is:
				// min(camera displacement, camera rotation in radians)^2 > EPS
				// using small-angle approximation cos(x/2) = 1 - x^2 / 8

				if ( zoomChanged ||
					 lastPosition.distanceToSquared( this.object.position ) > EPS ||
				    8 * ( 1 - lastQuaternion.dot( this.object.quaternion ) ) > EPS ) {

					lastPosition.copy( this.object.position );
					lastQuaternion.copy( this.object.quaternion );
					zoomChanged = false;

					return true;

				}

				return false;

			};

		}();

	};


	// This set of controls performs orbiting, dollying (zooming), and panning. It maintains
	// the "up" direction as +Y, unlike the TrackballControls. Touch on tablet and phones is
	// supported.
	//
	//    Orbit - left mouse / touch: one finger move
	//    Zoom - middle mouse, or mousewheel / touch: two finger spread or squish
	//    Pan - right mouse, or arrow keys / touch: three finter swipe

	THREE.OrbitControls = function ( object, domElement ) {

		var constraint = new OrbitConstraint( object );

		this.domElement = ( domElement !== undefined ) ? domElement : document;

		// API

		Object.defineProperty( this, 'constraint', {

			get: function() {

				return constraint;

			}

		} );

		this.getPolarAngle = function () {

			return constraint.getPolarAngle();

		};

		this.getAzimuthalAngle = function () {

			return constraint.getAzimuthalAngle();

		};

		// Set to false to disable this control
		this.enabled = true;

		// center is old, deprecated; use "target" instead
		this.center = this.target;

		// This option actually enables dollying in and out; left as "zoom" for
		// backwards compatibility.
		// Set to false to disable zooming
		this.enableZoom = true;
		this.zoomSpeed = 1.0;

		// Set to false to disable rotating
		this.enableRotate = true;
		this.rotateSpeed = 1.0;

		// Set to false to disable panning
		this.enablePan = true;
		this.keyPanSpeed = 7.0;	// pixels moved per arrow key push

		// Set to true to automatically rotate around the target
		// If auto-rotate is enabled, you must call controls.update() in your animation loop
		this.autoRotate = false;
		this.autoRotateSpeed = 2.0; // 30 seconds per round when fps is 60

		// Set to false to disable use of the keys
		this.enableKeys = true;

		// The four arrow keys
		this.keys = { LEFT: 37, UP: 38, RIGHT: 39, BOTTOM: 40 };

		// Mouse buttons
		this.mouseButtons = { ORBIT: THREE.MOUSE.LEFT, ZOOM: THREE.MOUSE.MIDDLE, PAN: THREE.MOUSE.RIGHT };

		////////////
		// internals

		var scope = this;

		var rotateStart = new THREE.Vector2();
		var rotateEnd = new THREE.Vector2();
		var rotateDelta = new THREE.Vector2();

		var panStart = new THREE.Vector2();
		var panEnd = new THREE.Vector2();
		var panDelta = new THREE.Vector2();

		var dollyStart = new THREE.Vector2();
		var dollyEnd = new THREE.Vector2();
		var dollyDelta = new THREE.Vector2();

		var STATE = { NONE : - 1, ROTATE : 0, DOLLY : 1, PAN : 2, TOUCH_ROTATE : 3, TOUCH_DOLLY : 4, TOUCH_PAN : 5 };

		var state = STATE.NONE;

		// for reset

		this.target0 = this.target.clone();
		this.position0 = this.object.position.clone();
		this.zoom0 = this.object.zoom;

		// events

		var changeEvent = { type: 'change' };
		var startEvent = { type: 'start' };
		var endEvent = { type: 'end' };

		// pass in x,y of change desired in pixel space,
		// right and down are positive
		function pan( deltaX, deltaY ) {

			var element = scope.domElement === document ? scope.domElement.body : scope.domElement;

			constraint.pan( deltaX, deltaY, element.clientWidth, element.clientHeight );

		}

		this.update = function () {

			if ( this.autoRotate && state === STATE.NONE ) {

				constraint.rotateLeft( getAutoRotationAngle() );

			}

			if ( constraint.update() === true ) {

				this.dispatchEvent( changeEvent );

			}

		};

		this.reset = function () {

			state = STATE.NONE;

			this.target.copy( this.target0 );
			this.object.position.copy( this.position0 );
			this.object.zoom = this.zoom0;

			this.object.updateProjectionMatrix();
			this.dispatchEvent( changeEvent );

			this.update();

		};

		function getAutoRotationAngle() {

			return 2 * Math.PI / 60 / 60 * scope.autoRotateSpeed;

		}

		function getZoomScale() {

			return Math.pow( 0.95, scope.zoomSpeed );

		}

		function onMouseDown( event ) {

			if ( scope.enabled === false ) return;

			event.preventDefault();

			if ( event.button === scope.mouseButtons.ORBIT ) {

				if ( scope.enableRotate === false ) return;

				state = STATE.ROTATE;

				rotateStart.set( event.clientX, event.clientY );

			} else if ( event.button === scope.mouseButtons.ZOOM ) {

				if ( scope.enableZoom === false ) return;

				state = STATE.DOLLY;

				dollyStart.set( event.clientX, event.clientY );

			} else if ( event.button === scope.mouseButtons.PAN ) {

				if ( scope.enablePan === false ) return;

				state = STATE.PAN;

				panStart.set( event.clientX, event.clientY );

			}

			if ( state !== STATE.NONE ) {

				document.addEventListener( 'mousemove', onMouseMove, false );
				document.addEventListener( 'mouseup', onMouseUp, false );
				scope.dispatchEvent( startEvent );

			}

		}

		function onMouseMove( event ) {

			if ( scope.enabled === false ) return;

			event.preventDefault();

			var element = scope.domElement === document ? scope.domElement.body : scope.domElement;

			if ( state === STATE.ROTATE ) {

				if ( scope.enableRotate === false ) return;

				rotateEnd.set( event.clientX, event.clientY );
				rotateDelta.subVectors( rotateEnd, rotateStart );

				// rotating across whole screen goes 360 degrees around
				constraint.rotateLeft( 2 * Math.PI * rotateDelta.x / element.clientWidth * scope.rotateSpeed );

				// rotating up and down along whole screen attempts to go 360, but limited to 180
				constraint.rotateUp( 2 * Math.PI * rotateDelta.y / element.clientHeight * scope.rotateSpeed );

				rotateStart.copy( rotateEnd );

			} else if ( state === STATE.DOLLY ) {

				if ( scope.enableZoom === false ) return;

				dollyEnd.set( event.clientX, event.clientY );
				dollyDelta.subVectors( dollyEnd, dollyStart );

				if ( dollyDelta.y > 0 ) {

					constraint.dollyIn( getZoomScale() );

				} else if ( dollyDelta.y < 0 ) {

					constraint.dollyOut( getZoomScale() );

				}

				dollyStart.copy( dollyEnd );

			} else if ( state === STATE.PAN ) {

				if ( scope.enablePan === false ) return;

				panEnd.set( event.clientX, event.clientY );
				panDelta.subVectors( panEnd, panStart );

				pan( panDelta.x, panDelta.y );

				panStart.copy( panEnd );

			}

			if ( state !== STATE.NONE ) scope.update();

		}

		function onMouseUp( /* event */ ) {

			if ( scope.enabled === false ) return;

			document.removeEventListener( 'mousemove', onMouseMove, false );
			document.removeEventListener( 'mouseup', onMouseUp, false );
			scope.dispatchEvent( endEvent );
			state = STATE.NONE;

		}

		function onMouseWheel( event ) {

			if ( scope.enabled === false || scope.enableZoom === false || state !== STATE.NONE ) return;

			event.preventDefault();
			event.stopPropagation();

			var delta = 0;

			if ( event.wheelDelta !== undefined ) {

				// WebKit / Opera / Explorer 9

				delta = event.wheelDelta;

			} else if ( event.detail !== undefined ) {

				// Firefox

				delta = - event.detail;

			}

			if ( delta > 0 ) {

				constraint.dollyOut( getZoomScale() );

			} else if ( delta < 0 ) {

				constraint.dollyIn( getZoomScale() );

			}

			scope.update();
			scope.dispatchEvent( startEvent );
			scope.dispatchEvent( endEvent );

		}

		function onKeyDown( event ) {

			if ( scope.enabled === false || scope.enableKeys === false || scope.enablePan === false ) return;

			switch ( event.keyCode ) {

				case scope.keys.UP:
					pan( 0, scope.keyPanSpeed );
					scope.update();
					break;

				case scope.keys.BOTTOM:
					pan( 0, - scope.keyPanSpeed );
					scope.update();
					break;

				case scope.keys.LEFT:
					pan( scope.keyPanSpeed, 0 );
					scope.update();
					break;

				case scope.keys.RIGHT:
					pan( - scope.keyPanSpeed, 0 );
					scope.update();
					break;

			}

		}

		function touchstart( event ) {

			if ( scope.enabled === false ) return;

			switch ( event.touches.length ) {

				case 1:	// one-fingered touch: rotate

					if ( scope.enableRotate === false ) return;

					state = STATE.TOUCH_ROTATE;

					rotateStart.set( event.touches[ 0 ].pageX, event.touches[ 0 ].pageY );
					break;

				case 2:	// two-fingered touch: dolly

					if ( scope.enableZoom === false ) return;

					state = STATE.TOUCH_DOLLY;

					var dx = event.touches[ 0 ].pageX - event.touches[ 1 ].pageX;
					var dy = event.touches[ 0 ].pageY - event.touches[ 1 ].pageY;
					var distance = Math.sqrt( dx * dx + dy * dy );
					dollyStart.set( 0, distance );
					break;

				case 3: // three-fingered touch: pan

					if ( scope.enablePan === false ) return;

					state = STATE.TOUCH_PAN;

					panStart.set( event.touches[ 0 ].pageX, event.touches[ 0 ].pageY );
					break;

				default:

					state = STATE.NONE;

			}

			if ( state !== STATE.NONE ) scope.dispatchEvent( startEvent );

		}

		function touchmove( event ) {

			if ( scope.enabled === false ) return;

			event.preventDefault();
			event.stopPropagation();

			var element = scope.domElement === document ? scope.domElement.body : scope.domElement;

			switch ( event.touches.length ) {

				case 1: // one-fingered touch: rotate

					if ( scope.enableRotate === false ) return;
					if ( state !== STATE.TOUCH_ROTATE ) return;

					rotateEnd.set( event.touches[ 0 ].pageX, event.touches[ 0 ].pageY );
					rotateDelta.subVectors( rotateEnd, rotateStart );

					// rotating across whole screen goes 360 degrees around
					constraint.rotateLeft( 2 * Math.PI * rotateDelta.x / element.clientWidth * scope.rotateSpeed );
					// rotating up and down along whole screen attempts to go 360, but limited to 180
					constraint.rotateUp( 2 * Math.PI * rotateDelta.y / element.clientHeight * scope.rotateSpeed );

					rotateStart.copy( rotateEnd );

					scope.update();
					break;

				case 2: // two-fingered touch: dolly

					if ( scope.enableZoom === false ) return;
					if ( state !== STATE.TOUCH_DOLLY ) return;

					var dx = event.touches[ 0 ].pageX - event.touches[ 1 ].pageX;
					var dy = event.touches[ 0 ].pageY - event.touches[ 1 ].pageY;
					var distance = Math.sqrt( dx * dx + dy * dy );

					dollyEnd.set( 0, distance );
					dollyDelta.subVectors( dollyEnd, dollyStart );

					if ( dollyDelta.y > 0 ) {

						constraint.dollyOut( getZoomScale() );

					} else if ( dollyDelta.y < 0 ) {

						constraint.dollyIn( getZoomScale() );

					}

					dollyStart.copy( dollyEnd );

					scope.update();
					break;

				case 3: // three-fingered touch: pan

					if ( scope.enablePan === false ) return;
					if ( state !== STATE.TOUCH_PAN ) return;

					panEnd.set( event.touches[ 0 ].pageX, event.touches[ 0 ].pageY );
					panDelta.subVectors( panEnd, panStart );

					pan( panDelta.x, panDelta.y );

					panStart.copy( panEnd );

					scope.update();
					break;

				default:

					state = STATE.NONE;

			}

		}

		function touchend( /* event */ ) {

			if ( scope.enabled === false ) return;

			scope.dispatchEvent( endEvent );
			state = STATE.NONE;

		}

		function contextmenu( event ) {

			event.preventDefault();

		}

		this.dispose = function() {

			this.domElement.removeEventListener( 'contextmenu', contextmenu, false );
			this.domElement.removeEventListener( 'mousedown', onMouseDown, false );
			this.domElement.removeEventListener( 'mousewheel', onMouseWheel, false );
			this.domElement.removeEventListener( 'MozMousePixelScroll', onMouseWheel, false ); // firefox

			this.domElement.removeEventListener( 'touchstart', touchstart, false );
			this.domElement.removeEventListener( 'touchend', touchend, false );
			this.domElement.removeEventListener( 'touchmove', touchmove, false );

			document.removeEventListener( 'mousemove', onMouseMove, false );
			document.removeEventListener( 'mouseup', onMouseUp, false );

			window.removeEventListener( 'keydown', onKeyDown, false );

		}

		this.domElement.addEventListener( 'contextmenu', contextmenu, false );

		this.domElement.addEventListener( 'mousedown', onMouseDown, false );
		this.domElement.addEventListener( 'mousewheel', onMouseWheel, false );
		this.domElement.addEventListener( 'MozMousePixelScroll', onMouseWheel, false ); // firefox

		this.domElement.addEventListener( 'touchstart', touchstart, false );
		this.domElement.addEventListener( 'touchend', touchend, false );
		this.domElement.addEventListener( 'touchmove', touchmove, false );

		window.addEventListener( 'keydown', onKeyDown, false );

		// force an update at start
		this.update();

	};

	THREE.OrbitControls.prototype = Object.create( THREE.EventDispatcher.prototype );
	THREE.OrbitControls.prototype.constructor = THREE.OrbitControls;

	Object.defineProperties( THREE.OrbitControls.prototype, {

		object: {

			get: function () {

				return this.constraint.object;

			}

		},

		target: {

			get: function () {

				return this.constraint.target;

			},

			set: function ( value ) {

				console.warn( 'THREE.OrbitControls: target is now immutable. Use target.set() instead.' );
				this.constraint.target.copy( value );

			}

		},

		minDistance : {

			get: function () {

				return this.constraint.minDistance;

			},

			set: function ( value ) {

				this.constraint.minDistance = value;

			}

		},

		maxDistance : {

			get: function () {

				return this.constraint.maxDistance;

			},

			set: function ( value ) {

				this.constraint.maxDistance = value;

			}

		},

		minZoom : {

			get: function () {

				return this.constraint.minZoom;

			},

			set: function ( value ) {

				this.constraint.minZoom = value;

			}

		},

		maxZoom : {

			get: function () {

				return this.constraint.maxZoom;

			},

			set: function ( value ) {

				this.constraint.maxZoom = value;

			}

		},

		minPolarAngle : {

			get: function () {

				return this.constraint.minPolarAngle;

			},

			set: function ( value ) {

				this.constraint.minPolarAngle = value;

			}

		},

		maxPolarAngle : {

			get: function () {

				return this.constraint.maxPolarAngle;

			},

			set: function ( value ) {

				this.constraint.maxPolarAngle = value;

			}

		},

		minAzimuthAngle : {

			get: function () {

				return this.constraint.minAzimuthAngle;

			},

			set: function ( value ) {

				this.constraint.minAzimuthAngle = value;

			}

		},

		maxAzimuthAngle : {

			get: function () {

				return this.constraint.maxAzimuthAngle;

			},

			set: function ( value ) {

				this.constraint.maxAzimuthAngle = value;

			}

		},

		enableDamping : {

			get: function () {

				return this.constraint.enableDamping;

			},

			set: function ( value ) {

				this.constraint.enableDamping = value;

			}

		},

		dampingFactor : {

			get: function () {

				return this.constraint.dampingFactor;

			},

			set: function ( value ) {

				this.constraint.dampingFactor = value;

			}

		},

		// backward compatibility

		noZoom: {

			get: function () {

				console.warn( 'THREE.OrbitControls: .noZoom has been deprecated. Use .enableZoom instead.' );
				return ! this.enableZoom;

			},

			set: function ( value ) {

				console.warn( 'THREE.OrbitControls: .noZoom has been deprecated. Use .enableZoom instead.' );
				this.enableZoom = ! value;

			}

		},

		noRotate: {

			get: function () {

				console.warn( 'THREE.OrbitControls: .noRotate has been deprecated. Use .enableRotate instead.' );
				return ! this.enableRotate;

			},

			set: function ( value ) {

				console.warn( 'THREE.OrbitControls: .noRotate has been deprecated. Use .enableRotate instead.' );
				this.enableRotate = ! value;

			}

		},

		noPan: {

			get: function () {

				console.warn( 'THREE.OrbitControls: .noPan has been deprecated. Use .enablePan instead.' );
				return ! this.enablePan;

			},

			set: function ( value ) {

				console.warn( 'THREE.OrbitControls: .noPan has been deprecated. Use .enablePan instead.' );
				this.enablePan = ! value;

			}

		},

		noKeys: {

			get: function () {

				console.warn( 'THREE.OrbitControls: .noKeys has been deprecated. Use .enableKeys instead.' );
				return ! this.enableKeys;

			},

			set: function ( value ) {

				console.warn( 'THREE.OrbitControls: .noKeys has been deprecated. Use .enableKeys instead.' );
				this.enableKeys = ! value;

			}

		},

		staticMoving : {

			get: function () {

				console.warn( 'THREE.OrbitControls: .staticMoving has been deprecated. Use .enableDamping instead.' );
				return ! this.constraint.enableDamping;

			},

			set: function ( value ) {

				console.warn( 'THREE.OrbitControls: .staticMoving has been deprecated. Use .enableDamping instead.' );
				this.constraint.enableDamping = ! value;

			}

		},

		dynamicDampingFactor : {

			get: function () {

				console.warn( 'THREE.OrbitControls: .dynamicDampingFactor has been renamed. Use .dampingFactor instead.' );
				return this.constraint.dampingFactor;

			},

			set: function ( value ) {

				console.warn( 'THREE.OrbitControls: .dynamicDampingFactor has been renamed. Use .dampingFactor instead.' );
				this.constraint.dampingFactor = value;

			}

		}

	} );

}() );


//from THREE.MeshLine/src/THREE.MeshLine.js
;(function() {

    "use strict";
    
    var root = this
    
    var has_require = typeof require !== 'undefined'
    
    var THREE = root.THREE || has_require && require('three')
    if( !THREE )
        throw new Error( 'MeshLine requires three.js' )
    
    function MeshLine() {
    
        this.positions = [];
    
        this.previous = [];
        this.next = [];
        this.side = [];
        this.width = [];
        this.indices_array = [];
        this.uvs = [];
        this.counters = [];
        this.geometry = new THREE.BufferGeometry();
    
        this.widthCallback = null;
    
        // Used to raycast
        this.matrixWorld = new THREE.Matrix4();
    }
    
    MeshLine.prototype.setMatrixWorld = function(matrixWorld) {
        this.matrixWorld = matrixWorld;
    }
    
    
    MeshLine.prototype.setGeometry = function( g, c ) {
        
        this.widthCallback = c;
    
        this.positions = [];
        this.counters = [];
        // g.computeBoundingBox();
        // g.computeBoundingSphere();
    
        // set the normals
        // g.computeVertexNormals();
        if( g instanceof THREE.Geometry ) {
            for( var j = 0; j < g.vertices.length; j++ ) {
                var v = g.vertices[ j ];
                var c = j/g.vertices.length;
                this.positions.push( v.x, v.y, v.z );
                this.positions.push( v.x, v.y, v.z );
                this.counters.push(c);
                this.counters.push(c);
            }
        }
    
        if( g instanceof THREE.BufferGeometry ) {
            // read attribute positions ?
        }
    
        if( g instanceof Float32Array || g instanceof Array ) {
            for( var j = 0; j < g.length; j += 3 ) {
                var c = j/g.length;
                this.positions.push( g[ j ], g[ j + 1 ], g[ j + 2 ] );
                this.positions.push( g[ j ], g[ j + 1 ], g[ j + 2 ] );
                this.counters.push(c);
                this.counters.push(c);
            }
        }
    
        this.process();
    
    }
    
    MeshLine.prototype.raycast = ( function () {
    
        var inverseMatrix = new THREE.Matrix4();
        var ray = new THREE.Ray();
        var sphere = new THREE.Sphere();
    
        return function raycast( raycaster, intersects ) {

            var precision = raycaster.params.Line.threshold;
            var precisionSq = precision * precision;

            var geometry = this.geometry;
    
            if ( geometry.boundingSphere === null ) geometry.computeBoundingSphere();

            // Checking boundingSphere distance to ray
    
            sphere.copy( geometry.boundingSphere );
            sphere.applyMatrix4( this.matrixWorld );
    
            var resultVec = new THREE.Vector3();
            raycaster.ray.intersectSphere( sphere, resultVec);
            if ( resultVec === false ) {
    
                return;
    
            }
    
            inverseMatrix.getInverse( this.matrixWorld );
            ray.copy( raycaster.ray ).applyMatrix4( inverseMatrix );
    
            var vStart = new THREE.Vector3();
            var vEnd = new THREE.Vector3();
            var interSegment = new THREE.Vector3();
            var interRay = new THREE.Vector3();
            var step = this instanceof THREE.LineSegments ? 2 : 1;
    
            if ( geometry instanceof THREE.BufferGeometry ) {
    
                var index = geometry.index;
                var attributes = geometry.attributes;
    
                if ( index !== null ) {
    
                    var indices = index.array;
                    var positions = attributes.position.array;
    
                    for ( var i = 0, l = indices.length - 1; i < l; i += step ) {
    
                        var a = indices[ i ];
                        var b = indices[ i + 1 ];
    
                        vStart.fromArray( positions, a * 3 );
                        vEnd.fromArray( positions, b * 3 );
    
                        var distSq = ray.distanceSqToSegment( vStart, vEnd, interRay, interSegment );
    
                        if ( distSq > precisionSq ) continue;
    
                        interRay.applyMatrix4( this.matrixWorld ); //Move back to world space for distance calculation
    
                        var distance = raycaster.ray.origin.distanceTo( interRay );
    
                        if ( distance < raycaster.near || distance > raycaster.far ) continue;
    
                        intersects.push( {
    
                            distance: distance,
                            // What do we want? intersection point on the ray or on the segment??
                            // point: raycaster.ray.at( distance ),
                            point: interSegment.clone().applyMatrix4( this.matrixWorld ),
                            index: i,
                            face: null,
                            faceIndex: null,
                            object: this
    
                        } );
    
                    }
    
                } else {
    
                    var positions = attributes.position.array;
    
                    for ( var i = 0, l = positions.length / 3 - 1; i < l; i += step ) {
    
                        vStart.fromArray( positions, 3 * i );
                        vEnd.fromArray( positions, 3 * i + 3 );
    
                        var distSq = ray.distanceSqToSegment( vStart, vEnd, interRay, interSegment );
    
                        if ( distSq > precisionSq ) continue;
    
                        interRay.applyMatrix4( this.matrixWorld ); //Move back to world space for distance calculation
    
                        var distance = raycaster.ray.origin.distanceTo( interRay );
    
                        if ( distance < raycaster.near || distance > raycaster.far ) continue;
    
                        intersects.push( {
    
                            distance: distance,
                            // What do we want? intersection point on the ray or on the segment??
                            // point: raycaster.ray.at( distance ),
                            point: interSegment.clone().applyMatrix4( this.matrixWorld ),
                            index: i,
                            face: null,
                            faceIndex: null,
                            object: this
    
                        } );
    
                    }
    
                }
    
            } else if ( geometry instanceof THREE.Geometry ) {
    
                var vertices = geometry.vertices;
                var nbVertices = vertices.length;
    
                for ( var i = 0; i < nbVertices - 1; i += step ) {
    
                    var distSq = ray.distanceSqToSegment( vertices[ i ], vertices[ i + 1 ], interRay, interSegment );
    
                    if ( distSq > precisionSq ) continue;
    
                    interRay.applyMatrix4( this.matrixWorld ); //Move back to world space for distance calculation
    
                    var distance = raycaster.ray.origin.distanceTo( interRay );
    
                    if ( distance < raycaster.near || distance > raycaster.far ) continue;
    
                    intersects.push( {
    
                        distance: distance,
                        // What do we want? intersection point on the ray or on the segment??
                        // point: raycaster.ray.at( distance ),
                        point: interSegment.clone().applyMatrix4( this.matrixWorld ),
                        index: i,
                        face: null,
                        faceIndex: null,
                        object: this
    
                    } );
    
                }
    
            }
    
        };
    
    }() );
    
    
    MeshLine.prototype.compareV3 = function( a, b ) {
    
        var aa = a * 6;
        var ab = b * 6;
        return ( this.positions[ aa ] === this.positions[ ab ] ) && ( this.positions[ aa + 1 ] === this.positions[ ab + 1 ] ) && ( this.positions[ aa + 2 ] === this.positions[ ab + 2 ] );
    
    }
    
    MeshLine.prototype.copyV3 = function( a ) {
    
        var aa = a * 6;
        return [ this.positions[ aa ], this.positions[ aa + 1 ], this.positions[ aa + 2 ] ];
    
    }
    
    MeshLine.prototype.process = function() {
    
        var l = this.positions.length / 6;
    
        this.previous = [];
        this.next = [];
        this.side = [];
        this.width = [];
        this.indices_array = [];
        this.uvs = [];
    
        for( var j = 0; j < l; j++ ) {
            this.side.push( 1 );
            this.side.push( -1 );
        }
    
        var w;
        for( var j = 0; j < l; j++ ) {
            if( this.widthCallback ) w = this.widthCallback( j / ( l -1 ) );
            else w = 1;
            this.width.push( w );
            this.width.push( w );
        }
    
        for( var j = 0; j < l; j++ ) {
            this.uvs.push( j / ( l - 1 ), 0 );
            this.uvs.push( j / ( l - 1 ), 1 );
        }
    
        var v;
    
        if( this.compareV3( 0, l - 1 ) ){
            v = this.copyV3( l - 2 );
        } else {
            v = this.copyV3( 0 );
        }
        this.previous.push( v[ 0 ], v[ 1 ], v[ 2 ] );
        this.previous.push( v[ 0 ], v[ 1 ], v[ 2 ] );
        for( var j = 0; j < l - 1; j++ ) {
            v = this.copyV3( j );
            this.previous.push( v[ 0 ], v[ 1 ], v[ 2 ] );
            this.previous.push( v[ 0 ], v[ 1 ], v[ 2 ] );
        }
    
        for( var j = 1; j < l; j++ ) {
            v = this.copyV3( j );
            this.next.push( v[ 0 ], v[ 1 ], v[ 2 ] );
            this.next.push( v[ 0 ], v[ 1 ], v[ 2 ] );
        }
    
        if( this.compareV3( l - 1, 0 ) ){
            v = this.copyV3( 1 );
        } else {
            v = this.copyV3( l - 1 );
        }
        this.next.push( v[ 0 ], v[ 1 ], v[ 2 ] );
        this.next.push( v[ 0 ], v[ 1 ], v[ 2 ] );
    
        for( var j = 0; j < l - 1; j++ ) {
            var n = j * 2;
            this.indices_array.push( n, n + 1, n + 2 );
            this.indices_array.push( n + 2, n + 1, n + 3 );
        }
    
        if (!this.attributes) {
            this.attributes = {
                position: new THREE.BufferAttribute( new Float32Array( this.positions ), 3 ),
                previous: new THREE.BufferAttribute( new Float32Array( this.previous ), 3 ),
                next: new THREE.BufferAttribute( new Float32Array( this.next ), 3 ),
                side: new THREE.BufferAttribute( new Float32Array( this.side ), 1 ),
                width: new THREE.BufferAttribute( new Float32Array( this.width ), 1 ),
                uv: new THREE.BufferAttribute( new Float32Array( this.uvs ), 2 ),
                index: new THREE.BufferAttribute( new Uint16Array( this.indices_array ), 1 ),
                counters: new THREE.BufferAttribute( new Float32Array( this.counters ), 1 )
            }
        } else {
            this.attributes.position.copyArray(new Float32Array(this.positions));
            this.attributes.position.needsUpdate = true;
            this.attributes.previous.copyArray(new Float32Array(this.previous));
            this.attributes.previous.needsUpdate = true;
            this.attributes.next.copyArray(new Float32Array(this.next));
            this.attributes.next.needsUpdate = true;
            this.attributes.side.copyArray(new Float32Array(this.side));
            this.attributes.side.needsUpdate = true;
            this.attributes.width.copyArray(new Float32Array(this.width));
            this.attributes.width.needsUpdate = true;
            this.attributes.uv.copyArray(new Float32Array(this.uvs));
            this.attributes.uv.needsUpdate = true;
            this.attributes.index.copyArray(new Uint16Array(this.indices_array));
            this.attributes.index.needsUpdate = true;
        }
    
        this.geometry.addAttribute( 'position', this.attributes.position );
        this.geometry.addAttribute( 'previous', this.attributes.previous );
        this.geometry.addAttribute( 'next', this.attributes.next );
        this.geometry.addAttribute( 'side', this.attributes.side );
        this.geometry.addAttribute( 'width', this.attributes.width );
        this.geometry.addAttribute( 'uv', this.attributes.uv );
        this.geometry.addAttribute( 'counters', this.attributes.counters );
    
        this.geometry.setIndex( this.attributes.index );
    
    }
    
    function memcpy (src, srcOffset, dst, dstOffset, length) {
        var i
    
        src = src.subarray || src.slice ? src : src.buffer
        dst = dst.subarray || dst.slice ? dst : dst.buffer
    
        src = srcOffset ? src.subarray ?
        src.subarray(srcOffset, length && srcOffset + length) :
        src.slice(srcOffset, length && srcOffset + length) : src
    
        if (dst.set) {
            dst.set(src, dstOffset)
        } else {
            for (i=0; i<src.length; i++) {
                dst[i + dstOffset] = src[i]
            }
        }
    
        return dst
    }
    
    /**
     * Fast method to advance the line by one position.  The oldest position is removed.
     * @param position
     */
    MeshLine.prototype.advance = function(position) {
    
        var positions = this.attributes.position.array;
        var previous = this.attributes.previous.array;
        var next = this.attributes.next.array;
        var l = positions.length;
    
        // PREVIOUS
        memcpy( positions, 0, previous, 0, l );
    
        // POSITIONS
        memcpy( positions, 6, positions, 0, l - 6 );
    
        positions[l - 6] = position.x;
        positions[l - 5] = position.y;
        positions[l - 4] = position.z;
        positions[l - 3] = position.x;
        positions[l - 2] = position.y;
        positions[l - 1] = position.z;
    
        // NEXT
        memcpy( positions, 6, next, 0, l - 6 );
    
        next[l - 6]  = position.x;
        next[l - 5]  = position.y;
        next[l - 4]  = position.z;
        next[l - 3]  = position.x;
        next[l - 2]  = position.y;
        next[l - 1]  = position.z;
    
        this.attributes.position.needsUpdate = true;
        this.attributes.previous.needsUpdate = true;
        this.attributes.next.needsUpdate = true;
    
    };
    
    THREE.ShaderChunk[ 'meshline_vert' ] = [
        '',
        THREE.ShaderChunk.logdepthbuf_pars_vertex,
        THREE.ShaderChunk.fog_pars_vertex,
        '',
        'attribute vec3 previous;',
        'attribute vec3 next;',
        'attribute float side;',
        'attribute float width;',
        'attribute float counters;',
        '',
        'uniform vec2 resolution;',
        'uniform float lineWidth;',
        'uniform vec3 color;',
        'uniform float opacity;',
        'uniform float near;',
        'uniform float far;',
        'uniform float sizeAttenuation;',
        '',
        'varying vec2 vUV;',
        'varying vec4 vColor;',
        'varying float vCounters;',
        '',
        'vec2 fix( vec4 i, float aspect ) {',
        '',
        '    vec2 res = i.xy / i.w;',
        '    res.x *= aspect;',
        '	 vCounters = counters;',
        '    return res;',
        '',
        '}',
        '',
        'void main() {',
        '',
        '    float aspect = resolution.x / resolution.y;',
        '    float pixelWidthRatio = 1. / (resolution.x * projectionMatrix[0][0]);',
        '',
        '    vColor = vec4( color, opacity );',
        '    vUV = uv;',
        '',
        '    mat4 m = projectionMatrix * modelViewMatrix;',
        '    vec4 finalPosition = m * vec4( position, 1.0 );',
        '    vec4 prevPos = m * vec4( previous, 1.0 );',
        '    vec4 nextPos = m * vec4( next, 1.0 );',
        '',
        '    vec2 currentP = fix( finalPosition, aspect );',
        '    vec2 prevP = fix( prevPos, aspect );',
        '    vec2 nextP = fix( nextPos, aspect );',
        '',
        '    float pixelWidth = finalPosition.w * pixelWidthRatio;',
        '    float w = 1.8 * pixelWidth * lineWidth * width;',
        '',
        '    if( sizeAttenuation == 1. ) {',
        '        w = 1.8 * lineWidth * width;',
        '    }',
        '',
        '    vec2 dir;',
        '    if( nextP == currentP ) dir = normalize( currentP - prevP );',
        '    else if( prevP == currentP ) dir = normalize( nextP - currentP );',
        '    else {',
        '        vec2 dir1 = normalize( currentP - prevP );',
        '        vec2 dir2 = normalize( nextP - currentP );',
        '        dir = normalize( dir1 + dir2 );',
        '',
        '        vec2 perp = vec2( -dir1.y, dir1.x );',
        '        vec2 miter = vec2( -dir.y, dir.x );',
        '        //w = clamp( w / dot( miter, perp ), 0., 4. * lineWidth * width );',
        '',
        '    }',
        '',
        '    //vec2 normal = ( cross( vec3( dir, 0. ), vec3( 0., 0., 1. ) ) ).xy;',
        '    vec2 normal = vec2( -dir.y, dir.x );',
        '    normal.x /= aspect;',
        '    normal *= .5 * w;',
        '',
        '    vec4 offset = vec4( normal * side, 0.0, 1.0 );',
        '    finalPosition.xy += offset.xy;',
        '',
        '    gl_Position = finalPosition;',
        '',
        THREE.ShaderChunk.logdepthbuf_vertex,
      THREE.ShaderChunk.fog_vertex && '    vec4 mvPosition = modelViewMatrix * vec4( position, 1.0 );',
      THREE.ShaderChunk.fog_vertex,
        '}'
    ].join( '\r\n' );
    
    THREE.ShaderChunk[ 'meshline_frag' ] = [
        '',
        THREE.ShaderChunk.fog_pars_fragment,
        THREE.ShaderChunk.logdepthbuf_pars_fragment,
        '',
        'uniform sampler2D map;',
        'uniform sampler2D alphaMap;',
        'uniform float useMap;',
        'uniform float useAlphaMap;',
        'uniform float useDash;',
        'uniform float dashArray;',
        'uniform float dashOffset;',
        'uniform float dashRatio;',
        'uniform float visibility;',
        'uniform float alphaTest;',
        'uniform vec2 repeat;',
        '',
        'varying vec2 vUV;',
        'varying vec4 vColor;',
        'varying float vCounters;',
        '',
        'void main() {',
        '',
        THREE.ShaderChunk.logdepthbuf_fragment,
        '',
        '    vec4 c = vColor;',
        '    if( useMap == 1. ) c *= texture2D( map, vUV * repeat );',
        '    if( useAlphaMap == 1. ) c.a *= texture2D( alphaMap, vUV * repeat ).a;',
        '    if( c.a < alphaTest ) discard;',
        '    if( useDash == 1. ){',
        '        c.a *= ceil(mod(vCounters + dashOffset, dashArray) - (dashArray * dashRatio));',
        '    }',
        '    gl_FragColor = c;',
        '    gl_FragColor.a *= step(vCounters, visibility);',
        '',
        THREE.ShaderChunk.fog_fragment,
        '}'
    ].join( '\r\n' );
    
    function MeshLineMaterial( parameters ) {
    
        THREE.ShaderMaterial.call( this, {
            uniforms: Object.assign({},
                THREE.UniformsLib.fog,
                {
                    lineWidth: { value: 1 },
                    map: { value: null },
                    useMap: { value: 0 },
                    alphaMap: { value: null },
                    useAlphaMap: { value: 0 },
                    color: { value: new THREE.Color( 0xffffff ) },
                    opacity: { value: 1 },
                    resolution: { value: new THREE.Vector2( 1, 1 ) },
                    sizeAttenuation: { value: 1 },
                    near: { value: 1 },
                    far: { value: 1 },
                    dashArray: { value: 0 },
                    dashOffset: { value: 0 },
                    dashRatio: { value: 0.5 },
                    useDash: { value: 0 },
                    visibility: {value: 1 },
                    alphaTest: {value: 0 },
                    repeat: { value: new THREE.Vector2( 1, 1 ) },
                }
            ),
    
            vertexShader: THREE.ShaderChunk.meshline_vert,
    
            fragmentShader: THREE.ShaderChunk.meshline_frag,
    
        } );
    
        this.type = 'MeshLineMaterial';
    
        Object.defineProperties( this, {
            lineWidth: {
                enumerable: true,
                get: function () {
                    return this.uniforms.lineWidth.value;
                },
                set: function ( value ) {
                    this.uniforms.lineWidth.value = value;
                }
            },
            map: {
                enumerable: true,
                get: function () {
                    return this.uniforms.map.value;
                },
                set: function ( value ) {
                    this.uniforms.map.value = value;
                }
            },
            useMap: {
                enumerable: true,
                get: function () {
                    return this.uniforms.useMap.value;
                },
                set: function ( value ) {
                    this.uniforms.useMap.value = value;
                }
            },
            alphaMap: {
                enumerable: true,
                get: function () {
                    return this.uniforms.alphaMap.value;
                },
                set: function ( value ) {
                    this.uniforms.alphaMap.value = value;
                }
            },
            useAlphaMap: {
                enumerable: true,
                get: function () {
                    return this.uniforms.useAlphaMap.value;
                },
                set: function ( value ) {
                    this.uniforms.useAlphaMap.value = value;
                }
            },
            color: {
                enumerable: true,
                get: function () {
                    return this.uniforms.color.value;
                },
                set: function ( value ) {
                    this.uniforms.color.value = value;
                }
            },
            opacity: {
                enumerable: true,
                get: function () {
                    return this.uniforms.opacity.value;
                },
                set: function ( value ) {
                    this.uniforms.opacity.value = value;
                }
            },
            resolution: {
                enumerable: true,
                get: function () {
                    return this.uniforms.resolution.value;
                },
                set: function ( value ) {
                    this.uniforms.resolution.value.copy( value );
                }
            },
            sizeAttenuation: {
                enumerable: true,
                get: function () {
                    return this.uniforms.sizeAttenuation.value;
                },
                set: function ( value ) {
                    this.uniforms.sizeAttenuation.value = value;
                }
            },
            near: {
                enumerable: true,
                get: function () {
                    return this.uniforms.near.value;
                },
                set: function ( value ) {
                    this.uniforms.near.value = value;
                }
            },
            far: {
                enumerable: true,
                get: function () {
                    return this.uniforms.far.value;
                },
                set: function ( value ) {
                    this.uniforms.far.value = value;
                }
            },
            dashArray: {
                enumerable: true,
                get: function () {
                    return this.uniforms.dashArray.value;
                },
                set: function ( value ) {
                    this.uniforms.dashArray.value = value;
                    this.useDash = ( value !== 0 ) ? 1 : 0
                }
            },
            dashOffset: {
                enumerable: true,
                get: function () {
                    return this.uniforms.dashOffset.value;
                },
                set: function ( value ) {
                    this.uniforms.dashOffset.value = value;
                }
            },
            dashRatio: {
                enumerable: true,
                get: function () {
                    return this.uniforms.dashRatio.value;
                },
                set: function ( value ) {
                    this.uniforms.dashRatio.value = value;
                }
            },
            useDash: {
                enumerable: true,
                get: function () {
                    return this.uniforms.useDash.value;
                },
                set: function ( value ) {
                    this.uniforms.useDash.value = value;
                }
            },
            visibility: {
                enumerable: true,
                get: function () {
                    return this.uniforms.visibility.value;
                },
                set: function ( value ) {
                    this.uniforms.visibility.value = value;
                }
            },
            alphaTest: {
                enumerable: true,
                get: function () {
                    return this.uniforms.alphaTest.value;
                },
                set: function ( value ) {
                    this.uniforms.alphaTest.value = value;
                }
            },
            repeat: {
                enumerable: true,
                get: function () {
                    return this.uniforms.repeat.value;
                },
                set: function ( value ) {
                    this.uniforms.repeat.value.copy( value );
                }
            },
        });
    
        this.setValues( parameters );
    }
    
    MeshLineMaterial.prototype = Object.create( THREE.ShaderMaterial.prototype );
    MeshLineMaterial.prototype.constructor = MeshLineMaterial;
    MeshLineMaterial.prototype.isMeshLineMaterial = true;
    
    MeshLineMaterial.prototype.copy = function ( source ) {
    
        THREE.ShaderMaterial.prototype.copy.call( this, source );
    
        this.lineWidth = source.lineWidth;
        this.map = source.map;
        this.useMap = source.useMap;
        this.alphaMap = source.alphaMap;
        this.useAlphaMap = source.useAlphaMap;
        this.color.copy( source.color );
        this.opacity = source.opacity;
        this.resolution.copy( source.resolution );
        this.sizeAttenuation = source.sizeAttenuation;
        this.near = source.near;
        this.far = source.far;
        this.dashArray.copy( source.dashArray );
        this.dashOffset.copy( source.dashOffset );
        this.dashRatio.copy( source.dashRatio );
        this.useDash = source.useDash;
        this.visibility = source.visibility;
        this.alphaTest = source.alphaTest;
        this.repeat.copy( source.repeat );
    
        return this;
    
    };
    
    if( typeof exports !== 'undefined' ) {
        if( typeof module !== 'undefined' && module.exports ) {
            exports = module.exports = { MeshLine: MeshLine, MeshLineMaterial: MeshLineMaterial };
        }
        exports.MeshLine = MeshLine;
        exports.MeshLineMaterial = MeshLineMaterial;
    }
    else {
        root.MeshLine = MeshLine;
        root.MeshLineMaterial = MeshLineMaterial;
    }
    
    }).call(this);