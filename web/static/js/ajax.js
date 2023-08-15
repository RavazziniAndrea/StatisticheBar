function ajaxCall(){
    var grafico = document.getElementById("select-grafico").value
    var tempo = document.getElementById("select-tempo").value

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
        complete: function(reponse) {
            console.log("Adesso devo avviare sse")
            sseCommunication()
        },
        error: function (status, error) {
            console.log("Errore AJAX, TODO usare notiflix")
        }
    });
}