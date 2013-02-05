Internet Programming with Python
================================

.. image:: img/bike.jpg
    :align: left
    :width: 50%

Week 5: Small Frameworks

.. class:: intro-blurb right

| "Reinventing the wheel is great
| if your goal is to learn more about the wheel"
|
| -- James Tauber, PyCon 2007

.. class:: image-credit

image: Britanglishman http://www.flickr.com/photos/britanglishman/5999131365/ - CC-BY

But First
---------

.. class:: big-centered

Review from the Assignment

URL Mapping
-----------

Two basic approaches to solving the problem::

    /books?id=id1
    /books/id1

.. class:: incremental

The first generally used ``environ['QUERY_STRING']``. The second used
``environ['PATH_INFO']``

.. class:: incremental

Both are fine. Largely a matter of taste. I find the latter more common in
daily work.

Regular Expressions
-------------------

My personal approach to the url mapping problem was the second, which relies
on regular expression mapping:

.. code-block:: python

    URLS = [(r'^$', 'books'),
            (r'^book/(id[\d]{1,2})$', 'book'), ]

.. class:: incremental

Regular expressions should be as tight as possible, it's easy to over-match

.. class:: incremental

Read the `Python Regexp How-to <http://docs.python.org/2.6/howto/regex.html>`_
and find a good `Regular Expression Tester <http://www.pythonregex.com/>`_

String Formatting
-----------------

This is awkward:

.. code-block:: python

    bob = {'a': 'things', 'b': 'stuff'}
    "I have lots of " + bob['a'] + " and " + bob['b'] + "."

.. class:: incremental

This is much less so:

.. code-block:: python
    :class: incremental

    bob = {'a': 'things', 'b': 'stuff'}
    "I have lots of %(a)s and %(b)s." % bob

.. class:: incremental

I am chastened.  string.format() is the best (most flexible)

WSGIScriptAlias
---------------

CGI required a cgi directory.  WSGI makes no such requirement.

.. class:: incremental

You can use WSGIScriptAlias to point to a single file

.. class:: incremental

Since a single file can often provide the entry point to an entire app, this
allows you to mount entire apps at arbitrary path locations:

.. class:: incremental

::

    WSGIScriptAlias / /path/to/main/app/wsgi_app.py
    WSGIScriptAlias /blog /path/to/blog/app/wsgi_app.py
    WSGIScriptAlias /forum /path/to/forum/app/wsgi_app.py

Bad HTML
--------

I know that web browsers are forgiving, but you should be less so.

These are *not* good HTML::

    <p><a href = /book/id4 >foobar</p>
    <P><A HREF='/book/id4'>foobar</A></P>

.. class:: incremental

This is: `<p><a href="/book/id4">foobar</a></p>`

.. class:: incremental

The `Mozilla Developer Network
<https://developer.mozilla.org/en-US/docs/HTML>`_ is a great resource for
proper HTML. It also has great reference information on JavaScript. Shun the
`w3schools`.

And Second
----------

.. class:: big-centered

Questions from the Reading?

And Third
---------

.. class:: center incremental

**Class Project**

.. class:: incremental

* Create a Website
* It can do anything you want it to. 
* It should have some user interactions (forms users complete).
* It should look nice-ish
* It should show off some aspect of what you've learned
* It should take you about 15-20 hours to create (so small)
* It will be due on the last day of class (March 10)
* We will spend half of each of the last two class session working on it in
  class.
* **Questions?**

And Now...
----------

.. class:: big-centered

Small Frameworks

A Moment to Reflect
-------------------

We've been at this for a while now.  We've learned a great deal:

.. class:: incremental

* Sockets, the TCP/IP Stack and Basic Mechanics
* Web Protocols and the Importance of Clear Communication
* APIs and Consuming Data from The Web
* CGI and WSGI and Getting Information to Your Dynamic Applications

.. class:: incremental

This concludes the foundational part of the course.

.. class:: incremental

Everything we do from here out will be based on tools built using what we've
learned these first four weeks.

We've built
-----------

.. class:: big-centered

A full-featured web server

We've built
-----------

.. class:: big-centered

Data-driven applications using web-based APIs

We've built
-----------

.. class:: big-centered

CGI web pages

We've built
-----------

.. class:: big-centered

A simple wsgi application

Onward
------

.. class:: big-centered

We are moving up the stack

From Now On
-----------

Think of everything we do as sitting on top of WSGI

.. class:: incremental

This may not *actually* be true

.. class:: incremental

But we will always be working at that level of abstraction.

The Abstraction Stack
---------------------

You can think of the libraries we use to write web applications as belonging
to one of several levels:

.. class:: incremental center

plumbing

.. class:: incremental center

tools

.. class:: incremental center

small frameworks

.. class:: incremental center

full-stack frameworks

.. class:: incremental center

systems

Plumbing
--------

We've done this part already:

.. class:: center

Sockets

.. class:: center

Protocols

.. class:: center

CGI/WSGI

Tools
-----

We've started to talk about these, we'll see more soon:

.. class:: center

cgitb

.. class:: center

wsgi middleware

.. class:: center

werkzeug tools

.. class:: center

WebOb

Small Frameworks
----------------

We're here today:

.. class:: center

Flask

.. class:: center

Bottle

.. class:: center

CherryPy

.. class:: center

Web.py

.. class:: center

and many many more...

Full Stack Frameworks
---------------------

We will visit this level next:

.. class:: center

Django

.. class:: center

Pyramid

.. class:: center

web2py

Systems
-------

We'll finish up here

.. class:: center

Plone


Frameworks
----------

From Wikipedia:

.. class:: center incremental

A web application framework (WAF) is a software framework that is designed to
support the development of dynamic websites, web applications and web
services. The framework aims to alleviate the overhead associated with common
activities performed in Web development. For example, many frameworks provide
libraries for database access, templating frameworks and session management,
and they often promote code reuse

What Does That *Mean*?
----------------------

You use a framework to build an application.

.. class:: incremental

A framework allows you to build different kinds of applications.

.. class:: incremental

A framework abstracts what needs to be abstracted, and allows control of the
rest.

.. class:: incremental

Think back over the last four weeks. What were your pain points? Which bits do
you wish you didn't have to think about?

Level of Abstraction
--------------------

This last part is important when it comes to choosing a framework

.. class:: incremental

* abstraction ∝ 1/freedom
* The more they choose, the less you can
* *Every* framework makes choices in what to abstract
* *Every* framework makes *different* choices

Python Web Frameworks
---------------------

There are scores of 'em (this is a partial list).

.. class:: incremental invisible small center

========= ======== ======== ========== ==============
Django    Grok     Pylons   TurboGears web2py
Zope      CubicWeb Enamel   Gizmo(QP)  Glashammer
Karrigell Nagare   notmm    Porcupine  QP
SkunkWeb  Spyce    Tipfy    Tornado    WebCore
web.py    Webware  Werkzeug WHIFF      XPRESS
AppWsgi   Bobo     Bo7le    CherryPy   circuits.web
Paste     PyWebLib WebStack Albatross  Aquarium
Divmod    Nevow    Flask    JOTWeb2    Python Servlet
Engine    Pyramid  Quixote  Spiked     weblayer
========= ======== ======== ========== ==============

Choosing a Framework
--------------------

Many folks will tell you "<XYZ> is the **best** framework".

.. class:: incremental

In most cases, what they really mean is "I know how to use <XYZ>"

.. class:: incremental

In some cases, what they really mean is "<XYZ> fits my brain the best"

.. class:: incremental

What they usually forget is that everyone's brain (and everyone's use-case) is
different.

Cris' First Law of Frameworks
-----------------------------

.. class:: center

**Pick the Right Tool for the Job**

.. class:: incremental

First Corollary

.. class:: incremental center

The right tool is the tool that allows you to finish the job quickly and
correctly.

.. class:: incremental center

But how do you know which that one is?

Cris' Second Law of Frameworks
------------------------------

.. class:: big-centered

You can't know unless you try

.. class:: incremental center

so let's try

Preparation
-----------

We proceed under the assumption that you have installed Flask into a
virtualenv, either on your laptop or on your VM.

.. class:: incremental

Start by activating the virtualenv with Flask installed.  Mine is 'flaskenv'.

.. class:: incremental

Next, create a new python source file: ``flask_intro.py``

.. class:: incremental

Finally, open that file in your text editor

Flask
-----

Getting started with Flask is pretty straightforward. Here's a complete,
simple app.  Type it into `flask_intro.py`:

.. code-block:: python
    :class: small

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()


Running our App
---------------

As you might expect by now, the last block in our ``flask_intro.py`` file
allows us to run this as a python program. Save your file, and in your
terminal try this::

    (flaskenv)$ python flask_intro.py

.. class:: incremental

Load ``http://localhost:5000`` in your browser to see it in action.

Debugging our App
-----------------

Last week, ``cgitb`` provided us with useful feedback when building an app.
Flask has a similar tool. Make the following changes to your
``flask_intro.py`` file:

.. code-block:: python
    :class: small

    @app.route('/')
    def hello_world():
        bar = 1 / 0
        return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True)

In your terminal, quit the app with ``^C`` and then restart it. Then reload
your browser and see what happens.


What's Happening Here?
----------------------

Flask the framework provides a Python class called `Flask`. This class
represents a single *application* in the WSGI sense.

.. class:: incremental

* You instantiate a `Flask` app with a name that represents the package or
  module containing the app.
* If your application is a single module, this should be `__name__`
* This is used to help the `Flask` app figure out where to look for
  *resources*
* *Resources* can be static files (css, images, javascript), templates, or
  additional python modules you create and need to import.
* You define a function and route a URL to call it

URL Routing
-----------

Remember our bookdb homework? How did you end up solving the problem of
mapping an HTTP request to the right function?

.. class:: incremental

Flask solves this problem by using the `route` decorator from your app.

.. class:: incremental

A 'route' takes a URL rule (more on that in a minute) and maps it to an
*endpoint* and a *function*.

.. class:: incremental

When a request arrives at a URL that matches a known rule, the function is
called.

Routes Can Be Dynamic
---------------------

You can provide *placeholders* in dynamic urls. Each *placeholder* is then a
named arg to your function (add these to ``flask_intro.py`` (and delete the
1/0 bit)):

.. code-block:: python
    :class: incremental small

    @app.route('/profile/<username>')
    def show_profile(username):
        return "My username is %s" % username

.. class:: incremental

These *placeholders* can also include *converters* that will ensure the
incoming argument is of the correct type.

.. code-block:: python
    :class: incremental small

    @app.route('/div/<float:val>/')
    def divide(val):
        return "%0.2f divided by 2 is %0.2f" % (val, val / 2)

Routes Can Be Filtered
----------------------

You can also determine which HTTP *methods* a given route will accept:

.. code-block:: python
    :class: small

    @app.route('/blog/entry/<int:id>/', methods=['GET',])
    def read_entry(id):
        return "reading entry %d" % id

    @app.route('/blog/entry/<int:id>/', methods=['POST', ])
    def write_entry(id):
        return 'writing entry %d' % id

.. class:: incremental

After adding that to ``flask_intro.py`` and saving, try loading
``http://localhost:5000/blog/entry/23/`` into your browser. Which was called?

Routes Can Be Reversed
----------------------

Reversing a URL means the ability to generate the url that would result in a
given endpoint being called.

.. class:: incremental

This means *you don't have to hard-code your URLs when building links*

.. class:: incremental

That means *you can change the URLs for your app without changing code or
templates*

.. class:: incremental

This is called **decoupling** and it is a good thing

Reversing URLs in Flask
-----------------------

In Flask, you reverse a url with the ``url_for`` function.

.. class:: incremental

* ``url_for`` requires an HTTP request context to work
* You can fake an HTTP request when working in a terminal (or testing)
* Use the ``test_request_context`` method of your app object
* This is a great chance to learn about the Python ``with`` statement
* **Don't type this**

.. code-block:: python
    :class: small incremental

    from flask import url_for
    with app.test_request_context():
      print url_for('endpoint', **kwargs)

Reversing in Action
-------------------

Quit your Flask app with ``^C``.  Then start a python interpreter in that same
terminal and import your ``flask_intro.py`` module:

.. code-block:: python

    import flask_intro
    from flask_intro import app
    from flask import url_for
    with app.test_request_context():
        print url_for('show_profile', username="cris")
        print url_for('divide', val=23.7)

    '/profile/cris/'
    '/div/23.7/'

Generating HTML
---------------

.. class:: big-centered

I enjoy writing building HTML in Python strings

.. class:: incremental right

-- nobody, ever

Templating
----------

A good framework will provide some way of generating HTML with a templating
system.

.. class:: incremental

There are nearly as many templating systems as there are frameworks

.. class:: incremental

Each has advantages and disadvantages

.. class:: incremental

Flask includes the *Jinja2* templating system (perhaps because it's built by
the same folks)

Jinja2 Template Basics
----------------------

There are a few basic things to know:

.. class:: incremental

* Variables in templates can be printed by surrounding the variable name with
  double curly braces: ``{{ name }}``.
* If a variable points to something like a dictionary or object, you can use
  *either* dot or subscript notation: ``{{ obj[attr] }}``, ``{{ dict.key
  }}``.
* Variables in templates can be *filtered*: ``{{ name|capitalize }}``. There
  is a list of builtin filters.
* Logic can be put into templates using the processor marker: ``{% for x in y
  %}{{ x }}{% endfor %}``
* Logic comes in pairs.  Any start *must* have an explicit end.

Advanced Jinja2
---------------

There is *way* too much about writing templates in Jinja2 for us to cover here
today. Read more here:

.. class:: center

http://jinja.pocoo.org/docs/templates/

Templates in Flask
------------------

Use the ``render_template`` function:

.. code-block:: python
    :class: small

    from flask import render_template

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)

.. class:: incremental

Flask looks for a ``templates`` directory in the same location as your app
module (remember ``app = Flask(__name__)``?).

.. class:: incremental

Any extra variables you want to pass to the template should be keyword
arguments to ``render_template``

Flask Template Context
----------------------

Flask adds a few things to the context of templates.  You can use these

.. class:: incremental

* **config**: contains the current configuration object
* **request**: contains the current request object
* **session**: any session data that might be available
* **g**: the request-local object to which global variables are bound
* **get_flashed_messages**: a function that returns messages you flash to your
  users (more on this later).
* **url_for**: so you can easily *reverse* urls from within your templates

Lab 1
-----

Open a terminal, change directories to the class repository, then to
``assignments/week05/lab/book_app``.

.. class:: incremental

* You'll find a file ``book_app.py`` which is all set up and ready to go
* You'll also find a ``templates`` directory with some templates
* Complete the functions to provide the right stuff to the templates
* Complete the templates to display the data to the end-user
* At the end you should have a reproduced version of last week's homework

.. class:: incremental center

**GO**

Lab 2 - Part 1
--------------

The rest of class today will be devoted to building and deploying a simple
micro-blog app using flask.

.. class:: incremental

This is based almost entirely on the `Flaskr tutorial
<http://flask.pocoo.org/docs/tutorial/>`_ from the Flask website.

Data Persistence
----------------

There are many models for persistance of data.

.. class:: incremental

* Flat files
* Relational Database (SQL RDBMs like PostgreSQL, MySQL, SQLServer, Oracle)
* Object Stores (Pickle, ZODB)
* NoSQL Databases (CouchDB, MongoDB, etc)

.. class:: incremental

It's also one of the most contentious issues in app design.

.. class:: incremental

For this reason, it's one of the things that most Small Frameworks leave
undecided.

Simple SQL
----------

For our second lab exercise today, we're going to use a simple SQL database.

.. class:: incremental

Python `PEP 249 <http://www.python.org/dev/peps/pep-0249/>`_ describes a
common API for database connections called DB API.

.. class:: incremental

The Python Standard Library comes with an implementation of this for a common,
light-weight sql database, sqlite3

.. class:: incremental

I am *not* going to talk a lot about SQL.  It's too deep a pool for us to get
into.  We'll concentrate only on those bits we need to get along.

Our Database
------------

We're going to keep this really really simple.

.. class:: incremental

In ``assignments/week05/lab/`` find the ``flaskr_1`` directory and open the
``schema.sql`` file in your editor. Add the following and save the file:

.. code-block:: sql
    :class: incremental

    drop table if exists entries;
    create table entries (
        id integer primary key autoincrement,
        title string not null,
        text string not null
    );

Our App
-------

We'll also need to do some configuration for our app.

.. class:: incremental

In that same directory, find the file ``flaskr.py`` and open it in your
editor. Add the following and save the file:

.. code-block:: python
    :class: incremental

    # configuration goes here
    DATABASE = '/tmp/flaskr.db'
    SECRET_KEY = 'development key'

    app = Flask(__name__) # this is already in the file
    app.config.from_object(__name__)


Creating the Database
---------------------

Still in ``flaskr.py`` let's add a function that will connect to our database:

.. code-block:: python
    :class: incremental

    # add this at the very top
    import sqlite3

    # add the rest of this below the app.config statement
    def connect_db():
        return sqlite3.connect(app.config['DATABASE'])

.. class:: incremental

This will be a convenience to us later on, and it will allow us to write our
very first test.

Tests and TDD
-------------

.. class:: center

**If it isn't tested, it's broken**

.. class:: incremental

Test-Driven Development means writing the tests before writing the functions.
As your tests pass, you know you're building what you want.

.. class:: incremental

We are going to write tests at every step of this lab. Along the way, we'll
learn a bit about the Python Standard Library module ``unittest``.

.. class:: incremental

You'll want to read more about this module. See our outline for reading
suggestions.

Testing Setup
-------------

In the same ``flaskr_1`` directory, find and open the ``flaskr_tests.py`` file
in your editor. Edit it to look like this:

.. code-block:: python
    :class: small

    import os
    import flaskr
    import unittest
    import tempfile

    class FlaskrTestCase(unittest.TestCase):

        def setUp(self):
            db_fd = tempfile.mkstemp()
            self.db_fd, flaskr.app.config['DATABASE'] = db_fd
            flaskr.app.config['TESTING'] = True
            self.client = flaskr.app.test_client()
            self.app = flaskr.app

Testing Teardown
----------------

Add the following method to your test class:

.. code-block:: python

    class FlaskrTestCase(unittest.TestCase):
        ...

        def tearDown(self):
            os.close(self.db_fd)
            os.unlink(flaskr.app.config['DATABASE'])

Make Tests Runnable
-------------------

And finally, add the following at the bottom of your ``flaskr_tests.py`` file:

.. code-block:: python

    if __name__ == '__main__':
        unittest.main()

.. class:: incremental

Now, we're ready to add our first method.

Test Databse Setup
------------------

We'd like to test that our database is correctly initialized. The schema has
one table with three columns. Let's test that.

Add the following method to your test class in ``flaskr_tests.py``:

.. code-block:: python

    def test_database_setup(self):
        con = flaskr.connect_db()
        cur = con.execute('PRAGMA table_info(entries);')
        rows = cur.fetchall()
        self.assertEquals(len(rows), 3)

Run the Tests
-------------

Since we added that ``if __name__ == '__main__'`` block, we can simply run our
tests with a flask-aware python executable:

.. class:: small

::

    (flaskenv)$ python flaskr_tests.py
    F
    ======================================================================
    FAIL: test_database_setup (__main__.FlaskrTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "flaskr_tests.py", line 23, in test_database_setup
        self.assertTrue(len(rows) == 3)
    AssertionError: False is not True

    ----------------------------------------------------------------------
    Ran 1 test in 0.011s

    FAILED (failures=1)

Make the Test Pass
------------------

Our database hasn't actually be properly created. We have no table and so no
rows are returned when we try to describe it. Let's fix that. Add the
following to ``flaskr.py``:

.. code-block:: python

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

We also need to call that function in our ``flaskr_tests.py``, in the
``setUp`` method of our test case.

Add the following line at the end of that ``setUp`` method:

.. code-block:: python

    def setUp(self):
        ...
        flaskr.init_db() # <- add this at the end

.. class:: incremental

Then, re-run the tests (``python flaskr_tests.py``) and see what you get.

.. class:: incremental center

**Wahoooo!**

Initialize the DB IRL
---------------------

Okay, so we know the ``init_db`` function we added sets up the database
properly.

.. class:: incremental

We still need to do this in real life, so that we can work against the
database.

.. class:: incremental

Start up a python interpreter in your ``flaskr_1`` folder and do the
following:

.. code-block:: python
    :class: incremental

    import flaskr
    flaskr.init_db()
    ^D

Lab 2 - Part 2
--------------

Okay, we have a database. Now it's time to write stuff into it, and read it
back.

.. class:: incremental

Once again, we're going to start by writing tests.

.. class:: incremental

If you've fallen behind, or if you just want to start fresh, you can find the
base of what we've done so far in the ``flaskr_2`` folder.

Managing DB Connections
-----------------------

Database connections should be bound to the borders of a request/response.

.. class:: incremental

Flask provides decorators that mark functions to be run at these borders:

.. class:: incremental

* ``@before_request``: any method decorated by this will be called before the
  cycle begins
* ``@after_request``: any method decorated by this will be called after the
  cycle is complete. If an unhandled exception occurs, these functions are
  skipped.
* ``@teardown_request``: any method decorated by this will be called at the
  end of the cycle, even if an unhandled exception occurs.

Manage our DB
-------------

Add the following code to our app (``flaskr.py``):

.. code-block:: python
    :class: small

    # add this import at the top:
    from flask import g

    # add these function after init_db
    @app.before_request
    def before_request():
        g.db = connect_db()

    @app.teardown_request
    def teardown_request(exception):
        g.db.close()

.. class:: incremental

We bind our db connection to the 'g' object, which is a global context flask
supplies to each request.

Test Writing Entries
--------------------

We want to test that we can write an entry by providing a title and text. Add
the following method to ``flaskr_tests.py``:

.. code-block:: python
    :class: small

    def test_write_entry(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            flaskr.write_entry(*expected)
            con = flaskr.connect_db()
            cur = con.execute("select * from entries;")
            rows = cur.fetchall()
        self.assertEquals(len(rows), 1)
        for val in expected:
            self.assertTrue(val in rows[0])

.. class:: incremental

Note that we have to set up a request context, and preprocess it to get our
@before_request method run.

Write an Entry
--------------

Now we are ready to write an entry to our database. Add this function to
``flaskr.py``:

.. code-block:: python

    def write_entry(title, text):
        g.db.execute('insert into entries (title, text) values (?, ?)',
                     [title, text])
        g.db.commit()

.. class:: incremental

When you're done, re-run your tests.  You should now be two for two.

Test Reading Entries
--------------------

.. code-block:: python
    :class: small

    def test_get_all_entries_empty(self):
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            entries = flaskr.get_all_entries()
            self.assertEquals(len(entries), 0)

    def test_get_all_entries(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            flaskr.write_entry(*expected)
            entries = flaskr.get_all_entries()
            self.assertEquals(len(entries), 1)
            for entry in entries:
                self.assertEquals(expected[0], entry['title'])
                self.assertEquals(expected[1], entry['text'])

Read Entries
------------

Okay, so now we have 4 tests, and two fail, add this function to ``flaskr.py``:

.. code-block:: python
    :class: small

    def get_all_entries():
        cur = g.db.execute('select title, text from entries order by id desc')
        entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
        return entries

.. class:: incremental

Re-run your tests.  You should now have four passing tests.  Great Job!

Lab 2 - Part 3
--------------

Now we can read and write blog entries, let's add views so we can see what
we're doing.

.. class:: incremental

Again.  Tests come first.

.. class:: incremental

And again, if you've fallen behind or want to start clean, the completed code
from our last step is in ``flaskr_3``

Test the Front Page
-------------------

Add the following tests to ``flaskr_tests.py``:

.. code-block::

    def test_empty_listing(self):
        rv = self.client.get('/')
        assert 'No entries here so far' in rv.data

    def test_listing(self):
        expected = ("My Title", "My Text")
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            flaskr.write_entry(*expected)
        rv = self.client.get('/')
        for value in expected:
            assert value in rv.data

Template Inheritance
--------------------

One aspect of Jinja2 templates we haven't seen yet is that templates can
inherit structure from other templates.

.. class:: incremental

* you can make replaceable blocks in templates with blocks: ``{% block foo
  %}{% endblock %}``.
* you can build on a template in a second template by extending: ``{% extends
  "layout.html" %}`` (this *must* be first)

.. class:: incremental

We want the parts of our app to look alike, so let's create a basic layout
first.  Create a file ``layout.html`` in the ``templates`` directory.

Creating Layout
---------------

.. code-block:: jinja

    <!DOCTYPE html>
    <html>
      <head>
        <title>Flaskr</title>
      </head>
      <body>
        <h1>Flaskr</h1>
        <div class="content">
        {% block body %}{% endblock %}
        </div>
      </body>
    </html>

Extending Layout
----------------

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

Creating a View
---------------

Now, we just need to hook up our entries to that template. In ``flaskr.py``
add the following code:

.. code-block:: python

    # at the top, import
    from flask import render_template

    # and after our last functions:
    @app.route('/')
    def show_entries():
        entries = get_all_entries()
        return render_template('show_entries.html', entries=entries)

.. class:: incremental

Run our tests.  Should be 6 for 6 now.

Authentication
--------------

We don't want just anyone to be able to add new entries. So we want to be able
to authenticate a user.

.. class:: incremental

We'll be using built-in functionality of Flask to do this, but this
simplest-possible implementation should serve only as a guide.

.. class:: incremental

We'll start with the tests, of course.

Test Authentication
-------------------

Back in ``flaskr_tests.py`` add new test methods:

.. code-block:: python
    :class: small

    def test_login_passes(self):
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            flaskr.do_login(flaskr.app.config['USERNAME'],
                            flaskr.app.config['PASSWORD'])
            self.assertTrue(session.get('logged_in', False))

    def test_login_fails(self):
        with self.app.test_request_context('/'):
            self.app.preprocess_request()
            self.assertRaises(ValueError, flaskr.do_login,
                              flaskr.app.config['USERNAME'],
                              'incorrectpassword')

Set Up Authentication
---------------------

Now, let's add the code in ``flaskr.py`` to support this:

.. code-block:: python
    :class: small

    # add an import
    from flask import session

    # and configuration
    USERNAME = 'admin'
    PASSWORD = 'default'

    # and a function
    def do_login(usr, pwd):
        if usr != app.config['USERNAME']:
            raise ValueError
        elif pwd != app.config['PASSWORD']:
            raise ValueError
        else:
            session['logged_in'] = True

Login/Logout in Tests
---------------------

Let's add tests for a view. We'll set up a form that redirects back to the
main view on success. First, methods to actually do the login/logout (in
``flaskr_tests.py``):

.. code-block:: python

    def login(self, username, password):
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout',
                               follow_redirects=True)

Test Authentication
-------------------

And now the test itself (again, ``flaskr_tests.py``):

.. code-block:: python

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

.. class:: incremental

We should be up to 9 tests, one failing

Add Login Template
------------------

Add ``login.html`` to ``templates``:

.. code-block:: jinja
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

Add Login/Logout Views
----------------------

And back in ``flaskr.py`` add new code.  Let's start with imports:

.. code-block:: python

    # at the top, new imports
    from flask import request
    from flask import redirect
    from flask import flash
    from flask import url_for

And the View Code
-----------------

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

Flask provides ``flash`` as a way of sending messages to the user from view
code. We need a place to show these messages. Add it to ``layout.html`` (along
with links to log in and out)

.. code-block:: jinja
    :class: small

    <h1>Flaskr</h1>       <!-- already there -->
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

Adding an Entry
---------------

We still lack a way to add an entry. We need a view to do that. Again, tests
first (in ``flaskr_tests.py``):

.. code-block:: python

    def test_add_entries(self):
        self.login('admin', 'default')
        rv = self.client.post('/add', data=dict(
            title='Hello',
            text='This is a post'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert 'Hello' in rv.data
        assert 'This is a post' in rv.data

Add the View
------------

We've already got all the stuff we need to write entries, we just need an
endpoint that will do it via the web (in ``flaskr.py``):

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

In the terminal where you've been running tests, run our flaskr app:

.. class:: incremental

::

    (flaskenv)$ python flaskr.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

The Big Payoff
--------------

Now load ``http://localhost:5000/`` in your browser and enjoy your reward.

Lab 2 - Part 4
--------------

On the other hand, what we've got here is pretty ugly.  We could prettify it.

.. class:: incremental

Again, if you want to start fresh or you fell behind you can find code
completed to this point in ``flaskr_4``.

.. class:: incremental

In that directory inside the ``static`` directory you will find
``styles.css``. Open it in your editor.  It contains basic CSS for this app.

.. class:: incremental

We'll need to include this file in our ``layout.html``.

Static Files
------------

Like page templates, Flask locates static resources like images, css and
javascript by looking for a ``static`` directory next to the app module.

.. class:: incremental

You can use the special url endpoint ``static`` to build urls that point here.
Open ``layout.html`` and add the following:

.. code-block:: jinja
    :class: small incremental

    <head>  <!-- you only need to add the <link> below -->
      <title>Flaskr</title>
      <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet" type="text/css">
    </head>


Deploying
---------

First, move the source code to your VM::

    (flaskenv)$ cd ../
    (flaskenv)$ tar -czvf flaskr.tgz flaskr
    (flaskenv)$ scp flaskr.tgz <your_vm>:~/
    (flaskenv)$ ssh <your_vm>
    $ tar -zxvf flaskr.tgz

Then, on your VM, set up a virtualenv with Flask installed

Deploying
---------

You'll need to make some changes to mod_wsgi configuration.

* Open ``/etc/apache2/sites-available/default`` in an editor (on the VM)

* Add the following line at the top (outside the VirtualHost block):
  ``WSGIPythonHome /path/to/flaskenv``

* Delete all other lines refering to mod_wsgi configuration
* Add the following in the VirtualHost block:

::

    WSGIScriptAlias / /var/www/flaskr.wsgi

Deploying
---------

Finally, you'll need to add the named wsgi file and edit it to match::

    $ sudo touch /var/www/flaskr.wsgi
    $ sudo vi /var/www/flasrk.wsgi


    import sys
    sys.path.insert(0, 'path/to/flaskr') # the flaskr app you uploaded

    from flaskr import app as application

Deploying
---------

Finally, restart apache and bask in the glow::

    $ sudo apache2ctl configtest
    $ sudo /etc/init.d/apache2 graceful

Load http://your_vm/

Wheeee!

Going Further
-------------

It's not too hard to see ways you could improve this.

.. class:: incremental

* For my part, I made a version using Bootstrap.js.
* You could limit the number of posts shown on the front page.
* You could add dates to the posts and provide archived views for older posts.
* You could add the ability to edit existing posts (and add an updated date to the schema)
* ...

But Instead
-----------

Instead of doing any of that, this week's assignment is a bit different.

.. class:: incremental

You've implemented an app in one Small Framework. I want you to do it all
again, in a different Small Framework.

.. class:: incremental

While you're working on it, think about the differences between your new
Framework and Flask. What do you like more? What do you like less? How might
this influence your choice of Frameworks in the future?

Assignment
----------

* Re-implement the Flaskr app we built in class in a different Small
  Framework.
* There are several named in the class outline, and in this presentation.
* Pick one of them, or a different one of your choice.  It must be Python.
* When you are finished, add your source code and a README that talks about
  your experience to the ``athome`` folder of week05.
* Tell me about your new Framework. Discuss the points above regarding
  differences.

Submitting The Assignment
-------------------------

* Try to get your code running on your VM
* Add your source code, in it's entirety, to the ``athome`` folder for week 5
* Add a README.txt file that discusses the experience.
* Commit your changes to your fork of the class repository and send me a pull
  request
