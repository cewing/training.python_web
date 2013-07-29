Internet Programming with Python
================================

.. image:: img/pyramid-medium.png
    :align: left
    :width: 50%

Session 10: A Pyramid Application

.. class:: intro-blurb right

| The flexible framework.
| Totally not built by aliens.


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

