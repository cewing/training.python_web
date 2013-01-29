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

Onward
------

.. class:: big-centered

We are moving up the stack

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

A framework allows you to build different kinds of applications.

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
* Pick a framework whose abstractions meet your needs

.. class:: incremental

Frameworks with a minimal level of abstraction are considered to be
*Microframeworks*

.. class:: incremental center

Where is the line between micro- and not?

Python Web Frameworks
---------------------

There are scores of 'em.

.. class:: incremental small

Django    Grok     Pylons TurboGears web2py 
Zope      CubicWeb Enamel Gizmo(QP) Glashammer 
Karrigell Nagare   notmm Porcupine QP 
SkunkWeb  Spyce    Tipfy Tornado WebCore 
web.py    Webware  Werkzeug WHIFF XPRESS 
AppWsgi   Bobo     Bo7le CherryPy circuits.web 
Paste     PyWebLib WebStack Albatross Aquarium 
Divmod    Nevow    Flask JOTWeb2 Python Servlet 
Engine    Pyramid  Quixote Spiked weblayer

scraps
------

What is a Framework?

What types of frameworks are there?

Why choose one over another?

Intro to Flask

Lab 1 create simple multi-page app with flask (redo week 4 homework in class)

templating (jinja2 in flask)

Deploying to webserver (virtualenv and mod_wsgi)

Lab 2 create a simple app with flask part 2

