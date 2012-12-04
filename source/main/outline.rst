Course Outline
==============

Each week will have in-class lectures, lab time, and lightning talks.  There
will be recommended reading, additional reading for the curious, and an 
assignment to be completed.

Week 1 - Introduction and Sockets
---------------------------------

**Date**: Jan. 8, 2013

In this class, we will discuss the fundamental concepts and structures that
underly the internet and networked computing. We will learn about the TCP/IP
stack (Internet Protocol Suite) and gain insight into how that model is
manifested in real life. We will learn about sockets and how to use them to
communicate between processes on a single machine or across a network.

Our class laboratory will focus on creating a small server-client program that
demonstrates the use of sockets. We will install the server on our Virtual
Machines, and accomplish our first networked communication.

The class assignment will focus on extending our use of sockets to support a
more complex use-case.

Reading
*******

* `Wikipedia - Internet Protocol Suite
  <http://en.wikipedia.org/wiki/Internet_Protocol_Suite>`_
* `Kessler - TCP/IP (sections 1 and 2)
  <http://www.garykessler.net/library/tcpip.html>`_
* `Wikipedia - Domain Name System
  <http://en.wikipedia.org/wiki/Domain_Name_System>`_
* `Wikipedia - Internet Sockets
  <http://en.wikipedia.org/wiki/Internet_socket>`_
* `RFC 5321 - SMTP (Appendix D only)
  <http://tools.ietf.org/html/rfc5321#appendix-D>`_

References
**********

* `Python Library - socket
  <http://docs.python.org/release/2.6.5/library/socket.html>`_
* `Socket Programming How-to
  <http://docs.python.org/release/2.6.5/howto/sockets.html>`_
* `Python Library - smtplib
  <http://docs.python.org/release/2.6.5/library/smtplib.html>`_

Further Reading
***************

* `Wikipedia - Berkeley socket interface
  <http://en.wikipedia.org/wiki/Berkeley_sockets>`_ 
* `RFC 821 - SMTP (initial) <http://tools.ietf.org/html/rfc821>`_
* `RFC 5321 - SMTP (latest) <http://tools.ietf.org/html/rfc5321>`_

Bonus
*****

`ZeroMQ Guide, Chapter 1 <http://zguide.zeromq.org/chapter:1>`_: ZeroMQ is a
modern, advanced implementation of the socket concept. Read this to find out
what sockets can get up to these days.

Assignment
**********

To be completed once I decide the right format.

Week 2 - Web Protocols
----------------------

**Date**: Jan. 15, 2013

In this class we will discuss the various languages of the Internet. What
differentiates one protocol from another? How are they similar? How can you
use the inherent qualities of each to determine which is appropriate for a
given purpose?

The class laboratory will cover creating a simple web server. Using the HTTP
protocol and information we learned in week one about sockets, we'll create a
simple web server that allows us to look at files and directories on our own
computers.

The class assignment will be to extend the simple web server, adding the
ability to run dynamic processes and return the results to the client.

Reading
*******

Read through the list of Python Internet Protocols. If you don't know what a
protocol is for, look it up online. Think about their relationship to each
other, which are clients? Which are servers? Which clients talk to which
servers? 

`Python Standard Library Internet Protocols
<http://docs.python.org/release/2.6.5/library/internet.html>`_

An introduction to the HTTP protocol:
`HTTP Made Really Easy <http://www.jmarshall.com/easy/http/>`_

References
**********

Skim these before class, you'll need them for lab and your assignment:

* `ftplib <http://docs.python.org/release/2.6.5/library/ftplib.html>`_
* `httplib <http://docs.python.org/release/2.6.5/library/httplib.html>`_
* `urllib <http://docs.python.org/release/2.6.5/library/urllib.html>`_
* `urllib2 <http://docs.python.org/release/2.6.5/library/urllib2.html>`_

Bonus
*****

httplib2_ - A comprehensive HTTP client library that supports many features
left out of other HTTP libraries.

.. _httplib2: http://code.google.com/p/httplib2/

Skim these four documents from different phases of HTTP's life. Get a feel for
how the specification has changed (and how it hasn't!).

* `HTTP/0.9 <http://www.w3.org/Protocols/HTTP/AsImplemented.html>`_
* `HTTP - as defined in 1992 <http://www.w3.org/Protocols/HTTP/HTTP2.html>`
* `Hypertext Transfer Protocol -- HTTP/1.0
  <http://www.w3.org/Protocols/rfc1945/rfc1945>`
* `Hypertext Transfer Protocol -- HTTP/1.1
  <http://www.w3.org/Protocols/rfc2616/rfc2616>`

Week 3 - APIs and Mashups
-------------------------

**Date**: Jan. 22, 2013

In this class we will explore some of the ways that you can consume and
explore the data provided by other websites. Online data can be provided in
ways intended for consumption. But you can also use scraping techniques to get
at data the original author may not have considered valuable enough to present
as consumable.

We'll explore the use of tools like BeautifulSoup to help make sense of the
truly horrible HTML that can be found in the wild. We will also look at "Web
Services" formats like XMLRPC and REST so we can understand the ways in which
we can find data, or present it ourselves.  Finally, we'll look at some "Web
Service APIs" to help understand how to read them, and how to use them to get
at the data they provide.

Reading
*******

* `Wikipedia's take on 'Web Services'
  <http://en.wikipedia.org/wiki/Web_service>`_
* `xmlrpc overview <http://www.xmlrpc.com/>`_
* `xmlrpc spec (short) <http://www.xmlrpc.com/spec>`_
* `json overview and spec (short) <http://www.json.org/>`_
* `How I Explained REST to My Wife (Tomayko 2004)
  <http://tomayko.com/writings/rest-to-my-wife>`_
* `A Brief Introduction to REST (Tilkov 2007)
  <http://www.infoq.com/articles/rest-introduction>`_
* `Why HATEOAS - *a simple case study on the often ignored REST constraint*
  <http://www.slideshare.net/trilancer/why-hateoas-1547275#btnPrevious>`_

References
**********

Python Standard Libraries:
++++++++++++++++++++++++++

* `httplib <http://docs.python.org/release/2.6.5/library/httplib.html>`_
* `htmlparser <http://docs.python.org/release/2.6.5/library/htmlparser.html>`_
* `xmlrpclib <http://docs.python.org/release/2.6.5/library/xmlrpclib.html>`_
* `DocXMLRPCServer
  <http://docs.python.org/release/2.6.5/library/docxmlrpcserver.html>`_
* `json <http://docs.python.org/release/2.6.5/library/json.html>`_

External Eibraries:
+++++++++++++++++++

* BeautifulSoup_ - "You didn't write that awful page. You're just trying to
  get some data out of it. Right now, you don't really care what HTML is
  supposed to look like. Neither does this parser."

* httplib2_ - A comprehensive HTTP client library that supports many features
  left out of other HTTP libraries.

* restkit_ - an HTTP resource kit for Python. It allows you to easily access
  to HTTP resource and build objects around it.

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/
.. _httplib2: http://code.google.com/p/httplib2/
.. _restkit: https://github.com/benoitc/restkit/

SOAP
++++

* rpclib_ - a simple, easily extendible soap library that provides several
  useful tools for creating, publishing and consuming soap web services

* Suds_ - a lightweight SOAP python client for consuming Web Services.

* `the SOAP specification <http://www.w3.org/TR/soap/>`_

.. _rpclib: https://github.com/arskom/rpclib
.. _Suds: https://fedorahosted.org/suds/

Bonus
*****

* `Wikipedia on REST
  <http://en.wikipedia.org/wiki/Representational_State_Transfer>`
* `Original REST disertation
  <http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm>`

Assignment
**********

To be completed once I decide the right format.

Week 4 - CGI and WSGI
---------------------

**Date**: Jan. 29, 2013

Reading
*******

* `CGI tutorial`_ - Read the following sections: Hello World, Debugging, Form.
  Other sections optional. Follow along, hosting CGI scripts either via Apache
  on our VMs, or locally using CGIHTTPServer.

* `WSGI tutorial`_ - Follow along, hosting WSGI scripts either via Apache on our
  VMs, or locally using wsgiref.

.. _CGI tutorial: http://webpython.codepoint.net/cgi_tutorial
.. _WSGI tutorial: http://webpython.codepoint.net/wsgi_tutorial

Prepare for class:
++++++++++++++++++

* `CGI example scripts`_ - Use these examples to get started experimenting with
  CGI.

.. _CGI example scripts: http://fixme.crisewing.com

(https://github.com/briandorsey/uwpython_web/tree/master/week05/cgi_example)

References
**********

* `CGI module`_ - utilities for CGI scripts, mostly form and query string parsing
* `Parse URLS into components
  <http://docs.python.org/release/2.6.5/library/urlparse.html>`_
* `CGIHTTPServer`_ - python -m CGIHTTPServer
* `WSGI Utilities and Reference implementation
  <http://docs.python.org/release/2.6.5/library/wsgiref.html>`_
* `WSGI 1.0 specification <http://www.python.org/dev/peps/pep-0333/>`_
* `WSGI 1.0.1 (Python 3 support) <http://python.org/dev/peps/pep-3333/>`_
* `test WSGI server, like cgi.test()
  <http://hg.moinmo.in/moin/1.8/raw-file/tip/wiki/server/test.wsgi>`_

.. _CGI module: http://docs.python.org/release/2.6.5/library/cgi.html
.. _CGIHTTPServer: http://docs.python.org/release/2.6.5/library/cgihttpserver.html

Alternate WSGI introductions:
+++++++++++++++++++++++++++++

* `Getting Started with WSGI`_ - by Armin Ronacher 
* `very minimal introduction to WSGI
  <http://be.groovie.org/post/296349572/wsgi-and-wsgi-middleware-is-easy>`_

.. _Getting Started with WSGI: http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/

Assignment
**********

To be completed once I decide the right format.

Week 5 - Small Frameworks
-------------------------

**Date**: Feb. 5, 2013

Assignment
**********

To be completed once I decide the right format.

Week 6 - Django I / Relational DBs
----------------------------------

**Date**: Feb. 12, 2013

Assignment
**********

To be completed once I decide the right format.

Week 7 - Django II
------------------

**Date**: Feb. 19, 2013

Assignment
**********

To be completed once I decide the right format.

Week 8 - Pyramid / SqlAlchemy
-----------------------------

**Date**: Feb. 26, 2013

Assignment
**********

To be completed once I decide the right format.

Week 9 - Pyramid - ZODB
-----------------------

**Date**: Mar. 5, 2013

Assignment
**********

To be completed once I decide the right format.

Week 10 - Plone
---------------

**Date**: Mar. 12, 2013

Assignment
**********

To be completed once I decide the right format.
