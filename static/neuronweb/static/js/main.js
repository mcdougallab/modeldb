/* Begin old JS for interaction with webserver.*/

buttonclicked = function() {
    send_to_server(1, []);
};

// everything below here should be server-communication code only
// keep it separate, so we can change it easily

// TODO: make the id unique, add some security to keep hackers
//       from just changing the userid
userid = 0

// NOTE: JSON not present in IE6/7. To support those, use json2 library

send_to_server = function(object_id, data) {
    ws.send(JSON.stringify({'object_id': object_id, 'data': data, 'userid': userid}));
};

var ws;
InitWebSocket = function(){
    ws = new WebSocket('ws://' + window.location.origin.split('//')[1] + '/socket')
    if ('WebSocket' in window) {
        ws.onopen = function() {
            console.log("i just opened the websocket!");
        };
        //message has been recieved from server
        ws.onmessage = function (evt) { 
            // update_colors(JSON.parse(evt.data));
            poll_success(evt.data);
            // thought i could just output the json..
            console.log("HI!");
            console.log(evt.data);
        };
        ws.onclose = function() { 
            console.log('Connection closed.');
            setTimeout(InitWebSocket, 1000);
        };
    } else {
        document.write('Sorry, but this browser does not support websockets.');
    }
};            

$(function() {
    InitWebSocket();
    });

