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


Security
--------

We've got a solid start on a wiki that works.

.. class:: incremental

But everyone who visits the wiki can author and edit pages.

.. class:: incremental

It's a recipe for **TOTAL CHAOS**

.. class:: incremental

Let's lock it down a bit.


AuthN and AuthZ
---------------

There are two aspects to the process of access control online.

.. class:: incremental

* **Authentication**: Verification of the identity of a *principal*
* **Authorization**: Enumeration of the rights of that *principal* in a
  context.

.. class:: incremental

All systems with access control involve both of these aspects.

.. class:: incremental

AuthZ in our Flask and Django apps was minimal


Pyramid Security
----------------

In Pyramid these two aspects are handled by separate configuration settings:

.. class:: incremental

* ``config.set_authentication_policy(AuthnPolicy())``
* ``config.set_authorization_policy(AuthzPolicy())``

.. class:: incremental

If you set one, you must set the other.

.. class:: incremental

Pyramid comes with a few policy classes included.

.. class:: incremental

You can also roll your own, so long as they fulfill the contract.


Our Wiki Security
-----------------

We'll be using two built-in policies today:

.. class:: incremental

* ``AuthTktAuthenticationPolicy``: sets an expirable authentication ticket
  cookie.
* ``ACLAuthorizationPolicy``: uses an *Access Control List* to grant
  permissions to *principals*

.. class:: incremental

Our access control system will have the following properties:

.. class:: incremental

* Everyone can view pages
* Users who log in may be added to an 'editors' group
* Editors can add and edit pages.


Testing First
-------------

Let's begin by testing for our desired properties.

.. class:: incremental

We'll need to create a new TestCase for this.

.. class:: incremental

This TestCase will be a bit different.  We need a request to engage security

.. class:: incremental

These tests will be *functional tests* where our earlier tests were *unit
tests*

.. class:: incremental

We'll set up a zodb and a full-fledged app.


In tests.py
-----------

We'll need some information for testing logging in:

.. code-block:: python
    :class: small
    
    class FunctionalTests(unittest.TestCase):

        viewer_login = '/login?login=viewer&password=viewer' \
                       '&came_from=FrontPage&form.submitted=Login'
        viewer_wrong_login = '/login?login=viewer&password=incorrect' \
                       '&came_from=FrontPage&form.submitted=Login'
        editor_login = '/login?login=editor&password=editor' \
                       '&came_from=FrontPage&form.submitted=Login'


Test Setup
----------

We'll also need to create an app and provide a zodb to hold it:

.. code-block:: python
    :class: tiny

    class FunctionalTests(unittest.TestCase):
        #...
        def setUp(self):
            import tempfile
            import os.path
            from wikitutorial import main
            self.tmpdir = tempfile.mkdtemp()

            dbpath = os.path.join( self.tmpdir, 'test.db')
            uri = 'file://' + dbpath
            settings = { 'zodbconn.uri' : uri ,
                         'pyramid.includes': ['pyramid_zodbconn',
                                              'pyramid_tm'] }

            app = main({}, **settings)
            self.db = app.registry._zodb_databases['']
            from webtest import TestApp
            self.testapp = TestApp(app)


Test Teardown
-------------

And since we set all that up, we need to destroy it after each test, too:

.. code-block:: python
    :class: small

    def tearDown(self):
        import shutil
        self.db.close()
        shutil.rmtree( self.tmpdir )


Testing Login
-------------

Let's add a few tests to demonstrate that ``AuthN`` works:

.. code-block:: python
    :class: small

    def test_successful_log_in(self):
        res = self.testapp.get( self.viewer_login, status=302)
        self.assertEqual(res.location, 'http://localhost/FrontPage')

    def test_failed_log_in(self):
        res = self.testapp.get( self.viewer_wrong_login, status=200)
        self.assertTrue('login' in res.body)


Testing Anonymous Users
-----------------------

We should verify that anonymous users can see pages, but cannot edit or add:

.. code-block:: python
    :class: small

    def test_anonymous_user_cannot_edit(self):
        res = self.testapp.get('/FrontPage/edit_page', status=200)
        self.assertTrue('Login' in res.body)

    def test_anonymous_user_cannot_add(self):
        res = self.testapp.get('/add_page/NewPage', status=200)
        self.assertTrue('Login' in res.body)


Testing Viewers
---------------

Authenticated users who are not editors should be the same:

.. code-block:: python
    :class: small

    def test_viewer_user_cannot_edit(self):
        res = self.testapp.get( self.viewer_login, status=302)
        res = self.testapp.get('/FrontPage/edit_page', status=200)
        self.assertTrue('Login' in res.body)

    def test_viewer_user_cannot_add(self):
        res = self.testapp.get( self.viewer_login, status=302)
        res = self.testapp.get('/add_page/NewPage', status=200)
        self.assertTrue('Login' in res.body)


Testing Editors
---------------

Finally, editors should be able to do it all:

.. code-block:: python
    :class: small

    def test_editors_member_user_can_edit(self):
        res = self.testapp.get( self.editor_login, status=302)
        res = self.testapp.get('/FrontPage/edit_page', status=200)
        self.assertTrue('Editing' in res.body)

    def test_editors_member_user_can_add(self):
        res = self.testapp.get( self.editor_login, status=302)
        res = self.testapp.get('/add_page/NewPage', status=200)
        self.assertTrue('Editing' in res.body)

    def test_editors_member_user_can_view(self):
        res = self.testapp.get( self.editor_login, status=302)
        res = self.testapp.get('/FrontPage', status=200)
        self.assertTrue('FrontPage' in res.body)


One Bit of Cleanup
------------------

These lines in our test setup will cause us problems:

.. code-block:: python
    :class: small
    
    from webtest import TestApp
    self.testapp = TestApp(app)

.. class:: incremental

We have introduced a dependency on the package ``webtest``

.. class:: incremental

Our package should be explicit about its dependencies.

.. class:: incremental

Do you remember how to declare a dependency?  


Fix setup.py / re-install
-------------------------

In ``setup.py`` find ``requires`` and add the following:

.. code-block:: python
    :class: small
    
    requires = [
        #...
        'docutils',
        'webtest', #<- we are adding this line
        ]

.. class:: incremental

Then, re-install our package using ``develop``:

.. class:: incremental small

::

    (pyramidenv)$ python setup.py develop


Run Our Tests
-------------

We can run these tests, to verify that they don't just work:

.. class:: small incremental

::

    (pyramidenv)$ python setup.py test

    ----------------------------------------------------------------------
    Ran 18 tests in 1.032s

    FAILED (failures=2, errors=7)

.. class:: incremental

Great!  Lot's of problems to fix!


Contextual ACLs
---------------

In Pyramid, ACL security is *contextual*.

.. class:: incremental

What a user is allowed to do is dependent on *context*.

.. class:: incremental

In a *traversal* app, context is defined as the object you are viewing.

.. class:: incremental

A *view* can require a given permission.

.. class:: incremental

The object viewed is responsible for determining *who* has *what rights*.


ACL Inheritance
---------------

Under the default ACL policy, permissions are inherited.

.. class:: incremental

If *this* object does not declare an ACL, then its ``__parent__`` is checked

.. class:: incremental

If you get all the way back to the root without hitting an ACL, then access is
denied.

.. class:: incremental

Thus, the default ACL policy is secure by default.

.. class:: incremental

Let's set up our policy.


Our Users and Groups
--------------------

Create a new file ``security.py`` in your wikitutorial package and add the
following:

.. code-block:: python
    :class: small incremental
    
    USERS = {
        'editor': 'editor',
        'viewer': 'viewer',
    }
    
    GROUPS = {
        'editor': ['group:editors'],
    }
    
    def groupfinder(userid, request):
        if userid in USERS:
            return GROUPS.get(userid, [])


Security Configuration
----------------------

In our ``__init__.py`` file, add the following:

.. code-block:: python
    :class: small

    # a few imports
    from pyramid.authentication import AuthTktAuthenticationPolicy
    from pyramid.authorization import ACLAuthorizationPolicy
    from .security import groupfinder
    
    # and some configuration
    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        authn_policy = AuthTktAuthenticationPolicy(
            'youdontknowit', callback=groupfinder, hashalg='sha512')
        authz_policy = ACLAuthorizationPolicy()
        config = Configurator(...) #<- already there
        config.set_authentication_policy(authn_policy)
        config.set_authorization_policy(authz_policy)
        #...


Add an ACL
----------

We can set a global ACL on our wiki root class:

.. code-block:: python
    :class: small
    
    # add an import
    from pyramid.security import Allow, Everyone
    
    # and alter our wiki class:
    class Wiki(PersistentMapping):
        #...
        __acl__ = [(Allow, Everyone, 'view'),
                   (Allow, 'group:editors', 'edit')]

.. class:: incremental

An ACL is a list of Access Control Entries

.. class:: incremental

Each ACE is a tuple of *action*, *principal* and *permission*


Require Permission
------------------

In order to match, an ACE must *Allow* the current *principal* the required
*permission*

.. class:: incremental

Our ``views`` are responsible for saying what *permission* is required

.. code-block:: python
    :class: incremental small
    
    # for the view_page() view:
    @view_config(context='.models.Page', renderer='templates/view.pt',
                 permission='view')
    
    # for add_page() and edit_page()
    @view_config(route_name='<name>', renderer='templates/edit.pt',
                 permission='edit')


Provide Login/Logout
--------------------

We need to allow users a way to log in and out.  Start with the views:

.. code-block:: python
    :class: small
    
    # add imports to views.py
    from pyramid.view import forbidden_view_config
    from pyramid.security import remember, forget
    from wikitutorial.security import USERS

    # and a logout view:
    @view_config(context='.models.Wiki', name='logout')
    def logout(context, request):
        headers = forget(request)
        return HTTPFound(location=request.resource_url(context),
                         headers=headers)

.. class:: incremental

Next, add the login view


The Login View
--------------

.. code-block:: python
    :class: tiny
    
    @view_config(context='.models.Wiki', name='login',
                 renderer='templates/login.pt')
    @forbidden_view_config(renderer='templates/login.pt')
    def login(request):
        login_url = request.resource_url(request.context, 'login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/' # never use the login form itself as came_from
        came_from = request.params.get('came_from', referrer)
        message = login = password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            if USERS.get(login) == password:
                headers = remember(request, login)
                return HTTPFound(location = came_from,
                                 headers = headers)
            message = 'Failed login'

        ctxt = dict(message=message, came_from=came_from,
                    login=login, password=password,
                    url=request.application_url + '/login',)
        return ctxt





The Login Template
------------------

Add ``login.pt`` to the ``templates`` directory

.. code-block:: xml
    :class: small
    
    <metal:main use-macro="load: base.pt">
      <metal:pagename metal:fill-slot="page-name">
        <b>Login</b><br/>
        <span tal:replace="message"/>
      </metal:pagename>
      <metal:login metal:fill-slot="login"></metal:login>
      <metal:content metal:fill-slot="main-content">
        <form action="${url}" method="post">
          <input type="hidden" name="came_from" value="${came_from}"/>
          <input type="text" name="login" value="${login}"/><br/>
          <input type="password" name="password"
                 value="${password}"/><br/>
          <input type="submit" name="form.submitted" value="Log In"/>
        </form>
      </metal:content>
    </metal:main>


Unblock Logout Link
-------------------

All along, we've had a logout link in our ``base.pt``

.. class:: incremental

But we've been blocking it from showing in our templates.

.. class:: incremental

Let's allow it to show in the ``view.pt`` and ``edit.pt`` templates:

.. code-block:: xml
    :class: small incremental
    
    <!-- Delete This Line -->
    <metal:login metal:fill-slot="login"></metal:login>


Conditional Logout
------------------

Look at ``base.pt``:

.. code-block:: xml
    :class: small
    
    <metal:login define-slot="login">
    <span tal:condition="logged_in">
      <a href="${request.application_url}/logout">Logout</a>
    </span>
    </metal:login>

.. class:: incremental

Showing the 'logout' link is dependent on ``logged_in``

.. class:: incremental

We have to make sure that this boolean flag is in the template context


Add logged_in Flag
------------------

Back in ``views.py`` add the following import:

.. code-block:: python
    :class: small
    
    from pyramid.security import authenticated_userid

.. class:: incremental

This will return the id of the authenticated user, or None.

.. container:: incremental

    Add this to all return contexts for our views (except ``login``):

    .. code-block:: python
        :class: small
    
        logged_in = authenticated_userid(request)


Check Your Work
---------------

.. class:: small

::

    (pyramidenv)$ python setup.py test
    ...
    test_anonymous_user_cannot_add (wikitutorial.tests.FunctionalTests) ... ok
    test_anonymous_user_cannot_edit (wikitutorial.tests.FunctionalTests) ... ok
    test_editors_member_user_can_add (wikitutorial.tests.FunctionalTests) ... ok
    test_editors_member_user_can_edit (wikitutorial.tests.FunctionalTests) ... ok
    test_editors_member_user_can_view (wikitutorial.tests.FunctionalTests) ... ok
    test_failed_log_in (wikitutorial.tests.FunctionalTests) ... ok
    test_successful_log_in (wikitutorial.tests.FunctionalTests) ... ok
    test_viewer_user_cannot_add (wikitutorial.tests.FunctionalTests) ... ok
    test_viewer_user_cannot_edit (wikitutorial.tests.FunctionalTests) ... ok
    ...
    ----------------------------------------------------------------------
    Ran 18 tests in 1.143s

    OK


Reap the Reward
---------------

Check your work in a browser:

.. class:: small

::

    (pyramidenv)$ pserve development.ini
    Starting server in PID 36414.
    serving on http://0.0.0.0:6543

.. class:: 

Visit http://localhost:6543 and play for a bit


Next Steps
----------

We've got a workable basic wiki here, but there are some improvements that
could be nice:

.. class:: incremental

* Make the add_page view show "Adding <NewPage>" in the header without
  creating a new template
* Improve messaging to let users know when they've saved or created a page.
* Make the link that says "You can return to the FrontPage" disappear when you
  are viewing the front page.
* Improve security by forcing the edit_page and add_page views **only** change
  data on POST.
* Improve the security model a bit: 'viewers' can add pages, and retain the
  ability to edit pages they created.


Closing Up
----------

But all that's for another time.

.. class:: incremental

For this session, we are done.

