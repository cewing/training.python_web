.. slideconf::
    :autoslides: False

Course Outline
==============

.. slide:: Course Outline
    :level: 1

    This document contains no slides.

This course takes place over 10 sessions. Each session is three hours long.
Each session contains lecture material and exercises you will type at a python
prompt. Each session has associated assignments which you will complete
between sessions.


Session 1 - MVC Applications and Data Persistence
-------------------------------------------------

In this session we will begin by introducing the idea of an MVC (*Model View
Controller*) application.  We'll discuss this popular application design
pattern and talk about the ways in which it does and does not apply to the
world of web applications.

We'll get started with our first application, a learning journal written in the
lignt but powerful *Pyramid* web framework. We'll set up a development
environment and install the framework and dependencies. We'll create our first
*models* and experiment with persisting data to a database.

References
**********


Preparation for Session 2
*************************

In preparation for session 2, please read the following materials:

* `Jinja2 Template Tutorial
  <presentations/template_tutorial-plain.html>`_
* `HTML5 Site Layout Tutorial
  <http://www.smashingmagazine.com/2009/08/04/designing-a-html-5-layout-from-scratch/>`_

Session 2 - Pyramid Views, Renderers and Forms
----------------------------------------------

In this session we extend our understanding of the MVC design pattern by
learning how Pyramid implements the *view* and *controller* aspects.

Pyramid *views* represent the *controller* part of the MVC pattern, and we'll
create a number of them. We'll also learn how Pyramid uses *routes* to properly
connect the *path* requested by a client to the *views* run by a server.

We'll meet with Pyramid's *renderers*, the *view* in MVC.  We'll start by using
a built-in renderer that simply turns view data into strings sent back to the
client as plain text responses.  We'll then install a template-based renderer
and use the *jinja2* template language to create visible HTML pages the brower
can load to show our learning journal entries.

Prepraration for Session 3
**************************

In preparation for session 3, please read up on getting started with `Heroku
and Python`_.  We'll be deploying our learning journal to Heroku by the end of
that session.

.. _Heroku and Python: https://devcenter.heroku.com/articles/getting-started-with-python#introduction

Sesstion 3 - Pyramid Authentication and Deployment
--------------------------------------------------

In this session we will learn the basic elements of access control:
authentication and authorization. We'll learn how Pyramid implements these two
aspects of security, and will implement a basic security policy for our
learning journal.

Once complete, we will deploy our application to Heroku.  We'll make a few
changes to how our app is configured to fit with the Heroku model and will be
able to see our application in action by the end of the session.

Time permitting, we will enhance our application with a few special features
such as Markdown formatting, and code highlighting. A list of potential future
enhancements will give you plenty to think about for the rest of the week.

Session 4 - TCP/IP and Sockets
------------------------------

We will continue with a disucssion of the fundamental concepts and structures
that underly the internet and networked computing. We'll learn about the
TCP/IP stack (Internet Protocol Suite) and gain some insights into how that
model manifests in real life. We will then dive into sockets and learn how to
use them to communicate between processes on a single machine, or across a
network.

Along the way, we'll build a basic Echo server and client to demonstrate the
processes we've learned. By the end of the session, we'll be sending messages
and receiving replies.

References
**********

* `Python Library - socket <http://docs.python.org/2/library/socket.html>`_
* `Socket Programming How-to <http://docs.python.org/2/howto/sockets.html>`_
* `Python Module of the Week - socket <http://pymotw.com/2/socket/>`_


Session 5 - Web Protocols
-------------------------

Protocols are the languages of the Internet. They govern how machines speak to
one another. We will focus on finding both the similarities and differences
between protocols. Can you use the inherent qualities of each to determine
which is appropriate for a given purpose?

Along the way, we'll build a simple web server. Using the HTTP protocol and
extending what we learned in the previous session we'll create an HTTP server
that allows us to serve files and directories from our own computers. By the
end of the day, you'll be browsing your filesystem with your own web browser.

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


Session 6 - APIs and Mashups
----------------------------

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

References
**********

* `httplib <http://docs.python.org/2/library/httplib.html>`_
* `htmlparser <http://docs.python.org/2/library/htmlparser.html>`_
* `xmlrpclib <http://docs.python.org/2/library/xmlrpclib.html>`_
* `DocXMLRPCServer <http://docs.python.org/2/library/docxmlrpcserver.html>`_
* `json <http://docs.python.org/2/library/json.html>`_


Session 7 - CGI and WSGI
------------------------

In this class we will explore ways of moving data from HTTP requests into the
dynamic scripts that process data. We will begin by looking at the original
specification for passing data, CGI (Common Gateway Interface). We'll look at
the benefits and drawbacks of the specification, and use it to create some
simple interactions.

Then we will investigate a more modern take on the same problem, WSGI (Web
Services Gateway Interface). We'll see the ways in which WSGI is similar to
CGI, and look at the ways in which it differs. We'll create a simple interaction
using WSGI and see what benefits and drawbacks it confers.

Preparation for Session 8
*************************

Please walk through this tutorial before session 8 begins.

* `An Introduction to Django <presentations/django_intro-plain.html>`_


Session 8 - Basic Django
------------------------

In this class we'll get introduced to arguably the most popular full-stack
Python web framework, Django. We'll install the framework, learn about how to
get it running and how to get started creating your very own app.

We'll be learning about the Django ORM and how Django Models can help shield
developers from much of the complexity of SQL.

During the week leading up to this session, we'll `get started building`_ a
blog app in Django. We'll learn how to use the tools Django provides to explore
and interact with your models while designing them. We'll also get a brief
introduction to the Django admin, Django's *killer feature*.

.. _get started building: presentations/django_intro-plain.html


Along the way, we'll build a nicely functional blog application.  We'll learn
about model relationships, customizing the Django admin, and adding front-end
views so users can see our work. We'll even learn how we can update our
database code and keep it in sync with our progressing development work.

Along the way we'll learn that the Django template language is quite similar
to the Jinja2 language (in fact, Jinja2 was modelled on the Django version).
We'll also get a chance to learn a bit more about the features that the Django
test framework provides over and above the standard Python ``unittest``
library.


Session 9 - Extending Django
----------------------------

During this session, we will continue our exploration of Django, and of pair
programming. Students will once again pair up and work together to implement
one or more feature extending the basic Django app we created previously.

Finally, we'll discuss some of the strengths and weaknesses of Django.  What
makes it a good choice for some projects but not for others.

`Lecture Slides <presentations/session08.html>`_


Session 10 - Deploying Django
-----------------------------


