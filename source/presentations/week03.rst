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
``urllib2`` to handle this task (note that we've shortened the URL):

.. code-block:: python

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
it supports standard file read operations:

.. code-block:: python

    >>> html = page.read()
    >>> len(html)
    373447
    >>> print html

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

"Some people, when confronted with a problem, think 'I know, I'll use regular
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
way that will allow us to come back to it:

.. code-block:: python

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

    $ python virtualenv.py --distribute soupenv
    New python executable in soupenv/bin/python2.6
    Also creating executable in soupenv/bin/python
    Installing distribute........................
    .............................................
    ...done.

What Happened?
--------------

When you ran that file, a couple of things took place:

.. class:: incremental

* A new directory with your requested name was created
* A new Python executable was created in <ENV>/bin (<ENV>/Scripts on Windows)
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
it:

.. code-block:: python

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
``feedEntry``:

.. code-block:: python

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

.. code-block:: python

    for e in entries:
        anchor = e.find('a')
        paragraph = e.find('p', 'discreet')
        title = anchor.text.strip()
        url = anchor.attrs['href']
        print title
        print url
        try:
            print paragraph.text.strip()
        except AttributeError:
            print 'Uncategorized'
        print

.. class:: incremental

Watch for unicode encoding errors, I don't get any, but you might.

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

Short Break
-----------

While you are taking a short break, you might take a moment to sign up for 
the geocoding service we'll use later:

http://geoservices.tamu.edu/UserServices/Signup.aspx

You can also view your profile once you've signed up:

http://geoservices.tamu.edu/UserServices/Profile/ViewProfile.aspx

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

We can!  Enter XML-RPC (Remote Procedure Call)

.. class:: incremental

* Provides a set of defined procedures which can take arguments
* Calls are made via HTTP GET, by passing an XML document
* Returns from a call are sent to the client in XML

.. class:: incremental

Easier to demonstrate than explain

XML-RPC Example - Server
------------------------

xmlrpc_server.py:

.. code-block:: python
    :class: small

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

.. code-block:: python
    :class: small

    >>> import xmlrpclib
    >>> proxy = xmlrpclib.ServerProxy('http://localhost:50000', verbose=True)
    >>> proxy.multiply(3, 24)
    ...
    72

XML-RPC Request
---------------

``verbose=True`` allows us to see the request we sent:

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


More XML-RPC
------------

Register an entire Python class as a service, exposing class methods::

    server.register_instance(MyClass())

Keep an instance method private    :

.. code-block:: python
    :class: tiny

    class MyServiceClass(object):
        ...
        def public_method(self, arg1, arg2):
            """this method is public"""
            pass
        
        def _private_method(self):
            """this method is private because it starts with '_'
            """
            pass

XML-RPC Introspection
---------------------

First, implement required methods on your service class:

.. code-block:: python
    :class: tiny

    from SimpleXMLRPCServer import list_public_methods
    
    class MyServiceClass(object):
        ...
        def _listMethods(self):
            """custom logic for presenting method names to users
            
            list_public_methods is a convenience function from the Python 
            library, but you can make your own logic if you wish.
            """
            return list_public_methods(self)
        
        def _methodHelp(self, method):
            """provide help text for an individual method
            """
            f = getattr(self, method)
            return f.__doc__

XML-RPC Introspection
---------------------

Then enable introspection via the server instance:

.. code-block:: python
    :class: small

    server.register_introspection_functions()

After this, a client proxy can call pre-defined methods to learn about what
your service offers:

.. code-block:: python
    :class: small

    >>> for name in proxy.system.listMethods():
    ...     help = proxy.system.methodHelp(name)
    ...     print name
    ...     print "\t%s" % help
    ... 
    public_method
        this method is public

Introspection Question
----------------------

I told you when we added the ``_private_method`` that any method that any
method whose name starts with ``_`` would be **private**.

.. class:: incremental

But we also added a ``_listMethods`` method and a ``_methodHelp`` method and
*those* methods are listed when you run ``proxy.system.listMethods()``

.. class:: incremental

Why is this?

.. class:: incremental

For a complete discussion of this, read `this MOTW post`_

.. _this MOTW post: http://www.doughellmann.com/PyMOTW/SimpleXMLRPCServer/index.html#introspection-api

Beyond XML-RPC
--------------

.. class:: incremental

* XML-RPC allows introspection
* XML-RPC forces you to introspect to get information
* *Wouldn't it be nice to get that automatically?*
* XML-RPC provides data types
* XML-RPC provides only *certain* data types
* *Wouldn't it be nice to have an extensible system for types?*
* XML-RPC allows calling methods with parameters
* XML-RPC only allows calling methods, nothing else
* *wouldn't it be nice to have contextual data as well?*

.. class:: incremental center

**Enter SOAP: Simple Object Access Protocol**

SOAP
----

SOAP extends XML-RPC in a couple of useful ways:

.. class:: incremental

* It uses Web Services Description Language (WSDL) to provide meta-data about
  an entire service in a machine-readable format (Automatic introspection)

* It establishes a method for extending available data types using XML
  namespaces

* It provides a wrapper around method calls called the **envelope**, which
  allows the inclusion of a **header** with system meta-data that can be used
  by the application

SOAP in Python
--------------

There is no standard library module that supports SOAP directly.

.. class:: incremental

* The best-known and best-supported module available is **Suds**
* The homepage is https://fedorahosted.org/suds/
* It can be installed using ``easy_install`` or ``pip install``

Install Suds
------------

* Quit your python interpreter if you have it running.
* If you see (soupenv) at your command line prompt, cool.
* If you do not, type ``source /path/to/soupenv/bin/activate``
* Windows folks: ``> \path\to\soupenv\Scripts\activate``
* Once activated: ``pip install suds``

Creating a Suds Client
----------------------

Suds allows us to create a SOAP client object. SOAP uses WSDL to define a
service. All we need to do to set this up in python is load the URL of the
WSDL for the service we want to use:

.. code-block:: python
    :class: small

    (soupenv)$ python
    >>> from suds.client import Client
    >>> geo_client = Client('https://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderService_V03_01.asmx?wsdl')
    >>> geo_client
    <suds.client.Client object at 0x10041fc10>

Peeking at the Service
----------------------

Suds allows us to visually scan the service. Simply print the client object to
see what the service has to offer:

.. code-block:: python
    :class: small

    >>> print geo_client

    Suds ( https://fedorahosted.org/suds/ )  version: 0.4 GA  build: R699-20100913

    Service ( GeocoderService_V03_01 ) tns="https://geoservices.tamu.edu/"
       Prefixes (1)
          ns0 = "https://geoservices.tamu.edu/"
       Ports (2):
          (GeocoderService_V03_01Soap)
          Methods (4):
             ...
          Types (12):
             ...

Debugging Suds
--------------

Suds uses python logging to deal with debug information, so if you want to see
what's going on under the hood, you configure it via the Python logging
module:

.. code-block:: python

    >>> import logging
    >>> logging.basicConfig(level=logging.INFO)
    >>> logging.getLogger('suds.client').setLevel(logging.DEBUG)

.. class:: incremental

This will allow us to see the messages sent and received by our client.

Client Options
--------------

SOAP Servers can provide more than one *service* and each *service* might have
more than one *port*. Suds provides two ways to configure which *service* and
*port* you wish to use.  

Via subscription:

.. code-block:: python

    client.service['<service>']['<port>'].method(args)

Or the way we will do it, via configuration:

.. code-block:: python

    geo_client.set_options(service='GeocoderService_V03_01',
                           port='GeocoderService_V03_01Soap')

Providing Arguments
-------------------

Arguments to a method are set up as a dictionary.  Although some may not be 
required according to api documentation, it is safest to provide them all:

.. code-block:: python
    :class: small

    apiKey = '<fill this in>'
    args = {'apiKey': apiKey, }
    args['streetAddress'] = '1325 4th Avenue'
    args['city'] = 'Seattle'
    args['state'] = 'WA'
    args['zip'] = '98101'
    args['version'] = 3.01
    args['shouldReturnReferenceGeometry'] = True
    args['shouldNotStoreTransactionDetails'] = True
    args['shouldCalculateCensus'] = False
    args['censusYear'] = "TwoThousandTen"

Making the Call
---------------

Finally, once we've got the arguments all ready we can go ahead and make a call
to the server:

.. code-block:: python
    :class: small

    >>> res = geo_client.service.GeocodeAddressNonParsed(**args)
    DEBUG:suds.client:sending to 
    (https://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderService_V03_01.asmx)
    message:
    ...

What does it look like?
-----------------------

.. class:: tiny

::

    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:ns0="https://geoservices.tamu.edu/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
       <SOAP-ENV:Header/>
       <ns1:Body>
          <ns0:GeocodeAddressNonParsed>
             <ns0:streetAddress>1325 4th Avenue</ns0:streetAddress>
             <ns0:city>Seattle</ns0:city>
             <ns0:state>WA</ns0:state>
             <ns0:zip>98101</ns0:zip>
             <ns0:apiKey>a450a9181f85498598e21f8a39440e9a</ns0:apiKey>
             <ns0:version>3.01</ns0:version>
             <ns0:shouldCalculateCensus>false</ns0:shouldCalculateCensus>
             <ns0:censusYear>TwoThousandTen</ns0:censusYear>
             <ns0:shouldReturnReferenceGeometry>true</ns0:shouldReturnReferenceGeometry>
             <ns0:shouldNotStoreTransactionDetails>true</ns0:shouldNotStoreTransactionDetails>
          </ns0:GeocodeAddressNonParsed>
       </ns1:Body>
    </SOAP-ENV:Envelope>

And the Reply?
--------------

.. class:: tiny

::

    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
      <soap:Body>
        <GeocodeAddressNonParsedResponse xmlns="https://geoservices.tamu.edu/">
          <GeocodeAddressNonParsedResult>
            <TransactionId>6ef9c110-994c-4142-93d5-a55173526b64</TransactionId>
            <Latitude>47.6084110119244</Latitude>
            <Longitude>-122.3351592971042</Longitude>
            <Version>3.01</Version>
            <Quality>QUALITY_ADDRESS_RANGE_INTERPOLATION</Quality>
            <MatchedLocationType>LOCATION_TYPE_STREET_ADDRESS</MatchedLocationType>
            <MatchType>Exact</MatchType>
            <FeatureMatchingResultCount>1</FeatureMatchingResultCount>
            ...
            <FArea>2910.69420560356</FArea>
            <FAreaType>Meters</FAreaType>
            <FGeometrySRID>4269</FGeometrySRID>
            <FGeometry>&lt;?xml version="1.0" encoding="utf-8"?&gt;&lt;LineString xmlns="http://www.opengis.net/gml"&gt;&lt;posList&gt;-122.334868 47.608226 -122.335777 47.609219&lt;/posList&gt;&lt;/LineString&gt;</FGeometry>
            ...
          </GeocodeAddressNonParsedResult>
        </GeocodeAddressNonParsedResponse>
      </soap:Body>
    </soap:Envelope>

And What of Our Result?
-----------------------

The WSDL we started with should provide type definitions for both data we send
and results we receive. The ``res`` symbol we bound to our result earlier
should now be an instance of a *GeocodeAddressNonParsedResult*. Lets see what
that looks like:

.. code-block:: python

    >>> type(res)
    <type 'instance'>
    >>> dir(res)
    ['CensusTimeTaken', 'CensusYear', 'ErrorMessage', 'FArea',
     'FAreaType', 'FCity', 'FCounty', 'FCountySubRegion', 
     ...]
    >>> res.Latitude, res.Longitude
    (47.608411011924403, -122.3351592971042)

A Word on Debugging
-------------------

.. class:: center

**blerg**

.. class:: incremental

* Messages sent to the server are long XML strings
* Error messages are generally based on parsing errors in XML
* These error messages can be quite cryptic:
* "There is an error in XML document (1, 572). ---> The string '' is not a
  valid Boolean value.'

.. class:: incremental

Try this:

.. code-block:: python
    :class: small incremental

    >>> geo_client.last_sent().str().replace(" ","")[:573]
    '...</ns0:version>\n<ns0:shouldCalculateCensus/>'


Afterword
---------

SOAP (and XML-RPC) have some problems:

.. class:: incremental

* XML is pretty damned inefficient as a data transfer medium
* Why should I need to know method names?
* If I can discover method names at all, I have to read a WSDL to do it?

.. class:: incremental

Suds is the best we have, and it hasn't been updated since Sept. 2010.

If Not XML, Then What?
----------------------

.. class:: big-centered incremental

**JSON**

JSON
----

JavaScript Object Notation:

.. class:: incremental

* a lightweight data-interchange format
* easy for humans to read and write
* easy for machines to parse and generate

.. class:: incremental

Based on Two Structures:

.. class:: incremental

* object: ``{ string: value, ...}``
* array: ``[value, value, ]``

.. class:: center incremental

pythonic, no?

JSON Data Types
---------------

JSON provides a few basic data types (see http://json.org/):

.. class:: incremental

* string: unicode, anything but ", \\ and control characters
* number: any number, but json does not use octal or hexidecimal
* object, array (we've seen these above)
* true
* false
* null

.. class:: incremental center

**No date type? OMGWTF??!!1!1**

Dates in JSON
-------------

.. class:: incremental

Option 1 - Unix Epoch Time (number):

.. code-block:: python
    :class: small incremental

    >>> import time
    >>> time.time()
    1358212616.7691269

.. class:: incremental

Option 2 - ISO 8661 (string):

.. code-block:: python
    :class: small incremental

    >>> import datetime
    >>> datetime.datetime.now().isoformat()
    '2013-01-14T17:18:10.727240'

JSON in Python
--------------

You can encode python to json, and decode json back to python:

.. code-block:: python
    :class: small

    >>> import json
    >>> array = [1,2,3]
    >>> json.dumps(array)
    >>> orig = {'foo': [1,2,3], 'bar': u'my resumé', 'baz': True}
    >>> encoded = json.dumps(orig)
    >>> encoded
    '{"baz": true, "foo": [1, 2, 3], "bar": "my resum\\u00e9"}'
    >>> decoded = json.loads(encoded)
    >>> decoded == orig
    True

.. class:: incremental

Customizing the encoder or decoder class allows for specialized serializations

JSON in Python
--------------

the json module also supports reading and writing to *file-like objects* via 
``json.dump(fp)`` and ``json.load(fp)`` (note the missing 's')

.. class:: incremental

Remember duck-typing. Anything with a ``.write`` and a ``.read`` method is
*file-like*

.. class:: incremental

Have we seen any network-related classes recently that behave that way?

What about WSDL?
----------------

SOAP was invented in part to provide completely machine-readable
interoperability.

.. class:: incremental

Does that really work in real life?

.. class:: incremental center

Hardly ever

What about WSDL?
----------------

Another reason was to provide extensibility via custom types

.. class:: incremental

Does that really work in real life?

.. class:: incremental center

Hardly ever

Why Do All The Work?
--------------------

So, if neither of these goals is really achieved by using SOAP, why pay all
the overhead required to use the protocol?

.. class:: incremental

Enter REST

REST
----

.. class:: center

Representational State Transfer

.. class:: incremental

* Originally described by Roy T. Fielding (did you read it?)
* Use HTTP for what it can do
* Read more in `this book
  <http://www.crummy.com/writing/RESTful-Web-Services/>`_\*

.. class:: image-credit incremental

\* Seriously. Buy it and read
(<http://www.crummy.com/writing/RESTful-Web-Services/)

A Comparison
------------

The XML-RCP/SOAP way:

.. class:: incremental small

* POST /getComment HTTP/1.1
* POST /getComments HTTP/1.1
* POST /addComment HTTP/1.1
* POST /editComment HTTP/1.1
* POST /deleteComment HTTP/1.1

.. class:: incremental

The RESTful way:

.. class:: incremental small

* GET /comment/<id> HTTP/1.1
* GET /comment HTTP/1.1
* POST /comment HTTP/1.1
* PUT /comment/<id> HTTP/1.1
* DELETE /comment/<id> HTTP/1.1

ROA
---

This is **Resource Oriented Architecture**

.. class:: incremental

The URL represents the *resource* we are working with

.. class:: incremental

The HTTP Verb represents the ``action`` to be taken

.. class:: incremental

The HTTP Code returned tells us the ``result`` (whether success or failure)

HTTP Codes Revisited
--------------------

.. class:: small

POST /comment HTTP/1.1  (creating a new comment):

.. class:: incremental small

* Success: ``HTTP/1.1 201 Created``
* Failure (unauthorized): ``HTTP/1.1 401 Unauthorized``
* Failure (NotImplemented): ``HTTP/1.1 405 Not Allowed``
* Failure (ValueError): ``HTTP/1.1 406 Not Acceptable``

.. class:: small incremental

PUT /comment/<id> HTTP/1.1 (edit comment):

.. class:: incremental small

* Success: ``HTTP/1.1 200 OK``
* Failure: ``HTTP/1.1 409 Conflict``

.. class:: small incremental

DELETE /comment/<id> HTTP/1.1 (delete comment):

.. class:: incremental small

* Success: ``HTTP/1.1 204 No Content``

HTTP Is Stateless
-----------------

No individual request may be assumed to know anything about any other request.

.. class:: incremental

All the required information for to represent the possible actions to take
*should be present in either the request or the response*.

.. class:: incremental big-centered

Thus:  HATEOAS

HATEOAS
-------

.. class:: big-centered

Hypermedia As The Engine Of Application State

Applications are State Engines
------------------------------

A State Engine is a machine that provides *states* for a resource to be in and
*transitions* to move resources between states.  A Restful api should:

.. class:: incremental

* provide information about the current state of a resource
* provide information about available transitions for that resource (URIs)
* provide all this in each HTTP response

Playing With REST
-----------------

Let's take a moment to play with REST.

.. class:: incremental

We tried geocoding with SOAP.  Let's repeat the exercise with a REST/JSON API

.. class:: incremental center

**Back to your interpreter**

Geocoding with Google APIs
--------------------------

https://developers.google.com/maps/documentation/geocoding

.. code-block:: python
    :class: small incremental

    >>> import urllib
    >>> import urllib2
    >>> from pprint import pprint
    >>> base = 'http://maps.googleapis.com/maps/api/geocode/json'
    >>> addr = '1325 4th Ave, Seattle, WA 98101'
    >>> data = {'address': addr, 'sensor': False }
    >>> query = urllib.urlencode(data)
    >>> res = urllib2.urlopen('?'.join([base, query]))
    >>> response = json.load(res)
    >>> pprint(response)

RESTful Job Listings
--------------------

https://github.com/mattnull/techsavvyapi

.. code-block:: python
    :class: small incremental

    >>> base = 'http://api.techsavvy.io/jobs'
    >>> search = 'python+web'
    >>> res = urllib2.urlopen('/'.join([base, search]))
    >>> response = json.load(res)
    >>> type(response)
    <type 'dict'>
    >>> response.keys()
    [u'count', u'data']
    >>> response['count']
    50
    >>> for post in response['data']:
    ...   for key in sorted(post.keys()):
    ...     print "%s:\n    %s" % (key, post[key])
    ...   print
    ... 

Lab 2 - Mashup
--------------

Some of the job postings from our TechSavvy api returned lat/lon pairs.

Google provides a reverse address lookup service via the geocoding api
(https://developers.google.com/maps/documentation/geocoding/#ReverseGeocoding)

Create a list of job postings, with an address for those postings that provide
the needed data

.. class:: incremental center

**GO**

Assignment
----------

Using what you've learned this week, create a more complex mashup of some data
that interests you. Map the locations of the breweries near your house. Chart
a multi-axial graph of the popularity of various cities across several
categories.  Visualize the most effective legislators in Congress.  You have
interests, the Web has tools.  Put them together to make something.

Submitting the Assignment
-------------------------

Place the following in the ``assignments/week03/athome`` directory and make a
pull request:

.. class:: small

A textual description of your mashup (README.txt).
  What data sources did you scan, what tools did you use, what is the
  outcome you wanted to create?

.. class:: small

Your source code (mashup.py).
  Give me an executable python script that I can run to get output.

.. class:: small

Any instructions I need.
  If I need instructions beyond 'python mashup.py' to get the right
  output, let me know.
