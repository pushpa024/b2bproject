//
(function ($bs) {
  const CLASS_NAME = "has-child-dropdown-show";
  $bs.Dropdown.prototype.toggle = (function (_orginal) {
    return function () {
      document.querySelectorAll("." + CLASS_NAME).forEach(function (e) {
        e.classList.remove(CLASS_NAME);
      });
      let dd = this._element
        .closest(".dropdown")
        .parentNode.closest(".dropdown");
      for (; dd && dd !== document; dd = dd.parentNode.closest(".dropdown")) {
        dd.classList.add(CLASS_NAME);
      }
      return _orginal.call(this);
    };
  })($bs.Dropdown.prototype.toggle);

  document.querySelectorAll(".dropdown").forEach(function (dd) {
    dd.addEventListener("hide.bs.dropdown", function (e) {
      if (this.classList.contains(CLASS_NAME)) {
        this.classList.remove(CLASS_NAME);
        e.preventDefault();
      }
      e.stopPropagation();
    });
  });
})(bootstrap);

//
function dropDownFuncMail() {
  document.getElementById("mailDropdown").classList.toggle("show-1");

  document.getElementById("bellDropdown").classList.remove("show-2");

  document.getElementById("userDropdown").classList.remove("show-3");
}

function dropDownFuncBell() {
  document.getElementById("bellDropdown").classList.toggle("show-2");

  document.getElementById("mailDropdown").classList.remove("show-1");

  document.getElementById("userDropdown").classList.remove("show-3");
}

function dropDownFuncUser() {
  document.getElementById("userDropdown").classList.toggle("show-3");

  document.getElementById("bellDropdown").classList.remove("show-2");

  document.getElementById("bellDropdown").classList.remove("show-1");
}

window.onclick = function (event) {
  if (!event.target.matches(".dropbtn-1")) {
    let dropdowns = document.getElementsByClassName("dropdown-content-1");
    for (let i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show-1")) {
        openDropdown.classList.remove("show-1");
      }
    }
  } else if (!event.target.matches(".dropbtn-2")) {
    let dropdowns = document.getElementsByClassName("dropdown-content-2");
    for (let i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show-2")) {
        openDropdown.classList.remove("show-2");
      }
    }
  } else if (!event.target.matches(".dropbtn-3")) {
    let dropdowns = document.getElementsByClassName("dropdown-content-3");
    for (let i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show-3")) {
        openDropdown.classList.remove("show-3");
      }
    }
  }
};

function handleClose() {
  document.getElementById("mailDropdown").classList.remove("show-1");
  document.getElementById("bellDropdown").classList.remove("show-2");
  document.getElementById("userDropdown").classList.remove("show-3");
}

// Profile
const chooseFile = document.getElementById("choose-file");
const imgPreview = document.getElementById("img-preview");

chooseFile.addEventListener("change", function () {
  removeSrc();
  getImgData();
});

function getImgData() {
  const files = chooseFile.files[0];
  if (files) {
    const fileReader = new FileReader();
    fileReader.readAsDataURL(files);
    fileReader.addEventListener("load", function () {
      imgPreview.style.display = "block";
      imgPreview.innerHTML = `<img src=${this.result} />`;
    });
  }
}
function removeSrc() {
  imgPreview.innerHTML = `<img src=${""} />`;
}

// profile Slider
// Profile
const chooseFileSlider = document.getElementById("choose-file-slider");
const imgPreviewSlider = document.getElementById("profile-dp-slide");

chooseFileSlider.addEventListener("change", function () {
  removeSrcSlider();
  getImgDataSlider();
});

function getImgDataSlider() {
  const files = chooseFileSlider.files[0];
  if (files) {
    const fileReader = new FileReader();
    fileReader.readAsDataURL(files);
    fileReader.addEventListener("load", function () {
      imgPreviewSlider.style.display = "block";
      imgPreviewSlider.innerHTML = `<img src=${this.result} />`;
    });
  }
}
function removeSrcSlider() {
  imgPreviewSlider.innerHTML = `<img src=${""} />`;
}
