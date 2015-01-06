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

About every 20-30 minutes, we will switch, so that each of you can take a turn
driving.


Preparation
-----------

In order for this to work properly, we'll need to have a few things in place.

.. container:: incremental small

    First, we'll start from a canonical copy of the microblog.  Make a fork of
    the following repository to your github account:

    .. code-block::
        :class: small

        https://github.com/UWPCE-PythonCert/training.sample-flask-app

.. container:: incremental small

    Then, clone that repository to your local machine:

    .. code-block:: bash
        :class: small

        $ git clone https://github.com/<your_name>/training.sample-flask-app.git
        or
        $ git clone git@github.com:<your_name>/training.sample-flask-app.git

Connect to Your Partner
-----------------------

Finally, you'll want to connect to your partner's repository, so that you can
each work on your own laptop and still share the changes you make.

.. container:: incremental small

    First, add your partner's repository as ``upstream`` to yours:

    .. code-block:: bash
        :class: small

        $ git remote add upstream https://github.com/<partner>/training.sample-flask-app.git
        or
        $ git remote add upstream git@github.com:<partner>/training.sample-flask-app.git

.. container:: incremental small

    Then, fetch their copy so that you can easily merge their changes later:

    .. code-block:: bash
        :class: small

        $ git fetch upstream

While You Work
--------------

.. class:: small

Now, when you switch roles during your work, here's the workflow you can use:

.. class:: small

1. The current driver commits all changes and pushes to their repository:

.. code-block:: bash
    :class: small

    $ git commit -a -m "Time to switch roles"
    $ git push origin master

.. class:: small

2. The new driver fetches and merges changes made upstream:

.. code-block:: bash
    :class: small

    $ git fetch upstream master
    $ git branch -a
    * master
      remotes/origin/master
      remotes/upstream/master
    $ git merge upstream/master

.. class:: small

3. The new driver continues working from where their partner left off.


Homework
--------

For this week, please read and complete the Introduction to Django tutorial
linked from the class website and from the course outline.

You will be expected to have successfully completed that tutorial upon arrival
in class for our next session.

We will begin our work starting from where it leaves off.

