$(document).ready(function () {
    //  initialize the sidenav-trigger line into the navbar
    $('.sidenav').sidenav();

    // initialize datepicker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    // initialize the select element
    $('select').formSelect();

    // initialize the collapsible task elements
    $('.collapsible').collapsible();

    // modal Initialization
    const modal1 = $('#modal1').modal();
    var instance = M.Modal.getInstance(modal1);
    // instance.options.dismissible = false;
    instance.options.opacity = 0.4;

    // Populate a modal with info about a category and set the delete link for that category.
    $(".modal-trigger").on('click', function() {
        categoryData = $(this).data('category');
        $("#modal-category-name").text(categoryData.category_name);
        $("#confirm-delete").attr("href", '/delete_category/' + categoryData.id)
    })


    // update copyright year in the footer
    $("#copyright").text(new Date().getFullYear());
});





