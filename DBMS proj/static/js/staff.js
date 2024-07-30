




var i = 0

function a(){
    if (i%2 == 0){
     document.getElementById("card2").style.display  = "block"
     document.getElementById("card2").style.flex  = "0 0 75%"
     i = 1;
    }
    else{
        document.getElementById("card2").style.display  = "none"
        document.getElementById("card3").style.display = "none"
        i=0;
    }

    
}

