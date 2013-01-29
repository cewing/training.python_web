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

Save Memory on Loading
----------------------

When you are loading data from an API, you can sometimes get more than you
bargained for. Both BeautifulSoup and the json library provide ways to help:

.. code-block:: python
    :class: incremental

    page = urllib2.urlopen(url)
    json_string = page.read()
    json.loads(json_string)

.. code-block:: python
    :class: incremental

    page = urllib2.urlopen(url)
    json.loads(page)

.. class:: incremental

The second form will *buffer* the input as it is read, and minimize memory
consumption. If you've got really large data sets this can be very good.

Protect Yourself From the Net
-----------------------------

We learned in our last class that APIs can flake. Remember that. It's *vital*!

.. code-block:: python
    :class: incremental

    page = urllib2.urlopen(url)
    parsed = BeautifulSoup(page)

.. code-block:: python
    :class: incremental

    page = urllib2.urlopen(url)
    if page.code == 200:
        parsed = BeautifulSoup(page)
    else:
        raise SomeExceptionYouCanCatch

.. class:: incremental

What happens if your desired API is offline when a user comes to see your
page? Make sure you give yourself a way to be kind to your users. 500 Internal
Server Errors suck!

What You Made
-------------

.. class:: incremental

* geographic locations of our Bluebox VMs
* Visualization of the popularity of Facebook Friends' first names
* Restaurants near your location with recent Health Inspection data
* A Last-FM user's top artists, with lists of mixcloud mixes featuring each of
  them
* A list of Craigslist apartments with the nearest bars, pizza and sushi
  places and their Yelp ratings
* Geographic locations of the top 20 users returned for a twitter search,
  along with other twitter data

A Note on Homeworks
-------------------

.. class:: incremental

* I've been saying that only attendance counts for your grade.
* It was brought to my attention this week that my own syllabus says
  differently
* The work we've done so far is all, in some sense, foundational. We will be
  using tools starting next week that build upon the tools we've encountered.

.. class:: incremental

Homework from this point out should be considered required. We are now
reaching the level of tools you will use on a day to day basis. Mastery comes
with practice.

And Second
----------

.. class:: big-centered

Questions from the Reading?

And Third
---------

Open ``assignments/week04/lab/type-along.txt``

.. class:: incremental

This contains all the code examples from today's lecture. It's meant to help
you with keeping up when we are moving quickly through sample slides. I hope
it is of some use.

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

Windows folks, for this next bit please open an ssh terminal on your VM.  

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
* IIS (on Windows)
* Some other HTTP server that implements CGI (lighttpd, ...?)

.. class:: incremental

Let's start locally by using the Python module

.. class:: incremental

Again, Windows folks, this is going to be most easily done on your VM

Running CGI - Preparations
--------------------------

If you are running this on your VM (*Windows users, this means **you***) and
you **do not already have the class repo on your vm**, here's the steps to get
it::

    $ cd
    $ mkdir git
    $ cd git
    $ git clone https://github.com/cewing/training.python_web.git
    $ cd training.python_web

Running CGI - First Test
------------------------

Make sure you have the latest source of the class documentation, then:

.. class:: incremental

* Open *two* terminal windows and in both, ``cd`` to the
  ``assignments/week04/lab`` directory
* In the first terminal, run ``python -m CGIHTTPServer``
* Open a web browser and load ``http://localhost:8000/`` 
* (if you're running on your VM, you'll open http://<YOUR_BLUEBOX_VM>.blueboxgrid.com:8000/)
* Click on *CGI Test 1*

Did that work?
--------------

* If nothing at all happens, check your terminal window
* Look for this: ``OSError: [Errno 13] Permission denied``
* If you see something like that, check permissions for ``cgi-bin`` *and*
  ``cgi_1.py``
* The file must be executable, the directory needs to be readable *and*
  executable.


.. class:: incremental

Remember that you can use the bash ``chmod`` command to change permissions

Break It
--------

Once that's working correctly, let's play with breaking it. Start by making
the file not executable:

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

| Put the permissions back to how they were before:
| $ chmod 755 cgi-bin/cgi_1.py

Break It Differently
--------------------

Okay, so problems with permissions can lead to failure. How about errors in
the script?  What happens there?

.. class:: incremental

* Open ``assignments/week04/lab/cgi-bin/cgi_1.py`` in an editor
* if you're on your VM, use ``nano cgi-bin/cgi_1.py`` (ctrl-o, <enter> to save, ctrl-x to exit)
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

Notice the first line of that script: ``#!/usr/bin/python``. This is called a
*shebang* (short for hash-bang) and it tells the system what executable
program to use when running the script.

CGI Process Execution
---------------------

When a web server like ``CGIHTTPServer`` or ``Apache`` runs a CGI script, it
simply attempts to run the script as if it were a normal system user.  This is
just like you calling::

    $ ./path/to/cgi_1.py

.. class:: incremental

In fact try that now (use the real path), what do you get?  

.. class:: incremental

What is missing?

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

Let's interfere with this:

.. class:: small

::

    $ ls -l /usr/bin/python*
    lrwxrwxrwx 1 root root       9 Oct  4 18:48 python -> python2.6
    lrwxrwxrwx 1 root root       9 Oct  4 18:48 python2 -> python2.6
    -rwxr-xr-x 1 root root 2288240 Apr 16  2010 python2.6
    $ sudo chmod 750 python
    $ ls -l /usr/bin/python*
    lrwxrwxrwx 1 root root       9 Oct  4 18:48 python -> python2.6
    lrwxrwxrwx 1 root root       9 Oct  4 18:48 python2 -> python2.6
    -rwxr-x--- 1 root root 2288240 Apr 16  2010 python2.6

.. class:: incremental

Now, reload your web browser. Did you get anything? Check your debugging
tools.

Enough of That
--------------

Okay, put the permissions back on your system python:

.. class:: small

::

    $ sudo chmod 755 /usr/bin/python
    $ ls -l /usr/bin/python*
    lrwxrwxrwx 1 root root       9 Oct  4 18:48 python -> python2.6
    lrwxrwxrwx 1 root root       9 Oct  4 18:48 python2 -> python2.6
    -rwxr-xr-x 1 root root 2288240 Apr 16  2010 python2.6

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

Let's find 'em.  In a terminal (on your local machine, please) fire up python:

.. code-block::

    >>> import CGIHTTPServer
    >>> CGIHTTPServer.__file__
    '/big/giant/path/to/lib/python2.6/CGIHTTPServer.py'

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

.. class:: incremental

As a corollary to this, the ``test`` method of the cgi module has this line:
``sys.stderr = sys.stdout``. Why?

Recap:
------

What the Server Does:

.. class:: incremental small

* parses the request
* sets up the environment, including HTTP and SERVER variables
* figures out if the URI points to a CGI script and runs it
* builds an appropriate HTTP Response first line ('HTTP/1.1 200 OK\\r\\n')
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

.. class:: incremental small

* In ``assignments/week04/lab/src`` you will find the file
  ``lab1_cgi_template.py``.
* Copy that file to ``assignments/week04/lab/cgi-bin/lab1_cgi.py`` (note the
  missing '_template' part)
* The script contains some html with text naming elements of the CGI
  environment.
* Use elements of os.environ to fill in the blanks.
* view your work in a browser at localhost:8000 *or* <yourvm>.blueboxgrid.com:8000

.. class:: incremental center

**GO**

Putting CGI Online
------------------

We have CGI working, how do we make it **live** so that others can see our
work?

.. class:: incremental big-centered

**Put It On A Server**

A Word About Our VMs
--------------------

We each have an individual VM that we can use for the duration of this class.

.. class:: incremental

These machines, with a value of $8000 or more, have been donated to us by Blue
Box Hosting.

.. image:: img/bluebox_logo.png
    :align: center
    :class: incremental
    :width: 60%

.. class:: incremental

If you need hosting services, consider https://bluebox.net/

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
* Enabling a site makes a link to the config in
  ``/etc/apache2/sites-enabled``

.. class:: incremental

Check your server to see what sites are available and enabled:

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

.. class:: incremental

More about Apache Configuration: http://httpd.apache.org/docs/

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
    :width: 75%

.. class:: incremental

Apache is configured to disallow directory listings for ``cgi-bin`` (No
``Option Indexes``)

Copy CGI To The Server
----------------------

To get our script to run, we have to put it in the ``cgi-bin`` directory.

.. class:: incremental

* The ``/usr/lib/cgi-bin`` directory is owned by **root**
* It is **not** world-writable
* You'll need to put it somewhere you can write without using ``sudo``
* Put it in your home directory
* If you are already working on your VM, you can skip this part.

.. class:: incremental

::

    $ cd /path/to/training.python_web
    $ scp assignments/week04/lab/cgi-bin/cgi_1.py uw@<yourvm>:~/

Move it to cgi-bin
------------------

Now that we have the script on the server, we can use sudo there to put it in
the right spot (execute these commands on your VM)::

    $ sudo mv ~/cgi_1.py /usr/lib/cgi-bin/
    $ ls -l /usr/lib/cgi-bin
    total 4
    -rwxr-xr-x 1 uw uw 42 Jan 20 04:34 cgi_1.py

.. class:: incremental

Does the file have the right permissions to be executed successfully?

.. class:: incremental small

``http://<your-vm-url>/cgi-bin/cgi_1.py``

Do it again
-----------

Repeat the process. This time, move your ``lab1_cgi.py`` script from our first
lab exercise.

And Now
-------

.. class:: big-centered

A Short Break

CGI Problems
------------

CGI is great, but there are problems:

.. class:: incremental

* Code is executed *in a new process*
* **Every** call to a CGI script starts a new process on the server
* Starting a new process is expensive in terms of server resources
* *Especially for interpreted languages like Python*

.. class:: incremental

How do we overcome this problem?

Alternatives to CGI
-------------------

The most popular approach is to have a long-running process *inside* the
server that handles CGI scripts.

.. class:: incremental

FastCGI and SCGI are existing implementations of CGI in this fashion.
**mod_python** offers a similar capability for Python code.

.. class:: incremental

* Each of these options has a specific API
* None are compatible with each-other
* Code written for one is **not portable** to another
* This makes it hard to **share resources**


WSGI
----

Enter WSGI, the Web Server Gateway Interface.

.. class:: incremental

Where other alternatives are specific implementations of the CGI standard,
WSGI is itself a new standard, not an implementation.

.. class:: incremental

WSGI is generalized to describe a set of interactions, so that developers can
write WSGI-capable apps and deploy them on any WSGI server.

.. class:: incremental

Read the WSGI spec: http://www.python.org/dev/peps/pep-0333

WSGI: Apps and Servers
----------------------

.. class:: small

WSGI consists of two parts, a *server* and an *application*.

.. class:: small

A WSGI Server must:

.. class:: incremental small

* set up an environment, much like the one in CGI
* provide a method ``start_response(status, headers, exc_info=None)``
* build a response body by calling an *application*, passing
  ``environment`` and ``start_response`` as args
* return a response with the status, headers and body

.. class:: small

A WSGI Appliction must:

.. class:: incremental small

* Be a callable (function, method, class) 
* Take an environment and a ``start_response`` callable as arguments
* Return an iterable of 0 or more strings, which are treated as the body of
  the response.

Flowcharts
----------

WSGI Servers:

.. class:: center incremental

**HTTP <---> WSGI**

.. class:: incremental

WSGI Applications:

.. class:: center incremental

**WSGI <---> app code**

The Whole Enchilada
-------------------

The WSGI *Stack* can thus be expressed like so:

.. class:: incremental big-centered

**HTTP <---> WSGI <---> app code**

Using wsgiref
-------------

The Python standard lib provides a reference implementation of WSGI:

.. image:: img/wsgiref_flow.png
    :align: center
    :width: 80%
    :class: incremental

Apache mod_wsgi
---------------

You can also deploy with Apache as your HTTP server, using **mod_wsgi**:

.. image:: img/mod_wsgi_flow.png
    :align: center
    :width: 80%
    :class: incremental

Proxied WSGI Servers
--------------------

Finally, it is also common to see WSGI apps deployed via a proxied WSGI
server:

.. image:: img/proxy_wsgi.png
    :align: center
    :width: 80%
    :class: incremental

WSGI Middleware
---------------

Another feature of WSGI is *middleware*:

.. class:: incremental

* Middleware implements both the *server* and *application* interfaces
* Middleware acts as a server when viewed from an application
* Middleware acts as an application when viewed from a server

.. image:: img/wsgi_middleware_onion.png
    :align: center
    :width: 38%
    :class: incremental

Simplified WSGI Server
----------------------

.. code-block:: python
    :class: small

    from some_application import simple_app
    
    def build_env(request):
        # put together some environment info from the reqeuest
        return env
    
    def handle_request(request, app):
        environ = build_env(request)
        iterable = app(environ, start_response)
        for data in iterable:
            # send data to client here
    
    def start_response(status, headers):
        # start an HTTP response, sending status and headers
    
    # listen for HTTP requests and pass on to handle_request()
    serve(simple_app)

WSGI Environment
----------------

.. class:: small incremental

REQUEST_METHOD
  The HTTP request method, such as "GET" or "POST". This cannot ever be an
  empty string, and so is always required.
SCRIPT_NAME
  The initial portion of the request URL's "path" that corresponds to the
  application object, so that the application knows its virtual "location".
  This may be an empty string, if the application corresponds to the "root" of
  the server.
PATH_INFO
  The remainder of the request URL's "path", designating the virtual
  "location" of the request's target within the application. This may be an
  empty string, if the request URL targets the application root and does not
  have a trailing slash.
QUERY_STRING
  The portion of the request URL that follows the "?", if any. May be empty or
  absent.
CONTENT_TYPE
  The contents of any Content-Type fields in the HTTP request. May be empty or
  absent.

WSGI Environment
----------------

.. class:: small

CONTENT_LENGTH
  The contents of any Content-Length fields in the HTTP request. May be empty
  or absent.
SERVER_NAME, SERVER_PORT
  When combined with SCRIPT_NAME and PATH_INFO, these variables can be used to
  complete the URL. Note, however, that HTTP_HOST, if present, should be used
  in preference to SERVER_NAME for reconstructing the request URL. See the URL
  Reconstruction section below for more detail. SERVER_NAME and SERVER_PORT
  can never be empty strings, and so are always required.
SERVER_PROTOCOL
  The version of the protocol the client used to send the request. Typically
  this will be something like "HTTP/1.0" or "HTTP/1.1" and may be used by the
  application to determine how to treat any HTTP request headers. (This
  variable should probably be called REQUEST_PROTOCOL, since it denotes the
  protocol used in the request, and is not necessarily the protocol that will
  be used in the server's response. However, for compatibility with CGI we
  have to keep the existing name.)

WSGI Environment
----------------

.. class:: small

HTTP\_ Variables
  Variables corresponding to the client-supplied HTTP request headers (i.e.,
  variables whose names begin with "HTTP\_"). The presence or absence of these
  variables should correspond with the presence or absence of the appropriate
  HTTP header in the request.

.. class:: center incremental

**Seem Familiar?**

Simple WSGI Application
-----------------------

Where the simplified server above is **not** functional, this is a complete
app:

.. code-block:: python

    def application(environ, start_response)
        status = "200 OK"
        body = "Hello World\n"
        response_headers = [('Content-type', 'text/plain',
                             'Content-length', len(body))]
        start_response(status, response_headers)
        return [body]

Simple WSGI Middleware
----------------------

Here's a very simple sample of middleware:

.. code-block:: python
    :class: small

    class Upperware:
        def __init__(self, app)
            self.wrapped_app = app
        
        def __call__(self, environ, start_response)
            for data in self.wrapped_app(environ, start_response):
                return data.upper()

.. class:: incremental

How does this fulfill the server part of the agreement?  

.. class:: incremental

The application part?

A Word on Middleware
--------------------

.. class:: incremental center

**TRANSPARENT**

.. class:: incremental

* loose coupling means layers should not need to know anything about each
  other
* You should be able to combine a server from one package, middleware from
  another, and application code from yet another
* A good test is this:

.. class:: incremental center

If you remove your middleware, does your app break?

.. class:: incremental

If so, the code should be in your app, not in middleware.

Interesting Middleware Uses
---------------------------

Middleware can be used for a number of really useful purposes:

.. class:: incremental

* Routing (stitch together multiple wsgi apps into one site)
* Authentication (share authentication between multiple apps, delegate)
* Cache Control (decide what to rebuild and what can be re-used)
* Debugging and Introspection (provide information about reqest, reponse and
  processing)
* Theming (use tools like xslt to build themes that can merge different apps)

WSGI on our VMs
---------------

For our lab, and for the homework, we'll be using WSGI via mod_wsgi on our
VMs.

.. class:: incremental

CGI was all set for us, once we turned on Apache.  

.. class:: incremental

How about WSGI?

.. class:: incremental

Let's find out.

Apache Modules
--------------

The abilities of Apache are extended using **modules**. You can list *loaded*
modules with the ``apache2ctl`` command.

.. class:: incremental

Open an ssh terminal on your VM:

.. class:: incremental

::

    $ which apache2ctl
    /usr/sbin/apache2ctl
    $ apache2ctl -M
    Loaded Modules:
     ...
     alias_module (shared)
     auth_basic_module (shared)
     authn_file_module (shared)
     authz_default_module (shared)
     ...

Another Way
-----------

You can also see which modules are enabled by checking the listings in
``/etc/apache2/mods-enabled/``:

.. class:: incremental small

::

    $ ls /etc/apache2/mods-enabled/
    alias.conf            authz_user.load  dir.load          php5.load
    alias.load            autoindex.conf   env.load          reqtimeout.conf
    auth_basic.load       autoindex.load   mime.conf         reqtimeout.load
    authn_file.load       cgi.load         mime.load         setenvif.conf
    authz_default.load    deflate.conf     negotiation.conf  setenvif.load
    authz_groupfile.load  deflate.load     negotiation.load  status.conf
    authz_host.load       dir.conf         php5.conf         status.load

Available Modules
-----------------

By default, not all the modules that are *available* have been *enabled*. You
can check the ``/etc/apache2/mods-available/`` directory to see what else is
there: 

.. class:: incremental small

::

    $ ls /etc/apache2/mods-available/
    actions.conf          cern_meta.load     ident.load           proxy_http.load
    actions.load          cgi.load           imagemap.load        proxy_scgi.load
    alias.conf            cgid.conf          include.load         reqtimeout.conf
    alias.load            cgid.load          info.conf            reqtimeout.load
    asis.load             charset_lite.load  info.load            rewrite.load
    auth_basic.load       dav.load           ldap.load            setenvif.conf
    auth_digest.load      dav_fs.conf        log_forensic.load    setenvif.load
    ...

Adding New Modules
------------------

.. class:: incremental

* Debian/Ubuntu provide pre-packaged versions of software like Apache
* The pre-packaged versions will come with popular extensions included
* We want to install an Apache module which is *not* included in the
  pre-packaged Apache
* We can use the packaging tools in Debian/Ubuntu to install it ourselves.
* The packaging tools are called **apt** (Advanced Packaging Tool)

.. class:: incremental

There is more to learn about **apt** than we can hope to cover here. Learn it
as you need it.

Searching Using apt-cache
-------------------------

You can search for a package using apt-cache (``apt-cache search`` *text*)::

    $ apt-cache search mod_wsgi

.. class:: incremental

Once you've found the name of a package, you can use apt-cache to read the
dependencies it has:

.. class:: incremental

::

    $ apt-cache depends libapache2-mod-wsgi
    libapache2-mod-wsgi
      Depends: apache2
        apache2-mpm-itk
    ...

Installing using apt-get
------------------------

Okay, so we know what the package is called, and what it will require.  Let's
install it! (we'll need superuser privileges to do this, so *sudo*)

::

    $ sudo apt-get install libapache2-mod-wsgi
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    ...
    Get:1 http://us.archive.ubuntu.com/ubuntu/ lucid/universe libapache2-mod-wsgi 2.8-2ubuntu1 [63.5kB]
    Fetched 63.5kB in 0s (197kB/s)              
    ...
    Setting up libapache2-mod-wsgi (2.8-2ubuntu1)
     * Restarting web server apache2
     ... waiting                                     [ OK ]

Check Your Work
---------------

Are we done?  Remember that command for checking loaded modules?

.. class:: incremental

::

    $ apache2ctl -M
    Loaded Modules:
     ...
     alias_module (shared)
     auth_basic_module (shared)
     ...
     status_module (shared)
     wsgi_module (shared)
    Syntax OK

.. class:: incremental center

**Wahooooo!**

Configure mod_wsgi
------------------

Like CGI, mod_wsgi requires that we do some set up in our Apache
configuration.

.. class:: incremental

Open the file /etc/apache2/sites-available/default in a text editor:

.. class:: incremental

::

    $ cd /etc/apache2
    $ vi sites-available/default

.. class:: incremental

You can also use ``nano`` or ``pico`` or ``joe`` or whatever simple text
editor you like.

Adding WSGIScriptAlias
----------------------

mod_wsgi uses the directive **WSGIScriptAlias** in exactly the same way that
CGI uses **ScriptAlias**:

.. code-block:: apache
    :class: small

    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
    <Directory "/usr/lib/cgi-bin">
            AllowOverride None
            Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
            Order allow,deny
            Allow from all
    </Directory>
    
    # Add this line to the file to expose a /wsgi-bin directory
    WSGIScriptAlias /wsgi-bin/ /usr/lib/wsgi-bin/

.. class:: incremental

Save your work and exit the editor

Give WSGI Something To Do
-------------------------

We've set Apache to look in ``/usr/lib/wsgi-bin/`` for wsgi scripts. We need
to make that directory since it doesn't exist by default::

    $ sudo mkdir /usr/lib/wsgi-bin

.. class:: incremental

On your local machine find the ``wsgi_test.py`` file in
``assignments/week04/lab/``. Use ``scp`` to move it to your home directory on
the VM. Then on the VM:

.. class:: incremental small

::

    $ sudo cp ~/wsgi_test.py /usr/lib/wsgi-bin/
    $ ls -l /usr/lib/wsgi-bin/
    total 4
    -rwxr-xr-x 1 root root 955 Jan 22 00:06 wsgi_test.py

Reload Apache
-------------

Any time you change Apache configuration, you need to restart to pick up the 
changes.  First, you should check your work to avoid
crashing Apache::

    $ apache2ctl configtest
    Syntax OK

.. class:: incremental

Okay, our syntax is good, no problems there.  Let's restart:

.. class:: incremental

::

    $ sudo /etc/init.d/apache2 graceful
    * Reloading web server config apache2           [ OK ]

.. class:: incremental

Hit http://YOUR_VM.blueboxgrid.com/wsgi-bin/wsgi_test.py with your browser.

Looking at wsgi_test.py
-----------------------

.. code-block:: python
    :class: tiny

    #!/usr/bin/python
    
    # This is our application object. It could have any name,
    # except when using mod_wsgi where it must be "application"
    def application(environ, start_response):
        
        # build the response body possibly using the environ dictionary
        response_body = 'The request method was %s' % environ['REQUEST_METHOD']
        
        # HTTP response code and message
        status = '200 OK'
        
        # These are HTTP headers expected by the client.
        # They must be wrapped as a list of tupled pairs:
        # [(Header name, Header value)].
        response_headers = [('Content-Type', 'text/plain'),
                            ('Content-Length', str(len(response_body)))]
        
        # Send them to the server using the supplied function
        start_response(status, response_headers)
        
        # Return the response body.
        # Notice it is wrapped in a list although it could be any iterable.
        return [response_body]

Lab 2
-----

Let's repeat what we did for CGI with WSGI:

.. class:: incremental

* In ``assignments/week04/lab/src`` you will find the file
  ``lab2_wsgi_template.py``.
* Copy that file to ``assignments/week04/lab/wsgi-bin/lab2_wsgi.py`` (note the
  missing '_template' part)
* The script contains some html with text naming elements of the WSGI
  environment.
* Use elements of ``environ`` to fill in the blanks.
* You can test and debug changes *locally* by running the script (``python
  lab2_wsgi.py``) and then pointing your browser to ``localhost:8080``

.. class:: incremental center

**GO**

Assignment
----------

Using what you've learned this week, Attempt the following:

.. class:: incremental

* Create a small, multi-page WSGI application
* Use ``assignments/week04/athome/bookdb.py`` as a data source
* Your app index page should list the books in the db
* Each listing should supply a link to a detail page
* Each detail page should list information about the book

.. class:: incremental

Use the Armin Ronacher reading from the class outline as a source for hints:
http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/

Submitting the Assignment
-------------------------

This week we are going to do something a bit different. Get your application
running on your VM. Then add the following to ``assignments/week04/athome``
and submit a pull request:

* A README.txt file containing the URL I can visit to see your application.
  You can also put questions or comments in this file.

* Your source code, whatever is up on your VM.
