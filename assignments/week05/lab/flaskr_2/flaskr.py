import sqlite3
from contextlib import closing

from flask import Flask


# configuration goes here
DATABASE = '/tmp/flaskr.db'
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


if __name__ == '__main__':
    app.run(debug=True)
