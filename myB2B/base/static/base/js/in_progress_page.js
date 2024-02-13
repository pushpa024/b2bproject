
//Handling typing effect
const typedText = document.querySelector('.typed-text');
const cursorSpan = document.querySelector('.cursor')
const textArray = [ "This page is under Development.", "We are working on this page.", "Comming soon!!","Giving it a revamp.", " Can't wait to have this."];
const typingDelay = 200;
const erasingDelay = 100;
const newTextDelay = 200 ;  //delay between words
let textArrIndex = 0;
let charIndex = 0;
function type(){
         if(charIndex < textArray[textArrIndex].length){
             if(!cursorSpan.classList.contains("typing"))
             cursorSpan.classList.add("typing")
             typedText.textContent += textArray[textArrIndex].charAt(charIndex);
             charIndex++;
             setTimeout(type, typingDelay);
         }
         else{
            cursorSpan.classList.remove("typing")
         setTimeout(erase, newTextDelay)

         }  
}
function erase(){
    if(charIndex > 0){
        if(!cursorSpan.classList.contains("typing")) 
         cursorSpan.classList.add("typing")
        typedText.textContent = textArray[textArrIndex].substring(0, charIndex-1);
        charIndex--;
        setTimeout(erase, erasingDelay)
    }
    else{
        cursorSpan.classList.remove("typing");
        textArrIndex++;
        if(textArrIndex >=textArray.length)
            textArrIndex =0;
            setTimeout(type, typingDelay + 1100)
    }
}
document.addEventListener('DOMContentLoaded', function() {
if(textArray.length)  setTimeout(type, newTextDelay + 100);
})
