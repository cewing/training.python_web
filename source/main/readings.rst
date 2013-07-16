Course Readings
===============

Web programming is a deep pool. There's more to cover than a one-week course
could ever hope to accomplish. To that end, I've compiled a list of related
readings that will support the information you'll learn in class. Think of
this as supplemental materials. You can read it at your leisure to help
increase both the depth and breadth of your knowledge.

The readings are organized like the class, by day, time and topic. 


Day 1 AM - TCP/IP and Sockets
-----------------------------

* `Wikipedia - Internet Protocol Suite
  <http://en.wikipedia.org/wiki/Internet_Protocol_Suite>`_
* `Kessler - TCP/IP (sections 1 and 2)
  <http://www.garykessler.net/library/tcpip.html>`_
* `Wikipedia - Domain Name System
  <http://en.wikipedia.org/wiki/Domain_Name_System>`_
* `Wikipedia - Internet Sockets
  <http://en.wikipedia.org/wiki/Internet_socket>`_
* `Wikipedia - Berkeley socket interface
  <http://en.wikipedia.org/wiki/Berkeley_sockets>`_

In addition, you may find it interesting to take a look at ZeroMQ, a
next-generation implementation of the socket concept built with parallel and
networked computing in mind:

* `ZeroMQ Guide, Chapter 1 <http://zguide.zeromq.org/py:all#Chapter-Basics>`_


Day 1 PM - Web Protocols
------------------------

* `Python Standard Library Internet Protocols
  <http://docs.python.org/2/library/internet.html>`_
* An introduction to the HTTP protocol: `HTTP Made Really Easy
  <http://www.jmarshall.com/easy/http/>`_

Python offers a number of external libraries that offer extended support for
covered web protocols, or support for protocols not covered in the Standard
Library:

* httplib2_ - A comprehensive HTTP client library that supports many features
  left out of other HTTP libraries.
* requests_ - "... an Apache2 Licensed HTTP library, written in Python, for
  human beings."
* paramiko_ - "a module for python 2.5 or greater that implements the SSH2
  protocol for secure (encrypted and authenticated) connections to remote
  machines"

.. _httplib2: http://code.google.com/p/httplib2/
.. _requests: http://docs.python-requests.org/en/latest/
.. _paramiko: http://docs.paramiko.org/

For a historical perspective on how protocols can change (as well as how they
remain unchanged) over time, skim these specifications for HTTP and SMTP:

* `HTTP/0.9 <http://www.w3.org/Protocols/HTTP/AsImplemented.html>`_
* `HTTP - as defined in 1992 <http://www.w3.org/Protocols/HTTP/HTTP2.html>`_
* `Hypertext Transfer Protocol -- HTTP/1.0
  <http://www.w3.org/Protocols/rfc1945/rfc1945>`_
* `Hypertext Transfer Protocol -- HTTP/1.1
  <http://www.w3.org/Protocols/rfc2616/rfc2616>`_

* `RFC 821 - SMTP (initial) <http://tools.ietf.org/html/rfc821>`_
* `RFC 5321 - SMTP (latest) <http://tools.ietf.org/html/rfc5321>`_


Day 2 AM - APIs and Mashups
---------------------------

* `Wikipedia's take on 'Web Services'
  <http://en.wikipedia.org/wiki/Web_service>`_
* `xmlrpc overview <http://www.xmlrpc.com/>`_
* `xmlrpc spec (short) <http://www.xmlrpc.com/spec>`_
* `the SOAP specification <http://www.w3.org/TR/soap/>`_
* `json overview and spec (short) <http://www.json.org/>`_
* `How I Explained REST to My Wife (Tomayko 2004)
  <http://tomayko.com/writings/rest-to-my-wife>`_
* `A Brief Introduction to REST (Tilkov 2007)
  <http://www.infoq.com/articles/rest-introduction>`_
* `Wikipedia on REST
  <http://en.wikipedia.org/wiki/Representational_State_Transfer>`
* `Original REST disertation
  <http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm>`
* `Why HATEOAS - *a simple case study on the often ignored REST constraint*
  <http://www.slideshare.net/trilancer/why-hateoas-1547275>`_

Python offers a number of solid external libraries to support Web Services, 
both from the side of production and consumption:

* BeautifulSoup_ - "You didn't write that awful page. You're just trying to
  get some data out of it. Right now, you don't really care what HTML is
  supposed to look like. Neither does this parser."
* httplib2_ - A comprehensive HTTP client library that supports many features
  left out of other HTTP libraries.
* rpclib_ - a simple, easily extendible soap library that provides several
  useful tools for creating, publishing and consuming soap web services
* Suds_ - a lightweight SOAP python client for consuming Web Services.
* restkit_ - an HTTP resource kit for Python. It allows you to easily access
  to HTTP resource and build objects around it.

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/
.. _httplib2: http://code.google.com/p/httplib2/
.. _rpclib: https://github.com/arskom/rpclib
.. _Suds: https://fedorahosted.org/suds/
.. _restkit: https://github.com/benoitc/restkit/


Day 2 PM - CGI and WSGI
-----------------------

* `CGI tutorial`_ - Read the following sections: Hello World, Debugging, Form.
  Other sections optional. Follow along using CGIHTTPServer.
* `WSGI tutorial`_ - Follow along using wsgiref.
* `CGI module`_ - utilities for CGI scripts, mostly form and query string
  parsing
* `Parse URLS into components
  <http://docs.python.org/release/2.6.5/library/urlparse.html>`_
* `CGIHTTPServer`_ - python -m CGIHTTPServer
* `WSGI Utilities and Reference implementation
  <http://docs.python.org/release/2.6.5/library/wsgiref.html>`_
* `WSGI 1.0 specification <http://www.python.org/dev/peps/pep-0333/>`_
* `WSGI 1.0.1 (Python 3 support) <http://python.org/dev/peps/pep-3333/>`_
* `test WSGI server, like cgi.test()
  <http://hg.moinmo.in/moin/1.8/raw-file/tip/wiki/server/test.wsgi>`_

.. _CGI tutorial: http://webpython.codepoint.net/cgi_tutorial
.. _WSGI tutorial: http://webpython.codepoint.net/wsgi_tutorial
.. _CGI module: http://docs.python.org/release/2.6.5/library/cgi.html
.. _CGIHTTPServer: http://docs.python.org/release/2.6.5/library/cgihttpserver.html

For alternative introductions to WSGI, try these two sources. They are a bit
more minimal and may be easier to comprehend off the bat.

* `Getting Started with WSGI`_ - by Armin Ronacher (really solid and quick!)
* `very minimal introduction to WSGI
  <http://be.groovie.org/2005/10/07/wsgi_and_wsgi_middleware_is_easy.html>`_

.. _Getting Started with WSGI: http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/


Day 3 AM - Frameworks and Flask
-------------------------------

* `Web Application Frameworks
  <http://en.wikipedia.org/wiki/Web_application_framework>`_

* `Jinja2 - Python page templates <http://jinja.pocoo.org/docs/>`_ - We'll
  learn something about templating in Python, starting with the Jinja2
  templating language. Focus primarily on the `templating documentation
  <http://jinja.pocoo.org/docs/templates/>`_, which provides a reasonable,
  non-technical introduction to the language and how it is used.

* `sqlite3 - DB API for sqlite3 <http://pymotw.com/2/sqlite3/index.html>`_ -
  We'll need a bit of familiarity with the sqlite3 module. How to open
  connections, execute queries, and read the results from a cursor. Just read
  the first two sections ('Creating a Database' and 'Retrieving Data').

* `Flask Documentation <http://flask.pocoo.org/docs/>`_ - Read the Foreward,
  Installation and Quickstart sections.

* `Unittest - Unit Testing Framework
  <http://docs.python.org/2/library/unittest.html>`_ - Starting in this module
  we'll begin writing tests to cover our code. Start learning how. For more,
  read the `Python Module of the Week on unittest
  <http://pymotw.com/2/unittest/index.html>`_

Flask is the microframework I've chosen as the subject of this course, but it
is by no means the only choice. A strong argument can be made in favor of any
of the following options, or even others. Your best bet is to experiment and
pick the one that fits your brain best.

* `Bottle <http://bottlepy.org/docs/dev/>`_: Python Web Framework.
* `CherryPy <http://www.cherrypy.org/>`_: A Minimalize Python Web Framework.
* `Web.py <http://webpy.org/>`_: Think about the ideal way to write a web app.
  Write the code to make it happen.
* `Aspen <http://aspen.io/>`_: A Python web framework that makes the most of
  the filesystem.