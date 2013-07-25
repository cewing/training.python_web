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

    They're in ``settings.py`` in the ``INSTALLED_APPS`` setting:

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


Our Class App
-------------

We are going to build an *app* to add to our *project*. To start with our app
will:

.. class:: incremental

* allow a user to create and edit blog posts
* allow a user to define categories
* allow a user to place a post in one or more categories

.. class:: incremental

As stated above, an *app* represents a unit within a system, the *project*. We
have a project, we need to create an *app*


Create an App
-------------

This is accomplished using ``manage.py``.

.. class:: incremental

In your terminal, make sure you are in the *outer* mysite directory, where the
file ``manage.py`` is located.  Then:

.. class:: incremental

::

    (djangoenv)$ python manage.py startapp myblog


What is Created
---------------

This should leave you with the following structure:

.. class:: small

::

    mysite/
        manage.py
        mysite/
            ...
        myblog/
            __init__.py
            models.py
            tests.py
            views.py

.. class:: incremental

We'll start by defining the main Python class in our blog system, a ``Post``.


Django Models
-------------

Any Python class in Django that is meant to be persisted *must* inherit from 
the Django ``Model`` class.

.. class:: incremental

This base class provides all the functionality that connects the Python code
you write to your database.

.. class:: incremental

You can override methods from the base ``Model`` class to alter how this works.

.. class:: incremental

You can also write new methods on your class that provide new functionality.


Our Post Model
--------------

Open the ``models.py`` file created in our ``myblog`` package. Add the
following:

.. code-block:: python
    :class: small

    from django.db import models
    from django.contrib.auth.models import User
    
    class Post(models.Model):
        title = models.CharField(max_length=128)
        text = models.TextField(blank=True)
        author = models.ForeignKey(User)
        created_date = models.DateTimeField(auto_now_add=True)
        modified_date = models.DateTimeField(auto_now=True)
        published_date = models.DateTimeField(blank=True, null=True)


Model Fields
------------

We've created a subclass of the Django ``Model`` class and added a bunch of
attributes.

.. class:: incremental

* These attributes are all instances of ``Field`` classes defined in Django
* Field attributes on a model map to columns in a database table
* The arguments you provide to each Field customize how it works

  * This means *both* how it operates in Django *and* how it is defined in SQL

* There are arguments shared by all Field types
* There are also arguments specific to individual types

.. class:: incremental

You can read much more about `Model Fields and options
<https://docs.djangoproject.com/en/1.5/ref/models/fields/>`_


Field Details
-------------

There are some features of our fields worth mentioning in specific:

.. class:: incremental

Notice we have no field that is designated as the *primary key*

.. class:: incremental

* You *can* make a field the primary key by adding ``primary_key=True`` in the
  arguments
* If you do not, Django will automatically create one. This field is always
  called ``id``
* No matter what the primary key field is called, its value is always
  available on a model instance as ``pk``


Field Details
-------------

.. code-block:: python
    :class: small
    
    title = models.CharField(max_length=128)

.. class:: incremental

The required ``max_length`` argument is specific to ``CharField`` fields.

.. class:: incremental

It affects *both* the Python and SQL behavior of a field.

.. class:: incremental

In python, it is used to *validate* supplied values during *model validation*

.. class:: incremental

In SQL it is used in the column definition: ``VARCHAR(128)``


Field Details
-------------

.. code-block:: python
    :class: small

    text = models.TextField(blank=True)
    # ...
    published_date = models.DateTimeField(blank=True, null=True)

.. class:: incremental

The argument ``blank`` is shared across all field types. The default is
``False``

.. class:: incremental

This argument affects only the Python behavior of a field, determining if the 
field is *required*

.. class:: incremental

The related ``null`` argument affects the SQL definition of a field: is the
column NULL or NOT NULL


Field Details
-------------

.. code-block:: python
    :class: small

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

.. class:: incremental

``auto_now_add`` is available on all date and time fields. It sets the value
of the field to *now* when an instance is first saved.

.. class:: incremental

``auto_now`` is similar, but sets the value anew each time an instance is
saved.

.. class:: incremental

Setting either of these will cause the ``editable`` attribute of a field to be
set to ``False``.


Field Details
-------------

.. code-block:: python
    :class: small

    author = models.ForeignKey(User)

.. class:: incremental

Django also models SQL *relationships* as specific field types.

.. class:: incremental

The required positional argument is the class of the related Model.

.. class:: incremental

By default, the reverse relation is implemented as the attribute
``<fieldname>_set``.

.. class:: incremental

You can override this by providing the ``related_name`` argument.


Our Category Model
------------------

Our app specification says that a user should be able to place a post in one
or more categories.

.. class:: incremental

We'll create a second Model to represent this. It should:

.. class:: incremental

* Have a unique name
* Have a description
* Be in a many-to-many relationship with our ``Post`` model
* Instances of ``Category`` should have a ``posts`` attribute that provides
  access to all posts in that category
* Instances of ``Post`` should have a ``categories`` attribute that provides
  access to all the categories it has been placed in.


My Solution
-----------

Add this new Model class to ``models.py``.

.. class:: incremental small

https://docs.djangoproject.com/en/1.5/ref/models/fields/

.. container:: incremental

    Here's my model code:

    .. code-block:: python
        :class: small

        class Category(models.Model):
            name = models.CharField(max_length=128)
            description = models.TextField(blank=True)
            posts = models.ManyToManyField(Post, 
                blank=True,
                null=True,
                related_name='categories'
            )

