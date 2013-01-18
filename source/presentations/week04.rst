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

