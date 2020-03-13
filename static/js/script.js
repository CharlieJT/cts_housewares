// Constants used to target specific class names needed for jQuery

const navbarContainer = document.getElementsByClassName("navbar-container");
const navbarLogo = document.getElementsByClassName("navbar-logo");
const navbarLogoScrolled = document.getElementsByClassName("navbar-logo-scrolled");
const previousPage = document.getElementsByClassName("previous-page");
const mainProductImage = document.getElementsByClassName("main-product-image");
const navbarToggler = document.getElementsByClassName("navbar-toggler");
const mobileNavbarContainer = document.getElementsByClassName("mobile-navbar-container");
const backdrop = document.getElementsByClassName("backdrop");


$(document).ready(() => {
    // Will check to see if the window has been scrolled 50px from the top.
    $(window).scroll(() => {
        if ($(document).scrollTop() > 50) {
            $(navbarContainer).css({ "height": "66px", "box-shadow": "0 2px 5px #5f5f5f" });
            $(navbarLogo).css("display", "none");
            $(navbarLogoScrolled).css("display", "block");
            $(mobileNavbarContainer).css("top", "66px");
        }
        else {
            $(navbarContainer).css({ "height": "92px", "box-shadow": "none" });
            $(navbarLogo).css("display", "block");
            $(navbarLogoScrolled).css("display", "none");
            $(mobileNavbarContainer).css("top", "92px");
        }
    });
    $(previousPage).on('click', () => {
        window.history.back(1);
    });
    $(backdrop).on("click", () => {
        $(navbarToggler).click();
    });
    $(navbarToggler).on('click', () => {
        if ($(navbarToggler).hasClass("collapsed")) {
            $(mobileNavbarContainer).css("right", "-70%");
            $(backdrop).css("display", "none");
        } else {
            $(mobileNavbarContainer).css("right", "0");
            $(backdrop).css("display", "block");
        }
    });
});