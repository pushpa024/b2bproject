//js for contact us page
const nameValue = document.querySelector("input[name='nameInput']");
const email = document.querySelector("input[name='emailInput']");
const country = document.querySelector("input[name='countryInput']");
const phone = document.querySelector("input[name='phoneInput']");
const message = document.getElementById("floatingTextarea2");
const form = document.getElementById("form");


let phoneFocus = false;

let nameError = document.getElementById("nameError");
let phoneError = document.getElementById("phoneError");
let emailError = document.getElementById("emailError");
let countryError = document.getElementById("countryError");
let msgError = document.getElementById("msgError");

const validMail = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{3,}))$/;


const validNumber = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;

form.addEventListener("submit", (e) => {
  if (
    nameValue.value &&
    validMail.test(email.value) &&
    validNumber.test(phone.value) &&
    country.value
  ) {
    return;
  } else {
    if (nameValue.value === "" || nameValue.value === null) {
      e.preventDefault();
      nameError.innerText = "Please enter name";

    } else if (nameValue.value.length < 2) {
      e.preventDefault();
      nameError.innerText = "Please enter valid name";
    }

    if (country.value === "" || country.value === null) {
      countryError.innerText = "Please enter country name";
    } 
    else if (country.value.length < 2) {
      countryError.innerText = "Please enter valid country name";
    } 
    else if (country.value.length >= 2) {
      countryError.innerText = "";
    }
    if (email.value === "" || email.value === null) {
      emailError.innerText = "Please enter email";
    } else if (!validMail.test(email.value)) {
      emailError.innerText = "Please enter valid email";
    } else if (validMail.test(email.value)) {
      emailError.innerText = "";
    }

    // Phone
    if (phone.value === "" || phone.value === null) {
      phoneError.innerText = "Please enter number";
    } else if (!validNumber.test(phone.value)) {
      phoneError.innerText = "Please enter valid number";
    } else {
      phoneError.innerText = "";
    }

    // Message
    if (message.value === "" || message.value === null) {
      msgError.innerText = "Please enter message";
    } else if (message.value.length < 4) {
      msgError.innerText = "Please enter valid message with min 5 characters";
    }
  }
});

function nameChange() {
  if (nameValue.value.length > 2) {
    nameError.innerText = "";
  } else {
    nameError.innerText = "Please enter valid name";
  }
}

function mailChange() {
  if (validMail.test(email.value)) {
    emailError.innerText = "";
  } else {
    emailError.innerText = "Please enter valid email";
  }
}

function countryChange() {
  if (country.value.length > 2) {
    countryError.innerText = "";
  } else {
    countryError.innerText = "Please enter valid country name";
  }
}

const phoneChange = () => {
  if (validNumber.test(phone.value) && phone.value.length === 10) {
    phoneError.innerText = "";
  } else {
    phoneError.innerText = "Please enter valid number";
  }
};

function msgChange() {
  if (message.value.length > 4) {
    msgError.innerText = "";
  } else {
    msgError.innerText = "Please enter valid country name";
  }
}
    } else if (message.value.length < 4) {
      msgError.innerText = "Please enter valid message with min 5 characters";
    } else {
      msgError.innerText = "";
    }
  }
});
