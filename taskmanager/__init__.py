import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# create an instance of the SQLAlchemy class, passing in the app
db = SQLAlchemy(app)

'''
routes imported last, because the 'routes' file, that we're about
to create, will rely on using both the 'app' and 'db' variables defined above.
If we try to import routes before 'app' and 'db' are defined, then we'll get circular-import
errors, meaning those variables aren't yet available to use, as they're defined after the routes.
'''
from taskmanager import routes  # noqa
