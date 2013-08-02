Installing the ZODB
===================

This takes some work.  Start early.


*nix Prep
---------

The ZODB uses C extensions, and so installing it on OS X or Linux requires a
compiler and python's development headers. On linux systems, this means using
the system package manager:

**Ubuntu/Debian**:

    $ sudo apt-get install python-dev


For **OS X** my usual approach is to install XCode. It's *big*, so expect it
to take a while if you don't already have it. Once you've downloaded it you'll
also need to install the command-line tools:

* Open XCode
* Open the XCode menu, then click 'Preferences' > 'Downloads' > 'Install
  Command Line Tools'
* Once this is done, you can close XCode again

If XCode is too much, there appear to be alternatives available.  I have not
tried any of these, but would appreciate any testimonial to their effectiveness:

* There is a stand-alone package of the command-line tools available through
  the apple developer center: https://developer.apple.com/downloads

* Kenneth Reitz has a github repository with instructions and installers for a
  stand-alone gcc compiler: https://github.com/kennethreitz/osx-gcc-installer

If you use either of these methods to get gcc, you will still require the
python development headers. Installing a new version of Python using the
python.org installers or MacPorts or Homebrew should suffice to get this done.


**Windows**: See the next section

Windows Prep
------------

Although there are pre-compiled binaries available for Windows, you'll need
one `.bat` file to get them to work properly. To get that file, you'll need to
install Visual Studio 2008 Express:

* Download the installer (894MB):
  http://download.microsoft.com/download/8/B/5/8B5804AD-4990-40D0-A6AA-CE894CBBB3DC/VS2008ExpressENUX1397868.iso
* Extract the files to a folder (call it VS2008ExpressENUX1397868—it will be
  2.68GB) using something like 7zip
* Inside that folder double-click on Setup.hta
* On the screen that comes up, click on the installer for Visual C++ 2008
  Express Edition and follow the instructions. **Note**: It does work if you
  include the following two options which are pre-selected for you: (1) MSDN
  Express Library for Visual Studio 2008, and (2) Microsoft SQL Server 2005
  Express Edition (x86).

The above will work for 32-bit Windows.  If you are using 64-bit Windwos, try
using the instructions on this wiki:

    http://wiki.cython.org/64BitCythonExtensionsOnWindows

I have yet to hear of anyone getting Python or C-extensions running on Windows
8 without a titanic struggle.


Virtualenv
----------

With that prep work out of the way, you're ready to start. First, you'll need
to set up a virtualenv. Working with virtualenv is something we will cover in
session 3, so **if you are not comfortable or have never seen virtualenv
before, you probably want to wait to take these next steps**.

These instructions assume you will be manually creating a virtualenv rather
than installing virtualenv with pip or easy_install. If you need a copy of the
``virtualenv.py`` file, you can find it in the same ``resources/common``
directory where these instructions are located. Once you have a copy, simply:

.. code-block:: bash

    $ python2.7 virtualenv.py pyramidenv
    ...
    $ source pyramidenv/bin/activate
    (pyramidenv)$ 

Windows users: ``> pyramidenv\Scripts\activate``


Install ZODB
------------

If you're on OS X or Linux:

    (pyramidenv)$ easy_install ZODB3==3.10.5

This will take some time. If you get errors, contact me directly or via the
Google Group.

Windows users, you'll have it a bit easier here. You have to install a binary
egg:

    [pyramidenv]> pip install --egg ZODB3==3.10.5

Self Evaluation
---------------

At this point, you can check your work. Fire up a python interpreter in your
virtualenv:

.. code-block:: bash

    (pyramidenv)$ python
    >>> import ZODB
    >>> ^D
    (pyramidenv)$

If you get an ImportError when you try that, you're not done.  Contact me.

If you get no errors, you are ready to go for our final sessions.
