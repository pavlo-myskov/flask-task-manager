$(document).ready(function () {
    //  initialize the sidenav-trigger line into the navbar
    $('.sidenav').sidenav();

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





