Internet Programming with Python
================================

.. image:: img/granny_mashup.png
    :align: left
    :width: 50%

Week 3: Scraping, APIs and Mashups

.. class:: intro-blurb

Wherein we learn how to make order from the chaos of the wild internet.

.. class:: image-credit

image: Paul Downey http://www.flickr.com/photos/psd/492139935/ - CC-BY

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

HTML

Ideally
-------

::

    <!DOCTYPE html>
    <html>
      <head>
      </head>
      <body>
        <p>A nice clean paragraph</p>
        <p>And another nice clean paragraph</p>
      </body>
    </html>

Yeah, Right
-----------

.. class:: big-centered

Is it ever actually like that?

HTML... IRL
-----------

::

    <html>
     <form>
      <table>
       <td><input name="input1">Row 1 cell 1
       <tr><td>Row 2 cell 1
      </form>
      <td>Row 2 cell 2<br>This</br> sure is a long cell
     </body>
    </html>

FFFFFFFFFUUUUUUUUUUUUU
----------------------

.. image:: img/scream.jpg
    :align: center
    :width: 32%

.. class:: image-credit

Photo by Matthew via Flickr (http://www.flickr.com/photos/purplemattfish/3918004964/) - CC-BY-NC-ND

The Law of The Internet
-----------------------

.. class:: big-centered

"Be strict in what you send and tolerant in what you receive"

But What If...
--------------

.. class:: incremental

You have some information you want to get from online.

.. class:: incremental

You really want to organize this information in some interesting way

.. class:: incremental

You *really really* don't want to spend the next three weeks cutting and
pasting

Web Scraping
------------

.. class:: big-centered

Let Python do the job for you.  Fire up your interpreter!

First Steps
-----------

First, you need to get a web page.  Let's use this one (a list of recent
blog posts about Django and PostgreSQL):

.. class:: center incremental

http://crisewing.com/cover/++contextportlets++ContentWellPortlets.BelowPortletManager3/open-source-posts/full_feed

First Steps - Get Source
------------------------

Let's start by grabbing the page we want. We use the Python Standard Library
``urllib2`` to handle this task (note that we've shortened the URL)::

    >>> import urllib2
    >>> page = urllib2.urlopen('http://tinyurl.com/osfeeds')
    >>> page
    <addinfourl at 4302170088 whose fp = <socket._fileobject object at 0x1005c6410>>
    >>> page.code
    200
    >>> page.headers['content-type']
    'text/html;charset=utf-8'
    >>> page.headers['content-length']
    '373447'

First Steps - Read Source
-------------------------

We can take the page we just opened, and read it. The object is file-like, so
it supports standard file read operations::

    >>> html = page.read()
    >>> len(page)
    373447
    >>> print page

    <!DOCTYPE html PUBLIC
      "-//W3C//DTD XHTML 1.0 Transitional//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
    ...
    </html>

Now What?
---------

**Goal**: Sort the blog post titles and URLs into two lists, one for Django
and one for PostgreSQL

What tools do we have to do this job?

.. class:: incremental

* String Methods?
* Regular Expressions?

Brief Interlude
---------------

.. class:: big-centered

"Some people, when confronted with a problem, think 'I know, I'ʹll use regular
expressions.' Now they have two problems."

Even Better
-----------

Read this excellent rant (during break):

http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454

But Really
----------

.. class:: center

So what *do* we use?

.. class:: incremental center

Special-purpose Parsers

.. class:: incremental center

Enter **BeautifulSoup**

Step Back for a Moment
----------------------

This is going to take some preparation, so let's set aside our html page in a
way that will allow us to come back to it::

    >>> fh = open('bloglist.html', 'w')
    >>> fh.write(html)
    >>> fh.close()

Now the page is saved to a file in your current working directory.

.. class:: incremental

**Quit your interpreter**

Virtualenv
----------

We are about to install a non-standard library.

.. class:: incremental

* As a real-world developer you need to do this a lot
* As a web developer you need to install *different* versions of the *same*
  library
* For every non-standard library installed into a System Python, the gods kill
  a kitten
* Use Virtualenv...
* **Always**

Getting Virtualenv
------------------

Three options for installing virtualenv (this is the exception to the above
rule):

* ``pip install virtualenv``
* ``easy_install virtualenv``

These both demand that you first install something else. If you haven't
already got ``pip`` or ``easy_install`` try this way instead:

* download ``https://raw.github.com/pypa/virtualenv/master/virtualenv.py``
* remember where it goes.  You'll need it

Creating a Virtualenv
---------------------

Creating a new virtualenv is very very simple::

    $ python virtualenv.py [options] <ENV>

<ENV> is just the name of the environment you want to create. It's arbitrary.
Let's make one for our BeautifulSoup install::

    $ python virtualanv.py --distribute soupenv
    New python executable in fooenv/bin/python2.6
    Also creating executable in fooenv/bin/python
    Installing distribute........................
    .............................................
    ...done.

What Happened?
--------------

When you ran that file, a couple of things took place:

.. class:: incremental

* A new directory with your requested name was created
* A new Python executable was created in <ENV>/bin
* The new Python was cloned from the Python used to run the file
* The new Python was isolated from any libraries installed in the old Python
* Distribute (a newer, better setuptools) was installed so you have ``easy_install``
* Pip was installed so you have ``pip``

.. class:: incremental

Cool, eh?  Learn more at http://www.virtualenv.org

Using Virtualenv
----------------

To install new libraries into a virtualenv, the easiest process is to first
activate the env::

    $ source soupenv/bin/activate
    (soupenv)$ which python
    /path/to/soupenv/bin/python

Or, on Windows::

    > \path\to\soupenv\Scripts\activate

.. class:: image-credit

If you use Powershell, read the note here:
http://www.virtualenv.org/en/latest/#activate-script

Install BeautifulSoup
---------------------

Once the virtualenv is activated, you can simply use pip or easy_install to
install the libraries you want::

    (soupenv)$ pip install beautifulsoup4


Choose a Parsing Engine
-----------------------

BeautifulSoup is built to use the Python HTMLParser.

.. class:: incremental

* Batteries Included.  It's already there
* It kinda sucks, especially before Python 2.7.3

.. class:: incremental

BeautifulSoup also supports using other parsers. Let's install one. There are
two decent choices: ``lxml`` and ``html5lib``.

.. class:: incremental

``lxml`` is better, but harder to install.  Let's use ``html5lib`` today.

Install a Parsing Engine
------------------------

Again, this is pretty simple::

    (soupenv)$ pip install html5lib

Once that is installed, BeautifulSoup will choose it instead of the standard
library module.

Parsing HTML
------------

Okay, we're all set here. Let's load up our HTML page and get ready to scrape
it::

    (soupenv)$ python
    >>> fh = open('bloglist.html', 'r')
    >>> from bs4 import BeautifulSoup
    >>> parsed = BeautifulSoup(fh)
    >>>

And that's it.  The document is now parsed and ready to scrape.

Scraping HTML
-------------

The next step is to figure out what it is from the HTML page that you want to
scrape.

.. class:: incremental

**Goal**: Sort the blog post titles and URLs into two lists, one for Django
and one for PostgreSQL

.. class:: incremental

What tools do we have to allow us to look at the source and find our targets?

HTML Inspection Demo
--------------------

We can use the developer tools that come in Safari, Chrome and IE, or use the 
Firebug extension to FireFox.

.. class:: incremental

So, we need to find ``<div>`` elements with the class ``feedEntry``.

Searching Your Soup
-------------------

BeautifulSoup has parsed our document

.. class:: incremental

* A parsed document acts like a ``tag``
* A ``tag`` can be searched using the ``find_all`` method
* The ``find_all`` method searches the descendents of the tag on which it is
  called.
* The ``find_all`` method takes arguments which act as *filters* on the search
  results

.. class:: incremental

| like so: 
| 
| ``tag.find_all(name, attrs, recursive, text, limit, **kwargs)``

Searching by CSS Class
----------------------

The items we are looking for are ``div`` tags which have the CSS class
``feedEntry``::

    >>> entries = parsed.find_all('div', class_='feedEntry')
    >>> len(entries)
    106

.. class:: incremental

| If you pass a simple string as the sole value to the ``attrs`` argument, that
  string is treated as a CSS class: 
| 
| ``parsed.find_all('div', 'feedEntry')``

Find a Single Match
-------------------

What bits of an entry have the details we need to meet our goals?

.. class:: incremental

* A ``tag`` also has a ``find`` method which returns only the **first** match
* ``tag.find(name, attrs, recursive, text, **kwargs)``
* In each entry, the first ``<a>`` has title and URL
* In each entry, the first ``<p>`` with the class ``discreet`` has the source
  of the feed (Planet Django or Planet PostgreSQL)

Testing it out
--------------

::

    >>> for e in entries:
    ...     anchor = e.find('a')
    ...     paragraph = e.find('p', 'discreet')
    ...     title = anchor.text.strip()
    ...     url = anchor.attrs['href']
    ...     print title
    ...     print url
    ...     try:
    ...         print paragraph.text.strip()
    ...     except AttributeError:
    ...         print 'Uncategorized'
    ...     print
    ...     
    >>>

Lab 1 - 20 mins
---------------

* Write a function, take a BeautifulSoup object as the sole argument
* find all the 'feedEntry' divs in the page
* Get the title and url of the entry and put them in a dictionary
* Categorize an entry as ``pgsql``, ``django`` or ``other``
* It should return three lists of categorized entries

| Call it like so:
| 
|   ``pgsql, django, other = my_function(parsed_page)``

.. class:: incremental center

**GO**

Another Approach
----------------

Scraping web pages is inherently brittle

.. class:: incremental

The owner of the website updates their layout, your code breaks

.. class:: incremental

But there is another way to get information from the web in a more normalized
fashion

.. class:: incremental center

**Web Services**

Web Services
------------

"a software system designed to support interoperable machine-to-machine
interaction over a network" - W3C

.. class:: incremental

* provides a defined set of calls
* returns structured data

Classifying Web Services
------------------------

Web services can be classified in a couple of ways: 

.. class:: incremental

* By how they are implemented (XML-RPC, SOAP, REST)

* By what they return (XML, JSON)

Early Web Services
------------------

RSS is one of the earliest forms of Web Services

* First known as ``RDF Site Summary``
* Became ``Really Simple Syndication``
* More at http://www.rss-specification.com/rss-specifications.htm

.. class:: incremental

A single web-based *endpoint* provides a dynamically updated listing of
content

.. class:: incremental

Implemented in pure HTTP.  Returns XML 

.. class:: incremental

**Atom** is a competing, but similar standard

RSS Document
------------

.. class:: tiny

::

    <?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
    <channel>
      <title>RSS Title</title>
      <description>This is an example of an RSS feed</description>
      <link>http://www.someexamplerssdomain.com/main.html</link>
      <lastBuildDate>Mon, 06 Sep 2010 00:01:00 +0000 </lastBuildDate>
      <pubDate>Mon, 06 Sep 2009 16:45:00 +0000 </pubDate>
      <ttl>1800</ttl>

      <item>
        <title>Example entry</title>
        <description>Here is some text containing an interesting description.</description>
        <link>http://www.wikipedia.org/</link>
        <guid>unique string per item</guid>
        <pubDate>Mon, 06 Sep 2009 16:45:00 +0000 </pubDate>
      </item>
      ...
    </channel>
    </rss>

XML-RPC
-------

If we can provide a single endpoint that returns a single data set (RSS), can
we also allow *calling procedures* at an endpoint?

.. class:: incremental

We can!  Enter XML-RPC

.. class:: incremental

* Provides a set of defined procedures which can take arguments
* Calls are made via HTTP GET, by passing an XML document
* Returns from a call are sent to the client in XML

.. class:: incremental

Easier to demonstrate than explain

XML-RPC Example - Server
------------------------

xmlrpc_server.py:

.. class:: small

::

    from SimpleXMLRPCServer import SimpleXMLRPCServer
    
    server = SimpleXMLRPCServer(('localhost', 50000))
    
    def multiply(a, b):
        return a * b
    server.register_function(multiply)
    
    try:
        print "Use Ctrl-C to Exit"
        server.serve_forever()
    except KeyboardInterrupt:
        print "Exiting"

XML-RPC Example - Client
------------------------

We can run a client from a terminal. First, open one terminal and run the
xmlrpc_server.py script:

    $ python xmlrcp_server.py

Then, open another terminal and start up python:

.. class:: small

::

    >>> import xmlrpclib
    >>> proxy = xmlrpclib.ServerProxy('http://localhost:50000', verbose=True)
    >>> proxy.multiply(3, 24)
    ...
    72

XML-RPC Request
---------------

``verbose=True``, allows us to see the request we sent:

.. class:: tiny

::

    POST /RPC2 HTTP/1.0
    Host: localhost:50000
    User-Agent: xmlrpclib.py/1.0.1 (by www.pythonware.com)
    Content-Type: text/xml
    Content-Length: 192
    
    <?xml version='1.0'?>
    <methodCall>
     <methodName>multiply</methodName>
     <params>
      <param>
       <value><int>3</int></value>
      </param>
      <param>
       <value><int>24</int></value>
      </param>
     </params>
    </methodCall>

XML-RPC Response
----------------

and we can see the response, too:

.. class:: tiny

::

    HTTP/1.0 200 OK
    Server: BaseHTTP/0.3 Python/2.6.1
    Date: Sun, 13 Jan 2013 03:38:00 GMT
    Content-type: text/xml
    Content-length: 121

    <?xml version='1.0'?>
    <methodResponse>
     <params>
      <param>
       <value><int>72</int></value>
      </param>
     </params>
    </methodResponse>


scraps
------


web services

rss/atom feeds

xml-rpc

soap

rest

lab

scrape the latest news stories from reddit front page and sort titles by
category. Omit NSFW stories if present

assignment

find two web services (or one webservice and a web page to scrape), combine
the information you can get from them into a mashup.

resource: http://www.programmableweb.com/
