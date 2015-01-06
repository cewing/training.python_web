.. slideconf::
    :autoslides: True

**********
Session 01
**********

.. image:: /_static/python.png
    :align: center
    :width: 43%


Introductions
=============

.. rst-class:: large centered

Wherin we learn about the Model View Controller approach to app design and
explore data persistence in Python.

But First
---------

.. rst-class:: left
.. container::

    Class presentations are available online for your use

    .. rst-class:: small

    https://github.com/UWPCE-PythonCert/training.python_web

    .. rst-class:: build
    .. container::

        Licensed with Creative Commons BY-NC-SA

        .. rst-class:: build

        * You must attribute the work
        * You may not use the work for commercial purposes
        * You have to share your versions just like this one

        Find mistakes? See improvements? Make a pull request.

.. nextslide::

**Classroom Protocol**

.. rst-class:: build
.. container::

    Questions to ask:

    .. rst-class:: build

    * What did you just say?
    * Please explain what we just did again?
    * How did that work?
    * Why didn't that work for me?
    * Is that a typo?

.. nextslide::

**Classroom Protocol**

.. rst-class:: build
.. container::

    Questions **not** to ask:

    .. rst-class:: build

    * **Hypotheticals**: What happens if I do X?
    * **Research**: Can Python do Y?
    * **Syllabus**: Are we going to cover Z in class?
    * **Marketing questions**: please just don't.
    * **Performance questions**: Is Python fast enough?
    * **Unpythonic**: Why doesn't Python do it some other way?
    * **Show off**: Look what I just did!

.. nextslide::

.. rst-class:: large center

Introductions


Working with Virtualenv
=======================

.. rst-class:: large

| For every
| add-on package installed
| in a system Python,
| the gods kill a kitten
|
| - me

Why Virtualenv?
---------------

.. rst-class:: build

* You will need to install packages that aren't in the Python standard
  Library
* You often need to install *different* versions of the *same* library for
  different projects
* Conflicts arising from having the wrong version of a dependency installed can
  cause long-term nightmares
* Use `virtualenv`_ ...
* **Always**

.. _virtualenv: http://www.virtualenv.org/

Installing Virtualenv
---------------------

The best way is to install directly in your system Python (one exception to the
rule).

.. rst-class:: build
.. container::

    To do so you will have to have `pip`_ installed.

    Try the following command:

    .. code-block:: bash

        $ which pip
        /usr/local/bin/pip

    If the ``which`` command returns no value for you, then ``pip`` is not
    installed in your system. To fix this, follow `the instructions here`_.

.. _pip: https://pip.pypa.io/en/latest/index.html
.. _the instructions here: https://pip.pypa.io/en/latest/installing.html

.. nextslide::

Once you have ``pip`` installed in your system, you can use it to install
`virtualenv`_.

.. rst-class:: build
.. container::

    Because you are installing it into your system python, you will most likely
    need ``superuser`` privileges to do so:

    .. code-block:: bash

        $ sudo pip install virtualenv
        Downloading/unpacking virtualenv
          Downloading virtualenv-1.11.2-py2.py3-none-any.whl (2.8MB): 2.8MB downloaded
        Installing collected packages: virtualenv
        Successfully installed virtualenv
        Cleaning up...

.. nextslide::

Great.  Once that's done, you should find that you have a ``virtualenv``
command available to you from your shell:

.. code-block:: bash

    $ virtualenv --help
    Usage: virtualenv [OPTIONS] DEST_DIR

    Options:
      --version             show program's version number and exit
      -h, --help            ...

Using Virtuelenv
----------------

Creating a new virtualenv is very very simple:

.. rst-class:: build
.. container::

    .. code-block:: bash

        $ virtualenv [options] <ENV>


    ``<ENV>`` is just the name of the environment you want to create.

    It's arbitrary, so name them to be easily remembered.

.. nextslide::

Let's make one for demonstration purposes:

.. code-block:: bash

    $ virtualenv demoenv
    New python executable in demoenv/bin/python
    Installing setuptools, pip...done.


.. nextslide:: What Happened?

When you ran that command, a couple of things took place:

.. rst-class:: build

* A new directory with your requested name was created
* A new Python executable was created in <ENV>/bin (<ENV>/Scripts on Windows)
* The new Python was cloned from your system Python (where virtualenv was
  installed)
* The new Python was isolated from any libraries installed in the old Python
* Setuptools was installed so you have ``easy_install`` for this new python
* Pip was installed so you have ``pip`` for this new python

Activation
----------

Every virtualenv you create contains an executable Python command.

.. rst-class:: build
.. container::

    If you do a quick check to see which Python executable is found by your
    terminal, you'll see that it is not the one:

    .. code-block:: bash

        $ which python
        /usr/bin/python

    You can execute the new Python by explicitly pointing to it:

    .. code-block:: bash

        $ ./demoenv/bin/python -V
        Python 2.7.5

.. nextslide::

But that's tedious and hard to remember.

.. rst-class:: build
.. container::

    Instead, ``activate`` your virtualenv using the ``source`` shell command:

    .. code-block:: bash

        $ source demoenv/bin/activate
        (demoenv)$ which python
        /Users/cewing/demoenv/bin/python

    Notice that when a virtualenv is *active* you can see it in your command
    prompt.

    So long as the virtualenv is *active* the ``python`` executable that will
    be used will be the new one in your ``demoenv``.

Installing Packages
-------------------

Since ``pip`` is also installed, the ``pip`` that is used to install new
software will also be the one in ``demoenv``.

.. code-block:: bash

    (demoenv)$ which pip
    /Users/cewing/demoenv/bin/pip

.. rst-class:: build
.. container::

    This means that using these tools to install packages will install them
    *into your virtual environment only*

    The are not installed into the system Python.

    Let's see this in action.

.. nextslide::

We'll install a package called ``docutils``

.. rst-class:: build
.. container::

    It provides tools for creating documentation using ReStructuredText

    Install it using pip (while your virtualenv is active):

    .. code-block:: bash

        (demoenv)$ pip install docutils
        Downloading/unpacking docutils
          Downloading docutils-0.11.tar.gz (1.6MB): 1.6MB downloaded
          Running setup.py (path:/Users/cewing/demoenv/build/docutils/setup.py) egg_info for package docutils
            ...
            changing mode of /Users/cewing/demoenv/bin/rst2xml.py to 755
            changing mode of /Users/cewing/demoenv/bin/rstpep2html.py to 755
        Successfully installed docutils
        Cleaning up...

.. nextslide::

And now, when we fire up our Python interpreter, the docutils package is
available to us:

.. code-block:: pycon

    (demoenv)$ python
    Python 2.7.5 (default, Aug 25 2013, 00:04:04)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import docutils
    >>> docutils.__path__
    ['/Users/cewing/demoenv/lib/python2.7/site-packages/docutils']
    >>> ^d
    (demoenv)$

.. nextslide:: Side Effects

Like some other Python libraries, the ``docutils`` package provides a number of
executable scripts when it is installed.

.. rst-class:: build
.. container::

    You can see these in the ``bin`` directory inside your virtualenv:

    .. code-block:: bash

        (demoenv)$ ls ./demoenv/bin
        ...
        python
        rst2html.py
        rst2latex.py
        ...

    These scripts are set up to execute using the Python with which they were
    built.

    Running these scripts will use the Python executable in your virtualenv,
    *even if that virtualenv is not active*!

Deactivation
------------

So you've got a virtual environment created and activated so you can work with
it.

.. rst-class:: build
.. container::

    Eventually you'll need to stop working with this ``virtualenv`` and switch
    to another

    It's a good idea to keep a separate ``virtualenv`` for every project you
    work on.

    When a ``virtualenv`` is active, all you have to do is use the
    ``deactivate`` command:

    .. code-block:: bash

        (demoenv)$ deactivate
        $ which python
        /usr/bin/python

    Note that your shell prompt returns to normal, and now the executable
    Python found when you check ``python`` is the system one again.

Cleaning Up
-----------

The final advantage that ``virtualenv`` offers you as a developer is
the ability to easily remove a batch of installed Python software from your
system.

.. rst-class:: build
.. container::

    Consider a situation where you installed a library that breaks your Python
    (it happens)

    If you are working in your system Python, you now have to figure out what
    that package installed

    You have to figure out where it is

    And you have to go clean it out manually.

    With ``virtualenv`` you simply remove the directory ``virtualenv`` created
    when you started out.

.. nextslide::

Let's do that with our ``demoenv``:

.. rst-class:: build
.. container::

    .. code-block:: bash

        $ rm -rf demoenv

    And that's it.

    The entire environment and all the packages you installed into it are now
    gone.

    There are no traces left to pollute your world.

.. nextslide:: Break Time

Let's take a moment to rest up and absorb what we've learned.

When we return, we'll begin talking about a particular approach to thinking
about application design:

.. rst-class:: centered

**Model View Controller**

MVC Applications
================

.. figure:: http://upload.wikimedia.org/wikipedia/commons/4/40/MVC_passive_view.png
    :align: center
    :width: 50%

    By Alan Evangelista (Own work) [CC0], via Wikimedia Commons

Separation of Concerns
----------------------

.. rst-class:: build
.. container::

    In the first part of this course, you were introduced to the concept of
    *Object Oriented Programming*

    OOP was `first formalized`_ in the 1970s in *Smalltalk*, invented by Alan
    Kay at *Xerox PARC*

    *Smalltalk* was also the first language which utilized the
    `Model View Controller`_ design pattern.

    This pattern (like all `design patterns`_) seeks to provide a way of
    thinking that helps to make software design easier.

    In this case, the goal is to help clarify the high-level *separation of
    concerns* in a system.

.. _first formalized: http://en.wikipedia.org/wiki/Object-oriented_programming#History
.. _Model View Controller: http://en.wikipedia.org/wiki/Model–view–controller
.. _design patterns: http://en.wikipedia.org/wiki/Software_design_pattern

Three Components
----------------

The pattern divides the elements of a system into three parts:

.. rst-class:: build

Model:
  This component represents the *data* that comprises the system, and the
  *logic* used to manipulate that data.

View:
  This component can be any *representation* of the data to the outside world:
  a chart, diagram, table, user interface, etc.

  It also includes representations of the *actions* available in the system.

Controller:
  This component coordinates the Model and the View in a system.

  It accepts input from a user and channels that input into the Model.

  It accepts information about the current state of the Model and transmits
  that information to the View.

On the Web
----------

This pattern has proven useful for thinking about the applications we build for
the web.

.. rst-class:: build
.. container::

    A web browser provides a convenient container for *views* of data.

    These *views* are created by *controller* software hosted on a server.

    This *controller* software accepts input from users via *HTTP requests*,
    channeling it into a *data model* usually stored in some database.

    The *controller* returns information about the state of the *data model* to
    the user via *HTTP responses*

.. nextslide::

This approach is so common, that it has been formalized into any number of *web
frameworks*

.. rst-class:: build
.. container::

    *Web frameworks* abstract away the specifics of the *HTTP request/response
    cycle*, leaving simple MVC components for the developer to use.

    *Web frameworks* exist in nearly all modern languages.

    Python has scores of them.

    Over the weeks to come, we'll learn about two of them, `Pyramid`_ and
    `Django`_.

.. _Pyramid: http://www.pylonsproject.org/projects/pyramid/about
.. _Django: https://www.djangoproject.com/

A Word About Terminology
------------------------

Although the MVC pattern is a useful abstraction, there are a few differences
in how things are named in Python web frameworks

.. rst-class:: build centered
.. container::

    model <--> model

    controller <--> view

    view <--> template (or even HTTP response)

    .. rst-class:: left

    For more on this difference, you can `read this`_ from the Pyramid design
    documentation.

.. _read this: http://docs.pylonsproject.org/projects/pyramid/en/latest/designdefense.html#pyramid-gets-its-terminology-wrong-mvc

Our First Application
=====================

.. rst-class:: left

But enough abstract blabbering.

.. rst-class:: build left
.. container::

    There's no better way to make concepts like these concrete than to build
    something using them.

    Let's make an application!

    We're going to build a Learning Journal.

    When we're done, you'll have a live, online application you can use to keep
    note of the things you are learning about Python development.

    We'll use one of our Python web framework to do this: `Pyramid`_

Pyramid
-------

First published in 2010, `Pyramid`_ is a powerful, flexible web framework.

.. rst-class:: build
.. container::

    You can create compelling one-page applications, much like in
    microframeworks like Flask

    You can also create powerful, scalable applications using the full
    power of Python

    Created by the combined powers of the teams behind Pylons and Zope

    It represents the first true second-generation web framework in
    existence.

Starting the Project
--------------------

The first step is to prepare for the project.

.. rst-class:: build
.. container::

    Begin by creating a location where you'll do your work.

    I generally put all my work in a folder called ``projects`` in my home
    directory:

    .. code-block:: bash

        $ cd
        $ mkdir projects
        $ cd projects
        $ mkdir learning-journal
        $ cd learning-journal
        $ pwd
        /Users/cewing/project/learning-journal

.. nextslide:: Creating an Environment

We continue our preparations by creating a virtualenv we will use for it.

.. rst-class:: build
.. container::

    Again, this will help us to keep our work here isolated from anything else
    we do.

    Remember how to make a new virtualenv?

    .. code-block:: bash

        $ virtualenv ljenv
        New python executable in ljenv/bin/python
        Installing setuptools, pip...done.

    And then, how to activate it?

    .. code-block:: bash

        $ source ljenv/bin/activate
        (ljenv)$

.. nextslide:: Installing Pyramid

Next, we install the Pyramid web framework into our new virtualenv.

.. rst-class:: build
.. container::

    We can do this with the ``pip`` in our active ``ljenv``:

    .. code-block:: bash

        (ljenv)$ pip install pyramid
        Collecting pyramid
          Downloading pyramid-1.5.2-py2.py3-none-any.whl (545kB)
            100% |################################| 548kB 172kB/s
        ...
        Successfully installed PasteDeploy-1.5.2 WebOb-1.4
        pyramid-1.5.2 repoze.lru-0.6 translationstring-1.3
        venusian-1.0 zope.deprecation-4.1.1 zope.interface-4.1.2

    Once that is complete, we are ready to create a *scaffold* for our project.

Working with Pyramid
--------------------

Many web frameworks require at least a bit of *boilerplate* code to get
started.

.. rst-class:: build
.. container::

    Pyramid does not.

    However, our application will require a database and handling that does
    require some.

    Pyramid provides a system for creating boilerplate called ``pcreate``.

    You use it to generate the skeleton for a project based on some pattern:

    .. code-block:: bash

        (ljenv)$ pcreate -s alchemy learning_journal
        Creating directory /Users/cewing/projects/learning-journal/learning_journal
        ...
        Welcome to Pyramid.  Sorry for the convenience.
        ===============================================================================

    Let's take a quick look at what that did

.. nextslide:: What You Get

.. code-block:: bash

    (ljenv)$ tree learning_journal/
    learning_journal/
    ...
    ├── development.ini
    ├── learning_journal
    │   ├── __init__.py
    │   ├── models.py
    │   ├── scripts
    │   │   ├── __init__.py
    │   │   └── initializedb.py
    │   ├── static
    ...
    │   ├── templates
    │   │   └── mytemplate.pt
    │   ├── tests.py
    │   └── views.py
    ├── production.ini
    └── setup.py

.. nextslide:: Saving Your Work

You've now created something worth saving.

.. rst-class:: build
.. container::

    Start by initializing a new git repository in the `learning_journal` folder
    you just created:

    .. code-block:: bash

        (ljenv)$ cd learning_journal
        (ljenv)$ git init
        Initialized empty Git repository in
         /Users/cewing/projects/learning-journal/learning_journal/.git/

.. nextslide:: Saving Your Work

Check ``git status`` to see where things stand:

.. code-block:: bash

    (ljenv)$ git status
    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        CHANGES.txt
        MANIFEST.in
        README.txt
        development.ini
        learning_journal/
        production.ini
        setup.py

.. nextslide:: Add the Project Code

Add your work to this new repository:

.. code-block:: bash

    (ljenv)$ git add .
    (ljenv)$ git status
    ...
    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

        new file:   CHANGES.txt
        new file:   MANIFEST.in
        ...
        new file:   production.ini
        new file:   setup.py

.. nextslide:: Ignore Irrelevant Files

Python creates ``.pyc`` files when it executes your code.

.. rst-class:: build
.. container::

    There are many other files you don't want or need in your repository

    You can ignore this in ``git`` with the ``.gitignore`` file.

    Create one now, in this same directory, and add the following basic lines::

        *.pyc
        .DS_Store

    Finally, add this new file to your repository, too.

.. nextslide:: Make It Permanent

To preserve all these changes, you'll need to commit what you've done:

.. code-block:: bash

    (ljenv)$ git commit -m "initial commit of the Pyramid learning journal"

.. rst-class:: build
.. container::

    This will make a first commit here in this local repository.

    For homework, you'll put this into GitHub, but this is enough for now.

    Let's move on to learning about what we've built so far.

.. nextslide:: Project Structure

When you ran the ``pcreate`` command, a new folder was created:
``learning_journal``.

.. rst-class:: build
.. container::

    This folder contains your *project*.

    At the top level, you have *configuration* (.ini files)

    You also have a file called ``setup.py``

    This file turns this collection of Python code and configuration into an
    *installable Python distribution*

    Let's take a moment to look over the code in that file

.. nextslide:: ``setup.py``

.. code-block:: python

    from setuptools import setup, find_packages
    ...
    requires = [
        'pyramid',
        ... # packages on which this software depends (dependencies)
        ]
    setup(name='learning_journal',
          version='0.0',
          ... # package metadata (used by PyPI)
          install_requires=requires,
          # Entry points are ways that we can run our code once installed
          entry_points="""\
          [paste.app_factory]
          main = learning_journal:main
          [console_scripts]
          initialize_learning_journal_db = learning_journal.scripts.initializedb:main
          """,
          )

Pyramid is Python
-----------------

In the ``__init__.py`` file of your app *package*, you'll find a ``main``
function:

.. code-block:: python

    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        config = Configurator(settings=settings)
        config.include('pyramid_chameleon')
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.add_route('home', '/')
        config.scan()
        return config.make_wsgi_app()

Let's take a closer look at this, line by line.

.. nextslide:: System Configuration

.. code-block:: python

    def main(global_config, **settings):

Configuration is passed in to an application after being read from the
``.ini`` file we saw above.

.. rst-class:: build
.. container::

    These files contain sections (``[app:main]``) containing ``name = value``
    pairs of *configuration data*

    This data is parsed with the Python
    `ConfigParser <http://docs.python.org/2/library/configparser.html>`_ module.

    The result is a dict of values:

    .. code-block:: python

        {'app:main': {'pyramid.reload_templates': True, ...}, ...}

    The default section of the file is passed in as ``global_config``, the
    section for *this app* as ``settings``.

.. nextslide:: Database Configuration

.. code-block:: python

    from sqlalchemy import engine_from_config
    from .models import DBSession, Base
    ...
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

We will use a package called ``SQLAlchemy`` to interact with our database.

.. rst-class:: build
.. container::

    Our connection is set up using settings read from the ``.ini`` file.

    Can you find the settings for the database?

    The ``DBSession`` ensures that each *database transaction* is tied to HTTP
    requests.

    The ``Base`` provides a parent class that will hook our *models* to the
    database.

.. nextslide:: App Configuration

.. code-block:: python

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()

Pyramid controlls application-level configuration using a ``Configurator`` class.

.. rst-class:: build
.. container::

    It uses app-specific settings passed in from the ``.ini`` file

    We can also ``include`` configuration from other add-on packages

    Additionally, we can configure *routes* and *views* needed to connect our
    application to the outside world here (more on this next week).

    Finally, the ``Configurator`` instance performs a ``scan`` to ensure there
    are no problems with what we've created.

.. nextslide:: A Last Word on Configuration

We will return to the configuration of our application repeatedly over the next
sessions.

.. rst-class:: build
.. container::

    Pyramid configuration is powerful and flexible.

    We'll use a few of its features

    But there's a lot more you could (and should) learn.

    Read about it in the `configuration chapter`_ of the Pyramid documentation.

.. _configuration chapter: http://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html

.. nextslide:: Break Time

Let's take a moment to rest up and absorb what we've learned.

When we return, we'll see how we can create *models* that will embody the data
for our Learning Journal application.

.. rst-class:: centered

**Pyramid Models**


Models in Pyramid
=================

.. rst-class:: left
.. container::

    The central component of MVC, the model, captures the behavior of the
    application in terms of its problem domain, independent of the user
    interface. The model directly manages the data, logic and rules of the
    application

    -- from the Wikipedia article on `Model-view-controller`_

.. _Model-view-controller: http://en.wikipedia.org/wiki/Model–view–controller

Models and ORMs
---------------

In an MVC application, we define the *problem domain* by creating one or more
*Models*.

.. rst-class:: build
.. container::

    These capture relevant details about the information we want to preserve
    and how we want to interact with it.

    In Python-based MVC applications, these *Models* are implemented as Python
    classes.

    The individual bits of data we want to know about are *attributes* of our
    classes.

    The actions we want to take using that data are *methods* of our classes.

    Together, we can refer to this as the *API* of our system.

.. nextslide:: Persistence

It's all well and good to have a set of Python classes that represent your
system.

.. rst-class:: build
.. container::

    But what happens when you want to *save* information.

    What happens to a instance of a Python class when you quit the interprer?

    When your script stops running?

    The code in a website runs when an HTTP request comes in from a client.

    It stops running when an HTTP response goes back out to the client.

    So what happens to the data in your system in-between these moments?

    The data must be *persisted*

.. nextslide:: Alternatives

In the last class from part one of this series, you explored a number of
alternatives for persistence

.. rst-class:: build

* Python Literals
* Pickle/Shelf
* Interchange Files (CSV, XML, INI)
* Object Stores (ZODB, Durus)
* NoSQL Databases (MongoDB, CouchDB)
* SQL Databases (sqlite, MySQL, PostgreSQL, Oracle, SQLServer)

.. rst-class:: build
.. container::

    Any of these might be useful for certain types of applications.

    On the web, you tend to see two used the most:

    .. rst-class:: build

    * NoSQL
    * SQL

.. nextslide:: Choosing One

How do you choose one over the other?

.. rst-class:: build
.. container::

    In general, the telling factor is going to be how you intend to use your
    data.

    In systems where the dominant feature is viewing/interacting with
    individual objects, a NoSQL storage solution might be the best way to go.

    In systems with objects that are related to eachother, SQL-based Relational
    Databases are a better choice.

    Our system is more like this latter type (trust me on that one for now).

    We'll be using SQL (sqlite to start with).


.. nextslide:: Objects and Tables

So we have a system where our data is captured in Python *objects*

.. rst-class:: build
.. container::

    And a storage system where our data must be rendered as database *tables*

    Python provides a specification for interacting directly with databases:
    `dbapi2`_

    And there are multiple Python packages that implement this specification
    for various databases:

    .. rst-class:: build

    * sqlite3
    * python-mysql
    * psycopg2
    * ...

    With these, you can write SQL to save your Python objects into your
    database.

.. _dbapi2: https://www.python.org/dev/peps/pep-0249/

.. nextslide:: ORMs

But that's a pain.

.. rst-class:: build
.. container::

    SQL, while not impossible, is yet another language to learn.

    And there is a viable alternative in using an *Object Relational Manager*
    (ORM)

    An ORM provides a layer of *abstraction* between you and SQL

    You instantiate Python objects and set attributes on them

    The ORM handles converting data from these objects into SQL statements (and
    back)

SQLAlchemy
----------

In our project we will be using the `SQLAlchemy`_ ORM.

.. rst-class:: build
.. container::

    You can find SQLAlchemy among the packages in ``requires`` in ``setup.py``
    in our new ``learning_journal`` package.

    However, we don't yet have that code installed.

    To do so, we will need to "install" our own package

    Make sure your ``ljenv`` virtualenv is active and then type the following:

    .. code-block:: bash
    
        (ljenv)$ python setup.py develop
        running develop
        running egg_info
        creating learning_journal.egg-info
        ...
        Finished processing dependencies for learning-journal==0.0

.. nextslide::

Once that is complete, all the *dependencies* listed in our ``setup.py`` will
be installed.

.. rst-class:: build
.. container::

    You can also install the package using ``python setup.py install``

    But using ``develop`` allows us to continue developing our package without
    needing to re-install it every time we change something.

    It is very similar to using the ``-e`` option to ``pip``

    Now, we'll only need to re-run this command if we change ``setup.py``
    itself.

.. nextslide::

We also need to adjust our ``.gitignore`` file:

.. rst-class:: build
.. code-block:: bash

    (ljenv)$ git status
    ...
    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        learning_journal.egg-info/

.. rst-class:: build
.. container::

    The ``egg-info`` directory that was just created is an artifact of
    installing a Python egg.

    It should never be committed to a repository.

    Let's add ``*.egg-info`` to our ``.gitignore`` file and then commit that
    change

    Remember how?

.. nextslide:: Our First Model

Our project skeleton contains up a first, basic model created for us:

.. code-block:: python

    # in models.py
    Base = declarative_base()

    class MyModel(Base):
        __tablename__ = 'models'
        id = Column(Integer, primary_key=True)
        name = Column(Text)
        value = Column(Integer)
    Index('my_index', MyModel.name, unique=True, mysql_length=255)

.. _SQLAlchemy: http://docs.sqlalchemy.org/en/rel_0_9/

.. rst-class:: build
.. container::

    Our class inherits from ``Base``

    We ran into ``Base`` earlier when discussing configuration.

    We were binding it to the database we wanted to use (the ``engine``)

.. nextslide:: ``Base``

Any class we create that inherits from this ``Base`` becomes a *model*

.. rst-class:: build
.. container::

    It will be connected through the ORM to a table in our database.

    The name of the table is determined by the ``__tablename__`` special
    attribute.

    Other aspects of table configuration can also be controlled through special
    attributes

    Instances of the class, once saved, will become rows in the table.

    Attributes of the model that are instances of ``Column`` will become
    columns in the table.

    You can learn much more in the `Declarative`_ chapter of the SQLAlchemy docs

.. _Declarative: http://docs.sqlalchemy.org/en/rel_0_9/orm/extensions/declarative/

Creating The Database
---------------------

We have a *model* which allows us to persist Python objects to an SQL database.

.. rst-class:: build
.. container::

    But we're still missing one ingredient here.

    We need to create our database, or there will be nowhere for our data to
    go.

    Luckily, our ``pcreate`` scaffold also gave us a convenient way to handle
    this:

    .. code-block:: python
    
        # in setup.py
        entry_points="""\
        [paste.app_factory]
        main = learning_journal:main
        [console_scripts]
        initialize_learning_journal_db = learning_journal.scripts.initializedb:main
        """,

    The ``console_script`` set up as an entry point will help us.

.. nextslide:: ``initialize_learning_journal_db``

Let's look at that code for a moment.

.. code-block:: python

    # in scripts/intitalizedb.py
    from ..models import DBSession, MyModel, Base
    # ...
    def main(argv=sys.argv):
        if len(argv) < 2:
            usage(argv)
        config_uri = argv[1]
        options = parse_vars(argv[2:])
        setup_logging(config_uri)
        settings = get_appsettings(config_uri, options=options)
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = MyModel(name='one', value=1)
            DBSession.add(model)

.. nextslide:: Console Scripts

By connecting this function as a ``console script``, our Python package makes
this command available to us.

.. rst-class:: build
.. container::

    When we exectute ``initialize_learning_journal_db`` at the command line, we
    will be running this function.

    It will use the configuration we pass in on the command line (an ``.ini``
    file)

    It will connect to the database by creating a ``DBSession``

    It will use the ``metadata`` property of our ``Base`` class to
    ``create_all`` tables needed by our models.

    It will create one instance of our ``MyModel`` class and add it to the
    session.
