.. slideconf::
    :autoslides: True

**********
Session 02
**********

.. image:: /_static/lj_entry.png
    :width: 65%
    :align: center

Interacting with Data
=====================

**Wherein we learn to display our data, and to create and edit it too!**


But First
---------

Last week we discussed the **model** part of the *MVC* application design
pattern.

.. rst-class:: build
.. container::

    We set up a project using the `Pyramid`_ web framework and the `SQLAlchemy`_
    library for persisting our data to a database.

    We looked at how to define a simple model by investigating the demo model
    created on our behalf.

    And we went over, briefly, the way we can interact with this model at the
    command line to make sure we've got it right.

    Finally, we defined what attributes a learning journal entry would have,
    and a pair of methods we think we will need to make the model complete.

.. _Pyramid: http://www.pylonsproject.org/projects/pyramid/about
.. _SQLAlchemy: http://docs.sqlalchemy.org/en/rel_0_9/

Our Data Model
--------------

Over the last week, your assignment was to create the new model.

.. rst-class:: build
.. container::

    Did you get that done?

    If not, what stopped you?

    Let's take a few minutes here to answer questions about this task so you
    are more comfortable.

    Questions?

.. nextslide:: A Complete Example

I have added a new folder to our `class repository`_, ``resources``.

.. _class repository: https://github.com/UWPCE-PythonCert/training.python_web/

.. rst-class:: build
.. container::

    If you clone the repository to your local machine you can get to it.

    You can also just browse the repository in github to view it.

    In this folder, I added a ``session02`` folder that contains resources for
    today.

    Among these resources is the completed ``models.py`` file with this new
    model added.

    Let's review how it works.

.. nextslide:: Demo Interaction

Another resource I've added is the ``ljshell.py`` script.

.. rst-class:: build
.. container::

    That script will allow you to interact with a db session just like I showed
    in class last week:

    .. code-block:: python

        # the script
        from pyramid.paster import get_appsettings, setup_logging
        from sqlalchemy import engine_from_config
        from sqlalchemy.orm import sessionmaker

        config_uri = 'development.ini'
        setup_logging(config_uri)
        settings = get_appsettings(config_uri)
        engine = engine_from_config(settings, 'sqlalchemy.')
        Session = sessionmaker(bind=engine)

    Just copy the file into your learning_journal Pyramid project folder (where
    ``setup.py`` is)

.. nextslide:: Using the ``ljshell.py`` script

Here's a demo interaction using the script to set up a session maker

.. rst-class:: build
.. container::

    First ``cd`` to your project code, fire up your project virtualenv and
    start python:

    .. code-block:: bash

        $ cd projects/learning-journal/learning_journal
        $ source ../ljenv/bin/activate
        (ljenv)$ python
        >>>

    Then, you can import the ``Session`` symbol from ``ljshell`` and you're off
    to the races:

    .. code-block:: pycon

        >>> from ljshell import Session
        >>> from learning_journal.models import MyModel
        >>> session = Session()
        >>> session.query(MyModel).all()
        [<learning_journal.models.MyModel object at 0x105849b90>]
        ...

    [demo]

The Controller
==============

.. rst-class:: left
.. container::

    Let's go back to thinking for a bit about the *Model-View-Controller*
    pattern.

    .. figure:: http://upload.wikimedia.org/wikipedia/commons/4/40/MVC_passive_view.png
        :align: center
        :width: 25%

        By Alan Evangelista (Own work) [CC0], via Wikimedia Commons

    .. rst-class:: build
    .. container::

        We talked last week (and today) about the *model*

        Today, we'll dig into *controllers* and *views*

        or as we will know them in Pyramid: *views* and *renderers*


HTTP Request/Response
---------------------

Internet software is driven by the HTTP Request/Response cycle.

.. rst-class:: build
.. container::

    A *client* (perhaps a user with a web browser) makes a **request**

    A *server* receives and handles that request and returns a **response**

    The *client* receives the response and views it, perhaps making a new
    **request**

    And around and around it goes.

.. nextslide:: URLs

An HTTP request arrives at a server through the magic of a **URL**

.. code-block:: bash

    http://uwpce-pythoncert.github.io/training.python_web/html/index.html

.. rst-class:: build
.. container::

    Let's break that up into its constituent parts:

    .. rst-class:: build

    \http://:
      This part is the *protocol*, it determines how the request will be sent

    uwpce-pythoncert.github.io:
      This is a *domain name*.  It's the human-facing address for a server
      somewhere.

    /training.python_web/html/index.html:
      This part is the *path*.  It serves as a locator for a resource *on the
      server*

.. nextslide:: Paths

In a static website (like our documentation) the *path* identifies a **physical
location** in the server's filesystem.

.. rst-class:: build
.. container::

    Some directory on the server is the *home* for the web process, and the
    *path* is looked up there.

    Whatever resource (a file, an image, whatever) is located there is returned
    to the user as a response.

    If the path leads to a location that doesn't exist, the server responds
    with a **404 Not Found** error.

    In the golden days of yore, this was the only way content was served via
    HTTP.

.. nextslide:: Paths in an MVC System

In todays world we have dynamic systems, server-side web frameworks like
Pyramid.

.. rst-class:: build
.. container::

    The requests that you send to a server are handled by a software process
    that assembles a response instead of looking up a physical location.

    But we still have URLs, with *protocol*, *domain* and *path*.

    What is the role for a path in a process that doesn't refer to a physical
    file system?

    Most web frameworks now call the *path* a **route**.

    They provide a way of matching *routes* to the code that will be run to
    handle requests.

Routes in Pyramid
-----------------

In Pyramid, routes are handled as *configuration* and are set up in the *main*
function in ``__init__.py``:

.. code-block:: python

    # learning_journal/__init__.py
    def main(global_config, **settings):
        # ...
        config.add_route('home', '/')
        # ...

.. rst-class:: build
.. container::

    Our code template created a sample route for us, using the ``add_route``
    method of the ``Configurator`` class.

    The ``add_route`` method has two required arguments: a *name* and a
    *pattern*

    In our sample route, the *name* is ``'home'``

    In our sample route, the *pattern* is ``'/'``

.. nextslide::

When a request comes in to a Pyramid application, the framework looks at all
the *routes* that have been configured.

.. rst-class:: build
.. container::

    One by one, in order, it tries to match the *path* of the incoming request
    against the *pattern* of the route.

    As soon as a *pattern* matches the *path* from the incoming request, that
    route is used and no further matching is performed.

    If no route is found that matches, then the request will automatically get
    a **404 Not Found** error response.

    In our sample app, we have one sample *route* named ``'home'``, with a
    pattern of ``/``.

    This means that any request that comes in for ``/`` will be matched to this
    route, and any other request will be **404**.

.. nextslide:: Routes as API

In a very real sense, the *routes* defined in an application *are* the public
API.

.. rst-class:: build
.. container::

    Any route that is present represents something the user can do.

    Any route that is not present is something the user cannot do.

    You can use the proper definition of routes to help conceptualize what your
    app will do.

    What routes might we want for a learning journal application?

    What will our application do?

.. nextslide:: Defining our Routes

Let's add routes for our application.

.. rst-class:: build
.. container::

    Open ``learning_journal/__init__.py``.

    For our list page, the existing ``'home'`` route will do fine, leave it.

    Add the following two routes:

    .. code-block:: python

        config.add_route('home', '/') # already there
        config.add_route('detail', '/journal/{id:\d+}')
        config.add_route('action', '/journal/{action}')

    The ``'detail'`` route will serve a single journal entry, identified by an
    ``id``.

    The ``action`` route will serve ``create`` and ``edit`` views, depending on
    the ``action`` specified.

    In both cases, we want to capture a portion of the matched path to use
    information it provides.

.. nextslide:: Matching an ID

In a pattern, you can capture a ``path segment`` *replacement
marker*, a valid Python symbol surrounded by curly braces:

.. rst-class:: build
.. container::

    ::

        /home/{foo}/

    If you want to match a particular pattern, like digits only, add a
    *regexp*::

        /journal/{id:\d+}

    Matched path segments are captured in a ``matchdict``::

        # pattern          # actual url   # matchdict
        /journal/{id:\d+}  /journal/27    {'id': '27'}

    The ``matchdict`` is made available as an attribute of the *request*


.. nextslide:: Connecting Routes to Views

In Pyramid, a *route* is connected by configuration to a *view*.

.. rst-class:: build
.. container::

    In our app, a sample view has been created for us, in ``views.py``:

    .. code-block:: python

        @view_config(route_name='home', renderer='templates/mytemplate.pt')
        def my_view(request):
            # ...

    The order in which *routes* are configured *is important*, so that must be
    done in ``__init__.py``.

    The order in which views are connected to routes *is not important*, so the
    *declarative* ``@view_config`` decorator can be used.

    When ``config.scan`` is called, all files in our application are searched
    for such *declarative configuration* and it is added.

The Pyramid View
----------------

Let's imagine that a *request* has come to our application for the path
``'/'``.

.. rst-class:: build
.. container::

    The framework made a match of that path to a *route* with the pattern ``'/'``.

    Configuration connected that route to a *view* in our application.

    Now, the view that was connected will be *called*, which brings us to the
    nature of *views*

    .. rst-class:: centered

    --A Pyramid view is a *callable* that takes *request* as an argument--

    Remember what a *callable* is?

.. nextslide:: What the View Does

So, a *view* is a callable that takes the *request* as an argument.

.. rst-class:: build
.. container::

    It can then use information from that request to build appropriate data,
    perhaps using the application's *models*.

    Then, it returns the data it assembled, passing it on to a `renderer`_.

    Which *renderer* to use is determined, again, by configuration:

    .. code-block:: python

        @view_config(route_name='home', renderer='templates/mytemplate.pt')
        def my_view(request):
            # ...

    More about this in a moment.

    The *view* stands at the intersection of *input data*, the application
    *model* and *renderers* that offer rendering of the results.

    It is the *Controller* in our MVC application.

.. nextslide:: Adding Stub Views

Add temporary views to our application in ``views.py`` (and comment out the
sample view):

.. code-block:: python

    @view_config(route_name='home', renderer='string')
    def index_page(request):
        return 'list page'

    @view_config(route_name='blog', renderer='string')
    def blog_view(request):
        return 'detail page'

    @view_config(route_name='blog_action', match_param='action=create', renderer='string')
    def blog_create(request):
        return 'create page'

    @view_config(route_name='blog_action', match_param='action=edit', renderer='string')
    def blog_update(request):
        return 'edit page'

.. nextslide:: Testing Our Views

Now we can verify that our view configuration has worked.

.. rst-class:: build
.. container::

    Make sure your virtualenv is properly activated, and start the web server:

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 84467.
        serving on http://0.0.0.0:6543

    Then try viewing some of the expected application urls:

    .. rst-class:: build

    * http://localhost:6543/
    * http://localhost:6543/journal/1
    * http://localhost:6543/journal/create
    * http://localhost:6543/journal/edit

    What happens if you visit a URL that *isn't* in our configuration?

.. nextslide:: Interacting With the Model

Now that we've got temporary views that work, we can fix them to get
information from our database

.. rst-class:: build
.. container::

    We'll begin with the list view.

    We need some code that will fetch all the journal entries we've written, in
    reverse order, and hand that collection back for rendering.

    .. code-block:: python

        from .models import (
            DBSession,
            MyModel,
            Entry, # <- Add this import
        )

        # and update this view function
        def index_page(request):
            entries = Entry.all()
            return {'entries': entries}

.. nextslide:: Using the ``matchdict``

Next, we want to write the view for a single entry.

.. rst-class:: build
.. container::

    We'll need to use the ``id`` value our route captures into the
    ``matchdict``.

    Remember that the ``matchdict`` is an attribute of the request.

    We'll get the ``id`` from there, and use it to get the correct entry.

    .. code-block:: python

        # add this import at the top
        from pyramid.exceptions import HTTPNotFound

        # and update this view function:
        def blog_view(request):
            this_id = request.matchdict.get('id', -1)
            entry = Entry.by_id(this_id)
            if not entry:
                return HTTPNotFound()
            return {'entry': entry}

.. nextslide:: Testing Our Views

We can now verify that these views work correctly.

.. rst-class:: build
.. container::

    Make sure your virtualenv is properly activated, and start the web server:

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 84467.
        serving on http://0.0.0.0:6543

    Then try viewing the list page and an entry page:

    * http://localhost:6543
    * http://localhost:6543/journal/1

    What happens when you request an entry with an id that isn't in the
    database?

    * http://localhost:6543/journal/100

outline
-------

Here, we'll use a *page template*, which renders HTML.

But Pyramid has other possible renderers: ``string``, ``json``, ``jsonp``.

And you can build your own.

.. _renderer: http://docs.pylonsproject.org/projects/pyramid/en/1.5-branch/narr/renderers.html


Templates
=========

We want to use Jinja, add jinja 2 as template engine and `python setup.py
develop` to install

quick intro to jinja2 templates.

create a nice basic html outline, see how it works

create a template to show a single entry, hook it up to your view/route and
test it by viewing it.

create a template to show a list of entries, hook it up and test by viewing.



Adding New Entries
==================

Add route, and view for creating new entry.

Discuss forms.

Create form for creating a new entry

use form in template.


homework
--------

What's the difference between creating new and editing existing?

add route and view for editing

create form for editing (subclass)

use form in template


homework



