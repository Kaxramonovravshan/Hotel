let codify = () => {


    return({
        createModal: (name) => {
            let btns = document.querySelectorAll(`.${name}`)
            let modal = document.querySelector(`#${name}`)

            for(let btn of btns){
                btn.addEventListener('click', ()=> {
                    modal.classList.toggle('d-none')
                })
            }
            
        },
       
    })
}

// var video = document.getElementById("myVideo");
// var btn = document.getElementById("myBtn");

// function myFunction() {
//     if (video.paused) {
//         video.play();
//         btn.innerHTML = "Pause";
//     } else {
//         video.pause();
//         btn.innerHTML = "Play";
//     }
// }

window.onload = function(){
    window.setInterval(function(){
        let date = new Date()

        let hours = date.getHours()
        let minuts = date.getMinutes()
        let seconds = date.getSeconds()
        if(hours<10){
            hours = '0' + hours
        }
        if(minuts<10){
            minuts ='0'+ minuts
        }
        if(seconds<10){
            seconds = '0'+ seconds
        }
        let clock = hours + ':' + minuts + ':'+ seconds
        document.getElementById('clock').innerHTML = clock


    })
};

