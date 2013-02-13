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

You should already have done this at home, but we'll look at it together
quickly, in case:

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
* **wsgi.py**: the .wsgi file which allows your project to be run in a wsgi
  server, like mod_wsgi.
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
such. Do not start a real project using sqlite3, expecting to move 'when
you go to production'.

.. class:: incremental

That being said, proper database administration is out-of-scope for this
class. If you haven't already got a PostgreSQL or MySQL database set up and
ready to use, just use sqlite3 so we can get through this.

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

Lab
---

The remainder of our class today will be lab time. We'll be directly playing
with Django from here on out.

Todays lab is drawn from the `Django Tutorial
<https://docs.djangoproject.com/en/1.4/intro/tutorial01/>`_, with some minor
adjustments.

Lab - Part One
--------------

We are going to create an *app* to add to our *project*.  This app will:

.. class:: incremental

* Allow a user to create poll questions
* Allow a user to provide choices for these questions
* Allow visitors to a site to see these questions and vote for an answer
* Allow the total vote tallies for the answers to a poll question to be
  displayed.

.. class:: incremental

As stated above, an *app* should represent a unit of functionality within a
larger system, the *project*.  We have a project, we need to create an *app*

Create an App
-------------

This is accomplished using ``manage.py``.

.. class:: incremental

In your terminal, make sure you are in the *outer* mysite directory, where the
file ``manage.py`` is located.  Then:

.. class:: incremental

::

    (djangoenv)$ python manage.py startapp polls

What is Created
---------------

This should leave you with the following structure:

.. class:: small

::

    mysite/
        manage.py
        mysite/
            ...
        polls/
            __init__.py
            models.py
            tests.py
            views.py

.. class:: incremental

We'll start by defining the objects we will work with: poll questions and
choices.

Models
------

Open the file ``models.py`` in your editor, and add the following code:

.. code-block:: python

    from django.db import models
    
    class Poll(models.Model):
        question = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
    
    class Choice(models.Model):
        poll = models.ForeignKey(Poll)
        choice = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)

Model Details
-------------

Let's look at that a bit more closely:

.. code-block:: python
    :class: small incrmental

    class Poll(models.Model):

.. class: incremental small

* Our Models are Python classes that inherit from the Model class
* The ``Model`` class provides a standard API for interacting with a database,
  centered on the object defined by the model.
* You can add functionality to your object by adding methods to these models.
* Consider methods added to a model to be row-level operations. They will work
  on a single record from the database, not on entire tables
* You can read much more about the `Model API
  <https://docs.djangoproject.com/en/1.4/ref/models/instances/>`_

Field Details
-------------

A model has attributes defined by ``Fields``:

.. code-block:: python
    :class: small

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    poll = models.ForeignKey(Poll)
    votes = models.IntegerField(default=0)

.. class:: incremental small

* Fields map to columns in a database table
* Note there are no explicit primary key fields. Django does this
  automatically
* Different field types map to different SQL column types, the ORM handles
  this.
* Django fields can handle complex relationships between objects.
* Field constructors take arguments, some are common to all Fields, others
  particular to a given Field type.
* **ALL** Django model fields default to being NOT NULL (required). You change
  this with the ``blank`` and ``null`` constructor arguments
* You can read much more about `Model Fields
  <https://docs.djangoproject.com/en/1.4/ref/models/fields/>`_

Hooking it Up
-------------

Okay, we've got a couple of models, now we need to add our *app* to our
project.

.. class:: incremental

In Django, this is accomplished by configuration.

.. class:: incremental

Configuration takes place in the project ``settings.py`` file.  

.. class:: incremental

Open that file now, in your editor.

Installing Apps
---------------

You extend Django functionality by *installing apps*. Find the following block
in ``settings.py`` and edit it like so:

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
        'polls', # <- YOU ADD THIS PART
    )

Setting Up the Database
-----------------------

By now, we should have some guess as to what the next step will be

.. code-block::
    :class: incremental

    (djangoenv)$ python manage.py syncdb

.. class:: incremental

This will execute the SQL commands needed to create the new tables in your
database.

A Word About Development
------------------------

These models we've created are not going to change. This is unusual for a
development cycle.

.. class:: incremental

The ``syncdb`` management command only creates tables that *do not yet exist*.
It **does not update tables**.

.. class:: incremental

It is easy to get your model definitions out of sync with your database.

.. class:: incremental

Django provides the management command ``sqlclear`` to handle this. It drops
all tables, so you can run ``syncdb`` again.

ACK!!!
------

.. class:: center

That doesn't sound very nice, does it?

.. class:: big-centered incremental

We'll learn a better way next week

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

Let's explore the Model Instance API directly using this shell

Model Instance API
------------------

::

    (djangoenv)$ python manage.py shell

.. code-block:: python

    >>> from polls.models import Poll
    >>> Poll.objects.count()
    0
    >>> p1 = Poll(question="What is your name?")
    >>> p1.full_clean()
    Traceback (most recent call last):
      ...
    >>> from django.utils import timezone
    >>> p1.pub_date = timezone.now()
    >>> p1.full_clean()
    >>> p1.save()
    >>> Poll.objects.count()
    1

More API
--------

.. code-block:: python
    :class: small

    >>> Poll.objects.filter(id=1)
    [<Poll: Poll object>]
    >>> what_polls = Poll.objects.filter(question__startswith="What")
    [<Poll: Poll object>]
    >>> mypoll = Poll.objects.get(pk=1)
    >>> mypoll.choice_set.all()
    []
    >>> from polls.models import Choice
    >>> c1 = Choice(choice="King Arthur of the Britons", poll=mypoll)
    >>> c1.save
    >>> mypoll.choice_set.all()
    [<Choice: Choice object>]
    >>> mypoll.choice_set.create(choice="Lancelot of Camelot")
    >>> mypoll.choice_set.all()
    [<Choice: Choice object>, <Choice: Choice object>]

Enhancing Models
----------------

It's clear that the representation of our objects leaves something to be
desired. Django can help

.. class:: incremental

Back in ``models.py``, add these methods:

.. code-block:: python
    :class: small incremental
    
    class Poll(models.Model):
        # ...
        def __unicode__(self):
            return self.question
    
    class Choice(models.Model):
        # ...
        def __unicode__(self):
            return self.choice

Model Methods
-------------

This ``__unicode__`` method is a normal python instance method. You can add
other methods, too (still ``models.py``):

.. code-block:: python
    :class: small incremental

    from django.utils import timezone
    
    class Poll(models.Model):
        # ...
        def published_today(self):
            now = timezone.now()
            time_delta = now - self.pub_date
            return time_delta.days == 0

.. class:: incremental

Save that, then start up the Django shell again (``python manage.py shell``)

Check Custom Methods
--------------------

.. code-block:: python

    >>> from polls.models import Poll
    >>> mypoll = Poll.objects.get(pk=1)
    >>> mypoll
    <Poll: What is your name?>
    >>> mypoll.choice_set.all()
    [<Choice: King Arthur of the Britons>, 
     <Choice: Lancelot of Camelot>, 
     <Choice: Robin of Camelot>]
    >>> mypoll.published_today()
    True

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

Locate and open this file in your editor.  We are going to add a few tests for
the models we've just written.

Testing Setup
-------------

.. code-block:: python
    :class: small

    from datetime import timedelta
    
    from django.test import TestCase
    from django.utils import timezone
    
    from polls.models import Poll

    class PollTest(TestCase):
        def setUp(self):
            self.expected_question = "what is the question?"
            self.expected_choice = "do you like spongecake?"
            self.poll = Poll.objects.create(
                question=self.expected_question,
                pub_date=timezone.now())
            self.choice = self.poll.choice_set.create(
                choice=self.expected_choice)

Writing Tests
-------------

.. code-block:: python
    :class: small
    
    def test_poll_display(self):
        self.assertEquals(unicode(self.poll), self.expected_question)
        new_question = "What is the answer?"
        self.poll.question = new_question
        self.assertEquals(unicode(self.poll), new_question)
    
    def test_choice_display(self):
        self.assertEquals(unicode(self.choice), self.expected_choice)
        new_choice = "is left better than right?"
        self.choice.choice = new_choice
        self.assertEquals(unicode(self.choice), new_choice)
    
    def test_published_today(self):
        self.assertTrue(self.poll.published_today())
        delta = timedelta(hours=26)
        self.poll.pub_date = self.poll.pub_date - delta
        self.assertFalse(self.poll.published_today())

Running Tests
-------------

You can run your tests using a management command provided by Django::

    (djangoenv)$ python manage.py test polls

.. class:: incremental

* This will run the tests for the ``polls`` app
* You can provide the name of any installed app
* If you provide no name, the tests for *all* installed apps will run
* You can run subsets by providing dotted names: ``polls.PollTest``,
  ``polls.PollTest.test_poll_display``

.. class:: incremental

There is a lot more to know about `Testing Django applications
<https://docs.djangoproject.com/en/1.4/topics/testing/>`_

What to Test
------------

In any framework, the question arises of what exactly to test. Much of the
functioning of your app is provided by framework tools. Do you need to test
that stuff?

.. class:: incremental

I *usually* don't write tests covering features provided directly by the
framework.

.. class:: incremental

I *do* write tests for functionality I add, and for places where I make
changes to how the default functionality works.

.. class:: incremental

This is largely a matter of style and taste (and of how much development time
you have).


Lab - Part Two
--------------

In this part, we'll be adding our app to the Django Admin.  This will allow
us to add, edit and delete objects with a minimum of work.

We'll focus instead on how to customize the admin to get the best results we
can.

Install the Admin
-----------------

The Django Admin is, itself, an *app*. It is not installed by default.  

.. class:: incremental

Open the ``settings.py`` file from our ``mysite`` project package and uncomment
the admin bit:

.. code-block:: python
    :class: incremental small

    INSTALLED_APPS = (
        # ...
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin', # <- THIS LINE HERE
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        'polls',
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

All set.  Let's add URLs next

Django URL Resolution
---------------------

Like Flas, Django has a system for routing URLs to code: the *urlconf*.

.. class:: incremental

* a urlconf is a list of mappings
* each mapping has a regexp *rule*, representing the URL
* each mapping names or provides the ``callable`` to be invoked
* each mapping can have a *name*, used to *reverse* the URL
* a urlconf should be created using functions from the ``django.conf.urls``
  module
* django will load the urlconf named ``urlpatterns`` that it finds in the file
  named in ``settings.ROOT_URLCONF``. 
* That urlconf must include any others it requires

Django URL Patterns
-------------------

Open the file ``urls.py`` from your ``mysite`` project package:

.. code-block:: python

    from django.conf.urls import patterns, include, url
    ...
    urlpatterns = patterns('',
        # list of url patterns
    )

.. class:: incremental

You can include lists of urls from installed apps by using the ``include``
function as the callable in a url pattern:

.. code-block:: python
    :class: incremental

    url(r'^blog/', include('my.blog.app.urls'))

Including the Admin
-------------------

Using this knowledge, we can add *all* the URLs provided by the Django admin
in one stroke. Edit ``urls.py``, which is open in your editor, and uncomment
three lines:

.. code-block:: python
    :class: incremental

    from django.contrib import admin #<- Uncomment these two
    admin.autodiscover()
    
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

Add Polls to the Admin
----------------------

Okay, let's add our app, and the models therein, to the admin.

.. class:: incremental

Add a new file to the ``polls`` app package: ``admin.py``. Edit it and add the
following:

.. code-block:: python
    :class: incremental

    from django.contrib import admin
    from polls.models import Poll, Choice

    admin.site.register(Poll)
    admin.site.register(Choice)

.. class:: incremental

Restart your Development server and reload the admin index

Customized Admin
----------------

The Django Admin displays ``ModelAdmin`` instances for any models that are
registered

.. class:: incremental

* The object ``admin.site`` is a global instance of the ``Admin`` class.
* Each call to ``admin.site.register`` adds a new model to the global *site*
* ``register`` takes two args: a *Model* subclass and a *ModelAdmin* subclass
* If you call it with only the *Model* subclass, the *ModelAdmin* is
  automatically generated.
* You can create, and customize, a *ModelAdmin* subclass for your models.

Create a PollAdmin
------------------

In ``admin.py`` add the following code (above the calls to ``register``):

.. code-block:: python

    class PollAdmin(admin.ModelAdmin):
        list_display = ('pub_date', 'question',
                        'published_today')
        list_filter = ('pub_date', )
        ordering = ('pub_date', )

.. class:: incremental

Then add this new class to the ``register`` call for our ``Poll``:

.. code-block:: python
    :class: incremental

    admin.site.register(Poll, PollAdmin)

More Convenient Relations
-------------------------

In our Admin site, you can see the ``Poll`` to which a ``Choice`` belongs.

.. class:: incremental

It'd be a lot nicer to be able to manage the ``Choices`` for a ``Poll`` from
the poll admin page, wouldn't it?

.. class:: incremental

The Django Admin provides a special type of ``ModelAdmin`` for just this
purpose: The ``InlineModelAdmin``.

.. class:: incremental

There are two flavors, *stacked* and *tabular*. The *tabular* version is more
compact as it displays each related object in a single table row.

Create a Choice Inline
----------------------

Add the following code *above* our ``PollAdmin`` class in ``admin.py``:

.. code-block:: python

    class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 3
        ordering = ('choice', )

Then, add the inline to ``PollAdmin``:

.. code-block:: python

    class PollAdmin(admin.ModelAdmin):
        # ...
        inlines = (ChoiceInline, )

Method Attributes for the Admin
-------------------------------

For example, methods of a class you use in the admin can have special
attributes that alter how it works. Make these changes to ``models.py``

.. code-block:: python

    class Poll(models.Model):
        ...
        def published_today(self):
            now = timezone.now()
            time_delta = now - self.pub_date
            return time_delta.days == 0
        published_today.boolean = True
        published_today.short_description = "Published Today?"


Reap the Rewards
----------------

Good work. You've set up a fully functional CRUD admin interface for your
application database in about 25 lines of code.

.. class:: incremental

Play with it for a bit.

Lab - Part Three
----------------

In this part, we'll add public views and set up a way for visitors to vote
in our poll.  

Along the way, we'll learn a bit about Django's *Generic Views* and the
*Django Templating Language*

Django Views
------------

Django views are callables that take a request and return a response.

.. class:: incremental

From the beginning, these have been functions.  They still can be.

.. class:: incremental

Version 1.3 added support for Class-based Views.

.. class:: incremental

Really, they've always been there implicitly. The Admin is just a big
class-based view.

Generic Views
-------------

One of the most common uses for Class-based Views is in creating Generic Views.

.. class:: incremental

Some public views are so common that providing a simple and generic interface
for making them is a big win.

.. class:: incremental

* Showing a list of objects of some type.
* Showing the details of a single object of some type.
* Displaying a static HTML template (or a template with some dynamic context)
* Displaying and processing a simple HTML form.

Our Application
---------------

We'd like to be able to add some views that show our polls to the public.

.. class:: incremental

What views would we like to have?

.. class:: incremental

* A list of all polls, perhaps ordered by publication date
* A display of a single poll, showing each choice and allowing a vote
* A view that processes a vote
* A view that shows the poll results after you vote.

.. class:: incremental

I start by configuring my URLs, it helps me think about the app API.

Configure URLs
--------------

In your ``polls`` app package, add a new file: ``urls.py``. Open it in an
editor:

.. code-block:: python
    :class: incremental small
    
    from django.conf.urls import patterns, url
    from django.http import HttpResponse

    def stub(request, *args, **kwargs):
        return HttpResponse('stub view', mimetype="text/plain")

    urlpatterns = patterns('',
        url(r'^$', stub, name="poll_list"),
        url(r'^(?P<pk>\d+)/$', stub, name="poll_detail"),
        url(r'^(?P<pk>\d+)/vote/$' stub, name="poll_vote"),
        url(r'^(?P<pk>\d+)/result/$', stub, name="poll_result"),
    )

Hook URLs to the Root
---------------------

Like with the Django Admin, we can now add all the urls for our poll app at
once.

.. class:: incremental

In the ``urls.py`` in our ``mysite`` project package, add the following:

.. code-block:: python
    :class: incremental small

    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^polls/', include('polls.urls')), # ADD
    )

.. class:: incremental

Restart the development server and load ``http://localhost:8000/polls/``

Generic Poll List
-----------------

Django's Generic Views allow you to do quite a lot with just a little code.
Edit ``urls.py``:

.. code-block:: python
    :class: incremental small

    # add this import
    from django.views.generic import ListView
    
    # edit the url pattern for the poll list:
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='polls',
            template_name="polls/list.html"
        ),
        name="poll_list"),

.. class:: incremental

Now, we just need to make that template

Django Templates
----------------

The `Django Template Language
<https://docs.djangoproject.com/en/1.4/topics/templates/>`_ looks a *lot* like
Jinja2. It is, however, quite a bit more limited.

.. class:: incremental

* variables available in context may be printed with ``{{ name }}``
* variables that are objects or dictionaries may be addressed with dots: ``{{
  name.attr }}``
* *filters* are available and look the same ``{{ name|upper }}``
* logical *tags*: ``{% for x in y %}{{ x }}{% endfor %}``
* available filters and tags may be extended with custom code
* templates can be *extended* and *included*
* you may define *blocks* in templates to be filled by other templates.
* you **may not** execute arbitrary python or assign variables and use them

Setting Up
----------

In ``assignments/week06/lab/source`` you'll find a file ``base.html``.

.. class:: incremental

Create a new directory, ``templates`` in your ``polls`` app package.

.. class:: incremental

Copy the ``base.html`` file into that new directory.

.. class:: incremental

Next, create a folder ``polls`` *inside* that new templates directory. We'll
add our individual templates here.

List Template
-------------

Add ``list.html`` inside ``templates/polls``:

.. code-block:: django
    :class: small

    {% extends "base.html" %}

    {% block content %}
    <h1>Latest Polls</h1>
    {% for poll in polls %}
    <div class="poll">
      <h2><a href="{% url poll_detail poll.pk %}">{{ poll }}</a></h2>
    </div>
    {% endfor %}
    {% endblock %}

.. class:: incremental

Now, load ``http://localhost:8000/polls/`` again.  

Detail View
-----------

Back in our ``polls`` app, let's edit ``urls.py`` again:

.. code-block:: python
    :class: incremental small

    # add this import
    from django.views.generic import ListView
    
    # and edit the detail url like so:
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name="polls/detail.html"
        ),
        name="poll_detail"),

.. class:: incremental

Again, we only need to add a template.

Forms in Django
---------------

We want to be able to vote on a poll. 

.. class:: incremental

Because doing so involves changing data on the server, we should do this with
a POST request.

.. class:: incremental

An html form is a simple way to allow us to force a POST request.

.. class:: incremental

Data-altering requests are vulnerable to Cross-Site Request Forgery, a common
attack vector.

Danger: CSRF
------------

Django not only provides a convenient system to fight this, it *requires* it
for any POST requests.

.. class:: incremental

The Django middleware that does this is enabled by default. All you need to do
is include the {% csrf_token %} tag in your form template.

.. class:: incremental

Create a new file ``detail.html`` in your ``templates/polls`` directory

Detail Template
---------------

.. code-block:: django
    :class: small
    
    {% extends "base.html" %}
    {% block content %}
    <h1>{{ poll }}</h1>
    {% if poll.choice_set.count > 0 %}
    <form action="{% url poll_vote poll.pk %}" method="POST">
      {% csrf_token %}
      {% for choice in poll.choice_set.all %}
      <div class="choice">
        <label for="choice_{{ choice.pk }}">
          <input type="radio" name="choice" id="choice_{{ choice.pk }}" 
                 value="{{ choice.pk }}"/>
          {{ choice }}</label></div>
      {% endfor %}
      <input type="submit" name="vote" value="Vote"/>
    </form>
    {% else %}
    <p>No choices are available for this poll</p>
    {% endif %}
    {% endblock %}

Processing The Vote
-------------------

We can now submit a form to the ``poll_vote`` url. We need to process that
vote

.. class:: incremental

Here, a class-based generic view is just going to get in our way.  Let's use
an old-fashioned view function.

.. class:: incremental

How is our user's vote reaching the server?

.. class:: incremental

It gets there as POST data, the value for the key 'choice'.

Django GET and POST Data
------------------------

Django provides the same type of Request/Response based interaction model that
most frameworks are based on. Views are called with the first argument being a
``request`` object.

.. class:: incremental

request.GET and request.POST are dictionary-like objects containing data
parsed from incoming HTTP request.

.. class:: incremental

You can use normal dictionary syntax to read values from these:

.. code-block:: python
    :class: incremental small

    bar = request.POST['bucko']
    foo = request.GET.get('somevar', None)

Vote View Skeleton
------------------

In ``views.py`` from our ``polls`` app package:

.. code-block:: python
    :class: small

    from django.core.urlresolvers import reverse
    from django.http import HttpResponseRedirect

    def vote_view(request, pk):
        if request.method == "POST":
            try:
                # attempt to get a choice
            except NoGoodChoice: # send back to detail
                url = reverse('poll_detail', args=[pk, ])
            else: # vote and send to result
                url = reverse('poll_result', args=[pk])
        else: # submitted via GET, ignore it
            url = reverse('poll_detail', args=[pk, ])

        return HttpResponseRedirect(url)

Get the Choice
--------------

Let's start by filling out the process of getting the choice:

.. code-block:: python
    :class: small

    # add imports
    from django.shortcuts import get_object_or_404
    from django.contrib import messages
    from polls.models import Poll, Choice
    # and edit our skeleton
    def vote_view(request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        if request.method == "POST":
            try:
                choice = poll.choice_set.get(
                    pk=request.POST.get('choice', 0))
            except Choice.DoesNotExist:
                msg = "Ooops, pick a choice that exists, please"
                messages.add_message(request, messages.ERROR, msg)
                url = reverse('poll_detail', args=[pk, ])

Add a Vote
----------

Next, let's record a vote on our choice:

.. code-block:: python
    :class: small

    def vote_view(request, pk):
        ...
        try:
            # choice = ...
        except Choice.DoesNotExist:
            # ...
        else:
            choice.votes += 1
            choice.save()
            messages.add_message(request, messages.INFO,
                                 "You voted for %s" % choice)
            url = reverse('poll_result', args=[pk])

Add the URL
-----------

Finally, we need to add this view to our urlconf. Back in ``urls.py`` in the
``polls`` app package, edit the url for the voting view like so:

.. code-block:: python
    :class: small

    url(r'^(?P<pk>\d+)/vote/$',
        'polls.views.vote_view',
        name="poll_vote"),

.. class:: incremental

Notice that the 'callable' in this pattern is a string. Django allows you to
use this sort of *dotted name* reference. It will resolve it (or throw an
error if it can't)

Display Result
--------------

The last view we need is the poll result. This can simply be a different
version of the Generic DetailView. Still in ``urls.py`` edit the pattern for
the results view:

.. code-block:: python
    :class: small

    url(r'^(?P<pk>\d+)/result/$',
        DetailView.as_view(
            model=Poll,
            template_name="polls/result.html"),
        name="poll_result")

.. class:: incremental

And, of course, we will need to create that final template

Result Template
---------------

In ``templates/polls`` create a new file, ``result.html``:

.. code-block:: django
    :class: small

    {% extends "base.html" %}

    {% block content %}
    <h1>{{ poll }}</h1>
    <ul>
      {% for choice in poll.choice_set.all %}
      <li>{{ choice }} ({{choice.votes}} votes)</li>
      {% endfor %}
    </ul>
    <a href="{% url poll_list %}">Back to the polls, please</a>
    {% endblock %}

Play a Bit
----------

Alright. You've done it. 

Take a few minutes to add some polls in the Admin.

Then return to the public side and vote. See how it goes.

Next Week
---------

We are going to mix it up quite a bit this week.

.. class:: incremental

I would like you all to divide into teams. Each team should have 4-6 people.
Each team should have both experienced and inexperienced members. Try to match
up with people whose strengths are different from your own.

.. class:: incremental

Now, each team, pick a 'facilitator'. This person will be responsible for
managing the operation of the team. This person will help to ensure that each
team member has a task. This should be a more experienced team member.

Assignment
----------

During this week, each **non-leader member** will duplicate the Flaskr app
using Django.

.. class:: incremental

* Create a new *app* which will hold all the code required.
* Define the model for the 'entry' object.
* Extend that model with two additional fields: ``publication_date``
  (DateTimeField), and ``author`` (ForeignKey to
  ``django.contrib.auth.models.User``)
* Define the URLs you'll need (an entry list, a form processor)
* Define the Views you'll need (see the two above).

Assignment
----------

During this week, each **team leader** will communicate with me to build a
plan for implementing a new feature for the Django flaskr app.

.. class:: incremental

* User Registration
* 'Archive' views based on date or author
* WYSIWYG visual editor for entry posts.
* Tagging
* Theme (make it beautiful)
* Search (this is a bigger one than you might think)

Submitting the Assignment
-------------------------

Leaders, you will communicate with me to make a plan

Members, you will do the usual submission of your code.

DO NOT ATTEMPT TO GET YOUR CODE RUNNING ON A VM

Next Week
---------

Our class next week will be a little different. Each team will be implementing
a new feature for our micro-blog application.

We will work in teams for the entire class up until 8:30, when we will show
off our results.

