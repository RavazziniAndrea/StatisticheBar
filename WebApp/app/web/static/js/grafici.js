
var dataArray = []
var chart = null
var type
var time
var graph

function aggiornaChart(){
    var record = dataArray.pop()

    //labels --> data ora
    //data --> per ogni tipo alcolico
        //labels   --> tipo alc
        //datasets --> 
        //  label    --> legenda per ogni dataset
        //  data     --> qta
    if(newGraph && chart != null){
        newGraph = false;
        chart.destroy();
        chart = null;
    }

    if(chart == null){
        type  = document.getElementById("select-tipo").value
        time  = document.getElementById("select-tempo").value
        graph = document.getElementById("select-grafico").value

        chart = new Chart(document.getElementById('grafico'),
        {
            type: (graph == 0) ? "line" : "pie",
            data: {
                labels: [],
                data: []
            }
        });
    }

    const date = record.date//getFormattedDate(record.date, time)

    if(!chart.data.labels.includes(date)){

        chart.data.labels.push(date)
        
        chart.data.datasets.forEach(element => {
            element.data.push(0) //elemento nuovo da cui si partirà a sommare
        })

    }

    var ix = chart.data.datasets.findIndex((element) => {
        return element.label == record.type
    })
    // console.log("ix: "+ix)
    
    if(ix < 0){
        var mapInDataset = new Map()
        var arrData = []
     
        chart.data.labels.forEach(() => {
            arrData.push(0)
        })
        
        mapInDataset.set("label", record.type)
        mapInDataset.set("data", arrData)  
        
        var color = getRandomColor();
        var ds = {
            label: record.type,
            fillColor: color,
            strokeColor: color,
            highlightFill: color,
            highlightStroke: color,
            backgroundColor: color,
            borderColor: ((graph == 0) ? color : "#000000"),
            data: arrData
        }

        chart.data.datasets.push(ds)

        ix = chart.data.datasets.length - 1
    }

    const numLabels = chart.data.labels.length
    const qtyOld = chart.data.datasets[ix].data[numLabels -1]

    chart.data.datasets[ix].data[numLabels -1] = parseInt(qtyOld) + parseInt(record.qty)

    // console.log(chart.data)
    chart.update()
}


function getFormattedDate(date, time){
    
    const splitted = date.split("-")
    switch(time){
        default:
        case 1:  return date;
        case 2:  return splitted[0]+"-"+splitted[1];
        case 3:  return splitted[0];
        case 4:  return "";
    }
}


function getRandomColor(){
    return "#"+Math.floor(Math.random()*16777215).toString(16);
}