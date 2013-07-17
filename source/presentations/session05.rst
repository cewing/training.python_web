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

    import flask_intro
    from flask_intro import app
    from flask import url_for
    with app.test_request_context():
        print url_for('show_profile', username="cris")
        print url_for('divide', val=23.7)

    '/profile/cris/'
    '/div/23.7/'


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
