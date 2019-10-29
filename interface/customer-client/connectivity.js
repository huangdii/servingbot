
import {ROSLIB} from "../ros_js_map_lib/roslib.js"
var ros = new ROSLIB.Ros();

// If there is an error on the backend, an 'error' emit will be emitted.
ros.on('error', function(error) {
  document.getElementById('connecting').style.display = 'none';
  document.getElementById('connected').style.display = 'none';
  document.getElementById('closed').style.display = 'none';
  document.getElementById('error').style.display = 'inline';
  console.log(error);
});

// Find out exactly when we made a connection.
ros.on('connection', function() {
  console.log('Connection made!');
  document.getElementById('connecting').style.display = 'none';
  document.getElementById('error').style.display = 'none';
  document.getElementById('closed').style.display = 'none';
  document.getElementById('connected').style.display = 'inline';
});

ros.on('close', function() {
  console.log('Connection closed.');
  document.getElementById('connecting').style.display = 'none';
  document.getElementById('connected').style.display = 'none';
  document.getElementById('closed').style.display = 'inline';
});

// Create a connection to the rosbridge WebSocket server.
ros.connect('ws://namlonxserver2:9090');
