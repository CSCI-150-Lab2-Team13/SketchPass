//use the html if you need to see the code in action
function pwgeneration() {
    var use = "";
    var final = "";
    var size = Number(document.getElementById('strlength').value);
    var uc = document.getElementById('uppcase').checked;
    var lc = document.getElementById('lowcase').checked;
    var nc = document.getElementById('numcase').checked;
    var sc = document.getElementById('symcase').checked;
    var items = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]; //no " due to string syntax issue in js
    var Choice = [uc, lc, nc, sc];
    if (size > 100 || size < 1) { alert("Please enter a password length between 1 and 100 charaters");
    } 
    else {
        if (uc + lc + nc + sc == 0) { alert("Please choose at least a single character type to assist in password generation");
        }
        else { 
            for (var i = 0; i <= 3; i++) { if (Choice[i] == 1) use += items[i];
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
    $('#id_password').val(pass);
};