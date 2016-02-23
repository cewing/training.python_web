**********
Session 07
**********

.. figure:: /_static/no_entry.jpg
    :align: center
    :width: 60%

    By `Joel Kramer via Flickr`_

.. _Joel Kramer via Flickr: https://www.flickr.com/photos/75001512@N00/2707796203

Security And Deployment
=======================

.. rst-class:: left
.. container::

    By the end of this session we'll have deployed our learning journal to a
    public server.

    So we will need to add a bit of security to it.

    We'll get started on that in a moment

But First
---------

.. rst-class:: large center

Questions About the Homework?

.. nextslide:: A Working Edit Form

.. code-block:: python

    class EntryEditForm(EntryCreateForm):
        id = HiddenField()

`View the form online <https://github.com/cewing/training.python_web/blob/807a49f20fea1e7e7393347c82df47eff83f3210/resources/session07/forms.py#L25>`_

.. nextslide:: A Working Edit View

.. code-block:: python

    @view_config(route_name='action', match_param='action=edit',
                 renderer='templates/edit.jinja2')
    def update(request):
        id = int(request.params.get('id', -1))
        entry = Entry.by_id(id)
        if not entry:
            return HTTPNotFound()
        form = EntryEditForm(request.POST, entry)
        if request.method == 'POST' and form.validate():
            form.populate_obj(entry)
            return HTTPFound(location=request.route_url('detail', id=entry.id))
        return {'form': form, 'action': request.matchdict.get('action')}

`See this view online <https://github.com/cewing/training.python_web/blob/807a49f20fea1e7e7393347c82df47eff83f3210/resources/session07/views.py#L43>`_

.. nextslide:: Linking to the Edit Form

.. code-block:: html+jinja

    {% extends "layout.jinja2" %}
    {% block body %}
    <article>
      <!-- ... -->
    </article>
    <p>
      <a href="{{ request.route_url('home') }}">Go Back</a> ::
      <a href="{{ request.route_url('action', action='edit', _query=(('id',entry.id),)) }}">
        Edit Entry</a>
    </p>
    {% endblock %}


`View this template online <https://github.com/cewing/training.python_web/blob/807a49f20fea1e7e7393347c82df47eff83f3210/resources/session07/detail.jinja2#L12>`_

.. nextslide:: A Working User Model

.. code-block:: python

    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(Unicode(255), unique=True, nullable=False)
        password = Column(Unicode(255), nullable=False)

        @classmethod
        def by_name(cls, name):
            return DBSession.query(cls).filter(cls.name == name).first()

`View this model online <https://github.com/cewing/training.python_web/blob/807a49f20fea1e7e7393347c82df47eff83f3210/resources/session07/models.py#L62>`_

Securing An Application
=======================

.. rst-class:: left
.. container::

    We've got a solid start on our learning journal.

    .. rst-class:: build
    .. container::

        We can:

        .. rst-class:: build

        * view a list of entries
        * view a single entry
        * create a new entry
        * edit existing entries

        But so can everyone who visits the journal.

        It's a recipe for **TOTAL CHAOS**

        Let's lock it down a bit.


AuthN and AuthZ
---------------

There are two aspects to the process of access control online.

.. rst-class:: build
.. container::

    .. rst-class:: build

    * **Authentication**: Verification of the identity of a *principal*
    * **Authorization**: Enumeration of the rights of that *principal* in a
      context.

    Think of them as **Who Am I** and **What Can I Do**

    All systems with access control involve both of these aspects.

    But many systems wire them together as one.


.. nextslide:: Pyramid Security

In Pyramid these two aspects are handled by separate configuration settings:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * ``config.set_authentication_policy(AuthnPolicy())``
    * ``config.set_authorization_policy(AuthzPolicy())``

    If you set one, you must set the other.

    Pyramid comes with a few policy classes included.

    You can also roll your own, so long as they fulfill the requried interface.

    You can learn about the interfaces for `authentication`_ and
    `authorization`_ in the Pyramid documentation

.. _authentication: http://docs.pylonsproject.org/projects/pyramid/en/latest/api/interfaces.html#pyramid.interfaces.IAuthenticationPolicy
.. _authorization: http://docs.pylonsproject.org/projects/pyramid/en/latest/api/interfaces.html#pyramid.interfaces.IAuthorizationPolicy

.. nextslide:: Our Journal Security

We'll be using two built-in policies today:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * ``AuthTktAuthenticationPolicy``: sets an expirable
      `authentication ticket`_ cookie.
    * ``ACLAuthorizationPolicy``: uses an `Access Control List`_ to grant
      permissions to *principals*

    Our access control system will have the following properties:

    .. rst-class:: build

    * Everyone can view entries, and the list of all entries
    * Users who log in may edit entries or create new ones

.. _authentication ticket: http://docs.pylonsproject.org/docs/pyramid/en/latest/api/authentication.html#pyramid.authentication.AuthTktAuthenticationPolicy
.. _Access Control List: http://docs.pylonsproject.org/docs/pyramid/en/latest/api/authorization.html#pyramid.authorization.ACLAuthorizationPolicy

.. nextslide:: Engaging Security

By default, Pyramid uses no security. We enable it through configuration.

.. rst-class:: build
.. container::

    Open ``learning_journal/__init__.py`` and update it as follows:

    .. code-block:: python

        # add these imports
        from pyramid.authentication import AuthTktAuthenticationPolicy
        from pyramid.authorization import ACLAuthorizationPolicy
        # and add this configuration:
        def main(global_config, **settings):
            # ...
            # update building the configurator to pass in our policies
            config = Configurator(
                settings=settings,
                authentication_policy=AuthTktAuthenticationPolicy('somesecret'),
                authorization_policy=ACLAuthorizationPolicy(),
                default_permission='view'
            )
            # ...

.. nextslide:: Verify It Worked

We've now informed our application that we want to use security.

.. rst-class:: build
.. container::

    By default we require the 'view' permission to see anything.

    But we have yet to assign *any permissions to anyone* at all.

    Let's verify now that we are unable to see anything in the website.

    Start your application, and try to view any page (You should get a 403
    Forbidden error response):

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 84467.
        serving on http://0.0.0.0:6543

    .. rst-class:: build

    * http://localhost:6543/
    * http://localhost:6543/journal/1
    * http://localhost:6543/journal/create
    * http://localhost:6543/journal/edit?id=1

Implementing Authz
------------------

Next we have to grant some permissions to principals.

.. rst-class:: build
.. container::

    Pyramid authorization relies on a concept it calls "context".

    A *principal* can be granted rights in a particular *context*

    Context can be made as specific as a single persistent object

    Or it can be generalized to a *route* or *view*

    To have a context, we need a Python object called a *factory* that must
    have an ``__acl__`` special attribute.

    The framework will use this object to determine what permissions a
    *principal* has

    Let's create one

.. nextslide:: Add ``security.py``

In the same folder where you have ``models.py`` and ``views.py``, add a new
file ``security.py``

.. rst-class:: build
.. container::

    .. code-block:: python

        from pyramid.security import Allow, Everyone, Authenticated

        class EntryFactory(object):
            __acl__ = [
                (Allow, Everyone, 'view'),
                (Allow, Authenticated, 'create'),
                (Allow, Authenticated, 'edit'),
            ]
            def __init__(self, request):
                pass

    The ``__acl__`` attribute of this object contains a list of *ACE*\ s

    An *ACE* combines an *action* (Allow, Deny), a *principal* and a *permission*

.. nextslide:: Using Our Context Factory

Now that we have a factory that will provide context for permissions to work,
we can tell our configuration to use it.

.. rst-class:: build
.. container::

    Open ``learning_journal/__init__.py`` and update the route configuration
    for our routes:

    .. code-block:: python

        # add an import at the top:
        from .security import EntryFactory
        # update the route configurations:
        def main(global_config, **settings):
            """ This function returns a Pyramid WSGI application.
            """
            # ... Add the factory keyword argument to our route configurations:
            config.add_route('home', '/', factory=EntryFactory)
            config.add_route('detail', '/journal/{id:\d+}', factory=EntryFactory)
            config.add_route('action', '/journal/{action}', factory=EntryFactory)

.. nextslide:: What We've Done

We've now told our application we want a principal to have the *view*
permission by default.

.. rst-class:: build
.. container::

    And we've provided a factory to supply context and an ACL for each route.

    Check our ACL. Who can view the home page?  The detail page?  The action
    pages?

    Pyramid allows us to set a *default_permission* for *all views*\ .

    But view configuration allows us to require a different permission for *a view*\ .

    Let's make our action views require appropriate permissions next

.. nextslide:: Requiring Permissions for a View

Open ``learning_journal/views.py``, and edit the ``@view_config`` for
``create`` and ``update``:

.. code-block:: python

    @view_config(route_name='action', match_param='action=create',
                 renderer='templates/edit.jinja2',
                 permission='create') # <-- ADD THIS
    def create(request):
        # ...

    @view_config(route_name='action', match_param='action=edit',
                 renderer='templates/edit.jinja2',
                 permission='edit') # <-- ADD THIS
    def update(request):
        # ...

.. nextslide:: Verify It Worked

At this point, our "action" views should require permissions other than the
default ``view``.

.. rst-class:: build
.. container::

    Start your application and verify that it is true:

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 84467.
        serving on http://0.0.0.0:6543

    .. rst-class:: build

    * http://localhost:6543/
    * http://localhost:6543/journal/1
    * http://localhost:6543/journal/create
    * http://localhost:6543/journal/edit?id=1

    You should get a ``403 Forbidden`` for the action pages only.

Implement AuthN
---------------

Now that we have authorization implemented, we need to add authentication.

.. rst-class:: build
.. container::

    By providing the system with an *authenticated user*, our ACEs for
    ``Authenticated`` will apply.

    We'll need to have a way for a user to prove who they are to the
    satisfaction of the system.

    The most common way of handling this is through a *username* and
    *password*.

    A person provides both in an html form.

    When the form is submitted, the system seeks a user with that name, and
    compares the passwords.

    If there is no such user, or the password does not match, authentication
    fails.

.. nextslide:: An Example

Let's imagine that Alice wants to authenticate with our website.

.. rst-class:: build
.. container::

    Her username is ``alice`` and her password is ``s3cr3t``.

    She fills these out in a form on our website and submits the form.

    Our website looks for a ``User`` object in the database with the username
    ``alice``.

    Let's imagine that there is one, so our site next compares the value she
    sent for her *password* to the value stored in the database.

    If her stored password is also ``s3cr3t``, then she is who she says she is.

    All set, right?

.. nextslide:: Encryption

The problem here is that the value we've stored for her password is in ``plain
text``.

.. rst-class:: build
.. container::

    This means that anyone could potentially steal our database and have access
    to all our users' passwords.

    Instead, we should *encrypt* her password with a strong one-way hash.

    Then we can store the hashed value.

    When she provides the plain text password to us, we *encrypt* it the same
    way, and compare the result to the stored value.

    If they match, then we know the value she provided is the same we used to
    create the stored hash.

.. nextslide:: Adding Encryption

Python provides a number of libraries for implementing strong encryption.

.. rst-class:: build
.. container::

    You should always use a well-known library for encryption.

    We'll use a good one called `Passlib`_.

    This library provides a number of different algorithms and a *context* that
    implements a simple interface for each.

    .. code-block:: python

        from passlib.context import CryptContext
        password_context = CryptContext(schemes=['pbkdf2_sha512'])
        hashed = password_context.encrypt('password')
        if password_context.verify('password', hashed):
            print "It matched"

.. _Passlib: https://pythonhosted.org/passlib/

.. nextslide:: Install Passlib

To install a new package as a dependency, we add the package to our list in
``setup.py``.

``Passlib`` provides a large number of different hashing schemes.  Some (like
``bcrypt``) require underlying ``C`` extensions to be compiled. If you do not
have a ``C`` compiler, these extensions will be disabled.

.. rst-class:: build
.. container::

    .. code-block:: python

        requires = [
          ...
          'wtforms',
          'passlib',
        ]

    Then, we re-install our package to pick up the new dependency:

    .. code-block:: bash

        (ljenv)$ python setup.py develop

    *note* if you have a c compiler installed but not the Python dev headers,
    this may not work.  Let me know if you get errors.

.. nextslide:: Using Passlib

As noted above, the passlib library uses a ``context`` object to manage
passwords.

.. rst-class:: build
.. container::

    This object supports a lot of functionality, but the only API we care about
    for this project is encrypting and verifying passwords.

    We'll create a single, global context to be used by our project.

    Since the ``User`` class is the component in our system that should have
    the responsibility for password interactions, we'll create our context in
    the same place it is defined.

    In ``learning_journal/models.py`` add the following code:

    .. code-block:: python
    
        # add an import at the top
        from passlib.context import CryptContext

        # then lower down, make a context at module scope:
        password_context = CryptContext(schemes=['pbkdf2_sha512'])


.. nextslide:: Comparing Passwords

Now that we have a context object available, let's write an instance method for
our ``User`` class that uses it to verify a plaintext password:

.. rst-class:: build
.. container::

    Again, in ``learning_journal/models.py`` add the following to the ``User``
    class:

    .. code-block:: python

        # add this method to the User class:
        class User(Base):
            # ...
            def verify_password(self, password):
                return password_context.verify(password, self.password)

.. nextslide:: Create a User

We'll also need to have a user for our system.

.. rst-class:: build
.. container::

    We can use the database initialization script to create one for us.

    Open ``learning_journal/scripts/initialzedb.py``:

    .. code-block:: python

        from learning_journal.models import password_context
        from learning_journal.models import User
        # and update the main function like so:
        def main(argv=sys.argv):
            # ...
            with transaction.manager:
                # replace the code to create a MyModel instance
                encrypted = password_context.encrypt('admin')
                admin = User(name='admin', password=encrypted)
                DBSession.add(admin)

.. nextslide:: Rebuild the Database:

In order to get our user created, we'll need to delete our database and
re-build it.

.. rst-class:: build
.. container::

    Make sure you are in the folder where ``setup.py`` appears.

    Then remove the sqlite database:

    .. code-block:: bash

        (ljenv)$ rm *.sqlite

    And re-initialize:

    .. code-block:: bash

        (ljenv)$ initialize_learning_journal_db development.ini
        ...
        2015-01-17 16:43:55,237 INFO  [sqlalchemy.engine.base.Engine][MainThread]
          INSERT INTO users (name, password) VALUES (?, ?)
        2015-01-17 16:43:55,237 INFO  [sqlalchemy.engine.base.Engine][MainThread]
          ('admin', '$2a$10$4Z6RVNhTE21mPLJW5VeiVe0EG57gN/HOb7V7GUwIr4n1vE.wTTTzy')

Providing Login UI
------------------

We now have a user in our database with a strongly encrypted password.

.. rst-class:: build
.. container::

    We also have a method on our user model that will verify a supplied
    password against this encrypted version.

    We must now provide a view that lets us log in to our application.

    We start by adding a new *route* to our configuration in
    ``learning_journal/__init__.py``:

    .. code-block:: python

        config.add_rount('action' ...)
        # ADD THIS
        config.add_route('auth', '/sign/{action}', factory=EntryFactory)

.. nextslide:: A Login Form

It would be nice to use the form library again to make a login form.

.. rst-class:: build
.. container::

    Open ``learning_journal/forms.py`` and add the following:

    .. code-block:: python

        # add an import:
        from wtforms import PasswordField
        # and a new form class
        class LoginForm(Form):
            username = TextField(
                'Username', [validators.Length(min=1, max=255)]
            )
            password = PasswordField(
                'Password', [validators.Length(min=1, max=255)]
            )


.. nextslide:: Login View in ``learning_journal/views.py``

.. ifnotslides::

    Next, we'll create a login view in ``learning_journal/views.py``

.. code-block:: python

    # new imports:
    from pyramid.security import forget, remember
    from .forms import LoginForm
    from .models import User
    # and a new view
    @view_config(route_name='auth', match_param='action=in', renderer='string',
         request_method='POST')
    def sign_in(request):
        login_form = None
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
        if login_form and login_form.validate():
            user = User.by_name(login_form.username.data)
            if user and user.verify_password(login_form.password.data):
                headers = remember(request, user.name)
            else:
                headers = forget(request)
        else:
            headers = forget(request)
        return HTTPFound(location=request.route_url('home'), headers=headers)

.. nextslide:: Where's the Renderer?

Notice that this view doesn't render anything. No matter what, you end up
returning to the ``home`` route.

.. rst-class:: build
.. container::

    We have to incorporate our login form somewhere.

    The home page seems like a good place.

    But we don't want to show it all the time.

    Only when we aren't logged in already.

    Let's give that a whirl.

.. nextslide:: Updating ``index_page``

Pyramid security provides a method that returns the id of the user who is
logged in, if any.

.. rst-class:: build
.. container::

    We can use that to update our home page in ``learning_journal/views.py``:

    .. code-block:: python

        # add an import:
        from pyramid.security import authenticated_userid

        # and update the index_page view:
        @view_config(...)
        def index_page(request):
            # ... get all entries here
            form = None
            if not authenticated_userid(request):
                form = LoginForm()
            return {'entries': entries, 'login_form': form}

.. nextslide:: Update ``list.jinja2``

Now we have to update the template for the ``index_page`` to display the form, *if it is there*

.. rst-class:: build
.. container::

    .. code-block:: jinja

        {% block body %}
        {% if login_form %}
        <aside><form action="{{ request.route_url('auth', action='in') }}" method="POST">
          {% for field in login_form %}
            {% if field.errors %}
              <ul>{% for error in field.errors %}
                <li>{{ error }}</li>
              {% endfor %}</ul>
            {% endif %}
              <p>{{ field.label }}: {{ field }}</p>
          {% endfor %}
          <p><input type="submit" name="Log In" value="Log In"/></p>
        </form></aside>
        {% endif %}
        {% if entries %}
        ...

.. nextslide:: Try It Out

We should be ready at this point.

.. rst-class:: build
.. container::

    Fire up your application and see it in action:

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 84467.
        serving on http://0.0.0.0:6543

    Load the home page and see your login form:

    * http://localhost:6543/
      
    Fill it in and submit the form, verify that you can add a new entry.

.. nextslide:: Break Time

That's enough for now.  We have a working application.

When we return, we'll deploy it.


Deploying An Application
========================

.. rst-class:: left
.. container::

    Now that we have a working application, our next step is to deploy it.

    .. rst-class:: build
    .. container::

        This will allow us to interact with the application in a live setting.

        We will be able to see the application from any computer, and can share
        it with friends and family.

        To do this, we'll be using one of the most popular platforms for
        deploying web applications today, `Heroku`_.

.. _Heroku: http://heroku.com

Heroku
------

.. figure:: /_static/heroku-logo.png
    :align: center
    :width: 40%

.. rst-class:: build
.. container::

    Heroku provides all the infrastructure needed to run many types of
    applications.

    It also provides `add-on services`_ that support everything from analytics
    to payment processing.

    Elaborate applications deployed on Heroku can be quite expensive.

    But for simple applications like our learning journal, the price is just
    right: **free**

.. _add-on services: https://addons.heroku.com

.. nextslide:: How Heroku Works

Heroku is predicated on interaction with a git repository.

.. rst-class:: build
.. container::

    You initialize a new Heroku app in a repository on your machine.

    This adds Heroku as a *remote* to your repository.

    When you are ready to deploy your application, you ``git push heroku
    master``.

    Adding a few special files to your repository allows Heroku to tell what
    kind of application you are creating.

    It responds to your push by running an appropriate build process and then
    starting your app with a command you provide.

Preparing to Run Your App
-------------------------

In order for Heroku to deploy your application, it has to have a command it can
run from a standard shell.

.. rst-class:: build
.. container::

    We could use the ``pserve`` command we've been using locally, but the
    server it uses is designed for development.

    It's not really suitable for a public deployment.

    Instead we'll use a more robust, production-ready server that came as one
    of our dependencies: `waitress`_.

    We'll start by creating a python file that can be executed to start the
    ``waitress`` server.

.. _waitress: http://waitress.readthedocs.org/en/latest/

.. nextslide:: Creating ``runapp.py``

At the very top level of your application project, in the same folder where you
find ``setup.py``, create a new file: ``runapp.py``

.. code-block:: python

    import os
    from paste.deploy import loadapp
    from waitress import serve

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app = loadapp('config:production.ini', relative_to='.')

        serve(app, host='0.0.0.0', port=port)

.. rst-class:: build
.. container::

    Once this exists, you can try running your app with it:

    .. code-block:: bash

        (ljenv)$ python runapp.py
        serving on http://0.0.0.0:5000

.. nextslide:: Running Via Shell

This would be enough, but we also want to *install* our application as a Python
package.

.. rst-class:: build
.. container::

    This will ensure that the dependencies for the application are installed.

    Add a new file called simply ``run`` in the same folder:

    .. code-block:: bash

        #!/bin/bash
        python setup.py develop
        python runapp.py

    The first line of this file will install our application and its
    dependencies.

    The second line will execute the server script.

.. nextslide:: Build the Database

We'll need to do the same thing for initializing the database.

.. rst-class:: build
.. container::

    Create another new file called ``build_db`` in the same folder:

    .. code-block:: bash

        #!/bin/bash
        python setup.py develop
        initialize_learning_journal_db production.ini

    Now, add ``run``, ``build_db`` and ``runapp.py`` to your repository and
    commit the changes.

.. nextslide:: Make it Executable

For Heroku to use them, ``run`` and ``build_db`` must be *executable*

.. rst-class:: build
.. container::

    For OSX and Linux users this is easy (do the same for ``run`` and
    ``build_db``):

    .. code-block:: bash

        (ljenv)$ chmod 755 run

    Windows users, if you have ``git-bash``, you can do the same

    For the rest of you, try this (for both ``run`` and ``build_db``):

    .. code-block:: posh

        C:\views\myproject>git ls-tree HEAD
        ...
        100644 blob 55c0287d4ef21f15b97eb1f107451b88b479bffe    run
        C:\views\myproject>git update-index --chmod=+x run
        C:\views\myproject>git ls-tree HEAD
        100755 blob 3689ebe2a18a1c8ec858cf531d8c0ec34c8405b4    run

    Commit your changes to git to make them permanent.


.. nextslide:: Procfile

Next, we have to inform Heroku that we will be using this script to run our
application online

.. rst-class:: build
.. container::

    Heroku uses a special file called ``Procfile`` to do this.

    Add that file now, in the same directory.

    .. code-block:: bash

        web: ./run

    This file tells Heroku that we have one ``web`` process to run, and that it
    is the ``run`` script located right here.

    Providing the ``./`` at the start of the file name allows the shell to
    execute scripts that are not on the system PATH.

    Add this new file to your repository and commit it.


.. nextslide:: Select a Python Version

By default, Heroku uses the latest update of Python version 2.7 for any Python
app.

.. rst-class:: build
.. container::

    You can override this and specify any runtime version of Python 
    `available in Heroku`_.
    
    Just add a file called ``runtime.txt`` to your repository, with one line
    only:

    .. code-block:: ini
    
        python-3.5.0

    Create that file, add it to your repository, and commit the changes.

.. _available in Heroku: https://devcenter.heroku.com/articles/python-runtimes#supported-python-runtimes


Set Up a Heroku App
-------------------

The next step is to create a new app with heroku.

.. rst-class:: build
.. container::

    You installed the Heroku toolbelt prior to class.

    The toolbelt provides a command to create a new app.

    From the root of your project (where the ``setup.py`` file is) run:

    .. code-block:: bash

        (ljenv)$ heroku create
        Creating rocky-atoll-9934... done, stack is cedar-14
        https://rocky-atoll-9934.herokuapp.com/ | https://git.heroku.com/rocky-atoll-9934.git
        Git remote heroku added

    Note that a new *remote* called ``heroku`` has been added:

    .. code-block:: bash

        $ git remote -v
        heroku  https://git.heroku.com/rocky-atoll-9934.git (fetch)
        heroku  https://git.heroku.com/rocky-atoll-9934.git (push)

.. nextslide:: Adding PostgreSQL

Your application will require a database, but ``sqlite`` is not really
appropriate for production.

.. rst-class:: build
.. container::

    For the deployed app, you'll use `PostgreSQL`_, the best open-source
    database.

    Heroku `provides an add-on`_ that supports PostgreSQL, and you'll need to
    set it up.

    Again, use the Heroku Toolbelt:

    .. code-block:: bash

        $ heroku addons:create heroku-postgresql:hobby-dev
        Creating postgresql-amorphous-6784... done, (free)
        Adding postgresql-amorphous-6784 to rocky-atoll-9934... done
        Setting DATABASE_URL and restarting rocky-atoll-9934... done, v3
        Database has been created and is available
         ! This database is empty. If upgrading, you can transfer
         ! data from another database with pg:copy
        Use `heroku addons:docs heroku-postgresql` to view documentation.

.. _PostgreSQL: http://www.postgresql.org
.. _provides an add-on: https://www.heroku.com/postgres

.. nextslide:: PostgreSQL Settings

You can get information about the status of your PostgreSQL service with the
toolbelt:

.. rst-class:: build
.. container::

    .. code-block:: bash

        (ljenv)$ heroku pg
        === DATABASE_URL
        Plan:        Hobby-dev
        ...
        Data Size:   6.4 MB
        Tables:      0
        Rows:        0/10000 (In compliance)

    And there is also information about the configuration for the database (and
    your app):

    .. code-block:: bash

        (ljenv)$ heroku config
        === rocky-atoll-9934 Config Vars
        DATABASE_URL:                 postgres://<username>:<password>@<domain>:<port>/<database-name>

Configuration for Heroku
------------------------

Notice that the configuration for our application on Heroku provides a specific
database URL.

.. rst-class:: build
.. container::

    We could copy this value and paste it into our ``production.ini``
    configuration file.

    But if we do that, then we will be storing that value in GitHub, where
    anyone at all can see it.

    That's not particularly secure.

    Luckily, Heroku provides configuration like the database URL in
    *environment variables* that we can read in Python.

    In fact, we've already done this with our ``runapp.py`` script:

    .. code-block:: python

        port = int(os.environ.get("PORT", 5000))

.. nextslide:: Adjusting Our DB Configuration

The Python standard library provides ``os.environ`` to allow access to
*environment variables* from Python code.

.. rst-class:: build
.. container::

    This attribute is a dictionary keyed by the name of the variable.

    We can use it to gain access to configuration provided by Heroku.

    Update ``learning_journal/__init__.py`` like so:

    .. code-block:: python

        # import the os module:
        import os
        # then look up the value we need for the database url
        def main(global_config, **settings):
            # ...
            if 'DATABASE_URL' in os.environ:
                settings['sqlalchemy.url'] = os.environ['DATABASE_URL']
            engine = engine_from_config(settings, 'sqlalchemy.')
            # ...

.. nextslide:: Adjust ``initializedb.py``

We'll need to make the same changes to
``learning_journal/scripts/initializedb.py``:

.. code-block:: python

    def main(argv=sys.argv):
        # ...
        settings = get_appsettings(config_uri, options=options)
        if 'DATABASE_URL' in os.environ:
            settings['sqlalchemy.url'] = os.environ['DATABASE_URL']
        engine = engine_from_config(settings, 'sqlalchemy.')
        # ...

.. nextslide:: Additional Security

This mechanism allows us to defer other sensitive values such as the password
for our initial user:

.. rst-class:: build
.. container::

    .. code-block:: python

        # in learning_journal/scripts/initializedb.py
        with transaction.manager:
            password = os.environ.get('ADMIN_PASSWORD', 'admin')
            encrypted = password_context.encrypt(password)
            admin = User(name=u'admin', password=encrypted)
            DBSession.add(admin)

    And for the secret value for our AuthTktAuthenticationPolicy

    .. code-block:: python

        # in learning_journal/__init__.py
        def main(global_config, **settings):
            # ...
            secret = os.environ.get('AUTH_SECRET', 'somesecret')
            ...
            authentication_policy=AuthTktAuthenticationPolicy(secret)
            # ...

.. nextslide:: Heroku Config

We will now be looking for three values from the OS environment:

.. rst-class:: build

* DATABASE_URL
* ADMIN_PASSWORD
* AUTH_SECRET

.. rst-class:: build
.. container::

    The ``DATABASE_URL`` value is set for us by the PosgreSQL add-on.

    But the other two are not.  We must set them ourselves using ``heroku
    config:set``:

    .. code-block:: bash

        (ljenv)$ heroku config:set ADMIN_PASSWORD=<your password>
        ...
        (ljenv)$ heroku config:set AUTH_SECRET=<a long random string>
        ...

.. nextslide:: Checking Configuration

You can see the values that you have set at any time using ``heroku config``:

.. code-block:: bash

    (ljenv)$ heroku config
    === rocky-atoll-9934 Config Vars
    ADMIN_PASSWORD:               <your password>
    AUTH_SECRET:                  <your auth secret value>
    DATABASE_URL:                 <your db URL>

.. rst-class:: build
.. container::

    These values are sent and received using secure transport.

    You do not need to worry about them being intercepted.

    This mechanism allows you to place important configuration values outside
    the code for your application.

.. nextslide:: Installing Dependencies

We've been handling our application's dependencies by adding them to
``setup.py``.

.. rst-class:: build
.. container::

    It's a good idea to install all of these before attempting to run our app.

    The ``pip`` package manager allows us to dump a list of the packages we've
    installed in a virtual environment using the ``freeze`` command:

    .. code-block:: bash
    
        (ljenv)$ pip freeze
        ...
        zope.interface==4.1.3
        zope.sqlalchemy==0.7.6

    We can tell heroku to install these dependencies by creating a file called
    ``requirements.txt`` at the root of our project repository:

    .. code-block:: bash
    
        (ljenv)$ pip freeze > requirements.txt

    Add this file to your repository and commit the changes.


.. nextslide:: Heroku-specific Dependencies

But there is also a new dependency we've added that is only needed for Heroku.

.. rst-class:: build
.. container::

    Because we are using a PostgreSQL database, we need to install the
    ``psycopg2`` package, which handles communicating with the database.

    We don't want to install this locally, though, where we use sqlite.

    Go ahead and add one more line to ``requirements.txt`` with the latest
    version of the ``pyscopg2`` package:

    .. code-block:: bash

        psycopg2==2.6.1

    Commit the change to your repository.

Deployment
----------

We are now ready to deploy our application.

.. rst-class:: build
.. container::

    All we need to do is push our repository to the ``heroku`` master:

    .. code-block:: bash

        (ljenv)$ git push heroku master
        ...
        remote: Building source:
        remote:
        remote: -----> Python app detected
        ...
        remote: Verifying deploy... done.
        To https://git.heroku.com/rocky-atoll-9934.git
           b59b7c3..54f7e4d  master -> master

.. nextslide:: Using ``heroku run``

You can use the ``run`` command to execute arbitrary commands in the Heroku
environment.

.. rst-class:: build
.. container::

    You can use this to initialize the database, using the shell script you
    created earlier:

    .. code-block:: bash

        (ljenv)$ heroku run ./build_db
        ...

    This will install our application and then run the database initialization
    script.

.. nextslide:: Test Your Results

At this point, you should be ready to view your application online.

.. rst-class:: build
.. container::

    Use the ``open`` command from heroku to open your website in a browser:

    .. code-block:: bash

        (ljenv)$ heroku open

    If you don't see your application, check to see if it is running:

    .. code-block:: bash

        (ljenv)$ heroku ps
        === web (1X): `./run`
        web.1: up 2015/01/18 16:44:37 (~ 31m ago)

    If you get no results, use the ``scale`` command to try turning on a web
    *dyno*:

    .. code-block:: bash

        (ljenv)$ heroku scale web=1
        Scaling dynos... done, now running web at 1:1X.

.. nextslide:: A Word About Scaling

Heroku pricing is dependent on the number of *dynos* you are running.

.. rst-class:: build
.. container::

    So long as you only run one dyno per application, you will remain in the
    free tier.

    Scaling above one dyno will begin to incur costs.

    **Pay attention to the number of dynos you have running**.

.. nextslide:: Troubleshooting

Troubleshooting problems with Heroku deployment can be challenging.

.. rst-class:: build
.. container::

    Your most powerful tool is the ``logs`` command:

    .. code-block:: bash

        (ljenv)$ heroku logs
        ...
        2015-01-19T01:17:59.443720+00:00 app[web.1]: serving on http://0.0.0.0:53843
        2015-01-19T01:17:59.505003+00:00 heroku[web.1]: State changed from starting to update

    This command will print the last 50 or so lines of logging from your
    application.

    You can use the ``-t`` flag to *tail* the logs.

    This will continually update log entries to your terminal as you interact
    with the application.

.. nextslide:: Revel In Your Glory

Try logging in to your application with the password you set up in Heroku
configuration.

.. rst-class:: build
.. container::

    Once you are logged in, try adding an entry or two.

    You are now off to the races!

    .. rst-class:: center

    **Congratulations**

Adding Polish
=============

.. rst-class:: left
.. container::

    So we have now deployed a running application.

    .. rst-class:: build
    .. container::

        But there are a number of things we can do to make the application
        better.

        Let's start by adding a way to log out.


Adding Logout
-------------

Our ``login`` view is already set up to work for logout.

.. rst-class:: build
.. container::

    What is the logical path taken if that view is accessed via ``GET``?

    All we need to do is add a view_config that allows that.

    Open ``learning_journal/views.py`` and make these changes:

    .. code-block:: python

        @view_config(route_name='auth', match_param='action=in', renderer='string',
                 request_method='POST') # <-- THIS IS ALREADY THERE
        # ADD THE FOLLOWING LINE
        @view_config(route_name='auth', match_param='action=out', renderer='string')
        # UPDATE THE VIEW FUNCTION NAME
        def sign_in_out(request):
            # ...

.. nextslide:: Re-Deploy

The chief advantage of Heroku is that we can re-deploy with a single command.

.. rst-class:: build
.. container::

    Add and commit your changes to git.

    Then re-deploy by pushing to the ``heroku master``:

    .. code-block:: bash

        (ljenv)$ git push heroku master

    Once that completes, you should be able to reload your application in the
    browser.

    Visit the following URL path to test log out:

    * /sign/out

Hide UI for Anonymous
---------------------

Another improvement we can make is to hide UI that is not available for users
who are not logged in.

.. rst-class:: build
.. container::

    The first step is to update our ``detail`` view to tell us if someone is
    logged in:

    .. code-block:: python

        # learning_journal/views.py
        @view_config(route_name='detail', renderer='templates/detail.jinja2')
        def view(request):
            # ...
            logged_in = authenticated_userid(request)
            return {'entry': entry, 'logged_in': logged_in}

    The ``authenticated_userid`` function returns the id of the logged in user,
    if there is one, and ``None`` if there is not.

    We can use that.

.. nextslide:: Hide "Create Entry" UI

First we can hide the UI for creating a new entry:

.. rst-class:: build
.. container::

    Edit ``templates/list.jinja2``:

    .. code-block:: jinja

        {% extends "layout.jinja2" %}
        {% block body %}
        <!-- ... ADD THE IF TAGS BELOW -->
        {% if not login_form %}
        <p><a href="{{ request.route_url('action', action='create') }}">New Entry</a></p>
        {% endif %}
        {% endblock %}

    This relies on the fact that the login form will only be present if there
    is **not** an authenticated user.

.. nextslide:: Hide "Edit Entry" UI

Next, we can hide the UI for editing an existing entry:

.. rst-class:: build
.. container::

    Edit ``templates/detail.jinja2``:

    .. code-block:: jinja

        {% extends "layout.jinja2" %}
        {% block body %}
        <!-- ... WRAP THE EDIT LINK -->
        <p>
          <a href="{{ request.route_url('home') }}">Go Back</a>
          {% if logged_in %}
          ::
          <a href="{{ request.route_url('action', action='edit', _query=(('id',entry.id),)) }}">
            Edit Entry</a>
          {% endif %}
        </p>
        {% endblock %}

Format Entries
--------------

It would be nice if our journal entries could have HTML formatting.

.. rst-class:: build
.. container::

    We could write HTML by hand in the body field, but that'd be a pain.

    Instead, let's allow ourselves to write entries `in Markdown`_, a popular
    markup syntax used by GitHub and many other websites.

    .. _in Markdown: http://daringfireball.net/projects/markdown/syntax

    Python provides several libraries that implement markdown formatting.

    They will take text that contains markdown formatting and convert it to
    HTML.

    Let's use one.

.. nextslide:: Adding the Dependency

The first step, is to pick a package and add it to our dependencies.

.. rst-class:: build
.. container::

    My recommendation is the `markdown`_ python library.

    Open ``setup.py`` and add the package to the ``requires`` list:

    .. code-block:: python

        requires = [
            # ...
            'cryptacular',
            'markdown', # <-- ADD THIS
            ]

    We'll test this locally first, so go ahead and re-install your app:

    .. code-block:: bash

        (ljenv)$ python setup.py develop
        ...
        Finished processing dependencies for learning-journal==0.0

.. _markdown: https://pythonhosted.org/Markdown/

.. nextslide:: Jinja2 Filters

We've seen before how Jinja2 provides a number of filters for values when
rendering templates.

.. rst-class:: build
.. container::

    A nice feature of the templating language is that it also allows you to
    `create your own filters`_.

    Remember the template syntax for a filter:

    .. code-block:: jinja

        {{ value|filter(arg1, ..., argN) }}

    A filter is simply a function that takes the value to the left of the ``|``
    character as a first argument, and any supplied arguments as the second and
    beyond:

    .. code-block:: python

        def filter(value, arg1, ..., argN):
            # do something to value here

.. _create your own filters: http://jinja.pocoo.org/docs/dev/api/#custom-filters

.. nextslide:: Our Markdown Filter

Creating a ``markdown`` filter will allow us to convert plain text stored in
the database to HTML at template rendering time.

.. rst-class:: build
.. container::

    Open ``learning_journal/views.py`` and add the following:

    .. code-block:: python

        # add two imports:
        from jinja2 import Markup
        import markdown
        # and a function
        def render_markdown(content):
            output = Markup(markdown.markdown(content))
            return output

    The ``Markup`` class from jinja2 marks a string with HTML tags as "safe".

    This prevents the tags from being *escaped* when they are rendered into a
    page.

.. nextslide:: Register the Filter

In order for ``Jinja2`` to be aware that our filter exists, we need to register
it.

.. rst-class:: build
.. container::

    In Pyramid, we do this in configuration.

    Open ``development.ini`` and edit it as follows:

    .. code-block:: ini

        [app:main]
        ...
        jinja2.filters =
            markdown = learning_journal.views.render_markdown

    This informs the main app that we wish to register a jinja2 filter.

    We will call it ``markdown`` and it will be embodied by the function we
    just wrote.

.. nextslide:: Use Your Filter

To see the results of our work, we'll need to use the filter in a template
somewhere.

.. rst-class:: build
.. container::

    I suggest using it in the ``learning_journal/templates/detail.jinja2``
    template:

    .. code-block:: jinja

        {% extends "layout.jinja2" %}
        {% block body %}
        <article>
          <!-- EDIT THIS LINE -->
          <p>{{ entry.body|markdown }}</p>
          <!-- -->
        </article>
        <p>
        <!-- -->
        {% endblock %}

.. nextslide:: Test Your Results

Start up your application, and create an entry using valid markdown formatting:

.. code-block:: bash

    (ljenv)$ pserve development.ini
    Starting server in PID 84331.
    serving on http://0.0.0.0:6543

.. rst-class:: build
.. container::

    Once you save your entry, you should be able to see it with actual
    formatting: headers, bulleted lists, links, and so on.

    That makes quite a difference.

    Go ahead and add the same filter registration to ``production.ini``

    Then commit your changes and redeploy:

    .. code-block:: bash

        (ljenv)$ git push heroku master


Syntax Highlighting
-------------------

The purpose of this journal is to allow you to write entries about the things
you learn in this class and elsewhere.

.. rst-class:: build
.. container::

    Markdown formatting allows for "preformatted" blocks of text like code
    samples.

    But there is nothing in markdown that handles *colorizing* code.

    Luckily, the markdown package allows for extensions, and one of these
    supports `colorization`_.

    It requires the `pygments`_ library

    Let's set this up next.

.. _colorization: https://pythonhosted.org/Markdown/extensions/code_hilite.html
.. _pygments: http://pygments.org

.. nextslide:: Install the Dependency

Again, we need to install our new dependency first.

.. rst-class:: build
.. container::

    Add the following to ``requires`` in ``setup.py``:

    .. code-block:: python

        requires = [
            # ...
            'markdown',
            'pygments', # <-- ADD THIS LINE
            ]

    Then re-install your app to pick up the software:

    .. code-block:: bash

        (ljenv)$ python setup.py develop
        ...
        Finished processing dependencies for learning-journal==0.0

.. nextslide:: Add to Our Filter

The next step is to extend our markdown filter in ``learning_journal/views.py``
with this feature.

.. rst-class:: build
.. container::

    .. code-block:: python

        def render_markdown(content):
            output = Markup(
                markdown.markdown(
                    content,
                    extensions=['codehilite(pygments_style=colorful)', 'fenced_code']
                )
            )
            return output

    Now, you'll be able to make highlighted code blocks just like in GitHub:

    .. code-block:: text

        ```python
        def foo(x, y):
            return x**y
        ```

.. nextslide:: Add CSS

Code highlighting works by putting HTML ``<span>`` tags with special CSS
classes around bits of your code.

.. rst-class:: build
.. container::

    We need to generate and add the css to support this.

    You can use the ``pygmentize`` command from pygments to
    `generate the css`_.

    Make sure you are in the directory with ``setup.py`` when you run this:

    .. code-block:: bash
    
        (ljenv)$ pygmentize -f html -S colorful -a .codehilite \
             >> learning_journal/static/styles.css

    The styles will be printed to standard out.

    The ``>>`` shell operator *appends* the output to the file named.

.. _generate the css: http://pygments.org/docs/cmdline/#generating-styles

.. nextslide::  Try It Out

Go ahead and restart your application and see the difference a little style
makes:

.. code-block:: bash

    (ljenv)$ pserve development.ini
    Starting server in PID 84331.
    serving on http://0.0.0.0:6543

.. rst-class:: build
.. container::

    Try writing an entry with a little Python code in it.

    Python is not the only language available.

    Any syntax covered by `pygments lexers`_ is available, just use the
    *shortname* from a lexer to get that type of style highlighting.

.. _pygments lexers: http://pygments.org/docs/lexers/

.. nextslide:: Deploy Your Changes

When you've got this working as you wish, go ahead and deploy it.

.. rst-class:: build
.. container::

    Add and commit all the changes you've made.

    Then push your results to the ``heroku master``:

    .. code-block:: bash
    
        (ljenv)$ git push heroku master

Homework
========

.. rst-class:: left
.. container::

    That's just about enough for now.

    .. rst-class:: build
    .. container::

        There's no homework for you to submit this week. You've worked hard enough.

        Take the week to review what we've done and make sure you have a solid
        understanding of it.

        If you wish, play with HTML and CSS to make your journal more personalized.

        However, in preparation for our work with Django next week, I'd like you to
        get started a bit ahead of time.

        Please read and follow along with this `basic intro to Django`_.

        .. rst-class:: centered

        **See You Then**

.. _basic intro to Django: django_intro.html
