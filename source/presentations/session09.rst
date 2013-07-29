Internet Programming with Python
================================

.. image:: img/pyramid-medium.png
    :align: left
    :width: 50%

Session 9: Intro To Pyramid

.. class:: intro-blurb right

| The flexible framework.
| Totally not built by aliens.


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

The creators of Pylons built WebOb (abstracted HTTP request and response
objects).

.. class:: incremental

This forms the foundation of Pylons much as Werkzeug is the foundation of
Flask.


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

Pyramid supports using neither, both and even combinations of the two.


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


Traversal
---------

In URL Dispatch, the ``PATH`` is a *virtual* construct.

.. class:: incremental

In our Django app ``/admin/myblog/post/13/`` doesn't map to any series of
*real* locations.

.. class:: incremental

This is unlike a filesystem where ``/usr/local/bin/python`` points to a *real*
location.

.. class:: incremental

When you use the ``cd`` command to move from place to place in a filesystem,
that is *traversal*


Object Graphs
-------------

In Python, objects can *contain* other objects.

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


We Got Both Directions
----------------------

``__getitem__`` allows movement from *container* to *contained*

.. container:: incremental

    What if the *contained* can keep track of its *container*?
    
    .. code-block:: python
        :class: small
    
        >>> class node(dict):
        ...   __parent__ = None
        ...   def __init__(self, parent=None):
        ...     self.__parent__ = parent
        ...
        >>> x = node()
        >>> x['y'] = node(x)
        >>> y = x['y']
        >>> y.__parent__ == x
        True


Traversal - Path Lookup
-----------------------

You can *traverse* across the object graph by treating a URL as a series of
*object names*

.. class:: incremental small

::

    http://family/parents/cris -> family['parents']['cris']

.. class:: incremental

If you have more names than objects, the remainder can be passed to the final
object as data:

.. class:: incremental small

::

    http://family/parents/cris/edit -> subpath = /edit
    http://family/parents/cris/next/steps -> subpath = /next/steps

.. class:: incremental

The subpath can be used to find object methods or views

Preparation
-----------

You should at this point have a virtualenv in which you have installed the
ZODB.

.. class:: incremental

Now, let's install pyramid too.

.. container:: incremental

    In your terminal, change directories to where you build that virtualenv and
    activate it:
    
    .. class:: small
    
    ::
    
        $ cd /path/to/right/place
        $ source pyramidenv/bin/activate
        <or>
        C:\> pyramidenv\Scripts\activate


Installation
------------

Next, install Pyramid and the extras we'll be using:

.. class:: incremental small

::

    (pyramidenv)$ pip install pyramid
    ...
    (pyramidenv)$ pip install docutils nose coverage
    ...
    (pyramidenv)$ pip install pyramid_zodbconn pyramid_tm
    ...
    (pyramidenv)$ pip install pyramid_debugtoolbar

.. class:: incremental

These tools will allow us to manage ZODB connections, debug our app, and run
cool tests.


Required Setup
--------------

In Django ``startproject`` and ``startapp`` gave us the boilerplate we needed.

.. class:: incremental

Pyramid uses what it calls *scaffolds* for the same purpose.

.. class:: incremental

When you installed it, a new ``pcreate`` command was generated in your
virtualenv.

.. container:: incremental

    Let's use it:
    
    .. class:: small
    
    ::
    
        (pyramidenv)$ pcreate -s zodb wikitutorial
        ...


Scaffolds and Opinions
----------------------

When you ran ``pcreate -s zodb wikitutorial`` you invoked the *zodb scaffold*

.. class:: incremental

Pyramid the framework is highly un-opinionated.

.. class:: incremental

*Scaffolds*, conversely, can be quite opinionated.  The one we used has chosen
our persistence mechanism (ZODB) and how we will reach our code (Traversal).

.. class:: incremental

You do not have to use *scaffolds* to start a project, but it can help.


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

There is no ``manage.py`` file. Pyramid commands are console scripts (look in
*pyramidenv/bin*).

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

Like Django's ``settings.py``, but **not** python.


INI format
----------

INI-style files have a particular format.

.. class:: incremental

Individual sections are marked by ``[SECTION_NAMES]`` in square brackets

.. class:: incremental

Each section will contain ``name = value`` pairs of settings.

.. class:: incremental

INI files are parsed using the Python `ConfigParser
<http://docs.python.org/2/library/configparser.html>`_ module.

.. code-block:: python
    :class: small incremental
    
    {'SECTION_NAME': {'name': 'value', ...}, ...}


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

Let's take a closer look at this, line by line.


INI Configuration
-----------------

.. code-block:: python
    :class: small

    def main(global_config, **settings):

.. class:: incremental

Arguments passed to ``main`` are configuration from ``.ini``.

.. class:: incremental

``global_config`` is a dictionary of settings in [DEFAULT]

.. class:: incremental

``settings`` will be the name-value pairs for your app.

.. container:: incremental

    ``[app:<name>]`` sections are mapped to apps by the ``use`` setting

    .. code-block:: ini
        :class: small

        [app:main]
        use = egg:wikitutorial


App Configuration
-----------------

.. code-block:: python
    :class: small

    config = Configurator(root_factory=root_factory,
                          settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()

.. class:: incremental

Pyramid configuration is done by the ``Configurator`` class.

.. class:: incremental

Configuration can be *imperative* (function calls) or *declarative*
(decorators)

.. class:: incremental

Either way, ``.scan()`` sets it all up and reports errors.

.. class:: incremental

Read more in `the pyramid.config documentation
<http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/api/config.html>`_


WSGI Hookup
-----------

.. code-block:: python
    :class: small

    return config.make_wsgi_app()

.. class:: incremental

Like Django and Flask, Pyramid runs in a WSGI world.

.. class:: incremental

``.make_wsgi_app()`` returns a ``Router`` object for your app.

.. container:: incremental

    ``Router`` has the following ``__call__`` method:
    
    .. code-block:: python
        :class: small
        
        def __call__(self, environ, start_response):
            request = self.request_factory(environ)
            response = self.invoke_subrequest(request, use_tweens=True)
            return response(request.environ, start_response)

.. class:: incremental

Familiar, no?


The Application Root
--------------------

The ``Configurator`` constructor takes a ``root_factory`` kwarg.

.. class:: incremental

This *callable* returns something to handle dispatching requests.

.. class:: incremental

The default root factory uses URL Dispatch.

.. class:: incremental

We want to use Traversal for our app, so we provide one.


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

``get_connection`` returns a connection to the ZODB.

.. class:: incremental

The ``root`` of this connection is then passed to ``appmaker``

.. class:: incremental

This is another factory method that returns the app root.

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

Remember, the ZODB is an *object store*, dict-like.

.. class:: incremental

We look for an ``app_root`` inside this *container*

.. class:: incremental

If there is none, we build one and put it there.

.. class:: incremental

This simple Python object will manage *Traversal* for our app.


Install Our App
---------------

Our app is, in fact, a Python package.

.. class:: incremental

In order for us to use it, we must *install* it.

.. class:: incremental

``setup.py`` allows us to do this: ``python setup.py install`` **BUT**

.. class:: incremental

Install will make a copy of our code and use that.

.. class:: incremental

We don't want that, since updates we make here would not be picked up.

*Develop* Installation
----------------------

We can use an alternate method called ``develop``.

.. class:: incremental

This will install a *pointer* to our package, but leave the code here.

.. class:: incremental

In a terminal, move to the ``wikitutorial`` *project* folder (find
``development.ini``) and ``develop`` the app:

.. class:: small incremental

::

    (pyramidenv)$ cd wikitutorial
    (pyramidenv)$ python setup.py develop


See It Live
-----------

Use the ``pserve`` command installed by pyramid to serve our app:

.. class:: small

::

    (pyramidenv)$ pserve development.ini
    Starting server in PID 16698.
    serving on http://0.0.0.0:6543

.. class:: incremental

This brings up a new *wsgi server* provided by ``waitress`` serving our app.

.. class:: incremental

Load http://localhost:6543 and view your app root.


Why is it Pretty?
-----------------

We should be looking at an instance of MyModel:

.. code-block:: python
    :class: small

    class MyModel(PersistentMapping):
        __parent__ = __name__ = None

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


View Config - Predicates
------------------------

View configuration takes many arguments.  Here we use two.

.. class:: incremental

``context`` determines the *type* of object to which this view can be applied

.. class:: incremental

It's an example of a *predicate* argument

.. class:: incremental

*Predicates* place restrictions on how and when a view is used.

.. class:: incremental

Read more about predicates in `view configuration
<http://docs.pylonsproject.org/projects/pyramid/en/1.1-branch/narr/viewconfig.html>`_


View Config - Renderers
-----------------------

Pyramid separates the concerns of *view* and *renderer*

.. class:: incremental

So far, *views* prepare a data context **and** render it

.. class:: incremental

In Pyramid, the *view* only prepares the data to be rendered

.. class:: incremental

A ``renderer`` transforms this to something suitable for an HTTP response.

.. class:: incremental

In this case, ``renderer`` is a template that will return HTML


View Config - Summary
---------------------

In summary, then, our view configuration:

.. class:: incremental

* checks to see that we have traversed to an instance of ``MyModel``
* calls the ``my_view`` function, which returns a simple dictionary
* passes that dictionary to the ``mytemplate`` template
* the template is rendered and returned as the body of an HTTP response.

.. class:: incremental

And that is how we end up looking at that very pretty page.


Break Time
----------

So far:

.. class:: incremental

* we've taken a look at where Pyramid comes from
* we've seen how it is like and unlike other frameworks we've seen.
* we've met the ZODB *object store* and talked about how it differs from a
  database
* we've learned about *traversal* and how it differs from URL dispatch
* we've set up a Pyramid app using both
* we've looked at how the example code in that application works.

.. class:: incremental

Next, we'll start working on building our app, starting with Models.


Before We Begin
---------------

In your *package* directory you should see a file: ``Data.fs``.

.. class:: incremental

We are going to be starting over, so let's clear it.

.. class:: incremental

Make sure Pyramid is not running.

.. class:: incremental

Delete Data.fs. It will be re-created as needed.

.. class:: incremental

You can also delete Data.fs.* (.tmp, .index, .lock)


Wiki Models
-----------

First, we want a *wiki* class to serve as our app *root*.

.. class:: incremental

We also need a *page* class representing a wiki page.

.. class:: incremental

This will be the type we view when we are looking at the wiki.

.. class:: incremental

These two classes will need to be stored in our ZODB

.. class:: incremental

This means we need to talk about *persistence*.


Persistence Magic
-----------------

In SQL, data *about* an object is written to tables.

.. class:: incremental

In the ZODB, the *object itself* is saved in the database.

.. class:: incremental

The ZODB provides special classes that help us with this.

.. class:: incremental

Instances of these classes are able to know when they've been changed.

.. class:: incremental

When a ZODB transaction is committed, all changes objects are saved.


Persistent Base Classes
-----------------------

We'll be using two of these classes in our wiki:

.. class:: incremental

* **Persistent** - automatically saves changes to class attributes

* **PersistentMapping** - like a *dictionary*, saves changes to itself *and
  its keys and values*.

.. class:: incremental small

Other structures like lists and B-Trees are also available, but we wont use
them here.

.. class:: incremental

By subclassing these, we automatically gain persistence.


Traversal Magic
---------------

Our wiki system will use *traversal* dispatch

.. class:: incremental

Two object attributes support *traversal*: 

.. class:: incremental

* ``__name__`` (who am I)
* ``__parent__`` (where am I)

.. class:: incremental

Every object in a traversal-based system **must** provide these two
attributes.

.. class:: incremental

The *root* object will set these to ``None``.


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

Update ``appmaker`` for our new models:

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

We've deleted the ``MyModel`` class.

.. class:: incremental

But we still have *views* that reference the class.

.. container:: incremental

    Open ``views.py`` and delete everything except the first import

    .. code-block:: python
        :class: small

        from pyramid.view import view_config

.. class:: incremental

Next come tests for our new models.


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

        def test_constructor(self):
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
            from wikitutorial.models import appmaker
            return appmaker(zodb_root)

        def test_initialization(self):
            root = {}
            self._callFUT(root)
            self.assertEqual(root['app_root']['FrontPage'].data,
                             'This is the front page')


A Side Note
-----------

Note that there are *few* module level imports in ``tests.py``

.. class:: incremental

Also note that each TestCase has a helper method to import the class it will
test.

.. class:: incremental

This is unusual, but it reflects Pyramid `testing best practices
<http://docs.pylonsproject.org/en/latest/community/testing.html>`_

.. class:: incremental

In short, the idea is to prevent import problems from breaking *all* your
tests.


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

    (pyramidenv)$ nosetests --cover-package=tutorial --cover-erase\
        --with-coverage


Preparing for Views
-------------------

The ``data`` attribute of our ``Page`` model holds the text of the page.

.. class:: incremental

We'll use ReStructuredText, which can be rendered to HTML

.. class:: incremental

Rendering is provided by a python package called ``docutils``.

.. class:: incremental

Our application is a python package, and can declare its own dependencies.

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

Changes to ``setup.py`` always require a re-install::

    (pyramidenv)$ python setup.py develop

.. class:: incremental

You'll see a whole bunch of stuff flicker by. In it will be a reference to
``Searching for docutils``.


Adding Views
------------

We are ready to add views now. We'll need:

.. class:: incremental

* A view of the Wiki itself, which redirects to the front page.
* A view of an existing Page
* A view that allows us to *add* a new Page
* A view that allows us to *edit* and existing Page

.. class:: incremental

As we move forward, we'll be writing tests first, then building the code to
pass them.


Testing the Wiki View
---------------------

We want our wiki to automaticall redirect to ``FrontPage``.

.. container:: incremental

    Add this new TestCase to ``tests.py``:
    
    .. code-block:: python
        :class: small
    
        class WikiViewTests(unittest.TestCase):

            def test_redirect(self):
                from wikitutorial.views import view_wiki
                context = testing.DummyResource()
                request = testing.DummyRequest()
                response = view_wiki(context, request)
                self.assertEqual(response.location,
                                 'http://example.com/FrontPage')


Run The Tests
-------------

.. class:: small

::

    (pyramidenv)$ python setup.py test
    ...

    ======================================================================
    ERROR: test_redirect (wikitutorial.tests.WikiViewTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/path/to/wikitutorial/wikitutorial/tests.py", line 51, in test_redirect
        from wikitutorial.views import view_wiki
    ImportError: cannot import name view_wiki

    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    FAILED (errors=1)


Adding view_wiki
----------------

Open ``views.py`` again.  Add the following:

.. code-block:: python
    :class: small
    
    from pyramid.httpexceptions import HTTPFound
    from pyramid.view import view_config # <- ALREADY THERE
    
    @view_config(context='.models.Wiki')
    def view_wiki(context, request):
        return HTTPFound(location=request.resource_url(context,
                                                       'FrontPage'))

.. container:: incremental

    And re-run tests:
    
    .. class:: small
    
    ::
    
        (pyramidenv)$ python setup.py test
        ...
        Ran 4 tests in 0.001s
        OK 


Some Notes
----------

Note that ``@view_config`` has no ``renderer`` argument.

.. class:: incremental

It will never be shown, so there's no need

.. class:: incremental

Instead, it returns ``HTTPFound``, (``302 Found``), which requires a
``location``

.. class:: incremental

The ``.resource_url()`` method of a ``request`` object builds a URL for us.


A Page View
-----------

Our view of a page will need to accomplish a few things:

.. class:: incremental

* convert the Page ``data`` to HTML
* make WikiWords in the HTML into appropriate links
* provide a url for editing itself

.. class:: incremental

Let's test and implement these features one at a time


Test HTML Rendering
-------------------

Add the following new TestCase to ``tests.py``

.. code-block:: python
    :class: small

    class PageViewTests(unittest.TestCase):
        def _callFUT(self, context, request):
            from wikitutorial.views import view_page
            return view_page(context, request)

        def test_it(self):
            wiki = testing.DummyResource()
            context = testing.DummyResource(data='Hello CruelWorld IDoExist')
            context.__parent__ = wiki
            context.__name__ = 'thepage'
            request = testing.DummyRequest()
            info = self._callFUT(context, request)
            self.assertTrue('<div class="document">' in info['content'])
            for word in context.data.split():
                self.assertTrue(word in info['content'])


Run The Tests
-------------

Verify that you now have five, and that one is failing

.. class:: incremental

Our tests is relying on an artifact of how docutils builds HTML

.. class:: incremental

It makes it a weak tests, but okay for illustrative purposes.

.. class:: incremental

Now, let's get it passing


Start view_page
---------------

Add this code to ``views.py``:

.. code-block:: python
    :class: small

    # an import
    from docutils.core import publish_parts
    
    # and a method
    @view_config(context='.models.Page', renderer='templates/view.pt')
    def view_page(context, request):
        content = publish_parts(
            context.data, writer_name='html')['html_body']
        return dict(page=context, content=content)

.. class:: small incremental

::

    (pyramidenv)$ python setup.py test
    ...
    Ran 5 tests in 0.143s
    OK


Test Link Building
------------------

Add the following to our test:

.. code-block:: python
    :class: small

    def test_it(self):
        wiki = testing.DummyResource()
        wiki['IDoExist'] = testing.DummyResource() #<- add this
        context = testing.DummyResource(data='Hello CruelWorld IDoExist')
        #...
        # Add the following loop and assertion
        for url in (request.resource_url(wiki['IDoExist']),
                    request.resource_url(wiki, 'add_page', 'CruelWorld')):
            self.assertTrue(url in info['content'])

.. class:: small incremental

::

    (pyramidenv)$ python setup.py test
    Ran 5 tests in 0.108s
    FAILED (failures=1)


Finding WikiWords
-----------------

We'll use a regular expression to find WikiWords in our page data

.. container:: incremental

    Add the following to ``views.py``:

    .. code-block:: python
        :class: small
    
        # one import
        import re
        
        # and one module constant
        WIKIWORDS = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

.. class:: incremental

Now, we use this to build a curried function that converts WikiWords to links


Converting WikiWords
--------------------

.. code-block:: python
    :class: small
    
    # in views.py
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
        content = WIKIWORDS.sub(check, content) #<- add this line
        return #... <- this already exists


Check Your Progress
-------------------

Tests should now be five for five again.


Test Edit Link
--------------

Finally, we need to verify that ``view_page`` also returns a link to edit
*this* page.

.. container:: incremental

    Add this to our test:
    
    .. code-block:: python
        :class: small
        
        def test_it(self):
            #...
            self.assertEqual(info['edit_url'],
                             'http://example.com/thepage/edit_page')

.. class:: small incremental

::

    (pyramidenv)$ python setup.py test
    Ran 5 tests in 0.110s
    FAILED (errors=1)


Return Edit Link
----------------

Update ``view_page``:

.. code-block:: python
    :class: small

    def view_page(context, request):
        #...
        content = wikiwords.sub(check, content) #<- already there
        edit_url = request.resource_url(context, 'edit_page') #<- add
        return dict(page=context,
                    content=content,
                    edit_url = edit_url)

.. class:: small incremental

::

    (pyramidenv)$ python setup.py test
    Ran 5 tests in 0.110s
    OK


Adding Templates
----------------

What is the page template name for ``view_page``?

.. class:: incremental

Create ``view.pt`` in your ``templates`` directory.

.. class:: incremental

Also copy the file ``base.pt`` from the class resources.

.. class:: incremental

Pyramid can use a number of different templating engines.

.. class:: incremental

We'll be using Chameleon, which also supports extending other templates.


Chameleon Templates
-------------------

Chameleon page templates are valid XML/HTML.

.. class:: incremental

You can validate and view templates in browsers without the templating engine.

.. class:: incremental

This can be helpful in working with designers or front-end folks

.. class:: incremental

Instead of using special tags for processing directives, Chameleon uses XML
tag attributes.


TAL/METAL
---------

Chameleon is descended from Zope Page Templates (ZPT)

.. class:: incremental

It uses two XML namespaces for directives:

.. class:: incremental

* TAL (Template Attribute Language)
* METAL (Macro Extension to the Template Attribute Language)

.. class:: incremental

TAL provides basic directives for logical structures

.. class:: incremental

METAL provides directives for creating and using template Macros


TAL Statements
--------------

TAL and METAL statements are XML tag attributes.

.. class:: incremental

This means they look just like ``id="foo"`` or ``class="bar"``

.. class:: incremental

* ``tal:<operator>=”<expression>”``

* The ``tal:`` is a ‘namespace identifier’ (xml)

  * Not strictly required, but helpful

  * Strongly encouraged :)


TAL Operators
-------------

There are seven basic TAL operators, which are processed in this order

.. class:: incremental

* ``tal:define`` - set a value or values
* ``tal:condition`` - test truth value to execute
* ``tal:repeat`` - loop over sets of values
* ``tal:content`` - set the content of a tag
* ``tal:replace`` - replace an entire tag
* ``tal:attributes`` - set html/xml attributes of a tag
* ``tal:omit-tag`` - if expression is false, omit the tag

.. class:: incremental

``content`` and ``replace`` are mutually exclusive.


TAL Expressions
---------------

The right half of a TAL statement is an *expression* using the TAL expression
syntax (TALES):

.. class:: incremental

* Exists - ``exists:foo``
* Import - ``import:foo.bar.baz``
* Load = ``load:../other_template.pt``
* Not - ``not: is_anon``
* Python - ``python: here.Title()``
* String - ``string:my ${value}``
* Structure - ``structure:some_html``


METAL Operators
---------------

METAL provides operators related to creating and using template macros:

.. class:: incremental

* ``metal:define-macro`` - designates a DOM scope as a macro
* ``metal:use-macro`` - indicates that a macro should be used
* ``metal:extend-macro`` - extend an existing macro
* ``metal:define-slot`` - designate a customization point for a macro
* ``metal:fill-slot`` - provide custom content for a macro slot

.. class:: incremental

Much of this will become clearer as we actually create our templates.


The view.pt Template
--------------------

Type this code into your ``view.pt`` file:

.. code-block:: xml

    <metal:main use-macro="load: base.pt">
     <metal:content metal:fill-slot="main-content">
      <div tal:replace="structure:content">
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

``<metal>`` and ``<tal>`` tags are processed and removed by the engine.

.. class:: incremental

* ``use-macro="load: base.pt"``: we will be using ``base.pt`` as our main
  template *macro*.
* Template *macros* define one or more *slots*.
* ``metal:fill-slot="main-content"``: everything goes in the ``main-content``
  slot.


More Notes
----------

.. code-block:: xml

    <div tal:replace="structure:content">
      Page text goes here.
    </div>

The ``tal`` directive ``replace`` replaces the ``<div>`` tag with ``content``.

The ``structure`` expression ensures that the HTML is not escaped.

.. container:: incremental

    .. code-block:: xml

        <a tal:attributes="href edit_url" href="">
          Edit this page
        </a>

    Here, we use the ``tal`` directive ``attributes`` to set the ``href`` for
    our anchor to the value passed into our template as ``edit_url``.


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


Page Editing
------------

You'll notice that the page has a link to ``Edit This Page``

.. class:: incremental

If you click it, you get a 404.  We haven't created that view yet.

.. class:: incremental

Let's start by adding tests to ensure:

.. class:: incremental

* the edit view will submit to itself
* will save page data updates
* will redirect back to the page view after saving


Test Page Editing
-----------------

In ``tests.py``:

.. code-block:: python
    :class: small
    
    class EditPageTests(unittest.TestCase):
        def _callFUT(self, context, request):
            from .views import edit_page
            return edit_page(context, request)

        def test_it_notsubmitted(self):
            context = testing.DummyResource()
            request = testing.DummyRequest()
            info = self._callFUT(context, request)
            self.assertEqual(info['page'], context)
            self.assertEqual(info['save_url'],
                             request.resource_url(context, 'edit_page'))


One More Method
---------------

.. code-block:: python
    :class: small
    
    class EditPageTests(unittest.TestCase):
        # ...
        
        def test_it_submitted(self):
            context = testing.DummyResource()
            request = testing.DummyRequest({'form.submitted':True,
                                            'body':'Chapel Hill Rocks'})
            response = self._callFUT(context, request)
            self.assertEqual(response.location, 'http://example.com/')
            self.assertEqual(context.data, 'Chapel Hill Rocks')

.. class:: small incremental

::

    (pyramidenv)$ python setup.py test
    Ran 7 tests in 0.110s
    FAILED (errors=2)


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

.. class:: incremental

Note the ``name`` in ``view_config``.

.. class:: incremental

When traversal runs out of objects, it tries to find views by name


Check Your Tests
----------------

Even without a template we can run our tests:

.. class:: small incremental

::

    (pyramidenv)$ python setup.py test
    ...
    ----------------------------------------------------------------------
    Ran 7 tests in 0.112s

    OK


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


Page Creation
-------------

Again, we need a new view.  This one will

.. class:: incremental

* have the wiki itself as ``context``
* allow us to fill out the new page content
* save the new page when submitted
* return us to a view of the new page

.. class:: incremental

Again, we start by testing for this


Test Adding a Page
------------------

In ``tests.py``:

.. code-block:: python 
    :class: small
    
    class AddPageTests(unittest.TestCase):
        def _callFUT(self, context, request):
            from .views import add_page
            return add_page(context, request)

        def test_it_notsubmitted(self):
            context = testing.DummyResource()
            request = testing.DummyRequest()
            request.subpath = ['AnotherPage']
            info = self._callFUT(context, request)
            self.assertEqual(info['page'].data,'')
            self.assertEqual(
                info['save_url'],
                request.resource_url(context, 'add_page', 'AnotherPage'))


One More Method
---------------

.. code-block:: python 
    :class: small
    
    class AddPageTests(unittest.TestCase):
        #...
        
        def test_it_submitted(self):
            context = testing.DummyResource()
            request = testing.DummyRequest({'form.submitted':True,
                                            'body':'Go UNC!'})
            request.subpath = ['AnotherPage']
            self._callFUT(context, request)
            page = context['AnotherPage']
            self.assertEqual(page.data, 'Go UNC!')
            self.assertEqual(page.__name__, 'AnotherPage')
            self.assertEqual(page.__parent__, context)

.. class:: small incremental

::

    (pyramidenv)$ python setup.py test
    Ran 9 tests in 0.117s
    FAILED (errors=2)


Adding a Page
-------------

Back in ``views.py`` add the code for creating a new page

.. container:: incremental

    Start with imports and the view_config:

    .. code-block:: python
        :class: small

        # add an import
        from wikitutorial.models import Page

        @view_config(name='add_page', context='.models.Wiki',
                     renderer='templates/edit.pt')


The View Function
-----------------

.. code-block:: python
    :class: small

    @view_config(...) #<- already there.
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

Note that this view also has a ``name``.

.. class:: incremental

``pagename = request.subpath[0]`` gives us the first element of the path
*after* the current context and view name. What is that?

.. class:: incremental

Notice that *here* is where we set the ``__name__`` and ``__parent__``
attributes of our new Page.

.. class:: incremental

We add a new Page to the wiki as if the wiki were a Python ``dict``:
``context[pagename] = page``


One More Note
-------------

Look at the similarity in how a form is handled here to the way it is handled
in Django and Flask (in pseudocode):

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


Check Your Tests
----------------

.. class:: small

::

    (pyramidenv)$ python setup.py test
    ...
    test_it_notsubmitted (wikitutorial.tests.AddPageTests) ... ok
    test_it_submitted (wikitutorial.tests.AddPageTests) ... ok
    test_initialization (wikitutorial.tests.AppmakerTests) ... ok
    test_it_notsubmitted (wikitutorial.tests.EditPageTests) ... ok
    test_it_submitted (wikitutorial.tests.EditPageTests) ... ok
    test_constructor (wikitutorial.tests.PageModelTests) ... ok
    test_it (wikitutorial.tests.PageViewTests) ... ok
    test_constructor (wikitutorial.tests.WikiModelTests) ... ok
    test_redirect (wikitutorial.tests.WikiViewTests) ... ok

    ----------------------------------------------------------------------
    Ran 9 tests in 0.111s

    OK

.. class:: incremental center

**WAHOOOOOOO!!!**


In-Class Exercises
------------------

Try to accomplish as many of these as you can before you leave:

.. class:: incremental

* Make the add_page view show "Adding <NewPage>" in the header (*do not create
  a new template to do this*)
* Make the edit_page and add_page views **only** change data on POST.
* Make the link that says "You can return to the FrontPage" disappear when you
  are viewing the front page.

