$(document).ready(function(){
    $('[data-bs-toggle="tooltip"]').tooltip();  
    $('.input_select').select2();
    $(".empty").select2(
        $(".empty").prop("disabled", true)
    );
});

function show_investment_size(a)
{
 document.getElementById("range_investment").innerHTML = a;
}

function show_runrate(runrate)
{
 document.getElementById("run_rate_sales").innerHTML= runrate;
}
function show_ebitda(ebitda)
{
 document.getElementById("ebitda_value").innerHTML= ebitda;
}
function show_ebitda_margin(ebitda_m)
{
 document.getElementById("ebitda_margin").innerHTML= ebitda_m;
}



function show_rating(rating)
{
 document.getElementById("rating_value").innerHTML= rating;
}



function show_est_date(eyear)
{
 document.getElementById("est_date").innerHTML= eyear;
}





const setLabel = (lbl, val) => {
    const label = $(`#slider-${lbl}-label`);
    label.text(val);
    const slider = $(`#slider-div .${lbl}-slider-handle`);
    const rect = slider[0].getBoundingClientRect();
    label.offset({
      top: rect.top - 30,
      left: rect.left
    });
  }
  
  const setLabels = (values) => {
    setLabel("min", values[0]);
    setLabel("max", values[1]);
  }
  
  
  $('#ex2').slider().on('slide', function(ev) {
    setLabels(ev.value);
  });
  setLabels($('#ex2').attr("data-value").split(","));