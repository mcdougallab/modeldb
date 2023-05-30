// NOTE: Must be loaded after main.js for event capture to work

var counter=0;
var i=0;

    poll_success = function(response) {
        /*
            examples of valid create messages:
            
            ["create", "dialog", "title", 1] -- 4th entry: True if max/min buttons; else False
            ["create", "button", divid, "text"]
            ["create", "label", divid, "text"]
                        
            returns:
            
            [-1, ['create', original obj, id created], user id]
            
            
            
            examples of valid change messages:
            
            ["change", "text", objid, "new text"] -- use for bottons and labels
            ["change", "value", objid, "new value"] -- use this for text fields
            ["change", "graph", objid, [[x1, y1], [x2, y2]]] -- for graphs


            examples of valid get messages:
            
            ["get", "text", objid] -- use for bottons and labels
            ["get", "value", objid] -- use this for text fields
            
            returns:
            
            [-1, ['create', original obj, id created], user id]
            
            
            examples of valid style message:
            
            ["style", objid, "color", "red"] -- changes the CSS property "color" of objid to "red" 
            
        */
        response = JSON.parse(response);
        console.log("parsing json inside of mydialog.js ;)");
        console.log(response);
        // response = JSON.parse(response);
        switch (response[0]) {
            case 'create':
                var create_what = response[1];
                var id = -1;
                switch (create_what) {
                    case 'dialog':
                        id = MakeDialog(response[2], response[3]);
                        console.log("in dialog", id);
                        break;
                    case 'button':			
						var counterCopy=counter+1;
                        id = AddButton(response[2], response[3], function() { 
							send_to_server(counterCopy, 'clicked');
						});
                        console.log("in button", id);
                        break;
                    case 'label':
                        id = AddLabel(response[2], response[3]);
                        console.log("in label", id);
                        break;
                    case 'textfield':
                        id = AddTextField(response[2], response[3]);
                        console.log("in textfield", id);
                        break;
                    case 'graph':
                        id = AddChart(response[2]);
                        redraw_chart(id, []);
                        console.log("in graph", id);
                        break;
                    default:
                        console.log("the create statement didn't work! :(");
                }
                send_to_server(-1, ['create', response, id]);
                break;
            case 'change':
                var obj = $('#' + response[2]);
                switch (response[1]) {
                    case 'text':
                        obj.text(response[3]);
                        break;
                    case 'value':
                        obj[0].value = response[3];
                        break;
                    case 'graph':
                        redraw_chart(response[2], response[3]);
                }
                break;
            case 'get':
                var obj = $('#' + response[2]);
                var result = '';
                switch (response[1]) {
                    case 'text':
                        result = obj.text();
                        break;
                    case 'value':
                        result = obj[0].value;
                        break;
                }
                send_to_server(-1, ['get', response, result]);                
                break;
            case 'style':
                var obj = $('#' + response[1]);
                obj[0].style[response[2]] = response[3];
                break;
            default:
                console.log("it didn't work :'(");
        }
       // window.setTimeout(poll, 0);
    };


    function close_browser_window() {
        win = window.open('', '_self');
        win.close();
    }
    
    function redraw_chart(id, data2) {
        // TODO: allow this to plot more than one thing, set plot options
        $.plot($('#placeholder' + id), [{data:data2, color: 'black'}]);
    }

    function max(a, b) {
        if (a > b) return a;
        return b;
    }

    function project_pt(pt, view) {
        /* view == 0: x-y plane
         * view == 1: x-z plane
         * view == 2: y-z plane
         */
        if (view == 0 || view == undefined) return [pt[0], pt[1]];
        if (view == 1) return [pt[0], pt[2]];
        if (view == 2) return [pt[1], pt[2]];
        console.log('unsupported projection view: ' + view);
    }
    
    neuron_data_ = {};
    neuron_view_ = {};
    neuron_colors_ = {};
    neuron_markers_ = {};
    neuron_hoverable_ = {};
    neuron_clickable_ = {};
    function redraw_neuron(id) {
        /* view == 0: x-y plane
         * view == 1: x-z plane
         * view == 2: y-z plane
         */
        if (!$('#placeholder' + (id + 2)).length) {
            // this would indicate the graph has been removed
            return;
        }
        data = neuron_data_[id];
        view = neuron_view_[id];
        colors = neuron_colors_[id];
        var plot_data = [];
        $.each(data, function(i, segment) {
            var color = 'black';
            if (colors != undefined) color = colors[i];
            var local_plot_data = [];
            $.each(segment, function(j, pt) {
                local_plot_data.push(project_pt(pt, view));
            });
            plot_data.push({data: local_plot_data, color: color});
        });
        if (neuron_markers_[id] != undefined) {
            var local_plot_data = [];
            $.each(neuron_markers_[id], function(i, pt) {
                local_plot_data.push(project_pt(pt, view));
            });
            plot_data.push({data: local_plot_data, points: {show: true}, color: 'red'});
        }
        // offset of 2 because id = the window, id + 1 = the button set
        plottedFlot['placeholder' + (id + 2)] = $.plot($('#placeholder' + (id + 2)), plot_data, {
            yaxis: {min: data.ymin, max: data.ymax}, 
            xaxis: {min: data.xmin, max: data.xmax},
            zoom:  {interactive: true},
            pan:   {interactive: true},
            grid:  {show: false, hoverable: neuron_hoverable_[id], clickable: neuron_clickable_[id]}
        });
    }
    
    function set_neuron_colors(id, colors) {
        neuron_colors_[id] = colors;
        redraw_neuron(id);
    }
    
    // highlight neuron segments by indexes
    function set_neuron_highlights(id, highlight_segments) {
        var colors = [];
        var i, stop = neuron_data_[id].length;
        for (i = 0; i < stop; i++) {
            colors.push('black');
        }
        for (i = 0; i < highlight_segments.length; i++) {
            colors[highlight_segments[i]] = 'red';
        }
        set_neuron_colors(id, colors);
    }
    
    function hide_dialog(id) {
        $('#' + id).parent().css('display', 'none');
    }

    function show_dialog(id) {
        $('#' + id).parent().css('display', 'block');
    }
    
    function set_neuron_markers(id, markers) {/*
        // force positive height
        if ($('#placeholder' + (id + 2)).height() == 0) {
            $('#placeholder' +(id + 2)).height(300);
        } */
        neuron_markers_[id] = markers;
        redraw_neuron(id);
    }

    function MakeNeuronViewer(title, data, parent_id) {
        /*
         * data consists of lists of lists of x, y, z, diameter points
         * when applying colors to the neurons, each of the inner lists (typically (?) corresponding to a NEURON segment)
         * gets a single color.
         * Example data:
         * [[[x1, y1, z1, d1], [x2, y2, z2, d2], [x3, y3, z3, d3]], [[x4, y4, z4, d4], [x5, y5, z5, d5]]
         * 
         * These viewers are unclosable.
         */
        let id;
        if (parent_id === undefined) {
            id = MakeDialog(title, true);
        } else {
            counter++;
            id = counter;
            $(`#${parent_id}`).append(`<div class="vbox" id="${id}" style="border: 1px black solid; padding: 1em"></div>`);
        }
        $('#' + id).parent().addClass('no-close');
        neuron_colors_[id] = undefined;
        neuron_data_[id] = data;
        var panel_id = AddButtonSet(id, ['X-Y', 'X-Z', 'Y-Z'], {selected:0, callback: function(a) {neuron_view_[id] = a; redraw_neuron(id);}});
        // center the button set
        $('#' + id + ' form').css('text-align', 'center');
        var flot_id = AddChart(id, {contextmenu: false, doplot: false});
        redraw_neuron(id);
        // a space for putting things below the graph
        $('#' + id).append('<div id="below' + id + '" style="display:none;"></div>');
        $('#' + id).resize(function() {
            $('#placeholder' + flot_id).height(max(250, $('#' + id).height() - $('#' + panel_id).height() - $('#below' + id).height() - 50));        
            plottedFlot['placeholder' + flot_id].draw();
        });
        return id;
    }

    function MakeDialog(title, dialogExtend){
        counter++;
        if(dialogExtend){
            $('<div class="vbox" id=\"' + counter + '\"></div>')
            .dialog({title:title, closeOnEscape: false})
            .dialogExtend({'dblclick':'maximize','maximizable': true, 'minimizable': true});
        }
        
        else
        {
            $('<div class="vbox" id=\"' + counter + '\"></div>')
            .dialog({title:title, closeOnEscape: false});
        }
        return counter;
      };
      
    function AddComponent(id, html){
        if ($('#'+id)[0].className.indexOf('vbox') != -1){
            $('#'+id).append(html + '<br/>');
        }
        else
        {
            $('#'+id).append('<td>'+html+'</td>');
        }
        return counter;
    }
    
    function DeclareCSSClass(name, css) {
        $('<style type="text/css"> .' + name + '{ ' + css + '}</style>').appendTo('head');
    };
    
    function AddLabel(id, label){ 
        counter++;
        return AddComponent(id , '<label id="' + counter + '">' + label + '</label>');
    };      
    
    function AddTextField(id, defaultText){
        counter++;
        return AddComponent(id , '<input type="text" id="' + counter + '" value="' + defaultText + '"></input>');
    };
    
    function AddButton(id, btnText, callback){
        counter++;
		var button_id = AddComponent(id , '<button id="'+counter+'">' + btnText + '</button>');
		if (!(callback === undefined))
			$('#' + button_id).click(callback);
		return button_id;        
    };
	
	function AddSpinner(id, defaultText){
        counter++;
        var spinner_id = AddComponent(id , '<input type="text" id="' + counter + '" value="' + counter + '"></input>');
		$('#'+spinner_id).spinner();
		return spinner_id;
    };

    function AddButtonSet(id, btnTexts, options) {
        if (options === undefined) options = {};
        var selected = options['selected'];
        var callback = options['callback'];
        counter++;
        var group_id = AddComponent(id, '<form><div id="' + counter + '"></div></form>');
        var group = $('#' + group_id);
        $.each(btnTexts, function(i, text) {
            var extra_text = '';
            if (i == selected) extra_text = ' checked="checked" ';
            group.append('<input type="radio"' + extra_text + ' id="' + counter + 'a' + i + '" value="' + i + '" name = "' + counter + '"/><label for="' + counter + 'a' + i + '">' + text + '</label>');
        });
        group.buttonset();
        if (callback === undefined) {} else {
            group.change(function() {
                callback($('#' + group_id + ' input:radio:checked').val());
            });
        }
        return group_id;
    };
    
    function AddTree(id, data) {
        var ul_id = AddTreeHelper(id, data);
        $('#' + ul_id + ' span').click(function() {
            if (!$(this).hasClass('noop')) {
                $('#' + ul_id + ' span').removeClass('selected');
                $(this).addClass('selected');
            }
        });
        $('#' + ul_id).treeview({
            collapsed: true
        });
    }

    function AddTreeHelper(id, data) {
        counter++;
        $('#' + id).append('<ul id="' + counter + '"></ul>');
        var ul = $('#' + counter);
        var ul_id = counter;
        var opts, callback;
        $.each(data, function(i, row) {
            counter++;
            var do_noop = '';
            if (row[1]['noop'] == true) {
                do_noop = ' class="noop"';
            }
            ul.append('<li id="' + counter + '"><span' + do_noop + '>' + row[0] + '</span></li>');
            opts = row[1];
            if (opts != undefined) {
                callback = opts['callback'];
                if (callback != undefined) {
                    $('#' + counter + ' span').click(callback);
                }
                children = opts['children'];
                if (children != undefined) {
                    AddTreeHelper(counter, children);
                }
            }
        });
        return ul_id;
    }    
    
    function AddAccordion(id, items) {
        counter++;
        var accordion_id = AddComponent(id, '<div id="' + counter + '"></div>');
        var accordion = $('#' + accordion_id);
        $.each(items, function(i, name) {
            accordion.append('<h3>'+name+'</h3><div class="vbox" id="' + accordion_id + 'a' + i + '"></div>');
        });
        accordion.accordion({
            heightStyle: 'fill',
            collapsible: true
        });
        $('#' + id).on("resize", function(event, ui) {accordion.accordion('refresh')});
        return accordion_id;
    };
    
    function AddChart(id, opts) {
        if (opts === undefined) {opts = {}};
        counter++;
        $('body').append(AssembleMenuString(counter));
        AddComponent(id , '<span id="flotContainer' + counter + '">' + '<div class="placeholder" id="placeholder' + counter + '" class="demo-placeholder" style="height:300px"></div></span>');
        $('#menu' + counter).menu();
        //console.log('#menu' + counter);
        data = {xmin:1, xmax:10, ymin:1, ymax:10}; //ARBITRARY!
        if (opts['contextmenu'] == undefined) opts['contextmenu'] = true;
        if (opts['doplot'] == undefined) opts['doplot'] = true;
        if (opts['doplot']) {
            Plot("placeholder" + counter, counter, data, opts); 
        }
        
        $('#placeholder'+counter).bind("contextmenu",function(e){return false;}); //In the div, contextmenu is not to appear onclick.(save as, view source, etc options)
        return counter;
    };
    
    function AddDropdown(id, list){
        counter++;
        $('#'+id).append('<select id="' + counter + '">');
        for(var i=0; i<list.length; i++){
            $('#'+counter).append('<option>' + list[i] + '</option>')
            };
        $('#'+id).append('</select>');
        return counter;
        };
        
    function SetViewMenu(id){
        //console.log('id:' + id);
        var dialogID = MakeDialog('Set View');
        var flot= plottedFlot['placeholder'+id];
        
        AddLabel(dialogID, 'X Min'); // dialogID is what we're appending to; counter is the label's id
        AddTextField(dialogID, flot.getXAxes()[0].min); 
        xminField=$('#'+counter)[0];
        
        AddLabel(dialogID, 'X Max');
        AddTextField(dialogID, flot.getXAxes()[0].max);
        xmaxField=$('#'+counter)[0];
        
        AddLabel(dialogID, 'Y Min');
        AddTextField(dialogID, flot.getYAxes()[0].min);
        yminField=$('#'+counter)[0];    
        
        AddLabel(dialogID, 'Y Max');
        AddTextField(dialogID, flot.getYAxes()[0].max);
        ymaxField=$('#'+counter)[0];
        
        var hboxID = AddHbox(dialogID, 3)
        
        var cancelButtonID= AddButton(hboxID, 'Cancel');
        var okButtonID=AddButton(hboxID, 'Ok');
        
        //console.log(dialogID + 'is dialog ID');
        //console.log(cancelButtonID + 'is cancelButtonID');
        
        $('#'+ cancelButtonID).click(function(){$('#'+dialogID).dialog('close');});
        $('#'+ okButtonID).click(function(){
            SetRange(flot, xminField.value, xmaxField.value, yminField.value, ymaxField.value);
            $('#'+dialogID).dialog('close');
            });
    };
        
    function AssembleMenuString(id){
        return(
            '<div id="menuDiv' + id + '" class="menu-invisible">' +
             '<ul id="menu' + id + '" style="font-size:62.5%">' +
              '<li><a href="#">View</a>' +
              '<ul>' +
                '<li><a href="#">View = plot</a></li>' +
                '<li><a href="#" onclick="SetViewMenu(' + id + ')">Set View</a></li>' +
                '<li><a href="#">10%&nbsp;Zoom&nbsp;out</a></li>' +
                '<li><a href="#">10% Zoom in</a></li>' +
                '<li><a href="#">New View</a></li>' +
                '<li><a href="#">Zoom in/out</a></li>' +
                '<li><a href="#">Translate</a></li>' +
                '<li><a href="#">Round View</a></li>' +
                '<li><a href="#">Whole Scene</a></li>' +
                '<li><a href="#">Scene=view</a></li>' +
                '<li><a href="#">Object Name</a></li>' +
              '</ul>' +
              '</li>' +
              '<li><a href="#">Crosshair</a></li>' +
              '<li><a href="#">Plot What?</a></li>' +
              '<li><a href="#">Pick Vector</a></li>' +
              '<li><a href="#">Color/Brush</a></li>' +
              '<li><a href="#">Axis Type</a>' +
                '<ul>' +
                  '<li><a href="#">View Axis</a></li>' +
                  '<li><a href="#">New Axis</a></li>' +
                  '<li><a href="#">View Box</a></li>' +
                  '<li><a href="#">Erase&nbsp;Axis</a></li>' +
                '</ul>' +
              '</li>' +
              '<li><a href="#">Keep Lines</a></li>' +
              '<li><a href="#">Family Label?</a></li>' +
              '<li><a href="#">Erase</a></li>' +
              '<li><a href="#">Move Text</a></li>' +
              '<li><a href="#">Change Text</a></li>' +
              '<li><a href="#">Delete</a></li>' +
            '</ul>' +
        '</div> ');
    }

    function AddVbox(id, frame){
        counter++;
        $('#'+id).append('<div class="vbox" id="'+counter+'"></div>');
        return counter;
    }
    
    function AddHbox(id, frame){
        counter++;
        $('#'+id).append('<div class="hbox" id="'+counter+'">');
        counter++;
        $('#'+id).append('<table><tbody><tr id="'+(counter)+'"></tr></tbody></table></div>');
        return counter;
    }

	function AddToolsRunControl(){
		console.log('counter in addtools:', counter);
		MakeDialog('RunControl '+(counter+1), true);
		console.log('counter after making dialog:', counter);
		var numHboxes=13; //number of options for the run-control panel.
		
		for (i=0; i<numHboxes; i++){
			var boxid = AddHbox(1, 1);
			AddButton(boxid, 'button ' + boxid);
			console.log('counter after making hbox:', counter);
		};
		
		return counter;
	
	}
