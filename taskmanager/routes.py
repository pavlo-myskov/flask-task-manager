from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.sql import exists

from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.due_date).all())
    return render_template("tasks.html", tasks=tasks)


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


def is_category_exist(category_name):
    category_name_exists = db.session.query(
        exists().where(Category.category_name == category_name)).scalar()
    return category_name_exists


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category_name = request.form.get("category_name")

        if is_category_exist(category_name):
            flash(f"Category {category_name} already exists")
            return redirect(url_for("add_category"))

        category = Category(category_name=category_name)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category_name = request.form.get("category_name")

        if category_name != category.category_name and \
                is_category_exist(category_name):
            flash(f"Category {category_name} already exists")
            return render_template("edit_category.html", category=category)

        category.category_name = category_name
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


def is_task_exist(task_name):
    # this flask_sqlalchemy method fetch the entire row from the database,
    # which is less efficient compared to using the exists()
    # task = Task.query.filter_by(task_name=task_name).first()
    # return task is not None

    # exists() function from SQLAlchemy only checks for the existence
    # of the row, without fetching any additional data.
    task_name_exists = db.session.query(
        exists().where(Task.task_name == task_name)).scalar()
    return task_name_exists


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task_name = request.form.get("task_name")

        if is_task_exist(task_name):
            flash(f"Task {task_name} already exists")
            return redirect(url_for("add_task"))

        task = Task(
            task_name=task_name,
            task_description=request.form.get(
                "task_description").strip() or None,
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date") or None,
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add_task.html", categories=categories)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    categories = list(Category.query.order_by(Category.category_name).all())
    task = Task.query.get_or_404(task_id)
    if request.method == "POST":
        task_name = request.form.get("task_name")

        if task_name != task.task_name and is_task_exist(task_name):
            flash(f"Task {task_name} already exists!")
            return render_template(
                "edit_task.html", task=task, categories=categories)

        task.task_name = task_name
        task.task_description = request.form.get(
            "task_description").strip() or None
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date") or None
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))
