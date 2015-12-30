**********
Session 09
**********

.. figure:: /_static/django-pony.png
    :align: center
    :width: 60%

    image: http://djangopony.com/


Deploying Django
================

.. rst-class:: left
.. container::

    Over the last two sessions you've built and extended a simple Django
    application.

    .. rst-class:: build
    .. container::

        Now it is time to deploy that application to a server so the world can
        see it.

        Previously, we used Heroku to deploy a simple Pyramid application.

        We could do the same with Django, but we won't.

        Instead, we'll deploy to **A**\ mazon **W**\ eb **S**\ ervices (AWS)


Choosing a Deployment Strategy
------------------------------

There are many many different ways to deploy a web application.

.. rst-class:: build
.. container::

    And there are many many services offering platforms for deployment.

    How do you choose the right one for you?

    In general there are a few rules of thumb to consider:

    .. rst-class:: build

    * The more convenient the service, the less configurable it is.
    * The less you pay for a service, the more work you have to do yourself.
    * With great power comes great responsibility.

.. nextslide::

In choosing a service and a strategy, you'll want to ask yourself a few
questions:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * What are the basic software components of my project?
    * How much control or customization of each component do I require?
    * What service supports all of my required components?
    * What service allows my required customizations?
    * If no single service does everything I need, which could be wired
      together?

    The answers to these questions will help to determine the correct choice
    for you.

.. nextslide:: Our Choice for Today

We are going to ignore all these questions, and simply ask one question.

.. rst-class:: build
.. container::

    Which service will allow us to set up each layer in a full web application
    stack so that we can learn how the stack works from front to back?

    The simplest answer to that question is **AWS**.

    Therefore, that's the service we will use today.

Preparing for AWS Deployment
----------------------------

You've started out this week by signing up for AWS.  

.. rst-class:: build
.. container::

    You've created a security group and a key pair to help with accessing any
    servers we create.

    You've also set up an IAM user and configured security credentials for that
    user.

    If we were to be automating our work today, we'd use those credentials to
    allow the `boto`_ library to connect to AWS as that IAM user.

    Then you could `create or destroy resources`_ using that library.

    Issues surrounding using that library on Windows prevent us from trying
    that path tonight.

.. nextslide::

Instead we'll be making a manual deployment using AWS.

.. rst-class:: build
.. container::

    This is always the first step to automation anyway, so this is an important
    first step.

    We'll begin by converting some aspects of our application to better provide
    for security

    In preparation for that we will need to add a new package to our django
    virtual environment.

    .. code-block:: bash
    
        (djangoenv)$ pip install dj-database-url



.. _boto: https://boto.readthedocs.org/
.. _create or destroy resources: http://codefellows.github.io/python-dev-accelerator/lectures/day11/boto.html


.. nextslide:: 12-Factor

This new package is an attempt to help Django get in line with a principle
called `12-factor`_.

.. rst-class:: build
.. container::

    The basic idea is that any data that your app uses for configuration that
    is *external* to the app itself, should be separated from the app.

    The link about contains much more effective explanations, read it.

    We've already done this to some degree with our Pyramid application, by
    putting some configuration values into *environment variables*

    ``dj-database-url`` allows us to do that with the configuration for our
    database.

.. _12-factor: http://12factor.net/


.. nextslide:: Updating Settings

Open ``settings.py`` and replace the current DATABASES dictionary with this:

.. code-block:: python

    DATABASES = {
        'default': dj_database_url.config(
            default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
        )
    }

.. rst-class:: build
.. container::

    The default behavior of ``dj-database-url`` is to look for a
    ``DATABASE_URL`` variable in the environment.

    If it doesn't find that, it uses the value you provide for *default*.

    It converts a `url-style`_ database connection string to the dictionary
    Django expects.

    Here, we've set the default to be the same as what we had previously.

.. _url-style: https://github.com/kennethreitz/dj-database-url#url-schema

.. nextslide:: Repeatable Envs

Another principle of the 12-factor philosophy is to keep the differences
between production and development to a minimum.

.. rst-class:: build
.. container::

    Again, in our Pyramid app we handled this with a ``requirements.txt`` file.

    Here we will do the same.

    At your command line, with the virtualenv active, run the following
    command:

    .. code-block:: bash
    
        (djangoenv)$ pip freeze > requirements.txt

    Then, add that file to your repository and commit the changes.

    At this point, we're about ready to begin working directly with AWS

Setting up An EC2 Instance
--------------------------

Our first step is to create an EC2 (Elastic Compute Cloud) instance for our
application.

.. rst-class:: build
.. container::

    Begin by opening the AWS homepage (http://aws.amazon.com)

    Then click on the big yellow "Sign in to the Console" button

    Fill in your email, check "I am a returning user..." and supply your
    password.

    When the page loads, you are viewing the AWS Console.

    If you don't see a big list of services in that first page, click on
    'Services' in the black header.

    From the list of services, click on ``EC2``.

.. nextslide::

The page that loads is the management console for EC2 resources.  You used it
to create your security group and key pair.

.. rst-class:: build
.. container::

    Click the large blue "Launch Instance" button to start a new instance.

    You should see a list of types of operating system listed.  

    If you don't click on *quick start* at the left.

    In the list, find "Ubuntu Server 14.04 LTS".

    Click on 'Select' to begin building an instance using that operating
    system.

.. nextslide::

The next page of the launch wizard allows you to choose how much CPU power and
RAM your machine will have.

.. rst-class:: build
.. container:: 

    There are only two types of instance that are in the free tier, and one is
    now deprecated.

    Select the *t2.micro* instance by clicking the checkbox to the left of that
    row (it may already be selected for you).

    Below the table of instance types, find and click on "Next: configure
    instance details"

.. nextslide::

Click through the next two steps until you reach "Configure Security Group"

.. rst-class:: build
.. container::

    Here, click the "select an existing security group" button, and pick your
    ssh-access group.

    This group acts as a control for a *firewall* which restricts network
    access to your new instance.

    You've configured that firewall to allow any machine to talk to your
    instance, but only on port 22 (SSH).

    Finish by clicking "Review and Launch"

    Then click on "Launch" to start the instance.

.. nextslide::

When you click "Launch" you are required to choose a key pair to control ssh
access to your new machine.

.. rst-class:: build
.. container::

    Without this key pair, you have no way to access the server, and you must
    destroy it and create a new one.

    Select your ``pk-aws`` pair from the list of existing key pairs.

    Then, check the box that indicates you have the private key and click
    "Launch Instance".

    It will take a few minutes for the new machine to initialize and be ready.

Accessing Your Instance
-----------------------

Once the machine indicates it is "running" you are ready to access that
machine.

.. rst-class:: build
.. container::

    ssh into that machine:

    .. code-block:: bash
    
        ssh -i ~/.ssh/pk-aws.pem ubuntu@<your-public-dns-name.com>

    You will need to indicate that you trust this connection.

    You are now logged in to the server as the default user.  

    AWS sets this user up with the ability to run commands using *sudo*

    You'll begin by updating the OS package manager so you are ensured of
    having the latest versions of any software you install:

    .. code-block:: bash
    
        sudo apt-get update

Deployment Layer 1: Web Server
------------------------------

In our deployment stack, the frontmost facing layer is the Web Server.

.. rst-class:: build
.. container::

    This software is responsible for receiving requests from clients' browsers.

    It will also handle serving static resources in order to relieve Django of
    that burden.

    If you are using ``https``, it's also a good place to handle terminating an
    SSL connection.

    Begin by using the Ubuntu package manager to install ``nginx``:

    .. code-block:: bash
    
        sudo apt-get install nginx

.. nextslide:: Controlling ``nginx``

Like many other packages installed by ``apt-get``, nginx is set up as a
*service*

You can check the status of the service:

.. code-block:: bash

    sudo service nginx status

You can start and stop the server:

.. code-block:: bash

    sudo service nginx stop
    sudo service nginx start

.. nextslide:: Configuring Nginx

Default configuration for nginx lives in ``/etc/nginx``.  Let's look at three
files there in particular:

* /etc/nginx/nginx.conf (controls behavior of the whole server)
* /etc/nginx/sites-available/default (controls a single 'site')
* /etc/nginx/sites-enabled/default (activates a single 'site')


.. nextslide:: Check Your results

Check your results by loading your public DNS name in a browser

.. rst-class:: build
.. container::

    you should see this, do you?

    .. figure:: /_static/nginx_hello.png
        :align: center
        :width: 40%

    Add port 80 to your security group.  Then reload.

Deployment Layer 3: Database
----------------------------

In order to deploy our database, we'll need to install some more software

.. rst-class:: build
.. container::

    Use ``apt-get istall`` to add each of the following packages:

    * build-essential
    * python-dev
    * python-pip
    * python-psycopg2
    * postgresql-client
    * git

.. nextslide:: RDS

You *can* set up postgres directly on the machine you just built, but that's no fun.  

.. rst-class:: build
.. container::

    Let's use RDS, the AWS service for providing databases.

    From 'services' in the header, select RDS.

    In the page that appears, click on 'Launch a DB Instance'

    From the selection of database types, choose PostgreSQL.

    Click **no** to indicate that you don't need a multi-AZ database.

.. nextslide::

On the database details page, You have a bit of work to do.

.. rst-class:: build
.. container::

    First, select ``db.t2.micro`` as the instance type.

    Then, for multi-AZ deployment, select **no** (again)

    Finally, provide values for the last four inputs

    The database identifier must be unique to your account and region, use
    "uwpce".

    For the master username, use "awsuser"

    Provide a password and repeat it to prove you can

.. nextslide::

For Advanced Settings, make sure your DB is in the same availability zone as
your EC2 instance.

.. rst-class:: build
.. container::

    Also ensure that you select the same security group you used for your EC2
    instance from the list of VPC security groups.

    Enter a database name, use "djangodb"

    Finally, click "Launch DB Instance"

    While the database launches, let's return to setting up our application on
    EC2

Deployment Layer 2: Application
-------------------------------

Back on the EC2 instance, in your ssh terminal, clone your django application:

.. code-block:: bash

    git clone <your-app-repo-url>

.. rst-class:: build
.. container::

    pip install the requirements for your app:

        cd djangoblog_uwpce
        pip install -r requirements.txt

    Finally, export a system environment variable called DATABASE_URL with the
    following format::

        postgres://username:password@host:port/dbname

    .. code-block:: bash
    
        export DATABASE_URL=<that string>

    You can now test access with dbshell:

    .. code-block:: bash
    
        python manage.py dbshell

    Work through any issues in getting that to work

.. nextslide::  Wiring It Up

Once working, we can point nginx at the instance:

.. rst-class:: build
.. container::

    .. code-block:: bash
    
        sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
        sudo vi /etc/nginx/sites-available/default

    Add the following content:

    .. code-block:: nginx
    
        server {
            listen 80;
            server_name <your-ec2-public-dns-name>;
            access_log /var/log/nginx/django.log;

            location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            }
        }

.. nextslide::

Save that file and restart nginx:

.. code-block:: bash

    sudo service nginx restart

Then reload your aws instance in a web browser, you should see a BAD GATEWAY
error

now start django and then reload:

.. code-block:: bash

    python manage.py runserver

This works, but as soon as you exit your ssh terminal, django will quit.  We
want a long-running process we can leave behind.


Deployment Layer 4: Permanence
------------------------------

Install gunicorn on the server

.. code-block:: bash

    pip install gunicorn

Back on your own machine, create ``mysite/production.py`` and add the following
content:

.. code-block:: python

    from settings import *

    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['<your instance public dns>', 'localhost']
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

Add the file to your repository and commit your changes.

Then pull the changes back on your EC2 instance

.. nextslide:: Configuration Changes for Nginx

Update nginx config (/etc/nginx/sites-available/default) to serve static files:

.. code-block:: nginx

    server {
        # ...

        location /static/ {
            root /home/ubuntu/djangoblog_uwpce;
        }

    }

.. nextslide:: Running with Gunicorn

Then set an environment variable to point at production settings::

    export DJANGO_SETTINGS_MODULE=mysite.production

Now, run the site using gunicorn::
    
    gunicorn -b 127.0.0.1:8000 -w 4 -D mysite.wsgi

Wahooo!

But still not great, because nothing is monitoring this process.  

There's no way to keep track of how it is doing. 

We can do better.  First, let's kill the processes that spawned::

    killall gunicorn

.. nextslide:: Managing Gunicorn

We can use a process manager to run the gunicorn command, and track the results.

Using linux `upstart`_ is relatively simple.

Put the following in ``/etc/init/djangoblog.conf``

.. code-block:: cfg

    description "djangoblog"

    start on (filesystem)
    stop on runlevel [016]

    respawn
    setuid nobody
    setgid nogroup
    chdir /home/ubuntu/djangoblog_uwpce
    env DJANGO_SETTINGS_MODULE=mysite.production
    env DATABASE_URL=postgres://awsuser:secret123@uwpcedb.c5zwspzpwwsq.us-west-2.rds.amazonaws.com:5432/djangoblog
    exec gunicorn -b 127.0.0.1:8000 -w 4 mysite.wsgi

.. _upstart: http://blog.terminal.com/getting-started-with-upstart/

.. nextslide:: Using Upstart

Once you've completed that, you will find that you can use the Linux
``service`` command to control the gunicorn process.

.. rst-class:: build
.. container::

    Use the following commands::

        $ sudo service djangoblog status
        $ sudo service djangoblog start
        $ sudo service djangoblog stop
        $ sudo service djangoblog restart

    If you see an error message about an ``unknown job`` when you run one of those
    commands, it means you have an error in your configuration file.

    Find the error with this command::

        $ init-checkconf /etc/init/djangoblog.conf

    And that's it!
