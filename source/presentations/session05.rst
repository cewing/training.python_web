Python Web Programming
======================

.. image:: img/bike.jpg
    :align: left
    :width: 50%

Day 3 AM: Frameworks and Flask

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

These technologies are foundational.

.. class:: incremental

Everything we do from here out will be based on tools *built* using them.


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


    