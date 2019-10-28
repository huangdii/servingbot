var SERVERNAME="namlonxserver2"
function requestContent(foodNum) {
    var xmlhttp = new XMLHttpRequest();
    var url = `http://${SERVERNAME}:5000/api/order/food/${foodNum}`;
    var content = url
    xmlhttp.onreadystatechange = function () {
        console.log("order success")
        document.getElementById("statustext").innerHTML = "<p>"+this.responseText+"</p>";
    };
    xmlhttp.open("GET", content, true);
    xmlhttp.send();
}

function orderReceived() {
    var xmlhttp = new XMLHttpRequest();
    var url = `http://${SERVERNAME}:5000/api/received/${foodNum}`;
    var content = url
    xmlhttp.onreadystatechange = function () {
        console.log("received")
        document.getElementById("statustext").innerHTML = "<p>"+this.responseText+"</p>";
    };
    xmlhttp.open("GET", content, true);
    xmlhttp.send();
}

function resetOrder(){
    var xmlhttp = new XMLHttpRequest();
    var url = `http://${SERVERNAME}:5000/api/reset/order/`;
    xmlhttp.onreadystatechange = function(){
        console.log("reset success");
        document.getElementById("statustext").innerHTML = "<p>"+this.responseText+"</p>"
    };
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
}
