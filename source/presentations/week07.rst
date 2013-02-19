Internet Programming with Python
================================

.. image:: img/django-pony.png
    :align: left
    :width: 50%

Week 7: Django - Part 2

.. class:: intro-blurb right

Wherein we extend Django's built-in features

.. class:: image-credit

image: http://djangopony.com/

But First
---------

.. class:: big-centered

Questions from the Reading?

And Second
----------

A reminder of our task for today:

.. class:: incremental

Extend a basic micro-blog application with one of the following features:

.. class:: incremental

* User Registration
* 'Archive' views based on date or author
* WYSIWYG visual editor for entry posts.
* Tagging
* Theme (make it beautiful)

Your Teams
----------

**Team 1**:

.. class:: incremental

**Leader**: Jon B

.. class:: incremental

**Members**: Tyler, Matt K, John C, Wilson, Divesh

.. class:: incremental

**Your Task**: User Registration with ``django-registration``

Your Teams
----------

**Team 2**:

.. class:: incremental

**Leader**: Matt O

.. class:: incremental

**Members**: David, Pho, Phil, Chris

.. class:: incremental

**Your Task**: Archive Views using Generic date-based views

Your Teams
----------

**Team 3**:

.. class:: incremental

**Leader**: Austin

.. class:: incremental

**Members**:  Edet, Eric, Allan

.. class:: incremental

**Your Task**: Content Tagging with ``django-taggit``

Your Teams
----------

**Team 4**:

.. class:: incremental

**Leader**: Jason

.. class:: incremental

**Members**:  Daniel, Conor, Maria

.. class:: incremental

**Your Task**: WYSIWYG Editing with ``django-ckeditor``

My Guidelines
-------------

Each team can work from a single *core* repository.

.. class:: incremental

Break the job into discreet tasks.

.. class:: incremental

Work in twos or threes, each small group take a task and complete it.

.. class:: incremental

Create a local branch. Complete your task then merge.

.. class:: incremental

Team leaders manage communications, keep an eye on the big picture.

First Step - Setup
------------------

Get a 'core' repository (perhaps leaders fork mine)::

    https://github.com/cewing/training.django_microblog

.. class:: incremental

Add your teammates as **collaborators**:

.. class:: incremental

* In your browser, view the repo you'll be working from in github.
* Click on the 'settings' tab (in the grey bar below the repo name)
* Click on the 'collaborators' menu item on the left
* Add your teammates by github id to the list of collaborators

.. class:: incremental

Now you should **all** have read-write access to this *core* repo.

Second Step - Workflow
----------------------

Each small group, pick a *driver*

.. class:: incremental

Each driver, clone the *core* repo to your local machine

.. class:: incremental

Pick a task. **Before** you start to work, make a local branch:

.. class:: incremental

::

    $ git checkout -b <task_name>

.. class:: incremental

Complete your task, making commits as you go (you're on a branch)

Third Step - Cleanup
--------------------

When you're finished with a task, you'll merge your branch:

.. class:: incremental small

::

    $ git branch
      master
    * <task_name>
    $ git checkout master
    Switched to branch 'master'
    $ git pull origin master
    From ...
     * branch            master     -> FETCH_HEAD
    Already up-to-date.
    $ git merge <task_name>
    $ git push origin master

.. class:: incremental

Rinse and repeat

In The End
----------

Leaders, make a copy of the *core* repository on your machine

.. class:: incremental

When your team is done, set up your machine to show off your results

.. class:: incremental

At 8:30 we'll come together. Each team will have 5 minutes to show a quick
demo of their work, and say something about what they learned along the way.

Almost There
------------

.. class:: big-centered

Any Questions?

And Now
-------

.. class:: big-centered

**begin**

Reference
---------

A Few useful git commands:

.. class:: small

::

    $ git clone <repo_url>          # make a clone
    $ git checkout -b <branch_name> # make a new local branch
    $ git checkout master           # return to the master
    $ git branch                    # list branches (and show current)
    $ git commit -m "message"       # make a commit locally
    $ git pull [origin [branch]]    # pull recent changes from remote
    $ git push [origin [branch]]    # push committed changes to remote
    $ git merge <branch_name>       # merge changes from other to current

Assignment - Prep
-----------------

.. class:: small

For this week, you have *no* code assignment. 

.. class:: small

Instead I want you to focus on installing software and reading for next week.
Software we'll be installing uses C extensions, and so installing it on OS X
or Linux requires a compiler and python's development headers.

.. class:: small

**Ubuntu** (our vms):

.. class:: small

::

    $ sudo apt-get install python-dev

.. class:: small

**OS X**: Ensure that you have XCode installed. It's free, but *big* expect it
to take a while if you don't already have it.

.. class:: small

**Windows**: You all are safe for the time being.

Assignment - Virtualenv
-----------------------

With that prep work out of the way, you're ready to start. First, set up a
virtualenv:

.. class:: incremental

::

    $ python2.6 virtualenv.py --distribute pyramidenv
    ...
    $ source pyramidenv/bin/activate
    (pyramidenv)$ 

.. class:: incremental

Remeber, Windows users: ``> pyramidenv\Scripts\activate``

Assignment - Install Pyramid
----------------------------

Once you've got a virtualenv set up and ready to go, install Pyramid:

.. class:: incremental

::

    (pyramidenv)$ easy_install pyramid

.. class:: incremental

This will install a number of dependency packages, do not be alarmed.

.. class:: incremental

Next, we'll install a different kind of Database, the ZODB.

Assignment - Install ZODB
-------------------------

If you're on OS X or Linux::

    (pyramidenv)$ easy_install ZODB3==3.10.5

This will take some time. If you get errors, contact me directly or via the
Google Group.

Windows users, you'll have it a bit easier here. You have to install a binary
egg::

    [pyramidenv]> pip install --egg ZODB3==3.10.5

Pause for Self Evaluation
-------------------------

At this point, you can check your work. Fire up a python interpreter in your
virtualenv::

    (pyramidenv)$ python
    >>> import ZODB
    >>> ^D
    (pyramidenv)$

If you get an ImportError when you try that, you're not done.  Contact me.

Assignment - Extras
-------------------

Next, we'll need to finish installing the bits we need for our work next
week::

    (pyramidenv)$ easy_install docutils nose coverage
    ...
    (pyramidenv)$ easy_install pyramid_zodbconn pyramid_tm
    ...
    (pyramidenv)$ easy_install pyramid_debugtoolbar

.. class:: incremental

These tools will allow us to manage ZODB connections, debug our app, and run
cool tests.

Assignment - Set Up Project
---------------------------

And finally, we'll set up a project for ourselves. This is like running
'startproject' for django in a way:

.. class:: incremental small

    (pyramidenv)$ pcreate -s zodb wikitutorial

.. class:: incremental small center

Do not be alarmed by the 'sorry for the convenience' message.

.. class:: incremental

You get a folder called ``wikitutorial``. In it you should see files like
``setup.py`` and ``development.ini`` among others.

.. class:: incremental

This is an installable ``package``. You can install this package with
easy_install.

Final Self Evaluation
---------------------

In fact, let's do that now, so we can prove to ourselves this all worked::

    (pyramidenv)$ cd wikitutorial
    (pyramidenv)$ python setup.py develop
    ...

.. class:: incremental

You'll see a bunch of output.  When it's over, run tests:

.. class:: incremental

::

    (pyramidenv)$ python setup.py test -q
    
Congratulations
---------------

When you've made it this far, and you see 1 test run successfully, you're
done.

If you like, you can see your work by running the new project::

    (pyramidenv)$ pserve development.ini
    Starting server in PID 3056.
    serving on http://0.0.0.0:6543

Visit ``http://localhost:6543`` to see your work in action. then go grab a
beer and curl up with the reading for the week. There's a lot.
