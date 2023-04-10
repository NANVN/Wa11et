const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
signUpButton.addEventListener('click',()=>{container.classList.add("right-panel-active");});
signInButton.addEventListener('click',()=>{container.classList.remove("right-panel-active");});

//function hasValue(){
////Не с цифры имя, в пароле спец символ без пробелов
//}

function validatePassword(input_1, input_2){
    if(input_1.value == input_2.value){return true;}
    document.getElementById('password2').style.border = "2px solid #ff8e7a";
    return false;}

const form = document.getElementById('qwerty');
form.addEventListener("submit", function(event) {
    event.preventDefault();
    let passwordValid = validatePassword(form.elements.password1, form.elements.password2);
    if(passwordValid){form.submit();}});

