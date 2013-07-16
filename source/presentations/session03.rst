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


Build a Search URL
------------------

First, let's build a function ``build_url`` that generates a good search url

.. class:: incremental

The standard library modules ``urllib`` and ``urllib2`` can help us

.. class:: incremental

* It will accept one keyword argument for each of the possible query values
* It will combine the values passed into an HTTP query
* It will combine that query with the base URL for the search and return the
  result

.. class:: incremental

Go ahead and write your version into ``mashup.py``


My Solution
-----------

.. code-block:: python
    :class: small incremental

    def build_url(**kwargs):
        base = 'http://raleigh.craigslist.org/search/apa'
        valid_kws = ('query', 'minAsk', 'maxAsk', 'bedrooms')
        use_kwargs = {}
        for kw in valid_kws:
            if kw in kwargs:
                use_kwargs[key] = kwargs[key]
        if not use_kwargs:
            raise ValueError("No valid keywords")
        query = urllib.urlencode(use_kwargs)
        return '%s?%s' % (base, query)


Grab and Parse a Page
---------------------

Next, we need a function ``parse_source`` to set up HTML for scraping. It will
need to:

.. class:: incremental

* Take the constructed URL from before as an argument
* Open the url
* If appropriate, attempt to parse the page with BeautifulSoup
* Return the parsed HTML for processing


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


My Solution
-----------

.. code-block:: python
    :class: incremental

    def parse_source(url):
        resp = urllib2.urlopen(url)
        if resp.code != 200:
            raise IOError("Error reading source URL")
        parsed = BeautifulSoup(resp)
        return parsed


Put It Together
---------------

To see how we're doing, we'll need to make our script do something when run.

.. class:: incremental

Add an ``if __name__ == '__main__`:`` block to the bottom of our library

.. class:: incremental small

* Build a good search url
* Parse the resulting search page
* For now, print out the results so we can see what we get

.. container:: incremental small

    You can print nice-looking output with BeautifulSoup::

        print parsed.prettify()


My Solution
-----------

.. code-block:: python
    :class: incremental

    if __name__ == '__main__':
        url = build_url(minAsk=500, maxAsk=1000, bedrooms=2)
        doc = parse_source(url)
        print doc.prettify()


Test Your Work
--------------

Assuming your virtualenv is still active, you should be able to execute the
script::

    (soupenv)$ python mashup.py
    <!DOCTYPE html>
    <html class="nojs">
     <head>
      <title>
       raleigh apts/housing for rent classifieds  - craigslist
      </title>
    ...


