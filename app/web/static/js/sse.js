
function sseCommunication(){
    console.log("Dentro")
    var evtSource = new EventSource("/stream");
    //var evtSource = new EventSource("{{ url_for('sse.sse') }}");

    evtSource.onmessage = function (e) {
        console.log("message: " + e.data);
        // dataArray
    }

    evtSource.onerror = function (e) {
        console.log("sse failed");
    }
}