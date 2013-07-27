Python Web Programming
======================

.. image:: img/flask_cover.png
    :align: left
    :width: 50%

Session 6: A Flask Application

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


Where We Stand
--------------

We've moved quite a ways in implementing our microblog:

.. class:: incremental

* We've created code to initialize our database schema
* We've added functions to manage the lifecycle of our database connection
* We've put in place functions to write and read blog entries
* And, since it's tested, we are reasonably sure our code does what we think
  it does.

.. class:: incremental

We're ready now to put a face on it, so we can see what we're doing!


Templates In Flask
------------------

First, though, a detour into templates as they work in Flask

.. container:: incremental

    Jinja2 templates use the concept of an *Environment* to:
    
    .. class:: incremental
    
    * Figure out where to look for templates
    * Set configuration for the templating system
    * Add some commonly used functionality to the template *context*

.. class:: incremental

Flask sets up a proper Jinja2 Environment when you instantiate your ``app``.


Flask Environment
-----------------

Flask uses the value you pass to the ``app`` constructor to calculate the root
of your application on the filesystem.

.. class:: incremental

From that root, it expects to find templates in a directory name ``templates``

.. container:: incremental

    This allows you to use the ``render_template`` command from ``flask`` like
    so:
    
    .. code-block:: python
        :class: small
    
        from flask import render_template
        page_html = render_template('hello_world.html', name="Cris")


Flask Context
-------------

Keyword arguments you pass to ``render_template`` become the *context* passed
to the template for rendering.

.. class:: incremental

Flask will add a few things to this context.

.. class:: incremental

* **config**: contains the current configuration object
* **request**: contains the current request object
* **session**: any session data that might be available
* **g**: the request-local object to which global variables are bound
* **url_for**: so you can easily *reverse* urls from within your templates
* **get_flashed_messages**: a function that returns messages you flash to your
  users (more on this later).


Setting Up Our Templates
------------------------

In your ``microblog`` directory, add a new ``templates`` directory

.. container:: incremental

    In this directory create a new file ``layout.html``

    .. code-block:: jinja
        :class: small
    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Microblog!</title>
          </head>
          <body>
            <h1>My Microblog</h1>
            <div class="content">
            {% block body %}{% endblock %}
            </div>
          </body>
        </html>

Template Inheritance
--------------------

You can combine templates in a number of different ways.

.. class:: incremental

* you can make replaceable blocks in templates with blocks

  * ``{% block foo %}{% endblock %}``

* you can build on a template in a second template by extending

  * ``{% extends "layout.html" %}`` 
  * this *must* be the first text in the template

* you can re-use common structure with *include*:

  * ``{% include "footer.html" %}``


Template Inheritance
--------------------

You can even build libraries of template *macros* and import them:

.. code-block:: jinja
    :class: small incremental

    {% macro input(label, name='input', value='', type='text') -%}
        <label>{{ label }}
        <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}"/>
        </label>
    {%- endmacro %}

.. code-block:: jinja
    :class: small incremental
    
    {% import "forms.html" as forms %}
    <form id="user_login" action="" method="POST">
        {{ forms.input("Username", name="username") }}
        {{ forms.input("Password", name="password" type="password") }}
        {{ forms.input("", type="submit" name="submit" value="Log in") }}
    </form>


Displaying an Entries List
--------------------------

Create a new file, ``show_entries.html`` in ``templates``:

.. code-block:: jinja
    :class: small

    {% extends "layout.html" %}
    {% block body %}
      <h2>Posts</h2>
      <ul class="entries">
      {% for entry in entries %}
        <li>
          <h2>{{ entry.title }}</h2>
          <div class="entry_body">
          {{ entry.text|safe }}
          </div>
        </li>
      {% else %}
        <li><em>No entries here so far</em></li>
      {% endfor %}
      </ul>
    {% endblock %}


Viewing Entries
---------------

We just need a Python function that will: 

.. class:: incremental

* build a list of entries
* pass the list to our template to be rendered
* return the result to a client's browser

.. class:: incremental

As usual, we'll start by writing tests for this new function


Test Viewing Entries
--------------------

Add the following two tests to ``microblog_tests.py``:

.. code-block:: python
    :class: small

    def test_empty_listing(self):
        response = self.client.get('/')
        assert 'No entries here so far' in response.data

    def test_listing(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            microblog.write_entry(*expected)
        response = self.client.get('/')
        for value in expected:
            assert value in response.data

.. class:: incremental

``app.test_client()`` creates a mock http client for us.


Run Your Tests
--------------

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    .F..F.
    ======================================================================
    FAIL: test_empty_listing (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 55, in test_empty_listing
        assert 'No entries here so far' in response.data
    AssertionError
    ======================================================================
    FAIL: test_listing (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 63, in test_listing
        assert value in response.data
    AssertionError
    ----------------------------------------------------------------------
    Ran 6 tests in 0.138s

    FAILED (failures=2)


Make Them Pass
--------------

In ``microblog.py``:

.. code-block:: python
    :class: small

    # at the top, import
    from flask import render_template

    # and after our last functions:
    @app.route('/')
    def show_entries():
        entries = get_all_entries()
        return render_template('show_entries.html', entries=entries)

.. class:: incremental small

::

    (flaskenv)$ python microblog_tests.py
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.100s

    OK


Authentication
--------------

We don't want just anyone to be able to add new entries. So we want to be able
to authenticate a user.

.. class:: incremental

Flask provides *session* concept as a way to store and access data for a given
client.

.. class:: incremental

The session in Flask uses encrypted HTTP *Cookies*

.. class:: incremental

We will require a few changes to our app configuration to use this session.


Additional Config
-----------------

In ``microblog.cfg`` add the following lines:

.. code-block:: python
    :class: small

    SECRET_KEY = "sooperseekritvaluenooneshouldknow"
    USERNAME = "admin"
    PASSWORD = "secret"

.. class:: incremental

``SECRET_KEY`` is a value that will be used to encrypt the session cookie. If
it isn't set, sessions won't be created.

.. class:: incremental

``USERNAME`` and ``PASSWORD`` are our admin credentials.  

.. class:: small center incremental

obviously this is not a robust login system, do not do this in real life


Test Authentication
-------------------

Back in ``microblog_tests.py`` add new test methods:

.. code-block:: python
    :class: small
    
    # up with the imports
    from flask import session

    # at the end of our list of test methods
    def test_login_passes(self):
        with self.app.test_request_context('/'):
            microblog.do_login(microblog.app.config['USERNAME'],
                               microblog.app.config['PASSWORD'])
            self.assertTrue(session.get('logged_in', False))

    def test_login_fails(self):
        with self.app.test_request_context('/'):
            self.assertRaises(ValueError, 
                              microblog.do_login,
                              microblog.app.config['USERNAME'],
                              'incorrectpassword')


Run Your Tests
--------------

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    .....EE.
    ======================================================================
    ERROR: test_login_fails (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 76, in test_login_fails
        microblog.do_login,
    AttributeError: 'module' object has no attribute 'do_login'
    ======================================================================
    ERROR: test_login_passes (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 69, in test_login_passes
        microblog.do_login(microblog.app.config['USERNAME'],
    AttributeError: 'module' object has no attribute 'do_login'
    ----------------------------------------------------------------------
    Ran 8 tests in 0.082s

    FAILED (errors=2)


Make Them Pass
--------------

In ``microblog.py``:

.. code-block:: python
    :class: small

    # add an import
    from flask import session

    # and a function
    def do_login(usr, pwd):
        if usr != app.config['USERNAME']:
            raise ValueError
        elif pwd != app.config['PASSWORD']:
            raise ValueError
        else:
            session['logged_in'] = True

.. class:: incremental

Re-run your tests, you should now be 8 for 8


Creating Login/Logout
---------------------

We need to have the ability to log in and out of our application.

.. container:: incremental

    This means we need views that will
    
    .. class:: incremental
    
    * Allow a user to provide credentials and attempt to login
    * Redirect to the listing page if they succeed
    * Give appropriate feedback if they fail
    * Allow a user to log out if they are logged in
    * Redirect to the listing page after logging out

.. class:: incremental

Let's begin as usual by writing some tests


Helper Methods in Tests
-----------------------

We will need to log in or out a few times in our test.

.. container:: incremental

    Add helper methods to our ``microblog_tests.py`` TestCase:

    .. code-block:: python
        :class: small

        def login(self, username, password):
            return self.client.post('/login', data=dict(
                username=username,
                password=password
            ), follow_redirects=True)

        def logout(self):
            return self.client.get('/logout',
                                   follow_redirects=True)

.. class:: incremental small

**Note:** Methods that do not begin with ``test`` will not be run as tests.


Testing Login/Logout
--------------------

And now the test itself:

.. code-block:: python
    :class: small

    def test_login_logout(self):
        # verify we can log in
        response = self.login('admin', 'secret')
        assert 'You were logged in' in response.data
        # verify we can log back out
        response = self.logout()
        assert 'You were logged out' in response.data
        # verify that incorrect credentials get a proper message
        response = self.login('notadmin', 'secret')
        assert 'Invalid Login' in response.data
        response = self.login('admin', 'notsosecret')
        assert 'Invalid Login' in response.data


Run Your Tests
--------------

You should now have nine tests, with one failure:

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    ......F..
    ======================================================================
    FAIL: test_login_logout (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 93, in test_login_logout
        assert 'You were logged in' in response.data
    AssertionError

    ----------------------------------------------------------------------
    Ran 9 tests in 0.047s

    FAILED (failures=1)


Login Form Template
-------------------

Add ``login.html`` to the ``templates`` directory:

.. code-block: jinja
    :class: tiny

    {% extends "layout.html" %}
    {% block body %}
      <h2>Login</h2>
      {% if error -%}
        <p class="error"><strong>Error</strong> {{ error }}
      {%- endif %}
      <form action="{{ url_for('login') }}" method="POST">
        <div class="field">
          <label for="username">Username</label>
          <input type="text" name="username" id="username"/>
        </div>
        <div class="field">
          <label for="password">Password</label>
          <input type="password" name="password" id="password"/>
        </div>
        <div class="control_row">
          <input type="submit" name="Login" value="Login"/>
        </div>
      </form>
    {% endblock %}


Required Imports
----------------

Back in ``microblog.py``, we need to import some symbols from flask:

.. code-block:: python

    # at the top, new imports
    from flask import request
    from flask import redirect
    from flask import flash
    from flask import url_for

.. class:: incremental

And finally, we'll add the view functions we need to fix our tests


Make the Test Pass
------------------

.. code-block:: python
    :class: small

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            try:
                do_login(request.form['username'],
                         request.form['password'])
            except ValueError:
                error = "Invalid Login"
            else:
                flash('You were logged in')
                return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)

    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('show_entries'))


About Flash
-----------

.. class:: small

``flash`` allows sending messages to clients. We need a place to show these
messages. Add it to ``layout.html`` (along with links to log in and out)

.. code-block:: jinja
    :class: small

    <h1>My Microblog</h1>       <!-- already there -->
    <div class="metanav"> <!-- add all this -->
    {% if not session.logged_in %}
      <a href="{{ url_for('login') }}">log in</a>
    {% else %}
      <a href="{{ url_for('logout') }}">log_out</a>
    {% endif %}
    </div>
    {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
    {% endfor %}
    <div class="content"> <!-- already there -->


Nine For Nine
-------------

At this point, we are displaying the messages we sent from the view code, so
our tests should pass:

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    .........
    ----------------------------------------------------------------------
    Ran 9 tests in 0.064s

    OK


Creating Entries
----------------

We still lack a way to add an entry. We need a view that will:

.. class:: incremental

* Verify that the user is authenticated
* Accept incoming form data from a request
* Get the data for ``title`` and ``text``
* Create a new entry in the database
* Provide feedback to the user on success or failure

.. class:: incremental

Again, first come the tests.


Testing Add an Entry
--------------------

Add this to ``microblog_tests.py``:

.. code-block:: python
    :class: small

    def test_add_entries(self):
        self.login('admin', 'secret')
        response = self.client.post('/add', data=dict(
            title='Hello',
            text='This is a post'
        ), follow_redirects=True)
        assert 'No entries here so far' not in response.data
        assert 'Hello' in response.data
        assert 'This is a post' in response.data


Run Your Tests
--------------

Verify that our test fails as expected:

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    F.........
    ======================================================================
    FAIL: test_add_entries (__main__.MicroblogTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "microblog_tests.py", line 110, in test_add_entries
        assert 'Hello' in response.data
    AssertionError

    ----------------------------------------------------------------------
    Ran 10 tests in 0.071s

    FAILED (failures=1)


Make Them Pass
--------------

We have all we need to write entries, all we lack is an endpoint (in
``microblog.py``):

.. code-block:: python
    :class: small

    # add an import
    from flask import abort

    @app.route('/add', methods=['POST'])
    def add_entry():
        if not session.get('logged_in'):
            abort(401)
        try:
            write_entry(request.form['title'], request.form['text'])
            flash('New entry was successfully posted')
        except sqlite3.Error as e:
            flash('There was an error: %s' % e.args[0])
        return redirect(url_for('show_entries'))


And...?
-------

.. class:: small

::

    (flaskenv)$ python microblog_tests.py
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.075s

    OK

.. class:: incremental center

**Hooray!**


Where do Entries Come From
--------------------------

Finally, we're almost done. We can log in and log out. We can add entries and
view them. But look at that last view. Do you see a call to
``render_template`` in there at all?

.. class:: incremental

There isn't one. That's because that view is never meant to be be visible.
Look carefully at the logic. What happens?

.. class:: incremental

So where do the form values come from?

.. class:: incremental

Let's add a form to the main view.  Open ``show_entries.html``


Provide a Form
--------------

.. code-block:: jinja
    :class: small

    {% block body %}  <!-- already there -->
    {% if session.logged_in %}
    <form action="{{ url_for('add_entry') }}" method="POST" class="add_entry">
      <div class="field">
        <label for="title">Title</label>
        <input type="text" size="30" name="title" id="title"/>
      </div>
      <div class="field">
        <label for="text">Text</label>
        <textarea name="text" id="text" rows="5" cols="80"></textarea>
      </div>
      <div class="control_row">
        <input type="submit" value="Share" name="Share"/>
      </div>
    </form>
    {% endif %}
    <h2>Posts</h2>  <!-- already there -->


All Done
--------

Okay.  That's it.  We've got an app all written.

.. class:: incremental

So far, we haven't actually touched our browsers at all, but we have
reasonable certainty that this works because of our tests. Let's try it.


.. class:: incremental

In the terminal where you've been running tests, run our microblog app:

.. class:: incremental

::

    (flaskenv)$ python microblog.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader


The Big Payoff
--------------

Now load ``http://localhost:5000/`` in your browser and enjoy your reward.


Making It Pretty
----------------

What we've got here is pretty ugly.

.. class:: incremental

If you've fallen behind, or want to start fresh, you can find the finished
``microblog`` directory in the class resources.

.. class:: incremental

In that directory inside the ``static`` directory you will find
``styles.css``. Open it in your editor.  It contains basic CSS for this app.

.. class:: incremental

We'll need to include this file in our ``layout.html``.


Static Files
------------

Like page templates, Flask locates static resources like images, css and
javascript by looking for a ``static`` directory relative to the app root.

.. class:: incremental

You can use the special url endpoint ``static`` to build urls that point here.
Open ``layout.html`` and add the following:

.. code-block:: jinja
    :class: small incremental

    <head>  <!-- you only need to add the <link> below -->
      <title>Flaskr</title>
      <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet" type="text/css">
    </head>


Going Further
-------------

It's not too hard to see ways you could improve this.

.. class:: incremental

* For my part, I made a version with styles from Bootstrap.js.
* You could limit the number of posts shown on the front page and add
  pagination.
* You could add *created date* to the entry schema and provide archived views
  for older posts.
* You could add the ability to edit existing posts (and add a modified date to
  the schema)
* You could support multi-user blogging by providing a more complex
  authentication system and some more views.


Wrap-Up
-------

For educational purposes you might try taking a look at the source code for
Flask and Werkzeug.  Neither is too large a package.  

.. class:: incremental

In particular seeing how Werkzeug sets up a Request and Response--and how
these relate to the WSGI specification--can be very enlightening.

.. class:: incremental center

**See You Tomorrow!**
