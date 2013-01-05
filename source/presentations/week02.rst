Internet Programming with Python
================================

.. image:: img/protocol.png
    :align: left
    :width: 45%

Week 2: Web Protocols

.. class:: intro-blurb

Wherein we learn about the languages that the internet speaks and how to
choose the right one for our message

But First
---------

.. class:: big-centered

Review from the Assignment

And Second
----------

.. class:: big-centered

Questions from the Reading?

And Now...
----------

.. image:: img/protocol_sea.png
    :align: center
    :width: 50%

What is a Protocol?
-------------------

.. class:: incremental big-centered

a set of rules or conventions

.. class:: incremental big-centered

governing communications


Protocols IRL
-------------

Life has lots of sets of rules for how to do things.

.. class:: incremental

* What do you do on a first date?

* What do you do in a job interview?

* What do (and don't) you talk about at a dinner party?

* ...?

Protocols In Computers
----------------------

Digital life has lots of rules too:

.. class:: incremental

* how to identify yourself

* how to find a partner

* how to ask for information

* how to provide answers

* how to say goodbye

What does this look like?
-------------------------

SMTP::

    S: 220 foo.com Simple Mail Transfer Service Ready
    C: EHLO bar.com
    S: 250-foo.com greets bar.com
    S: 250-8BITMIME
    S: 250-SIZE
    S: 250-DSN
    S: 250 HELP
    C: MAIL FROM:<Smith@bar.com>
    S: 250 OK
    C: RCPT TO:<Jones@foo.com>
    S: 250 OK
    ...

What does this look like?
-------------------------

SMTP::

    ...
    C: RCPT TO:<Green@foo.com>
    S: 550 No such user here
    C: DATA
    S: 354 Start mail input; end with <CRLF>.<CRLF>
    C: Blah blah blah...
    C: ...etc. etc. etc.
    C: .
    S: 250 OK
    C: QUIT
    S: 221 foo.com Service closing transmission channel
