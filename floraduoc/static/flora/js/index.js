$(document).ready(function() {

    callApi();
});   


function callApi(){

    fetch('https://api.openweathermap.org/data/2.5/weather?lat=-33.0280812&lon=-71.5547107&appid=f5c8c6819b39703cb924fe27c0490700&units=metric', {
    method: 'GET'
    }).then(res => res.json())
    .then(res => {
        console.log(res)
        var temperatura = res.main.temp
        var icon = res.weather[0].icon
        var img = "http://openweathermap.org/img/wn/"+icon+"@2x.png";


        document.getElementById("imgClima").src=img;

        document.getElementById("textClima").innerHTML = temperatura+"°";

        


    });

}



