
var io = require('socket.io-client');
var socket = io.connect("http://localhost:9090/ws");
socket.on('connect', function() {
    console.log("a");
    //socket.emit('test', {'vehicleId': 1, 'pos': [0,1]});
    socket.send('test');
    //var answer = confirm(data.message);
    //fn(answer);
});
