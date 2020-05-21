from flask import Flask
from utils.database import db, migrate
from apps.endpoints import api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

"""Initializing plugins"""
db.init_app(app)
migrate.init_app(app, db)
api.init_app(app)

if __name__ == '__main__':
    app.run()

