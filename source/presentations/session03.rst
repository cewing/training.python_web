Python Web Programming
======================

.. image:: img/granny_mashup.png
    :align: left
    :width: 50%

Week 3: Scraping, APIs and Mashups

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

It would be nice to be able to combine data from different source to create
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

.. class:: incremental

* ``pip install virtualenv``
* ``easy_install virtualenv``

.. class:: incremental

These both demand that you have already got ``pip`` or ``easy_install``. If
you haven't, try this way instead:

.. class:: incremental

* download ``https://raw.github.com/pypa/virtualenv/master/virtualenv.py``
* remember where it goes.  You'll need it


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
        New python executable in soupenv/bin/python2.6
        New python executable in soupenv/bin/python
        Installing setuptools........................done.
        Installing pip...................done.


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

.. class:: incremental

Once that is installed, BeautifulSoup will choose it instead of the standard
library module.

.. class:: incremental

BeautifulSoup will choose the best available, you don't need to worry about it
(though you can specify).


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

* Base URL: ``http://raleigh.craigslist.org/search/apa``
* keywords: ``query=keyword+values+here``
* price: ``minAsk=NNN maxAsk=NNN``
* bedrooms: ``bedrooms=N`` (N in range 1-8)

.. class:: incremental

We can make a request with these parameters using the ``requests`` library we
installed a moment ago


Opening URLs with Requests
--------------------------

Requests has a very nice API for doing HTTP requests.

.. class:: incremental

Each HTTP method is represented by a module-level function:

.. class:: incremental

* ``GET`` == ``requests.get(url, **kwargs)``
* ``POST`` == ``requests.post(url, **kwargs)``
* ...

.. class:: incremental

Keyword arguments allow for other parts of an HTTP request:
    
.. class:: incremental

* ``params``: url parameters (?foo=bar&baz=bim)
* ``headers``: headers to send with the request
* ``data``: the body of the request, if any (form data for POST goes here)
* ...


Getting Responses with Requests
-------------------------------

Once you've made a request using one of these methods, the return value is a
``response``.

.. class:: incremental

This object has a number of useful attributes:

.. class:: incremental

* ``response.status_code``: see the HTTP Status Code returned
* ``response.ok``: True if ``response.status_code`` is not an error code
* ``response.headers``: The headers sent in the response from the server
* ``response.text``: Body of the response, decoded to a unicode string
* ``response.encoding``: The encoding used to decode ``response.text``
* ``response.content``: The original response body, not decoded (useful for
  binary content)

.. class:: incremental

If an error status is returned, you can raise a Python error by calling
``response.raise_for_status``.


Fetch Search Results
--------------------

We can start our work by writing a function ``fetch_search_results``

.. class:: incremental

* It will accept one keyword argument for each of the possible query values
* It will build a dictionary of request query parameters from incoming keywords
* It will make a request to the craigslist server using this query
* It will return the body of the response if there is no error
* It will raise an error if there is a problem with the response

.. class:: incremental

Using what you've learned, take a stab at writing this function. Put it in
``mashup.py``


My Solution
-----------

Here's the one I created:

.. code-block:: python
    :class: small incremental

    import requests

    def fetch_search_results(**kwargs):
        base = 'http://raleigh.craigslist.org/search/apa'
        valid_kws = ('query', 'minAsk', 'maxAsk', 'bedrooms')
        use_kwargs = dict(
            [(key, val) for key, val in kwargs.items() if key in valid_kws])
        if not use_kwargs:
            raise ValueError("No valid keywords")

        resp = requests.get(base, params=use_kwargs, timeout=3)
        if resp.ok:
            return resp.text, resp.encoding
        else:
            resp.raise_for_status()


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

To see how we're doing, we'll need to make our script do something when run.

.. class:: incremental

Add an ``if __name__ == '__main__`:`` block to the bottom of our library

.. class:: incremental

* Fetch a search results page
* Parse the resulting HTML
* For now, print out the results so we can see what we get

.. container:: incremental small

    You can print nice-looking output with BeautifulSoup::

        print parsed.prettify()


My Solution
-----------

Try to come up with the proper code on your own.  Add it to ``mashup.py``

.. code-block:: python
    :class: incremental

    if __name__ == '__main__':
        params = {'minAsk': 500, 'maxAsk': 1000, 'bedrooms': 2}
        html, encoding = fetch_search_results(**params)
        doc = parse_source(html, encoding)
        print doc.prettify(encoding=encoding)


Test Your Work
--------------

Assuming your virtualenv is still active, you should be able to execute the
script.

.. class:: incremental small

::

    (soupenv)$ python mashup.py
    <!DOCTYPE html>
    <html class="nojs">
     <head>
      <title>
       raleigh apts/housing for rent classifieds  - craigslist
      </title>
    ...

.. container:: incremental

    Try it again, this time redirect the output to a local file, so we can use
    it without needing to hit the craiglist servers each time:
    
    .. class:: small
    
    ::

        (soupenv)$ python mashup.py > craigslist_results.html


Finding The Needle
------------------

The next step is to find the bits of this pile of HTML that matter to us.

.. class:: incremental

We've got this HTML file, so let's open it in a browser and take a look

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

Now that we know what we are looking for, we can extract it. In BeautifulSoup:

.. class:: incremental

* All HTML elements (including the parsed document itself) act like ``tags``
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
    >>> len(entries)
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
