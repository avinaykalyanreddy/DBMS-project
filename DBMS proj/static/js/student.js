function a(){
    document.getElementById('card4').style.display = 'none'
    document.getElementById('card3').style.display = 'none'
    document.getElementById("card5").style.display = 'none'
    document.getElementById('card4').style.flex = '0 0 75%'
    document.getElementById('card2').style.display = 'block'
}

function i(){
    document.getElementById('card4').style.display = 'none'
    document.getElementById('card2').style.display = 'none'
    document.getElementById("card5").style.display = 'none'
    document.getElementById('card4').style.flex = '0 0 75%'
    document.getElementById('card3').style.display = 'block'
}

function s(){

    document.getElementById('card2').style.display = 'none'
    document.getElementById('card3').style.display = 'none'
    document.getElementById("card5").style.display = 'none'
    document.getElementById('card4').style.flex = '0 0 75%'
    document.getElementById('card4').style.display = 'block'
}

function get_staff_info(name, professor, email, subject, branch, sem) {
    const card5 = document.getElementById("card5");
    card5.style.flex = '0 0 35.5%';
    card5.style.display = 'block';
    card5.innerHTML = `
        <div ">
            <h2 style="color: #e74c3c; font-weight: bolder; text-align: left;">Staff Details</h2>
            
            <h3 style="color: #21618C; font-weight: bolder; text-transform: uppercase; text-align: center;">${name}</h3>
            <p style="text-align: center; font-style: italic;">${professor}</p>
            <hr style="border: 1px solid #21618C;">
            <p style="text-align: left; font-size: 16px; margin: 10px 0;">Subject: <span style="font-weight: bold;">${subject}</span></p>
            <p style="text-align: left; font-size: 16px; margin: 10px 0;">Sem: <span style="font-weight: bold;">${sem}</span></p>
            <p style="text-align: left; font-size: 16px; margin: 10px 0;">Branch: <span style="font-weight: bold;">${branch}</span></p>
            <hr style="border: 1px solid #21618C;">
            <p style="text-align: left; font-size: 16px; margin: 10px 0;">E-mail: <a href="mailto:${email}" style="text-decoration: none; color: #2980b9;">${email}</a></p>

            <p><button style="background-color:#E74C3C;color:white;padding:7px;border:none; cursor:pointer; border-radius: 8px;" onclick="closeCard()">Close</button></p>

        </div>
    `;

    const card4 = document.getElementById("card4");
    card4.style.flex = '0 0 37.5%';
}


function closeCard() {
    document.getElementById("card5").style.display = 'none';
    document.getElementById('card4').style.flex = '0 0 75%';
}
