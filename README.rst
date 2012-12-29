.. contents::

Introduction
============

This package provides the source for all lecture materials used for the
`Internet Programming in Python`_ section of the `Certificate in Python
Programming`_ offered by the University of Washington Professional & Continuing
Education program. This version of the documentation is used for the Winter
2013 instance of the course, taught by `Cris Ewing`_.

.. _Internet Programming in Python: http://www.pce.uw.edu/courses/internet-programming-python/downtown-seattle-winter-2013/
.. _Certificate in Python Programming: http://www.pce.uw.edu/certificates/python-programming.html
.. _Cris Ewing: http://www.linkedin.com/profile/view?id=19741495

Building The Documentation
--------------------------

After cloning this package from the repository, do the following::

  $ cd training.python_web  # the location of your local copy
  $ python bootstrap.py  # must be Python 2.6 or 2.7
  $ bin/buildout
  $ bin/sphinx   # to build the main documentation and course outline
  $ bin/build_s5   # to build the class session presentations

At the end of a successful build, you will find a ``build/html`` directory,
containing the completed documentation and presentations.

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
