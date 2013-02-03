import sqlite3
from contextlib import closing

from flask import Flask
from flask import g


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


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    g.db.close()


def write_entry(title, text):
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [title, text])
    g.db.commit()


def get_all_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return entries


if __name__ == '__main__':
    app.run(debug=True)
