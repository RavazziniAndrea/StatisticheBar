
//var isSseStarted=false;

var evtSource = null;

function sseCommunication(){

    if(evtSource != null)
    {
        evtSource.close()
        console.log("sse chiuso");
    }

    console.log("Dentro sse communication");

    evtSource = new EventSource("/stream");

    evtSource.onmessage = function (e) 
    {
        console.log("message: " + e.data);
    }

    evtSource.onerror = function (e) 
    {
        console.log("sse failed");
        evtSource.close();
    }
}