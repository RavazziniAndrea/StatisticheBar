
var dataArray = [];
var primoChart = true;
var chart;
var i=0;

function aggiornaChart(){
    console.log("ENTRA?")
    if(i++<10){
        if(primoChart){
            primoChart = false;
            chart = new Chart(document.getElementById('grafico'),{
                type: 'line',
                data: {
                    labels: dataArray.map(row => row.chart),
                    datasets: [{
						data : [ 186, 205, 1321, 1516, 2107, 2191, 3133, 3221, 4783, 5478 ],
                        label : "America",
                        borderColor : "#3cba9f",
                        fill : false
                    }]
                }
            });
        }
         else {
            chart.data.labels = dataArray.map(row => row.chart)
            chart.data.datasets[0].data = [i, i+10]
            chart.update()
        }
    }
}


// function aggiornaChart(){
//     if(primoChart){
//         // primoChart = false;
//         chart = new Chart(document.getElementById('grafico'),{
//             type: 'line',
//             data: {
//                 labels: dataArray.map(row => row.chart),
//                 datasets: [{
//                     label: 'Acquisitions by year',
//                     data: dataArray.pop
//                 }]
//             }
//         });
//     }
//      else {
//         chart.data.labels = dataArray.map(row => row.chart)
//         chart.data.datasets[0].data = dataArray.pop
//         chart.update()
//     }
// }