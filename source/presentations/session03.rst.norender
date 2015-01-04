Python Web Programming
======================

.. image:: img/granny_mashup.png
    :align: left
    :width: 50%

Session 3: Scraping, APIs and Mashups

.. class:: intro-blurb

Wherein we learn how to make order from the chaos of the wild internet.

.. class:: image-credit

image: Paul Downey http://www.flickr.com/photos/psd/492139935/ - CC-BY


A Dilemma
---------

The internet makes a vast quantity of data available.

.. class:: incremental

But not always in the form or combination you want.

.. class:: incremental

It would be nice to be able to combine data from different sources to create
*meaning*.


The Big Question
----------------

.. class:: big-centered

But How?


The Big Answer
--------------

.. class:: big-centered

Mashups


Mashups
-------

A mashup is:

    a web page, or web application, that uses and combines data, presentation
    or functionality from two or more sources to create new services.

.. class:: image-credit

definition courtsey of `wikipedia
<http://en.wikipedia.org/wiki/Mashup_(web_application_hybrid)>`_


Data Sources
------------

The key to mashups is the idea of data sources.

.. class:: incremental

These come in many flavors:

.. class:: incremental

* Simple websites with data in HTML
* Web services providing structured data
* Web services providing tranformative service (geocoding)
* Web services providing presentation (mapping)


HTML Sources
------------

It would be nice if all online data were available in well-structured formats.

.. class:: incremental

The reality is that much data is available only in HTML.

.. class:: incremental

Still we can get at it, with some effort.

.. class:: incremental

By scraping the data from the web pages.


HTML, Ideally
-------------

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


Taming the Mess
---------------

Luckily, there's a tool to help with this:  ``BeautifulSoup``.

.. class:: incremental

BeautifulSoup is a great tool, but it's not in the Standard Library. We'll
need to install it.

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

.. class:: incremental small

* ``pip install virtualenv``
* ``easy_install virtualenv``

.. class:: incremental

You must have ``pip`` or ``easy_install`` installed.  Try this:

.. class:: incremental small

::

    $ curl -O \
    https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.tar.gz
    $ tar -xzvf virtualenv-1.11.tar.gz

.. class:: incremental

* remember where it goes.  You'll need it
* there is a copy in the class resources (``resources/common``)


Creating a Virtualenv
---------------------

Creating a new virtualenv is very very simple:

.. class:: small

::

    $ python virtualenv.py [options] <ENV>
    <or>
    $ virtualenv [options] <ENV>

.. container:: incremental small

    <ENV> is just the name of the environment you want to create. It's
    arbitrary. Let's make one for our BeautifulSoup install::

        $ python virtualenv.py soupenv
        Using real prefix '/Users/cewing/newpythons/parts/opt'
        New python executable in soupenv26/bin/python2.6
        Also creating executable in soupenv26/bin/python
        Installing setuptools, pip...done.


What Happened?
--------------

When you ran that file, a couple of things took place:

.. class:: incremental

* A new directory with your requested name was created
* A new Python executable was created in <ENV>/bin (<ENV>/Scripts on Windows)
* The new Python was cloned from the Python used to run the file
* The new Python was isolated from any libraries installed in the old Python
* Setuptools was installed so you have ``easy_install`` for this new python
* Pip was installed so you have ``pip`` for this new python

.. class:: incremental

Cool, eh?  Learn more at http://www.virtualenv.org


Using Virtualenv
----------------

To install new libraries into a virtualenv, first activate the env::

    $ source soupenv/bin/activate
    (soupenv)$ which python
    /path/to/soupenv/bin/python

Or, on Windows::

    > \path\to\soupenv\Scripts\activate

.. class:: image-credit

If you use Powershell, read the note here:
http://www.virtualenv.org/en/latest/virtualenv.html#activate-script


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
* It's not great, especially before Python 2.7.3

.. class:: incremental

BeautifulSoup also supports using other parsers.

.. class:: incremental

There are two good choices: ``lxml`` and ``html5lib``.

.. class:: incremental

``lxml`` is better, but much harder to install.  Let's use ``html5lib``.


Install a Parsing Engine
------------------------

Again, this is pretty simple::

    (soupenv)$ pip install html5lib

.. class:: incremental

Once installed, BeautifulSoup will choose it automatically.

.. class:: incremental

BeautifulSoup will choose the "best" available.

.. class:: incremental

You can specify the parser if you need to for some reason.


Install Requests
----------------

Python provides tools for opening urls and communicating with servers. It's
spread across the ``urllib`` and ``urllib2`` packages.

.. class:: incremental

These packages have pretty unintuitive APIs.

.. class:: incremental

The ``requests`` library is becoming the de-facto standard for this type of
work.  Let's install it too.

.. class:: incremental

::

    (soupenv)$ pip install requests


Our Class Mashup
----------------

We're going to build a mashup together today.

.. class:: incremental

It will give us an annotated list of apartment rentals, so the next time we
have to move, we can find the exact right place.

.. class:: incremental

We'll start by getting a raw list of apartment rentals from today's canonical
source:

.. class:: incremental

Craigslist

.. class:: incremental

Open a new file in your editor: ``mashup.py``.


Examine the Source
------------------

Craigslist doesn't have an api, just a website, so we'll need to dig a bit

.. class:: incremental

By going to the website and playing with the form there, we can derive a
formula for a search URL

.. class:: incremental

* Base URL: ``http://seattle.craigslist.org/search/apa``
* keywords: ``query=keyword+values+here``
* price: ``minAsk=NNN maxAsk=NNN``
* bedrooms: ``bedrooms=N`` (N in range 1-8)

.. class:: incremental

We'll make an HTTP request with these parameters


Opening URLs with Requests
--------------------------

In ``requests``, each HTTP method has a module-level function:

.. class:: incremental

* ``GET`` == ``requests.get(url, **kwargs)``
* ``POST`` == ``requests.post(url, **kwargs)``
* ...

.. class:: incremental

``kwargs`` represent other parts of an HTTP request:
    
.. class:: incremental

* ``params``: a dict of url parameters (?foo=bar&baz=bim)
* ``headers``: a dict of headers to send with the request
* ``data``: the body of the request, if any (form data for POST goes here)
* ...


Getting Responses with Requests
-------------------------------

The return value from one of these functions is a ``response`` which provides:

.. class:: incremental

* ``response.status_code``: see the HTTP Status Code returned
* ``response.ok``: True if ``response.status_code`` is not an error
* ``response.raise_for_status()``: call to raise a python error if it is
* ``response.headers``: The headers sent from the server
* ``response.text``: Body of the response, decoded to unicode
* ``response.encoding``: The encoding used to decode
* ``response.content``: The original encoded response body as bytes

.. class:: incremental small

``requests documentation``: http://docs.python-requests.org/en/latest/

Fetch Search Results
--------------------

We'll start by writing a function ``fetch_search_results``

.. class:: incremental

* It will accept one keyword argument for each of the possible query values
* It will build a dictionary of request query parameters from incoming keywords
* It will make a request to the craigslist server using this query
* It will return the body of the response if there is no error
* It will raise an error if there is a problem with the response

.. class:: incremental

Try writing this function. Put it in ``mashup.py``


My Solution
-----------

Here's the one I created:

.. code-block:: python
    :class: small incremental

    import requests

    def fetch_search_results(
        query=None, minAsk=None, maxAsk=None, bedrooms=None
    ):
        incoming = locals().copy()
        base = 'http://seattle.craigslist.org/search/apa'
        search_params = dict(
            [(key, val) for key, val in incoming.items() 
                        if val is not None])
        if not search_params:
            raise ValueError("No valid keywords")

        resp = requests.get(base, params=search_params, timeout=3)
        resp.raise_for_status() #<- no-op if status==200
        return resp.content, resp.encoding


Parse the Results
-----------------

Next, we need a function ``parse_source`` to set up HTML for scraping. It will
need to:

.. class:: incremental

* Take the response body from the previous method (or some other source)
* Parse it using BeautifulSoup
* Return the parsed object for further processing

.. class:: incremental

Before you start, a word about parsing HTML with BeautifulSoup


Parsing HTML with BeautifulSoup
-------------------------------

The BeautifulSoup object can be instantiated with a string or a file-like
object as the sole argument:

.. code-block:: python
    :class: small

    from bs4 import BeautifulSoup
    parsed = BeautifulSoup('<h1>Some HTML</h1>')
    
    fh = open('a_page.html', 'r')
    parsed = BeautifulSoup(fh)
    
    page = urllib2.urlopen('http://site.com/page.html')
    parsed = BeautifulSoup(page)


.. class:: incremental

You might want to open the documentation as reference
(http://www.crummy.com/software/BeautifulSoup/bs4/doc)


My Solution
-----------

Take a shot at writing this new function in ``mashup.py``

.. code-block:: python
    :class: incremental small
    
    # add this import at the top
    from bs4 import BeautifulSoup

    # then add this function lower down
    def parse_source(html, encoding='utf-8'):
        parsed = BeautifulSoup(html, from_encoding=encoding)
        return parsed


Put It Together
---------------

We'll need to make our script do something when run.

.. code-block:: python
    :class: incremental small

    if __name__ == '__main__':
        # do something

.. class:: incremental

* Fetch a search results page
* Parse the resulting HTML
* For now, print out the results so we can see what we get

.. container:: incremental small

    Use the ``prettify`` method on a BeautifulSoup object::

        print parsed.prettify()


My Solution
-----------

Try to come up with the proper code on your own.  Add it to ``mashup.py``

.. code-block:: python
    :class: incremental small

    if __name__ == '__main__':
        html, encoding = fetch_search_results(
            minAsk=500, maxAsk=1000, bedrooms=2
        )
        doc = parse_source(html, encoding)
        print doc.prettify(encoding=encoding)


Test Your Work
--------------

Assuming your virtualenv is still active, you should be able to execute the
script.

.. class:: incremental

::

    (soupenv)$ python mashup.py
    <!DOCTYPE html>
    <html class="nojs">
     <head>
      <title>
       seattle apts/housing for rent classifieds  - craigslist
      </title>
    ...  


Preserve the Results
--------------------

Try it again, this time redirect the output to a local file, so we can use
it without needing to hit the craiglist servers each time::

    (soupenv)$ python mashup.py > craigslist_results.html


Finding The Needle
------------------

Next we find the bits of this pile of HTML that matter to us.

.. class:: incremental

Open your html file in a browser and take a look (w/ dev tools).

.. class:: incremental

We'll want to find:

.. class:: incremental

* The HTML element that contains a single listing
* The source of location data, listings without location should be abandoned
* The description of a listing
* The link to a full listing page on craigslist
* Relevant price or size data.


Pulling it Out
--------------

We can extract this information now. In BeautifulSoup:

.. class:: incremental

* All HTML elements (including the parsed document itself) are ``tags``
* A ``tag`` can be searched using its ``find_all`` method
* This searches the descendents of the tag on which it is called.
* It takes arguments which act as *filters* on the search results

.. container:: incremental

    like so: 

    .. class:: small

    ::

        tag.find_all(name, attrs, recursive, text, limit, **kwargs)


Searching by CSS Class
----------------------

The items we are looking for are ``p`` tags which have the CSS class
``row``:

.. class:: incremental

``find_all`` supports keyword arguments. If the keyword you use isn't one of
the listed arguments, it is treated as an ``attribute``

.. class:: incremental

In Python, ``class`` is a reserved word, so we can't use it as a keyword, but
you can use ``class_``!

.. class:: incremental small

::

    parsed.find_all('p', class_='row')


Try It Out
----------

Let's fire up a python interpreter and get our hands dirty here::

    (soupenv)$ python

.. code-block:: python
    :class: small incremental

    >>> html = open('craigslist_results.html', 'r').read()
    >>> from bs4 import BeautifulSoup
    >>> parsed = BeautifulSoup(html)
    >>> listings = parsed.find_all('p', class_='row')
    >>> len(listings)
    100


.. class:: incremental

That sounds about right. Let's see if we can get only those with location
data.


Filtering Tricks
----------------

Attribute filters given a ``True`` value match tags with that attribute

.. class:: incremental

Location data was in the ``data-latitude`` and ``data-longitude`` attributes.

.. code-block:: python
    :class: small incremental

    >>> location_attrs = {
    ...     'data-longitude': True,
    ...     'data-latitude': True}
    >>> locatable = parsed.find_all(
    ...     'p', class_='row', attrs=location_attrs)
    >>> len(locatable)
    43

.. class:: incremental

Great.  That worked nicely


Parsing a Row
-------------

Now that we have the rows we want, we need to parse them. We want to preserve:

.. class:: incremental

* Location data (latitude and longitude)
* Source link (to craiglist detailed listing)
* Description text
* Price and size data

.. class:: incremental

Which parts of a single row contain each of these elements?


Extracting Location
-------------------

Location data is in the ``data-`` attributes we used to filter rows.

.. container:: incremental

    We can read the HTML attributes of a 'tag' easily, using ``attrs``:

    .. code-block:: python
        :class: small

        >>> row1 = locatable[0]
        >>> row1.attrs
        {u'data-pid': u'3949023084', u'data-latitude': u'35.8625743108992',
         u'class': [u'row'], u'data-longitude': u'-78.6232739959049'}
        >>> lat = row1.attrs.get('data-latitude', None)
        >>> lon = row1.attrs.get('data-longitude', None)
        >>> print lat, lon
        46.9989830869194 -122.847250593816


Extracting Description and Link
-------------------------------

Where ``find_all`` will find many elements, ``find`` will only find the first
that matches the filters you provide.

.. container:: incremental

    Our targets are in the first ``a`` tag in the ``pl`` span inside our row:

    .. code-block:: python
        :class: small

        >>> link = row1.find('span', class_='pl').find('a')

.. container:: incremental

    The link path will be in the attrs:

    .. code-block:: python
        :class: small

        >>> path = link.attrs['href']

.. container:: incremental

    Text contained *inside* tags is in the ``string`` property:

    .. code-block:: python
        :class: small

        >>> description = link.string.strip()


Extracting Price and Size
-------------------------

Both price and size are held in the ``l2`` span:

.. code-block:: python
    :class: small

    >>> l2 = row1.find('span', class_='l2')

.. container:: incremental

    Price, conveniently, is in it's own container:
    
    .. code-block:: python
        :class: small
    
        >>> price_span = l2.find('span', class_='price')
        >>> price = price_span.string.strip()

.. class:: incremental

But the size element is not. It is a standalone *text node*.

.. class:: incremental

Try finding it by reading the ``string`` property of our ``l2`` tag.


Simple Navigation and Text
--------------------------

We can get to a simple text node by navigating there.

.. class:: incremental

You can navigate up, down and across document nodes.

.. container:: incremental

    We already have the ``price`` span, the size text node is next at the same
    level:

    .. code-block:: python
        :class: small

        >>> size = price_span.next_sibling.strip(' \n-/')
        >>> size
        u'2br - 912ft\xb2'

.. class:: incremental

You may have noticed that we keep using ``strip``. There are two reasons for
this.


The NavigableString Element
---------------------------

The most obvious reason is that we don't want extra whitespace.

.. class:: incremental

The second reason is more subtle. The values returned by ``string`` are
**not** simple unicode strings

.. container:: incremental

    They are actually instances of a class called ``NavigableString``:

    .. code-block:: python
        :class: small

        >>> price_span.next_sibling.__class__
        <class 'bs4.element.NavigableString'>

.. class:: incremental

Calling ``strip`` or casting them to ``unicode`` converts them, saving memory


Put It All Together
-------------------

Okay, a challenge.  Combine everything we've done into a function that:

.. class:: incremental

* Extracts all the locatable listings from our html page
* Iterates over each of them, and builds a dictionary of data
  
  * include ``location``, ``href``, ``description``, ``price`` and ``size``

* Returns a list of these dictionaries

.. class:: incremental

Call it ``extract_listings``

.. class:: incremental

Put this new function into ``mashup.py`` and call it from ``__main__``,
printing the result


Break Time
----------

Once you have this working, take a break.

.. class:: incremental

When we return, we'll try a saner approach to getting data from online

.. container:: incremental

    While you have a moment, sign up for an API key from this service:

    http://www.walkscore.com/professional/api.php


My Solution
-----------

.. code-block:: python
    :class: small incremental

    def extract_listings(doc):
        location_attrs = {'data-latitude': True,
                          'data-longitude': True}
        for row in doc.find_all('p', class_='row',
                                attrs=location_attrs):
            location = dict(
                [(key, row.attrs.get(key)) for key in location_attrs])
            link = row.find('span', class_='pl').find('a')
            price_span = row.find('span', class_='price')
            listing = {
                'location': location,
                'href': link.attrs['href'],
                'description': link.string.strip(),
                'price': price_span.string.strip(),
                'size': price_span.next_sibling.strip(' \n-/')
            }
            yield listing


My Solution
-----------

.. code-block:: python
    :class: small

    if __name__ == '__main__':
        html, encoding = fetch_search_results(
            minAsk=500, maxAsk=1000, bedrooms=2
        )
        doc = parse_source(html, encoding)
        for listing in extract_listings(doc):
            print listing


Another Approach
----------------

Scraping web pages is tedious and inherently brittle

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

RSS provides a pre-defined data set, can we also allow *calling procedures* to
get more dynamic data?

.. class:: incremental

We can!  Enter XML-RPC (Remote Procedure Call)

.. class:: incremental

* Provides a set of defined procedures which can take arguments
* Calls are made via HTTP GET, by passing an XML document
* Returns from a call are sent to the client in XML

.. class:: incremental

There is an interactive example of this at the end of this session. We will
not go through it here, though.


Beyond XML-RPC
--------------

.. class:: incremental

* XML-RPC allows introspection
* XML-RPC forces you to introspect to get information
* **Wouldn't it be nice to get that automatically?**
* XML-RPC provides data types
* XML-RPC provides only *certain* data types
* **Wouldn't it be nice to have an extensible system for types?**
* XML-RPC allows calling methods with parameters
* XML-RPC only allows calling methods, nothing else
* **wouldn't it be nice to have contextual data as well?**

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

.. class:: incremental

Again, there is a good example of using SOAP via the ``suds`` library at the
end of this session.

.. class:: incremental

But we're going to move on


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
* number: any number, but json does not use octal or hexadecimal
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
    >>> '[1, 2, 3]'
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

This usage can be much more memory-friendly with large files/sources


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

* Originally described by Roy T. Fielding (worth reading)
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

The HTTP Method represents the ``action`` to be taken

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

All the required information representing the possible actions to take *should
be present in every response*.

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
* provide all this in *each* HTTP response


Playing With REST
-----------------

Let's take a moment to play with REST.

.. class:: incremental

We'll use a common, public API provided by Google.

.. class:: incremental center

**Geocoding**


Geocoding with Google APIs
--------------------------

https://developers.google.com/maps/documentation/geocoding

.. container:: incremental

    Open a python interpreter using our virtualenv: 

    .. class:: small

    ::

        (soupenv)$ python

.. code-block:: python
    :class: small incremental

    >>> import requests
    >>> import json
    >>> from pprint import pprint
    >>> url = 'http://maps.googleapis.com/maps/api/geocode/json'
    >>> addr = '1325 4th Ave, Seattle, 98101'
    >>> parameters = {'address': addr, 'sensor': 'false' }
    >>> resp = requests.get(url, params=parameters)
    >>> data = json.loads(resp.text)
    >>> if data['status'] == 'OK':
    ...     pprint(data)
    


Reverse Geocoding
-----------------

You can do the same thing in reverse, supply latitude and longitude and get
back address information:

.. code-block:: python
    :class: small

    >>> location = data['results'][0]['geometry']['location']
    >>> latlng="{lat},{lng}".format(**location)
    >>> parameters = {'latlng': latlng, 'sensor': 'false'}
    >>> resp = requests.get(url, params=paramters)
    >>> data = json.loads(resp.text)
    >>> if data['status'] == 'OK':
    ...     pprint(data)

.. class:: incremental

Notice that there are a number of results returned, ordered from most specific
to least.


Mash It Up
----------

Let's add a new function to ``mashup.py``.  It will:

.. class:: incremental

* take a single listing from our craiglist work
* format the location data provided in that listing properly
* make a reverse geocoding lookup using the google api above
* add the best available address to the listing 
* return the updated listing

.. class:: incremental

Call it ``add_address``


My Solution
-----------

.. code-block:: python
    :class: small incremental
    
    # add an import
    import json

    # and a function
    def add_address(listing):
        api_url = 'http://maps.googleapis.com/maps/api/geocode/json'
        loc = listing['location']
        latlng_tmpl = "{data-latitude},{data-longitude}"
        parameters = {
            'sensor': 'false',
            'latlng': latlng_tmpl.format(**loc),
        }
        resp = requests.get(api_url, params=parameters)
        data = json.loads(resp.text)
        if data['status'] == 'OK':
            best = data['results'][0]
            listing['address'] = best['formatted_address']
        else:
            listing['address'] = 'unavailable'
        return listing


Add Address to Output
---------------------

Go ahead and bolt the new function into our ``__main__`` block:

.. code-block:: python
    :class: small incremental

    import pprint
    if __name__ == '__main__':
        params = {'minAsk': 500, 'maxAsk': 1000, 'bedrooms': 2}
        html, encoding = fetch_search_results(**params)
        doc = parse_source(html, encoding)
        for listing in extract_listings(doc):
            listing = add_address(listing)
            pprint.pprint(listing)

.. container:: incremental

    And give the result a whirl:

    .. class:: small

    ::

        (soupenv)$ python mashup.py
        {'address': u'123 Some Street, Chapel Hill, NC ...',
         'description': u'3 bedroom 2 bathroom unit is move in ready!'
         ...
        }


One More Step
-------------

I'm a big fan of walking places.

.. class:: incremental

So I'd like to find an apartment that is located somewhere 'walkable'

.. class:: incremental

There's an API for that!

.. class:: incremental

http://www.walkscore.com/professional/api.php

.. class:: incremental

If you haven't already, sign up for an API key now.


Getting a Walk Score
--------------------

The API documentation tells us we have to provide lat, lon and address to get
a walk score, along with our API key.

.. class:: incremental

It also tells us we have a choice of XML or JSON output.  Let's use JSON

.. class:: incremental

Let's poke at it and see what we get back

.. class:: incremental

Fire up your virtualenv Python interpreter again


Making an API Call
------------------

::

    (soupenv)$ python

.. code-block:: python
    :class: small

    >>> import requests
    >>> import json
    >>> from pprint import pprint
    >>> api_url = 'http://api.walkscore.com/score'
    >>> lat, lon = 35.9108986, -79.053783
    >>> addr = '120 E. Cameron Avenue Chapel Hill, NC 27599'
    >>> params = {'lat': lat, 'lon', lon, 'address': addr}
    >>> params['wsapikey'] = '<type your api key here>'
    >>> params['format'] = 'json'
    >>> resp = requests.get(api_url, params=params)
    >>> data = json.loads(resp.text)
    >>> if data['status'] == 1:
    ...     pprint(data)


Mash It Up
----------

Add a function to ``mashup.py`` that:

.. class:: incremental

* takes a single listing from our craigslist search
* uses the location and address to make a walkscore api call
* adds the description, walkscore and ws_link parameters to the listing
* returns the updated listing

.. class:: incremental

Call the function ``add_walkscore``

.. class:: incremental

Bolt it into our script's ``__main__`` block where it fits best


My Solution
-----------

.. code-block:: python
    :class: small incremental

    def add_walkscore(listing):
        api_url = 'http://api.walkscore.com/score'
        apikey = '<your api key goes here>'
        loc = listing['location']
        if listing['address'] == 'unavailable':
            return listing
        parameters = {
            'lat': loc['data-latitude'], 'lon': loc['data-longitude'],
            'address': listing['address'], 'wsapikey': apikey,
            'format': 'json'
        }
        resp = requests.get(api_url, params=parameters)
        data = json.loads(resp.text)
        if data['status'] == 1:
            listing['ws_description'] = data['description']
            listing['ws_score'] = data['walkscore']
            listing['ws_link'] = data['ws_link']
        return listing


My Results
----------

.. code-block:: python
    :class: small

    if __name__ == '__main__':
        params = {'minAsk': 500, 'maxAsk': 1000, 'bedrooms': 2}
        html, encoding = fetch_search_results(**params)
        doc = parse_source(html, encoding)
        for listing in extract_listings(doc):
            listing = add_address(listing)
            listing = add_walkscore(listing)
            pprint.pprint(listing)

.. container:: incremental

    Let's try it out::

        (soupenv)$ python mashup.py


Wrap Up
-------

We've built a simple mashup combining data from three different sources.

.. class:: incremental

As a result we can now make a listing of apartments ranked by the walkability
of their neighborhood.

.. class:: incremental

What other data sources might we use? Check out
http://www.programmableweb.com/apis/directory to see some of the possibilities


Addenda
-------

Altough we do not have class time to do walkthrough examples of using XML-RPC
and SOAP, I have provided exercises in each as an addenda to this session. If
you have the time and the interest, please try them out.

.. class:: center

`Web Service API Addenda <session03-addenda.html>`_


Homework
--------

For your homework this week, you'll be creating a mashup of your own.

.. class:: incremental

Use the programmable web api directory from above as a source of inspiration.

.. class:: incremental

Your mashup should combine at least two sources of data in some way that
tickles your fancy.

.. class:: incremental

Your results need not look pretty. Focus on data acquisition and processing.


Submitting Your Homework
------------------------

To submit your homework:

* Create a new python script in ``assignments/session03``. It should be
  something I can run with::

    $ python your_script.py

* Provide me with a text file describing what you did. Tell me about the
  sources you use, how you combine them, what you hoped to achieve.

* Include any instruction I might need to successfully run your script.

* Commit your changes to your fork of the repo in github, then open a pull
  request.


Extra Credit
------------

Bonus points if you write unit tests for the elements of your mashup.  

