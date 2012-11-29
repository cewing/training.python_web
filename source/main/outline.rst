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

Assignment
**********

To be completed once I decide the right format.

Week 4 - CGI and WSGI
---------------------

**Date**: Jan. 29, 2013

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
