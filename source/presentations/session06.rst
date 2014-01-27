Python Web Programming
======================

.. image:: img/flask_cover.png
    :align: left
    :width: 50%

Session 6: Extending Flask

.. class:: intro-blurb right

| "Web Development,
| one drop at a time"

.. class:: image-credit

image: Flask Logo (http://flask.pocoo.org/community/logos/)


Last Week
---------

Last week, we created a nice, simple flask microblog application.

.. class:: incremental

Over the week, as your homework, you added in authentication and flash
messaging.

.. class:: incremental

There's still quite a bit more we can do to improve this application.

.. class:: incremental

And today, that's what we are going to do.


Pair Programming
----------------

`Pair programming <http://en.wikipedia.org/wiki/Pair_programming>`_ is a
technique used in agile development.

.. class:: incremental

The basic idea is that two heads are better than one.

.. class:: incremental

A pair of developers work together at one computer. One *drives* and the other
*navigates*

.. class:: incremental

The driver can focus on the tactics of completing a function, while the
navigator can catch typos, think strategically, and find answers to questions
that arise.


Pair Up
-------

We are going to employ this technique for todays class.

.. class:: incremental

So take the next few minutes to find a partner and pair up. You must end up
sitting next to your partner, so get up and move.

.. class:: incremental

One of you will start as the driver, the other as the observer.

.. class:: incremental

About every 20 minutes, we will switch, so that each of you can take a turn
driving.


Preparation
-----------

In order for this to work properly, we'll need to have a few things in place.

.. container:: incremental

    First, you'll all need to make sure that you have the very latest code from the
    class repository available on your local machine::

        $ git add remote uwpce git@github.com:UWPCE-PythonCert/training.python_web.git

.. container:: incremental

    First, you both will need to make a branch of the class repository that you
    can work on::

        $ git checkout -b session06-class

