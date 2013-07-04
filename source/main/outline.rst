Course Outline
==============

This course is five days long. Each day is split into morning and afternoon
sessions. Each session will consist of three or so hours of instruction and
exercises and a couple of short breaks.

Day 1 AM - TCP/IP and Sockets
-----------------------------

We will begin by covering basic front-matter for the course: daily schedule,
class protocol, introductions and such. Next we will move into a disucssion of
the fundamental concepts and structures that underly the internet and
networked computing. We will learn about the TCP/IP stack (Internet Protocol
Suite) and gain some insights into how that model manifests in real life. We
will then dive into sockets and learn how to use them to communicate between
processes on a single machine, or across a network.

Along the way, we'll build a basic Echo server and client to demonstrate the
processes we've learned. By lunch, we'll be sending messages and receiving 
replies.

`Lecture Slides <presentations/session01.html>`_

References
**********

* `Python Library - socket <http://docs.python.org/2/library/socket.html>`_
* `Socket Programming How-to <http://docs.python.org/2/howto/sockets.html>`_
* `Python Module of the Week - socket <http://pymotw.com/2/socket/>`_


Day 1 PM - Web Protocols
------------------------

Protocols are the languages of the Internet. They govern how machines speak to
one-another. We will focus on finding both the similarities and differences
between protocols. Can you use the inherent qualities of each to determine
which is appropriate for a given purpose?

Along the way, we'll build a simple web server. Using the HTTP protocol and
extending what we learned in the morning about we'll create an HTTP server
that allows us to serve files and directories from our own computers. By the
end of the day, you'll be browsing your filesystem with your own web browser.

`Lecture Slides <presentations/session02.html>`_

References
**********

* `smtplib <http://docs.python.org/2/library/smtplib.html>`_
* `imaplib <http://docs.python.org/2/library/imaplib.html>`_
* `httplib <http://docs.python.org/2/library/httplib.html>`_
* `urllib <http://docs.python.org/2/library/urllib.html>`_
* `urllib2 <http://docs.python.org/2/library/urllib2.html>`_

If you have more curiosity about other Python Standard Library implementations
of internet protocols, you should read Doug Hellmann's Python Module Of The
Week on `Internet Protocols and Support`_. His entries on these libraries are
clear and concise and have some great code examples.

.. _Internet Protocols and Support: http://pymotw.com/2/internet_protocols.html


Day 2 AM - APIs and Mashups
---------------------------

The internet is a treasure trove of information. But meaning can be hard to
find among all that data. Mashups offer a way to combine data from disparate
sources in order to derive meaning. Data online can be offered in forms ripe
for consumption. APIs built in XMLRPC, SOAP or REST offer rich tools for
extraction, but even simple websites can be scraped using tools like
BeautifulSoup.

We'll explore the differences between various 'Web Services' formats, learning
how to serve information and consume it. We'll also explore using BeautifulSoup
to help extract information from the sea of HTML in the wild.

Along the way, we'll create a mashup of our own, using the tools we learn to
build a script that can produce derived meaning out of data we find online.

`Lecture Slides <presentations/session03.html>`_

References
**********

* `httplib <http://docs.python.org/2/library/httplib.html>`_
* `htmlparser <http://docs.python.org/2/library/htmlparser.html>`_
* `xmlrpclib <http://docs.python.org/2/library/xmlrpclib.html>`_
* `DocXMLRPCServer <http://docs.python.org/2/library/docxmlrpcserver.html>`_
* `json <http://docs.python.org/2/library/json.html>`_


Day 2 PM - CGI and WSGI
-----------------------

In this class we will explore ways of moving data from HTTP requests into the
dynamic scripts that process data. We will begin by looking at the original
specification for passing data, CGI (Common Gateway Interface). We'll look at
the benefits and drawbacks of the specification, and use it to create some
simple interactions.

Then we will investigate a more modern take on the same problem, WSGI (Web
Services Gateway Interface). We'll see the ways in which WSGI is similar to
CGI, and look at the ways in which it differs. We'll create a simple interaction
using WSGI and see what benefits and drawbacks it confers.

`Week 4 Presentation <presentations/week04.html>`_

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
~~~~~~~~~~~~~~~~~~

* `CGI example scripts`_ - Use these examples to get started experimenting with
  CGI.

.. _CGI example scripts: https://github.com/cewing/training.python_web/tree/master/assignments/week04/lab/cgi-bin

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Getting Started with WSGI`_ - by Armin Ronacher (really solid and quick!)
* `very minimal introduction to WSGI
  <http://be.groovie.org/2005/10/07/wsgi_and_wsgi_middleware_is_easy.html>`_

.. _Getting Started with WSGI: http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/


Day 3 AM - Intro to Flask
-------------------------

In this class we learn about using frameworks to help us reach our goals. We
will learn what makes up a framework and some criteria for evaluating which is
the right one for you.

This week we will also learn about the final project for the class and students
will begin to think about what they wish to do to complete the project.

In our class lab we will explore using a specific framework (Flask) to create
a simple web application. We'll learn how to install the framework, how to
read the documentation for it, how to build a simple dynamic application, and
how to push further on.

For our assignment we will extend our knowledge by trying out a different
framework. We will have the chance to repeat the class lab, or create another
dynamic system using one of the many other python web frameworks available to
us.

`Week 5 Presentation <presentations/week05.html>`_

Reading
*******

* `Web Application Frameworks
  <http://en.wikipedia.org/wiki/Web_application_framework>`_
* `Flask Documentation <http://flask.pocoo.org/docs/>`_ - Read the Foreward,
  Installation and Quickstart sections.
* `Unittest - Unit Testing Framework
  <http://docs.python.org/2.6/library/unittest.html>`_ - We will be writing
  tests from here forward. Start learning how.

Please also skim this:

* `sqlite3 - DB API for sqlite3
  <http://www.doughellmann.com/PyMOTW/sqlite3/index.html>`_ - We'll need a bit
  of familiarity with the sqlite3 module. How to open connections, execute
  queries, and read the results from a cursor. Just read the first two
  sections ('Creating a Database' and 'Retrieving Data').

Before Class
************

* Install Flask in a virtualenv on your local machine.
* Walk through the examples in the Quickstart section.
* You can play with the tutorial if you want. We'll be doing this in class as
  our lab work
  
Reference
*********

* `Bottle: Python Web Framework <http://bottlepy.org/docs/dev/>`_
* `CherryPy: A Minimalize Python Web Framework <http://www.cherrypy.org/>`_
* `Web.py: Think about the ideal way to write a web app. Write the code to
  make it happen. <http://webpy.org/>`_

These are only a few of the many python web frameworks available in the
'microframework' class. I offer these resources as a starting point. For your
assignment, pick one of these to work with, or select one from the list at the
python wiki below. **Do Not Use Django or Pyramid**. We will be covering those
specifically in class.

* `Python Web Frameworks <http://wiki.python.org/moin/WebFrameworks>`_

You may also want to do more reading on the unittest module:

* `PyMOTW - unittest
  <http://www.doughellmann.com/PyMOTW/unittest/index.html>`_


Day 3 PM - A Flask Application
------------------------------

In this class we'll get introduced to arguably the most popular full-stack
Python web framework, Django. We'll build a simple application that introduces
us to the basics of Models, Views and Templates.  We'll also learn about the 
Django admin and how it can help us rapidly develop effective applications.

We'll cover basic relational modeling and talk about how to create effective
database schemas to model real-world problems.  We'll take a look at how the 
Django ORM (and ORMs in general) can help shield Python developers from SQL.

For our homework, we'll take a look at a set of specifications for a project
and create a set of Django Models that will fulfill the specification.

`Week 6 Presentation <presentations/week06.html>`_

Reading
*******

* `Django at a Glance
  <https://docs.djangoproject.com/en/1.4/intro/overview/>`_ - introduction to
  the concepts and execution of Django

* `Quick Install Guide
  <https://docs.djangoproject.com/en/1.4/intro/install/>`_ - lightweight
  instructions on installing Django. Use Python 2.6, not 2.5.    

* `Django Tutorial, part 1
  <https://docs.djangoproject.com/en/1.4/intro/tutorial01/>`_ - as noted
  below, please actually follow the steps in the tutorial up until you reach
  *Creating Models*

Before Class
************

* Install Django 1.4.3. Use a Virtualenv and pip or easy_install. (see the
  installation quick-start above, and the more in-depth guide below)

* Install an RDBMS (I personally recommend PostgreSQL, but MySQL or any other
  will do. We can even live with sqlite3, so long as you understand it is
  **not for production**)

* Set up a Django project. Walk through the first part of the tutorial above
  until you reach *Creating Models*. **Do Not** create models)

Reference
*********

* `Using Django <https://docs.djangoproject.com/en/1.4/topics/>`_ - far more
  in-depth information about core topics in Django. Pay particular attention
  to the installation documentation here.

* `Django Design Philosophies
  <https://docs.djangoproject.com/en/dev/misc/design-philosophies/>`_ - some
  well-considered words on why Django is the way it is.

Day 4 AM - Intro to Django
--------------------------

In this class we'll dive a bit further into Django. We'll start with a
duplicate of the micro-blog we built in week 5 and work in teams to extend the
functionality by integrating existing apps. Along the way, we'll have a chance
to explore team-based development workflow.

Finally, we'll discuss some of the strengths and weaknesses of Django.  What 
makes it a good choice for some projects but not for others.

Our assignment for the week will be to prepare for working with Pyramid in
Week 8.

`Week 7 Presentation <presentations/week07.html>`_

Reading
*******

* `Using Django <https://docs.djangoproject.com/en/1.4/topics/>`_ - far more
  in-depth information about core topics in Django. Pay attention specifically
  to the following topics (you'll want to follow links in these documents):

  * `Models <https://docs.djangoproject.com/en/1.4/topics/db/models/>`_ -
    details of the django modelling system. How to represent data for,
    relationships between and the presentation of your objects.

  * `Queries <https://docs.djangoproject.com/en/1.4/topics/db/queries/>`_ -
    basic information about the Django ORM and how to use it to create,
    retrieve, update and delete objects.

  * `Working with Forms
    <https://docs.djangoproject.com/en/1.4/topics/forms/>`_ - how to create,
    display, and process forms in Django, including forms that are associated
    with a given model.

  * `The Django Template Language
    <https://docs.djangoproject.com/en/1.4/topics/templates/>`_ - learn
    template basics like variables, filters, tags and blocks, and learn about
    template inheritance.

  * `Class-based Generic Views
    <https://docs.djangoproject.com/en/1.4/topics/class-based-views/>`_ - an
    introduction to the simplest way to present your objects to your adoring
    public.

  * `Testing Django Applications
    <https://docs.djangoproject.com/en/1.4/topics/testing/>`_ - learn
    different approaches to testing Django applications, including unit
    testing and doctests.

Reference
*********

* `SQLAlchemy and You <http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/>`_
  - A really in-depth look at the differences between the Django ORM and the
  reigning king of Python database integration, SQLAlchemy.

* `About Django from the Pyramid Guy
  <http://www.djangocon.us/schedule/presentations/22/>`_ - a talk given at
  DjangoCon 2012 by Chris McDonough, one of the driving forces behind the
  Pyramid framework. Also available in `video form
  <http://www.youtube.com/watch?v=eN7h6ZbzMy0>`_.


Day 4 PM - A Django Application
-------------------------------

Day 5 AM - Intro to Pyramid
---------------------------

This week we will look at a relative newcomer to the Python Web Framework
scene, Pyramid. Although the framework is a newcomer, it is represents a
combination of several projects, notably Repoze and Pylons, that have been
around for quite some time. In fact, the roots of Repoze go back to Zope, the
original Python web framework (and quite possibly the first web framework in
any language).

We will talk a bit about what makes Pyramid different from other web
frameworks. We will look at the specific problems that the creators of Pyramid
are looking to solve, and we will investigate how those decisions have
influenced the design of the framework.

We'll specifically look at two technologies that set the Pyramid framework
apart: the ZODB and URL Traversal.  We'll do this by implementing a wiki using
these technologies and then discuss what might make such tools appealing to a
certain type of project.

We'll also look at a very different templating system, Chameleon, which grew
out of Zope Page Templates and the Template Attribute Language. Chameleon
provides code structures via XML namespaces, allowing you to write templates
that will load in a browser looking like HTML without needing a framework to
render them.

`Week 8 Presentation <presentations/week08.html>`_

Reading
*******

Why you should care about `Traversal
<http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/muchadoabouttraversal.html>`_.

Compare and contrast forms of dispatch in Pyramid:

* `URL Route Dispatch
  <http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/urldispatch.html>`_
* `Object Traversal
  <http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/traversal.html>`_

Learn a bit about the `ZODB <http://zodb.org/index.html>`_

* Read the `tutorial <http://zodb.org/documentation/tutorial.html>`_ for a
  quick overview of usage (don't actually do it, though).
* Read the `more complete walk-through here
  <http://zodb.org/documentation/articles/ZODB1.html>`_ altough, again, do not
  actually do the code examples.
* Learn about `object references in the ZODB
  <http://blog.startifact.com/posts/older/a-misconception-about-the-zodb.html>`_
  - one of its greatest strengths.

Learn a bit about the Chameleon ZPT templating language:

* Read about `Chameleon Templates in Pyramid
  <http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/templates.html#chameleon-zpt-templates>`_
* A `Quick Intro to TAL <https://weblion.psu.edu/trac/weblion/wiki/TAL>`_

* `Chameleon Documentation <https://chameleon.readthedocs.org/en/latest/>`_ 

In particular, pay attention to:

* `Basics (TAL)
  <https://chameleon.readthedocs.org/en/latest/reference.html#basics-tal>`_
* `Expressions (TALES)
  <https://chameleon.readthedocs.org/en/latest/reference.html#expressions-tales>`_


References
**********

* `The ZODB Book <http://zodb.readthedocs.org/en/latest/>`_ - A work in
  progress by Carlos De La Guardia.

* The `ZPT Appendix <http://docs.zope.org/zope2/zope2book/AppendixC.html>`_ to
  the Zope Book

* Read `Defending Pyramid's Design
  <http://docs.pylonsproject.org/projects/pyramid/en/latest/designdefense.html>`_
  - an excellent point-by-point explanation of the design decisions that went
  into creating this framework.



Day 5 PM - A Pyramid Application
--------------------------------
