/*Script for Checkbox working*/

const btn = document.querySelector('#submitbtn');
btn.addEventListener('click',(event) => {
    event.preventDefault();
    let checkboxes = document.querySelectorAll('input[name="hobby"]:checked');
    let values = [];
    checkboxes.forEach((checkboxes) => {
        values.push(checkboxes.value);
        checkboxes.checked = true;
    });
    alert("Hobbies selected : " + values + ". Click 'OK' to know more about these :)");
    showhobby(values);
});

function showhobby(hobbies){
      var keys = ["Sports and Games","Playing Keyboard","Gym and Fitness","Listening Music","Rail Fan","Marvel Cinematic Universe"] ;
      keys.forEach( (e) => document.getElementById(e).style.display = "none" )                                                                                                                                                                           
   
    hobbies.forEach( (hobby) => { 
       document.getElementById(hobby).style.display = "block"
    })
}


