.. contents::

Introduction
============

This package provides the source for all lecture materials for a 10-session
course in Web Development using Python.

This package provides the source for all lecture materials used for the
`Internet Programming in Python`_ section of the `Certificate in Python
Programming`_ offered by the `University of Washington Professional &
Continuing Education`_ program. This version of the documentation is used for
the Winter 2016 instance of the course, Taught by `Cris Ewing`_

.. _Internet Programming in Python: http://www.pce.uw.edu/courses/internet-programming-python/downtown-seattle-winter-2016/
.. _Certificate in Python Programming: http://www.pce.uw.edu/certificates/python-programming.html
.. _University of Washington Professional & Continuing Education: http://www.pce.uw.edu/
.. _Cris Ewing: http://www.linkedin.com/profile/view?id=19741495

This course is taught using Python 3.

This documentation builds both an HTML version of the course lectures (for the
students) and a set of slides (for the instructor).  It uses the Python-based
documentation tool `Sphinx`_ and the `hieroglyph`_ sphinx extension. Shell
examples use `iPython` and tests are written for `pytest`. The build
environment is managed using `virtualenv` and `pip`

.. _iPython: http://ipython.org/
.. _Sphinx: http://sphinx-doc.org/
.. _hieroglyph: http://docs.hieroglyph.io/en/latest/
.. _pytest: http://pytest.org/latest/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _pip: https://pip.pypa.io/en/stable

Building The Documentation
--------------------------

To build the documentation locally, begin by cloning the project to your
machine:

.. code-block:: bash

    $ git clone https://github.com/cewing/training.python_web.git

Change directories into the repository, then create a virtualenv using Python
3:

.. code-block:: bash

    $ cd training.python_web
    $ virtualenv --python /path/to/bin/python3.4 .
    Running virtualenv with interpreter /path/to/bin/python3.4
    New python executable in training.python_web/bin/python3.4
    Also creating executable in training.python_web/bin/python
    Installing setuptools, pip...done.

Install the requirements for the documentation using pip:

.. code-block:: bash

    $ bin/pip install -r requirements.pip
    ...

    Successfully installed Babel-2.0 Jinja2-2.8 MarkupSafe-0.23 Pygments-2.0.2 Sphinx-1.3.1 alabaster-0.7.6 appnope-0.1.0 decorator-4.0.2 docutils-0.12 gnureadline-6.3.3 hieroglyph-0.7.1 ipython-4.0.0 ipython-genutils-0.1.0 path.py-8.1 pexpect-3.3 pickleshare-0.5 py-1.4.30 pytest-2.7.2 pytz-2015.4 simplegeneric-0.8.1 six-1.9.0 snowballstemmer-1.2.0 sphinx-rtd-theme-0.1.8 traitlets-4.0.0

Once that has successfully completed, you should be able to build both the html
documentation and the slides using the included Makefile.

.. code-block:: bash

    $ make html
    ...

    Build finished. The HTML pages are in build/html.

    (webdocs)$ make slides
    ...

    Build finished. The HTML slides are in build/slides.

.. note:: If you prefer to build your virtualenvs in other ways, you will need
          to adjust the `BINDIR` variable in `Makefile` to fit your reality.



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
