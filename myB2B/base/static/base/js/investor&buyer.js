const min = 40;
const max = 1000;






const fname= document.querySelector("#inputFname");
window.onload = (event) => {
    console.log(fname)

  };
fname.addEventListener("input", ()=>{
    let nameInput =  document.querySelector("#inputFname").value

    if(!nameInput){
        document.querySelector(".nameFError").innerText = "Please Enter your name";
    }else if(nameInput.length < 3){
        document.querySelector(".nameFError").innerText = "Please Enter valid name"
    } else if(nameInput.length >= 3){
        document.querySelector(".nameFError").innerText = ""
    }

})
const lName = document.querySelector("#inputLname");
lName.addEventListener("input", ()=>{
    let nameInput = document.querySelector("#inputLname").value

    if(!nameInput){
        document.querySelector(".nameLError").innerText = "Please Enter your name";
    }else if(nameInput.length < 3){
        document.querySelector(".nameLError").innerText = "Please Enter valid name"
    } else if(nameInput.length >= 3){
        document.querySelector(".nameLError").innerText = ""
    }

})

const validMail =
  /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{3,}))$/;

const YourEmail = document.querySelector("#inputEmail");
YourEmail.addEventListener("input", () => {
    let mailError = document.querySelector(".emailError")
    let value = document.querySelector("#inputEmail").value;
    if(!value){
        mailError.innerText = "Please Enter Your Mail"
    }else if(!value.match(validMail)){
        mailError.innerText = "Please Enter Valid Mail"
    }else if(value.match(validMail)){
        mailError.innerText = ""
    }
});



const validNumber = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;


const phone = document.querySelector("#phone");
phone.addEventListener("input", () => {
    let mobileError = document.querySelector(".mobileError")
    let value = document.querySelector("#phone").value;
    if(!value){
        mobileError.innerText = "Please Enter Number"
    }else if(isNaN(value) === true){
        mobileError.innerText = "Please Enter Only Numbers"
    }
    else if(!value.match(validNumber)){
        mobileError.innerText = "Please Enter Valid Number"
    }
    else if(value.match(validNumber)){
        mobileError.innerText = ""
    }
})



const textArea1 = document.getElementById('factors');
textArea1.minLength = min;
textArea1.maxLength = max;
textArea1.addEventListener('keyup', () => {
    console.log(max)
    let value = textArea1.value;
    if(value.length < min){
    document.querySelector(".factorsError").innerText = "Please Enter above 40 characters"
    }else if(value.length === max){
        document.querySelector(".factorsError").innerText = "Maximum 1000 Characters only"
    } else if(min < value.length < max){
        document.querySelector(".factorsError").innerText = ""
    }
});


const textArea2 = document.getElementById('company_info');
textArea2.minLength = min;
textArea2.maxLength = max;
textArea2.addEventListener('keyup', () => {
    let value = textArea2.value;
    if(value.length < min){
        document.querySelector(".companyError").innerText = "Please Enter above 40 characters"
        }else if(value.length === max){
            document.querySelector(".companyError").innerText = "Maximum 1000 Characters only"
        } 
        else if(min < value.length < max){
            document.querySelector(".companyError").innerText = ""
        }   
});


// Image Validation and Preview
let urls1 = []
let fileImages1;
const allowedImages1 = 
/(\.jpeg|\.png|\.jpg)$/i;
function previewMultiple1(event){
    fileImages1 = document.getElementById("business_proof");
    document.getElementById("preview1").innerHTML = "";
    
    
    if(fileImages1.files[0].size > 300000){
        document.getElementById("preview1").innerHTML = "<p>Please select below 300kb</p>";
        urls1.length = ""
    }
    else  if(!allowedImages1.exec(fileImages1.files[0].name)){
        document.getElementById("preview1").innerHTML = "<p>Please select jpeg/png/jpg files only</p>"
        urls1.length = ""

    }else if(fileImages1.files.length > 3){
            document.getElementById("preview1").innerHTML = "<p>Please select only 3 files</p>";
            urls1.length = ""
        }else {
            document.getElementById("preview1").innerHTML = '';
            urls1.length = ""
            for(let i = 0; i < 3; i++){
                let url = URL.createObjectURL(event.target.files[i]);
                urls1.push(url)
                if(allowedImages1.exec(fileImages1.files[i].name)){
                    document.getElementById("preview1").innerHTML += '<img src="'+urls1[i]+'">';
                }else if(!allowedImages1.exec(fileImages1.files[i].name)){
                    urls1.length = ""
                    document.getElementById("preview1").innerHTML = "<p>Please select jpeg/png/jpg files only</p>"
                    Img.style.display="none";
                    
                }
            }
        }

    
}

business_proof.addEventListener("change", previewMultiple1);





// Image Validation and Preview
let urls2 = []
let fileImages2;
const allowedImages2 = 
/(\.jpeg|\.png|\.jpg)$/i;
function previewMultiple2(event){
    fileImages2 = document.getElementById("corporate_profile");
    document.getElementById("preview2").innerHTML = "";
    
    
    if(fileImages2.files[0].size > 300000){
        document.getElementById("preview2").innerHTML = "<p>Please select below 300kb</p>";
        urls2.length = ""
    }
    else  if(!allowedImages2.exec(fileImages2.files[0].name)){
        document.getElementById("preview2").innerHTML = "<p>Please select jpeg/png/jpg files only</p>"
        urls2.length = ""

    }else if(fileImages2.files.length > 3){
            document.getElementById("preview2").innerHTML = "<p>Please select only 3 files</p>";
            urls2.length = ""
        }else {
            document.getElementById("preview2").innerHTML = '';
            urls2.length = ""
            for(let i = 0; i < 3; i++){
                let url = URL.createObjectURL(event.target.files[i]);
                urls2.push(url)
                if(allowedImages2.exec(fileImages2.files[i].name)){
                    document.getElementById("preview2").innerHTML += '<img src="'+urls2[i]+'">';
                }else if(!allowedImages2.exec(fileImages2.files[i].name)){
                    urls2.length = ""
                    document.getElementById("preview2").innerHTML = "<p>Please select jpeg/png/jpg files only</p>"
                    Img.style.display="none";
                    
                }
            }
        }

    
}

corporate_profile.addEventListener("change", previewMultiple2);
















//Initialising bootstrap tooltips
$(document).ready(function(){
    // $('[data-bs-toggle="tooltip"]').tooltip();  
    $('.multi_select').select2( {
        maximumSelectionLength: 30,
        allowClear: true,
        closeOnSelect : false,
        multiple: true,
        placeholder: 'Select options',
     })
     $(".empty").select2(
        $(".empty").prop("disabled", true)
    );
     $('.single_select').select2()
});



//Initialising IntlTelInputs
const phone_input = document.getElementById("phone"); 
window.intlTelInput(phone_input, {  separateDialCode: true });

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

