$(document).ready(function() {
    var name = "drop1"
    var query = decodeURIComponent(
    (new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null

    $(" tr ").each(function(){
        var ciudad = $(this).attr('id')
        if(query !== ciudad && query!=null && query!=="") {
            document.getElementById(ciudad).remove();
        }
    });
    var ciudades = document.getElementById("drop1");
    [].slice.call(ciudades.options)
    .map(function(a){
    if(this[a.innerText]){
    ciudades.removeChild(a);
    } else {
    this[a.innerText]=1;
    }
    },{});

});