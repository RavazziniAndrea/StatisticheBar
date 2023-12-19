
var dataArray = []
var dataInChart= []
var dataTest = [1,2,3,4,5,6]
var chart = null
var i=0

var type
var time
var graph


var types = []



function aggiornaChart(){
    var record = dataArray.pop()

    //labels --> data ora
    //data --> per ogni tipo alcolico
        //labels   --> tipo alc
        //datasets --> 
        //  label    --> legenda per ogni dataset
        //  data     --> qta

    if(chart == null){
        //TODO beccare il tipo di grafico

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

    // console.log(timeIntervals)
    // console.log(chart.data.labels.includes(record.date))
    
    if(!chart.data.labels.includes(record.date)){

        chart.data.labels.push(record.date)
        
        chart.data.datasets.forEach(element => {
            element.data.push(0) //elemento nuovo da cui si partirà a sommare
        })

    }
    // console.log(chart.data.labels)


    // var ix = chart.data.labels.indexOf(record.date)
    var ix = chart.data.datasets.findIndex((element) => {
        return element.label == record.type
    })
    console.log("ix: "+ix)
    
    if(ix < 0){
        console.log("DENOTRS")
        var mapInDataset = new Map()
        var arrData = []
     
        chart.data.labels.forEach(() => {
            arrData.push(0)
        })
        
        mapInDataset.set("label", record.type)
        mapInDataset.set("data", arrData)  
        
        var ds = {
            label: record.type,
            fillColor: "rgba(187,205,151,0.5)",
            strokeColor: "rgba(187,205,151,0.8)",
            highlightFill: "rgba(187,205,151,0.75)",
            highlightStroke: "rgba(187,205,151,1)",
            data: arrData
        }

        chart.data.datasets.push(ds)

        ix = chart.data.datasets.length - 1
    }

    var numLabels = chart.data.labels.length
    var qtyOld = chart.data.datasets[ix].data[numLabels -1]

    chart.data.datasets[ix].data[numLabels -1] = parseInt(qtyOld) + parseInt(record.qty)
    // console.log(chart.data.datasets[ix].get("data"))
    // console.log(parseInt(qtyOld)+" + "+ parseInt(record.qty))

    console.log(chart.data)
    chart.update()


    // var qty = types.get(record.type)
    // if(!qty){ //nuovo tipo trovato
    //     qty=0

    //     // chart.data.labels.push("ASSE x") //<--- ASSE X, CI ANTRÀ IL TEMPO
        // var mapInDataset = new Map()
        // var arrData = []
     
        // chart.data.labels.forEach(() => {
        //     arrData.push(0)
        // })
        
        // mapInDataset.set("label", record.type)
        // mapInDataset.set("data", arrData)  
        
        // chart.data.datasets.push(mapInDataset) 
        // console.log(chart.data.datasets)
    // }
    

    // var qty = types.get(record.type)
    // if(!qty){ //nuovo tipo trovato
    //     qty=0
    //     // chart.data.labels.push("ASSE x") //<--- ASSE X, CI ANTRÀ IL TEMPO
    //     var mapInDataset = new Map()
    //     var arrData = []
    //     mapInDataset.set("label", record.type)
    //     mapInDataset.set("data", arrData)
    //     chart.data.datasets.push(mapInDataset)
    // }
    
    // var qtyTot = parseInt(qty)+parseInt(record.qty);
    // types.set(record.type, qtyTot)

    // var ix = chart.data.datasets.findIndex((element) => {
    //     return element.get("label") == record.type
    // })

    // console.log(chart.data.datasets[ix].get("data"))
    // console.log(chart.data.datasets.length + "::" +ix + "::"+qtyTot+ "::"+chart.data.labels.length)

    // //TODO non devo mettere la qtyTot perchè se no crea array con qta progressive
    // chart.data.datasets[ix].get("data").push(qtyTot) 
    // chart.update()


}


// function aggiornaChart(){
//     if(primoChart){
//         // primoChart = false;
//         chart = new Chart(document.getElementById('grafico'),{
//             type: 'line',
            // data: {
            //     labels: dataArray.map(row => row.chart),
            //     datasets: [{
            //         label: 'Acquisitions by year',
            //         data: dataArray.pop
            //     }]
            // }
//         });
//     }
//      else {
//         chart.data.labels = dataArray.map(row => row.chart)
//         chart.data.datasets[0].data = dataArray.pop
//         chart.update()
//     }
// }