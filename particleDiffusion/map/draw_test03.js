// Note: You have to change the host var 
// if your client runs on a different machine than the websocket server
//var host = "ws://localhost:9090/";



function setup(){
    //var socket = new WebSocket(host);
    //var host = "http://localhost:9090/get";
    var host = "ws://localhost:9090/cur";
    var webSocket = null;
    var out = document.getElementById("debug");
    var data = null;
    out.value + "ccccc";

    if (webSocket == null) {
        // WebSocket の初期化
        webSocket = new WebSocket(host);
        // イベントハンドラの設定
        webSocket.onopen = function() { 
            webSocket.send("Hello, world");
        };
        webSocket.onmessage = function (evt) { 
            alert(evt.data);
        };
   //     webSocket.onmessage = onMessage;
   //     webSocket.onclose = onClose;
   //     webSocket.onerror = onError;
    }
    // 接続イベント
    /*
    function onOpen(event) {
        //chat("接続しました。");
        websocket.send("hello world");
    }
*/

/*
    $.getJSON(host, {
        //format: 'json',
        //      , timeout: 1000

    }, function(data){
        console.log(data);
    });        
*/

/*
    $.ajax({
        url: host,
        type: "GET",
        datatype: 'json',
        //      , timeout: 1000
        successs: function(json){
            var len = json.length;
            console.log(json);
        },
        
    });
*/
/*
    }).done(function(data, status, xhr) {
        console.log(data);
    }).fail(function(xhr, status, error) {

        console.log(xhr);
        console.log(status);
        console.log(error);
    });
*/
    var test = "vvvvvv";
    console.log(test);



    
/*
    if (webSocket == null) {
        // WebSocket の初期化
        //webSocket = new WebSocket(uri);
        webSocket = new WebSocket(host);
        // イベントハンドラの設定
        webSocket.onopen = onOpen;
        webSocket.onmessage = onMessage;
        //webSocket.onclose = onClose;
        webSocket.onerror = onError;
        //webSocket.send("aaaaa");
    }
*/
    // 接続イベント
    function onOpen(event) {
        chat("接続しました。");
        console.log("socket status: " + webSocket.readyState);   
    }

    // メッセージ受信イベント
    function onMessage(event) {
        if (event && event.data) {
            //chat(event.data);
            console.log("socket status: " + webSocket.readyState);   
        }
        console.log("socket status: " + webSocket.readyState);   
    }

    // エラーイベント
    function onError(event) {
        //chat("エラーが発生しました。");
    }


    /*
      var $txt = $("#data");
      var $btnSend = $("#sendtext");
      $txt.focus();
    */
};


// event handlers for UI
/*
  $btnSend.on('click',function(){
  var text = $txt.val();
  if(text == ""){
  return;
  }
  socket.send(text);
  $txt.val("");    
  });

  $txt.keypress(function(evt){
  if(evt.which == 13){
  $btnSend.click();
  }
  });
*/
/*
// event handlers for websocket
if(socket){

socket.onopen = function(){
//alert("connection opened....");
}

socket.onmessage = function(msg){
showServerResponse(msg.data);
}

socket.onclose = function(){
//alert("connection closed....");
showServerResponse("The connection has been closed.");
}

}else{
console.log("invalid socket");
}
*/
/*
function showServerResponse(txt){
    var p = document.createElement('p');
    p.innerHTML = txt;
    document.getElementById('output').appendChild(p); 
}
*/
