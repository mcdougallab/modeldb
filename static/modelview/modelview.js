var modelview_neuron_viewers = [];

var last_right, last_top;
var doc_width = document.width;
var default_action = [];
var cellviews;

function reposition_dialog(id) {
    // set next to the last positioned dialog
    var me = $('#' + id);
    var mep = me.parent();
    mep.offset({left: last_right + 10, top: last_top});

    // except: drop down if too far to the right
    if (mep.offset().left + mep.outerWidth() > doc_width) {
        mep.offset({left: 20, top: last_top + 100});
    }
    last_top = mep.offset().top;
    last_right = mep.offset().left + mep.outerWidth();
}

var colorbar_types = [];

var did_sub;

function init_modelview() {
    // only call setup modelview if no substitutions to do
    // if there are substitutions, process_level_ will recall init_modelview
    // when done
    did_sub = false;
    process_level_(modelview_data.tree);
    if (did_sub) {
        // if here, then did an include so stop and will be rerun later
        return;
    }
    setup_modelview();
    
    $.each(default_action, function(i, action) {
        if (action != undefined) {
            action(false);
        }
    });
}

var json_parent_obj_, json_index_;

function jsonp_callback_(new_row) {
    json_parent_obj_[json_index_] = new_row;
    init_modelview();
}

function process_level_(data) {
    // returns true if requested a substitution; else false
    $.each(data, function(i, row) {
        if (row.include != undefined) {
            //to convert the .asp to .cshtml, add by rixin wang 20160408
            row.include = row.include.replace("modelview_components.asp", "modelview_components.cshtml");

            // do substitution via JSONP
            json_index_ = i;
            json_parent_obj_ = data;
            
            // force including from the internet when testing locally
            // TODO: is this always a good idea?
            if ((window.location.protocol == 'file:' || window.location.protocol == 'file') && row.include.substr(0, 2) == '//') {
                row.include = 'https:' + row.include;
            }
            
            $('body').append('<script src="' + row.include + '"></script>');
            did_sub = true;
        }
        if (did_sub) {
            return true;
        }
        if (row.include == undefined && row.children != undefined) {
            if (process_level_(row.children)) {
                return true;
            }
        }
    });
    return false;
}


function setup_modelview() {
    cellviews = modelview_data.cellviews;
    if (modelview_data.title != undefined) {
        document.title = 'ModelView: ' + modelview_data.title;
    } else {
        document.title = 'ModelView';
        modelview_data.title = 'ModelView';
    }
    
    if (modelview_data.short_title == undefined) {
        modelview_data.short_title = modelview_data.title;
    }
    
    if (modelview_data.colorbars != undefined) {
        $.each(modelview_data.colorbars, function(i, colorbar_data) {
            colorbar_types.push(colorbar_data.type);
            if (colorbar_data.type == 'css') {
                DeclareCSSClass('colorbar' + i, colorbar_data.css);
            } else {
                console.log('unknown colorbar type: ' + colorbar_data.type)
            }
        });
    }
    // create a dialog for the tree with no close box
    tree_dialog = "modelview_tree"; // MakeDialog(modelview_data.short_title, true);
    var tree_dialog_handle = $('#' + tree_dialog);
    
    if (modelview_data.stochastic == true) {
        AddComponent(tree_dialog, '<div style="background-color: #ff5a5a;"><b>This model contains stochastic features.</b> This is one possible view.</div>');
    }
    
    // generate the tree
    AddTree(tree_dialog, modelview_build_tree_(modelview_data.tree));

    last_top = tree_dialog_handle.parent().offset().top;
    last_right = tree_dialog_handle.parent().offset().left + tree_dialog_handle.parent().outerWidth();
    
    last_positioned_dialog = tree_dialog;
    
    // open all links in new window, based on http://trevordavis.net/blog/use-jquery-to-open-all-external-links-in-a-new-window
    $('a').attr('target', '_blank');
    
    // setup the neuron views
    if (modelview_data.neuron == undefined) {
        modelview_data.neuron = [];
    }

    if (modelview_data.neuronviewer == undefined) {
        modelview_data.neuronviewer = [];
    }
    
    $.each(modelview_data.neuronviewer, function(i, neuron_view) {
        var neuron_data = modelview_data.neuron[neuron_view];
        var my_cell_views = undefined;
        if (modelview_data.cellviews != undefined) {
            if (i < modelview_data.cellviews.length) {
                my_cell_views = modelview_data.cellviews[i];
            }
        }            
        var new_view_id = MakeNeuronViewer(neuron_data.title, neuron_data.morphology, "modelview_graph1"); // my_cell_views);
        seg_names_[new_view_id] = neuron_data.seg_names;
        //reposition_dialog(new_view_id);
        modelview_neuron_viewers.push(new_view_id);
        hide_dialog(new_view_id);
    });
    
    // flot dialog (TODO: allow many)
    flot_dialog = "modelview_graph2"; //MakeDialog(modelview_data.short_title, true);
    $('#' + flot_dialog).parent().addClass('no-close');
    counter++;
    flot_title = AddComponent(flot_dialog, '<div style="text-align: center;" id=' + counter + '>title</div>');
    flot_fig = AddChart(flot_dialog, {contextmenu: false, doplot: false});
    try {
        plottedFlot['placeholder' + flot_fig] = $.plot($('#placeholder' + flot_fig), []);
    } catch (error) {
        // probably wasn't displayed
    }
    $('#' + flot_dialog).resize(function() {
        $('#placeholder' + flot_fig).height(max(300, $('#' + flot_dialog).height() - $('#' + flot_title).height() - 50));
        plottedFlot['placeholder' + flot_fig].draw();
    });
    hide_dialog(flot_dialog);
    
    // svg dialog (TODO: combine with flot dialog(s)?)
    svg_dialog = MakeDialog(modelview_data.short_title, true);
    $('#' + svg_dialog).parent().addClass('no-close');
    reposition_dialog(svg_dialog);
    hide_dialog(svg_dialog);

}

function show_flot_(data, title, xaxes, yaxes, hoverable, clickable) {
    if (xaxes == undefined || !xaxes.length) xaxes = undefined;
    if (yaxes == undefined || !yaxes.length) yaxes = undefined;
    if (title == undefined) title = '';
    show_dialog(flot_dialog);
    $('#' + flot_title)[0].innerHTML = title;
    var opts = {zoom: {interactive: true}, pan: {interactive: true}, xaxes: xaxes, yaxes: yaxes};
    if (hoverable || clickable) {
        opts.grid = {'hoverable': hoverable, 'clickable': clickable};
    }
    plottedFlot['placeholder' + flot_fig] = $.plot($('#placeholder' + flot_fig), data, opts);
}

function modelview_hide_all_() {
    var i, id;
    $.each(modelview_neuron_viewers, function (i, id) {
        hide_dialog(id);
    });
    hide_dialog(flot_dialog);
    hide_dialog(svg_dialog);
}

function set_colorbar(id, colorbar, orientation, lo, hi) {
    var obj = $('#below' + id);
    if (colorbar == undefined) {
        obj.css('display', 'none');
    } else {
        if (orientation != 'horizontal') {
            console.log('unsupported colorbar orientation: ' + orientation);
        } else {
            if (colorbar_types[colorbar] != 'css') {
                console.log('unsupported colorbar type: ' + colorbar_types[colorbar]);
            } else {
                obj.html('<div class="colorbar' + colorbar + '">&nbsp;</div><div><span style="float: left">' + lo + '</span><span style="float: right">' + hi + '</span></div><div style="clear: both;"></div>');
                obj.css('display', 'block');
            }
        }
    }
}

function ensure_tooltip(id) {
    if (!$('#tooltip' + id).length) {
        $('<div id="tooltip' + id + '"></div>').css({
            position: 'absolute',
            display: 'none',
            border: '1px solid #000',
            padding: '2px',
            'background-color': '#fee',
            opacity: 0.8,
            zIndex: 10000
        }).appendTo('body');
    }
}

var flot_highlighted = undefined;
var neuron_highlighted_ = undefined;
var neuron_highlighted_pt_ = undefined;

function clear_neuron_highlight_() {
    if (neuron_highlighted_ != undefined) {
        neuron_highlighted_.unhighlight(neuron_highlighted_pt_, 0);
        neuron_highlighted_ = undefined;
    }
}

seg_names_ = {};

function modelview_build_tree_(src_tree) {
    var result = [];
    var f, i, j;
    $.each(src_tree, function (i, row) {
        children = undefined;
        if (row.children != undefined) {
            children = modelview_build_tree_(row.children);
            if (children.length == 0) children = undefined;
        }
        if (row.noop == true) {
            f = undefined;
        } else {
            if (row.action != undefined) {
                f = function(do_hide_all) {
                    if (do_hide_all == undefined || do_hide_all) {
                        modelview_hide_all_();
                    }
                    $.each(row.action, function (j, action) {                    
                        if (action.kind == 'neuronviewer') {
                            var id = modelview_neuron_viewers[action.id];
                            neuron_hoverable_[id] = true;
                            show_dialog(id);
                            set_neuron_markers(id, action.markers);
                            if (action.highlight != undefined) {
                                set_neuron_highlights(id, action.highlight);
                            } else {
                                if (action.colors != undefined) {
                                    while (action.colors.length < neuron_data_[id].length) {
                                        action.colors.push('black');
                                    }
                                }
                                set_neuron_colors(id, action.colors);
                            }
                            set_colorbar(id, action.colorbar, action.colorbar_orientation, action.colorbar_low, action.colorbar_high);
                            var placeholder = $('#' + id).children('span')[0].id.replace('flotContainer', 'placeholder');
                            ensure_tooltip(id);
                            
                            $('#' + placeholder).bind("plothover", function (event, pos, item) {
                                if (item) {
                                    var tooltip_text = '';
                                    if (item.seriesIndex < neuron_data_[id].length) {
                                        var pt = neuron_data_[id][item.seriesIndex][item.dataIndex];

                                        if (seg_names_[id] != undefined) {
                                            tooltip_text += seg_names_[id][item.seriesIndex] + '<br/>';
                                        }
                                        tooltip_text += '(' + pt[0].toPrecision(4) + ', ' + pt[1].toPrecision(4) + ', ' + pt[2].toPrecision(4) + ')';
                                        if (action.colored_var != undefined && action.values != undefined) {
                                            if (item.seriesIndex < action.values.length && action.values[item.seriesIndex] != 'nan') {
                                                tooltip_text += '<br/>' + action.colored_var + ' = ' + Number(action.values[item.seriesIndex]).toPrecision(6);
                                            }
                                        }
                                        if (action.hover_text != undefined) {
                                            if (action.hover_text[item.seriesIndex] != undefined) {
                                                tooltip_text += '<br/>' + action.hover_text[item.seriesIndex];
                                            }
                                        }
                                        $('#tooltip' + id).html(tooltip_text).css({left: item.pageX + 5, top: item.pageY + 5}).show();
                                        if (flot_highlighted != undefined) {
                                            plottedFlot['placeholder' + flot_fig].unhighlight(0, flot_highlighted);
                                            flot_highlighted = undefined;
                                        }
                                        if (action.flotindices != undefined) {
                                            flot_highlighted = action.flotindices[item.seriesIndex];
                                            if (flot_highlighted != undefined && flot_highlighted >= 0) {
                                                plottedFlot['placeholder' + flot_fig].highlight(0, flot_highlighted);
                                            }
                                        }
                                    } else if (item.seriesIndex == neuron_data_[id].length) {
                                        // markers!
                                        if (action.marker_mouseovers != undefined) {
                                            tooltip_text += action.marker_mouseovers[item.dataIndex];
                                        }                                        
                                        $('#tooltip' + id).html(tooltip_text).css({left: item.pageX + 5, top: item.pageY + 5}).show();                                        
                                    }

                                } else {
                                    if (flot_highlighted != undefined) {
                                        plottedFlot['placeholder' + flot_fig].unhighlight(0, flot_highlighted);
                                        flot_highlighted = undefined;
                                    }
                                    $('#tooltip' + id).hide();
                                }
                            });
                        } else if (action.kind == 'flot') {
                            show_flot_(action.data, action.title, action.xaxes, action.yaxes, action.hoverable, action.clickable);
                            if (action.hoverable) {
                                ensure_tooltip(flot_fig);
                                $('#placeholder' + flot_fig).bind("plothover", function (event, pos, item) {
                                    if (item) {
                                        var tooltip = '(' + item.datapoint[0].toPrecision(4) + ', ' + item.datapoint[1].toPrecision(4) + ')';
                                        //        seg_names_[new_view_id] = neuron_data.seg_names;
                                        if (action.neuron_highlight_id != undefined) {
                                            clear_neuron_highlight_();
                                            var id = modelview_neuron_viewers[action.neuron_highlight_id];
                                            var placeholder = $('#' + id).children('span')[0].id.replace('flotContainer', 'placeholder');
                                            plottedFlot[placeholder].highlight(action.neuron_highlight_segs[item.dataIndex], 0);
                                            neuron_highlighted_ = plottedFlot[placeholder];
                                            neuron_highlighted_pt_ = action.neuron_highlight_segs[item.dataIndex];                                            
                                            tooltip = seg_names_[id][item.dataIndex] + '<br/>' + tooltip;
                                        }
                                        $('#tooltip' + flot_fig).html(tooltip).css({left: item.pageX + 5, top: item.pageY + 5}).show();
                                    } else {
                                        clear_neuron_highlight_();
                                        $('#tooltip' + flot_fig).hide();
                                    }
                                    //console.log(item.series);
                                });
                            }
                        } else if (action.kind == 'svg') {
                            $('#' + svg_dialog).html('<svg xmlns="http://www.w3.org/2000/svg" viewbox="' + action.viewbox + '" style="width:100%; height:100%">' + action.svg + '</svg>');
                            show_dialog(svg_dialog);
                        } else {
                            console.log('ignoring unknown action kind: ' + action.kind);
                        }
                    });
                }
            } else {
                f = function(do_hide_all) {
                    if (do_hide_all == undefined || do_hide_all) {
                        modelview_hide_all_();
                    }
                }
            }
            if (row.default_action) {
                default_action.push(f);
            }
        }
        result.push([row.text, {children: children, callback: f, noop: row.noop, mouseover: row.mouseover}]);
    });
    return result;
}
