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

Pyramid Views
=============

.. rst-class:: left
.. container::

    Let's go back to thinking for a bit about the *Model-View-Controller*
    pattern.

    .. rst-class:: build
    .. container::
    
        .. figure:: http://upload.wikimedia.org/wikipedia/commons/4/40/MVC_passive_view.png
            :align: center
            :width: 25%

            By Alan Evangelista (Own work) [CC0], via Wikimedia Commons

        We talked last week (and today) about the *model*

outline
-------

views are "controllers"

requests come in with user input, data sent out

views are connected to the outside world via "routes" and these determine URLs

see how it works for the current MyModel and my_view

add route to config tells the application which urls will work
  try urls that are not in config, see what happens

view_config tells the view what renderer to use, which route to connect to, and
can help discriminate between views that share the same route

renderers are the "view" in mvc

our data model is the program's api for our application

Think of routes as the user API for the application, it determines what the
user can do.

Add routes for our application, what do we need to be able to do?

Add stub views for our application, we can see our routes, and can tell when
we've succeeded in getting past them.

Test the application routes

Create a view to view all entries

create a view to view one entry by id

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



