
var tipo        = null
var tempo       = null
var grafico     = null
var old_tipo    = null
var old_tempo   = null
var old_grafico = null

function ajaxCall(){
    tipo    = document.getElementById("select-tipo").value
    tempo   = document.getElementById("select-tempo").value
    grafico = document.getElementById("select-grafico").value
    
    if(tipo == 0 || tempo == 0)
    {
        console.log("Selezionare un valore")
        console.log("TODO, uscire un notiflix?")
    }
    else if(old_tipo != tipo || old_tempo != tempo || old_grafico != grafico)
    {
        old_tipo    = tipo
        old_tempo   = tempo
        old_grafico = grafico

        $.ajax({
            type: "POST",
            url: "/graph",
            data: jQuery.param({ 
                graph: graph,
                time  : time
            }),
            complete: function(response) {
                sseCommunication() //create EventStream
            },
            error: function (status, error) {
                console.log("AJAX Error")
            }
        });
    }
    else 
    {
        console.log("Valori uguali")
    }
}