import os

# ip and port of the flask local server
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")

os.environ.setdefault("SECRET_KEY", "my_secret_key")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")

# postgresql represents the database type and taskmanager is the name of the database,
# /// means that the database is local within the workspace
os.environ.setdefault("DB_URL", "postgresql:///taskmanager")
