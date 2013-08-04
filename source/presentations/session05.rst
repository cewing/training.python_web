Python Web Programming
======================

.. image:: img/bike.jpg
    :align: left
    :width: 50%

Session 5: Frameworks and Flask

.. class:: intro-blurb right

| "Reinventing the wheel is great
| if your goal is to learn more about the wheel"
|
| -- James Tauber, PyCon 2007

.. class:: image-credit

image: Britanglishman http://www.flickr.com/photos/britanglishman/5999131365/ - CC-BY


A Moment to Reflect
-------------------

We've been at this for a couple of days now.  We've learned a great deal:

.. class:: incremental

* Sockets, the TCP/IP Stack and Basic Mechanics
* Web Protocols and the Importance of Clear Communication
* APIs and Consuming Data from The Web
* CGI and WSGI and Getting Information to Your Dynamic Applications

.. class:: incremental

Everything we do from here out will be based on tools built using these
*foundational technologies*.


From Now On
-----------

Think of everything we do as sitting on top of WSGI

.. class:: incremental

This may not *actually* be true

.. class:: incremental

But we will always be working at that level of abstraction.


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

Think back over the last four sessions. What were your pain points? Which bits
do you wish you didn't have to think about?


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


Practice Safe Development
-------------------------

We are going to install Flask, and the packages it requires, into a
virtualenv.

.. class:: incremental

This will ensure that it is isolated from everything else we do in class (and
vice versa)

.. container:: incremental

    Remember the basic format for creating a virtualenv:

    .. class:: small

    ::

        $ python virtualenv.py [options] <ENV>
        <or>
        $ virtualenv [options] <ENV>


Set Up a VirtualEnv
-------------------

Start by creating your virtualenv::

    $ python virtualenv.py flaskenv
    <or>
    $ virtualenv flaskenv
    ...

.. container:: incremental

    Then, activate it::
    
        $ source flaskenv/bin/activate
        <or>
        C:\> flaskenv\Scripts\activate


Install Flask
-------------

Finally, install Flask using `setuptools` or `pip`::

    (flaskenv)$ pip install flask
    Downloading/unpacking flask
      Downloading Flask-0.10.1.tar.gz (544kB): 544kB downloaded
    ...
    Installing collected packages: flask, Werkzeug, Jinja2, 
      itsdangerous, markupsafe
    ...
    Successfully installed flask Werkzeug Jinja2 itsdangerous 
      markupsafe


Kicking the Tires
-----------------

We've installed the Flask microframework and all of its dependencies.

.. class:: incremental

Now, let's see what it can do

.. class:: incremental

In your class working directory, create a file called ``flask_intro.py`` and 
open it in your text editor.


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
Flask has similar functionality. Make the following changes to your
``flask_intro.py`` file:

.. code-block:: python
    :class: small

    def hello_world():
        bar = 1 / 0
        return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True)

.. class:: incremental

Restart your app and then reload your browser to see what happens (clean up
the error when you're done).


What's Happening Here?
----------------------

Flask the framework provides a Python class called `Flask`. This class
functions as a single *application* in the WSGI sense.

.. class:: incremental

Remember, a WSGI application must be a *callable* that takes the arguments
*environ* and *start_response*.

.. class:: incremental

It has to call the *start_response* method, providing status and headers.

.. class:: incremental

And it has to return an *iterable* that represents the HTTP response body.


Under the Covers
----------------

In Python, an object is a *callable* if it has a ``__call__`` method.

.. container:: incremental

    Here's the ``__call__`` method of the ``Flask`` class:
    
    .. code-block:: python
    
        def __call__(self, environ, start_response):
            """Shortcut for :attr:`wsgi_app`."""
            return self.wsgi_app(environ, start_response)

.. class:: incremental

As you can see, it calls another method, called ``wsgi_app``.  Let's follow
this down...


Flask.wsgi_app
--------------

.. code-block:: python
    :class: small

    def wsgi_app(self, environ, start_response):
        """The actual WSGI application.  
        ...
        """
        ctx = self.request_context(environ)
        ctx.push()
        error = None
        try:
            try:
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.make_response(self.handle_exception(e))
            return response(environ, start_response)
        #...

.. class:: incremental

``response`` is another WSGI app.  ``Flask`` is actually *middleware*


Abstraction Layers
------------------

Finally, way down in a package called *werkzeug*, we find this response object
and it's ``__call__`` method:

.. code-block:: python
    :class: small

    def __call__(self, environ, start_response):
        """Process this response as WSGI application.

        :param environ: the WSGI environment.
        :param start_response: the response callable provided by the WSGI
                               server.
        :return: an application iterator
        """
        app_iter, status, headers = self.get_wsgi_response(environ)
        start_response(status, headers)
        return app_iter


Common Threads
--------------

All Python web frameworks that operate under the WSGI spec will do this same
sort of thing.

.. class:: incremental

They have to do it.

.. class:: incremental

And these layers of abstraction allow you, the developer to focus only on the
thing that really matters to you.

.. class:: incremental

Getting input from a request, and returning a response.


Popping Back Up the Stack
-------------------------

Returning up to the level where we will be working, remember what you've done:

.. class:: incremental

* You instantiated a `Flask` app with a name that represents the package or
  module containing the app

  * Because our app is a single Python module, this should be ``__name__``
  * This is used to help the `Flask` app figure out where to look for
    *resources*

* You defined a function that returned a response body
* You told the app which requests should use that function with a *route*

.. class:: incremental

Let's take a look at how that last bit works for a moment...


URL Routing
-----------

Remember our bookdb exercise? How did you end up solving the problem of
mapping an HTTP request to the right function?

.. class:: incremental

Flask solves this problem by using the `route` decorator from your app.

.. class:: incremental

A 'route' takes a URL rule (more on that in a minute) and maps it to an
*endpoint* and a *function*.

.. class:: incremental

When a request arrives at a URL that matches a known rule, the function is
called.


URL Rules
---------

URL Rules are strings that represent what environ['PATH_INFO'] will look like.

.. class:: incremental

They are added to a *mapping* on the Flask object called the *url_map*

.. class:: incremental

You can call ``app.add_url_rule()`` to add a new one

.. class:: incremental

Or you can use what we've used, the ``app.route()`` decorator


Function or Decorator
---------------------

.. code-block:: python
    :class: small

    def index():
        """some function that returns something"""
        # ...
    
    app.add_url_rule('/', 'homepage', index)

.. container:: incremental

    is identical to

    .. code-block:: python
        :class: small
    
        @app.route('/', 'homepage')
        def index():
            """some function that returns something"""
            # ...


Routes Can Be Dynamic
---------------------

A *placeholder* in a URL rule becomes a named arg to your function (add these
to ``flask_intro.py``):

.. code-block:: python
    :class: incremental small

    @app.route('/profile/<username>')
    def show_profile(username):
        return "My username is %s" % username

.. class:: incremental

And *converters* ensure the incoming argument is of the correct type.

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
* This is a great chance to use the Python ``with`` statement
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

    >>> from flask_intro import app
    >>> from flask import url_for
    >>> with app.test_request_context():
    ...     print url_for('show_profile', username="cris")
    ...     print url_for('divide', val=23.7)
    ... 
    '/profile/cris/'
    '/div/23.7/'
    >>>


Break Time
----------

Now's a good time to take a rest.

.. class:: incremental

When we return, we'll take a look at templating and data persistence.


Generating HTML
---------------

.. class:: big-centered

"I enjoy writing HTML in Python"

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

Let's start with the absolute basics.

.. container:: incremental

    Fire up a Python interpreter, using your flask virtualenv:
    
    .. code-block:: python
        :class: small
    
        (flaskenv)$ python
        >>> from jinja2 import Template

.. container:: incremental

    A template is built of a simple string:
    
    .. code-block:: python
        :class: small

        >>> t1 = Template("Hello {{ name }}, how are you?")


Rendering a Template
--------------------

Call the ``render`` method, providing some *context*:

.. code-block:: python
    :class: incremental small

    >>> t1.render(name="Freddy")
    u'Hello Freddy, how are you?'
    >>> t1.render({'name': "Roberto"})
    u'Hello Roberto, how are you?'
    >>>

.. class:: incremental

*Context* can either be keyword arguments, or a dictionary


Dictionaries in Context
-----------------------

Dictionaries passed in as part of the *context* can be addressed with *either*
subscript or dotted notation:

.. code-block:: python
    :class: incremental small

    >>> person = {'first_name': 'Frank',
    ...           'last_name': 'Herbert'}
    >>> t2 = Template("{{ person.last_name }}, {{ person['first_name'] }}")
    >>> t2.render(person=person)
    u'Herbert, Frank'

.. class:: incremental

* Jinja2 will try the *correct* way first (attr for dotted, item for
  subscript).
* If nothing is found, it will try the opposite.
* If nothing is found, it will return an *undefined* object.


Objects in Context
------------------

The exact same is true of objects passed in as part of *context*:

.. code-block:: python
    :class: incremental small

    >>> t3 = Template("{{ obj.x }} + {{ obj['y'] }} = Fun!")
    >>> class Game(object):
    ...   x = 'babies'
    ...   y = 'bubbles'
    ...
    >>> bathtime = Game()
    >>> t3.render(obj=bathtime)
    u'babies + bubbles = Fun!'

.. class:: incremental

This means your templates can be a bit agnostic as to the nature of the things
in *context*


Filtering values in Templates
-----------------------------

You can apply *filters* to the data passed in *context* with the pipe ('|')
operator:

.. code-block:: python
    :class: incremental small

    t4 = Template("shouted: {{ phrase|upper }}")
    >>> t4.render(phrase="this is very important")
    u'shouted: THIS IS VERY IMPORTANT'

.. container:: incremental

    You can also chain filters together:
    
    .. code-block:: python
        :class: small
    
        t5 = Template("confusing: {{ phrase|upper|reverse }}")
        >>> t5.render(phrase="howdy doody")
        u'confusing: YDOOD YDWOH'


Control Flow
------------

Logical control structures are also available:

.. code-block:: python
    :class: incremental small

    tmpl = """
    ... {% for item in list %}{{ item }}, {% endfor %}
    ... """
    >>> t6 = Template(tmpl)
    >>> t6.render(list=[1,2,3,4,5,6])
    u'\n1, 2, 3, 4, 5, 6, '

.. class:: incremental

Any control structure introduced in a template **must** be paired with an 
explicit closing tag ({% for %}...{% endfor %})


Template Tests
--------------

There are a number of specialized *tests* available for use with the
``if...elif...else`` control structure:

.. code-block:: python
    :class: incremental small

    >>> tmpl = """
    ... {% if phrase is upper %}
    ...   {{ phrase|lower }}
    ... {% elif phrase is lower %}
    ...   {{ phrase|upper }}
    ... {% else %}{{ phrase }}{% endif %}"""
    >>> t7 = Template(tmpl)
    >>> t7.render(phrase="FOO")
    u'\n\n  foo\n'
    >>> t7.render(phrase="bar")
    u'\n\n  BAR\n'
    >>> t7.render(phrase="This should print as-is")
    u'\nThis should print as-is'


Basic Python Expressions
------------------------

Basic Python expressions are also supported:

.. code-block:: python
    :class: incremental small

    tmpl = """
    ... {% set sum = 0 %}
    ... {% for val in values %}
    ... {{ val }}: {{ sum + val }}
    ...   {% set sum = sum + val %}
    ... {% endfor %}
    ... """
    >>> t8 = Template(tmpl)
    >>> t8.render(values=range(1,11))
    u'\n\n\n1: 1\n  \n\n2: 3\n  \n\n3: 6\n  \n\n4: 10\n
      \n\n5: 15\n  \n\n6: 21\n  \n\n7: 28\n  \n\n8: 36\n
      \n\n9: 45\n  \n\n10: 55\n  \n'


Much, Much More
---------------

There's more that Jinja2 templates can do, and we'll see more in the next
session when we write templates for our Flask app.

.. container:: incremental

    Make sure that you bookmark the Jinja2 documentation for later use::
    
        http://jinja.pocoo.org/docs/templates/


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
undecided, Flask included.


Simple SQL
----------

`PEP 249 <http://www.python.org/dev/peps/pep-0249/>`_ describes a
common API for database connections called DB-API 2.

.. container:: incremental

    The goal was to

        achieve a consistency leading to more easily understood modules, code
        that is generally more portable across databases, and a broader reach
        of database connectivity from Python

        .. class:: image-credit

        source: http://www.python.org/dev/peps/pep-0248/


A Note on DB API
----------------

.. class:: incremental center

It is important to remember that PEP 249 is **only a specification**.

.. class:: incremental

There is no code or package for DB-API 2 on it's own.  

.. class:: incremental

Since 2.5, the Python Standard Library has provided a `reference
implementation of the api <http://docs.python.org/2/library/sqlite3.html>`_
based on SQLite3

.. class:: incremental

Before Python 2.5, this package was available as ``pysqlite``


Using DB API
------------

To use the DB API with any database other than SQLite3, you must have an
underlying API package available.

.. container:: incremental

    Implementations are available for:

    * PostgreSQL (**psycopg2**, txpostgres, ...)
    * MySQL (**mysql-python**, PyMySQL, ...)
    * MS SQL Server (**adodbapi**, pymssql, mxODBC, pyodbc, ...)
    * Oracle (**cx_Oracle**, mxODBC, pyodbc, ...)
    * and many more...

    .. class:: image-credit

    source: http://wiki.python.org/moin/DatabaseInterfaces


Installing API Packages
-----------------------

Most db api packages can be installed using typical Pythonic methods::

    $ easy_install psycopg2
    $ pip install mysql-python
    ...

.. class:: incremental

Most api packages will require that the development headers for the underlying
database system be available. Without these, the C symbols required for
communication with the db are not present and the wrapper cannot work.


Not Today
---------

We don't want to spend the next hour getting a package installed, so let's use
``sqlite3`` instead.

.. class:: incremental

I **do not** recommend using sqlite3 for production web applications, there are
too many ways in which it falls short

.. class:: incremental

But it will provide a solid learning tool


Getting Started
---------------

In the class resources folder, you'll find an ``sql`` directory. Copy that to
your working directory.

.. class:: incremental

Open the file ``createdb.py`` in your text editor.  Edit ``main`` like so:

.. code-block:: python
    :class: incremental small

    def main():
        conn =  sqlite3.connect(DB_FILENAME)
        if DB_IS_NEW:
            print 'Need to create database and schema'
        else:
            print 'Database exists, assume schema does, too.'
        conn.close()


Try It Out
----------

Run the ``createdb.py`` script to see it in effect::

    $ python createdb.py
    Need to create database and schema
    $ python createdb.py
    Database exists, assume schema does, too.
    $ ls
    books.db
    ...

.. class:: incremental

Sqlite3 will automatically create a new database when you connect for the
first time, if one does not exist.


Set Up A Schema
---------------

Make the following changes to ``createdb.py``:

.. code-block:: python
    :class: small

    DB_FILENAME = 'books.db'
    SCHEMA_FILENAME = 'ddl.sql' # <- this is new
    DB_IS_NEW = not os.path.exists(DB_FILENAME)

    def main():
        with sqlite3.connect(DB_FILENAME) as conn: # <- context mgr
            if DB_IS_NEW: # A whole new if clause:
                print 'Creating schema'
                with open(SCHEMA_FILENAME, 'rt') as f:
                    schema = f.read()
                conn.executescript(schema)
            else:
                print 'Database exists, assume schema does, too.'
        # delete the `conn.close()` that was here.


Verify Your Work
----------------

Quit your python interpreter and delete the file ``books.db``

.. container:: incremental

    Then run the script from the command line again to try it out::

        $ python createdb.py
        Creating schema
        $ python createdb.py
        Database exists, assume schema does, too.

Introspect the Database
-----------------------

Add the following to ``createdb.py``:

.. code-block:: python
    :class: small

    # in the imports, add this line:
    from utils import show_table_metadata

    else:
        # in the else clause, replace the print statement with this:
        print "Database exists, introspecting:"
        tablenames = ['author', 'book']
        cursor = conn.cursor()
        for name in tablenames:
            print "\n"
            show_table_metadata(cursor, name)

.. class:: incremental

Then try running ``python createdb.py`` again

My Results
----------

.. class:: small

::

    $ python createdb.py
    Table Metadata for 'author':
    cid        | name       | type       | notnull    | dflt_value | pk         |
    -----------+------------+------------+------------+------------+------------+-
    0          | authorid   | INTEGER    | 1          | None       | 1          |
    -----------+------------+------------+------------+------------+------------+-
    1          | name       | TEXT       | 0          | None       | 0          |
    -----------+------------+------------+------------+------------+------------+-


    Table Metadata for 'book':
    cid        | name       | type       | notnull    | dflt_value | pk         |
    -----------+------------+------------+------------+------------+------------+-
    0          | bookid     | INTEGER    | 1          | None       | 1          |
    -----------+------------+------------+------------+------------+------------+-
    1          | title      | TEXT       | 0          | None       | 0          |
    -----------+------------+------------+------------+------------+------------+-
    2          | author     | INTEGER    | 1          | None       | 0          |
    -----------+------------+------------+------------+------------+------------+-


Inserting Data
--------------

Let's load up some data. Fire up your interpreter and type:

.. code-block:: python
    :class: small

    >>> import sqlite3
    >>> insert = """
    ... INSERT INTO author (name) VALUES("Iain M. Banks");"""
    >>> with sqlite3.connect("books.db") as conn:
    ...     cur = conn.cursor()
    ...     cur.execute(insert)
    ...     cur.rowcount
    ...     cur.close()
    ...     
    <sqlite3.Cursor object at 0x10046e880>
    1
    >>> 

.. class:: incremental

Did that work?


Querying Data
-------------

Let's query our database to find out:

.. code-block:: python
    :class: small

    >>> query = """
    ... SELECT * from author;"""
    >>> with sqlite3.connect("books.db") as conn:
    ...     cur = conn.cursor()
    ...     cur.execute(query)
    ...     rows = cur.fetchall()
    ...     for row in rows:
    ...         print row
    ...
    <sqlite3.Cursor object at 0x10046e8f0>
    (1, u'Iain M. Banks')

.. class:: incremental

Alright!  We've got data in there.  Let's make it more efficient


Parameterized Statements
------------------------

Try this:

.. code-block:: python
    :class: small

    >>> insert = """
    ... INSERT INTO author (name) VALUES(?);"""
    >>> authors = [["China Mieville"], ["Frank Herbert"],
    ... ["J.R.R. Tolkien"], ["Susan Cooper"], ["Madeline L'Engle"]]
    >>> with sqlite3.connect("books.db") as conn:
    ...     cur = conn.cursor()
    ...     cur.executemany(insert, authors)
    ...     print cur.rowcount
    ...     cur.close()
    ...
    <sqlite3.Cursor object at 0x10046e8f0>
    5


Check Your Work
---------------

Again, query the database:

.. code-block:: python
    :class: small

    >>> query = """
    ... SELECT * from author;"""
    >>> with sqlite3.connect("books.db") as conn:
    ...     cur = conn.cursor()
    ...     cur.execute(query)
    ...     rows = cur.fetchall()
    ...     for row in rows:
    ...         print row
    ...
    <sqlite3.Cursor object at 0x10046e8f0>
    (1, u'Iain M. Banks')
    ...
    (4, u'J.R.R. Tolkien')
    (5, u'Susan Cooper')
    (6, u"Madeline L'Engle")


Transactions
------------

Transactions group operations together, allowing you to verify them *before*
the results hit the database.

.. class:: incremental

In SQLite3, data-altering statements require an explicit ``commit`` unless
auto-commit has been enabled.

.. class:: incremental

The ``with`` statements we've used take care of committing when the context
manager closes.

.. class:: incremental

Let's change that so we can see what happens explicitly


Populating the Database
-----------------------

Let's start by seeing what happens when you try to look for newly added data
before the ``insert`` transaction is committed.

.. class:: incremental

Begin by quitting your interpreter and deleting ``books.db``.  

.. container:: incremental

    Then re-create the database, empty::

        $ python createdb.py
        Creating schema


Setting Up the Test
-------------------

.. class:: small

Open ``populatedb.py`` in your editor, replace the final ``print``:

.. code-block:: python
    :class: small

    conn1 = sqlite3.connect(DB_FILENAME)
    conn2 = sqlite3.connect(DB_FILENAME)
    print "\nOn conn1, before insert:"
    show_authors(conn1)
    authors = ([author] for author in AUTHORS_BOOKS.keys())
    cur = conn1.cursor()
    cur.executemany(author_insert, authors)
    print "\nOn conn1, after insert:"
    show_authors(conn1)
    print "\nOn conn2, before commit:"
    show_authors(conn2)
    conn1.commit()
    print "\nOn conn2, after commit:"
    show_authors(conn2)
    conn1.close()
    conn2.close()


Running the Test
----------------

.. class:: small

Quit your python interpreter and run the ``populatedb.py`` script:

.. class:: small incremental

::

    On conn1, before insert:
    no rows returned
    On conn1, after insert:
    (1, u'China Mieville')
    (2, u'Frank Herbert')
    (3, u'Susan Cooper')
    (4, u'J.R.R. Tolkien')
    (5, u"Madeline L'Engle")

    On conn2, before commit:
    no rows returned
    On conn2, after commit:
    (1, u'China Mieville')
    (2, u'Frank Herbert')
    (3, u'Susan Cooper')
    (4, u'J.R.R. Tolkien')
    (5, u"Madeline L'Engle")


Rollback
--------

That's all well and good, but what happens if an error occurs?

.. class:: incremental

Transactions can be rolled back in order to wipe out partially completed work.

.. class:: incremental

Like with commit, using ``connect`` as a context manager in a ``with``
statement will automatically rollback for exceptions.

.. class:: incremental

Let's rewrite our populatedb script so it explicitly commits or rolls back a
transaction depending on exceptions occurring


Edit populatedb.py (slide 1)
----------------------------

.. class:: small

First, add the following function above the ``if __name__ == '__main__'``
block:

.. code-block:: python
    :class: small

    def populate_db(conn):
        authors = ([author] for author in AUTHORS_BOOKS.keys())
        cur = conn.cursor()
        cur.executemany(author_insert, authors)

        for author in AUTHORS_BOOKS.keys():
            params = ([book, author] for book in AUTHORS_BOOKS[author])
            cur.executemany(book_insert, params)


Edit populatedb.py (slide 2)
----------------------------

.. class:: small

Then, in the runner:

.. code-block:: python
    :class: small

    with sqlite3.connect(DB_FILENAME) as conn1:
        with sqlite3.connect(DB_FILENAME) as conn2:
            try:
                populate_db(conn1)
                print "\nauthors and books on conn2 before commit:"
                show_authors(conn2)
                show_books(conn2)
            except sqlite3.Error:
                conn1.rollback()
                print "\nauthors and books on conn2 after rollback:"
                show_authors(conn2)
                show_books(conn2)
                raise
            else:
                conn1.commit()
                print "\nauthors and books on conn2 after commit:"
                show_authors(conn2)
                show_books(conn2)


Try it Out
----------

Remove ``books.db`` and recrete the database, then run our script:

.. class:: small

::

    $ rm books.db
    $ python createdb.py
    Creating schema
    $ python populatedb.py

.. class:: small incremental

::

    authors and books on conn2 after rollback:
    no rows returned
    no rows returned
    Traceback (most recent call last):
      File "populatedb.py", line 57, in <module>
        populate_db(conn1)
      File "populatedb.py", line 46, in populate_db
        cur.executemany(book_insert, params)
    sqlite3.InterfaceError: Error binding parameter 0 - probably unsupported type.

Oooops, Fix It
--------------

.. class:: small

Okay, we got an error, and the transaction was rolled back correctly.

.. container:: incremental small

    Open ``utils.py`` and find this:

    .. code-block:: python 

        'Susan Cooper': ["The Dark is Rising", ["The Greenwitch"]],

.. container:: incremental small

    Fix it like so:

    .. code-block:: python

        'Susan Cooper': ["The Dark is Rising", "The Greenwitch"],

.. class:: small incremental

It appears that we were attempting to bind a list as a parameter.  Ooops.


Try It Again
------------

.. container:: small

    Now that the error in our data is repaired, let's try again::

        $ python populatedb.py

.. class:: small incremental

::

    Reporting authors and books on conn2 before commit:
    no rows returned
    no rows returned
    Reporting authors and books on conn2 after commit:
    (1, u'China Mieville')
    (2, u'Frank Herbert')
    (3, u'Susan Cooper')
    (4, u'J.R.R. Tolkien')
    (5, u"Madeline L'Engle")
    (1, u'Perdido Street Station', 1)
    (2, u'The Scar', 1)
    (3, u'King Rat', 1)
    (4, u'Dune', 2)
    (5, u"Hellstrom's Hive", 2)
    (6, u'The Dark is Rising', 3)
    (7, u'The Greenwitch', 3)
    (8, u'The Hobbit', 4)
    (9, u'The Silmarillion', 4)
    (10, u'A Wrinkle in Time', 5)
    (11, u'A Swiftly Tilting Planet', 5)


Next Steps
----------

We've learned a bit about the basics of using Flask, writing templates and
using DB API to persist data.

.. class:: incremental

This afternoon, we'll put this to use by writing a small application in Flask

.. class:: incremental

By the end of the day, we'll have a fully-tested microblog ready to go.


Lunch Time
----------

.. class:: big-centered

We'll see you back here in an hour.  Enjoy!
