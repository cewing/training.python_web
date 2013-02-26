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

.. image:: img/sheep_pyramid.jpg
    :align: center
    :width: 65%

.. class:: image-credit

image: Ionics http://www.flickr.com/photos/ionics/6337525967/ - CC_BY

What is Pyramid?
----------------

A Web Framework

.. class:: incremental

"Its primary job is to make it easier for a developer to create an arbitrary
web application"

.. class:: incremental

Makes as few decisions as possible for you.

.. class:: incremental

Allows *you* to make decisions, and provides tools to support you when you do

.. class:: incremental

"Pay only for what you eat"

Why is Pyramid?
---------------

Micro-frameworks are great for lightweight apps

.. class:: incremental

Micro-frameworks do not scale up or change specs easily

.. class:: incremental

Full-stack frameworks have lots of opinions. *Bending* them can be difficult.

.. class:: incremental

Pyramid can build a lightweight app easily, but it can also scale and bend

History - Zope and Repoze
-------------------------

Many of the core developers of Pyramid started as Zope developers.

.. class:: incremental

Born in 1996, Zope was the first Python web framework, and possibly the first
in any language.

.. class:: incremental

After 14 years, the developers of Zope had seen and learned *a lot*.

.. class:: incremental

Repoze was a short-lived (2008-2010) framework intended to embody the lessons
learned from Zope.

History - Pylons
----------------

Pylons was released in 2005.

.. class:: incremental

It was among the first frameworks to fully embrace the WSGI specification.

.. class:: incremental

The creators of Pylons build WebTest, WebError and WebOb (abstracted HTTP
request and response objects)

History - 2010
--------------

In 2010, the authors of Repoze and Pylons got together and made an unusual
decision.

.. class:: incremental

Why duplicate efforts when there are already so many other frameworks?

.. class:: incremental

Repoze was re-named 'Pyramid' and the 'Pylons Project' was born to shepherd
this new combined project.

Implications
------------

Pylons was a framework predicated largely on relational persistence and URL
Dispatch.

.. class:: incremental

Zope/Repoze was based on the ZODB and Object Traversal.

.. class:: incremental

Each of these approaches has strengths and weaknesses.

.. class:: incremental

Pyramid supports neither, both and even combinations of the two.

Relational DB / URL Dispatch
----------------------------

You've seen this before, both in Flask and Django

.. class:: incremental

SQLite3, the Django ORM, both are examples of relational persistence models

.. class:: incremental

Routes/urlpatterns, both are examples of URL Dispatch

.. class:: incremental

Pyramid can work this way too.  SQLAlchemy, Route-based views.  

.. class:: incremental

Been there, done that.  Let's see something else.

ZODB
----

ORMs allow developers to pretend that Objects are like DB Tables.

.. class:: incremental

But Objects are *not* tables, so there's a `conceptual mismatch
<http://en.wikipedia.org/wiki/Object-relational_impedance_mismatch>`_ between
the two.

.. class:: incremental

The ZODB is an *object store*, rather than a relational database.

.. class:: incremental

If your data is best represented by *heterogenous* objects, it's a better
persistence solution.

Traversal - Object Graphs
-------------------------

Python objects can *contain* other objects.

.. class:: incremental

Using *dict*-like structures, you can build a *graph* of objects:

.. class:: incremental

::

    Family
    ├── Parents
    │  ├── Cris
    │  ├── Kristina
    ├── Children
    │  ├── Kieran
    │  ├── Finnian

Traversal - Path Lookup
-----------------------

You can *traverse* across the object graph by treating a URL as a series of
*node names*

.. class:: incremental small

::

    http://family/parents/cris -> family['parents']['cris']

.. class:: incremental

Further path segments can be view names or information passed to the view

.. class:: incremental small

::

    http://family/parents/cris/edit -> edit view
    http://family/parents/cris/next/steps -> subpath = /next/steps

Break Time
----------

We've got the concept of object stores and traversal

.. class:: incremental

The next step is to see how those work in real life.

.. class:: incremental

Take the next few minutes here to ensure that you have a working Pyramid setup
with the ZODB and a project created with ``pcreate -s zodb``.

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

The ``Configurator`` provides an extensible API for configuring just about
everything.

.. class:: incremental

You can read more in `the pyramid.config documentation
<http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/api/config.html>`_

The Application Root
--------------------

The ``Configurator`` constructor can take a ``root_factory`` keyword argument.

.. class:: incremental

The ``root_factory`` of your app returns the router that determines how to
dispatch individual requests.

.. class:: incremental

If you do not provide this argument, the default root factory, which uses URL
Dispatch, will be used.

.. class:: incremental

In our case, we want to use Traversal for our app, so we provide a custom
``root_factory``.

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

We grab a connection to the ZODB and pass that into a call to ``appmaker``,
the result is returned (and becomes our app root).

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

We ensure that there is an ``app_root`` object stored in the ZODB, and return
it. That simple Python object will manage our *Traversal* based application.

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
callable will be handled. In our case, it's a template that will render to an
HTML page.

.. class:: incremental small

``context`` determines the *type* of object for which this view may be used. It
is an example of a ``predicate`` argument, which can be used to place
restrictions on when and how a view may be called.

.. class:: incremental small

Predicates are a very powerful system for choosing views. Read more about them
in `view configuration
<http://docs.pylonsproject.org/projects/pyramid/en/1.1-branch/narr/viewconfig.html>`_

Lab - Part Two
--------------

.. class:: big-centered

Data Models and Tests

Wiki Models
-----------

Now that we have a basic idea of what's going on in the code generated for us,
it's time to build our wiki models.

.. class:: incremental

We'll need to have a Python class that corresponds to a *page* in our wiki.

.. class:: incremental

This will be the type of object we view when we are looking at the wiki.

.. class:: incremental

We'll also need to have a *root* object, which will be a container for all the
*pages* we create for the wiki.

Persistence Magic
-----------------

In an SQL database, data *about* an object is written to tables. In the ZODB,
the *object itself* is saved in the database.

.. class:: incremental

The ZODB provides base classes that will *automatically save themselves*. We
will use two of these:

.. class:: incremental

* **Persistent** - a class that automatically tracks changes to class
  attributes and saves them. 

* **PersistentMapping** - roughly equivalent to a Python *dictionary*, this
  class will save changes to itself *and its keys and values*.

.. class:: incremental small

The ZODB also provides lists and more complex persistent data structures like
BTrees.

Traversal Magic
---------------

Traversal is supported by two object properties: ``__name__`` and
``__parent__``.

.. class:: incremental

Every object in a system which is going to use Traversal **must** provide
these two attributes.

.. class:: incremental

The *root* object in a Traversal system will have both of these attributes set
to ``None``.

The Wiki Class
--------------

Open ``models.py`` from our ``wikitutorial`` *package* directory.

.. class:: incremental

First, delete the ``MyModel`` class.  We won't need it.

.. class:: incremental

Add the following in its place:

.. code-block:: python
    :class: incremental

    class Wiki(PersistentMapping):
        __name__ = None
        __parent__ = None

The Page Class
--------------

To that same file (models.py) add one import and a second class definition:

.. code-block:: python

    from persistent import Persistent
    
    class Page(Persistent):
        def __init__(self, data):
            self.data = data

.. class:: incremental

What about ``__name__`` and ``__parent__``?

.. class:: incremental

We'll add those to each instance when we create it.

Update Appmaker
---------------

The existing ``appmaker`` function needs to be updated for our new models:

.. code-block:: python

    def appmaker(zodb_root):
        if not 'app_root' in zodb_root:
            app_root = Wiki()
            frontpage = Page('This is the front page')
            app_root['FrontPage'] = frontpage
            frontpage.__name__ = 'FrontPage'
            frontpage.__parent__ = app_root
            zodb_root['app_root'] = app_root
            import transaction
            transaction.commit()
        return zodb_root['app_root']

A Last Bit of Cleanup
---------------------

We've deleted the ``MyModel`` class.  But we still have *views* that 
reference the class.

.. class:: incremental

Open the ``views.py`` file in your *package* directory and comment out
everything **except** the first line:

.. code-block:: python
    :class: incremental

    from pyramid.view import view_config

.. class:: incremental

Next, we'll test our models.

Test the Wiki Model
-------------------

Open ``tests.py`` from the *package* directory. Delete the ``ViewTests``
class and replace it with the following:

.. code-block:: python
    :class: small

    class WikiModelTests(unittest.TestCase):

        def _getTargetClass(self):
            from wikitutorial.models import Wiki
            return Wiki

        def _makeOne(self):
            return self._getTargetClass()()

        def test_it(self):
            wiki = self._makeOne()
            self.assertEqual(wiki.__parent__, None)
            self.assertEqual(wiki.__name__, None)

Test the Page Model
-------------------

Add the following test class as well:

.. code-block:: python
    :class: small

    class PageModelTests(unittest.TestCase):

        def _getTargetClass(self):
            from wikitutorial.models import Page
            return Page

        def _makeOne(self, data=u'some data'):
            return self._getTargetClass()(data=data)

        def test_constructor(self):
            instance = self._makeOne()
            self.assertEqual(instance.data, u'some data')

Test Appmaker
-------------

One more test class:

.. code-block:: python
    :class: small

    class AppmakerTests(unittest.TestCase):

        def _callFUT(self, zodb_root):
            from .models import appmaker
            return appmaker(zodb_root)

        def test_it(self):
            root = {}
            self._callFUT(root)
            self.assertEqual(root['app_root']['FrontPage'].data,
                             'This is the front page')

A Quick Interlude
-----------------

In your *package* directory you should see a file: ``Data.fs``.

.. class:: incremental

This is the ZODB. It contains references to a class that doesn't exist
anymore (MyModel). This means it is broken.

.. class:: incremental

Make sure Pyramid is not running.

.. class:: incremental

Delete Data.fs. It will be re-created as needed.

.. class:: incremental

You can also delete Data.fs.* (.tmp, .index, .lock)

Run our Tests
-------------

Finally, let's run our tests::

    (pyramidenv)$ python setup.py test
    ...
    Ran 3 tests in 0.000s

    OK

.. class:: incremental

We can also run tests to tell us our code-coverage:

.. class:: incremental small

::

    (pyramidenv)$ nosetests --cover-package=tutorial --cover-erase --with-coverage

Break
-----

.. class:: big-centered

Take a few minutes to breathe

Lab - Part Three
----------------

.. class:: big-centered

Views and Templates

Preparing for Views
-------------------

Our ``Page`` model has a ``data`` attribute, which represents the text in the
page. 

.. class:: incremental

Our pages will use ReStructuredText, a plain-text format that can be rendered
to HTML with a Python module called ``docutils``.

.. class:: incremental

Our project is installable as a python package. It declares its own
*dependencies* so that they will also be installed.

.. class:: incremental

We need to add the ``docutils`` package to this list.

Package Dependencies
--------------------

Open the ``setup.py`` file from our *project* directory. Add ``docutils`` to
the list ``requires``:

.. code-block:: python

    requires = [
        'pyramid',
        'pyramid_zodbconn',
        'transaction',
        'pyramid_tm',
        'pyramid_debugtoolbar',
        'ZODB3',
        'waitress',
        'docutils', # <- ADD THIS
        ]

Complete the Change
-------------------

Any time you make a change to ``setup.py`` for a package you are working on,
you need to re-install that package to pick up the changes::

    (pyramidenv)$ python setup.py develop

.. class:: incremental

You'll see a whole bunch of stuff flicker by. In it will be a reference to
``Searching for docutils``.

Adding Views
------------

Open ``views.py`` again.  Add the following:

.. code-block:: python
    :class: small

    from docutils.core import publish_parts
    import re
    
    from pyramid.httpexceptions import HTTPFound
    from pyramid.view import view_config # <- ALREADY THERE
    
    from wikitutorial.models import Page
    
    # regular expression used to find WikiWords
    wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")
    
    @view_config(context='.models.Wiki')
    def view_wiki(context, request):
        return HTTPFound(location=request.resource_url(context,
                                                       'FrontPage'))

Some Notes
----------

New pages in a typical wiki are added by writing *WikiWords* into the page.

.. class:: incremental

``r"\b([A-Z]\w+[A-Z]+\w+)"`` is a regular expression that will locate
WikiWords.

.. class:: incremental

Note that the ``@view_config`` for the ``view_wiki`` function has no
``renderer`` argument. It will never be *shown*

.. class:: incremental

Instead, it returns ``HTTPFound``, (``302 Found``). Calling
``request.resource_url`` provides a URL for the redirect.

Add a Page View
---------------

.. code-block:: python
    :class: small

    @view_config(context='.models.Page', renderer='templates/view.pt')
    def view_page(context, request):
        wiki = context.__parent__
        
        def check(match):
            word = match.group(1)
            if word in wiki:
                page = wiki[word]
                view_url = request.resource_url(page)
                return '<a href="%s">%s</a>' % (view_url, word)
            else:
                add_url = request.application_url + '/add_page/' + word 
                return '<a href="%s">%s</a>' % (add_url, word)
        
        content = publish_parts(
            context.data, writer_name='html')['html_body']
        content = wikiwords.sub(check, content)
        edit_url = request.resource_url(context, 'edit_page')
        return dict(page=context, content=content, edit_url=edit_url)

Adding Templates
----------------

What will the page template for the ``view_page`` function need to be called?

.. class:: incremental

Go ahead and create ``view.pt`` in your ``templates`` directory.

.. class:: incremental

While you're there, also copy the file ``base.pt`` from
``assignments/week08/lab`` in the class repo.

.. class:: incremental

Like Django templates, Chameleon templates can extend other templates. Our
``base.pt`` template will be the master, and our ``view.pt`` and ``edit.pt``
templates will extend it.

The view.pt Template
--------------------

Type this code into your ``view.pt`` file:

.. code-block:: xml

    <metal:main use-macro="load: base.pt">
     <metal:content metal:fill-slot="main-content">
      <div tal:replace="structure content">
        Page text goes here.
      </div>
      <p>
        <a tal:attributes="href edit_url" href="">
          Edit this page
        </a>
      </p>
     </metal:content>
    </metal:main>

A Few Notes
-----------

Chameleon page templates are valid XML. The templating language uses ``tal``/``metal``
namespace XML tag attributes.

.. class:: incremental

``<metal:main use-macro="load: base.pt">`` tells us we will be using
``base.pt`` as our main template *macro*.

.. class:: incremental

Template *macros* can define one or more *slots*. These are like the *blocks*
in Jinja2 or Django templates.

.. class:: incremental

``<metal:content metal:fill-slot="main-content">`` tells us that everything
here will go in the ``main-content`` slot.

More Notes
----------

.. code-block:: xml

    <div tal:replace="structure content">
      Page text goes here.
    </div>

This uses the ``tal`` directive ``replace`` to completely replace the
``<div>`` tag with whatever html is in ``content``.

.. code-block:: xml
    :class: incremental

    <a tal:attributes="href edit_url" href="">
      Edit this page
    </a>

.. class:: incremental

Here, we use the ``tal`` directive ``attributes`` to set the ``href`` for our
anchor to the value passed into our template as ``edit_url``.

View Your Work
--------------

We've created the following:

.. class:: incremental small

* A wiki view that redirects to the automatically-created FrontPage page
* A page view that will render the ``data`` from a page, along with a url for
  editing that page
* A page template to show a wiki page.

.. class:: incremental

That's all we need to be able to see our work.  Start Pyramid:

.. class:: incremental small

::

    (pyramidenv)$ pserve development.ini
    Starting server in PID 43925.
    serving on http://0.0.0.0:6543

.. class:: incremental

Load http://localhost:6543/

What You Should See
-------------------

.. image:: img/wiki_frontpage.png
    :align: center
    :width: 95%

Editing a Page
--------------

Back in ``views.py`` add the following:

.. code-block:: python
    :class: small

    @view_config(name='edit_page', context='.models.Page',
                 renderer='templates/edit.pt')
    def edit_page(context, request):
        if 'form.submitted' in request.params:
            context.data = request.params['body']
            return HTTPFound(location = request.resource_url(context))

        return dict(page=context,
                    save_url=request.resource_url(context, 'edit_page'))

The Edit Template
-----------------

Create and fill ``edit.pt`` in ``templates``:

.. code-block:: xml
    :class: small

    <metal:main use-macro="load: base.pt">
      <metal:pagename metal:fill-slot="page-name">
      Editing 
      <b><span tal:replace="page.__name__">Page Name Goes Here
         </span></b>
      </metal:pagename>
      <metal:content metal:fill-slot="main-content">
        <form action="${save_url}" method="post">
          <textarea name="body" tal:content="page.data" rows="10"
                    cols="60"/><br/>
          <input type="submit" name="form.submitted" value="Save"/>
        </form>
      </metal:content>
    </metal:main>

FrontPage Content
-----------------

Restart Pyramid, then back in your browser, click the ``Edit this page`` link.

.. class:: incremental

Erase the existing text and add this instead:

.. class:: incremental small

::

    ==========
    Front Page
    ==========

    This is the front page.  It features

    * a heading
    * a list
    * a wikiword link to AnotherPage

View Your Work
--------------

Click the *Save* button and see what you've gotten.  

.. class:: incremental

If you get strangely formatted text that warns you about *Title overline too
short*, you didn't add enough equals signs above or below the page title. Go
back and ensure that there are the same number of equal signs as the total
number of characters in the title.

.. class:: incremental

Note that ``AnotherPage`` is a link, click it.

Adding a Page
-------------

Back in ``views.py`` add the code for creating a new page:

.. code-block:: python
    :class: small

    @view_config(name='add_page', context='.models.Wiki',
                 renderer='templates/edit.pt')
    def add_page(context, request):
        pagename = request.subpath[0]
        if 'form.submitted' in request.params:
            body = request.params['body']
            page = Page(body)
            page.__name__ = pagename
            page.__parent__ = context
            context[pagename] = page
            return HTTPFound(location = request.resource_url(page))
        save_url = request.resource_url(context, 'add_page', pagename)
        page = Page('')
        page.__name__ = pagename
        page.__parent__ = context
        return dict(page=page, save_url=save_url)

A Few Notes
-----------

Notice that the ``context`` for this view is *the Wiki model*

.. class:: incremental

``pagename = request.subpath[0]`` gives us the first element of the path
*after* the current context and view. What is that?

.. class:: incremental

Notice that *here* is where we set the ``__name__`` and ``__parent__``
attributes of our new Page.

.. class:: incremental

We add a new Page to the wiki as if the wiki were a Python ``dict``:
``context[pagename] = page``

One More Note
-------------

Look at the similarity in how a form is handled here to the way it is handled
in Django (in pseudocode):

.. class:: incremental

::

    if the_form_is_submitted:
        handle_the_form()
        return go_to_the_success_url()
    return an_empty_form()

.. class:: incremental

Forms that modify data should only be handled on POST. 

.. class:: incremental

Could you improve this code to ensure that?

And a Question
--------------

.. class:: big-centered

Why do we create a new, empty ``Page`` object at the end of the add_page view?

In-Class Exercises
------------------

Try to accomplish as many of these as you can before you leave:

.. class:: incremental

* Make the add_page view show "Adding <NewPage>" in the header (*do not create
  a new template to do this*)
* Make the edit_page and add_page views **only** change data on POST.
* Make the link that says "You can return to the FrontPage" disappear when you
  are viewing the front page.

Assignment
----------

By now you should have some idea what you want to do for your final project.

.. class:: incremental

Your assignment this week is to get started on it.

.. class:: incremental

If you have not already done so, please talk to Dan or me about your ideas. I
want to help you pick something you can get done in time.

.. class:: incremental

If you are stuck on how to start, reach out to Dan or me. We are here to help
you.

Next Week
---------

Next week we will have a short lecture about deployment options for Python web
applications.

.. class:: incremental

We'll look at deploying to shared hosting servers, VPSs and 'the cloud'.

.. class:: incremental

Your classmate Austin will give a short talk on the tools he used to deploy
``djangor`` to his VM in last week's class.

.. class:: incremental

And the rest of the time (about 1.5-2 hours) will be reserved for working on 
your final projects.  



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

