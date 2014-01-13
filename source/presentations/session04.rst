Python Web Programming
======================

.. image:: img/gateway.jpg
    :align: left
    :width: 50%

Session 4: CGI, WSGI and Living Online

.. class:: intro-blurb

Wherein we discover the gateways to dynamic processes on a server.

.. class:: image-credit

image: The Wandering Angel http://www.flickr.com/photos/wandering_angel/1467802750/ - CC-BY

Previously
----------

.. class:: incremental

* You've learned about passing messages back and forth with sockets
* You've created a simple HTTP server using sockets
* You may even have made your server *dynamic* by returning the output of a
  python script.

.. class:: incremental

What if you want to pass information to that script?

.. class:: incremental

How can you give the script access to information about the HTTP request
itself?


Stepping Away
-------------

A computer has an *environment*:

.. container:: incremental

    in \*nix, you can see this in a shell:
    
    .. class:: small
    
    ::
    
        $ printenv
        TERM_PROGRAM=iTerm.app
        ...

.. container:: incremental

    or in Windows at the command prompt:
    
    .. class:: small
    
    ::
    
        C:\> set
        ALLUSERSPROFILE=C:\ProgramData
        ...


Setting The Environment
-----------------------

This can be manipulated:

.. container:: incremental

    In a ``bash`` shell we can do this:
    
    .. class:: small
    
    ::
    
        $ export VARIABLE='some value'
        $ echo $VARIABLE
        some value

.. container:: incremental

    or at a Windows command prompt:
    
    .. class:: small
    
    ::
    
        C:\Users\Administrator\> set VARIABLE='some value'
        C:\Users\Administrator\> echo %VARIABLE%
        'some value'


Viewing the Results
-------------------

These new values are now part of the *environment*

.. container:: incremental

    \*nix:
    
    .. class:: small
    
    ::
    
        $ printenv
        TERM_PROGRAM=iTerm.app
        ...
        VARIABLE=some value

.. container:: incremental

    Windows:
    
    .. class:: small
    
    ::
    
        C:\> set
        ALLUSERSPROFILE=C:\ProgramData
        ...
        VARIABLE='some value'

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
    :class: small

    >>> os.environ['VARIABLE'] = 'new_value'
    >>> print os.environ['VARIABLE']
    new_value

.. container:: incremental

    But that doesn't change the original value, *outside* Python:
    
    .. class:: small
    
    ::

        >>> ^D

        $ echo this is the value: $VARIABLE
        this is the value: some_value
        <OR>
        C:\> \Users\Administrator\> echo %VARIABLE%
        'some value'

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

Let's keep it simple by using the Python module


Preparations
------------

In the class resources, you'll find a directory named ``cgi``. Make a copy of
that folder in your class working directory.

.. class:: incremental small red

Windows Users, you will have to edit the first line of
``cgi/cgi-bin/cgi_1.py`` to point to your python executable.

.. class:: incremental

* Open *two* terminal windows in this ``cgi`` directory
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


.. class:: incremental

Remember that you can use the bash ``chmod`` command to change permissions in
\*nix

.. class:: incremental

Windows users, use the 'properties' context menu to get to permissions, just
grant 'full'

Break It
--------

Problems with permissions can lead to failure. So can scripting errors

.. class:: incremental

* Open ``cgi/cgi-bin/cgi_1.py`` in an editor
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


Repair the Error
----------------

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

    $ ./cgi_bin/cgi_1.py

.. class:: incremental

In fact try that now in your second terminal (use the real path), what do you
get?

.. class:: incremental small center

Windows folks, you may need ``C:\>python cgi_1.py``

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

Use the same method as above to import and open the source file for the
``cgi`` module. Note what ``test`` does for an example of this.


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


In-Class Exercise
-----------------

You've seen the output from the ``cgi.test()`` method from the ``cgi`` module.
Let's make our own version of this.

.. class:: incremental small

* In the directory ``cgi-bin`` you will find the file ``cgi_2.py``.
* Open that file in your editor.
* The script contains some html with text naming elements of the CGI
  environment.
* You should use the values in os.environ to fill in the blanks.
* You should be able to view the results of your work by loading
  ``http://localhost:8000/`` and clicking on *Exercise One*

.. class:: incremental center

**GO**


User Provided Data
------------------

All this is well and good, but where's the *dynamic* stuff?

.. class:: incremental

It'd be nice if a user could pass form data to our script for it to use.

.. container:: incremental

    In HTTP, these types of inputs show up in the URL *query* (the part after
    the ``?``)::

        http://myhost.com/script.py?a=23&b=37


Form Data in CGI
----------------

In the ``cgi`` module, we get access to this with the ``FieldStorage`` class:

.. code-block:: python
    :class: incremental small

    import cgi
    
    form = cgi.FieldStorage()
    stringval = form.getvalue('a', None)
    listval = form.getlist('b')

.. class:: incremental

* The values in the ``FieldStorage`` are *always* strings
* ``getvalue`` allows you to return a default, in case the field isn't present
* ``getlist`` always returns a list: empty, one-valued, or as many values as
  are present


In-Class Exercise
-----------------

Let's create a dynamic adding machine.

.. class:: incremental

* In the ``cgi-bin`` directory you'll find ``cgi_sums.py``.
* In the ``index.html`` file in the ``cgi`` directory, the third link leads to
  this file.
* You will use the structure of that link, and what you learned just now about
  ``cgi.FieldStorage``.
* Complete the cgi script in ``cgi_sums.py`` so that the result of adding all
  operands sent via the url query is returned.

.. class:: incremental

For extra fun, return the results in ``json`` format (mimetype:
'application/json').


My Solution
-----------

.. code-block:: python
    :class: small incremental

    form = cgi.FieldStorage()
    operands = form.getlist('operand')
    total = 0
    for operand in operands:
        try:
            value = int(operand)
        except ValueError:
            value = 0
        total += value

    output = {'result': total}
    json_output = json.dumps(output)

    print "Content-Type: application/json"
    print "Content-Length: %s" % len(json_output)
    print
    print json_output


Stopping Point
--------------

.. class:: big-centered

Let's take a break here, before continuing


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

FastCGI and SCGI are existing implementations of CGI in this fashion. The
Apache module **mod_python** offers a similar capability for Python code.

.. class:: incremental

* Each of these options has a specific API
* None are compatible with each-other
* Code written for one is **not portable** to another

.. class:: incremental

This makes it much more difficult to *share resources*


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
* Call the ``start_response`` method.
* Return an iterable of 0 or more strings, which are treated as the body of
  the response.


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


Simple WSGI Application
-----------------------

Where the simplified server above is **not** functional, this *is* a complete
app:

.. code-block:: python

    def application(environ, start_response)
        status = "200 OK"
        body = "Hello World\n"
        response_headers = [('Content-type', 'text/plain',
                             'Content-length', len(body))]
        start_response(status, response_headers)
        return [body]


WSGI Middleware
---------------

A third part of the puzzle is something called WSGI *middleware*

.. class:: incremental

* Middleware implements both the *server* and *application* interfaces
* Middleware acts as a server when viewed from an application
* Middleware acts as an application when viewed from a server

.. image:: img/wsgi_middleware_onion.png
    :align: center
    :width: 38%
    :class: incremental


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


The WSGI Environment
--------------------

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


The WSGI Environment
--------------------

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


The WSGI Environment
--------------------

.. class:: small

HTTP\_ Variables
  Variables corresponding to the client-supplied HTTP request headers (i.e.,
  variables whose names begin with "HTTP\_"). The presence or absence of these
  variables should correspond with the presence or absence of the appropriate
  HTTP header in the request.

.. class:: center incremental

**Seem Familiar?**


A Bit of Repetition
-------------------

Let's start simply.  We'll begin by repeating our first CGI exercise in WSGI

.. class:: incremental

* Find the ``wsgi`` directory in the class resources. Copy it to your working
  directory.
* Open the file ``wsgi_1.py`` in your text editor.
* We will fill in the missing values using the wsgi ``environ``, just as we
  use ``os.environ`` in cgi

.. class:: incremental center

**But First**


Orientation
-----------

.. code-block:: python
    :class: small

    if __name__ == '__main__':
        from wsgiref.simple_server import make_server
        srv = make_server('localhost', 8080, application)
        srv.serve_forever()

.. class:: incremental

Note that we pass our ``application`` function to the server factory

.. class:: incremental

We don't have to write a server, ``wsgiref`` does that for us.

.. class:: incremental

In fact, you should *never* have to write a WSGI server.


Orientation
-----------

.. code-block:: python
    :class: small

    def application(environ, start_response):
        response_body = body % (
             environ.get('SERVER_NAME', 'Unset'), # server name
                ...
             )
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html'),
                            ('Content-Length', str(len(response_body)))]
        start_response(status, response_headers)
        return [response_body]

.. class:: incremental

We do not define ``start_response``, the application does that.

.. class:: incremental

We *are* responsible for determining the HTTP status.


Running a WSGI Script
---------------------

You can run this script with python::

    $ python wsgi_1.py

.. class:: incremental

This will start a wsgi server. What host and port will it use?

.. class:: incremental

Point your browser at ``http://localhost:8080/``. Did it work?

.. class:: incremental

Go ahead and fill in the missing bits. Use the ``environ`` passed into
``application``


Some Tips
---------

Because WSGI is a long-running process, the file you are editing is *not*
reloaded after you edit it.

.. class:: incremental

You'll need to quit and re-run the script between edits.

.. class:: incremental

You may also want to consider using ``print environ`` in your application so
you can see the dictionary.

.. class:: incremental

If you do that, where will the printed environment appear?


A More Complex Example
----------------------

Let's create a multi-page wsgi application. It will serve a small database of
python books.

.. class:: incremental

The database (with a very simple api) can be found in ``wsgi/bookdb.py``

.. class:: incremental

* We'll need a listing page that shows the titles of all the books
* Each title will link to a details page for that book
* The details page for each book will display all the information and have a
  link back to the list


Some Questions to Ponder
------------------------

.. class:: incremental

When viewing our first wsgi app, do we see the name of the wsgi application
script anywhere in the URL?

.. class:: incremental

In our wsgi application script, how many applications did we actually have?

.. class:: incremental

How are we going to serve different types of information out of a single
application?


Dispatch
--------

We have to write an app that will map our incoming request path to some code
that can handle that request.

.. class:: incremental

This process is called ``dispatch``. There are many possible approaches

.. class:: incremental

Let's begin by designing this piece of it.

.. class:: incremental

Open ``bookapp.py`` from the ``wsgi`` folder.  We'll do our work here.


PATH
----

The wsgi environment gives us access to *PATH_INFO*, which maps to the URI the
user requested when they loaded the page.

.. class:: incremental

We can design the URLs that our app will use to assist us in routing.

.. class:: incremental

Let's declare that any request for ``/`` will map to the list page

.. container:: incremental

    We can also say that the URL for a book will look like this::
    
        http://localhost:8080/book/<identifier>

Writing resolve_path
--------------------

Let's write a function, called ``resolve_path`` in our application file.

.. class:: incremental

* It should take the *PATH_INFO* value from environ as an argument.
* It should return the function that will be called.
* It should also return any arguments needed to call that function.
* This implies of course that the arguments should be part of the PATH


My Solution
-----------

.. code-block:: python
    :class: small incremental

    def resolve_path(path):
        urls = [(r'^$', books),
                (r'^book/(id[\d]+)$', book)]
        matchpath = path.lstrip('/')
        for regexp, func in urls:
            match = re.match(regexp, matchpath)
            if match is None:
                continue
            args = match.groups([])
            return func, args
        # we get here if no url matches
        raise NameError


Application Updates
-------------------

We need to hook our new router into the application.

.. class:: incremental

* The path should be extracted from ``environ``.
* The router should be used to get a function and arguments
* The body to return should come from calling that function with those
  arguments
* If an error is raised by calling the function, an appropriate response
  should be returned
* If the router raises a NameError, the application should return a 404
  response


My Solution
-----------

.. code-block:: python
    :class: small incremental

    def application(environ, start_response):
        headers = [("Content-type", "text/html")]
        try:
            path = environ.get('PATH_INFO', None)
            if path is None:
                raise NameError
            func, args = resolve_path(path)
            body = func(*args)
            status = "200 OK"
        except NameError:
            status = "404 Not Found"
            body = "<h1>Not Found</h1>"
        except Exception:
            status = "500 Internal Server Error"
            body = "<h1>Internal Server Error</h1>"
        finally:
            headers.append(('Content-length', str(len(body))))
            start_response(status, headers)
            return [body]


Test Your Work
--------------

Once you've got your script settled, run it::

    $ python bookapp.py

.. class:: incremental

Then point your browser at ``http://localhost:8080/``

.. class:: incremental
    
* ``http://localhost/book/id3``
* ``http://localhost/book/id73/``
* ``http://localhost/sponge/damp``

.. class:: incremental

Did that all work as you would have expected?


Building the List
-----------------

The function ``books`` should return an html list of book titles where each
title is a link to the detail page for that book

.. class:: incremental

* You'll need all the ids and titles from the book database.
* You'll need to build a list in HTML using this information
* Each list item should have the book title as a link
* The href for the link should be of the form ``/book/<id>``


My Solution
-----------

.. code-block:: python
    :class: incremental small

    def books():
        all_books = DB.titles()
        body = ['<h1>My Bookshelf</h1>', '<ul>']
        item_template = '<li><a href="/book/{id}">{title}</a></li>'
        for book in all_books:
            body.append(item_template.format(**book))
        body.append('</ul>')
        return '\n'.join(body)


Test Your Work
--------------

Quit and then restart your application script::

    $ python bookapp.py

.. container:: incremental

    Then reload the root of your application::

        http://localhost:8080/

.. class:: incremental

You should see a nice list of the books in the database. Do you?

.. class:: incremental

Click on a link to view the detail page. Does it load without error?


Showing Details
---------------

The next step of course is to polish up those detail pages.

.. class:: incremental

* You'll need to retrieve a single book from the database
* You'll need to format the details about that book and return them as HTML
* You'll need to guard against ids that do not map to books

.. class:: incremental

In this last case, what's the right HTTP response code to send?


My Solution
-----------

.. code-block:: python
    :class: incremental small

    def book(book_id):
        page = """
    <h1>{title}</h1>
    <table>
        <tr><th>Author</th><td>{author}</td></tr>
        <tr><th>Publisher</th><td>{publisher}</td></tr>
        <tr><th>ISBN</th><td>{isbn}</td></tr>
    </table>
    <a href="/">Back to the list</a>
    """
        book = DB.title_info(book_id)
        if book is None:
            raise NameError
        return page.format(**book)


Revel in Your Success
---------------------

Quit and restart your script one more time

.. class:: incremental

Then poke around at your application and see the good you've made

.. class:: incremental

And your application is portable and sharable

.. class:: incremental

It should run equally well under any `wsgi server
<http://www.wsgi.org/en/latest/applications.html>`_


A Few Steps Further
-------------------

Next steps for an app like this might be:

* Create a shared full page template and incorporate it into your app
* Improve the error handling by emitting error codes other than 404 and 500
* Swap out the basic backend here with a different one, maybe a Web Service?
* Think about ways to make the application less tightly coupled to the pages
  it serves


Homework
--------

For your homework this week, you'll be creating a wsgi application of your
own.

.. class:: incremental

As the source of your data, use the mashup you created last week.

.. class:: incremental

Your application should have at least two separate "pages" in it.

.. class:: incremental

The HTML you produce does not need to be pretty, but it should be something
that shows up in a browser.


Submitting Your Homework
------------------------

To submit your homework:

.. class:: small

* Create a new python script in ``assignments/session04``. It should be
  something I can run with:

.. class:: small

::

    $ python your_script.py

.. class:: small

* Once your script is running, I should be able to view your application in my
  browser.

* Include all instructions I need to successfully run and view your script.

* Add tests for your code. I should be able to run the tests like so:

.. class:: small

::

    $ python tests.py

.. class:: small

* Commit your changes to your fork of the repo in github, then open a pull
  request.


Wrap-Up
-------

For educational purposes, you might wish to take a look at the source code for
the ``wsgiref`` module. It's the canonical example of a simple wsgi server

    >>> import wsgiref
    >>> wsgiref.__file__
    '/full/path/to/your/copy/of/wsgiref.py'
    ...

.. class:: incremental center

**See you Next Time**
