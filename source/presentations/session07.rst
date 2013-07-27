Python Web Programming
======================

.. image:: img/django-pony.png
    :align: left
    :width: 50%

Session 7: Introducing Django

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


Django and WSGI
---------------

If you open ``wsgi.py``, you'll see the following:

.. code-block:: python
    :class: small

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

.. container:: incremental

    Django is pointing the python environment at your settings file and then
    getting a wsgi application:

    .. code-block:: python
        :class: small

        def get_wsgi_application():
            return WSGIHandler()


The Django WSGIHandler
----------------------
.. code-block:: python
    :class: tiny

    class WSGIHandler(base.BaseHandler):
        #...
        def __call__(self, environ, start_response):
            if self._request_middleware is None:
                #... set up django middleware
            #...
            try:
                request = self.request_class(environ)
            except UnicodeDecodeError:
                #...
                response = http.HttpResponseBadRequest()
            else:
                response = self.get_response(request)
            #...
            try:
                status_text = STATUS_CODE_TEXT[response.status_code]
            except KeyError:
                status_text = 'UNKNOWN STATUS CODE'
            status = '%s %s' % (response.status_code, status_text)
            response_headers = [(str(k), str(v)) for k, v in response.items()]
            for c in response.cookies.values():
                response_headers.append((str('Set-Cookie'), str(c.output(header=''))))
            start_response(force_str(status), response_headers)
            return response


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

You can override methods from the base ``Model`` class to alter how this works
or write new methods to add functionality.

.. class:: incremental

Learn more about `models
<https://docs.djangoproject.com/en/1.5/topics/db/models/>`_


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


Hooking it Up
-------------

In order to use our new models, we need Django to know about our *app*

.. class:: incremental

This is accomplished by configuration in the ``settings.py`` file.

.. class:: incremental

Open that file now, in your editor, and find the INSTALLED_APPS setting.


Installing Apps
---------------

You extend Django functionality by *installing apps*. This is pretty simple:

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
        'myblog', # <- YOU ADD THIS PART
    )


Setting Up the Database
-----------------------

You know what the next step will be:

.. code-block::
    :class: incremental

    (djangoenv)$ python manage.py syncdb
    Creating tables ...
    Creating table myblog_post
    Creating table myblog_category_posts
    Creating table myblog_category
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)

.. class:: incremental

Django has now created tables for our app.  How many did it create?


ORM and SQL
-----------

That third table is the SQL mechanism by which a ``Post`` is related to a
``Category``.

.. class:: incremental

The ORM shields us, as Python developers, from SQL intricacies.

.. class:: incremental

We don't need to know that a join table is needed for a ManyToMany relation.

.. class:: incremental

This is but one of the ways that the ORM helps us.  More soon.


A Word About Development
------------------------

These models we've created are not going to change often. This is unusual for
a development cycle.

.. class:: incremental

The ``syncdb`` management command only creates tables that *do not yet exist*.
It **does not update tables**.

.. class:: incremental

The ``sqlclear <appname>`` command will print the ``DROP TABLE`` statements to
remove the tables for your app.

.. class:: incremental

Or ``sql <appname>`` will show the ``CREATE TABLE`` statements, and you can work
out the differences and update manually.


ACK!!!
------

That doesn't sound very nice, does it?

.. class:: incremental

Luckily, there is an app available for Django that helps with this: ``South``

.. class:: incremental

South allows you to incrementally update your database in a simplified way.

.. class:: incremental

South supports forward, backward and data migrations.

.. class:: incremental

We'll learn a bit more about this in our next session.


Break Time
----------

.. class:: big-centered

Let's take a break here and return in 10 minutes.


The Django Shell
----------------

Django provides a management command ``shell``:

.. class:: incremental

* Shares the same ``sys.path`` as your project, so all installed python
  packages are present.
* Imports the ``settings.py`` file from your project, and so shares all
  installed apps and other settings.
* Handles connections to your database, so you can interact with live data
  directly.

.. class:: incremental

Let's explore the Model Instance API directly using this shell:

.. class:: incremental

::

    (djangoenv)$ python manage.py shell


Creating Instances
------------------

Instances of our model can be created by simple instantiation:

.. code-block:: python
    :class: small

    >>> from myblog.models import Post
    >>> p1 = Post(title="My first post",
    ...           text="This is the first post I've written")
    >>> p1
    <Post: Post object>

.. container:: incremental

    We can also validate that our new object is okay before we try to save it:

    .. code-block:: python
        :class: small

        >>> p1.full_clean()
        Traceback (most recent call last):
          ...
        ValidationError: {'author': [u'This field cannot be null.']}


Django Model Managers
---------------------

We have to hook our ``Post`` to an author, which must be a ``User``.

.. class:: incremental

To do this, we need to have an instance of the ``User`` class.

.. class:: incremental

We can use the ``User`` *model manager* to run table-level operations like
``SELECT``:

.. class:: incremental

All Django models have a *manager*. By default it is accessed through the
``objects`` class attribute.


Making a ForeignKey Relation
----------------------------

Let's use the *manager* to get an instance of the ``User`` class:

.. code-block:: python
    :class: small

    >>> from django.contrib.auth.models import User
    >>> all_users = User.objects.all()
    >>> all_users
    [<User: cewing>]
    >>> u1 = all_users[0]
    >>> p1.author = u1

.. container:: incremental

    And now our instance should validate properly:

    .. code-block:: python
        :class: small

        >>> p1.full_clean()
        >>> 


Saving New Objects
------------------

Our model has three date fields, two of which are supposed to be
auto-populated:

.. class:: python
    :class: small
    
    >>> print(p1.created_date)
    None
    >>> print(p1.modified_date)
    None

.. container:: incremental

    When we save our post, these fields will get values assigned:
    
    .. code-block:: python
        :class: small
    
        >>> p1.save()
        >>> p1.created_date
        datetime.datetime(2013, 7, 26, 20, 2, 38, 104217, tzinfo=<UTC>)
        >>> p1.modified_date
        datetime.datetime(2013, 7, 26, 20, 2, 38, 104826, tzinfo=<UTC>)


Updating An Instance
--------------------

Models operate much like 'normal' python objects.

.. container:: incremental

    To change the value of a field, simply set the instance attribute to a new
    value. Call ``save()`` to persist the change:

    .. code-block:: python
        :class: small
    
        >>> p1.title = p1.title + " (updated)"
        >>> p1.save()
        >>> p1.title
        'My first post (updated)'


Create a Few Posts
------------------

Let's create a few more posts so we can explore the Django model manager query
API:

.. code-block:: python
    :class: small

    >>> p2 = Post(title="Another post",
    ...           text="The second one created",
    ...           author=u1).save()
    >>> p3 = Post(title="The third one",
    ...           text="With the word 'heffalump'",
    ...           author=u1).save()
    >>> p4 = Post(title="Posters are great decoration",
    ...           text="When you are a poor college student",
    ...           author=u1).save()
    >>> Post.objects.count()
    4


The Django Query API
--------------------

The *manager* on each model class supports a full-featured query API.

.. class:: incremental

API methods take keyword arguments, where the keywords are special
constructions combining field names with field *lookups*:

.. class:: incremental small

* title__exact="The exact title"
* text__contains="decoration"
* id__in=range(1,4)
* published_date__lte=datetime.datetime.now()

.. class:: incremental

Each keyword argument generates an SQL clause.


QuerySets
---------

API methods can be divided into two basic groups: methods that return
``QuerySets`` and those that do not.

.. class:: incremental

The former may be chained without hitting the database:

.. code-block:: python
    :class: small incremental

    >>> a = Post.objects.all() #<-- no query yet
    >>> b = a.filter(title__icontains="post") #<-- not yet
    >>> c = b.exclude(text__contains="created") #<-- nope
    >>> [(p.title, p.text) for p in c] #<-- This will issue the query

.. container:: incremental

    Conversely, the latter will issue an SQL query when executed.

    .. code-block:: python
        :class: small
    
        >>> a.count() # immediately executes an SQL query


QuerySets and SQL
-----------------

If you are curious, you can see the SQL that a given QuerySet will use:

.. code-block:: python
    :class: small incremental

    >>> print(c.query)
    SELECT "myblog_post"."id", "myblog_post"."title", 
        "myblog_post"."text", "myblog_post"."author_id", 
        "myblog_post"."created_date", "myblog_post"."modified_date", 
        "myblog_post"."published_date" 
    FROM "myblog_post" 
    WHERE ("myblog_post"."title" LIKE %post% ESCAPE '\'
           AND NOT ("myblog_post"."text" LIKE %created% ESCAPE '\' )
    )

.. class:: incremental

The exact SQL will vary automatically depending on the database you are using.


Exploring the QuerySet API
--------------------------

See https://docs.djangoproject.com/en/1.5/ref/models/querysets


.. code-block:: python
    :class: small

    >>> [p.pk for p in Post.objects.all().order_by('created_date')]
    [1, 2, 3, 4]
    >>> [p.pk for p in Post.objects.all().order_by('-created_date')]
    [4, 3, 2, 1]
    >>> [p.pk for p in Post.objects.filter(title__contains='post')]
    [1, 2, 4]
    >>> [p.pk for p in Post.objects.exclude(title__contains='post')]
    [3]
    >>> qs = Post.objects.exclude(title__contains='post')
    >>> qs = qs.exclude(id__exact=3)
    >>> [p.pk for p in qs]
    []
    >>> qs = Post.objects.exclude(title__contains='post', id__exact=3)
    >>> [p.pk for p in qs]
    [1, 2, 3, 4]


Updating via QuerySets
----------------------

You can update all selected objects at the same time.

.. class:: incremental

Changes are persisted without needing to call ``save``.

.. code-block:: python
    :class: small incremental

    >>> qs = Post.objects.all()
    >>> [p.published_date for p in qs]
    [None, None, None, None]
    >>> from datetime import datetime
    >>> from django.utils.timezone import UTC
    >>> utc = UTC()
    >>> now = datetime.now(utc)
    >>> qs.update(published_date=now)
    4
    >>> [p.published_date for p in qs]
    [datetime.datetime(2013, 7, 27, 1, 20, 30, 505307, tzinfo=<UTC>),
     ...]


Testing Our Models
------------------

As with any project, we want to test our work. Django provides a testing
framework to allow this.

.. class:: incremental

Django supports both *unit tests* and *doctests*. I strongly suggest using
*unit tests*.

.. class:: incremental

You add tests for your *app* to the file ``tests.py``, which should be at the
same package level as ``models.py``.

.. class:: incremental

Locate and open this file in your editor.


Django TestCase Classes
-----------------------

**SimpleTestCase** is for basic unit testing with no ORM requirements

.. class:: incremental

**TransactionTestCase** is useful if you need to test transactional
actions (commit and rollback) in the ORM

.. class:: incremental

**TestCase** is used when you require ORM access and a test client

.. class:: incremental

**LiveServerTestCase** launches the django server during test runs for
front-end acceptance tests.


Testing Data
------------

Sometimes testing requires base data to be present. We need a User for ours.

.. class:: incremental

Django provides *fixtures* to handle this need.

.. class:: incremental

Create a directory called ``fixtures`` inside your ``myblog`` app directory.

.. class:: incremental

Copy the file ``myblog_test_fixture.json`` from the class resources into this
directory, it contains a user for us.


Setting Up Our Tests
--------------------

Now that we have a fixture, we need to instruct our tests to use it.

.. container:: incremental

    Edit ``tests.py`` (which comes with one test already) to look like this:

    .. code-block:: python
        :class: small

        from django.test import TestCase
        from django.contrib.auth.models import User
    
        class PostTestCase(TestCase):
            fixtures = ['myblog_test_fixture.json', ]

            def setUp(self):
                self.user = User.objects.get(pk=1)


Our First Enhancement
---------------------

Look at the way our Post represents itself in the Django shell:

.. code-block:: python
    :class: small 

    >>> [p for p in Post.objects.all()]
    [<Post: Post object>, <Post: Post object>, 
     <Post: Post object>, <Post: Post object>]

.. class:: incremental

Wouldn't it be nice if the posts showed their titles instead?

.. class:: incremental

In Django, the ``__unicode__`` method is used to determine how a Model
instance represents itself.

.. class:: incremental

Then, calling ``unicode(instance)`` gives the desired result.


Write The Test
--------------

Let's write a test that demonstrates our desired outcome:

.. code-block:: python
    :class: small
    
    # add this import at the top
    from myblog.models import Post

    # and this test method to the PostTestCase
    test_unicode(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = unicode(p1)
        self.assertEqual(expected, actual)


Run The Test
------------

To run tests, use the ``test`` management command

.. class:: incremental

Without arguments, it will run all TestCases it finds in all installed *apps*

.. class:: incremental

You can pass the name of a single app to focus on those tests

.. class:: incremental

Quit your Django shell and in your terminal run the test we wrote:

.. code-block:: bash
    :class: small incremental

    (djangoenv)$ python manage.py test myblog


The Result
----------

We have yet to implement this enhancement, so our test should fail:

.. class:: small

::

    Creating test database for alias 'default'...
    F
    ======================================================================
    FAIL: test_unicode (myblog.tests.PostTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/cewing/projects/training/uw_pce/training.python_web/scripts/session07/mysite/myblog/tests.py", line 15, in test_unicode
        self.assertEqual(expected, actual)
    AssertionError: 'This is a title' != u'Post object'

    ----------------------------------------------------------------------
    Ran 1 test in 0.007s

    FAILED (failures=1)
    Destroying test database for alias 'default'...


Make it Pass
------------

Let's add an appropriate ``__unicode__`` method to our Post class

.. class:: incremental

It will take ``self`` as its only argument

.. class:: incremental

And it should return its own title as the result

.. class:: incremental

Go ahead and take a stab at this in ``models.py``

.. code-block:: python
    :class: small incremental
    
    class Post(models.Model):
        #... 

        def __unicode__(self):
            return self.title


Did It Work?
------------

Re-run the tests to see:

.. code-block:: bash
    :class: small

    (djangoenv)$ python manage.py test myblog
    Creating test database for alias 'default'...
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.007s

    OK
    Destroying test database for alias 'default'...

.. class:: incremental center

**YIPEEEE!**


Repeat the Exercise
-------------------

Although we haven't played with it yet, our Category class could use the same
treatment, using the ``name`` field.

.. class:: incremental

Add a CategoryTestCase to ``tests.py`` with one test that shows this.

.. class:: incremental

Run the tests, demonstrating that you have two tests and one failure

.. class:: incremental

Add the appropriate method to the appropriate class in ``models.py`` and
re-run the tests.


My Test
-------

.. code-block:: python
    :class: incremental
    
    # another import
    from myblog.models import Category
    
    # and the test case and test
    class CategoryTestCase(TestCase):

        def test_unicode(self):
            expected = "A Category"
            c1 = Category(name=expected)
            actual = unicode(c1)
            self.assertEqual(expected, actual)


My Method
---------

.. code-block:: python

    class Category(models.Model):
        #... 
        
        def __unicode__(self):
            return self.name


What to Test
------------

In any framework, the question arises of what to test. Much of your app's
functionality is provided by framework tools. Does that need testing?

.. class:: incremental

I *usually* don't write tests covering features provided directly by the
framework.

.. class:: incremental

I *do* write tests for functionality I add, and for places where I make
changes to how the default functionality works.

.. class:: incremental

This is largely a matter of style and taste (and of budget).


More Later
----------

We've only begun to test our blog app.

.. class:: incremental

We'll be adding many more tests later

.. class:: incremental

In between, you might want to take a look at the Django testing documentation:

.. class:: incremental center

https://docs.djangoproject.com/en/1.5/topics/testing/


The Django Admin
----------------

As I stated earlier, the Django admin is really Django's *killer feature*

.. class:: incremental

To demonstrate this, we are going to set up the admin for our blog


Install the Admin
-----------------

The Django Admin is, itself, an *app*. It is not installed by default.  

.. class:: incremental

Open the ``settings.py`` file from our ``mysite`` project package and
uncomment the admin bit:

.. code-block:: python
    :class: incremental small

    INSTALLED_APPS = (
        # ...
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin', # <- THIS LINE HERE
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        'myblog',
    )


Add the Admin Tables
--------------------

As you might expect, enabling the admin alters our DB. We'll need to run
the ``syncdb`` management command::

    (djangoenv)$ python manage.py syncdb
    Creating tables ...
    Creating table django_admin_log
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)

.. class:: incremental

All set.  Now let's make it visitable


Django URL Resolution
---------------------

Django too has a system for routing URLs to code: the *urlconf*.

.. class:: incremental

* A urlconf is a list of calls to the ``django.conf.urls.url`` function
* This function takes:
  
  * a regexp *rule*, representing the URL
  
  * a ``callable`` to be invoked (or a name identifying one)
  
  * an optional *name* kwarg, used to *reverse* the URL
  
  * other optional arguments we will skip for now

* The function returns a *resolver* that matches the request path to the
  callable
* django will load the urlconf named ``urlpatterns`` that it finds in the file
  named in ``settings.ROOT_URLCONF``. 


Including URLs
--------------

Many Django add-on *apps*, like the Django Admin, come with their own urlconf

.. class:: incremental

It is standard to include these urlconfs by rooting them at some path in your
site.

.. container:: incremental

    You can do this by using the ``include`` function as the callable in a
    ``url`` call:

    .. code-block:: python
        :class: small

        url(r'^forum/', include('random.forum.app.urls'))


Including the Admin
-------------------

We can use this to add *all* the URLs provided by the Django admin in one
stroke.

.. container:: incremental

    Uncomment three lines in ``urls.py``:

    .. code-block:: python
        :class: small

        from django.contrib import admin #<- Uncomment these two
        admin.autodiscover()             #<-

        urlpatterns = patterns('',

            # Uncomment the next line to enable the admin:
            url(r'^admin/', include(admin.site.urls)), #<- and this
        )


Using the Development Server
----------------------------

We can now view the admin.  We'll use the Django development server.

.. class:: incremental

In your terminal, use the ``runserver`` management command to start the
development server:

.. class:: incremental

::

    (djangoenv)$ python manage.py runserver
    Validating models...

    0 errors found
    Django version 1.4.3, using settings 'mysite.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


Viewing the Admin
-----------------

Load ``http://localhost:8000/``.  You should see this:

.. image:: img/django-admin-login.png
    :align: center
    :width: 50%

.. class:: incremental

Login with the name and password you created before.


The Admin Index
---------------

The index will provide a list of all the installed *apps* and each model
registered.  You should see this:

.. image:: img/admin_index.png
    :align: center
    :width: 90%

.. class:: incremental

Click on ``Users``. Find yourself? Edit yourself, but **don't** uncheck
``superuser``.


Add Posts to the Admin
----------------------

Okay, let's add our app models to the admin.

.. class:: incremental

Add a new file to the ``myblog`` app package: ``admin.py``. Open it and add
the following:

.. code-block:: python
    :class: incremental

    from django.contrib import admin
    from myblog.models import Post, Category

    admin.site.register(Post)
    admin.site.register(Category)

.. class:: incremental

Restart your Development server and reload the admin index


Play A Bit
----------

Visit the admin page for Posts. You should see the posts we created earlier in
the Django shell.

.. class:: incremental

Look at the listing of Posts. Because of our ``__unicode__`` method we see a
nice title.

.. class:: incremental

Are there other fields you'd like to see listed?

.. class:: incremental

Click on a Post, note what is and is not shown.

.. class:: incremental

Poke at the Category admin a bit too.


Next Steps
----------

We've learned a great deal about Django's ORM and Models.

.. class:: incremental

We've also spent some time getting to know the Query API provided by model
managers and QuerySets.

.. class:: incremental

We've also hooked up the Django Admin and noted some shortcomings.

.. class:: incremental

In our next session we'll improve how the admin works for us.

.. class:: incremental

Then we'll put a front-end on this blog.


Break Time
----------

.. class:: big-centered

See you back soon.
