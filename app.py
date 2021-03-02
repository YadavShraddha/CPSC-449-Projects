# Name - Shraddha Yadav [CWID - 887352110]
# Email - shraddhayadav@csu.fullerton.edu
# CPSC 449 Project - 2


# Add custom command init to create and populate the test database

import click
import sqlite3
from flask import Flask
from flask import g
import time

app = Flask(__name__)

DATABASE = './users_887352110.db'

@app.cli.command("init")
def init():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db