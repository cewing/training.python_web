A Quick Flask Walkthrough
=========================

If you've already set up your virtualenv and installed flask, you can simply
activate it and skip down to **Kicking the Tires**

If not...

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

With your flaskenv activated, create a file called ``flask_intro.py`` and
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

Restart your app and then reload your browser to see what happens.

Click in the stack trace that appears in your browser.  Notice anything fun?

(clean up the error when you're done playing).


Your work so far
----------------

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

Enough for Now
--------------

That will give you plenty to think about before class.  We'll put this all to
good use building a real flask app in our next session.
