// enable hidden nav bar
const nav = document.querySelector('.navigation');
const navY = nav.offsetHeight;
const footer = document.getElementById("footer");
const footerY = nav.offsetHeight;
let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {
  if (pageYOffset >= navY && lastScrollY < window.scrollY) {
    // If current scroll position is greater than or equal to navY and scrolling down,
    // add 'nav--hidden' class to hide the navigation bar.
    nav.classList.add('nav--hidden');
  } else if (lastScrollY - 7 > window.scrollY) {
      nav.classList.remove('nav--hidden');
    }

  // Update the last scroll position to the current scroll position.
  lastScrollY = window.scrollY;
});

const navToggle = document.querySelector(".nav-toggle");
const links = document.querySelector(".nav-links");

navToggle.addEventListener("click", function () {
  // console.log(links.classList);
  // console.log(links.classList.contains("random"));
  // console.log(links.classList.contains("links"));
  // if (links.classList.contains("show-links")) {
  //   links.classList.remove("show-links");
  // } else {
  //   links.classList.add("show-links");
  // }
  links.classList.toggle("show-links");
  navToggle.classList.toggle("active-case")
});

// fader on scroll

const faders = document.querySelectorAll('.fade-in');

const sliders = document.querySelectorAll('.slide-in');

const appearOptions = {
  threshold: 0,
  rootMargin: "0px 0px -100px 0px"
}


const appearsOnScroll = new IntersectionObserver(function(entries, observer) {
  entries.forEach(entry => {
    if (!entry.isIntersecting) {
      return;
    } else {
      entry.target.classList.add('appear');
      observer.unobserve(entry.target);
    }
  })
}, appearOptions);

sliders.forEach(slider => {
  appearsOnScroll.observe(slider);
})

// gallery pages

// Get the modal
const modal = document.getElementById("myModal");

// Get the modal image and caption elements
const modalImg = document.getElementById("img01");
const captionText = document.getElementById("caption");

// Get all images that will open the modal
const images = document.querySelectorAll('.modal-img');

// Add click event listeners to each image
images.forEach((img, index) => {
  img.onclick = function() {
    modal.style.display = "block";
    modal.style.zIndex = "1000";
    slideIndex = index + 1;  // Update the slide index
    showSlides(slideIndex);
  }
});

// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
};

let slideIndex = 1;

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  const images = document.querySelectorAll('.modal-img');  // Get all the images again
  const dots = document.getElementsByClassName("demo");

  if (n > images.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = images.length }

  // Update the modal image and caption
  modalImg.src = images[slideIndex - 1].src;
  captionText.innerHTML = images[slideIndex - 1].alt;

  // Remove 'active' class from all dots
  for (let i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  // Add 'active' class to the corresponding dot
  dots[slideIndex - 1].className += " active";
}


// Add gallery page
// get more image inputs
document.addEventListener("DOMContentLoaded", function() {
// Get all image input divs
  const imageInputs = document.querySelectorAll(".image-input-display");
// Hide all image inputs initially
  imageInputs.forEach(input => input.style.display = "none");
// Get the button to show more image inputs
  const openButton = document.querySelector(".open-image-input");
// Get the button to hide image inputs
  const closeButton = document.querySelector(".close-image-input");
// Initialize a counter to keep track of the current image input to display
  let currentImageIndex = 0;
// Show image input on button click
  openButton.addEventListener('click', function() {
    if (currentImageIndex < imageInputs.length) {
      imageInputs[currentImageIndex].style.display = "block";
      currentImageIndex++;
    }});
// Hide image input on button click
    closeButton.addEventListener('click', function() {
      if (currentImageIndex > 0) {
        currentImageIndex--;
        imageInputs[currentImageIndex].style.display = "none";
      }
    });
  });