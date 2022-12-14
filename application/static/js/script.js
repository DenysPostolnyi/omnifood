const yearEl = document.querySelector(".year");
const currentYear = new Date().getFullYear();
yearEl.textContent = currentYear.toString();

const btnNav = document.querySelector('.btn-mobile-nav');
const headerEl = document.querySelector('.header');

btnNav.addEventListener('click', function () {
    headerEl.classList.toggle('nav-open');
});

// // close nav menu
// const mainNavLink = document.querySelectorAll('.main-nav-link');
// mainNavLink.forEach(function (nav) {
//     nav.addEventListener('click', function () {
//         headerEl.classList.toggle('nav-open');
//     });
// });

/////////////////////////////////////////////////////////////////////////
//Smooth scrolling animation

const allLinks = document.querySelectorAll('a:link');
allLinks.forEach(function (link) {
    link.addEventListener('click', function (ev) {
        ev.preventDefault();
        const href = link.getAttribute('href');

        // Scroll back to the top
        if (href === '#') window.scrollTo({
            top: 0,
            behavior: 'smooth',
        })
        // Scroll back to the top
        else if (href !== '#' && href.startsWith('#')) {
            const sectionEl = document.querySelector(href);
            sectionEl.scrollIntoView({behavior: 'smooth'});
        } else {
            location.assign(href);
        }
// close nav menu
        if (link.classList.contains('main-nav-link'))
            headerEl.classList.toggle('nav-open');
    });
});

////////////////////////////////////////////////////////////
// Sticky navigation

const sectionHero = document.querySelector('.section-hero');

const obs = new IntersectionObserver(function (entries) {
        const ent = entries[0];
        if (!ent.isIntersecting) {
            document.body.classList.add('sticky');
        }

        if (ent.isIntersecting) {
            document.body.classList.remove('sticky');
        }
    },
    {
        // in the viewport
        root: null,
        threshold: 0,
        rootMargin: '-80px'
    });
obs.observe(sectionHero);

// Fixing flexbox gap property missing in some Safari versions
function checkFlexGap() {
    let flex = document.createElement("div");
    flex.style.display = "flex";
    flex.style.flexDirection = "column";
    flex.style.rowGap = "1px";

    flex.appendChild(document.createElement("div"));
    flex.appendChild(document.createElement("div"));

    document.body.appendChild(flex);
    let isSupported = flex.scrollHeight === 1;
    flex.parentNode.removeChild(flex);
    // console.log(isSupported);

    if (!isSupported) document.body.classList.add("no-flexbox-gap");
}

checkFlexGap();

/////////////////////////////////////
// Showing message

function message(text) {
    alert(text);
}

///////////////////////////////
// Modal window

const modal = document.querySelector(".login");

// Get the button that opens the modal
const signBtn = document.querySelector(".sign-in-btn");

// Get the <button> element that closes the modal
const closeBtn = document.querySelector('.btn-login-close');

// When the user clicks on the button, open the modal
if (signBtn !== null){
    signBtn.addEventListener('click', function () {
        modal.classList.toggle('open-modal');
    });
}

// When the user clicks on <span> (x), close the modal
closeBtn.addEventListener('click', function () {
    modal.classList.toggle('open-modal');
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.classList.toggle('open-modal');
    }
}

//////////////////////////////////////////////////////
// Falling list

const list = document.querySelector(".fall-list-cont");

// Get the button that opens the modal
const openList = document.querySelector(".fall-opener");

// When the user clicks on the button, open the modal
if (openList !== null){
    openList.addEventListener('click', function () {
        list.classList.toggle('fall-list-cont-open');
    });
}


