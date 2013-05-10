Internet Programming with Python
================================

.. image:: img/plone-icon-256-white-bg.png
    :align: left
    :width: 38%

| Week 9: System Example: 
| The Plone CMS

.. class:: intro-blurb right

Content management done right.


.. class:: image-credit

The Plone logo is a trademark of the Plone Foundation.

This Week
---------

We'll have an introduction to the Plone Content Management System

.. class:: incremental

We'll see a demo of this system in action

.. class:: incremental

We'll talk a bit about the differences between a system and a framework

.. class:: incremental

We'll spend the rest of the time working on your Final Projects.

What is Plone?
--------------

Plone is a Content Management System

.. class:: incremental

**System**: A tightly integrated set of tools oriented to a purpose

.. class:: incremental

**Content Management**: The task of creating, editing, organizing and
controlling access to content throughout it's lifecycle.

.. class:: incremental

**Content**: Information and materials stored in a website which has value
that can be maintained over time.

Plone Features
--------------

Plone comes with an extensive feature set OOTB:

.. class:: incremental

* Fully translated UI, with over 40 languages supported
* Fine-grained permissions system for access to content and actions
* Built-in, fully configurable user and group management
* Workflow configurable per content type
* Automatic and configurable versioning of content
* Built-in system for event handling, including user notifications
* Built-in content rules allowing for complex automation of common actions
* Content Type framework allowing for TTW creation of new types
* Theme engine allowing for TTW creation of custom themes

And There's More
----------------

By installing additional packages in the core distribution get:

.. class:: incremental

* In-place content staging (working copies)
* Powerfully flexible caching
* Per-location workflow configuration

.. class:: incremental

And with other add-ons you can have

.. class:: incremental

* Multi-lingual content
* TTW form building
* layered calendars
* much, much more...


Separators
----------

What is it that separates Plone from other web-based CMS solutions?

.. class:: incremental

* Simplicity
* Scalability
* Speed
* Security


Simplicity
----------

Plone features an in-place content editing model

.. class:: incremental

Users create content in the place where they want it to be located

.. class:: incremental

There is no separate authoring back-end where you must go to create and place
content

.. class:: incremental

All aspects of management: workflow, security, versioning and staging can be
managed in-place.

Scalability
-----------

Plone is fast and easy enough to support small websites

.. class:: incremental

But you can scale it up to the very largest sizes

.. class:: incremental

Corporate or Education intranets with over 100,000 pieces of content are not
unusual.

Speed
-----

Out of the box, Plone can serves content faster than Drupal, WordPress or
SharePoint.

.. class:: incremental

With the simple installation of a caching add-on, this speed is greatly
accelerated.

.. class:: incremental

Support for load-balancing and HTTP acceleration means you can push it further
yet.

Security
--------

Issues reported for various technologies in CVE (last 3 years):

.. class:: incremental

* Plone: 13 (9)
* Zope: 27 (9)
* Python: 111 (65)
* Drupal: 371 (269)
* Joomla: 653 (441)
* MySQL: 282 (84)
* PostgreSQL: 82 (22)
* PHP: 18,859 (5,813)

.. class:: incremental

And then there is Plone's true secret weapon

Community
---------

.. image:: img/plone_conf_2012.jpg
    :align: center
    :width: 85%

About the Community
-------------------

Plone has more than 300 *active* core contributors.

.. class:: incremental

The `add-on ecosystem <http://github.com/collective>`_ contains ~850 public
repositories

.. class:: incremental

The community averages one major sprint each month, in locations in Asia,
Africa, Europe, South America, North America and Australia.

.. class:: incremental

Plone is a "do-ocracy", meaning that your standing in the community is 
determined by your contributions

History
-------

In 1999 Plone is a theme for the Zope Content Management Framework.

.. class:: incremental

* By 2001, it had grown popular enough to warrant a public release.
* In 2003 Plone 1.0 is released
* In 2004 Plone 2.0 brings the Archetypes Content Type Framework
* In 2005 Plone 2.1 brings default content types via Archetypes
* In 2006 Plone 2.5 brings versioning and pluggable authentication
* In 2007 Plone 3.0 integrates the Zope Component Architecture
* In 2010 Plone 4.0 brings speed and the Dexterity Content Framework
* This week, Plone 4.3rc1 brings through the web theming

Installation
------------

Plone is an application that runs *on top of* the Zope Application Server.

.. class:: incremental

Installing Plone involves installing Zope, the ZODB and a number of other 
technologies.

.. class:: incremental

Forget all that, just use the installers

.. class:: incremental

Go to http://plone.org, click "download now", pick the right installer and go.

Running Plone
-------------

After running the installer of your choice, you start Plone from the command
line:

.. class:: incremental

::

    $ bin/instance fg

.. class:: incremental

This runs plone in the *foreground* which allows you to see errors if they
happen and get tracebacks.

.. class:: incremental

Once you see the message "Zope Ready to handle requests", the system is running

Setting up Your First Site
--------------------------

When the site is running, you'll find it at localhost:8080

.. class:: incremental

Load that page and you see a message instructing you to add your first site

.. class:: incremental

Click the button, and your site is created with a bit of default content

.. class:: incremental

At that point, you can start managing content

Demo of Plone
-------------

.. class:: big-centered

Let's see it in action

Take-away
---------

Plone is a full-featured and flexible Content Management System

.. class:: incremental

Plone customization is generally going to be *integration* - altering existing
functionality to fit business needs.

.. class:: incremental

Treating Plone as a *framework* - trying to build arbitrary web applications -
is not easy.

.. class:: incremental

But if the feature set it offers is in largely in line with your needs, you
won't find a better tool.

Reminder
--------

Your final projects are **due Friday at noon**.

.. class:: incremental

I will not accept submissions that arrive after noon on Friday (March 15).

.. class:: incremental

You will need to supply:

.. class:: incremental

* A Link to your site deployed online (your VM, in the cloud, ...)
* A Link to **your project source code repository** in Github.
* Text describing **the goals and outcomes** of your project. 
* Instructions on **how I can run your project locally** on my laptop

Another reminder
----------------

.. class:: big-centered

**LEAVE TIME FOR DEPLOYMENT**

Final Word
----------

.. class:: big-centered

**thank you all**

Lab Time
--------

For the rest of today, we work on your projects.
