from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    # - refer to the Task model to create a one to many relationship.
    # - backref is used to create a virtual column in the Task model
    #   and establish a bidirectional relationship between the two models,
    #   meaning it sort of reverses and becomes many-to-one
    # - lazy=True means that when we query the database for categories,
    #   it can simultaneously identify any task linked to the categories
    tasks = db.relationship("Task", backref="category",
                            cascade="all, delete", lazy=True)


def __repr__(self):
    return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # one to many relationship with Category. A category can have many tasks
    # and when a category is deleted, all tasks associated with it are deleted
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"),
        nullable=False)

    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
