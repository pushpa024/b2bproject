




const min = 15;
const max = 1000;      

const fName= document.querySelector("#inputFname");
let nameError = document.querySelector(".nameFError");
window.onload = (event) => {
    console.log(fName)

  };
fName.addEventListener("input", ()=>{
    let nameInput =  document.querySelector("#inputFname").value

    if(!nameInput){
        nameError.innerText = "Please enter your name";
    }else if(nameInput.length < 3){
        nameError.innerText = "Please enter valid name"
    } else if(nameInput.length >= 3){
        nameError.innerText = ""
    }

})







const validMail =
  /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{3,}))$/;

const YourEmail = document.querySelector("#inputEmail");
let mailError = document.querySelector(".emailError");
YourEmail.addEventListener("input", () => {
    let value = document.querySelector("#inputEmail").value;
    if(!value){
        mailError.innerText = "Please enter your mail"
    }else if(!value.match(validMail)){
        mailError.innerText = "Please enter valid mail"
    }else if(value.match(validMail)){
        mailError.innerText = ""
    }
});


const cName= document.querySelector("#countryEmail");
let countryError = document.querySelector(".countryError");
window.onload = (event) => {
    console.log(cName)

  };
cName.addEventListener("input", ()=>{
    let countryInput =  document.querySelector("#countryEmail").value

    if(!countryInput){
        countryError.innerText = "Please enter your name";
    }else if(countryInput.length < 3){
        countryError.innerText = "Please enter valid name"
    } else if(countryInput.length >= 3){
        countryError.innerText = ""
    }

})

const validNumber = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
let mobileError = document.querySelector(".mobileError");
const phone = document.querySelector("#phone");
phone.addEventListener("input", () => {
    let value = document.querySelector("#phone").value;
    if(!value){
        mobileError.innerText = "Please enter your number"
    }else if(isNaN(value) === true){
        mobileError.innerText = "Please enter only numbers"
    }
    else if(!value.match(validNumber)){
        mobileError.innerText = "Please enter valid number"
    }
    else if(value.match(validNumber)){
        mobileError.innerText = ""
    }
})






;


const textArea1 = document.querySelector("#message");
let msgError = document.querySelector(".messageError");
textArea1.minLength = min;
textArea1.maxLength = max;
textArea1.addEventListener('keyup', () => {
    console.log(max)
    let value = textArea1.value;
    if(value.length < min){
    document.querySelector(".messageError").innerText = "Please Enter above 15 characters"
    }else if(value.length === max){
        document.querySelector(".messageError").innerText = "Maximum 1000 Characters only"
    } else if(min < value.length < max){
        document.querySelector(".messageError").innerText = ""
    }
});

document.getElementById("submit_form").addEventListener("submit", (e) => {
    e.preventDefault();
    if (fName.value && validMail.test(YourEmail.value) && cName.value  && validNumber.test(phone.value) && textArea1.value) {
      console.log("successfully logged in..");
      fName.value = "";
      YourEmail.value = "";
      cName.value = "";
      phone.value = "";
      textArea1.value = "";
    } else {
      if (fName.value === "" || fName.value === null) {
        // e.preventDefault();
        nameError.innerText = "Please enter first name";
      } 
      
  
      if (YourEmail.value === "" || YourEmail.value === null) {
        mailError.innerText = "Please enter  email address";
      }
      if (cName.value === "" || lName.value === null) {
        // e.preventDefault();
        countryError.innerText = "Please enter country";
      } 

     
  
      // Phone
      if (phone.value === "" || phone.value === null) {
        mobileError.innerText = "Please enter  number";
      }
  
      // Address
      if (textArea1.value === "" || textArea1.value === null) {
        msgError.innerText = "Please enter above 15 characters"
      } 
    }
  });










   
   

