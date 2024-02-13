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

// onchange

function ShowHideDiv() {
  var interested = document.getElementById("interested");
  var dropdown3 = document.getElementById("dropdown3");
  var dropdown1 = document.getElementById("dropdown1");
  var dropdown2 = document.getElementById("dropdown2");
  var dropdown4 = document.getElementById("dropdown4");
  var commonInput = document.getElementById("commonInput");

  dropdown3.style.display = interested.value == "loan" ? "block" : "none";
  dropdown1.style.display = interested.value == "fullSale" ? "block" : "none";
  dropdown2.style.display =
    interested.value == "partialBusiness" ? "block" : "none";
  dropdown4.style.display =
    interested.value == "sellingLeasing" ? "block" : "none";
  commonInput.style.display =
    interested.value == "sellingLeasing" ? "none" : "block";
}

// onchange

const min = 40;
const max = 1000;

const fname = document.querySelector("#inputFname");
window.onload = (event) => {
  console.log(fname);
  
};
fname.addEventListener("input", () => {
  let nameInput = document.querySelector("#inputFname").value;

  if (!nameInput) {
    document.querySelector(".nameFError").innerText = "Please Enter your name";
  } else if (nameInput.length < 3) {
    document.querySelector(".nameFError").innerText = "Please Enter valid name";
  } else if (nameInput.length >= 3) {
    document.querySelector(".nameFError").innerText = "";
  }
});
const cname = document.querySelector("#companyName");
window.onload = (event) => {
  console.log(fname);
};
cname.addEventListener("input", () => {
  let companyInput = document.querySelector("#companyName").value;

  if (!companyInput) {
    document.querySelector(".companyNameError").innerText =
      "Please Enter your company name";
  } else if (companyInput.length < 3) {
    document.querySelector(".companyNameError").innerText =
      "Please Enter valid company name";
  } else if (companyInput.length >= 3) {
    document.querySelector(".companyNameError").innerText = "";
  }
});

const validNumber =
  /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
const phone = document.querySelector("#phone");
phone.addEventListener("input", () => {
  let phoneError = document.querySelector(".phoneError");
  let value = document.querySelector("#phone").value;
  if (!value) {
    phoneError.innerText = "Please Enter Number";
  } else if (isNaN(value) === true) {
    phoneError.innerText = "Please Enter Only Numbers";
  } else if (!value.match(validNumber)) {
    phoneError.innerText = "Please Enter Valid Number";
  } else if (value.match(validNumber)) {
    phoneError.innerText = "";
  }
});

const validMail =
  /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{3,}))$/;

const YourEmail = document.querySelector("#inputEmail");
YourEmail.addEventListener("input", () => {
  let mailError = document.querySelector(".mailError");
  let value = document.querySelector("#inputEmail").value;
  if (!value) {
    mailError.innerText = "Please Enter Your EMail ID";
  } else if (!value.match(validMail)) {
    mailError.innerText = "Please Enter Valid EMail";
  } else if (value.match(validMail)) {
    mailError.innerText = "";
  }
});

const textArea1 = document.getElementById("singleLine");
textArea1.minLength = min;
textArea1.maxLength = max;
textArea1.addEventListener("keyup", () => {
  console.log(max);
  let value = textArea1.value;
  if (value.length < min) {
    document.querySelector(".singleLineError").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".singleLineError").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".singleLineError").innerText = "";
  }
});

const textArea2 = document.getElementById("highlights");
textArea2.minLength = min;
textArea2.maxLength = max;
textArea2.addEventListener("keyup", () => {
  let value = textArea2.value;
  if (value.length < min) {
    document.querySelector(".highlightsError").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".highlightsError").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".highlightsError").innerText = "";
  }
});

const textArea3 = document.getElementById("ListAll");
textArea3.minLength = min;
textArea3.maxLength = max;
textArea3.addEventListener("keyup", () => {
  let value = textArea3.value;
  if (value.length < min) {
    document.querySelector(".ListAllError").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".ListAllError").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".ListAllError").innerText = "";
  }
});

const textArea4 = document.getElementById("facility");
textArea4.minLength = min;
textArea4.maxLength = max;
textArea4.addEventListener("keyup", () => {
  let value = textArea4.value;
  if (value.length < min) {
    document.querySelector(".facilityError").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".facilityError").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".facilityError").innerText = "";
  }
});

const textArea5 = document.getElementById("tangible");
textArea5.minLength = min;
textArea5.maxLength = max;
textArea5.addEventListener("keyup", () => {
  let value = textArea5.value;
  if (value.length < min) {
    document.querySelector(".tangibleError").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".tangibleError").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".tangibleError").innerText = "";
  }
});

const textArea6 = document.getElementById("reason");
textArea6.minLength = min;
textArea6.maxLength = max;
textArea6.addEventListener("keyup", () => {
  let value = textArea6.value;
  if (value.length < min) {
    document.querySelector(".reasonError").innerText =
      "Please Enter above 40 characters";
  } else if (value.length === max) {
    document.querySelector(".reasonError").innerText =
      "Maximum 1000 Characters only";
  } else if (min < value.length < max) {
    document.querySelector(".reasonError").innerText = "";
  }
});

// Add Brand logo
// const allowedImages = /(\.jpeg|\.png|\.jpg)$/i;


// Add Photos of your Facility / Stores
function previewFacilityPhotos(event) {
  print("inside photos")
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
// const allowedDoc = /(\.doc|\.docx|\.pdf|\..xlsx|\.xls|\.jpeg|\.png|\.jpg)$/i;
function previewBrochure_doc1(event) {
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
brochure_doc.addEventListener("change", previewBrochure_doc1);

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
    document.getElementById("business_proof-brochure_doc-preview").innerHTML =
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
