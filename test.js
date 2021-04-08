const card = document.querySelector(".card");
const card2 = document.querySelector(".card2");
const card3 = document.querySelector(".card3");
const card4 = document.querySelector(".card4");
const card5 = document.querySelector(".card5");
const card6 = document.querySelector(".card6");
const card7 = document.querySelector(".card7");

card.addEventListener("mousemove", (e) => { 
    console.log(e.pageX) 
});
    /*let xAxis = (window.innerWidth / 2 - e.pageX) / 25;
    let yAxis = (window.innerHeight / 2 - e.pageY) / 25;
    card.style.transform = 'rotateY(${xAxis}deg) rotateX(${yAxis}deg)'
    */
