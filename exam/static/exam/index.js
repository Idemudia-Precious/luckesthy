document.addEventListener('DOMContentLoaded', function(){
  document.querySelector('.mathematics').addEventListener('click', () => load_mathematics());
  document.querySelector('.mathematics2').addEventListener('click', () => load_mathematics2());

  load_mathematics();
  countdown(0, 59, 59);
});

function countdown(hr, mm, ss) {
  var interval = setInterval(function () {
    if(hr == 0 && mm == 0 && ss == 0)clearInterval(interval);
    ss--;
    if(ss == 0){
      ss = 59;
      mm--;
      if(mm == 0){
        mm = 59;
        hr --;
      }
    }
    if(hr == 0 && mm == 1 && ss == 1)
    {
      hr = 0;
      mm = 0;
      ss = 59;
    }
    if(hr.toString().length < 2) hr = "0"+hr;
    if(mm.toString().length < 2) mm = "0"+mm;
    if(ss.toString().length < 2) ss = "0"+ss;
    var time = $("#timer").html(hr+" : "+mm+" : "+ss);

    if (hr == "00" && mm == "30" && ss == "01" )
    {
      alert("Dear Candidate, you have 30 minutes more")
    }
    if (hr == "00" && mm == "15" && ss == "01" )
    {
      alert("Dear Candidate, you have 15 minutes more")
      var blink = document.getElementById('submit');
      blink.style.animation = 'blinkingBackground 2s infinite';
    }
    if (hr == "00" && mm == "05" && ss == "01" )
    {
      alert("Dear Candidate, you have 5 minutes more")
    }
    if (hr == "00" && mm == "00" && ss == "59" )
    {
      alert("Dear Candidate, you have 1 minute more")
    }

    if (hr == "00" && mm == "00" && ss == "30" )
    {
      alert("Dear Candidate, you have 30 seconds more")
    }

    if (hr == "00" && mm == "00" && ss == "01" )
    {
      var button = document.getElementById('submit');
      button.click();
    }
    //document.querySelector("#timer").innerHTML = `hr+" : "+mm+" : "+ss`
  }, 1000);
}

function load_mathematics() {
  document.querySelector('.mathematicsii').style.display='none';
  document.querySelector('.mathematicsi').style.display='block';
  document.getElementById('mathematics').style.background='white';
  document.getElementById('mathematics2').style.background='#aeaeae';
}
function load_mathematics2() {
  document.querySelector('.mathematicsi').style.display='none';
  document.querySelector('.mathematicsii').style.display='block';
  document.getElementById('mathematics2').style.background='white';
  document.getElementById('mathematics').style.background='#aeaeae';
}
