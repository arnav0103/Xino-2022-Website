//dark mode for events page
const darkModeBtn = document.querySelector('.dark-toggle__input');
let darkMode = localStorage.getItem('darkMode');
console.log(darkMode);

function enableDarkMode () {
   document.querySelector('.loading-wrapper').classList.add('loading-dark-theme');
   document.querySelector('body').classList.add('dark-theme');
   document.querySelector('.navbar__logo').src = '/img/logo white.png';
   document.querySelector('.dark-toggle span').classList.add('dark-toggle-span');  
   const navLinks = document.querySelectorAll('.navbar__link');
    navLinks.forEach((link) => {
        link.classList.add('navbar__link-dark-mode');
    });
    const ctaBtn = document.querySelectorAll('.btn-black');
    ctaBtn.forEach((btn) => {
        btn.classList.add('btn-black-dark-mode');
    });
    const alumnusPost = document.querySelectorAll('.alumnus__post');
    alumnusPost.forEach((post) => {
        post.classList.add('alumnus__post-dark-mode');
    });
    document.querySelector('.toggleNav').classList.add('toggleNav-dark-mode');
    document.querySelector('.navbar-responsive').classList.add('navbar-responsive-dark-mode');
    document.querySelector('.navbar-responsive span').classList.add('navbar-responsive-span-dark-mode');
    document.querySelector('.navbar-responsive label').classList.add('navbar-responsive-label-dark-mode');
    const respNavLinks = document.querySelectorAll('.navbar-responsive a');
    respNavLinks.forEach((link) => {
        link.classList.add('navbar-responsive-links-dark-mode');
    });
    document.querySelector('.navbar-responsive span').textContent = 'Light Mode';
    localStorage.setItem('darkMode', 'enabled');
}

function disableDarkMode () {
    document.querySelector('.loading-wrapper').classList.remove('loading-dark-theme');
    document.querySelector('body').classList.remove('dark-theme');
    document.querySelector('.navbar__logo').src = '/img/logo dark.png';
    document.querySelector('.dark-toggle span').classList.remove('dark-toggle-span');  
    const navLinks = document.querySelectorAll('.navbar__link');
    navLinks.forEach((link) => {
        link.classList.remove('navbar__link-dark-mode');
    }); 
    const ctaBtn = document.querySelectorAll('.btn-black');
    ctaBtn.forEach((btn) => {
        btn.classList.remove('btn-black-dark-mode');
    });
    const alumnusPost = document.querySelectorAll('.alumnus__post');
    alumnusPost.forEach((post) => {
        post.classList.remove('alumnus__post-dark-mode');
    });
    document.querySelector('.toggleNav').classList.remove('toggleNav-dark-mode');
    document.querySelector('.navbar-responsive').classList.remove('navbar-responsive-dark-mode');
    document.querySelector('.navbar-responsive span').classList.remove('navbar-responsive-span-dark-mode');
    document.querySelector('.navbar-responsive label').classList.remove('navbar-responsive-label-dark-mode');
    const respNavLinks = document.querySelectorAll('.navbar-responsive a');
    respNavLinks.forEach((link) => {
        link.classList.remove('navbar-responsive-links-dark-mode');
    });
    document.querySelector('.navbar-responsive span').textContent = 'Dark Mode';
    localStorage.setItem('darkMode', null);
}

if (darkMode === 'enabled') {
    enableDarkMode();
    darkModeBtn.checked = true;
}

darkModeBtn.addEventListener('click', () => {
    darkMode = localStorage.getItem('darkMode');
    if (darkMode !== 'enabled') {
        console.log(darkMode);
        enableDarkMode();
    } else {
        console.log(darkMode);
        disableDarkMode();
    }
})