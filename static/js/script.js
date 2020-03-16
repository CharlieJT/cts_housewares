// Constants used to target specific class names needed for jQuery

const navbarContainer = document.getElementsByClassName("navbar-container");
const navbarLogo = document.getElementsByClassName("navbar-logo");
const navbarLogoScrolled = document.getElementsByClassName("navbar-logo-scrolled");
const previousPage = document.getElementsByClassName("previous-page");
const mainProductImage = document.getElementsByClassName("main-product-image");
const navbarToggler = document.getElementsByClassName("navbar-toggler");
const mobileNavbarContainer = document.getElementsByClassName("mobile-navbar-container");
const backdrop = document.getElementsByClassName("backdrop");
const burgerIcon1 = document.getElementsByClassName("burger-icon-1");
const burgerIcon2 = document.getElementsByClassName("burger-icon-2");
const burgerIcon3 = document.getElementsByClassName("burger-icon-3");


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
            $(burgerIcon1).css("transform", "translateY(-3px) rotate(0deg)");
            $(burgerIcon2).css({"transform": "translateX(0px)", "opacity": "1"});
            $(burgerIcon3).css("transform", "translateY(3px) rotate(0deg)");
        } else {
            $(mobileNavbarContainer).css("right", "0");
            $(backdrop).css("display", "block");
            $(burgerIcon1).css("transform", "translateY(4px) rotate(-135deg)");
            $(burgerIcon2).css({"transform": "translateX(-50px)", "opacity": "0"});
            $(burgerIcon3).css("transform", "translateY(-4px) rotate(135deg)");
        }
    });
});