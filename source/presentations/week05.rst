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

And Second
----------

.. class:: big-centered

Questions from the Reading?

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

Start by activating the virtualenv with Flask installed

.. class:: incremental

Next, create a new python source file: `flask_intro.py`

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

.. class:: incremental

Load http://localhost:5000 in your browser to see it in action.

What's Happening Here?
----------------------

Flask the framework provides a Python class called `Flask`. This class
represents a single *application* in the WSGI sense.

.. class:: incremental

* You instantiate a `Flask` app with a name that represents the package or
  module containing the app. 
* If your application is a single module, this should be `__name__`
* This is used to help the `Flask` app figure out where to look for resources

scraps
------

Intro to Flask

Lab 1 create simple multi-page app with flask (redo week 4 homework in class)

templating (jinja2 in flask)

Deploying to webserver (virtualenv and mod_wsgi)

Lab 2 create a simple app with flask part 2

