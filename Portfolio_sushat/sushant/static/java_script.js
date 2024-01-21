let x=document.querySelector('.fa-bars');
let y=document.querySelector('.fa-xmark');
let z=document.querySelectorAll('.navbar');
x.addEventListener('click',function () {
    for(let s of z) {
       s.classList.add("active") 
      };
});
y.addEventListener('click',function () {
    for(let s of z) {
       s.classList.remove("active")
      };  
});