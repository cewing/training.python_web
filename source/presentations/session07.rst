Python Web Programming
======================

.. image:: img/django-pony.png
    :align: left
    :width: 50%

Day 4 AM: Introducing Django

.. class:: intro-blurb right

Wherein we become 'perfectionists with deadlines'

.. class:: image-credit

image: http://djangopony.com/


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
* User authentication and authorization 

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

The Django Admin is a great example of the Pareto Priciple, a.k.a. the 80/20
rule:

.. class:: incremental center

**80% of the problems can be solved by 20% of the effort**

.. class:: incremental

The converse also holds true:

.. class:: incremental center

**Fixing the last 20% of the problems will take the remaining 80% of the
effort.**


Other Django Advantages
-----------------------

Clearly the most popular full-stack Python web framework at this time

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

Django releases in the last 12+ months:

.. class:: incremental

* 1.5.1 (March 2013)
* 1.5 (February 2013)
* 1.4.5 (February 2013)
* 1.3.7 (February 2013)
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


Django Organization
-------------------

A Django *project* represents a whole website:

.. class:: incremental

* global configuration settings
* inclusion points for additional functionality
* master list of URL endpoints

.. class:: incremental

A Django *app* encapsulates a unit of functionality:

.. class:: incremental

* A blog section
* A discussion forum
* A content tagging system


Apps Make Up a Project
----------------------

.. class:: big-centered

One *project* can (and likely will) consist of many *apps*


Practice Safe Development
-------------------------

We'll install Django and any other packages we use with it in a virtualenv.

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

    $ python virtualenv.py djangoenv
    <or>
    $ virtualenv djangoenv
    ...

.. container:: incremental

    Then, activate it::

        $ source djangoenv/bin/activate
        <or>
        C:\> djangoenv\Scripts\activate


Install Django
--------------

Finally, install Django 1.5.1 using `setuptools` or `pip`:

.. class:: small

::

    (djangoenv)$ pip install Django==1.5.1
    Downloading/unpacking Django==1.5.1
      Downloading Django-1.5.1.tar.gz (8.0MB): 8.0MB downloaded
      Running setup.py egg_info for package Django
         changing mode of /path/to/djangoenv/bin/django-admin.py to 755
    Successfully installed Django
    Cleaning up...
    (djangoenv)$


Starting a Project
------------------

Everything in Django stems from the *project*

.. class:: incremental

To get started learning, we'll create one

.. class:: incremental

We'll use a script installed by Django, ``django-admin.py``:

.. code-block::
    :class: incremental

    (djangoenv)$ django-admin.py startproject mysite

.. class:: incremental

This will create a folder called 'mysite'.  Let's take a look at it:


Project Layout
--------------

The folder created by ``django-admin.py`` contains the following structure:

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
Make sure you've installed 1.5.1.


What Got Created
----------------

.. class:: incremental

* **outer *mysite* folder**: this is just a container and can be renamed or
  moved at will
* **inner *mysite* folder**: this is your project directory. It should not be
  renamed.
* **__init__.py**: magic file that makes *mysite* a python package.
* **settings.py**: file which holds configuration for your project, more soon.
* **urls.py**: file which holds top-level URL configuration for your project,
  more soon.
* **wsgi.py**: binds a wsgi application created from your project to the
  symbol ``application``
* **manage.py**: a management control script.


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


A Quick Word about Databases
----------------------------

Sqlite3 is **not** a production-capable database. Do not attempt to use it as
such. 

.. class:: incremental

Do not start a real project using sqlite3, expecting to move 'when you go to
production'.

.. class:: incremental

That being said, proper database administration is out-of-scope for this
class. 

.. class:: incremental

So we'll be using sqlite3 for todays work.


Your Database Settings
----------------------

Edit ``settings.py`` in your project package to match:

.. code-block:: python
    :class: small
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mysite.db',
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }


Django and Your Database
------------------------

Django interfaces with the database using an ORM (Object Relational Mapping)

.. class:: incremental

You write Python *models* describing the object that make up your system.

.. class:: incremental

The ORM handles converting data from these objects into SQL statements (and
back)

.. class:: incremental

We'll learn much more about this in a bit


Core Django *Apps*
------------------

Django already includes some *apps* for you.

.. container:: incremental

    They're ``settings.py`` in the ``INSTALLED_APPS`` setting:

    .. code-block:: python
        :class: small
    
        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            # Uncomment the next line to enable the admin:
            # 'django.contrib.admin',
            # Uncomment the next line to enable admin documentation:
            # 'django.contrib.admindocs',
        )


Creating the Database
---------------------

These *apps* define models of their own, tables must be created.

.. container:: incremental

    You make them by running the ``syncdb`` management command:
    
    .. class:: small
    
    ::

        (djangoenv)$ python manage.py syncdb
        Creating tables ...
        Creating table auth_permission
        Creating table auth_group_permissions
        Creating table auth_group
        ...
        You just installed Django's auth system, ...
        Would you like to create one now? (yes/no): 

.. class:: incremental

Add your first user at this prompt (remember the password)

