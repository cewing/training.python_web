Python Web Programming
======================

.. image:: img/flask_cover.png
    :align: left
    :width: 50%

Day 3 PM: A Flask Application

.. class:: intro-blurb right

| "Web Development,
| one drop at a time"

.. class:: image-credit

image: Flask Logo (http://flask.pocoo.org/community/logos/)


A Quick Reminder
----------------

In our last session we set up a virtualenv in which we have installed the
microframework Flask

.. class:: incremental

We spent a few minutes exploring how Flask works, and how it is similar to the
wsgi app we wrote ourselves.

.. class:: incremental

We then took a detour to introduce ``Jinja2``, the templating language Flask
uses out of the box.

.. class:: incremental

Finally, we learned about the Python DB API 2 by seeing how we can set up a
sqlite3 database and work with it safely.


Moving On
---------

Now it is time to put all that together.

.. class:: incremental

We'll spend this session building a "microblog" application.

.. class:: incremental

Let's dive right in.

.. class:: incremental

Start by activating your Flask virtualenv


Our Database
------------

We need first to define what an *entry* for our microblog might look like.

.. class:: incremental

Let's keep it a simple as possible for now.

.. class:: incremental

Create a new directory ``microblog``, and open a new file in it:
``schema.sql``

.. code-block:: sql
    :class: incremental small

    drop table if exists entries;
    create table entries (
        id integer primary key autoincrement,
        title string not null,
        text string not null
    );


App Configuration
-----------------

For any but the most trivial applications, you'll need some configuration.

.. class:: incremental

Flask provides a number of ways of loading configuration.  We'll be using a
config file

.. class:: incremental

Create a new file ``microblog.cfg`` in the same directory.  

.. code-block:: python
    :class: small incremental
    
    # application configuration for a Flask microblog
    DATABASE = 'microblog.db'


Our App Skeleton
----------------

Finally, we'll need a basic app skeleton to work from.

.. class:: incremental

Create one more file ``microblog.py`` in the same directory, and enter the
following:

.. code-block:: python
    :class: small incremental

    from flask import Flask

    app = Flask(__name__)

    app.config.from_pyfile('microblog.cfg')

    if __name__ == '__main__':
        app.run(debug=True)


Test Your Work
--------------

This is enough to get us off the ground.

.. container:: incremental

    From a terminal in the ``microblog`` directory, run the app:
    
    .. class:: small
    
    ::

        (flaskenv)$ python microblog.py
        * Running on http://127.0.0.1:5000/
        * Restarting with reloader

.. class:: incremental

Then point your browser at http://localhost:5000/

.. class:: incremental

What do you see in your browser?  In the terminal?  Why?


Creating the Database
---------------------

Quit the app with ``^C``. Then return to ``microblog.py`` and add the
following:

.. code-block:: python
    :class: incremental small

    # add this up at the top
    import sqlite3

    # add the rest of this below the app.config statement
    def connect_db():
        return sqlite3.connect(app.config['DATABASE'])

.. class:: incremental

This should look familiar. What will happen?

.. class:: incremental

This convenience method allows us to write our very first test.


Tests and TDD
-------------

.. class:: center

**If it isn't tested, it's broken**

.. class:: incremental

Test-Driven Development means writing the tests before writing the code.
As your tests pass, you know you're building what you want.

.. class:: incremental

We are going to write tests at every step of this exercise using the
``unittest`` module.

.. class:: incremental

You'll want to read more about this module. See the reading list for
suggestions.


Testing Envrionment
-------------------

The Python ``unittest`` module defines a class called a ``TestCase``. It
serves as a container for a set of tests and the code needed to run them.

.. class:: incremental

This class provides ``setUp`` and ``tearDown`` methods to control the
environment for each test.

.. class:: incremental

These methods are run before and after *each test*, and may be used to provide
*isolation* between tests.

.. class:: incremental

Create a ``microblog_tests.py`` file.  Open it in your editor


Testing Setup
-------------

Add the following to provide minimal test setup.

.. code-block:: python
    :class: small

    import os
    import tempfile
    import unittest
    
    import microblog

    class MicroblogTestCase(unittest.TestCase):

        def setUp(self):
            db_fd = tempfile.mkstemp()
            self.db_fd, microblog.app.config['DATABASE'] = db_fd
            microblog.app.config['TESTING'] = True
            self.client = microblog.app.test_client()
            self.app = microblog.app


Testing Teardown
----------------

Add this method to your test case class to tear down after each test:

.. code-block:: python

    class MicroblogTestCase(unittest.TestCase):
        # ...

        def tearDown(self):
            os.close(self.db_fd)
            os.unlink(microblog.app.config['DATABASE'])


Make Tests Runnable
-------------------

To make the test module runnable, we need a ``__main__`` block.

.. class:: incremental

Calling the ``unittest.main()`` function here will find test cases and run
their tests.

.. container:: incremental

    Add the following at the end of ``microblog_tests.py``:

    .. code-block:: python
        :class: small

        if __name__ == '__main__':
            unittest.main()

.. class:: incremental

Now, we're ready to add our first actual test..

Test Databse Setup
------------------

We'd like to test that our database is correctly initialized. The schema has
one table with three columns. Let's test that.

.. container:: incremental

    Add the following method to your test class in ``microblog_tests.py``:

    .. code-block:: python
        :class: small

        def test_database_setup(self):
            con = microblog.connect_db()
            cur = con.execute('PRAGMA table_info(entries);')
            rows = cur.fetchall()
            self.assertEquals(len(rows), 3)


Run the Tests
-------------

We can now run our test module:

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    F
    ======================================================================
    FAIL: test_database_setup (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 23, in test_database_setup
        self.assertEquals(len(rows) == 3)
    AssertionError: 0 != 3

    ----------------------------------------------------------------------
    Ran 1 test in 0.011s

    FAILED (failures=1)


Make the Test Pass
------------------

This is an expected failure. Why?

.. container:: incremental

    Let's add some code to ``microblog.py`` that will actually create our
    database schema:

    .. code-block:: python
        :class: small

        # add this import at the top
        from contextlib import closing

        # add this function after the connect_db function
        def init_db():
            with closing(connect_db()) as db:
                with app.open_resource('schema.sql') as f:
                    db.cursor().executescript(f.read())
                db.commit()


Initialize the DB in Tests
--------------------------

We also need to call that function in our ``microblog_tests.py`` to set up the
database schema for each test.

.. container:: incremental

    Add the following line at the end of that ``setUp`` method:

    .. code-block:: python
        :class: small

        def setUp(self):
            # ...
            microblog.init_db() # <- add this at the end

.. class:: incremental

::

    (flaskenv)$ python microblog_tests.py


Success?
--------

.. class:: big-centered incremental

 \\o/ Wahoooo!


Initialize the DB IRL
---------------------

Our test passed, so we have confidence that ``init_db`` does what it should

.. class:: incremental

We'll need to have a working database for our app, so let's go ahead and do
this "in real life"

.. class:: incremental

    (flaskenv)$ python

.. code-block:: python
    :class: incremental

    >>> import microblog
    >>> microblog.init_db()
    >>> ^D


Reading and Writing Data
------------------------

After you quit the interpreter, you should see ``microblog.db`` in your 
directory.

.. class:: incremental

It's time now to think about writing and reading data for our blog.

.. class:: incremental

We'll start by writing tests.

.. class:: incremental

But first, a word or two about the circle of life.


The Request/Response Cycle
--------------------------

Every interaction in HTTP is bounded by the interchange of one request and one
response.

.. class:: incremental

No HTTP application can do anything until some client makes a request.

.. class:: incremental

And no action by an application is complete until a response has been sent
back to the client.

.. class:: incremental

This is the lifecycle of an http web application.


Managing DB Connections
-----------------------

It makes sense to bind the lifecycle of a database connection to this same
border.

.. class:: incremental

Flask does not dictate that we write an application that uses a database.

.. class:: incremental

Because of this, managing the lifecycle of database connection so that they
are connected to the request/response cycle is up to us.

.. class:: incremental

Happily, Flask *does* have a way to help us.


Request Boundary Decorators
---------------------------

The Flask *app* provides decorators we can use on our database lifecycle
functions:

.. class:: incremental

* ``@app.before_request``: any method decorated by this will be called before
  the cycle begins

* ``@app.after_request``: any method decorated by this will be called after
  the cycle is complete. If an unhandled exception occurs, these functions are
  skipped.

* ``@app.teardown_request``: any method decorated by this will be called at
  the end of the cycle, *even if* an unhandled exception occurs.


Managing our DB
---------------

Think about the following functions:

.. code-block:: python
    :class: small

    def get_database_connection():
        db = connect_db()
        return db

    @app.teardown_request
    def teardown_request(exception):
        db.close()

.. class:: incremental

How does the ``db`` object get from one place to the other?


Global Context in Flask
-----------------------

Our flask ``app`` is only really instantiated once

.. class:: incremental

This means that anything we tie to it will be shared across all requests.

.. class:: incremental

This is what we call ``global`` context.

.. class:: incremental

What happens if two clients make a request at the same time?


Local Context in Flask
----------------------

Flask provides something it calls a ``local global``: "g".

.. class:: incremental

This is an object that *looks* global (you can import it anywhere)

.. class:: incremental

But in reality, it is *local* to a single request.

.. class:: incremental

Resources tied to this object are *not* shared among requests. Perfect for
things like a database connection.


Working DB Functions
--------------------

Add the following, working methods to ``microblog.py``:

.. code-block:: python
    :class: small

    # add this import at the top:
    from flask import g

    # add these function after init_db
    def get_database_connection():
        db = getattr(g, 'db', None)
        if db is None:
            g.db = db = connect_db()
        return db

    @app.teardown_request
    def teardown_request(exception):
        db = getattr(g, 'db', None)
        if db is not None:
            db.close()


Writing Blog Entries
--------------------

Our microblog will have *entries*. We've set up a simple database schema to
represent them.

.. class:: incremental

To write an entry, what would we need to do?

.. class:: incremental

* Provide a title
* Provide some body text
* Write them to a row in the database

.. class:: incremental

Let's write a test of a function that would do that.


Test Writing Entries
--------------------

The database connection is bound by a request. We'll need to mock one (in
``microblog_tests.py``)

.. container:: incremental

    Flask provides ``app.test_request_context`` to do just that

    .. code-block:: python
        :class: small

        def test_write_entry(self):
            expected = ("My Title", "My Text")
            with self.app.test_request_context('/'):
                microblog.write_entry(*expected)
                con = microblog.connect_db()
                cur = con.execute("select * from entries;")
                rows = cur.fetchall()
            self.assertEquals(len(rows), 1)
            for val in expected:
                self.assertTrue(val in rows[0])


Run Your Test
-------------

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    .E
    ======================================================================
    ERROR: test_write_entry (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 30, in test_write_entry
        microblog.write_entry(*expected)
    AttributeError: 'module' object has no attribute 'write_entry'

    ----------------------------------------------------------------------
    Ran 2 tests in 0.018s

    FAILED (errors=1)

.. class:: incremental

Great.  Two tests, one passing.


Make It Pass
------------

Now we are ready to write an entry to our database. Add this function to
``microblog.py``:

.. code-block:: python
    :class: small incremental

    def write_entry(title, text):
        con = get_database_connection()
        con.execute('insert into entries (title, text) values (?, ?)',
                     [title, text])
        con.commit()

.. class:: incremental small

::

    (flaskenv)$ python microblog_tests.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.146s

    OK


Reading Entries
---------------

We'd also like to be able to read the entries in our blog

.. container:: incremental

    We need a method that returns all of them for a listing page

    .. class:: incremental

    * The return value should be a list of entries
    * If there are none, it should return an empty list
    * Each entry in the list should be a dictionary of 'title' and 'text'

.. class:: incremental

Let's begin by writing tests.


Test Reading Entries
--------------------

In ``microblog_tests.py``:

.. code-block:: python
    :class: small

    def test_get_all_entries_empty(self):
        with self.app.test_request_context('/'):
            entries = microblog.get_all_entries()
            self.assertEquals(len(entries), 0)

    def test_get_all_entries(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            microblog.write_entry(*expected)
            entries = microblog.get_all_entries()
            self.assertEquals(len(entries), 1)
            for entry in entries:
                self.assertEquals(expected[0], entry['title'])
                self.assertEquals(expected[1], entry['text'])


Run Your Tests
--------------

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    .EE.
    ======================================================================
    ERROR: test_get_all_entries (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 47, in test_get_all_entries
        entries = microblog.get_all_entries()
    AttributeError: 'module' object has no attribute 'get_all_entries'

    ======================================================================
    ERROR: test_get_all_entries_empty (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 40, in test_get_all_entries_empty
        entries = microblog.get_all_entries()
    AttributeError: 'module' object has no attribute 'get_all_entries'

    ----------------------------------------------------------------------
    Ran 4 tests in 0.021s

    FAILED (errors=2)

Make Them Pass
--------------

Now we have 4 tests, and two fail, add this function to ``microblog.py``:

.. code-block:: python
    :class: small

    def get_all_entries():
        con = get_database_connection()
        cur = con.execute('SELECT title, text FROM entries ORDER BY id DESC')
        return [dict(title=row[0], text=row[1]) for row in cur.fetchall()]

.. container:: incremental small

    And back in your terminal:
    
    .. class:: small
    
    ::

        (flaskenv)$ python microblog_tests.py
        ....
        ----------------------------------------------------------------------
        Ran 4 tests in 0.021s

        OK
