Internet Programming with Python
================================

.. image:: img/gateway.jpg
    :align: left
    :width: 50%

Week 4: CGI, WSGI and Living Online

.. class:: intro-blurb

Wherein we discover the gateways to dynamic processes on a server.

.. class:: image-credit

image: The Wandering Angel http://www.flickr.com/photos/wandering_angel/1467802750/ - CC-BY

But First
---------

.. class:: big-centered

Review from the Assignment

And Second
----------

.. class:: big-centered

Questions from the Reading?

And Now...
----------

.. class:: big-centered

Gateways

Think Back
----------

In week two, we wrote an HTTP server.

We set up the server to be *dynamic* by returning the output of a python
script

.. class:: incremental

But what if we want to pass information to that script?

.. class:: incremental

How do we let the script have access to information about the HTTP request
itself?

Stepping Away
-------------

Let's think about this same problem in another realm, the command line.

.. class:: incremental

In a ``bash`` shell we can do this:

.. class:: incremental

::

    $ export VARIABLE='some_value'
    $ echo this is the value: $VARIABLE
    this is the value: some_value

Environment
-----------

This new variable is now part of our shell **environment**, and we can see that:

.. class:: incremental

::

    $ printenv
    VARIABLE=some_value
    TERM_PROGRAM=iTerm.app
    TERM=xterm
    SHELL=/bin/bash
    ...

Environment in Python
---------------------

We can see this *environment* in Python, too::

    $ python

.. code-block:: python

    >>> import os
    >>> print os.environ['VARIABLE']
    some_value
    >>> print os.environ.keys()
    ['VERSIONER_PYTHON_PREFER_32_BIT', 'VARIABLE', 
     'LOGNAME', 'USER', 'PATH', ...]

Altering the Environment
------------------------

You can alter os environment values while in Python:

.. code-block:: python

    >>> os.environ['VARIABLE'] = 'new_value'
    >>> print os.environ['VARIABLE']
    new_value

.. class:: incremental

But that doesn't change the original value, *outside* Python:

.. class:: incremental

::

    >>> ^D
    $ echo this is the value: $VARIABLE
    this is the value: some_value

Lessons Learned
---------------

.. class:: incremental

* Subprocesses inherit their environment from their Parent
* Parents do not see changes to environment in subprocesses
* In Python, you can actually set the environment for a subprocess explicitly

.. class:: incremental small

::

    subprocess.Popen(args, bufsize=0, executable=None, 
                     stdin=None, stdout=None, stderr=None, 
                     preexec_fn=None, close_fds=False, 
                     shell=False, cwd=None, env=None, # <-------
                     universal_newlines=False, startupinfo=None, 
                     creationflags=0)

Web Environment
---------------

.. class:: big-centered

CGI is little more than a set of standard environmental variables

RFC 3875
--------

First discussed in 1993, formalized in 1997, the current version (1.1) has
been in place since 2004.

From the preamble:

.. class:: center

*This memo provides information for the Internet community. It does not specify
an Internet standard of any kind.*

.. class:: image-credit

RFC 3875 - CGI Version 1.1: http://tools.ietf.org/html/rfc3875

Meta-Variables
--------------

.. class:: small

::

    4.  The CGI Request . . . . . . . . . . . . . . . . . . . . . . .  10
        4.1. Request Meta-Variables . . . . . . . . . . . . . . . . .  10
             4.1.1.  AUTH_TYPE. . . . . . . . . . . . . . . . . . . .  11
             4.1.2.  CONTENT_LENGTH . . . . . . . . . . . . . . . . .  12
             4.1.3.  CONTENT_TYPE . . . . . . . . . . . . . . . . . .  12
             4.1.4.  GATEWAY_INTERFACE. . . . . . . . . . . . . . . .  13
             4.1.5.  PATH_INFO. . . . . . . . . . . . . . . . . . . .  13
             4.1.6.  PATH_TRANSLATED. . . . . . . . . . . . . . . . .  14
             4.1.7.  QUERY_STRING . . . . . . . . . . . . . . . . . .  15
             4.1.8.  REMOTE_ADDR. . . . . . . . . . . . . . . . . . .  15
             4.1.9.  REMOTE_HOST. . . . . . . . . . . . . . . . . . .  16
             4.1.10. REMOTE_IDENT . . . . . . . . . . . . . . . . . .  16
             4.1.11. REMOTE_USER. . . . . . . . . . . . . . . . . . .  16
             4.1.12. REQUEST_METHOD . . . . . . . . . . . . . . . . .  17
             4.1.13. SCRIPT_NAME. . . . . . . . . . . . . . . . . . .  17
             4.1.14. SERVER_NAME. . . . . . . . . . . . . . . . . . .  17
             4.1.15. SERVER_PORT. . . . . . . . . . . . . . . . . . .  18
             4.1.16. SERVER_PROTOCOL. . . . . . . . . . . . . . . . .  18
             4.1.17. SERVER_SOFTWARE. . . . . . . . . . . . . . . . .  19

Running CGI
-----------

You have a couple of options:

.. class:: incremental

* Python Standard Library CGIHTTPServer
* Apache
* Some other HTTP server that implements CGI (lighttpd, ...?)

.. class:: incremental

Let's start locally by using the Python module

Running CGI - First Test
------------------------

Make sure you have the latest source of the class documentation, then:

.. class:: incremental

* Open *two* terminal windows and in both, ``cd`` to the
  ``assignments/week04/lab`` directory
* In the first terminal, run ``python -m CGIHTTPServer``
* Open a web browser and load ``http://localhost:8000/``
* Click on *CGI Test 1*

Did that work?
--------------

* If nothing at all happens, check your terminal window
* Look for this: ``OSError: [Errno 13] Permission denied``
* If you see something like that, check permissions for ``cgi-bin`` *and*
  ``cgi_1.py``
* The file must be executable, the directory needs to be readable *and*
  executable.

Break It
--------

Once that's working correctly, let's play with breaking it. Start by making
the file not exectuable:

.. class:: incremental small

::

    $ ls -l cgi-bin/cgi_1.py
    -rwxr-xr-x 1 cewing  staff  42 Jan 17 22:30 cgi-bin/cgi_1.py
    $ chmod 444 cgi-bin/cgi_1.py
    $ ls -l cgi-bin/cgi_1.py
    -r--r--r-- 1 cewing  staff  42 Jan 17 22:35 cgi-bin/cgi_1.py

.. class:: incremental

Reload your web browser and see what happens.

.. class:: incremental

Put the permissions back to how they were before.

Break It Differently
--------------------

Okay, so problems with permissions can lead to failure. How about errors in
the script?  What happens there?

.. class:: incremental

* Open ``assignments/week04/lab/cgi-bin/cgi_1.py`` in an editor
* Before where it says ``cgi.test()``, add a single line:

.. code-block:: python
    :class: incremental

    1 / 0

.. class:: incremental

Reload your browser, what happens now?

Errors in CGI
-------------

CGI is famously difficult to debug.  There are reasons for this:

.. class:: incremental

* CGI is designed to provide access to runnable processes to *the internet*
* The internet is a wretched hive of scum and villainy
* Revealing error conditions can expose data that could be exploited

Viewing Errors in Python CGI
----------------------------

Back in your editor, add the following lines, just below ``import cgi``:

.. code-block:: python
    :class: incremental

    import cgitb
    cgitb.enable()

.. class:: incremental

Now, reload again.  

cgitb Output
------------

.. image:: img/cgitb_output.png
    :align: center
    :width: 100%

Another Way to Break It
-----------------------

Let's fix the error from our traceback.  Edit your ``cgi_1.py`` file to match:

.. code-block:: python
    :class: small

    #!/usr/bin/python
    import cgi
    import cgitb

    cgitb.enable()

    cgi.test()

.. class:: incremental

Notice the first line of that script: ``#!/usr/bin/python``. This is called
the *shebang* (short for hash-bang) and it tells the system what executable
program to use when running the script.

CGI Process Execution
---------------------

When a web server like ``CGIHTTPServer`` or ``Apache`` runs a CGI script, it
simply attempts to run the script as if it were a normal system user.  This is
just like you calling::

    $ ./path/to/cgi_1.py

.. class:: incremental

In fact try that now (use the real path), what do you get?  What is missing?

CGI Process Execution
---------------------

There are a couple of important facts that are related to the way CGI
processes are run:

.. class:: incremental

* The script **must** include a *shebang* so that the system knows how to run
  it.
* The script **must** be executable.
* The *executable* named in the *shebang* will be called as the *nobody* user.
* This is a security feature to prevent CGI scripts from running as a user
  with any privileges.
* This means that the *executable* from the script *shebang* must be one that
  *anyone* can run.

More Permission Fun
-------------------

Let's interfere with this::

    $ ls -l /usr/bin/python
    -rwxr-xr-x  2 root  wheel ... /usr/bin/python
    $ sudo chmod 750 /usr/bin/python
    Password: 
    $ ls -l /usr/bin/python
    -rwxr-x---  2 root  wheel ... /usr/bin/python

.. class:: incremental

Now, reload your web browser. Did you get anything? Check your debugging
tools.

Enough of That
--------------

Okay, put the permissions back on your system python::

    $ sudo chmod 755 /usr/bin/python
    Password: 
    $ ls -l /usr/bin/python
    -rwxr-xr-x  2 root  wheel ... /usr/bin/python

The CGI Environment
-------------------

CGI is largely a set of agreed-upon environmental variables.

.. class:: incremental

We've seen how environmental variables are found in python in ``os.environ``

.. class:: incremental

We've also seen that at least some of the variables in CGI are **not** in the
standard set of environment variables.

.. class:: incremental

Where do they come from?

CGI Servers
-----------

Let's find 'em.  In a terminal fire up python:

.. code-block::

    >>> import CGIHTTPServer
    >>> CGIHTTPServer.__file__
    '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/CGIHTTPServer.py'

.. class:: incremental

Copy this path and open the file it points to in your text editor

Environmental Set Up
--------------------

From CGIHTTPServer.py, in the CGIHTTPServer.run_cgi method:

.. code-block:: python
    :class: tiny

    # Reference: http://hoohoo.ncsa.uiuc.edu/cgi/env.html
    # XXX Much of the following could be prepared ahead of time!
    env = {}
    env['SERVER_SOFTWARE'] = self.version_string()
    env['SERVER_NAME'] = self.server.server_name
    env['GATEWAY_INTERFACE'] = 'CGI/1.1'
    env['SERVER_PROTOCOL'] = self.protocol_version
    env['SERVER_PORT'] = str(self.server.server_port)
    env['REQUEST_METHOD'] = self.command
    ...
    ua = self.headers.getheader('user-agent')
    if ua:
        env['HTTP_USER_AGENT'] = ua
    ...
    os.environ.update(env)
    ...

CGI Scripts
-----------

And that's it, the big secret. The server takes care of setting up the
environment so it has what is needed.

.. class:: incremental

Now, in reverse. How does the information that a script creates end up in your
browser?

.. class:: incremental

A CGI Script must print it's results to stdout.

Recap:
------

What the Server Does:

.. class:: incremental small

* parses the request
* sets up the environment, including HTTP and SERVER variables
* figures out if the URI points to a CGI script and runs it
* builds an appropriate HTTP Response first line ('HTTP/1.1 200 Ok\r\n')
* appends what comes from the script on stdout and sends that back

What the Script Does:

.. class:: incremental small

* names appropriate *executable* in it's *shebang* line
* uses os.environ to read information from the HTTP request
* builds *any and all* appropriate **HTTP Headers** (Content-type:,
  Content-length:, ...)
* prints headers, empty line and script output (body) to stdout

Lab 1
-----

You've seen the output from the ``cgi.test()`` method from the ``cgi`` module.
Let's make our own version of this.

.. class:: incremental

* In ``assignments/week04/lab/src`` you will find the file
  ``lab1_cgi_template.py``.
* Copy that file to ``assignments/week04/lab/cgi-bin/lab1_cgi.py`` (note the
  missing '_template' part)
* The script contains some html with text naming elements of the CGI
  environment.
* Use elements of os.environ to fill in the blanks.

.. class:: incremental center

**GO**

Putting CGI Online
------------------

We have CGI working, how do we make it **live** so that others can see our
work?

.. class:: incremental big-centered

**Put It On A Server**

Apache
------

Our VMs have the Apache HTTP Server installed and ready to use. Unfortunately
for our current purposes, Apache is not the running web server software.

Load ``http://<your-vm-id>.blueboxgrid.com`` in your web browser.  What do you see?

.. image:: img/nginx.png
    :align: center
    :class: incremental
    :width: 75%

Managing Server Processes
-------------------------

.. class:: incremental

* Nginx is a great webserver, but it doesn't support running external processes
* This is a good choice for security, but not good for us right now
* We need to turn it off, and turn on Apache

.. class:: incremental

SSH into your server. Then run:

.. class:: incremental

::

    $ sudo /etc/init.d/nginx stop
    Stopping nginx: nginx.
    $ sudo /etc/init.d/apache2 start
     * Starting web server apache2    [ OK ]

Check Your Work
---------------

Reload your web browser.  You should now see this:

.. image:: img/apache.png
    :align: center
    :width: 75%

.. class:: incremental

This means that you've stopped nginx and started Apache. Congrats, you are now
a sysadmin!

Default Site
------------

.. class:: incremental

* Apache on Ubuntu is set to do virtual hosting
* Config for individual sites is added in ``/etc/apache2/sites-available``
* Activating a site makes a link to the config in
  ``/etc/apache2/sites-enabled``

.. class:: incremental

Check your server to see what sites are available and active:

.. class:: incremental small

::

    $ cd /etc/apache2/
    $ ls sites-available/
    default  default-ssl
    $ ls -l sites-enabled/
    total 0
    ... 000-default -> ../sites-available/default

Apache Configuration
--------------------

::

    $ less sites-available/default

.. code-block:: apache
    :class: small incremental

    <VirtualHost *:80>
        ServerAdmin webmaster@localhost

        DocumentRoot /var/www
        <Directory />
                Options FollowSymLinks
                AllowOverride None
        </Directory>
        <Directory /var/www/>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
        </Directory>

More Apache Configuration
-------------------------

Skip over the ``ScriptAlias`` for a moment (we'll come back)

.. code-block:: apache
    :class: small incremental

        ErrorLog /var/log/apache2/error.log
        # Possible values include: debug, info, notice, warn, error, crit,
        # alert, emerg.
        LogLevel warn
        CustomLog /var/log/apache2/access.log combined
        
        Alias /doc/ "/usr/share/doc/"
        <Directory "/usr/share/doc/">
            Options Indexes MultiViews FollowSymLinks
            AllowOverride None
            Order deny,allow
            Deny from all
            Allow from 127.0.0.0/255.0.0.0 ::1/128
        </Directory>
        
    </VirtualHost>

Apache CGI Configuration
------------------------

This is the bit that sets up CGI for us:

.. code-block:: apache

    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
    <Directory "/usr/lib/cgi-bin">
            AllowOverride None
            Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
            Order allow,deny
            Allow from all
    </Directory>

Setting up Our Script
---------------------

The directory for CGI is ``/usr/lib/cgi-bin/``.  What's there now?

.. class:: incremental

::

    $ ls -la /usr/lib/cgi-bin/
    total 24
    drwxr-xr-x  2 root root  4096 Apr 13  2010 .
    drwxr-xr-x 66 root root 20480 Nov 23  2011 ..

No Directory Listing
--------------------

Check the ``cgi-bin`` directory in your browser:

``http://<your-vm-id>.blueboxgrid.com/cgi-bin/``

.. image:: img/forbidden.png
    :align: center
    :class: incremental
    :width: 60%

.. class:: incremental

Apache is configured to disallow directory listings for ``cgi-bin`` (No
``Option Indexes``)






scraps 
------

How to run CGI scripts

- locally

- on a server

How does WSGI differ from CGI?

What is WSGI?

Is WSGI Python-specific?

How to run locally

How to run on a server

