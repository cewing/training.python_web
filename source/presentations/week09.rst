Internet Programming with Python
================================

.. image:: img/cloud_cover.jpg
    :align: left
    :width: 50%

Week 9: The Cloud

.. class:: intro-blurb right

| Every cloud has its silver lining 
| but it is sometimes a little difficult 
| to get it to the mint.
| --Don Marquis


.. class:: image-credit

image: mnsc http://www.flickr.com/photos/mnsc/2768391365/ - CC-BY

Deployment
----------

You've built your app, tested it, now it's time to *go live*

.. class:: incremental

What are your options?

.. class:: incremental center

**It Depends**

The Traditional Way
--------------------

In the old days™ you had one option

.. class:: incremental

Buy a server, build it and host it yourself

.. class:: incremental

You have total control

.. class:: incremental small

* buy exactly the hardware you want
* run only the services you need

.. class:: incremental

You *also* have total responsibility

.. class:: incremental small

* when something breaks, you have to fix it
* you bear *all* the costs yourself

Traditional Drawbacks
---------------------

Expensive

.. class:: incremental

* Server-class hardware $2k-$10k or more
* Systems Administrator $90K/year

.. class:: incremental

Inefficient

.. class:: incremental

* Most web sites don't get enough traffic to tax a good server
* Web traffic tends to be assymetrical
* Systems administration tasks also highly assymetrical

.. class:: incremental

A problem of resource utilization

The First Solution
------------------

VPS (*Virtual Private Server*)

.. class:: incremental

A part of a server (or perhaps an entire server) purchased from a provider.

.. class:: incremental

You pay for only a portion of a server and a portion of a systems
administrator.

.. class:: incremental

You retain control of the system

.. class:: incremental

You also retain responsibility for everything above the bare iron.

VPS Outcomes
------------

Benefits

.. class:: incremental

* Reduced cost ($30-$100+/month vs server and salary)
* Reduced burden (The provider handles hardware upkeep and low-level
  maintenance)
* Retain control of your full software stack

.. class:: incremental

Drawbacks

.. class:: incremental

* You install and maintain the web stack (requires knowledge)
* You lose control over resource utilization
* Your resources are still fixed (always the same size)

The Second Solution
-------------------

Shared Hosting

.. class:: incremental

You pay a provider to set you up with a [django/flask/pyramid/etc.] system.

.. class:: incremental

Hardware and most software maintenance is provided

.. class:: incremental

You are able to install some (but perhaps not all) add-ons

.. class:: incremental

This solution is very popular in the PHP world

.. class:: incremental

Much less so with Python.  Why?...

Shared Hosting Outcomes
-----------------------

Benefits

.. class:: incremental

* Enormously less expensive ($5-$15+/month)
* Much lower maintenance burden
* Simplified installation process

.. class:: incremental

Drawbacks

.. class:: incremental

* Tight resource restrictions (cpu, ram, disk space)
* Little to no control over most of the stack
* Reduced availability of some frameworks or packages

.. class:: incremental

And still, no ability to grow if you need

The Third Solution
------------------

.. class:: big-centered incremental

**The Cloud**

.. class:: incremental center small

(*cue fanfare*)

The Cloud Concept
-----------------

You don't know today what you will need tomorrow

.. class:: incremental

Today your website is getting 100-500 unique visitors

.. class:: incremental

Tomorrow you might have 10,000, 100,000.  Who knows?

.. class:: incremental

Should you have to buy enough hardware to handle that traffic today?

.. class:: incremental

Cloud computing offers rapid deployment solutions so you can scale at will

What is 'the Cloud'?
--------------------

Really, it differs from place to place.

.. class:: incremental

Some are more do-it-yourself (Amazon EC2, Rackspace Cloud)

.. class:: incremental

Some are more automated (Heroku, Elastic Beanstalk, AppEngine)

.. class:: incremental

All try to abstract common deployment tasks to make it easy to repeat

.. class:: incremental

So, how does that work?

Fabric
------

Fabric is *not* a cloud service. Instead, it's a tool built to help developers
simplify the process of deploying complex apps to a server.

.. class:: incremental

It can be used in any setup where you have ``ssh`` access to the filesystem
of the remote server.  

.. class:: incremental

Your classmate Austin used it a couple of weeks back to deploy Django to his
bluebox VM.

.. class:: incremental

Today, he's going to share that experience with you...

Heroku
------

.. image:: img/heroku-logo.png
    :align: center
    :width: 50%

.. class:: incremental center

I tried a number of cloud providers

.. class:: incremental center

This was hands-down the easiest.

Heroku - Sign-up
----------------

You'll need a Heroku account to do anything, so the first step is to get that

.. class:: incremental

Go to http://www.heroku.com

.. class:: incremental

Click on 'Sign Up' and enter your email address

.. class:: incremental

When the email arrives, click the link and create your password

.. class:: incremental

Once you've signed up, you'll see your 'dashboard' page with tips on getting
started.

Heroku - Setup
--------------

Like pretty much all the 'cloud' providers out there, Heroku has some
command-line tools you need to use.

.. class:: incremental

You can find them at https://toolbelt.heroku.com/

.. class:: incremental

Download and install the package, and then login:

.. class:: incremental

::

    $ heroku login
    Email: your-email@your.domain.com
    Password: <fill it in>

.. class:: incremental

The tool will find, or help you create, an ssh public key

Heroku - Branch my App
----------------------

As an exercise, I decided to deploy the *djangor* micro-blog app we created in
class.

.. class:: incremental

The first step was to clone the app, then create a local branch for deployment:

.. class:: incremental small

::

    $ mkdir heroku-test
    $ cd heroku-test
    $ git clone git@github.com:cewing/training.django_microblog.git
    ...
    $ cd training.django_microblog
    $ git checkout -b heroku-deploy
    Switched to a new branch 'heroku-deploy'
    $

Heroku - Setup Virtualenv
-------------------------

Again, like many cloud providers Heroku uses virtualenvs to ensure it's
installed correctly

.. class:: incremental

I set up a python 2.7 virtualenv right in my git repository:

.. class:: incremental small

::

    $ ~/pythons/bin/virtualenv-2.7 --distribute venv
    ...
    $ source venv/bin/activate
    (venv)$

.. class:: incremental

I don't want to check that virtualenv into git, so I add ``venv`` to my
.gitignore file.

.. class:: incremental

That way, git will ignore that directory and everything in it.

Heroku - Install Dependencies
-----------------------------

For Heroku to work, it needs to know what packages you'll need installed.  

.. class:: incremental

We can use ``pip`` to take care of this:

.. class:: incremental small

::

    (venv)$ pip install Django=1.4.5 psycopg2 dj-database-url

.. class:: incremental

Psycopg2 is a DBAPI connector for PostgreSQL.  Heroku requires Postgresql

.. class:: incremental

``dj-database-url`` allows the Django DB settings to come from an ``env`` variable.

Heroku - Freeze Dependencies
----------------------------

Heroku uses ``pip`` too. It uses a file called ``requirements.txt`` to know
what to do.

.. class:: incremental

You create that file:

.. class:: incremental small

::

    (venv)$ pip freeze > requirements.txt

.. class:: incremental

Then, add the file to your repository and commit:

.. class:: incremental small

::

    (venv)$ git add requirements.txt
    (venv)$ git commit -m "setting requirements for heroku"

Heroku - Django Settings
------------------------

To adapt Django to the Heroku environment, we need to add the following to the 
end of our ``settings.py`` file:

.. code-block:: python
    :class: incremental small

    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

.. class:: incremental

Commit these changes to your heroku-deploy branch.

.. class:: incremental

Local development settings are different. You can `use different settings for
production and development
<http://stackoverflow.com/questions/5159852/managing-multiple-settings-py-files>`_

Heroku - Procfile
-----------------

Finally, we need to create a file named ``Procfile``.

.. class:: incremental

Heroku uses this to learn about the processes we want running.

.. class:: incremental

Lines in the file take the form *process_type*: *command*,

.. class:: incremental

Create the file ``Procfile`` and add the following text:

.. class:: incremental small

web: python manage.py runserver 0.0.0.0:$PORT --noreload

.. class:: incremental small

Then, add and commit that file to the repository.

Heroku - Create and Deploy
--------------------------

At this point, we're ready to go. 

.. class:: incremental

First, we create a new ``app`` in heroku with our repo:

.. class:: incremental small

::

    (venv)$ heroku create 
    Creating fierce-plains-6505... done, stack is cedar
    http://fierce-plains-6505.herokuapp.com/ | git@heroku.com:fierce-plains-6505.git
    Git remote heroku added
    (venv)$

.. class:: incremental

Then, deploy it by 'pushing' to the heroku remote (master branch):

.. class:: incremental small

::

    (venv)$ git push heroku heroku-deploy:master

Heroku - What Happens
---------------------

Heroku works like github, in a way.

.. class:: incremental

When our repository is *pushed*, a hook script detects the update and starts
working.

.. class:: incremental

* Heroku `detects <https://devcenter.heroku.com/articles/buildpacks>`_ that we
  are building a python project
* A python virtualenv is created
* ``pip`` installs the dependencies in ``requirements.txt``
* Heroku further detects that we are building a Django app and runs
  ``collectstatic``
* Our ``Procfile`` is read, and data about the processes we want is written to
  the environment

Heroku - Syncdb
---------------

Heroku will not run syncdb for us.  We have to do that on our own.  

.. class:: incremental

Heroku *does* provide us with a way to run one-off commands on our server, though:

.. class:: incremental

::

    (venv)$ heroku run python manage.py syncdb

.. class:: incremental

This command is run through an ssh tunnel. We can interact with it.

.. class:: incremental

We can use other commands, like ``shell`` with ``heroku run``.

Heroku - Reap the Rewards
-------------------------

All we have to do now is start a process so we can see our work:

.. class:: incremental small

::

    (venv)$ heroku ps:scale web=1
    Scaling web processes... done, now running 1
    (venv)$ heroku ps
    === web: `python manage.py runserver 0.0.0.0:$PORT --noreload`
    web.1: up 2013/03/05 06:28:13 (~ 21m ago)
    (venv)$ heroku open

.. class:: incremental

That last bit will automatically open a web browser pointing at the URL where
may be seen.

Heroku - DNS
------------

Heroku does not want you to point A record DNS names at it's services.

.. class:: incremental

Using ``www.mydomain.com`` is okay, but ``mydomain.com`` is not.

.. class:: incremental

They also don't want you to use IP addresses, since their architecture means
IP addresses change.

.. class:: incremental

I set up a CNAME record for ``microblog.crisewing.com``. It points to the URL
opened when I type ``heroku open``.

.. class:: incremental

So long as I keep this heroku ``app``, that domain name will not change.

Clean-up
--------

This is but one example of a cloud deployment.

.. class:: incremental

It is considerably easier to do than most other cloud deployments.

.. class:: incremental

It is also considerably more constrained than other deployments.

Take-away
---------

When you are making choices about deployment, you **must** take into
consideration your needs, both now and in the future:

.. class:: incremental

* What type of Framework will you use?
* What type of Database will you use?
* What growth do you expect to experience (best and worst case)?
* How much control do you want over *all* the processes that make your website
  run?
* How much time/expertise do you have (or can you afford to acquire)?

.. class:: incremental

Carefully consider these questions, and you will find an appropriate solution.

Lab Time
--------

For the rest of today, we work on your projects.

