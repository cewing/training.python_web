.. slideconf::
    :autoslides: False

***********************
An Introduction To Venv
***********************

.. slide:: An Introduction To Venv
    :level: 1

    This document contains no slides.

In this tutorial you'll learn a bit about the `pyvenv`_ command and the
``venv`` module that powers it. You'll learn how to create self-contained
Python environments in order to practice safe development and manage package
dependency conflicts.

Working with Virtual Environments
=================================

.. rst-class:: large

| For every package 
| installed in the
| system Python, the 
| gods kill a kitten

.. rst-class:: build
.. container::

    | - me

Why Virtual Environments?
-------------------------

.. rst-class:: build

* You will need to install packages that aren't in the Python standard
  Library
* You often need to install *different* versions of the *same* library for
  different projects
* Conflicts arising from having the wrong version of a dependency installed can
  cause long-term nightmares
* Use `pyvenv`_ ...
* **Always**

.. _pyvenv: https://docs.python.org/3/library/venv.html

Creating a Venv
---------------

Since version 3.3, Python has come with a built-in ``venv`` module.  This
module provides a command you can use to create virtual environments:
``pyvenv``

.. rst-class:: build
.. container::

    The basic usage for this command is as follows:

    .. code-block:: bash
    
        $ pyvenv /path/to/new/environment

    On Windows you'll need something a bit different:

    .. code-block:: posh
    
        c:\Temp>c:\Python35\python -m venv myenv

    Unless you have the Python executable in your path, in which case this:

    .. code-block:: posh
    
        c:\Temp>python -m venv myenv


.. nextslide::

In any of these command forms, the name of the new virtual environment
(``myenv``) is arbitrary.

.. rst-class:: build
.. container::

    I suggest that you name virtual environments to match the project for which
    the environment is to be used.

    I also suggest that you keep your virtual environments *in the same
    directory* as the project code you are writing.

.. nextslide::

Let's make one for demonstration purposes:

.. code-block:: bash

    $ pyvenv demoenv
    $ ls demoenv
    bin     include     lib     pyvenv.cfg


.. nextslide:: What Happened?

When you ran that command, a couple of things took place:

.. rst-class:: build

* A new directory with your requested name was created
* A new Python executable was created in <ENV>/bin (<ENV>/Scripts on Windows)
* The new Python was cloned from your system Python (where virtualenv was
  installed)
* The new Python was isolated from any libraries installed in the old Python
* Setuptools was installed so you have ``easy_install`` for this new python
* Pip was installed so you have ``pip`` for this new python

Activation
----------

Every virtual environment you create contains an executable Python command.

.. rst-class:: build
.. container::

    If you do a quick check to see which Python executable is found by your
    terminal, you'll see that it is not the one:

    .. container::
    
        .. code-block:: bash

            $ which python
            /usr/bin/python

        in powershell:

        .. code-block:: posh
        
            $ gcm python
            ...

    You can execute the new Python by explicitly pointing to it:

    .. code-block:: bash

        $ ./demoenv/bin/python -V
        Python 3.5.0

.. nextslide::

But that's tedious and hard to remember.

.. rst-class:: build
.. container::

    Instead, ``activate`` your virtual environment using a shell command:

    +----------+------------+----------------------------------------+
    | Platform | Shell      | Activation Command                     |
    +==========+============+========================================+
    | Posix    | bash/zsh   | ``$ source <venv>/bin/activate``       |
    +          +------------+----------------------------------------+
    |          | fish       | ``$ . <venv>/bin/activate.fish``       |
    +          +------------+----------------------------------------+
    |          | csh/tcsh   | ``$ source <venv>/bin/activate.csh``   |
    +----------+------------+----------------------------------------+
    | Windows  | cmd.exe    | ``C:> <venv>/Scripts/activate.bat``    |
    +          +------------+----------------------------------------+
    |          | powershell | ``PS C:> <venv>/Scripts/Activate.ps1`` |
    +----------+------------+----------------------------------------+

.. nextslide::

Notice that when a virtualenv is *active* you can see it in your command
prompt:

.. rst-class:: build
.. container::

    .. code-block:: bash

        (demoenv)$

    So long as the virtualenv is *active* the ``python`` executable that will
    be used will be the new one in your ``demoenv``.

Installing Packages
-------------------

Since ``pip`` is also installed, the ``pip`` that is used to install new
software will also be the one in ``demoenv``.

.. code-block:: bash

    (demoenv)$ which pip
    /Users/cewing/demoenv/bin/pip

.. rst-class:: build
.. container::

    This means that using these tools to install packages will install them
    *into your virtual environment only*

    The are not installed into the system Python.

    Let's see this in action.

.. nextslide::

We'll install a package called ``docutils``

.. rst-class:: build
.. container::

    It provides tools for creating documentation using ReStructuredText

    Install it using pip (while your virtualenv is active):

    .. code-block:: bash

        (demoenv)$ pip install docutils
        Downloading/unpacking docutils
          Downloading docutils-0.11.tar.gz (1.6MB): 1.6MB downloaded
          Running setup.py (path:/Users/cewing/demoenv/build/docutils/setup.py) egg_info for package docutils
            ...
            changing mode of /Users/cewing/demoenv/bin/rst2xml.py to 755
            changing mode of /Users/cewing/demoenv/bin/rstpep2html.py to 755
        Successfully installed docutils
        Cleaning up...

.. nextslide::

And now, when we fire up our Python interpreter, the docutils package is
available to us:

.. code-block:: pycon

    (demoenv)$ python
    Python 3.5.0 (default, Sep 16 2015, 10:42:55)
    [GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.49)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import docutils
    >>> docutils.__path__
    ['/Users/cewing/projects/uwpce/training.python_web/testenvs/sess01/demoenv/lib/python3.5/site-packages/docutils']
    >>> ^d
    (demoenv)$

.. nextslide:: Side Effects

Like some other Python libraries, the ``docutils`` package provides a number of
executable scripts when it is installed.

.. rst-class:: build
.. container::

    You can see these in the ``bin`` directory inside your virtualenv:

    .. code-block:: bash

        (demoenv)$ ls ./demoenv/bin
        ...
        python
        rst2html.py
        rst2latex.py
        ...

    These scripts are set up to execute using the Python with which they were
    built.

    Running these scripts *from this location* will use the Python executable
    in your virtualenv, *even if that virtualenv is not active*!

Deactivation
------------

So you've got a virtual environment created and activated so you can work with
it.

.. rst-class:: build
.. container::

    Eventually you'll need to stop working with this ``venv`` and switch
    to another

    It's a good idea to keep a separate ``venv`` for every project you
    work on.

    When a ``venv`` is active, all you have to do is use the
    ``deactivate`` command:

    .. code-block:: bash

        (demoenv)$ deactivate
        $ which python
        /usr/bin/python

    Note that your shell prompt returns to normal, and now the executable
    Python found when you check ``python`` is the system one again.

Cleaning Up
-----------

The final advantage that ``venv`` offers you as a developer is the ability to
easily remove a batch of installed Python software from your system.

.. rst-class:: build
.. container::

    Consider a situation where you installed a library that breaks your Python
    (it happens)

    If you are working in your system Python, you now have to figure out what
    that package installed

    You have to figure out where it is

    And you have to go clean it out manually.

    With ``venv`` you simply remove the directory ``venv`` created when you
    started out.

.. nextslide::

Let's do that with our ``demoenv``:

.. rst-class:: build
.. container::

    .. code-block:: bash

        $ rm -r demoenv

    And that's it.

    The entire environment and all the packages you installed into it are now
    gone.

    There are no traces left to pollute your world.
