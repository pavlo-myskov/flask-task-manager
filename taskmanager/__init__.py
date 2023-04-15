from config import load_config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(load_config())


# create an instance of the SQLAlchemy class, passing in the app
db = SQLAlchemy(app)
migrate = Migrate(app, db)

'''
routes imported last, because the 'routes' file, that we're about
to create, will rely on using both the 'app' and 'db' variables defined above.
If we try to import routes before 'app' and 'db' are defined, then we'll get
circular-import errors, meaning those variables aren't yet available to use,
as they're defined after the routes.
'''
from taskmanager import routes  # noqa
