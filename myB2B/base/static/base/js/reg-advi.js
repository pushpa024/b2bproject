
//   $(document).ready(function() {
//       $("#button-first").click(function() {
//           $("#button-first").addClass("active");
//           $("#button-second").removeClass("active");
//           $("#first").css("display", "block");
//           $("#second").css("display", "none");
//       });
//       $("#button-second").click(function() {
//           $("#button-second").addClass("active");
//           $("#button-first").removeClass("active");
//           $("#first").css("display", "none");
//           $("#second").css("display", "block");
//       });
//   });

//   Buttons
const button_1 = document.querySelector("#planset-button-BUY_SIDE_PLANS");
const button_2 = document.querySelector("#planset-button-SELL_SIDE_PLANS");
const btn_2_elements_remove = document.getElementsByClassName("btn_2_element");
const btn_1_elements_remove = document.getElementsByClassName("btn_1_element");
console.log("btn_2_elements_remove " + btn_2_elements_remove.length);
button_1.classList.add("active");
for (const element of btn_2_elements_remove) {
    element.classList.add("elements_remove");
}

button_1.addEventListener("click", () => {
    console.log("button_1  " + button_1 );
    button_1.classList.add("active");
    button_2.classList.remove("active");
    for (const element of btn_2_elements_remove) {
        element.classList.add("elements_remove");
    }
    for (const element of btn_1_elements_remove) {
        element.classList.remove("elements_remove");
    }  
});

button_2.addEventListener("click", () => {
    console.log("button_2 " + button_2);
    button_1.classList.remove("active");
    button_2.classList.add("active");
    for (const element of btn_1_elements_remove) {
        element.classList.add("elements_remove");
    }
    for (const element of btn_2_elements_remove) {
        element.classList.remove("elements_remove");
    }
})

// window.addEventListener('load', (event) => {
//     console.log('page is fully loaded');
// });