function time(){
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let session = 'AM';

    if(hh>=12){
        session='PM'
    }
    hh = (hh<10)? "0" + hh : hh;
    mm = (mm<10)? "0" + mm : mm;
    let display = `${hh}<br> ${mm}`
    document.getElementById("clock").innerHTML = display;
    let sess = `${session}`
    document.getElementById("session").innerHTML = sess
   
    setTimeout( function(){
        time()},1000
    )    
}time()

let back = document.getElementById("back")
let counter = 0
let int = setInterval(img, 3000)
function img(){
    counter++
    if(counter == 1){
        back.style.background = "url(/static/images/back1.jpg)"
        back.style.backgroundPosition = "center center"
        back.style.backgroundSize = "cover";
        back.style.backgroundRepeat = "no-repeat"
    }
    else if(counter == 2){
        back.style.background = "url(/static/images/back2.jpg)"
        back.style.backgroundPosition = "center center"
        back.style.backgroundSize = "cover";
        back.style.backgroundRepeat = "no-repeat"
    }
    else if(counter == 3){
        back.style.background = "url(/static/images/back3.jpg)"
        back.style.backgroundPosition = "center center"
        back.style.backgroundSize = "cover";
        back.style.backgroundRepeat = "no-repeat"
    }
    else if(counter == 4){
        back.style.background = "url(/static/images/back4.jpg)"
        back.style.backgroundPosition = "center center"
        back.style.backgroundSize = "cover";
        back.style.backgroundRepeat = "no-repeat"
        counter = 0
    }
}img()


var icon = document.querySelectorAll('img')
let text = document.getElementById('text')
let menu = document.getElementById('menu')

icon[1].addEventListener('click',  clk)
icon[2].addEventListener('click', insta)
icon[3].addEventListener('click', whats)
menu.addEventListener('click', menU)
function clk(){
    text.innerHTML= "Please, click on the indicated icon"
    text.style.display = "block"
}

function insta(){
    text.innerHTML = "come on! you can see that big a** arrow right??"
    text.style.display = "block"
}
function whats(){
    text.innerHTML = "Are you kidding me?!!!"
    text.style.display = "block"
}
function menU(){
    text.innerHTML = "Please, click on the indicated icon and also try out the edit button"
    text.style.display = "block"
}
