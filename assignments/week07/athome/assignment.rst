Week 7 Assignment Instructions
==============================

Prep
----

For this week, you have *no* code assignment. 

Instead I want you to focus on installing software and reading for next week.
Software we'll be installing uses C extensions, and so installing it on OS X
or Linux requires a compiler and python's development headers.

**Ubuntu** (our vms):

    $ sudo apt-get install python-dev

**OS X**: Ensure that you have XCode installed. It's free, but *big* expect it
to take a while if you don't already have it.

**Windows**: You all are safe for the time being.

Virtualenv
----------

With that prep work out of the way, you're ready to start. First, set up a
virtualenv:

    $ python2.6 virtualenv.py --distribute pyramidenv
    ...
    $ source pyramidenv/bin/activate
    (pyramidenv)$ 

Remeber, Windows users: ``> pyramidenv\Scripts\activate``

Install Pyramid
---------------

Once you've got a virtualenv set up and ready to go, install Pyramid:

    (pyramidenv)$ easy_install pyramid

This will install a number of dependency packages, do not be alarmed.

Next, we'll install a different kind of Database, the ZODB.

Install ZODB
------------

If you're on OS X or Linux:

    (pyramidenv)$ easy_install ZODB3==3.10.5

This will take some time. If you get errors, contact me directly or via the
Google Group.

Windows users, you'll have it a bit easier here. You have to install a binary
egg:

    [pyramidenv]> pip install --egg ZODB3==3.10.5

Pause for Self Evaluation
-------------------------

At this point, you can check your work. Fire up a python interpreter in your
virtualenv:

    (pyramidenv)$ python
    >>> import ZODB
    >>> ^D
    (pyramidenv)$

If you get an ImportError when you try that, you're not done.  Contact me.

Extras
------

Next, we'll need to finish installing the bits we need for our work next
week:

    (pyramidenv)$ easy_install docutils nose coverage
    ...
    (pyramidenv)$ easy_install pyramid_zodbconn pyramid_tm
    ...
    (pyramidenv)$ easy_install pyramid_debugtoolbar

These tools will allow us to manage ZODB connections, debug our app, and run
cool tests.

Set Up Project
--------------

And finally, we'll set up a project for ourselves. This is like running
'startproject' for django in a way:

    (pyramidenv)$ pcreate -s zodb wikitutorial

Do not be alarmed by the 'sorry for the convenience' message.

You get a folder called ``wikitutorial``. In it you should see files like
``setup.py`` and ``development.ini`` among others.

This is an installable ``package``. You can install this package with
easy_install.

Final Self Evaluation
---------------------

In fact, let's do that now, so we can prove to ourselves this all worked:

    (pyramidenv)$ cd wikitutorial
    (pyramidenv)$ python setup.py develop
    ...

You'll see a bunch of output.  When it's over, run tests:

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

