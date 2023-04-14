$(document).ready(function () {
    //  initialize the sidenav-trigger line into the navbar
    M.Sidenav.init($('.sidenav'));

    // initialize datepicker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    // initialize the select element
    M.FormSelect.init($('select'));

    // initialize the collapsible task elements
    M.Collapsible.init($('.collapsible'));


    // Populate a modal with info about a category and set the delete link for that category.
    $("#delete-category-btn").on('click', function() {
        console.log('he')
        categoryData = $(this).data('category');
        // console.dir(categoryData)
        $("#modal-category-name").text(categoryData.category_name);
        $("#confirm-delete").attr("href", '/delete_category/' + categoryData.id)
    })

    // `delete category` modal Initialization
    M.Modal.init($('#modal-delete-category'));

    // flashes modal Initialization
    M.Modal.init($("#flashes-modal"), {
        opacity: 0.4,
    });

    const flashesInstance = M.Modal.getInstance($("#flashes-modal"));
    // flashing message in modal
    if ($("#flashes-wrapper *").length > 0) {
        flashesInstance.open();
    }


    // update copyright year in the footer
    $("#copyright").text(new Date().getFullYear());
});





