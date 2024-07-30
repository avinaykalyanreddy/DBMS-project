function b(a) {
    if (a == 1) {
        document.getElementById("div4").style.display = "none";
        document.getElementById("div3").style.display = "block";
    } else {
        document.getElementById("div3").style.display = "none";
        document.getElementById("div4").style.display = "block";
    }
}

function togglepasswordvisibility(id){

    let pass = document.getElementById(id);

    if(pass.type === "password"){
        pass.type = "text";
    }
    else{
        pass.type = "password";
    }
}