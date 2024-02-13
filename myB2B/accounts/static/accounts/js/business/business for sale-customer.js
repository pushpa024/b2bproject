const swiper1 = new Swiper(".mySwiper1", {
    slidesPerView: 1,
    spaceBetween: 10,
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 50,
      },
    },
    pagination: {
      el: ".swiper-pagination1",
      clickable: true,
    },
    autoplay: {
  delay: 2500,
  disableOnInteraction: false,
},

navigation: {
  nextEl: ".swiper-button-next1",
  prevEl: ".swiper-button-prev1",
},
   
  });

const swiper2 = new Swiper(".mySwiper2", {
    slidesPerView: 1,
    spaceBetween: 10,
    pagination: {
      el: ".swiper-pagination2",
      clickable: true,
    },
    autoplay: {
  delay: 2500,
  disableOnInteraction: false,
},

navigation: {
  nextEl: ".swiper-button-next2",
  prevEl: ".swiper-button-prev2",
},
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 50,
      },
    },
  });

const swiper3 = new Swiper(".mySwiper3", {
    slidesPerView: 1,
    spaceBetween: 10,
    pagination: {
      el: ".swiper-pagination3",
      clickable: true,
    },
    autoplay: {
  delay: 2500,
  disableOnInteraction: false,
},

navigation: {
  nextEl: ".swiper-button-next3",
  prevEl: ".swiper-button-prev3",
},
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 50,
      },
    },
  });

  const swiper4 = new Swiper(".mySwiper4", {
    slidesPerView: 1,
    spaceBetween: 10,
    pagination: {
      el: ".swiper-pagination-4",
      clickable: true,
    },
    autoplay: {
  delay: 2500,
  disableOnInteraction: false,
},

navigation: {
  nextEl: ".swiper-button-next4",
  prevEl: ".swiper-button-prev4",
},
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 30,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 30,
      },
    },
  });
  