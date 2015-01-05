.. slideconf::
    :autoslides: False

Course Readings
===============

.. slide:: Course Readings
    :level: 1

    This document contains no slides.

Web programming is a deep pool. There's more to cover than a 10-session course
could ever hope to accomplish. To that end, I've compiled a list of related
readings that will support the information you'll learn in class. Think of
this as supplemental materials. You can read it at your leisure to help
increase both the depth and breadth of your knowledge.

The readings are organized like the class, by session and topic. 


Session 1 - MVC Applications and Data Persistence
-------------------------------------------------

As we'll be learning about Pyramid over the first three sessions, please take
some time to read and digest some of the `copious documentation`_ for thie
powerful framework.

In particular, to cover the topics we address in this session you'll want to
read the following:

* `Pyramid Configuration
  <http://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html>`_
* `Defending Pyramid's Design
  <http://docs.pylonsproject.org/projects/pyramid/en/latest/designdefense.html>`_

.. _copious documentation: http://docs.pylonsproject.org/projects/pyramid/en/latest/index.html

You may also wish to read a bit about `SQLAlchemy`_.  In particular you may
want to work through the `Object Relational Tutorial`_ to get a more complete
understanding of how the SQLAlchemy ORM works.

.. _SQLAlchemy: http://docs.sqlalchemy.org/en/rel_0_9/
.. _Object Relational Tutorial: http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html


Session 2 - Pyramid Views, Renderers and Forms
----------------------------------------------

Sesstion 3 - Pyramid Authentication and Deployment
--------------------------------------------------

Session 4 - TCP/IP and Sockets
------------------------------

* `Wikipedia - Internet Protocol Suite
  <http://en.wikipedia.org/wiki/Internet_Protocol_Suite>`_
* `Kessler - TCP/IP (sections 1 and 2)
  <http://www.garykessler.net/library/tcpip.html>`_
* `Wikipedia - Domain Name System
  <http://en.wikipedia.org/wiki/Domain_Name_System>`_
* `Wikipedia - Internet Sockets
  <http://en.wikipedia.org/wiki/Network_socket>`_
* `Wikipedia - Berkeley socket interface
  <http://en.wikipedia.org/wiki/Berkeley_sockets>`_

If you want to know a bit more about the lower layers of the stack, you might
find the following readings enlightening:

**Transport Layer**

* `Wikipedia - Universal Datagram Protocol (UDP)
  <http://en.wikipedia.org/wiki/User_Datagram_Protocol>`_
* `Wikipedia - Transmission Control Protocol (TCP)
  <http://en.wikipedia.org/wiki/Transmission_Control_Protocol>`_

**Internet Layer**

* `Wikipedia - Internet Protocol (IP)
  <http://en.wikipedia.org/wiki/Internet_Protocol>`_
* `Wikipedia - IPv4 Packet Structure
  <http://en.wikipedia.org/wiki/IPv4#Packet_structure>`_
* `Wikipedia - IPv6 Packet Structure
  <http://en.wikipedia.org/wiki/IPv6_packet#Fixed_header>`_

**Link Layer**

* `Wikipedia - Link Layer Protocols
  <http://en.wikipedia.org/wiki/Link_Layer#Link_layer_protocols>`_

In addition, you may find it interesting to take a look at ZeroMQ, a
next-generation implementation of the socket concept built with parallel and
networked computing in mind:

* `ZeroMQ Guide, Chapter 1 <http://zguide.zeromq.org/py:all#Chapter-Basics>`_


Session 5 - Web Protocols
-------------------------

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


Session 6 - APIs and Mashups
----------------------------

* `Introduction to HTML (from the Mozilla Developer Network)
  <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction>`_
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
  <http://en.wikipedia.org/wiki/Representational_State_Transfer>`_
* `Original REST disertation
  <http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm>`_
* `Why HATEOAS - *a simple case study on the often ignored REST constraint*
  <http://www.slideshare.net/trilancer/why-hateoas-1547275>`_

Python offers a number of solid external libraries to support Web Services, 
both from the side of production and consumption:

* BeautifulSoup_ - "You didn't write that awful page. You're just trying to
  get some data out of it. Right now, you don't really care what HTML is
  supposed to look like. Neither does this parser."
* requests_ - HTTP for humans
* httplib2_ - A comprehensive HTTP client library that supports many features
  left out of other HTTP libraries.
* rpclib_ - a simple, easily extendible soap library that provides several
  useful tools for creating, publishing and consuming soap web services
* Suds_ - a lightweight SOAP python client for consuming Web Services.
* restkit_ - an HTTP resource kit for Python. It allows you to easily access
  to HTTP resource and build objects around it.

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/
.. _requests: http://docs.python-requests.org/en/latest/
.. _httplib2: http://code.google.com/p/httplib2/
.. _rpclib: https://github.com/arskom/rpclib
.. _Suds: https://fedorahosted.org/suds/
.. _restkit: https://github.com/benoitc/restkit/


Session 7 - CGI and WSGI
------------------------

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


Sessions 8, 9, & 10 - Django
----------------------------

Though it's way too much to read in any one sitting (or even in 10 or 20), the
Django documentation is excellent and thorough. As a start, take a look at
these sections:

* `Django at a Glance
  <https://docs.djangoproject.com/en/1.7/intro/overview/>`_ - introduction to
  the concepts and execution of Django

* `Quick Install Guide
  <https://docs.djangoproject.com/en/1.7/intro/install/>`_ - lightweight
  instructions on installing Django. Use Python 2.7.

* `Django Tutorial <https://docs.djangoproject.com/en/1.7/intro/tutorial01/>`_
  - The tutorial covers many of the same concepts we will in class. Go over it
  to re-enforce the lessons you learn

* `Using Django <https://docs.djangoproject.com/en/1.7/topics/>`_ - far more
  in-depth information about core topics in Django. In particular, the
  installation instructions here can be helpful when you run into trouble.

Bookmark the `Django Documentation homepage
<https://docs.djangoproject.com/en/1.7/>`_. It really is "everything you need
to know about Django"

When you have some time, read `Django Design Philosophies
<https://docs.djangoproject.com/en/dev/misc/design-philosophies/>`_ - for some
well-considered words on why Django is the way it is.

Conversely, for some well-considered criticisms of Django and the way it is,
read this in-depth comparison of SQLAlchemy and the Django ORM by the creator
of Flask: `SQLAlchemy and You <http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/>`_

Or consider viewing `this video <http://www.youtube.com/watch?v=eN7h6ZbzMy0>`_
of a talk given at DjangoCon 2012 by Chris McDonough, one of the driving
forces behind the Pyramid framework.
