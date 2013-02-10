Internet Programming with Python
================================

.. image:: img/django-pony.png
    :align: left
    :width: 50%

Week 6: Django - Part 1

.. class:: intro-blurb right

Wherein we become 'perfectionists with deadlines'

.. class:: image-credit

image: http://djangopony.com/

But First
---------

.. class:: big-centered

Review from the Assignment

And Second
----------

.. class:: big-centered

Questions from the Reading?

And Now
-------

.. image:: img/django_lead.png
    :align: center
    :width: 79%


Full Stack Framework
--------------------

Django is **One Big Package**

.. class:: incremental

When you installed Flask, you also installed *werkzeug* and *jinja2*, a total
of 1.85MB

.. class:: incremental

Django 1.4.3 weighs in at 7.7MB (4 times the size of Flask)

.. class:: incremental

So what do you get?

Full Stack Framework
--------------------

Django comes with:

.. class:: incremental

* Persistence via the *Django ORM*
* CRUD content editing via the automatic *Django Admin*
* URL Mapping via *urlpatterns*
* Templating via the *Django Template Language*
* Caching with levels of configurability
* Internationalization via i18n hooks
* Form rendering and handling

.. class:: incremental

Pretty much everything you need to make a solid website quickly

What Sets it Apart?
-------------------

Lots of frameworks offer some of these features, if not all.

.. class:: incremental

What is Django's *killer feature*

.. class:: incremental center

**The Django Admin**

The Django Admin
----------------

Works in concert with the Django ORM to provide automatic CRUD functionality

.. class:: incremental

You write the models, it provides the UI

.. class:: incremental center

**Really**

The Pareto Principle
--------------------

The Django Admin is a perfect embodiment of the Pareto Priciple, a.k.a. the
80/20 rule:

.. class:: incremental center

80% of the problems can be solved by 20% of the effort

.. class:: incremental

The converse also holds true:

.. class:: incremental center

Fixing the last 20% of the problems will take the remaining 80% of the effort.

Other Django Advantages
-----------------------

Clearly the most popular Python web framework at this time

.. class:: incremental

Popularity translates into:

.. class:: incremental

* Active, present community
* Plethora of good examples to be found online
* Rich ecosystem of *apps* (encapsulated add-on functionality)

.. class:: incremental center

**Jobs**

Active Development
------------------

Popular frameworks tend to be actively developed.

.. class:: incremental

Django releases in the last 12 months:

.. class:: incremental

* 1.5 (any day now)
* 1.4.3 (December 2012)
* 1.3.5 (December 2012)
* 1.4.2 (November 2012)
* 1.3.3 (August 2012)
* 1.4.1 (July 2012)
* 1.3.2 (July 2012)
* 1.4 (March 2012)

Great Documentation
-------------------

Thorough, readable, and discoverable.

.. class:: incremental

Led the way to better documentation for all Python

.. class:: incremental

`Read The Docs <https://readthedocs.org/>`_ - built in connection with
Django, sponsored by the Django Software Foundation.

.. class:: incremental

Write documentation as part of your python package, and render new versions of
that documentation for every commit

.. class:: incremental center

**this is awesome**

History
-------

Django was created to power the website of the Lawrence Journal-World
newspaper, Lawrence, KS

.. class:: incremental

This birth in practicality is reflected in the design of the system.

.. class:: incremental

Pretty much every design decision was made to solve a real problem.

.. class:: incremental

You can read more in `this Quora post
<http://www.quora.com/What-is-the-history-of-the-Django-web-framework>`_

Django Organization
-------------------

Django is organized into *projects* and *apps*

.. class:: incremental

A Django *project* represents the totality of a website, all the pages it 
will contain and all the functionality it supports

.. class:: incremental

A Django *app* represents an individual unit of functionality: a blog, a
forum, a registration system, a content tagging system, etc.

.. class:: incremental

One *project* can (and likely will) consist of many *apps*

Starting a Project
------------------

You should already have done this at home, but we'll look at it together in
case:

.. class:: incremental

* Set up a Django virtualenv
* Activate that env and ``pip install django``
* Create a new Django project:

.. code-block::
    :class: incremental

    (djangoenv)$ django-admin.py startproject mysite

.. class:: incremental

This will create a folder called 'mysite'.  Let's take a look at it:

Project Layout
--------------

The folder created by *django-admin.py* contains the following structure:

.. code-block::

    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py

.. class:: incremental

If what you see doesn't match that, you're using an older version of Django.
Make sure you've installed 1.4.3.

*django-admin.py* and *manage.py*
---------------------------------

*django-admin.py* provides a hook for administrative tasks and abilities:

.. class:: incremental

* creating a new project or app
* running the development server
* executing tests
* entering a python interpreter
* entering a database shell session with your database
* much much more (run ``django-admin.py`` without an argument)

.. class:: incremental

*manage.py* wraps this functionality, adding the full environment of your
project.

Development Server
------------------

At this point, you should be ready to use the development server::

    (djangoenv)$ cd mysite
    (djangoenv)$ python manage.py runserver
    ...

.. class:: incremental

Load ``http://localhost:8000`` in your browser.

A Blank Slate
-------------

You should see this:

.. image:: img/django-start.png
    :align: center
    :width: 98%

.. class:: incremental center

**Do you?**

Connecting A Database
---------------------

Django comes with its own ORM (Object-Relational Mapper)

.. class:: incremental

The first step in working with Django is to connect it to your database (this
is set in ``settings.py``)

.. code-block:: python
    :class: small incremental

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.<your_db_backend>',
            'NAME': '<your_db_name>',
            'USER': '<your_db_user>',
            'PASSWORD': '<your_db_password>',
            'HOST': '<not_needed_on_localhost>',
            'PORT': '<not_needed_on_localhost>',
        }
    }

Building DB Tables
------------------

The Django ORM builds tables. Django models describe the objects you want, the
ORM does the rest.

.. class:: incremental

Django comes with some *apps* set up and ready to use. These define models,
and need tables to power them. You create the tables by running the management
command *syncdb*:

.. class:: incremental

::

    (djangoenv)$ python manage.py syncdb

.. class:: incremental

Add your first admin user when prompted (remember the password)

scraps
------

- manage.py startproject

- manage.py startapp

connecting to a database

writing models

writing views

writing tests

what next?

