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

The MVC Controller
==================

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

.. _renderer: http://docs.pylonsproject.org/projects/pyramid/en/1.5-branch/narr/renderers.html


.. nextslide:: Adding Stub Views

Add temporary views to our application in ``views.py`` (and comment out the
sample view):

.. code-block:: python

    @view_config(route_name='home', renderer='string')
    def index_page(request):
        return 'list page'

    @view_config(route_name='detail', renderer='string')
    def view(request):
        return 'detail page'

    @view_config(route_name='action', match_param='action=create', renderer='string')
    def create(request):
        return 'create page'

    @view_config(route_name='action', match_param='action=edit', renderer='string')
    def update(request):
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
        def view(request):
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

The MVC View
============

.. rst-class:: left
.. container::

    Again, back to the *Model-View-Controller* pattern.

    .. figure:: http://upload.wikimedia.org/wikipedia/commons/4/40/MVC_passive_view.png
        :align: center
        :width: 25%

        By Alan Evangelista (Own work) [CC0], via Wikimedia Commons

    .. rst-class:: build
    .. container::

        We've built a *model* and we've created some *controllers* that use it.

        In Pyramid, we call *controllers* **views** and they are callables that
        take *request* as an argument.

        Let's turn to the last piece of the *MVC* patter, the *view*

Presenting Data
---------------

The job of the *view* in the *MVC* pattern is to present data in a format that
is readable to the user of the system.

.. rst-class:: build
.. container::

    There are many ways to present data.

    Some are readable by humans (tables, charts, graphs, HTML pages, text
    files).

    Some are more for machines (xml files, csv, json).

    Which of these formats is the *right one* depends on your purpose.

    What is the purpose of our learning journal?

Pyramid Renderers
-----------------

In Pyramid, the job of presenting data is performed by a *renderer*.

.. rst-class:: build
.. container::

    So we can consider the Pyramid **renderer** to be the *view* in our *MVC*
    app.

    We've already seen how we can connect a *renderer* to a Pyramid *view* with
    configuration.

    In fact, we have already done so, using a built-in renderer called
    ``'string'``.

    This renderer converts the return value of its *view* to a string and sends
    that back to the client as an HTTP response.

    But the result isn't so nice looking.

.. nextslide:: Template Renderers

The `built-in renderers` (``'string'``, ``'json'``, ``'jsonp'``) in Pyramid are
not the only ones available.

.. _built-in renderers: http://docs.pylonsproject.org/projects/pyramid/en/1.5-branch/narr/renderers.html#built-in-renderers

.. rst-class:: build
.. container::

    There are add-ons to Pyramid that support using various *template
    languages* as renderers.

    In fact, one of these was installed by default when you created this
    project.

.. nextslide:: Configuring a Template Renderer

.. code-block:: python

    # in setup.py
    requires = [
        # ...
        'pyramid_chameleon',
        # ...
    ]

    # in learning_journal/__init__.py
    def main(global_config, **settings):
        # ...
        config.include('pyramid_chameleon')

.. rst-class:: build
.. container::

    The `pyramid_chameleon` package supports using the `chameleon` template
    language.

    The language is quite nice and powerful, but not so easy to learn.

    Let's use a different one, *jinja2*

.. nextslide:: Changing Template Renderers

Change ``pyramid_chameleon`` to ``pyramid_jinja2`` in both of these files:

.. code-block:: python

    # in setup.py
    requires = [
        # ...
        'pyramid_jinja2',
        # ...
    ]

    # in learning_journal/__init__.py
    def main(global_config, **settings):
        # ...
        config.include('pyramid_jinja2')

.. nextslide:: Picking up the Changes

We've changed the dependencies for our Pyramid project.

.. rst-class:: build
.. container::

    As a result, we will need to re-install it so the new dependencies are also
    installed:

    .. code-block:: bash

        (ljenv)$ python setup.py develop
        ...
        Finished processing dependencies for learning-journal==0.0
        (ljenv)$

    Now, we can use *Jinja2* templates in our project.

    Let's learn a bit about how `Jinja2 templates`_ work.

.. _Jinja2 templates: http://jinja.pocoo.org/docs/templates/

Jinja2 Template Basics
----------------------

We'll start with the absolute basics.

.. rst-class:: build
.. container::

    Fire up a Python interpreter, using your `ljenv` virtualenv:

    .. code-block:: bash

        (ljenv)$ python
        >>>

    Then import the ``Template`` class from the ``jinja2`` package:

    .. code-block:: pycon

        >>> from jinja2 import Template

.. nextslide:: Templates are Strings

A template is constructed with a simple string:

.. code-block:: python

    >>> t1 = Template("Hello {{ name }}, how are you?")

.. rst-class:: build
.. container::

    Here, we've simply typed the string directly, but it is more common to
    build a template from the contents of a *file*.

    Notice that our string has some odd stuff in it: ``{{ name }}``.

    This is called a placeholder and when the template is *rendered* it is
    replaced.

.. nextslide:: Rendering a Template

Call the ``render`` method, providing *context*:

.. code-block:: python

    >>> t1.render(name="Freddy")
    u'Hello Freddy, how are you?'
    >>> t1.render({'name': "Roberto"})
    u'Hello Roberto, how are you?'
    >>>

.. rst-class:: build
.. container::

    *Context* can either be keyword arguments, or a dictionary

    Note the resemblance to something you've seen before:

    .. code-block:: python
    
        >>> "This is {owner}'s string".format(owner="Cris")
        'This is Cris's string'


.. nextslide:: Dictionaries in Context

Dictionaries passed in as part of the *context* can be addressed with *either*
subscript or dotted notation:

.. code-block:: python

    >>> person = {'first_name': 'Frank',
    ...           'last_name': 'Herbert'}
    >>> t2 = Template("{{ person.last_name }}, {{ person['first_name'] }}")
    >>> t2.render(person=person)
    u'Herbert, Frank'

.. rst-class:: build

* Jinja2 will try the *correct* way first (attr for dotted, item for
  subscript).
* If nothing is found, it will try the opposite.
* If nothing is found, it will return an *undefined* object.


.. nextslide:: Objects in Context

The exact same is true of objects passed in as part of *context*:

.. rst-class:: build
.. container::

    .. code-block:: python

        >>> t3 = Template("{{ obj.x }} + {{ obj['y'] }} = Fun!")
        >>> class Game(object):
        ...   x = 'babies'
        ...   y = 'bubbles'
        ...
        >>> bathtime = Game()
        >>> t3.render(obj=bathtime)
        u'babies + bubbles = Fun!'

    This means your templates can be a bit agnostic as to the nature of the
    things in *context*

.. nextslide:: Filtering values in Templates

You can apply `filters`_ to the data passed in *context* with the pipe ('|')
operator:

.. _filters: http://jinja.pocoo.org/docs/dev/templates/#filters

.. code-block:: python

    t4 = Template("shouted: {{ phrase|upper }}")
    >>> t4.render(phrase="this is very important")
    u'shouted: THIS IS VERY IMPORTANT'

.. rst-class:: build
.. container::

    You can also chain filters together:

    .. code-block:: python

        t5 = Template("confusing: {{ phrase|upper|reverse }}")
        >>> t5.render(phrase="howdy doody")
        u'confusing: YDOOD YDWOH'

.. nextslide:: Control Flow

Logical `control structures`_ are also available:

.. _control structures: http://jinja.pocoo.org/docs/dev/templates/#list-of-control-structures

.. rst-class:: build
.. container::

    .. code-block:: python

        tmpl = """
        ... {% for item in list %}{{ item }}, {% endfor %}
        ... """
        >>> t6 = Template(tmpl)
        >>> t6.render(list=[1,2,3,4,5,6])
        u'\n1, 2, 3, 4, 5, 6, '

    Any control structure introduced in a template **must** be paired with an
    explicit closing tag ({% for %}...{% endfor %})

    Remember, although template tags like ``{% for %}`` or ``{% if %}`` look a
    lot like Python, they are not.

    The syntax is specific and must be followed correctly.

.. nextslide:: Template Tests

There are a number of specialized *tests* available for use with the
``if...elif...else`` control structure:

.. code-block:: python

    >>> tmpl = """
    ... {% if phrase is upper %}
    ...   {{ phrase|lower }}
    ... {% elif phrase is lower %}
    ...   {{ phrase|upper }}
    ... {% else %}{{ phrase }}{% endif %}"""
    >>> t7 = Template(tmpl)
    >>> t7.render(phrase="FOO")
    u'\n\n  foo\n'
    >>> t7.render(phrase="bar")
    u'\n\n  BAR\n'
    >>> t7.render(phrase="This should print as-is")
    u'\nThis should print as-is'


.. nextslide:: Basic Expressions

Basic `Python-like expressions`_ are also supported:

.. _Python-like expressions: http://jinja.pocoo.org/docs/dev/templates/#expressions

.. code-block:: python

    tmpl = """
    ... {% set sum = 0 %}
    ... {% for val in values %}
    ... {{ val }}: {{ sum + val }}
    ...   {% set sum = sum + val %}
    ... {% endfor %}
    ... """
    >>> t8 = Template(tmpl)
    >>> t8.render(values=range(1,11))
    u'\n\n\n1: 1\n  \n\n2: 3\n  \n\n3: 6\n  \n\n4: 10\n
      \n\n5: 15\n  \n\n6: 21\n  \n\n7: 28\n  \n\n8: 36\n
      \n\n9: 45\n  \n\n10: 55\n  \n'


Our Templates
-------------

There's more that Jinja2 templates can do, but it will be easier to introduce
you to that in the context of a working template.  So let's make some.

.. nextslide:: Detail Template

We have a Pyramid view that returns a single entry. Let's create a template to
show it.

.. rst-class:: build
.. container::

    In ``learning_journal/templates`` create a new file ``detail.jinja2``:

    .. code-block:: jinja
    
        <article>
          <h1>{{ entry.title }}</h1>
          <hr/>
          <p>{{ entry.body }}</p>
          <hr/>
          <p>Created <strong title="{{ entry.created }}">{{entry.created}}</strong></p>
        </article>

    Then wire it up to the detail view in ``views.py``:

    .. code-block:: python
    
        # views.py
        @view_config(route_name='detail', renderer='templates/detail.jinja2')
        def view(request):
            # ...

.. nextslide:: Try It Out

Now we should be able to see some rendered HTML for our journal entry details.

.. rst-class:: build
.. container::

    Start up your server:

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 90536.
        serving on http://0.0.0.0:6543

    Then try viewing an individual journal entry

    * http://localhost:6543/journal/1

.. nextslide:: Listing Page

The index page of our journal should show a list of journal entries, let's do
that next.

.. rst-class:: build
.. container::

    In ``learning_journal/templates`` create a new file ``list.jinja2``:

    .. code-block:: jinja

        {% if entries %}
        <h2>Journal Entries</h2>
        <ul>
          {% for entry in entries %}
            <li>
            <a href="{{ request.route_url('detail', id=entry.id) }}">{{ entry.title }}</a>
            </li>
          {% endfor %}
        </ul>
        {% else %}
        <p>This journal is empty</p>
        {% endif %}

.. nextslide::

It's worth taking a look at a few specifics of this template.

.. rst-class:: build
.. container::

    .. code-block:: jinja
    
        <a href="{{ request.route_url('detail', id=entry.id) }}">{{ entry.title }}</a>

    Jinja2 templates are rendered with a *context*.

    The return values of the Pyramid *view* for a template get included in that
    context.

    So does *request*, which is placed there by the framework.

    Request has a method ``route_url`` that will create a URL for a named
    route.

    This allows you to include URLs in your template without needing to know
    exactly what they will be.

    This process is called *reversing*, since it's a bit like a reverse phone
    book lookup.

.. nextslide::

Finally, you'll need to connect this new renderer to your listing view:

.. code-block:: python

    @view_config(route_name='home', renderer='templates/list.jinja2')
    def index_page(request):
        # ...

.. nextslide:: Try It Out

We can now see our list page too.  Let's try starting the server:

.. rst-class:: build
.. container::

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 90536.
        serving on http://0.0.0.0:6543

    Then try viewing the home page of your journal:

    * http://localhost:6543/

    Click on the link to an entry, it should work.

.. nextslide:: Sharing Structure

These views are reasonable, if quite plain.

.. rst-class:: build
.. container::

    It'd be nice to put them into something that looks a bit more like a
    website.

    Jinja2 allows you to combine templates using something called
    `template inheritance`_.

    You can create a basic page structure, and then *inherit* that structure in
    other templates.

    In our class resources I've added a page template ``layout.jinja2``.  Copy
    that page to your templates directory

.. _template inheritance: http://jinja.pocoo.org/docs/dev/templates/#template-inheritance

.. nextslide:: ``layout.jinja2``

.. code-block:: jinja

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Python Learning Journal</title>
        <!--[if lt IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
      </head>
      <body>
        <header>
          <nav><ul><li><a href="{{ request.route_url('home') }}">Home</a></li></ul></nav>
        </header>
        <main>
          <h1>My Python Journal</h1>
          <section id="content">{% block body %}{% endblock %}</section>
        </main>
        <footer><p>Created in the UW PCE Python Certificate Program</p></footer>
      </body>
    </html>

.. nextslide:: Template Blocks

The important part here is the ``{% block body %}{% endblock %}`` expression.

.. rst-class:: build
.. container::

    This is a template **block** and it is a kind of placeholder.

    Other templates can inherit from this one, and fill that block with
    additional HTML.

    Let's update our detail and list templates:

    .. code-block:: jinja
    
        {% extends "layout.jinja2" %}
        {% block body %}
        <!-- everything else that was already there goes here -->
        {% endblock %}

.. nextslide:: Try It Out

Let's try starting the server so we can see the result:

.. rst-class:: build
.. container::

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 90536.
        serving on http://0.0.0.0:6543

    Then try viewing the home page of your journal:

    * http://localhost:6543/

    Click on the link to an entry, it should work.

    And now you have shared page structure that is in both.

Static Assets
-------------

Although we have a shared structure, it isn't particularly nice to look at.

.. rst-class:: build
.. container::

    Aspects of how a website looks are controlled by CSS (*Cascading Style
    Sheets*).

    Stylesheets are one of what we generally speak of as *static assets*.

    Other static assets include *images* that are part of the look and feel of
    the site (logos, button images, etc) and the *JavaScript* files that add
    client-side dynamic behavior to the site.

.. nextslide:: Static Assets in Pyramid

Serving static assets in Pyramid requires a *static view* to configuration.
Luckily, ``pcreate`` already handled that for us:

.. rst-class:: build
.. container::

    .. code-block:: python
    
        # in learning_journal/__init__.py
        def main(global_config, **settings):
            # ...
            config.add_static_view('static', 'static', cache_max_age=3600)
            # ...

    The first argument to ``add_static_view`` is a *name* that will need to
    appear in the path of URLs requesting assets.

    The second argument is a *path* that is relative to the package being
    configured.

    Assets referenced by the *name* in a URL will be searched for in the
    location defined by the *path*

    Additional keyword arguments control other aspects of how the view works.

.. nextslide:: Static Assets in Templates

Once you have a static view configured, you can use assets in that location in
templates.

.. rst-class:: build
.. container::

    The *request* object in Pyramid provides a ``static_url`` method that
    builds appropriate URLs

    Add the following to our ``layout.jinja2`` template:

    .. code-block:: jinja
    
        <head>
          <!-- ... -->
          <link href="{{ request.static_url('learning_journal:static/styles.css') }}" rel="stylesheet">
        </head>

    The one required argument to ``request.static_url`` is a *path* to an
    asset.

    Note that because any package *might* define a static view, we have to
    specify which package we want to look in.

    That's why we have ``learning_journal:static/styles.css`` in our call.

.. nextslide:: Basic Styles

I've created some very very basic styles for our learning journal.

.. rst-class:: build
.. container::

    You can find them in ``resources/session02/styles.css``.  Go ahead and copy
    that file.

    Add it to ``learning_journal/static``.

    Then restart your web server and see what a difference a little style
    makes:

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 90536.
        serving on http://0.0.0.0:6543

.. nextslide:: The Outcome

Your site should look something like this:

.. figure:: /_static/learning_journal_styled.png
    :align: center
    :width: 75%

    The learning journal with basic styles applied

Getting Interactive
===================

.. rst-class:: left
.. container::

    We have a site that allows us to view a list of journal entries.

    .. rst-class:: build
    .. container::

        We can also view the details of a single entry.

        But as yet, we don't really have any *interaction* in our site yet.

        We can't create new entries.

        Let's add that functionality next.

User Input
----------

In HTML websites, the traditional way of getting input from users is via
`HTML forms`_.

.. rst-class:: build
.. container::

    Forms use *input elements* to allow users to enter data, pick from
    drop-down lists, or choose items via checkbox or radio button.

    It is possible to create plain HTML forms in templates and use them with
    Pyramid.

    It's a lot easier, however, to work with a *form library* to create forms,
    render them in templates and interact with data sent by a client.

    We'll be using a form library called `WTForms`_ in our project

.. _HTML forms: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms
.. _WTForms: http://wtforms.readthedocs.org/en/latest/

.. nextslide:: Installing WTForms

The first step to working with this library is to install it.

.. rst-class:: build
.. container::

    Start by makin the library as a *dependency* of our package by adding it to
    the *requires* list in ``setup.py``:

    .. code-block:: python

        requires = [
            # ...
            'wtforms', # <- add this to the list
        ]

    Then, re-install our package to download and install the new dependency:

    .. code-block:: bash

        (ljenv)$ python setup.py develop
        ...
        Finished processing dependencies for learning-journal==0.0

Using WTForms
-------------

We'll want a form to allow a user to create a new Journal Entry.

.. rst-class:: build
.. container::

    Add a new file called ``forms.py`` in our learning_journal package, next to
    ``models.py``:

    .. code-block:: python
    
        from wtforms import Form, TextField, TextAreaField, validators

        strip_filter = lambda x: x.strip() if x else None

        class EntryCreateForm(Form):
            title = TextField(
                'Entry title',
                [validators.Length(min=1, max=255)],
                filters=[strip_filter])
            body = TextAreaField(
                'Entry body',
                [validators.Length(min=1)],
                filters=[strip_filter])

.. nextslide:: Using a Form in a View

Next, we need to add a new view that uses this form to create a new entry.

.. rst-class:: build
.. container::

    Add this to ``views.py``:

    .. code-block:: python

        # add these imports
        from pyramid.exceptions import HTTPFound
        from .forms import EntryCreateForm

        # and update this view function
        def create(request):
            entry = Entry()
            form = EntryCreateForm(request.POST)
            if request.method == 'POST' and form.validate():
                form.populate_obj(entry)
                DBSession.add(entry)
                return HTTPFound(location=request.route_url('home'))
            return {'form': form, 'action': request.matchdict.get('action')}

.. nextslide:: Testing the Route/View Connection

We already have a route that connects here.  Let's test it.

.. rst-class:: build
.. container::

    Start your server:

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 90536.
        serving on http://0.0.0.0:6543

    And then try connecting to the ``action`` route:

    * http://localhost:6543/journal/create
    
    You should see something like this::

        {'action': u'create', 'form': <learning_journal.forms.EntryCreateForm object at 0x10e7d6b90>}

.. nextslide:: Rendering A Form

Finally, we need to create a template that will render our form.

.. rst-class:: build
.. container::

    Add a new template called ``edit.jinja2`` in
    ``learning_journal/templates``:

    .. code-block:: jinja

        {% extends "templates/layout.jinja2" %}
        {% block body %}
        <form action="." method="POST">
        {% for field in form %}
          {% if field.errors %}
            <ul>
            {% for error in field.errors %}
                <li>{{ error }}</li>
            {% endfor %}
            </ul>
          {% endif %}
            <p>{{ field.label }}: {{ field }}</p>
        {% endfor %}
            <p><input type="submit" name="submit" value="Submit" /></p>
        </form>
        {% endblock %}

.. nextslide:: Connecting the Renderer

You'll need to update the view configuration to use this new renderer.

.. rst-class:: build
.. container::

    Update the configuration in ``learning_journal/views.py``:

    .. code-block:: python
    
        @view_config(route_name='action', match_param='action=create',
                     renderer='templates/edit.jinja2')
        def create(request):
            # ...

    And then you should be able to start your server and test:

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 90536.
        serving on http://0.0.0.0:6543

    * http://localhost:6543/create

.. nextslide:: Providing Access

Great!  Now you can add new entries to your journal.

.. rst-class:: build
.. container::

    But in order to do so, you have to hand-enter the url.

    You should add a new link in the UI somewhere that helps you get there more
    easily.

    Add the following to ``list.jinja2``:

    .. code-block:: jinja

        {% extends "layout.jinja2" %}
        {% block body %}
        {% if entries %}
        ...
        {% else %}
        ...
        {% endif %}
        <!-- Add This Link -->
        <p><a href="{{ request.route_url('action', action='create') }}">New Entry</a></p>
        {% endblock %}

Homework
========

.. rst-class:: left
.. container::

    You have a website now that allows you to create, view and list journal
    entries

    .. rst-class:: build
    .. container::

        However, there are still a few flaws in this system.

        You should be able to edit a journal entry that already exists, in case
        you make a spelling error.

        It would also be nice to see a prettier site.

        Let's handle that for homework this week.

Part 1: Add Editing
-------------------

For part one of your assignment, add editing of existing entries. You will need:

* A form that shows an existing entry (what is different about this form from
  one for creating a new entry?)
* A pyramid view that handles that form. It should:

  * Show the form with the requested entry when the page is first loaded
  * Accept edits only on POST
  * Update an existing entry with new data from the form
  * Show the view of the entry after editing so that the user can see the edits
    saved correctly
  * Show errors from form validation, if any are present

* A link somewhere that leads to the editing page for a single entry (probably
  on the view page for a entry)

You'll need to update a bit of configuration, but not much.  Use the create
form we did here in class as an example.

Part 2: Make it Yours
---------------------

I've created for you a very bare-bones layout and stylesheet.

You will certainly want to add a bit of your own style and panache.

Spend a few hours this week playing with the styles and getting a site that
looks more like you want it to look.

The Mozilla Developer Network has `some excellent resources`_ for learning CSS.

In particular, the `Getting Started with CSS`_ tutorial is a thorough
introduction to the basics.

You might also look at their `CSS 3 Demos`_ to help fire up your creative
juices.

Here are a few more resources:

* `A List Apart <http://alistapart.com>`_ offers outstanding articles.  Their
  `Topics list <http://alistapart.com/topics>`_ is worth a browse.
* `Smashing Magazine <http://www.smashingmagazine.com>`_ is another excellent
  resource for articles on design.

.. _some excellent resources: https://developer.mozilla.org/en-US/docs/Web/CSS
.. _Getting Started with CSS: https://developer.mozilla.org/en-US/docs/CSS/Getting_Started
.. _CSS 3 Demos: https://developer.mozilla.org/en-US/demos/tag/tech:css3


Part 3: User Model
------------------

As it stands, our journal accepts entries from anyone who comes by.

Next week we will add security to allow only logged-in users to create and edit
entries.

To do so, we'll need a user model

The model should have:

* An ``id`` field that is a primary key
* A ``username`` field that is unicode, no more than 255 characters, not
  nullable, unique and indexed.
* A ``password`` field that is unicode and not nullable

In addition, the model should have a classmethod that retrieves a specific user
when given a username.

Part 4: Preparation for Deployment
----------------------------------

At the end of class next week we will be deploying our application to Heroku.

You will need to get a free account.

Once you have your free account set up and you have logged in, run through the
`getting started with Python`_ tutorial.

Be sure to at least complete the *set up* step. It will have you install the
Heroku Toolbelt, which you will need to have ready in class.

.. _getting started with Python: https://devcenter.heroku.com/articles/getting-started-with-python#introduction

