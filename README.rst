.. contents::

Introduction
============

This package provides the source for all lecture materials for a 10-session
course in Web Development using Python.

This version of the documentation is used for a one-week Python Web
Programming Workshop taught by `Cris Ewing`_. This workshop is being `offered
August 5-9, 2013`_ on the campus of the University of North Carolina in Chapel Hill, NC.

.. _offered August 5-9, 2013: http://trizpug.org/boot-camp/pywebpw13/
.. _Cris Ewing: http://www.linkedin.com/profile/view?id=19741495

Building The Documentation
--------------------------

This documentation is built using docutils and Sphinx. The package uses
`zc.buildout` to manage setup and dependencies. This package uses the v1
`bootstrap.py` script.

After cloning this package from the repository, do the following::

  $ cd training.python_web  # the location of your local copy
  $ python bootstrap.py  # must be Python 2.6 or 2.7
  $ bin/buildout
  $ bin/sphinx   # to build the main documentation and course outline
  $ bin/build_s5   # to build the class session presentations

At the end of a successful build, you will find a ``build/html`` directory,
containing the completed documentation and presentations.

.. _zc.buildout: https://pypi.python.org/pypi/zc.buildout/
.. _bootstrap.py: http://downloads.buildout.org/1/bootstrap.py

Reading The Documentation
-------------------------

A rendered version of this documentation is maintained online.  You can view
the latest updates at http://cewing.github.com/training.python_web/

LICENSE
=======

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a copy of
this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send
a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View,
California, 94041, USA.

A copy of this license in text format is included in this package under the
``docs`` directory
