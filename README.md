# Task Manager

This mini-project is a simple task manager app built using Flask, SQLAlchemy ORM, and a frontend framework Materialize.

The app allows to perform full CRUD (create, read, update, and delete) functionality on a database of tasks. All functionality is available through an HTML-based user interface. To provide a more user-friendly experience, the interface is styled using the Materialize which is a modern responsive front-end framework based off of Google's Material Design concept.

Live Demo: https://taskmanager-flaskapp.herokuapp.com/


## Features
### Navigation Bar
The navigation bar is displayed at the top of the page. It includes a logo with the name of the app and link to the home page. The navigation bar also includes a button to add a new task and a button to open a modal window with a list of categories.

### Main Content
- #### Add a Task
The home page displays a button to add a task. When the button is clicked, the window is expanded and a form to add a task is displayed. The form includes fields for the task name, task description, due date, if the task is urgent, and the task category. The form also includes a button to add the task to the database if all fields are filled out.

- #### Tasks
The List of Tasks is a list of collapsible elements. Each element represents a task storaged in the database. Once the task is clicked, the task details is expanded and displayed. The summary info of the task contains the task name, due date, whether the task is urgent. The task details include the task category, description and buttons to edit or delete the task.

### Categories
The List of Categories contains a button to add a new category and a list of all categories in the database. Each card of the category list contains the category name and two buttons to edit or delete the category from database. If the category is deleted, all tasks associated with the category are also deleted.

### Form elements
To provide a more user-friendly experience, the app contains vairous form elements, such as:
[switches](https://materializecss.com/switches.html), [datepickers](https://materializecss.com/pickers.html), [selectors](https://materializecss.com/select.html), and the [standard input boxes](https://materializecss.com/text-inputs.html).

## Technologies Used
- [Materialize](https://materializecss.com/getting-started.html) - front-end framework based on Material Design
- [jQuery 3.6.4](https://releases.jquery.com/) - JavaScript library
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - micro web framework written in Python
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for the Python programming language
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Flask extension that adds support for SQLAlchemy to your Flask application
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - Flask extension that handles SQLAlchemy database migrations for Flask applications using Alembic


## Project Setup
- ### Virtual Environment
#### Set Up Virtualenv with Virtualenvwrapper on Ubuntu 22.04
To isolate the project from the rest of the system, I used a virtual environment.
1. Install virtualenv and virtualenvwrapper using pip:
    ```
    $ sudo pip install virtualenv virtualenvwrapper
    ```
2. Add the directory where virtualenv was installed <~/.local/bin> to your system's PATH
    ```
    $ nano .bashrc
    <export PATH="$HOME/.local/bin:$PATH">
    ```
    **or**
    ```
    echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
    ```
    Any executables installed in <~/.local/bin> will be available to you from anywhere in your shell.
3. Finally edit <.bashrc> or <.bash_profile> or both:
    ```
    $ nano .bashrc
    <export WORKON_HOME=~/.virtualenvs>
    <export PROJECT_HOME=~/repos> # or wherever you keep your projects
    <export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv>
    <source ~/.local/bin/virtualenvwrapper.sh>
    ```
4. Reload the shell:
    ```
    $ source .bashrc
    ```
5. **Create a virtual environment** (flag `-a` means to associate the virtual       environment with a project):
    ```
    $ cd <path to project>
    $ mkvirtualenv -a <path to project> <name of virtual environment>
    ```
6. Activate the virtual environment:
    ```
    $ workon <name of virtual environment>
    ```

- ### Python Packages: Flask, Flask-SQLAlchemy, SQLAlchemy, psycopg2
- To install the required packages, run the following command:
    By installing Flask-SQLAlchemy, this actually comes with both Flask and the SQLAlchemy requirements together in one download.
    ```
    pip install 'Flask-SQLAlchemy<3' psycopg2 sqlalchemy==1.4.46
    ```
**OR**

- Add the following lines to the `<requirements.txt>` file:
    ```
    Flask==2.2.3
    Flask-SQLAlchemy==2.5.1
    psycopg2==2.9.6
    SQLAlchemy==1.4.46
    ```
    and run the following command:
    ```
    pip install -r requirements.txt
    ```

- ### App Environment Configuration Setup
**Configuring from Python Files `<config.py>` and `<.env>`**

Most applications need more than one configuration. There should be at least separate configurations for the production server and the one used during development. Configuration becomes more useful if you can store it in a separate file, ideally located outside the actual application package. You can deploy your application, then separately configure it for the specific deployment. This is especially useful if you have multiple environments, such as development, testing, and production.

- Create configuration file `<config.py>` in the root package.
- Install the `python-dotenv` package to load the environment variables from the `<.env>` file:
    ```
    $ pip install python-dotenv
    ```
- Import the `load_dotenv()` function in the `<config.py>` file:
    ```
    from dotenv import load_dotenv
    load_dotenv()
    ```
- Create environment variable `<.env>` for sensitive information and add it to the `<.gitignore>` file:
    ```
    $ touch .env .gitignore
    $ echo .env >> .gitignore
    ```
- Set the environment variables in the `<.env>` file:
    See the `<.env_example>` file.
- Import the `load_config()` function in the `__init__.py` file of the `taskmanager` package:
    ```
    from .config import load_config
    app.config.from_object(load_config())
    ```

- ### Database Setup

- ##### Local Setup
- Create database (_PostgreSQL 14/Ubuntu 22.04_):
    - Start running the PostgreSQL server:
        ```
        $ sudo service postgresql start
        ```
    - Log in to the PostgreSQL server as the default user:
        _This command connect you to the `postgres` database as the `postgres` user_
        ```
        $ sudo -u postgres psql
        ```
        If you want to connect to a different database, or as a different user, you can use the following command:
        ```
        $ psql -d <database name> -U <user name>
        ```
        **or**
        ```
        $ psql <database name>
        ```
    - Create a new database:
        ```
        # CREATE DATABASE <database name>;
        ```
    - Switch to the new database:
        ```
        # \c <database name>
        ```
    - Check the dt table in the database:
        ```
        # psql <database name>
        # \dt
        ```
    - Create tables using the SQLAlchemy ORM in the `models.py` file

- ##### Local Migration

    - Initial setup

    _This method only for initial setup, it creates all the necessary tables in your database as defined by your SQLAlchemy models. **Not recommended** if you are going to use Flask-Migrate extension, as initial setup woun't contain information about creating tables which affects the remote migration, and you will have to manually create the tables in the database using the the same method as for the local setup._
        ```
        $ python
        >>> from taskmanager import db
        >>> db.create_all()
        >>> exit()
        ```
    - **To make changes to the database, you need [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) extension:**

        ```
        $ pip install Flask-Migrate
        ```
    - Add the following lines to the `<__init__.py>` file of the main Flask app package:
        ```
        from flask_migrate import Migrate

        migrate = Migrate(app, db)
        ```

    - Create a migration repository

    _Run only once to initialize a new Alembic environment and create the required folder structure for managing database schema migrations_
        ```
        $ flask db init
        ```
    - Generate an initial migration:
        ```
        $ flask db migrate -m "Initial migration."
        ```
    - Apply the migration (changes described by the migration script) to the database:
        ```
        $ flask db upgrade
        ```
    **Note**: _Each time you make changes to the models, you need to run the migrate and upgrade commands to update the database_

    - To downgrade the database to the previous migration, you need to run the downgrade command:
        ```
        $ flask db downgrade
        ```

- ### jQuery
Add jQuery script using the CDN (Content Delivery Network) version of the framework.

Note: _jQuery library must be loaded before the Materialize `<script>` tag_
```
<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.6.4.js" integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E="crossorigin="anonymous"></script>
```

- ### Materialize and Material Design Icons
The easiest way to work with [Materialize](https://materializecss.com/getting-started.html) is to use the CDN (Content Delivery Network) version of the framework. To do this, add the following line to the `<head>` section of your HTML file:
```

<!-- Material Design Icons courtesy of Google -->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

<!-- Compiled and minified CSS -->
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
```
Then, add the following line to the end of the `<body>` section of your HTML file:
```
 <!-- Compiled and minified JavaScript -->
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
```

## Deployment
The application is deployed on Heroku.

Live Demo: https://taskmanager-flaskapp.herokuapp.com/

#### Deployment process using Heroku CLI:
- Create requirements file:
    ```$ pip freeze > requirements.txt```
- Add gunicorn server to requirements:
    ```$ echo "gunicorn" >> requirements.txt```
- Create a Heroku Procfile:
    * To run the flask app using using the Gunicorn WSGI server (recommended for production environments):
        ```$ echo "web: gunicorn run:app" > Procfile```
        - The `run` refers to the module (file) where your web application's main entry point is located.
        - The `app` refers to the application object or callable within that module, which is responsible for handling the incoming HTTP requests and returning the appropriate responses. This object is often an instance of a Flask or Django application.
    * To run the flask app using built-in Flask development server (not recommended):
    _Requires app.run() code in the `app.py` script_
        ```$ echo "web: python app.py" > Procfile```
- Login to Heroku:
    ```$ heroku login```
- Create a Heroku app:
    For existing repositories, simply add the heroku remote (connect to remote).
    ```$ heroku create example-app (or create using UI heroku)```
- Connect Git remote to Heroku:
    * By Heroku CLI and app name (full string can be obtained from the app's deploy page):
    ```$ heroku git:remote -a example-app```
    * By Heroku git URL ( URL can be obtained from the app's settings page on the Heroku):
    ```$ git remote add heroku <heroku-git-url>```
- Set environment variables:
    ```
    $ heroku config:set <key>=<value>
    ---
    $ heroku config:set SECRET_KEY=mysecretkey
    $ heroku config:set DATABASE_URL=<database_url>
    $ heroku config:set ENV=production
    $ heroku config:set FLASK_APP=run.py
    ```
- Commit all changes to Git
    ```$ git add .```
    ```$ git commit -m "Setup Heroku files for deployment"```
- Deploy to Heroku directly from CLI or connect to GitHub using Heroku UI:
    ```$ git push heroku master```

### Database Setup
- ##### Remote Setup (_ElephantSQL_)
- Create a new database in ElephantSQL (`Create new instance`)
- Give your plan Name (this is commonly the name of your application) and region (choose the closest region to you)
- Copy the database URL
- Paste the database URL in the Heroku Config Vars as `DATABASE_URL` or use the Heroku CLI:
    ```
    $ heroku config:set DATABASE_URL=<database_url>
    ```

- ##### Remote Migration
The remote migration process is the same as the local migration process, except that you need to run the commands on the Heroku server and don't need to use `flask db init` and `flask db migrate` if you gonna apply the same changes for the new DB.

To run the commands on the Heroku server, you need to use the Heroku CLI or the console on the Heroku UI app page and before the commands put the `heroku run` command. E.g.: `heroku run flask db upgrade --app <app_name>`

- Remote Database Migration
If you are using the same type of database for both local development and production (e.g., both are PostgreSQL), you can use migrations info from your local database that contained in the `migrations` folder. Push the migrations folder to the remote repository, and then apply the migrations to the remote database.

Just run the following commands on the Heroku server:
    ```
    $ heroku run bash --app taskmanager-flaskapp
    $ flask db upgrade
    $ exit
    ```
**Note:**_It works correctly if you initialized your local migrations using Flask-Migrate as it contains the table creation information. If you initialized your local migrations manually, you need to create the tables manually on the remote database._

- Remote Database Initialization
If you are going to use new different type of database you need to initialize the database on the remote server. Don't push the migrations folder to the remote repository. Just run the following commands on the Heroku server:
    ```
    $ heroku run <command>
    or
    $ heroku run <command> --app <app_name>
    ---
    $ heroku run bash --app taskmanager-flaskapp
    $ flask db init
    $ flask db migrate -m "Initial migration."
    $ flask db upgrade
    $ exit
    ```

## Credits
- The webapp build based on the [Code institute](https://codeinstitute.net/) walkthrough.
- Migration and Deployment process based on the Real Python and DigitalOcean tutorials and Heroku documentation.

Favicon taken from [icons8](https://icons8.com/)