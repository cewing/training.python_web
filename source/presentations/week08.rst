Internet Programming with Python
================================

.. image:: img/pyramid-medium.png
    :align: left
    :width: 50%

Week 8: Pyramid

.. class:: intro-blurb right

| Wherein we learn
| it's not built by aliens

But First
---------

.. class:: big-centered

Questions from the Reading?

And Now
-------




Lab - Part One
--------------

.. class:: big-centered

Getting To Know Pyramid

Scaffolds and Opinions
----------------------

Pyramid uses what it calls *scaffolds* to get you started on a new project.

.. class:: incremental

When you ran ``pcreate -s zodb wikitutorial`` you were invoking the *zodb
scaffold*

.. class:: incremental

Pyramid the framework is highly un-opinionated.

.. class:: incremental

*Scaffolds*, conversely, can be quite opinionated.  The one we used has chosen
our persistence mechanism (ZODB) and how we will reach our code (Traversal).

Project Layout
--------------

Running ``pcreate`` has set up a file structure for us:

.. class:: small

::

    wikitutorial/
        CHANGES.txt
        development.ini
        MANIFEST.in
        production.ini
        README.txt
        setup.cfg
        setup.py
        wikitutorial/
            __init__.py
            models.py
            static/
            templates/
            tests.py
            views.py

Similarities to Django
----------------------

Our project is organized with an outer *project* folder and an inner *package*
folder (see the ``__init__.py``?)

.. class:: incremental

The name of that outer directory is not really important.

.. class:: incremental

Our inner *package* folder has a models.py, tests.py and views.py module

.. class:: incremental

Our inner *package* folder has a ``static/`` and ``templates/`` directory

Differences from Django
-----------------------

Our *outer* module has a ``setup.py`` file, which allows it to be installed
with ``pip`` or ``easy_install``

.. class:: incremental

There is no ``manage.py`` file.  Pyramid commands are console scripts.

.. class:: incremental

There is nothing magical in Pyramid about the name of the ``models.py``
module.

.. class:: incremental

There is nothing magical in Pyramid about the names of the ``static/`` or
``templates/`` directories.

Pyramid System Configuration
----------------------------

Pyramid keeps configuration intended for an entire installation in ``.ini``
files at the top of a project.

.. class:: incremental

When you deploy an app to some wsgi server, you'll reference one of these files

.. class:: incremental

Settings there affect the environment of all apps that are running in that 
wsgi server.

.. class:: incremental

It is much like Django's ``settings.py`` but is not a python module.

Pyramid is Python
-----------------

Running a Pyramid application is really just like running a Python module. In
the ``__init__.py`` file of your app *package*, you'll find a ``main``
function:

.. code-block:: python
    :class: small incremental

    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        config = Configurator(root_factory=root_factory,
                              settings=settings)
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.scan()
        return config.make_wsgi_app()

.. class:: incremental

App-level configuration is done here.

App Configuration
-----------------

.. code-block:: python
    :class: small

    def main(global_config, **settings):

.. class:: incremental

``global_config`` will be a dictionary of the settings from your ``.ini`` file
that come in the [DEFAULT] section (if there is one).  These settings will be
shared across all apps that are involved in the system.

.. class:: incremental

The ``settings`` passed in here are the settings from your ``.ini`` file that
come in the section that corresponds to your application.  They will be used
only by your app.

App Configuration
-----------------

.. code-block:: python
    :class: small

    config = Configurator(root_factory=root_factory,
                          settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()

.. class:: incremental

Pyramid does configuration work when an app is run using the ``Configurator``
class.

.. class:: incremental

The ``Configurator`` provides and extensible API for configuring just about
everything.

.. class:: incremental

You can read more in `the pyramid.config documentation
<http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/api/config.html>`_

The Application Root
--------------------

The ``Configurator`` constructor can take a ``root_factory`` keyword argument.

.. class:: incremental

The ``root_factory`` of your app is the router that determines how to dispatch
individual requests.

.. class:: incremental

If you do not provide this argument, the default root factory, which uses URL
Dispatch, will be used.

.. class:: incremental

In our case, we want to use Traversal for our app, so we have to provide a
custom ``root_factory``.

Our Root Factory
----------------

.. code-block:: python
    :class: small

    from pyramid_zodbconn import get_connection
    from .models import appmaker
    
    def root_factory(request):
        conn = get_connection(request)
        return appmaker(conn.root())

.. class:: incremental

In our root_factory method, we grab a connection to the ZODB and pass that into
a call to ``appmaker``, the result is returned (and becomes our app root).

.. class:: incremental

So what exactly does ``appmaker`` do?

The appmaker
------------

.. code-block:: python
    :class: small

    def appmaker(zodb_root):
        if not 'app_root' in zodb_root:
            app_root = MyModel()
            zodb_root['app_root'] = app_root
            import transaction
            transaction.commit()
        return zodb_root['app_root']

.. class:: incremental

In essence, we are ensuring that there is an ``app_root`` object stored in the
ZODB, and then returning that. And that simple Python object will manage our
*Traversal* based application.

Seeing It Live
--------------

You've done this at home, but let's repeat the exercise here.

.. class:: incremental

In a terminal, change directories into your ``wikitutorial`` *project* folder
(where you see ``development.ini``). Fire up your pyramid virtualenv and serve
our app:

.. class:: incremental

::

    (pyramidenv)$ pserve development.ini
    Starting server in PID 16698.
    serving on http://0.0.0.0:6543

.. class:: incremental

Load http://localhost:6543 and view your app root.

Why is it Pretty?
-----------------

If we understand correctly what is happening so far, we are looking at an
instance of ``MyModel``.

.. class:: incremental

What makes it look like this?

.. class:: incremental

The secret sauce lies in *view configuration*

Pyramid Views
-------------

.. code-block:: python
    :class: small

    from pyramid.view import view_config
    from .models import MyModel
    
    @view_config(context=MyModel, renderer='templates/mytemplate.pt')
    def my_view(request):
        return {'project': 'wikitutorial'}

.. class:: incremental

Pyramid views can be configured with the ``@view_config()`` decorator.

.. class:: incremental

Or call ``config.add_view()`` method in your app ``main``.

.. class:: incremental

``config.scan()`` in ``main`` picks up all config decorators.

View Configuration
------------------

.. class:: small

The ``view_config`` decorator (and the ``add_view`` method) take a number of
interesting arguments.  In our case there are two.  

.. class:: incremental small

``renderer`` is used to designate how the results returned by the view
callable will be handled.  In our case, it's a template that will render

.. class:: incremental small

``context`` determines the *type* of object for which this view may be used. It
is an example of a ``predicate`` argument, which can be used to place
restrictions on when and how a view may be called.

.. class:: incremental small

Predicates are a very powerful system for choosing views. Read more about them
in `view configuration
<http://docs.pylonsproject.org/projects/pyramid/en/1.1-branch/narr/viewconfig.html>`_

scraps
------

Pyramid Intro

- What is it
- Where does it come from
- What problem is it trying to solve?

Things that make pyramid like other frameworks we've seen

- uses request/response model
- can use url route dispatch
- can use sql-based persistence

Things that make pyramid __unlike__ other frameworks we've seen

- can also use traversal
- can work with Object persistence via the ZODB

What is Traversal (as opposed to route dispatch?)

What is the ZODB?

Lab
---

work up the wiki tutorial
only go through views, then add tests

add security as an at-home exercise

