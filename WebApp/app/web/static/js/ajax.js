
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
            url: "/grafici",
            data: jQuery.param({ 
                grafico: grafico,
                tempo  : tempo
            }),
            success: function (response) {
                console.log(response + " TODO Da qui devo tirare fuori i grafici")
            },
            complete: function(response) {
                sseCommunication()
            },
            error: function (status, error) {
                console.log("Errore AJAX, TODO usare notiflix")
            }
        });
    }
    else 
    {
        console.log("Valori uguali")
    }
}