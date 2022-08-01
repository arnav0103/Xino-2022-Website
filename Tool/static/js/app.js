//loader
window.addEventListener('load', ()=> {
    setTimeout(()=> {
        document.querySelector('.loading-wrapper').classList.add('faded');
    }, 500);
})

//navbar responsive
const navBtn = document.querySelector('.toggleNav');
const navBar = document.querySelector('.navbar-responsive')

navBtn.addEventListener('click', () => {
    if (navBar.classList.contains('navbar-responsive-dark-mode')) {
        if (navBtn.classList.contains('close-dark-mode') || navBtn.classList.contains('close')) {
            navBar.classList.toggle('open');
            navBtn.classList.remove('close-dark-mode');
            navBtn.classList.remove('close');
        } else {
            navBar.classList.toggle('open');
            navBtn.classList.add('close-dark-mode');
            navBtn.classList.remove('close');
        }
    } else {
        if (navBtn.classList.contains('close') || navBtn.classList.contains('close-dark-mode')) {
            navBar.classList.toggle('open');
            navBtn.classList.remove('close');
            navBtn.classList.remove('close-dark-mode');
        } else {
            navBar.classList.toggle('open');
            navBtn.classList.add('close');
            navBtn.classList.remove('close-dark-mode');
        }
    }
})
