//  initialize the sidenav-trigger line into the navbar
$(document).ready(function () {
    $('.sidenav').sidenav();
});

// update copyright year in the footer
$("#copyright").text(new Date().getFullYear());