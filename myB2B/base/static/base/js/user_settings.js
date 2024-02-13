$(document).ready(function() {
    $('.location-selector').select2({
        maximumSelectionLength: 30,
        allowClear: true,
        closeOnSelect : false,
        multiple: true,
        placeholder: 'Preferred Locations',
    }
    );
})

function process() {
     

    const file = document.querySelector("#upload").files[0];
   if (!file) return;  
   const reader = new FileReader();
   reader.readAsDataURL(file);
 

 
   reader.onload = function (event) {
     const imgElement = document.createElement("img");
     imgElement.src = event.target.result;
   //   document.querySelector("#input").src = event.target.result;       
   //uncomment above line if you want to show the original image
 
     imgElement.onload = function (e) {
       const canvas = document.createElement("canvas");
       const MAX_WIDTH = 150;
       const MAX_HEIGHT=150;
 
       const scaleSize = MAX_WIDTH / e.target.width;
       canvas.width = MAX_WIDTH;
       canvas.height = MAX_HEIGHT;

       // canvas.height = e.target.height * scaleSize;
 
       const ctx = canvas.getContext("2d");
 
       ctx.drawImage(e.target, 0, 0, canvas.width, canvas.height);
 
       const srcEncoded = ctx.canvas.toDataURL(e.target, "image/jpeg");
 
       // you can send srcEncoded to the server
       // document.querySelector("#output").src = srcEncoded;
       document.getElementById('show-final').src=srcEncoded;
     };
   };
 }
