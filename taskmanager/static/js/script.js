$(document).ready(function () {
    $(".delete-task-btn").click(delete_task);
    $(".delete-category-btn").click(delete_category);

    //  initialize the sidenav-trigger line into the navbar
    M.Sidenav.init($('.sidenav'));
    // initialize datepicker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: { done: "Select" }
    });
    // initialize the select element
    M.FormSelect.init($('select'));
    // initialize the collapsible task elements
    M.Collapsible.init($('.collapsible'));

    // `delete task` modal Initialization
    M.Modal.init($('.delete-modal'))

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


/**
 * Populate a modal with info about a category and
 * set the delete link for that category.
 */
function delete_category() {
    categoryData = $(this).data('category');
    $("#modal-category-name").text(categoryData.category_name);
    $("#confirm-delete-category").attr("href", '/delete_category/' + categoryData.id)
}

/**
 * Populate a modal with info about a task
 *  and set the delete link for that task.
 */
function delete_task() {
    taskData = $(this).data('task');
    $("#modal-task-name").text(taskData.task_name);
    $("#confirm-delete-task").attr("href", '/delete_task/' + taskData.id)
}



