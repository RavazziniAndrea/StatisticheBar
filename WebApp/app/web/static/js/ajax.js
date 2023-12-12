
var grafico     = null;
var tempo       = null;
var old_grafico = null;
var old_tempo   = null;

function ajaxCall(){
    grafico = document.getElementById("select-grafico").value
    tempo   = document.getElementById("select-tempo").value
    
    if(old_grafico != grafico || old_tempo != tempo)
    {
        old_grafico = grafico;
        old_tempo   = tempo;

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