// Constants used to target specific class names needed for jQuery

const navbarContainer = document.getElementsByClassName("navbar-container");
const navbarLogo = document.getElementsByClassName("navbar-logo");
const navbarLogoScrolled = document.getElementsByClassName("navbar-logo-scrolled");

$(document).ready(() => {
    // Will check to see if the window has been scrolled 50px from the top.
    $(window).scroll(() => {
        if ($(document).scrollTop() > 50) {
            $(navbarContainer).css("height", '66px');
            $(navbarLogo).css("display", "none");
            $(navbarLogoScrolled).css("display", "block");
        }
        else {
            $(navbarContainer).css("height", '92px');
            $(navbarLogo).css("display", "block");
            $(navbarLogoScrolled).css("display", "none");
        }
    });
});