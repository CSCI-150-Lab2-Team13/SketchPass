
//use the html if you need to see the code in action 
function pwgeneration() {
    var use = "";
    var final = "";
    var size = Number(document.getElementById('passlength').value);
    var uc = document.getElementById('uppcase').value;
    var lc = document.getElementById('lowcase').value;
    var nc = document.getElementById('numcase').value;
    var sc = document.getElementById('symcase').value;
    var items = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]; //no " due to string syntax issue in js
    var Choice = [uc, lc, nc, sc];
    if (size > 100 || size < 1) { alert("Please enter a password length between 1 and 100 charaters");
    } 
    else {
        if (uc + lc + nc + sc == "falsefalsefalsefalse") { alert("Please choose at least a single character type to assist in password generation");
        }
        else { 
            for (var i = 0; i <= 3; i++) { if (Choice[i] == "true") use += items[i];
            }
            for (var i = 0; i < size; i++) { final += use.charAt(Math.floor(Math.random() * use.length));
            }
         $('#password-input').val(final);
        }
    }
};

function submitpw(){
    var pass = $('#password-input').val();
    if(pass.length > 100){ alert("The password created and modified is over 100 charaters in length and will be reduced to 100 characters automatcally starting from the end of the password.");
        pass = pass.substring(0,100);
    }
    else { $('#pwgenmodal').modal('hide');}
    $('#id_password').val(pass);
};

function getid(elmid){
    var jid = "#"+elmid;
    var idv = document.getElementById(elmid).value;

    if (idv == "true"){
        $(jid).val("false");
        document.getElementById(elmid).classList.remove("active");
        document.getElementById(elmid).classList.remove("btn-dark");
        document.getElementById(elmid).classList.add("btn-outline-dark");
    }
    else {
        $(jid).val("true");
        document.getElementById(elmid).classList.add("active"); 
        document.getElementById(elmid).classList.add("btn-dark");
        document.getElementById(elmid).classList.remove("btn-outline-dark");
    }

    if (jid == "#uppcase"){
        if ( idv == "true") {$(jid).text("❌ Uppercase Letters - ABC");}
        else {$(jid).text("✔ Uppercase Letters - ABC");}  
    }

    else if (jid == "#lowcase"){
        if (idv == "true") {$(jid).text("❌ Lowercase Letters - abc");}
        else {$(jid).text("✔ Lowercase Letters - abc");}  
    }

    else if (jid == "#numcase"){
        if (idv == "true") {$(jid).text("❌ Numbers - 123");}
        else {$(jid).text("✔ Numbers - 123");}  
    }

    else if (jid == "#symcase"){
        if (idv == "true") {$(jid).text("❌ Symbols - %@^");}
        else {$(jid).text("✔ Symbols - %@^");}  
    }

    else alert("Error: choice field");

};

function sliderupdate(){  
    $("#plength").text($("#passlength").val());
};
