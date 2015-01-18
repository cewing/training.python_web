**********
Session 03
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

`View this online <https://github.com/cewing/training.python_web/blob/5e02f6f84322145433c515c191679ccf976dcae4/resources/session03/forms.py#L25>`_

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

`View this online <https://github.com/cewing/training.python_web/blob/5e02f6f84322145433c515c191679ccf976dcae4/resources/session03/views.py#L43>`_

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


`View this online <https://github.com/cewing/training.python_web/blob/9e1c9db3a379d1d63371cffddaf8e63f862872c8/resources/session03/detail.jinja2#L12>`_

.. nextslide:: A Working User Model

.. code-block:: python

    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(Unicode(255), unique=True, nullable=False)
        password = Column(Unicode(255), nullable=False)

        @classmethod
        def by_name(cls, name):
            return DBSession.query(User).filter(User.name == name).first()

`View this online <https://github.com/cewing/training.python_web/blob/5e02f6f84322145433c515c191679ccf976dcae4/resources/session03/models.py#L62>`_

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

.. _authentication: http://docs.pylonsproject.org/docs/pyramid/en/latest/api/interfaces.html#pyramid.interfaces.IAuthenticationPolicy
.. _authorization: http://docs.pylonsproject.org/docs/pyramid/en/latest/api/interfaces.html#pyramid.interfaces.IAuthorizationPolicy

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

    We've told it that by default we want a principal to have the 'view'
    permission to see anything.

    Let's verify that this worked.

    Start your application, and try to view any page (You should get 403
    Forbidden):

    .. code-block:: bash

        (ljenv)$ pserve development.ini
        Starting server in PID 84467.
        serving on http://0.0.0.0:6543

    .. rst-class:: build

    * http://localhost:6543/
    * http://localhost:6543/journal/1
    * http://localhost:6543/journal/create
    * http://localhost:6543/journal/edit

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
    * http://localhost:6543/journal/edit

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

    We'll use a good one called `Cryptacular`_.

    This library provides a number of different algorithms and a *Manager* that
    implements a simple interface for each.

    .. code-block:: python

        from cryptacular.bcrypt import BCRYPTPasswordManager
        manager = BCRYPTPasswordManager()
        hashed = manager.encode('password')
        if manager.check(hashed, 'password'):
            print "It matched"

.. _Cryptacular: https://pypi.python.org/pypi/cryptacular/

.. nextslide:: Install Cryptactular

To install a new package as a dependency, we add the package to our list in
``setup.py``:

.. rst-class:: build
.. container::

    .. code-block:: python

        requires = [
          ...
          'wtforms',
          'cryptacular',
        ]

    Then, we re-install our package to pick up the new dependency:

    .. code-block:: bash

        (ljenv)$ python setup.py develop

    *note* if you have a c compiler installed but not the Python dev headers,
    this may not work.  Let me know if you get errors.

.. nextslide:: Comparing Passwords

The job of comparing passwords should belong to the ``User`` object.

.. rst-class:: build
.. container::

    Let's add an instance method that handles it for us.

    Open ``learning_journal/models.py`` and add the following to the ``User``
    class:

    .. code-block:: python

        # add this import at the top
        # from cryptacular.pbkdf2 import PBKDF2PassordManager as Manager
        from cryptacular.bcrypt import BCRYPTPasswordManager as Manager

        # add this method to the User class:
        class User(Base):
            # ...
            def verify_password(self, password):
                manager = Manager()
                return manager.check(self.password, password)

.. nextslide:: Create a User

We'll also need to have a user for our system.

.. rst-class:: build
.. container::

    We can leverage the database initialization script to handle this.

    Open ``learning_journal/scripts/initialzedb.py``:

    .. code-block:: python

        # add the import
        # from cryptacular.pbkdf2 import PBKDF2PassordManager as Manager
        from cryptacular.bcrypt import BCRYPTPasswordManager as Manager
        from ..models import User
        # and update the main function like so:
        def main(argv=sys.argv):
            # ...
            with transaction.manager:
                # replace the code to create a MyModel instance
                manager = Manager()
                password = manager.encode(u'admin')
                admin = User(name=u'admin', password=password)
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
          (u'admin', '$2a$10$4Z6RVNhTE21mPLJW5VeiVe0EG57gN/HOb7V7GUwIr4n1vE.wTTTzy')

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


.. nextslide:: Login View

We'll use that form in a view to log in (in ``learning_journal/views.py``):

.. rst-class:: build
.. container::

    .. code-block:: python

        # a new imports:
        from pyramid.security import remember
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
            return HTTPFound(location=request.route_url('home'),
                             headers=headers)

.. nextslide:: Where's the form?

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

Now we have to update our template to display the form, *if it is there*

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
        {% else %}
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

.. nextslide:: Running Your App

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

    That allows us to use the database initialization script we've created.

    Add a new file called simply ``run`` in the same folder:

    .. code-block:: bash
    
        #!/bin/bash
        python setup.py develop
        python runapp.py

    The first line of this file will install our application and verify its
    dependencies.

    The second line will execute the server script.

    Now, add these two new files to your repository and commit them.

.. nextslide:: Make it Executable

In order for this file to run, it needs to be *executable*

.. rst-class:: build
.. container::

    For OSX and Linux users this is easy:

    .. code-block:: bash
    
        (ljenv)$ chmod 755 run

    Windows users, if you have ``git-bash``, you can do the same

    For the rest of you, try this:

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



outline
-------

set up heroku app for this application

install postgresql plugin

Show how you can get DB url from config and environment,

Note how python has os.environ to allow us to access environment variables

alter __init__.py to use this to set up the database url (and initializedb as well)

Note how we can use the the environment for other special values too:

* administrator password
* authentication policy secret

Update app to use those as well

git push heroku master

git run initialize_learning_journal_db heroku.ini

heroku logs


add logout??

Adding Polish
=============

Markdown for posts so you can create a formatted entry

add markdown package, pygments package

pygmentize -f html -S colorful -a .syntax

create jinja2 filter

add filter to configuration (.ini file or in __init__.py)




