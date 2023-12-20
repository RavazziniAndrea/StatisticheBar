
//var isSseStarted=false;

var evtSource = null;

var newGraph = false;

function sseCommunication(){

    if(evtSource != null)
    {
        evtSource.close()
        console.log("sse chiuso");
    }

    console.log("Dentro sse communication");
    newGraph = true

    evtSource = new EventSource("/stream");


    var i = 0;

    evtSource.onmessage = function (e) 
    {
        const message = e.data;
        // console.log("message: " + message);
        const vals = message.split('#');
        var qty  = vals[1];
        var type = vals[2];
        var date = vals[3];
        var time = vals[4].split('.')[0];

        dataArray.push(new Record(qty, type, date, time));
        aggiornaChart();

        // console.log("qty: " + qty + "type: " + type + "date: " + date + "time: " + time)

    }

    evtSource.onerror = function (e) 
    {
        console.log("sse failed");
        evtSource.close();
    }
}