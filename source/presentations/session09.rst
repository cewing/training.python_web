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

    **For the time being, all these actions should only be taken by one
    partner**.

    First, we'll start from a canonical copy of the microblog.  Make a fork of
    the following repository to your github account::

        https://github.com/cewing/djangoblog_uwpce.git

    Then, clone that repository to your local machine:

    .. code-block:: bash

        $ git clone https://github.com/<your_name>/djangoblog_uwpce.git


Connect to Your Partner
-----------------------

Finally, you'll need to add your partner as a collaborator for your new
repository.

.. rst-class:: build
.. container::

    Go to the *settings* for your repository.

    Click the *collaborators* tab on the left side of the window (you'll need
    to enter your github password).

    Look up your partner by email address or github username.

    Add them.

    Then your partner can clone the repository to their desktop too.

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

        2. The new driver gets the changes:

        .. code-block:: bash

            $ git pull origin master

    3. The new driver continues working from where their partner left off.
    4. PROFIT.....

Homework
========

Next week, we will deploy your Django application to a server.

.. rst-class:: build
.. container::

    To help illustrate the full set of tools at our disposal, we'll go a bit
    overboard for this.

    We'll be setting up an HTTP server, proxying to a WSGI server serving your
    Django app.

    We'll do this all "In the cloud" using Amazon's `AWS`_ service.

    Before class starts, you'll need to accomplish a few non-programming tasks

.. _AWS: http://aws.amazon.com/free

Sign Up For AWS
---------------

Begin by going to the `AWS homepage`_ and clicking on the large, yellow button
that reads "Sign In to the Console".

.. rst-class:: build
.. container::

    On the sign-in page that appears, click the radio button for 'I am a new
    user', fill in your email address, and then click through to begin the
    sign-up process.

    You will be required to provide credit card information.

    If you are still eligible for the AWS free tier, you will not incur any
    charges for work you do in this class.

.. _AWS homepage: http://aws.amazon.com


Set Up an IAM User
------------------

Once you've signed up for an account take the following actions:

* `Create an IAM user`_ and place them in a group with Power User access. (Search for PowerUser when selecting a policy for your group).

  * Set up Security Credentials for that IAM user.
  * Save these Security Credentials in a safe place so you can use them for class.

.. _Create an IAM user: http://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html

Prepare for Login
-----------------

* `Create a Keypair`_

  * Choose the 'US West (Oregon)' region since it's geographically closest to you.</li>
  * When you download your private key, save it to ~/.ssh/pk-aws.pem
  * Make sure that the private key is secure and useable by doing the following command

    * ``$ chmod 400 ~/.ssh/pk-aws.pem``

* `Create a custom security group`_

  * The security group should be named 'ssh-access'
  * Add one custom TCP rule
    * allow port 22
    * allow addresses 0.0.0.0/0

.. _Create a Keypair: http://docs.aws.amazon.com/gettingstarted/latest/wah/getting-started-create-key-pair.html
.. _Create a custom security group: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html
