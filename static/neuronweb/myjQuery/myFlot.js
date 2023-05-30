/* 
Sahil's Code Below
$(document).ready(function() {
	var AddMenuInput = $('.AddMenuInput');
	var AddMenu = $('.AddMenu');
	
	 AddMenu.click(function() {
		var intValue = AddMenuInput.val();
		$('#menu'+intValue).menu();
	 });
});*/

var plottedFlot = {}; //empty object

function Plot(flotID, id, data, opts) {
        if (opts == undefined) {opts = {}};
		var counter = 0;
		var d1 = [];
		for (var i = 0; i < 14; i += 0.5) {
			d1.push([i, Math.sin(i)]);
		}
		var d2 = [[0, 3], [4, 8], [8, 5], [9, 13]];

		// A null signifies separate line segments
		var d3 = [[0, 12], [7, 12], null, [7, 2.5], [12, 2.5]];

		plottedFlot[flotID] = $.plot("#"+flotID, [ d1, d2, d3 ], {
		    yaxis: {min: data.ymin, max: data.ymax}, 
		    xaxis: {min: data.xmin, max: data.xmax},
		    zoom:  {interactive: true},
		    pan:   {interactive: true},
		    xaxes: [{axisLabel: 'x label', labelcolor: 'black'}],
		    yaxes: [{axisLabel: 'y label', labelcolor: 'black'}],
		    grid: {'hoverable': true, 'clickable': true}
		});
		
		if (opts['contextmenu'] == undefined) {
		    contextmenu = true;
	    } else {
	        contextmenu = opts['contextmenu'];
        }
        if (contextmenu) {
		
		    $('#'+flotID).bind("contextmenu",function(e){return false;}); //In the div, contextmenu is not to appear onclick.(save as, view source, etc options)
		    /*$('#placeholder').bind("contextmenu",function(e){return false;}); //In the div, contextmenu is not to appear onclick.(save as, view source, etc options)*/
		    $('#menuDiv' + id).bind("contextmenu",function(e){return false;});
		    $('#menu' + id).bind("contextmenu",function(e){return false;});
		
		    $('#'+flotID).mousedown(
		    function(event){
			    if(event.which == 3)
			    {
				    if($('#menuDiv' + id)[0].className=="menu-visible"){
					    $('#menuDiv' + id)[0].className="menu-invisible";
					    }
				    else if($('#menuDiv' + id)[0].className=="menu-invisible"){
					    $('#menuDiv' + id)[0].className="menu-visible";
					    }
					
			    var parentOffset = $(this).parent().offset(); 
				    var relX = event.pageX;// - parentOffset.left;
				    var relY = event.pageY;
				    console.log('rely=' + relY);
				    $('#menu' + id)[0].style.cssText="font-size: 62.5%; position:relative; left:"+ relX + "px; top:"+ relY + "px";		
			    }
		    });
		
		    $('#menuDiv' + id).click(
		    function(event){
					    $('#menuDiv' + id)[0].className="menu-invisible";
					    });
		    /*
		    We don't need flot to be resizeable right now.
		    $( ".placeholder" ).resizable();
		    */
		
		    };
        }
        
		function SetRange (flot, xmin, xmax, ymin, ymax){
			flot.getAxes().xaxis.options.min=xmin;
			flot.getAxes().xaxis.options.max=xmax;
			flot.getAxes().yaxis.options.min=ymin;
			flot.getAxes().yaxis.options.max=ymax;
			flot.setupGrid();
			flot.draw();
		}
	
