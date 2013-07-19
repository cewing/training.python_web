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

 \o/ Wahoooo!