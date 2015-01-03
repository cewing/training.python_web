Course Outline
==============

This course takes place over 10 sessions. Each session is three hours long.
Each session contains lecture material and exercises you will type at a python
prompt. Each session has associated assignments which you will complete
between sessions.

Session 1 - TCP/IP and Sockets
------------------------------

We will begin with a disucssion of the fundamental concepts and structures
that underly the internet and networked computing. We'll learn about the
TCP/IP stack (Internet Protocol Suite) and gain some insights into how that
model manifests in real life. We will then dive into sockets and learn how to
use them to communicate between processes on a single machine, or across a
network.

Along the way, we'll build a basic Echo server and client to demonstrate the
processes we've learned. By the end of the session, we'll be sending messages
and receiving replies.

`Lecture Slides <presentations/session01.html>`_

References
**********

* `Python Library - socket <http://docs.python.org/2/library/socket.html>`_
* `Socket Programming How-to <http://docs.python.org/2/howto/sockets.html>`_
* `Python Module of the Week - socket <http://pymotw.com/2/socket/>`_


Session 2 - Web Protocols
-------------------------

Protocols are the languages of the Internet. They govern how machines speak to
one another. We will focus on finding both the similarities and differences
between protocols. Can you use the inherent qualities of each to determine
which is appropriate for a given purpose?

Along the way, we'll build a simple web server. Using the HTTP protocol and
extending what we learned in the previous session we'll create an HTTP server
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


Session 3 - APIs and Mashups
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

* `Lecture Slides <presentations/session03.html>`_
* `As Plain HTML <presentations/session03-plain.html>`_

References
**********

* `httplib <http://docs.python.org/2/library/httplib.html>`_
* `htmlparser <http://docs.python.org/2/library/htmlparser.html>`_
* `xmlrpclib <http://docs.python.org/2/library/xmlrpclib.html>`_
* `DocXMLRPCServer <http://docs.python.org/2/library/docxmlrpcserver.html>`_
* `json <http://docs.python.org/2/library/json.html>`_


Session 4 - CGI and WSGI
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

* `Lecture Slides <presentations/session04.html>`_
* `As Plain HTML <presentations/session04-plain.html>`_

Homework Tutorials
******************

Please walk through all three of these tutorials before session 5 begins.

* `Jinja2 Template Tutorial <presentations/template_tutorial-plain.html>`_
* `SQL Persistence Tutorial <presentations/sql_persistence_tutorial-plain.html>`_
* `Flask Walkthrough <presentations/lask_walkthrough-plain.html>`_


Session 5 - Frameworks and Flask
--------------------------------

In this class we learn about using frameworks to help us reach our goals. We
will learn what makes up a framework and some criteria for evaluating which is
the right one for you.

After an introduction to the idea of frameworks, we'll look at a specific
implementation of a *microframework*, `Flask <http://flask.pocoo.org/>`_.
We'll install the framework and take a look at how it works. What does it have
in common with work we've already done?

Finally, we'll spend our class implementing a simple application using Flask.
We'll decide the functionality we need, write tests to demonstrate that it
works, and then write the code to make the tests pass. When we finish, we'll
have a tested, simple app that we can view through the browser.

Along the way, we'll learn a bit about how flask operates in a real
application. We'll learn some more about the Jinja2 templating language, and
we'll learn to tie the transactions of our database interaction to the cycles
of request and response.

`Lecture Slides <presentations/session05.html>`_


Session 6 - A Flask Application
-------------------------------

During this class, we will explore the technique of `pair programming`_ in the
process of extending and improving our Flask application. Students will divide
into pairs and each pair will work together to implement one or more new
features for the Flask app we finished in the previous class.

Along the way, we'll gain insight into how to build a more complex Flask
application, how to integrate with existing front-end design frameworks, and
even how to use alternate storage strategies. Most importantly, we'll gain a
bit of experience in the workflow of a small team as we explore how to share
our work quickly across different environments.

.. _pair programming: http://en.wikipedia.org/wiki/Pair_programming

`Lecture Slides <presentations/session06.html>`_

Homework Tutorials
******************

Please walk through this tutorial before session 7 begins.

* `An Introduction to Django <presentations/django_intro-plain.html>`_


Session 7 - Basic Django
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

`Lecture Slides <presentations/session07.html>`_


Session 8 - Extending Django
----------------------------

During this session, we will continue our exploration of Django, and of pair
programming. Students will once again pair up and work together to implement
one or more feature extending the basic Django app we created previously.

Finally, we'll discuss some of the strengths and weaknesses of Django.  What
makes it a good choice for some projects but not for others.

`Lecture Slides <presentations/session08.html>`_


Session 9 - Intro to Pyramid
----------------------------

In this class we will look at a relative newcomer to the Python Web Framework
scene, Pyramid. Although the framework is a newcomer, it is represents a
combination of several projects, notably Repoze and Pylons, that have been
around for quite some time. In fact, the roots of Repoze go back to Zope, the
original Python web framework (and quite possibly the first web framework in
any language).

We will talk a bit about what makes Pyramid different from other web
frameworks. We will look at the specific problems that the creators of Pyramid
are looking to solve, and we will investigate how those decisions have
influenced the design of the framework.

Along the way, we'll learn how Pyramid works under the covers, and how this is
like and unlike other frameworks we've seen so far. We'll get started building
the Data Model and configuration structure for the wiki application we'll be 
completing in the next session.

And we'll continue focusing on test-driven development, specifying
functionality and writing tests to demostrate it before ever writing the code
that provides it.

`Lecture Slides <presentations/session09.html>`_


Session 10 - A Pyramid Application
----------------------------------

In this class we'll dive into building a real Pyramid application. We'll be
implementing a simple wiki, using traversal dispatch, ZODB persistence and
Chameleon templates. We'll get a chance to work with simple forms, see how
views work in Pyramid, and implement an ACL-based authorization scheme.

Along the way we'll be taking a good look at a very different templating
system, Chameleon. It grew out of Zope Page Templates (ZPT) and the Template
Attribute Language (TAL). It's chief advantage is that it provides structure
and variable interpolation via XML namespaced attributes. This allows you to 
write templates that load in a browser and look 'right' without needing the
framework to render them.

And we'll continue our drive for test-driven development by writing
tests that cover the functionality we want and then writing the code to make
them pass. 

By the end of the session, you'll have a fully functional wiki you can play
with. Maybe you'll use it to track the information you learned about Python
Web Development.

`Lecture Slides <presentations/session10.html>`_
