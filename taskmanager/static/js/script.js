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

    // confirm delete modal Initialization
    M.Modal.init($('#modal1'), {
        opacity: 0.4
    });

    // flashes modal Initialization
    M.Modal.init($("#flashes-modal"), {
        opacity: 0.4,
    });
    const flashesInstance = M.Modal.getInstance($("#flashes-modal"));
    // flashing message in modal
    console.log($("#flashes-wrapper *"));
    if ($("#flashes-wrapper *").length > 0) {
        flashesInstance.open();
    }

    // Populate a modal with info about a category and set the delete link for that category.
    $(".modal-trigger").on('click', function() {
        categoryData = $(this).data('category');
        $("#modal-category-name").text(categoryData.category_name);
        $("#confirm-delete").attr("href", '/delete_category/' + categoryData.id)
    })


    // update copyright year in the footer
    $("#copyright").text(new Date().getFullYear());
});





