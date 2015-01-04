Internet Programming with Python
================================

.. image:: img/django-pony.png
    :align: left
    :width: 50%

Session 8: Extending Django

.. class:: intro-blurb right

Wherein we extend our Django blog app.

.. class:: image-credit

image: http://djangopony.com/


Last Week
---------

Last week, we created a nice, simple Django microblog application.

.. class:: incremental

Over the week, as your homework, you made some modifications to improve how it
works.

.. class:: incremental

There's still quite a bit more we can do to improve this application.

.. class:: incremental

And today, that's what we are going to do.


Preparation
-----------

In order for this to work properly, we'll need to have a few things in place.

.. container:: incremental small

    First, we'll start from a canonical copy of the microblog.  Make a fork of
    the following repository to your github account:

    .. code-block::
        :class: small

        https://github.com/cewing/django-microblog

.. container:: incremental small

    Then, clone that repository to your local machine:

    .. code-block:: bash
        :class: small

        $ git clone https://github.com/<your_name>/django-microblog.git
        or
        $ git clone git@github.com:<your_name>/django-microblog.git


Connect to Your Partner
-----------------------

Finally, you'll want to connect to your partner's repository, so that you can
each work on your own laptop and still share the changes you make.

.. container:: incremental small

    First, add your partner's repository as ``upstream`` to yours:

    .. code-block:: bash
        :class: small

        $ git remote add upstream https://github.com/<partner>/django-microblog.git
        or
        $ git remote add upstream git@github.com:<partner>/django-microblog.git

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

    $ git fetch --all
    $ git branch -a
    * master
      remotes/origin/master
      remotes/upstream/master
    $ git merge upstream/master

.. class:: small

3. The new driver continues working from where their partner left off.


Homework
--------

For this week's homework, you will need to install the Zope Object Database
(ZODB)

Instructions for this `may be found here`_.

.. _may be found here: https://github.com/UWPCE-PythonCert/training.python_web/blob/master/resources/common/zodb-install-instructions.rst

This is not trivial work.  Please be sure to start early in the week so if
there is trouble, you'll be able to recover.

