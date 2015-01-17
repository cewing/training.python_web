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

.. code-block:: jinja

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

Introduce authn/authz


Discuss authz

Discuss ACLs

Create a 'factory' for our action views

prove that the edit/create buttons now return "403 Forbidden"


Introduce Authentication

Discuss methods for proving who you are, username/password combination

Passwords and encryption

How Cryptacular works

Adding encryption to our application

Update initializedb so that it creates a user, stores it with an enrypted
password

Add api instance method to user that will verify a password

Add routes for login/logout actions

Add login/logout views


Start app and login/logout


Deploying An Application
========================

A bit about how heroku works

running the application

Create a runapp.py (use it locally from python to demonstrate)

add a shell script that will install and then run the app using the above script

Create a Procfile

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

Adding Polish
=============

Markdown for posts so you can create a formatted entry

add markdown package, pygments package

pygmentize -f html -S colorful -a .syntax

create jinja2 filter

add filter to configuration (.ini file or in __init__.py)




