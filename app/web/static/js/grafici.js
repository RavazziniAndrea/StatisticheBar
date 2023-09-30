
var dataArray = [];
var primoChart = true;
var chart;


function aggiornaChart(){
    if(primoChart){
        primoChart = false;
        chart = new Chart(document.getElementById('grafico'),{
            type: 'line',
            data: {
                labels: dataArray.map(row => row.chart),
                datasets: [{
                    label: 'Acquisitions by year',
                    data: dataArray.map(row => row.value)
                }]
            }
        });
    } else {
        chart.data.labels = dataArray.map(row => row.chart)
        chart.data.datasets[0].data = dataArray.map(row => row.value)
        chart.update()
    }
}