Internet Programming with Python
================================

Lab Time
--------

For this lab, we'll be building a basic HTTP server.

* update your fork of the class repository by pulling from the ``upstream`` remote

* find the folder ``assignments/week02/lab`` and open ``echo_server.py``

    * this is a canonical example of what we built last week

* We'll move in steps to turn this into an HTTP server.

Lab Time - Step 1
-----------------

First, echo an HTTP request

* Run `echo_server.py` in a terminal

* Point your browser at ``http://localhost:5000``, what do you get back?

* Save the script as ``http_serve1.py``, then edit it to make it return the
  HTML you find in ``tiny_html.html``

* What does this look like?

Lab Time - Step 2
-----------------

Return a proper HTTP response:

* Save the file as ``http_serve2.py``

* Add a new method that takes a string 'body' and returns a proper ``200 OK``
  HTTP response.  Call the method ``ok_response``.

* Bonus Points: add a GMT ``Date:`` header in the proper format (RFC-1123).
  *hint: see email.utils.formatdate in the python standard library*

* How does the returned HTML look now?

Lab Time - Step 3
-----------------

Parse an incoming request to get the URI:

* Save the file as ``http_serve3.py``

* Add a new method called ``parse_request`` that takes a request and returns a
  URI. Have the server print the URI to the console (rudimentary logging).

* Make sure that the method validates that the incoming request is HTTP and
  that the verb is ``GET``. If either is not true, it should raise a
  ValueError

* Bonus points: add an ``client_error_response`` method that returns an
  appropriate HTTP code if the validation from ``parse_request`` fails. What
  is the right response code?

Lab Time - Step 4
-----------------

Serve directory listings:

* Save the file as ``http_serve4.py`` * Add a method called ``resolve_uri``
  which takes as an argument the URI returned from our previous step and
  returns an HTTP response. The method should start from a given directory
  ('web') and check the URI:

    * If the URI names a directory, return the content listing as a ``200 OK``
    
    * If the URI names a file, raise a NotImplementedError (coming soon)
    
    * If the URI does not exist, raise a ValueError

* Bonus points: add a ``notfound_response`` method that returns a proper ``404
  Not Found`` response to the client. Use it when appropriate. (where is
  that?)

Lab Time - Step 5
-----------------

Serve different types of files:

* Save the file as ``http_serve5.py``

* Update the ``resolve_uri`` method. If the URI names a file, return it as the
  body of a ``200 OK`` response.

* You'll need a way to return the approprate ``Content-Type:`` header.

* Support at least ``.html``, ``.txt``, ``.jpeg``, and ``.png`` files

* Try it out.

.. class:: incremental

You've now got a reasonably functional HTTP web server.  Congratulations!

Assignment
----------

Using what you've learned this week, take your new webserver to the next
level. Accomplish as many of the following as you can:

* If you were unable to complete the first five steps in class, circle back
  and finish them

* Complete the 'Bonus point' parts from the first five steps, if you haven't
  already done so

* Format your directory listing as HTML

* In the HTML directory listing, make the files clickable links

* Add a new, dynamic endpoint. If the URI /time-page is requested, return an
  HTML page with the current time displayed.

Submitting the Assignment
-------------------------

* Copy your final html server into the ``assignments/week02/athome``
  directory in your fork of the repository.

* Copy the ``assignments/week02/lab/web`` directory into
  ``assignments/week02/at_home``

* Make a new plain-text file at the top level of the web directory. Tell me
  what you did in it.

* Make a new pull request for the week02 assignments.

* I should be able to run the server on my local machine, open your plain text
  file in my browser, and evaluate your work from there.

* For bonus points, set the server running on your VM, with the ``web`` home
  directory. I should be able to load http://yourserver.bluboxgrid.com:50000
  in my web browser and evaluate your results.

Lightning Talks
---------------

.. class:: big-centered

Ready, Steady, GO!