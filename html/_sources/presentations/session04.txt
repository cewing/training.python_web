**********
Session 04
**********

.. figure:: /_static/granny_mashup.png
    :align: center
    :width: 70%

    Paul Downey http://www.flickr.com/photos/psd/492139935/ - CC-BY

Scraping, APIs and Mashups
==========================

Wherein we learn how to make order from the chaos of the wild internet.


A Dilemma
---------

The internet makes a vast quantity of data available.

.. rst-class:: build
.. container::

    But not always in the form or combination you want.

    It would be nice to be able to combine data from different sources to
    create *meaning*.


The Big Question
----------------

.. rst-class:: large centered

But How?


The Big Answer
--------------

.. rst-class:: large centered

Mashups


Mashups
-------

A mashup is::

    a web page, or web application, that uses and combines data, presentation
    or functionality from two or more sources to create new services.

    -- wikipedia (http://en.wikipedia.org/wiki/Mashup_(web_application_hybrid))


Data Sources
------------

The key to mashups is the idea of data sources.

.. rst-class:: build
.. container::

    These come in many flavors:

    .. rst-class:: build

    * Simple websites with data in HTML
    * Web services providing structured data
    * Web services providing tranformative service (geocoding)
    * Web services providing presentation (mapping)

Web Scraping
============

.. rst-class:: left
.. container::

    It would be nice if all online data were available in well-structured formats.

    .. rst-class:: build
    .. container::

        The reality is that much data is available only in HTML.

        Still we can get at it, with some effort.

        By scraping the data from the web pages.


HTML
----

.. ifnotslides::

    Ideally, it looks like this:

.. code-block:: html

    <!DOCTYPE html>
    <html>
      <head>
      </head>
      <body>
        <p>A nice clean paragraph</p>
        <p>And another nice clean paragraph</p>
      </body>
    </html>


.. nextslide:: HTML... IRL

.. ifnotslides::

    But in real life, it's more often like this:

.. code-block:: html

    <html>
     <form>
      <table>
       <td><input name="input1">Row 1 cell 1
       <tr><td>Row 2 cell 1
      </form>
      <td>Row 2 cell 2<br>This</br> sure is a long cell
     </body>
    </html>


.. nextslide:: FFFFFFFFFUUUUUUUUUUUUU!!!!

.. figure:: /_static/scream.jpg
    :align: center
    :width: 32%

    Photo by Matthew via Flickr (http://www.flickr.com/photos/purplemattfish/3918004964/) - CC-BY-NC-ND


.. nextslide:: The Law of The Internet

.. rst-class:: large centered

"Be strict in what you send and tolerant in what you receive"


Taming the Mess
---------------

Luckily, there are tools to help with this.

.. rst-class:: build
.. container::

    In python there are several candidates, but I like ``BeautifulSoup``.

    BeautifulSoup is a great tool, but it's not in the Standard Library.

    We'll need to install it.

    Create a virtualenv to do so:

    .. code-block:: bash

        $ pyvenv soupenv
        ...
        $ source soupenv/bin/activate

    (remember, for Windows users that should be ``soupenv/Scripts/activate.bat``)


.. nextslide:: Install BeautifulSoup

Once the virtualenv is activated, you can simply use pip or easy_install to
install the libraries you want:

.. code-block:: bash

    (soupenv)$ pip install beautifulsoup4


.. nextslide:: Choose a Parsing Engine

BeautifulSoup is built to use the Python HTMLParser.

.. rst-class:: build

* Batteries Included.  It's already there
* It's not great, especially before Python 2.7.3

.. rst-class:: build
.. container::

    BeautifulSoup also supports using other parsers.

    There are two good choices: ``lxml`` and ``html5lib``.

    ``lxml`` is better, but much harder to install.  Let's use ``html5lib``.


.. nextslide:: Install a Parsing Engine

Again, this is pretty simple::

    (soupenv)$ pip install html5lib

.. rst-class:: build
.. container::

    Once installed, BeautifulSoup will choose it automatically.

    BeautifulSoup will choose the "best" available.

    You can specify the parser if you need to for some reason.

    In fact, in recent versions of BeautifulSoup, you'll be warned if you don't
    (though you can ignore the warning).


.. nextslide:: Install Requests

Python provides tools for opening urls and communicating with servers. It's
spread across the ``urllib`` and ``urllib2`` packages.

.. rst-class:: build
.. container::

    These packages have pretty unintuitive APIs.

    The ``requests`` library is becoming the de-facto standard for this type of
    work.  Let's install it too.

    .. code-block:: bash

        (soupenv)$ pip install requests


Our Class Mashup
----------------

We're going to explore some tools for making a mashup today

.. rst-class:: build
.. container::

    We'll be starting by scraping restaurant health code data for
    a given ZIP code

    Then, we'll look up the geographic location of those zipcodes using Google

    Finally, we'll display the results of our work on a map

    Start by opening a new file in your editor: ``mashup.py``.


.. nextslide:: Getting Some HTML

The source for the data we'll be displaying is a search tool provided by King
County.

.. rst-class:: build
.. container::

    It's supposed to have a web service, but the service is broken.

    Luckily, the HTML search works just fine.

    Open `the search form`_ in your browser.

    Fill in a ZIP code (perhaps 98101).

    Add a start and end date (perhaps about 1 or 2 years apart).

    Submit the form, and take a look at what you get.

.. _the search form: http://info.kingcounty.gov/health/ehs/foodsafety/inspections/search.aspx


.. nextslide:: Repeat, But Automate

Next we want to automate the process.

.. rst-class:: build
.. container::

    Copy the domain and path of the url into your new ``mashup.py`` file like
    so:

    .. code-block:: python

        INSPECTION_DOMAIN = "http://info.kingcounty.gov"
        INSPECTION_PATH = "/health/ehs/foodsafety/inspections/Results.aspx"

.. nextslide:: Repeat, But Automate

Next, copy the query parameters from the URL and convert them to a dictionary:

.. code-block:: python

    INSPECTION_PARAMS = {
        'Output': 'W',
        'Business_Name': '',
        'Business_Address': '',
        'Longitude': '',
        'Latitude': '',
        'City': '',
        'Zip_Code': '',
        'Inspection_Type': 'All',
        'Inspection_Start': '',
        'Inspection_End': '',
        'Inspection_Closed_Business': 'A',
        'Violation_Points': '',
        'Violation_Red_Points': '',
        'Violation_Descr': '',
        'Fuzzy_Search': 'N',
        'Sort': 'H'
    }


Fetching Search Results
-----------------------

Next we'll use the ``requests`` library to write a function to fetch these
results on demand.

.. rst-class:: build
.. container::

    In ``requests``, each HTTP method has a module-level function:

    .. rst-class:: build

    * ``GET`` == ``requests.get(url, **kwargs)``
    * ``POST`` == ``requests.post(url, **kwargs)``
    * ...

    ``kwargs`` represent other parts of an HTTP request:

    .. rst-class:: build

    * ``params``: a dict of url parameters (?foo=bar&baz=bim)
    * ``headers``: a dict of headers to send with the request
    * ``data``: the body of the request, if any (form data for POST goes here)
    * ...


.. nextslide:: Handling Requests Responses

The return value from one of these functions is a ``response`` object which
provides:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * ``response.status_code``: see the HTTP Status Code returned
    * ``response.ok``: True if ``response.status_code`` is not an error
    * ``response.raise_for_status()``: call to raise a python error if it is
    * ``response.headers``: The headers sent from the server
    * ``response.text``: Body of the response, decoded to unicode
    * ``response.encoding``: The encoding used to decode
    * ``response.content``: The original encoded response body as bytes

    ``requests documentation``: http://docs.python-requests.org/en/latest/

.. nextslide:: Fetch Search Results

We'll start by writing a function ``get_inspection_page``

.. rst-class:: build
.. container::

    .. rst-class:: build

    * It will accept keyword arguments for each of the possible query values
    * It will build a dictionary of request query parameters from incoming
      keywords, using INSPECTION_PARAMS as a template
    * It will make a request to the inspection service search page using this
      query
    * It will return the encoded content and the encoding used as a tuple

    Try writing this function. Put it in ``mashup.py``


My Solution
-----------

Here's the one I created:

.. rst-class:: build

.. code-block:: python

    import requests

    def get_inspection_page(**kwargs):
        url = INSPECTION_DOMAIN + INSPECTION_PATH
        params = INSPECTION_PARAMS.copy()
        for key, val in kwargs.items():
            if key in INSPECTION_PARAMS:
                params[key] = val
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp.text


Parse the Results
-----------------

Next, we'll need to parse the results we get when we call that function

But before we start, a word about parsing HTML with BeautifulSoup


.. nextslide:: Parsing HTML with BeautifulSoup

The BeautifulSoup object can be instantiated with a string or a file-like
object as the sole argument:

.. rst-class:: build
.. container::

    .. code-block:: python

        from bs4 import BeautifulSoup
        parsed = BeautifulSoup('<h1>Some HTML</h1>')

        fh = open('a_page.html', 'r')
        parsed = BeautifulSoup(fh)

        page = urllib2.urlopen('http://site.com/page.html')
        parsed = BeautifulSoup(page)

    You might want to open the documentation as reference
    (http://www.crummy.com/software/BeautifulSoup/bs4/doc)


My Solution
-----------

Take a shot at writing this new function in ``mashup.py``

.. code-block:: python

    # add this import at the top
    from bs4 import BeautifulSoup

    # then add this function lower down
    def parse_source(html):
        parsed = BeautifulSoup(html)
        return parsed


Put It Together
---------------

We'll need to make our script do something when run.

.. code-block:: python

    if __name__ == '__main__':
        # do something

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Fetch a search results page
    * Parse the resulting HTML
    * For now, print out the results so we can see what we get

    .. container::

        Use the ``prettify`` method on a BeautifulSoup object::

            print(parsed.prettify())


My Solution
-----------

Try to come up with the proper code on your own.  Add it to ``mashup.py``

.. rst-class:: build
.. code-block:: python

    if __name__ == '__main__':
        use_params = {
            'Inspection_Start': '2/1/2013',
            'Inspection_End': '2/1/2015',
            'Zip_Code': '98101'
        }
        html = get_inspection_page(**use_params)
        parsed = parse_source(html)
        print(parsed.prettify())


.. nextslide:: Test The Results

Assuming your virtualenv is still active, you should be able to execute the
script.

.. rst-class:: build
.. container::

    .. code-block:: bash
    
        (soupenv)$ python mashup.py
        ...
           <script src="http://www.kingcounty.gov/kcscripts/kcPageAnalytics.js" type="text/javascript">
           </script>
           <script type="text/javascript">
             //<![CDATA[
             var usasearch_config = { siteHandle:"kingcounty" };
             var script = document.createElement("script");
             script.type = "text/javascript";
             script.src = "http://search.usa.gov/javascripts/remote.loader.js";
             document.getElementsByTagName("head")[0].appendChild(script);
             //]]>
           </script>
          </form>
         </body>
        </html>

    This script is available as ``resources/session04/mashup_1.py``



.. nextslide:: Preserve the Results

Now, let's re-run the script, saving the output to a file so we can use it
later::

    $ python mashup.py > inspection_page.html

.. rst-class:: build
.. container::

    Then add a quick function to our script that will use these saved results:

    .. code-block:: python

        def load_inspection_page(name):
            file_path = pathlib.Path(name)
            return file_path.read_text(encoding='utf8')

    Finally, bolt that in to your script to use it:

    .. code-block:: python

        # COMMENT OUT THIS LINE AND REPLACE IT
        # html = get_inspection_page(**use_params)
        html = load_inspection_page('inspection_page.html')


Extracting Data
---------------

Next we find the bits of this pile of HTML that matter to us.

.. rst-class:: build
.. container::

    Open the page you just wrote to disk in your web browser and open the
    developer tools to inspect the page source.

    You'll want to start by finding the element in the page that contains all
    our search results.

    Look at the source and identify the single element we are looking for.

.. nextslide:: Tags and Searching

Having found it visually, we can now search for it automatically. In
BeautifulSoup:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * All HTML elements (including the parsed document itself) are ``tags``
    * A ``tag`` can be searched using its ``find`` or ``find_all`` methods
    * This searches the descendents of the tag on which it is called.
    * It takes arguments which act as *filters* on the search results

    .. container::

        like so::

            tag.find(name, attrs, recursive, text, **kwargs)
            tag.find_all(name, attrs, recursive, text, limit, **kwargs)


.. nextslide:: Searching by Attribute

The ``find`` method allows us to pass *kwargs*.

.. rst-class:: build
.. container::

    Keywords that are not among the named parameters will be considered an HTML
    attribute.

    We can use this to find the column that holds our search results:

    .. code-block:: python

        content_col = parsed.find('td', id="contentcol")

    Add that line to our mashup script and try it out:

    .. code-block:: python

        #...
        parsed = parse_source(html)
        content_col = parsed.find("td", id="contentcol")
        print content_col.prettify()

    .. code-block:: bash

        (soupenv)$ python mashup.py
        <td id="contentcol">
            ...
        </td>


.. nextslide:: Filtering By Regular Expression

The next job is to find the inspection data we can see when we click on the
restaurant names in our page.

.. rst-class:: build
.. container::

    Do you notice a pattern in how that data is structured?

    For each restaurant in our results, there are *two* ``<div>`` tags.

    The first contains the content you see at first, the second the content
    that displays when we click.

    What can you see that identifies these items?

    ``<div id="PR0084952"...>`` and ``<div id="PR0084952~"...>``

    Each pair shares an ID, and the stuff we want is in the second one

    Each number is different for each restaurant

    We can use a regular expression to help us here.

.. nextslide:: Getting the Information Divs

Let's write a function in ``mashup.py`` that will find all the divs in our
column with the right kind of id:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * It should match ``<div>`` tags only
    * It should match ids that start with ``PR``
    * It should match ids that contain some number of *digits* after that
    * It should match ids that end with a *tilde* (``~``) character

    .. code-block:: python

        # add an import up top
        import re

        # and add this function
        def restaurant_data_generator(html):
            id_finder = re.compile(r'PR[\d]+~')
            return html.find_all('div', id=id_finder)


.. nextslide:: Verify It Works

Let's add that step to the *main* block at the bottom of ``mashup.py`` (only
print the first of the many divs that match):

.. rst-class:: build
.. container::

    .. code-block:: python

        html, encoding = load_inspection_page('inspection_page.html')
        parsed = parse_source(html, encoding)
        content_col = parsed.find("td", id="contentcol")
        data_list = restaurant_data_generator(content_col)
        print data_list[0].prettify()


    Finally, test it out:

    .. code-block:: bash

        (soupenv)$ python mashup.py
        <div id="PR0001203~" name="PR0001203~" onclick="toggleShow(this.id);"...>
         <table style="width: 635px;">
         ...
         </table>
        </div>

    This code is available as ``/resources/session04/mashup_2.py``


Parsing Restaurant Data
-----------------------

Now that we have the records we want, we need to parse them.

.. rst-class:: build
.. container::

    We'll start by extracting information about the restaurants:

    .. rst-class:: build

    * Name
    * Address
    * Location

    How is this information contained in our records?


.. nextslide:: Complex Filtering

Each record consists of a table with a series of *rows* (``<tr>``).

.. rst-class:: build
.. container::

    The rows we want at this time all have two *cells* inside them.

    The first contains the *label* of the data, the second contains the *value*

    We'll need a function in ``mashup.py`` that:

    .. rst-class:: build

    * takes an HTML element as an argument
    * verifies that it is a ``<tr>`` element
    * verifies that it has two immediate children that are ``<td>`` elements

    My solution:

    .. code-block:: python

        def has_two_tds(elem):
            is_tr = elem.name == 'tr'
            td_children = elem.find_all('td', recursive=False)
            has_two = len(td_children) == 2
            return is_tr and has_two

.. nextslide:: Test It Out

Let's try this out in an interpreter:

.. code-block:: ipython

    In [1]: from mashup_3 import load_inspection_page, parse_source,
            restaurant_data_generator, has_two_tds
    In [2]: html = load_inspection_page('inspection_page.html')
    In [3]: parsed = parse_source(html)
    ...
    In [4]: content_col = parsed.find('td', id='contentcol')
    In [5]: records = restaurant_data_generator(content_col)
    In [6]: rec = records[4]

.. nextslide:: Test It Out

We'd like to find all table rows in that div that contain *two* cells

.. rst-class:: build
.. container::

    The table rows are all contained in a ``<tbody>`` tag.

    We only want the ones at the top of that tag (ones nested more deeply
    contain other data)

    .. code-block:: ipython

        In [13]: data_rows = rec.find('tbody').find_all(has_two_tds, recursive=False)
        In [14]: len(data_rows)
        Out[14]: 7
        In [15]: print(data_rows[0].prettify())
        <tr>
         <td class="promptTextBox" style="width: 125px; font-weight: bold">
          - Business Name
         </td>
         <td class="promptTextBox" style="width: 520px; font-weight: bold">
          SPICE ORIENT
         </td>
        </tr>

.. nextslide:: Extracting Labels and Values

Now we have a list of the rows that contain our data.

.. rst-class:: build
.. container::

    Next we have to collect the data they contain

    The *label/value* structure of this data should suggest the right container
    to store the information.

    Let's start by trying to get at the first label

    .. code-block:: ipython
    
        In [18]: row1 = data_rows[0]
        In [19]: cells = row1.find_all('td')
        In [20]: cell1 = cells[0]
        In [21]: cell1.text
        Out[21]: '\n            - Business Name\n           '

    That works well enough, but all that extra stuff is nasty

    We need a method to clean up the text we get from these cells

    It should strip extra whitespace, and characters like ``-`` and ``:`` we
    don't want.

.. nextslide:: My Solution

Try writing such a function for yourself now in ``mashup.py``

.. rst-class:: build
.. container::

    .. code-block:: python

        def clean_data(td):
            return td.text.strip(" \n:-")

    Add it to your interpreter and test it out:

    .. code-block:: ipython
    
        In [25]: def clean_data(td):
           ....:     return td.text.strip(" \n:-")
           ....:
        In [26]: clean_data(cell1)
        Out[26]: 'Business Name'
        In [27]:

    Ahhh, much better

.. nextslide:: The Complete Function

So we can get a list of the rows that contain label/value pairs.

.. rst-class:: build
.. container::

    And we can extract clean values from the cells in these rows

    Now we need a function in ``mashup.py`` that will iterate through the rows
    we find and build a dictionary of the pairs.

    We have to be cautious because some rows don't have a label.

    The values in these rows should go with the label from the previous row.

.. nextslide:: My Solution

Here's the version I came up with:

.. code-block:: python

    def extract_restaurant_metadata(elem):
        restaurant_data_rows = elem.find('tbody').find_all(
            has_two_tds, recursive=False
        )
        rdata = {}
        current_label = ''
        for data_row in restaurant_data_rows:
            key_cell, val_cell = data_row.find_all('td', recursive=False)
            new_label = clean_data(key_cell)
            current_label = new_label if new_label else current_label
            rdata.setdefault(current_label, []).append(clean_data(val_cell))
        return rdata


.. nextslide:: Testing It Out

Add it to our script:

.. rst-class:: build
.. container::

    .. code-block:: python
    
        # ...
        data_list = restaurant_data_generator(content_col)
        for data_div in data_list:
            metadata = extract_restaurant_metadata(data_div)
            print metadata

    And then try it out:

    .. code-block:: bash
    
        (soupenv)$ python mashup.py
        ...
        {u'Business Category': [u'Seating 0-12 - Risk Category III'],
         u'Longitude': [u'122.3401786000'], u'Phone': [u'(206) 501-9554'],
         u'Business Name': [u"ZACCAGNI'S"], u'Address': [u'97B PIKE ST', u'SEATTLE, WA 98101'],
         u'Latitude': [u'47.6086651300']}

    This script is available as ``resources/session04/mashup_3.py``


Extracting Inspection Data
--------------------------

The final step is to extract the inspection data for each restaurant.

.. rst-class:: build
.. container::

    We want to capture only the score from each inspection, details we can
    leave behind.

    We'd like to calculate the average score for all known inspections.

    We'd also like to know how many inspections there were in total.

    Finally, we'd like to preserve the highest score of all inspections for a
    restaurant.

    We'll add this information to our metadata about the restaurant.


.. nextslide:: Finding the Data

Let's start by getting our bearings. Return to viewing the
``inspection_page.html`` you saved in a browser.

.. rst-class:: build
.. container::

    Find a restaurant that has had an inspection or two.

    What can you say about the HTML that contains the scores for these
    inspections?

    I notice four characteristics that let us isolate the information we want:

    .. rst-class:: build

    * Inspection data is containd in ``<tr>`` elements
    * Rows with inspection data in them have four ``<td>`` children
    * The text in the first cell contains the word "inspection"
    * But the text does not *start* with the word "inspection"
    
    Let's try to write a filter function like the one above that will catch
    these rows for us.

.. nextslide:: The filter

Add this new function ``is_inspection_data_row`` to ``mashup.py``

.. rst-class:: build
.. code-block:: python

    def is_inspection_data_row(elem):
        is_tr = elem.name == 'tr'
        if not is_tr:
            return False
        td_children = elem.find_all('td', recursive=False)
        has_four = len(td_children) == 4
        this_text = clean_data(td_children[0]).lower()
        contains_word = 'inspection' in this_text
        does_not_start = not this_text.startswith('inspection')
        return is_tr and has_four and contains_word and does_not_start

.. nextslide:: Test It Out

We can test this function by adding it into our script:

.. code-block:: python

    for data_div in data_list:
        metadata = extract_restaurant_metadata(data_div)
        # UPDATE THIS BELOW HERE
        inspection_rows = data_div.find_all(is_inspection_data_row)
        print(metadata)
        print(len(inspection_rows))
        print('*'*10)

.. rst-class:: build
.. container::

    And try running the script in your terminal:

    .. code-block:: bash
    
        (soupenv)$ python mashup.py
        {u'Business Category': [u'Seating 0-12 - Risk Category III'],
         u'Longitude': [u'122.3401786000'], u'Phone': [u'(206) 501-9554'],
         u'Business Name': [u"ZACCAGNI'S"], u'Address': [u'97B PIKE ST', u'SEATTLE, WA 98101'],
         u'Latitude': [u'47.6086651300']}
        0
        **********

.. nextslide:: Building Inspection Data

Now we can isolate a list of the rows that contain inspection data.

.. rst-class:: build
.. container::

    Next we need to calculate the average score, total number and highest score
    for each restaurant.

    Let's add a function to ``mashup.py`` that will:

    .. rst-class:: build

    * Take a div containing a restaurant record
    * Extract the rows containing inspection data
    * Keep track of the highest score recorded
    * Sum the total of all inspections
    * Count the number of inspections made
    * Calculate the average score for inspections
    * Return the three calculated values in a dictionary

.. nextslide:: My Solution

Try writing this routine yourself.

.. code-block:: python

    def get_score_data(elem):
        inspection_rows = elem.find_all(is_inspection_data_row)
        samples = len(inspection_rows)
        total = high_score = average = 0
        for row in inspection_rows:
            strval = clean_data(row.find_all('td')[2])
            try:
                intval = int(strval)
            except (ValueError, TypeError):
                samples -= 1
            else:
                total += intval
                high_score = intval if intval > high_score else high_score
        if samples:
            average = total/float(samples)
        return {'Average Score': average, 'High Score': high_score,
                'Total Inspections': samples}

.. nextslide:: Test It Out

We can now incorporate this new routine into our ``mashup`` script.

.. rst-class:: build
.. container::

    We'll want to add the data it produces to the metadata we've already
    extracted.

    .. code-block:: python

        for data_div in data_list:
            metadata = extract_restaurant_metadata(data_div)
            inspection_data = get_score_data(data_div)
            metadata.update(inspection_data)
            print metadata

    And test it out at the command line:

    .. code-block:: bash

        (soupenv)$ python mashup.py
        ...
        {u'Business Category': [u'Seating 0-12 - Risk Category III'],
         u'Longitude': [u'122.3401786000'], u'High Score': 0,
         u'Phone': [u'(206) 501-9554'], u'Business Name': [u"ZACCAGNI'S"],
         u'Total Inspections': 0, u'Address': [u'97B PIKE ST', u'SEATTLE, WA 98101'],
         u'Latitude': [u'47.6086651300'], u'Average Score': 0}

Break Time
----------

Once you have this working, take a break.

When we return, we'll try a saner approach to getting data from online



Another Approach
================

.. rst-class:: left
.. container::

    Scraping web pages is tedious and inherently brittle

    .. rst-class:: build
    .. container::

        The owner of the website updates their layout, your code breaks

        But there is another way to get information from the web in a more normalized
        fashion

        .. rst-class:: centered

        **Web Services**


Web Services
------------

"a software system designed to support interoperable machine-to-machine
interaction over a network" - W3C

.. rst-class:: build

* provides a defined set of calls
* returns structured data


.. nextslide:: Early Web Services

**RSS** is one of the earliest forms of Web Services

.. rst-class:: build
.. container::

    A single web-based *endpoint* provides a dynamically updated listing of
    content

    Implemented in pure HTTP.  Returns XML

    **Atom** is a competing, but similar standard

    There's a solid Python library for consuming RSS: `feedparser`_.

.. _feedparser: https://pythonhosted.org/feedparser/

.. nextslide:: XML-RPC

XML-RPC extended the essentially static nature of RSS by allowing users to call
procedures and pass arguments.

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Calls are made via HTTP GET, by passing an XML document
    * Returns from a call are sent to the client in XML

    In python, you can access XML-RPC services using `xmlrpc`_ from the
    standard library. It has two libraries, ``xmlrpc.client`` and
    ``xmlrpc.server``

.. _xmlrpc: https://docs.python.org/3.5/library/xmlrpc.html

.. nextslide:: SOAP

SOAP extends XML-RPC in a couple of useful ways:

.. rst-class:: build

* It uses Web Services Description Language (WSDL) to provide meta-data about
  an entire service in a machine-readable format (Automatic introspection)

* It establishes a method for extending available data types using XML
  namespaces

.. rst-class:: build
.. container::

    There is no standard library module that supports SOAP directly.

    .. rst-class:: build

    * The best-known and best-supported module available is **Suds**
    * The homepage is https://fedorahosted.org/suds/
    * It can be installed using ``easy_install`` or ``pip install``
    * A `fork of the library`_ compatible with Python 3 does exist

    **I HATE SOAP**

.. _fork of the library: https://github.com/cackharot/suds-py3

.. nextslide:: What about WSDL?

SOAP was invented in part to provide completely machine-readable
interoperability.

.. rst-class:: build
.. container::

    *Does that really work in real life?*

    .. rst-class:: centered

    **Hardly ever**

    Another reason was to provide extensibility via custom types

    *Does that really work in real life?*

    .. rst-class:: centered

    **Hardly ever**

.. nextslide:: I have to write XML?

In addition, XML is a pretty inefficient medium for transmitting data.  There's
a lot of extra characters transmitted that lack any meaning.

.. code-block:: xml

    <?xml version="1.0"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
      <soap:Header>
      </soap:Header>
      <soap:Body>
        <m:GetStockPrice xmlns:m="http://www.example.org/stock/Surya">
          <m:StockName>IBM</m:StockName>
        </m:GetStockPrice>
      </soap:Body>
    </soap:Envelope>

.. nextslide:: Why Do All The Work?

So, if neither of the original goals is really achieved by using SOAP

.. rst-class:: build
.. container::

    And if the transmission medium is too bloated to use

    why pay all the overhead required to use the protocol?

    Is there another way we could consider approaching the problem?

    .. rst-class:: centered

    **Enter REST**


REST
----

.. rst-class:: centered

**Representational State Transfer**

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Originally described by Roy T. Fielding (worth reading)
    * Use HTTP for what it can do
    * Read more in `RESTful Web Services <http://www.crummy.com/writing/RESTful-Web-Services/>`_\*

    \* Seriously. Buy it and read it

.. nextslide:: A Comparison

The XML-RCP/SOAP way:

.. rst-class:: build

* POST /getComment HTTP/1.1
* POST /getComments HTTP/1.1
* POST /addComment HTTP/1.1
* POST /editComment HTTP/1.1
* POST /deleteComment HTTP/1.1

.. rst-class:: build
.. container::

    The RESTful way:

    .. rst-class:: build

    * GET /comment/<id> HTTP/1.1
    * GET /comment HTTP/1.1
    * POST /comment HTTP/1.1
    * PUT /comment/<id> HTTP/1.1
    * DELETE /comment/<id> HTTP/1.1


.. nextslide:: ROA

REST is a **Resource Oriented Architecture**

.. rst-class:: build
.. container::

    The URL represents the *resource* we are working with

    The HTTP Method indicates the ``action`` to be taken

    The HTTP Code returned tells us the ``result`` (whether success or failure)

.. nextslide:: HTTP Codes Revisited

.. rst-class:: build
.. container::

    POST /comment HTTP/1.1  (creating a new comment):

    .. rst-class:: build

    * Success: ``HTTP/1.1 201 Created``
    * Failure (unauthorized): ``HTTP/1.1 401 Unauthorized``
    * Failure (NotImplemented): ``HTTP/1.1 405 Not Allowed``
    * Failure (ValueError): ``HTTP/1.1 406 Not Acceptable``

    PUT /comment/<id> HTTP/1.1 (edit comment):

    .. rst-class:: build

    * Success: ``HTTP/1.1 200 OK``
    * Failure: ``HTTP/1.1 409 Conflict``

    DELETE /comment/<id> HTTP/1.1 (delete comment):

    .. rst-class:: build

    * Success: ``HTTP/1.1 204 No Content``

REST uses JSON
--------------

JavaScript Object Notation:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * a lightweight data-interchange format
    * easy for humans to read and write
    * easy for machines to parse and generate

    Based on Two Structures:

    * object: ``{ string: value, ...}``
    * array: ``[value, value, ]``

    .. rst-class:: centered

    pythonic, no?


.. nextslide:: JSON Data Types

JSON provides a few basic data types (see http://json.org/):

.. rst-class:: build
.. container::

    .. rst-class:: build

    * string: unicode, anything but ", \\ and control characters
    * number: any number, but json does not use octal or hexadecimal
    * object, array (we've seen these above)
    * true
    * false
    * null

    .. rst-class:: centered

    **No date type? OMGWTF??!!1!1**

.. nextslide:: Dates in JSON

You have two options:

.. rst-class:: build
.. container::

    .. container::

        Option 1 - Unix Epoch Time (number):

        .. code-block:: python

            >>> import time
            >>> time.time()
            1358212616.7691269

    .. container::

        Option 2 - ISO 8661 (string):

        .. code-block:: python

            >>> import datetime
            >>> datetime.datetime.now().isoformat()
            '2013-01-14T17:18:10.727240'


JSON in Python
--------------

You can encode python to json, and decode json back to python:

.. rst-class:: build
.. container::

    .. code-block:: python

        In [1]: import json
        In [2]: array = [1, 2, 3]
        In [3]: json.dumps(array)
        Out[3]: '[1, 2, 3]'
        In [4]: orig = {'foo': [1,2,3], 'bar': 'my resumé', 'baz': True}
        In [5]: encoded = json.dumps(orig)
        In [6]: encoded
        Out[6]: '{"foo": [1, 2, 3], "bar": "my resum\\u00e9", "baz": true}'
        In [7]: decoded = json.loads(encoded)
        In [8]: decoded == orig
        Out[8]: True

    Customizing the encoder or decoder class allows for specialized serializations


.. nextslide::

the json module also supports reading and writing to *file-like objects* via
``json.dump(fp)`` and ``json.load(fp)`` (note the missing 's')

.. rst-class:: build
.. container::

    Remember duck-typing. Anything with a ``.write`` and a ``.read`` method is
    *file-like*

    This usage can be much more memory-friendly with large files/sources


Playing With REST
-----------------

Let's take a moment to play with REST.

.. rst-class:: build
.. container::

    We'll use a common, public API provided by Google.

    .. rst-class:: centered

    **Geocoding**

.. nextslide:: Geocoding with Google APIs

https://developers.google.com/maps/documentation/geocoding

.. rst-class:: build
.. container::

    Open a python interpreter using our virtualenv::

        (soupenv)$ python

    .. code-block:: ipython

        In [1]: import requests
        In [2]: import json
        In [3]: from pprint import pprint
        In [4]: url = 'http://maps.googleapis.com/maps/api/geocode/json'
        In [5]: addr = '1325 4th Ave, Seattle, 98101'
        In [6]: parameters = {'address': addr, 'sensor': 'false'}
        In [7]: resp = requests.get(url, params=parameters)
        In [8]: data = resp.json()


.. nextslide:: Reverse Geocoding

You can do the same thing in reverse, supply latitude and longitude and get
back address information:

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [15]: if data['status'] == 'OK':
           ....:     pprint(data['results'])
           ....:
        [{'address_components': [{'long_name': '1325',
                                  'short_name': '1325',
          ...
          'types': ['street_address']}]

    Notice that there may be a number of results returned, ordered from most
    specific to least.


Mashing It Up
-------------

Google's geocoding data is quite nice.

.. rst-class:: build
.. container::

    But it's not in a format we can use directly to create a map

    For that we need `geojson`

    Moreover, formatting the data for all those requests is going to get
    tedious.

    Luckily, people create *wrappers* for popular REST apis like google's
    geocoding service.

    Once such wrapper is `geocoder`_, which provides not only google's service,
    but many others under a single umbrella.

.. _geocoder: http://geocoder.readthedocs.org/en/latest/
.. _geojson: http://geojson.org

.. nextslide:: Install ``geocoder``

Install geocoder into your ``soupenv`` so that it's available to use:

.. code-block:: bash

    (soupenv)$ pip install geocoder

.. rst-class:: build
.. container::

    Our final step for tonight will be to geocode the results we have scraped
    from the inspection site.

    We'll then convert that to ``geojson``, insert our own properties and map
    the results.

    Let's begin by converting our script so that what we have so far is
    contained in a generator function

    We'll eventually sort our results and generate the top 10 or so for
    geocoding.

    Open up ``mashup.py`` and copy everthing in the ``main`` block.

.. nextslide:: Make a Generator Function

Add a new function ``result_generator`` to the ``mashup.py`` script. Paste the
code you copied from the ``main`` block and then update it a bit:

.. rst-class:: build
.. code-block:: python

    def result_generator(count):
        use_params = {
            'Inspection_Start': '2/1/2013',
            'Inspection_End': '2/1/2015',
            'Zip_Code': '98101'
        }
        # html, encoding = get_inspection_page(**use_params)
        html, encoding = load_inspection_page('inspection_page.html')
        parsed = parse_source(html, encoding)
        content_col = parsed.find("td", id="contentcol")
        data_list = restaurant_data_generator(content_col)
        for data_div in data_list[:count]:
            metadata = extract_restaurant_metadata(data_div)
            inspection_data = get_score_data(data_div)
            metadata.update(inspection_data)
            yield metadata


.. nextslide:: Test It Out

Update the ``main`` block of your ``mashup.py`` script to use the new function:

.. rst-class:: build
.. container::

    .. code-block:: python

        if __name__ == '__main__':
            for result in result_generator(10):
                print result

    Then run your script and verify that the only thing that has changed is the
    number of results that print.

    .. code-block:: bash
    
        (soupenv)$ python mashup.py
        # you should see 10 dictionaries print here.

Add Geocoding
-------------

The API for geocoding with ``geocoder`` is the same for all providers.

.. rst-class:: build
.. container::

    You give an address, it returns geocoded data.

    You provide latitude and longitude, it provides address data

    .. code-block:: ipython
    
        In [1]: response = geocoder.google(<address>)
        In [2]: response.json
        Out[2]: # json result data
        In [3]: response.geojson
        Out[3]: # geojson result data

.. nextslide:: Adding The Function

Let's add a new function ``get_geojson`` to ``mashup.py``

.. rst-class:: build
.. container::

    It will 

    .. rst-class:: build

    * Take a result from our search as it's input
    * Get geocoding data from google using the address of the restaurant
    * Return the geojson representation of that data

    Try to write this function on your own

    .. code-block:: python
    
        def get_geojson(result):
            address = " ".join(result.get('Address', ''))
            if not address:
                return None
            geocoded = geocoder.google(address)
            return geocoded.geojson

.. nextslide:: Testing It Out

Next, update our ``main`` block to get the geojson for each result and print
it:

.. rst-class:: build
.. container::

    .. code-block:: python

        if __name__ == '__main__':
            for result in result_generator(10):
                geojson = get_geojson(result)
                print geojson

    Then test your results by running your script:

    .. code-block:: bash
    
        (soupenv)$ python mashup.py
        {'geometry': {'type': 'Point', 'coordinates': [-122.3393005, 47.6134378]},
         'type': 'Feature', 'properties': {'neighborhood': 'Belltown',
         'encoding': 'utf-8', 'county': 'King County', 'city_long': 'Seattle',
         'lng': -122.3393005, 'quality': u'street_address', 'city': 'Seattle',
         'confidence': 9, 'state': 'WA', 'location': u'1933 5TH AVE SEATTLE, WA 98101',
         'provider': 'google', 'housenumber': '1933', 'accuracy': 'ROOFTOP',
         'status': 'OK', 'state_long': 'Washington',
         'address': '1933 5th Avenue, Seattle, WA 98101, USA', 'lat': 47.6134378,
         'postal': '98101', 'ok': True, 'road_long': '5th Avenue', 'country': 'US',
         'country_long': 'United States', 'street': '5th Ave'},
         'bbox': [-122.3406494802915, 47.6120888197085, -122.3379515197085, 47.6147867802915]}

.. nextslide:: Update Geojson Properties

The ``properties`` of our geojson records are filled with data we don't really
care about.

.. rst-class:: build
.. container::

    Let's replace that information with some of the metadata from our
    inspection results.

    We'll update our ``get_geojson`` function so that it:

    .. rst-class:: build

    * Builds a dictionary containing only the values we want from our
      inspection record.
    * Converts list values to strings (geojson requires this)
    * Replaces the 'properties' of our geojson with this new data
    * Returns the modified geojson record

.. nextslide:: Write the Function

See if you can make the updates on your own.

.. rst-class:: build
.. code-block:: python

    def get_geojson(result):
        # ...
        geocoded = geocoder.google(address)
        geojson = geocoded.geojson
        inspection_data = {}
        use_keys = (
            'Business Name', 'Average Score', 'Total Inspections', 'High Score'
        )
        for key, val in result.items():
            if key not in use_keys:
                continue
            if isinstance(val, list):
                val = " ".join(val)
            inspection_data[key] = val
        geojson['properties'] = inspection_data
        return geojson

.. nextslide:: Making Mappable Data

We are now generating a series of ``geojson`` *Feature* objects.

.. rst-class:: build
.. container::

    To map these objects, we'll need to create a file which contains a
    ``geojson`` *FeatureCollection*.

    The structure of such a collection looks like this:

    .. code-block:: json
    
        {'type': 'FeatureCollection', 'features': [...]}

    Let's update our ``main`` function to append each feature to such a
    structure.

    Then we can dump the structure as ``json`` to a file.

.. nextslide:: Update the Script

In ``mashup.py`` update the ``main`` block like so:

.. rst-class:: build
.. container::

    .. code-block:: python

        # add an import at the top:
        import json

        if __name__ == '__main__':
            total_result = {'type': 'FeatureCollection', 'features': []}
            for result in result_generator(10):
                geojson = get_geojson(result)
                total_result['features'].append(geojson)
            with open('my_map.json', 'w') as fh:
                json.dump(total_result, fh)

    When you run the script nothing will print, but the new file will appear.

    .. code-block:: bash

        (soupenv)$ python mashup.py

    This script is available as ``resources/session04/mashup_5.py``

Display the Results
-------------------

Once the new file is written you are ready to display your results.

.. rst-class:: build
.. container::

    Open your web browser and go to http://geojson.io

    Then drag and drop the new file you wrote onto the map you see there.

    .. figure:: /_static/geojson-io.png
        :align: center
        :width: 75%

Wrap Up
-------

We've built a simple mashup combining data from different sources.

.. rst-class:: build
.. container::

    We scraped health inspection data from the King County government site.

    We geocoded that data.

    And we've displayed the results on a map.

    What other sources of data might we choose to combine?

    Check out `programmable web <http://www.programmableweb.com/apis/directory>`_
    to see some of the possibilities




Homework
========

.. rst-class:: left
.. container::

    For your homework this week, you'll be polishing this mashup.

    .. rst-class:: build
    .. container::

        Begin by sorting the results of our search by the average score (can
        you do this and still use a generator for getting the geojson?).

        Then, update your script to allow the user to choose how to sort, by
        average, high score or most inspections::

            (soupenv)$ python mashup.py highscore

        Next, allow the user to choose how many results to map::

            (soupenv)$ python mashup.py highscore 25

        Or allow them to reverse the results, showing the lowest scores first::

            (soupenv)$ python mashup.py highscore 25 reverse

        If you're feeling particularly adventurous, see if you can use the
        `argparse`_ module from the standard library to handle command line
        arguments

.. _argparse: https://docs.python.org/2/library/argparse.html#module-argparse

More Fun
--------

Next, try adding a bit of information to your map by setting the
``marker-color`` property. This will display a marker with the provided
css-style color (``#FF0000``)

.. rst-class:: build
.. container::

    See if you can make the color change according to the values used for the
    sorting of the list.  Either vary the intensity of the color, or the hue.

    Finally, if you are feeling particularly frisky, you can update your script
    to automatically open a browser window with your map loaded on
    *geojson.io*.

    To do this, you'll want to read about the `webbrowser`_ module from the
    standard library.

    In addition, you'll want to read up on using the URL parameters API for
    *geojson.io*.  Click on the **help** tab in the sidebar to view the
    information.

    You will also need to learn about how to properly quote special characters
    for a URL, using the `urllib.parse`_ ``quote`` function.

.. _urllib.parse: https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote
.. _webbrowser: https://docs.python.org/3/library/webbrowser.html

Submitting Your Work
--------------------

Create a github repository to contain your mashup work. Start by populating it
with the script as we finished it today (mashup_5.py).

As you implement the above features, commit early and commit often.

When you're ready for us to look it over, email a link to your repository to
Maria and I.

