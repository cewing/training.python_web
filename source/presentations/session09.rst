**********
Session 09
**********

.. figure:: /_static/django-pony.png
    :align: center
    :width: 60%

    image: http://djangopony.com/

Extending Django
================

.. rst-class:: large

Wherein we extend our Django blog app.


Last Week
---------

Last week, we created a nice, simple Django microblog application.

.. rst-class:: build
.. container::

    Over the week, as your homework, you made some modifications to improve how
    it works.

    There's still quite a bit more we can do to improve this application.

    And today, that's what we are going to do.


Preparation
-----------

In order for this to work properly, we'll need to have a few things in place.

.. rst-class:: build
.. container::

    First, we'll start from a canonical copy of the microblog.  Make a fork of
    the following repository to your github account::

        https://github.com/cewing/django-microblog

    Then, clone that repository to your local machine:

    .. code-block:: bash

        $ git clone https://github.com/<your_name>/django-microblog.git


Connect to Your Partner
-----------------------

Finally, you'll want to connect to your partner's repository, so that you can
each work on your own laptop and still share the changes you make.

.. rst-class:: build
.. container::

    First, add your partner's repository as ``upstream`` to yours:

    .. code-block:: bash

        $ git remote add upstream https://github.com/<partner>/django-microblog.git

    Then, fetch their copy so that you can easily merge their changes later:

    .. code-block:: bash

        $ git fetch --all


While You Work
--------------

Now, when you switch roles during your work, here's the workflow you can use:

.. rst-class:: build
.. container::

    .. container::

        1. The current driver commits all changes and pushes to their repository:

        .. code-block:: bash

            $ git commit -a -m "Time to switch roles"
            $ git push origin master

    .. container::

        2. The new driver fetches and merges changes made upstream:

    .. code-block:: bash

        $ git fetch --all
        $ git branch -a
        * master
          remotes/origin/master
          remotes/upstream/master
        $ git merge upstream/master

    3. The new driver continues working from where their partner left off.
