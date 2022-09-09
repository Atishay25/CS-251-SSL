const bluebtn = document.getElementById('bluebtn');
const redbtn = document.getElementById('redbtn');

bluebtn.addEventListener('click', function onClick(event){
    const sometext = document.getElementById('sometext');
    sometext.style.color = 'blue';
});

redbtn.addEventListener('click', function onClick(event){
    const sometext = document.getElementById('sometext');
    sometext.style.color = 'red';
});

function handlesubmit(){
    let name = document.querySelector('input').value;
    alert("Hello " + name + ", You're doing well!");
}
