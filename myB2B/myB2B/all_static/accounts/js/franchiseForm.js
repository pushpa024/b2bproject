//Initialising bootstrap tooltips
$(document).ready(function () {
  // $('[data-bs-toggle="tooltip"]').tooltip();
  $(".multi_select").select2({
    maximumSelectionLength: 30,
    allowClear: true,
    closeOnSelect: false,
    multiple: true,
    placeholder: "Select options",
  });
  $(".empty").select2($(".empty").prop("disabled", true));
  $(".single_select").select2();
});

//Initialising IntlTelInputs
// const phone_input = document.getElementById("phone");
// window.intlTelInput(phone_input, {  separateDialCode: true });

//Handling Select2Js inputs
// $(document).ready(function() {
//     $('.js-example-basic-single').select2();
//         $(".empty").select2(
//             $(".empty").prop("disabled", true)
//         );
//     $('#select-curency').hide();
//     $("#currency_changer").on('click', function(e) {
//         $('#select-curency').show();
// }
// })

// Validation
// Authorised Person NAme
const personName = document.getElementById("inputFname");
window.onload = (event) => {
  console.log("page is fully loaded");
};
personName.addEventListener("input", () => {
  let nameInput = document.getElementById("inputFname").value;

  if (!nameInput) {
    document.querySelector(".nameError").innerText = "Please Enter your name";
  } else if (nameInput.length < 3) {
    document.querySelector(".nameError").innerText = "Please Enter valid name";
  } else if (nameInput.length >= 3) {
    document.querySelector(".nameError").innerText = "";
  }
});

// Email
const validMail =
  /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{3,}))$/;

const businessEmail = document.querySelector("#inputEmail");
businessEmail.addEventListener("input", () => {
  let mailError = document.querySelector(".mailError");
  let value = document.querySelector("#inputEmail").value;
  if (!value) {
    mailError.innerText = "Please Enter Your Mail";
  } else if (!value.match(validMail)) {
    mailError.innerText = "Please Enter Valid Mail";
  } else if (value.match(validMail)) {
    mailError.innerText = "";
  }
});

// Phone
const validNumber =
  /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
const phone = document.querySelector("#phone");
phone.addEventListener("input", () => {
  let mobileError = document.querySelector(".phoneError");
  let value = document.querySelector("#phone").value;
  if (!value) {
    mobileError.innerText = "Please Enter Number";
  } else if (isNaN(value) === true) {
    mobileError.innerText = "Please Enter Only Numbers";
  } else if (!value.match(validNumber)) {
    mobileError.innerText = "Please Enter Valid Number";
  } else if (value.match(validNumber)) {
    mobileError.innerText = "";
  }
});

// Designation
const designationName = document.getElementById("inputDesignation");
designationName.addEventListener("input", () => {
  let nameInput = document.getElementById("inputDesignation").value;

  if (!nameInput) {
    document.querySelector(".designationError").innerText =
      "Please Enter your name";
  } else if (nameInput.length < 3) {
    document.querySelector(".designationError").innerText =
      "Please Enter valid name";
  } else if (nameInput.length >= 3) {
    document.querySelector(".designationError").innerText = "";
  }
});

// About your brand
const min = 10;
const max = 20;

const textArea1 = document.getElementById("about-brand");
textArea1.minLength = min;
textArea1.maxLength = max;
textArea1.addEventListener("keyup", () => {
  let value = textArea1.value;
  if (value.length < min) {
    document.querySelector(".about-brand-error").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".about-brand-error").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".about-brand-error").innerText = "";
  }
});

// Mention all products/services your brand provides
const textArea2 = document.getElementById("product-services");
textArea2.minLength = min;
textArea2.maxLength = max;
textArea2.addEventListener("keyup", () => {
  let value = textArea2.value;
  if (value.length < min) {
    document.querySelector(".product-services-error").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".product-services-error").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".product-services-error").innerText = "";
  }
});

// What is your expectation from the user who takes up this opportunity
const textArea3 = document.getElementById("user-expectations");
textArea3.minLength = min;
textArea3.maxLength = max;
textArea3.addEventListener("keyup", () => {
  let value = textArea3.value;
  if (value.length < min) {
    document.querySelector(".user-expectations-error").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".user-expectations-error").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".user-expectations-error").innerText = "";
  }
});

// What kind of support can the sales partner expect from you?
const textArea4 = document.getElementById("user-support");
textArea4.minLength = min;
textArea4.maxLength = max;
textArea4.addEventListener("keyup", () => {
  let value = textArea4.value;
  if (value.length < min) {
    document.querySelector(".user-support-error").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".user-support-error").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".user-support-error").innerText = "";
  }
});

// What is the procedure to become your Sales Partner?
const textArea5 = document.getElementById("partner-procedure");
textArea5.minLength = min;
textArea5.maxLength = max;
textArea5.addEventListener("keyup", () => {
  let value = textArea5.value;
  if (value.length < min) {
    document.querySelector(".partner-procedure-error").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".partner-procedure-error").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".partner-procedure-error").innerText = "";
  }
});

// Format Name
const formatName = document.getElementById("format-name");
formatName.addEventListener("input", () => {
  let nameInput = document.getElementById("format-name").value;

  if (!nameInput) {
    document.querySelector(".format-name-error").innerText =
      "Please Enter your name";
  } else if (nameInput.length < 3) {
    document.querySelector(".format-name-error").innerText =
      "Please Enter valid name";
  } else if (nameInput.length >= 3) {
    document.querySelector(".format-name-error").innerText = "";
  }
});

// Mention details of Royalty charged or Commission paid
const textArea6 = document.getElementById("Royalty-charges");
textArea6.minLength = min;
textArea6.maxLength = max;
textArea6.addEventListener("keyup", () => {
  let value = textArea6.value;
  if (value.length < min) {
    document.querySelector(".Royalty-charges-error").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".Royalty-charges-error").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".Royalty-charges-error").innerText = "";
  }
});

// Add Brand logo
const allowedImages = /(\.jpeg|\.png|\.jpg)$/i;

function previewLogo(event) {
  let fileImages = document.getElementById("brand_logo");
  document.getElementById("brand_logo-preview").innerHTML = "";

  if (fileImages.files[0].size > 300000) {
    document.getElementById("brand_logo-preview").innerHTML =
      "<p>Please select below 300KB</p>";
  } else if (!allowedImages.exec(fileImages.files[0].name)) {
    document.getElementById("brand_logo-preview").innerHTML =
      "<p>Please select jpeg/png/jpg files only</p>";
  } else {
    document.getElementById("brand_logo-preview").innerHTML = "";
    let url = URL.createObjectURL(event.target.files[0]);
    if (allowedImages.exec(fileImages.files[0].name)) {
      document.getElementById("brand_logo-preview").innerHTML +=
        '<img src="' + url + '">';
    }
  }
}

brand_logo.addEventListener("change", previewLogo);

// Add Photos of your Facility / Stores
function previewFacilityPhotos(event) {
  let urls = [];
  let fileImages = document.getElementById("facility_photos");
  document.getElementById("facility_photos-preview").innerHTML = "";

  if (fileImages.files[0].size > 300000) {
    document.getElementById("facility_photos-preview").innerHTML =
      "<p>Please select below 300KB</p>";
    urls.length = "";
  } else if (!allowedImages.exec(fileImages.files[0].name)) {
    document.getElementById("facility_photos-preview").innerHTML =
      "<p>Please select jpeg/png/jpg files only</p>";
    urls.length = "";
  } else if (fileImages.files.length > 3) {
    document.getElementById("facility_photos-preview").innerHTML =
      "<p>Please select only 3 files</p>";
    urls.length = "";
  } else {
    document.getElementById("facility_photos-preview").innerHTML = "";
    urls.length = "";
    for (let i = 0; i < 3; i++) {
      let url = URL.createObjectURL(event.target.files[i]);
      urls.push(url);
      if (allowedImages.exec(fileImages.files[i].name)) {
        document.getElementById("facility_photos-preview").innerHTML +=
          '<img src="' + urls[i] + '">';
      } else if (!allowedImages.exec(fileImages.files[i].name)) {
        urls.length = "";
        document.getElementById("facility_photos-preview").innerHTML =
          "<p>Please select jpeg/png/jpg files only</p>";
        Img.style.display = "none";
      }
    }
  }
}
facility_photos.addEventListener("change", previewFacilityPhotos);

// Add Brochures & Document
const allowedDoc = /(\.doc|\.docx|\.pdf|\..xlsx|\.xls|\.jpeg|\.png|\.jpg)$/i;
function previewBrochure_doc(event) {
  let urls = [];
  let fileImages = document.getElementById("brochure_doc");
  document.getElementById("brochure_doc-preview").innerHTML = "";

  if (fileImages.files[0].size > 1000000) {
    document.getElementById("brochure_doc-preview").innerHTML =
      "<p>Please select below 1MB</p>";
    urls.length = "";
  } else if (!allowedDoc.exec(fileImages.files[0].name)) {
    document.getElementById("brochure_doc-preview").innerHTML =
      "<p>Please select jpeg/png/jpg files only</p>";
    urls.length = "";
  } else if (fileImages.files.length > 3) {
    document.getElementById("brochure_doc-preview").innerHTML =
      "<p>Please select only 3 files</p>";
    urls.length = "";
  } else {
    document.getElementById("brochure_doc-preview").innerHTML = "";
    urls.length = "";
    for (let i = 0; i < 3; i++) {
      let url = URL.createObjectURL(event.target.files[i]);
      urls.push(url);
      if (allowedDoc.exec(fileImages.files[i].name)) {
        document.getElementById("brochure_doc-preview").innerHTML +=
          '<img src="' +
          urls[i] +
          '" + alt="' +
          fileImages.files[i].name +
          '">';
      } else if (!allowedDoc.exec(fileImages.files[i].name)) {
        urls.length = "";
        document.getElementById("brochure_doc-preview").innerHTML =
          "<p>Please select jpeg/png/jpg files only</p>";
        Img.style.display = "none";
      }
    }
  }
}
brochure_doc.addEventListener("change", previewBrochure_doc);

// Attach Proof of Business
function previewBusiness_proof(event) {
  let urls = [];
  let fileImages = document.getElementById("business_proof");
  document.getElementById("business_proof-preview").innerHTML = "";

  if (fileImages.files[0].size > 1000000) {
    document.getElementById("business_proof-preview").innerHTML =
      "<p>Please select below 1MB</p>";
    urls.length = "";
  } else if (!allowedDoc.exec(fileImages.files[0].name)) {
    document.getElementById("business_proof-preview").innerHTML =
      "<p>Please select jpeg/png/jpg files only</p>";
    urls.length = "";
  } else if (fileImages.files.length > 3) {
    document.getElementById("business_proof-brochure_doc-preview").innerHTML =
      "<p>Please select only 3 files</p>";
    urls.length = "";
  } else {
    document.getElementById("business_proof-preview").innerHTML = "";
    urls.length = "";
    for (let i = 0; i < 3; i++) {
      let url = URL.createObjectURL(event.target.files[i]);
      urls.push(url);
      if (allowedDoc.exec(fileImages.files[i].name)) {
        document.getElementById("business_proof-preview").innerHTML +=
          '<img src="' +
          urls[i] +
          '" + alt="' +
          fileImages.files[i].name +
          '">';
      } else if (!allowedDoc.exec(fileImages.files[i].name)) {
        urls.length = "";
        document.getElementById("business_proof-preview").innerHTML =
          "<p>Please select jpeg/png/jpg files only</p>";
        Img.style.display = "none";
      }
    }
  }
}
business_proof.addEventListener("change", previewBusiness_proof);
