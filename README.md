# Task Manager

This mini-project is a Relational Database Management System built using Flask, SQLAlchemy ORM, and a frontend framework Materialize.

The app allows to perform full CRUD (create, read, update, and delete) functionality on a database of tasks. All functionality is available through an HTML-based user interface. To provide a more user-friendly experience, the interface is styled using the Materialize which is a modern responsive front-end framework based off of Google's Material Design concept.


## Features


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

- ### App Configuration
1. Create environment variable for sensitive information and add it to the `<.gitignore>` file:
    ```
    $ touch env.py .gitignore
    $ echo env.py >> .gitignore
    ```
2. Set the environment variables in the `<env.py>` file:
    See the `example_env.py` file.
3. Make imports and set the configuration in the `__init__.py` file of the main Flask app package.
4. Create database (_PostgreSQL 14/Ubuntu 22.04_):
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

5. Local Migration

    - Initial setup

    _This method only for initial setup, it creates all the necessary tables in your database as defined by your SQLAlchemy models_
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
        $ flask db upgrade
        ```

6. Remote Migration
    https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/#remote-migration

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

## Credits