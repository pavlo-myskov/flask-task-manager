# Task Manager

This mini-project is a Relational Database Management System built using Flask, SQLAlchemy ORM, and a frontend framework Materialize.

The app allows to perform full CRUD (create, read, update, and delete) functionality on a database of tasks. All functionality is available through an HTML-based user interface. To provide a more user-friendly experience, the interface is styled using the Materialize which is a modern responsive front-end framework based off of Google's Material Design concept.


## Features


## Technologies Used
- [Materialize](https://materializecss.com/getting-started.html) - front-end framework based on Material Design
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - micro web framework written in Python
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for the Python programming language
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Flask extension that adds support for SQLAlchemy to your Flask application


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
    - Create tables using the SQLAlchemy ORM in the `models.py` file
5. Migrations
    - Simple initial migration
    (_this method good for initial setup, but not for later updates_):
        ```
        $ flask --app run.py shell
        >>> from app import db
        >>> db.create_all()
        >>> exit()
        ```
    - Migration with Flask-Migrate
        ...

    - Check the dt table in the database:
    ```
    # psql <database name>
    # \dt
    ```
    Note: _If you modify the models later, you need to migrate the changes each time the file is updated with new context_

- ### Materialize
The easiest way to work with [Materialize](https://materializecss.com/getting-started.html) is to use the CDN (Content Delivery Network) version of the framework. To do this, add the following line to the `<head>` section of your HTML file:
```
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