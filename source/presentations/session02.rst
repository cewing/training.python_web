Internet Programming with Python
================================

.. image:: img/protocol.png
    :align: left
    :width: 45%

Week 2: Web Protocols

.. class:: intro-blurb

Wherein we learn about the languages that machines speak to each other


What is a Protocol?
-------------------

.. class:: incremental center

a set of rules or conventions

.. class:: incremental center

governing communications


Protocols IRL
-------------

Life has lots of sets of rules for how to do things.

.. class:: incremental

* What do you say when you get on the elevator?

* What do you do on a first date?

* What do you wear to a job interview?

* What do (and don't) you talk about at a dinner party?

* ...?


Protocols IRL
-------------

.. image:: img/icup.png
    :align: center
    :width: 58%

.. class:: image-credit

http://blog.xkcd.com/2009/09/02/urinal-protocol-vulnerability/


Protocols In Computers
----------------------

Digital life has lots of rules too:

.. class:: incremental

* how to say hello

* how to identify yourself

* how to ask for information

* how to provide answers

* how to say goodbye


Real Protocol Examples
----------------------

.. class:: big-centered

What does this look like in practice?


Real Protocol Examples
----------------------

.. class:: incremental

* SMTP (Simple Message Transfer Protocol)
  http://tools.ietf.org/html/rfc5321#appendix-D

* POP3 (Post Office Protocol)
  http://www.faqs.org/docs/artu/ch05s03.html

* IMAP (Internet Message Access Protocol)
  http://www.faqs.org/docs/artu/ch05s03.html

* HTTP (Hyper-Text Transfer Protocol)
  http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol


What does SMTP look like?
-------------------------

SMTP (Say hello and identify yourself)::

    S: 220 foo.com Simple Mail Transfer Service Ready
    C: EHLO bar.com
    S: 250-foo.com greets bar.com
    S: 250-8BITMIME
    S: 250-SIZE
    S: 250-DSN
    S: 250 HELP


What does SMTP look like?
-------------------------

SMTP (Ask for information, provide answers)::

    C: MAIL FROM:<Smith@bar.com>
    S: 250 OK
    C: RCPT TO:<Jones@foo.com>
    S: 250 OK
    C: RCPT TO:<Green@foo.com>
    S: 550 No such user here
    C: DATA
    S: 354 Start mail input; end with <CRLF>.<CRLF>
    C: Blah blah blah...
    C: ...etc. etc. etc.
    C: .
    S: 250 OK

What does SMTP look like?
-------------------------

SMTP (Say goodbye)::

    C: QUIT
    S: 221 foo.com Service closing transmission channel


SMTP Characteristics
--------------------

.. class:: incremental

* Interaction consists of commands and replies
* Each command or reply is *one line* terminated by <CRLF>
* The exception is message payload, terminated by <CRLF>.<CRLF>
* Each command has a *verb* and one or more *arguments*
* Each reply has a formal *code* and an informal *explanation*


What does POP3 look like?
-------------------------

POP3 (Say hello and identify yourself)::

    C: <client connects to service port 110> 
    S: +OK POP3 server ready <1896.6971@mailgate.dobbs.org>
    C: USER bob
    S: +OK bob
    C: PASS redqueen
    S: +OK bob's maildrop has 2 messages (320 octets)


What does POP3 look like?
-------------------------

POP3 (Ask for information, provide answers)::

    C: STAT
    S: +OK 2 320
    C: LIST
    S: +OK 1 messages (120 octets)
    S: 1 120
    S: .


What does POP3 look like?
-------------------------

POP3 (Ask for information, provide answers)::

    C: RETR 1
    S: +OK 120 octets
    S: <server sends the text of message 1>
    S: .
    C: DELE 1
    S: +OK message 1 deleted


What does POP3 look like?
-------------------------

POP3 (Say goodbye)::

    C: QUIT
    S: +OK dewey POP3 server signing off (maildrop empty)
    C: <client hangs up>


POP3 Characteristics
--------------------

.. class:: incremental

* Interaction consists of commands and replies
* Each command or reply is *one line* terminated by <CRLF>
* The exception is message payload, terminated by <CRLF>.<CRLF>
* Each command has a *verb* and one or more *arguments*
* Each reply has a formal *code* and an informal *explanation*

.. class:: incremental

The codes don't really look the same, though, do they?


One Other Difference
--------------------

The exception to the one-line-per-message rule is *payload*

.. class:: incremental

In both SMTP and POP3 this is terminated by <CRLF>.<CRLF>

.. class:: incremental

In SMTP, the *client* has this ability

.. class:: incremental

But in POP3, it belongs to the *server*.  Why?


What does IMAP look like?
-------------------------

IMAP (Say hello and identify yourself)::

    C: <client connects to service port 143>
    S: * OK example.com IMAP4rev1 v12.264 server ready
    C: A0001 USER "frobozz" "xyzzy"
    S: * OK User frobozz authenticated


What does IMAP look like?
-------------------------

IMAP (Ask for information, provide answers [connect to an inbox])::

    C: A0002 SELECT INBOX
    S: * 1 EXISTS
    S: * 1 RECENT
    S: * FLAGS (\Answered \Flagged \Deleted \Draft \Seen)
    S: * OK [UNSEEN 1] first unseen message in /var/spool/mail/esr
    S: A0002 OK [READ-WRITE] SELECT completed


What does IMAP look like?
-------------------------

IMAP (Ask for information, provide answers [Get message sizes])::

    C: A0003 FETCH 1 RFC822.SIZE
    S: * 1 FETCH (RFC822.SIZE 2545)
    S: A0003 OK FETCH completed


What does IMAP look like?
-------------------------

IMAP (Ask for information, provide answers [Get first message header])::

    C: A0004 FETCH 1 BODY[HEADER]
    S: * 1 FETCH (RFC822.HEADER {1425}
    <server sends 1425 octets of message payload>
    S: )
    S: A0004 OK FETCH completed


What does IMAP look like?
-------------------------

IMAP (Ask for information, provide answers [Get first message body])::

    C: A0005 FETCH 1 BODY[TEXT]
    S: * 1 FETCH (BODY[TEXT] {1120}
    <server sends 1120 octets of message payload>
    S: )
    S: * 1 FETCH (FLAGS (\Recent \Seen))
    S: A0005 OK FETCH completed

What does IMAP look like?
-------------------------

IMAP (Say goodbye)::

    C: A0006 LOGOUT
    S: * BYE example.com IMAP4rev1 server terminating connection
    S: A0006 OK LOGOUT completed
    C: <client hangs up>


IMAP Characteristics
--------------------

.. class:: incremental

* Interaction consists of commands and replies
* Each command or reply is *one line* terminated by <CRLF>
* Each command has a *verb* and one or more *arguments*
* Each reply has a formal *code* and an informal *explanation*

.. class:: incremental


IMAP Differences
----------------

.. class:: incremental

* Commands and replies are prefixed by 'sequence identifier'
* Payloads are prefixed by message size, rather than terminated by reserved
  sequence

.. class:: incremental

Compared with POP3, what do these differences suggest?


Protocols in Python
-------------------

.. class:: big-centered

Let's try this out for ourselves!


Protocols in Python
-------------------

.. class:: big-centered

Fire up your python interpreters and prepare to type.


IMAP in Python
--------------

Begin by importing the ``imaplib`` module from the Python Standard Library::

    >>> import imaplib
    >>> dir(imaplib)
    ['AllowedVersions', 'CRLF', 'Commands', 
     'Continuation', 'Debug', 'Flags', 'IMAP4', 
     'IMAP4_PORT', 'IMAP4_SSL', 'IMAP4_SSL_PORT', 
     'IMAP4_stream', 'Int2AP', 'InternalDate', 
     'Internaldate2tuple', 'Literal', 'MapCRLF', 
     ...
     'socket', 'ssl', 'sys', 'time']


IMAP in Python
--------------

I've prepared a server for us to use, we'll need to set up a client to speak
to it. Our server requires SSL for connecting to IMAP servers, so let's
initialize an IMAP4_SSL client and authenticate::

    >>> conn = imaplib.IMAP4_SSL('mail.webfaction.com')
      57:04.83 imaplib version 2.58
      57:04.83 new IMAP4 connection, tag=FNHG
    >>> conn.login(username, password)
    ('OK', ['Logged in.'])


IMAP in Python
--------------

Let's set up debugging so that we can see the communication back and forth
between client and server::

    >>> conn.debug = 4 # >3 prints all messages

We can start by listing the mailboxes we have on the server::

    >>> conn.list()
      00:41.91 > FNHG3 LIST "" *
      00:41.99 < * LIST (\HasNoChildren) "." "INBOX"
      00:41.99 < FNHG3 OK List completed.
    ('OK', ['(\\HasNoChildren) "." "INBOX"'])


IMAP in Python
--------------

To interact with our email, we must select a mailbox from the list we received
earlier::

    >>> conn.select('INBOX')
      00:00.47 > FNHG2 SELECT INBOX
      00:00.56 < * FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
      00:00.56 < * OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
      00:00.56 < * 2 EXISTS
      00:00.57 < * 0 RECENT
      00:00.57 < * OK [UNSEEN 2] First unseen.
      00:00.57 < * OK [UIDVALIDITY 1357449499] UIDs valid
      00:00.57 < * OK [UIDNEXT 3] Predicted next UID
      00:00.57 < FNHG2 OK [READ-WRITE] Select completed.
    ('OK', ['2'])


IMAP in Python
--------------

We can search our selected mailbox for messages matching one or more criteria.
The return value is a string list of the UIDs of messages that match our
search::

    >>> conn.search(None, '(FROM "IPIP")')
      18:25.41 > FNHG5 SEARCH (FROM "IPIP")
      18:25.54 < * SEARCH 1 2
      18:25.54 < FNHG5 OK Search completed.
    ('OK', ['1 2'])
    >>>


IMAP in Python
--------------

Once we've found a message we want to look at, we can use the ``fetch``
command to read it from the server. IMAP allows fetching each part of
a message independently::

    >>> conn.fetch('2', '(BODY[HEADER])')
    ...
    >>> conn.fetch('2', '(BODY[TEXT])')
    ...
    >>> conn.fetch('2', '(FLAGS)')


Python Means Batteries Included
-------------------------------

So we can download an entire message and then make a Python email message
object

.. class:: small

::

    >>> import email
    >>> typ, data = conn.fetch('2', '(RFC822)')
      28:08.40 > FNHG8 FETCH 2 (RFC822)
      ...

Parse the returned data to get to the actual message

.. class:: small

::

    >>> for part in data:
    ...   if isinstance(part, tuple):
    ...     msg = email.message_from_string(part[1])
    ... 
    >>> 


IMAP in Python
--------------

Once we have that, we can play with the resulting email object::

    >>> msg['to']
    'demo@crisewing.com'
    >>> print msg.get_payload()
    This is an email message


.. class:: incremental center

**Neat, huh?**


What Have We Learned?
---------------------

.. class:: incremental

* Protocols are just a set of rules for how to communicate

* Protocols tell us how to delimit messages

* Protocols tell us what messages are valid

* If we properly format request messages to a server, we can get answer
  messages

* Python supports a number of these protocols

* So we don't have to remember how to format the commands ourselves

.. class:: incremental

But in every case we've seen, we could do the same thing with a socket and
some strings


HTTP
----

.. class:: big-centered

HTTP is no different


HTTP
----

HTTP is also message-centered, with two-way communications:

.. class:: incremental

* Requests (Asking for information)
* Responses (Providing answers)

What does HTTP look like?
-------------------------

HTTP (Ask for information)::

    GET /index.html HTTP/1.1
    Host: www.example.com
    <CRLF>

What does HTTP look like?
-------------------------

HTTP (Provide answers)::

    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: "3f80f-1b6-3e1cb03b"
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8
    <CRLF>
    <438 bytes of content>


HTTP Req/Resp Format
--------------------

Both share a common basic format:

.. class:: incremental

* Line separators are <CRLF> (familiar, no?)
* An required initial line (a command or a response code)
* A (mostly) optional set of headers, one per line
* A blank line
* An optional body



HTTP Requests
-------------

In HTTP 1.0, the only required line in an HTTP request is this::

    GET /path/to/index.html HTTP/1.0
    <CRLF>

.. class:: incremental

As virtual hosting grew more common, that was not enough, so HTTP 1.1 adds a
single required *header*, **Host**:

.. class:: incremental

::

    GET /path/to/index.html HTTP/1.1
    Host: www.mysite1.com:80
    <CRLF>


HTTP Verbs
----------

**GET** ``/path/to/index.html HTTP/1.1``

.. class:: incremental

* Every HTTP request must start with a *verb*
* There are four main HTTP verbs:

    .. class:: incremental

    * GET
    * POST
    * PUT
    * DELETE

.. class:: incremental

* There are others, notably HEAD, but you won't see them too much


HTTP Verbs
----------

These four verbs are mapped to the four basic steps (*CRUD*) of persistent
storage:

.. class:: incremental

* POST = Create
* GET = Read
* PUT = Update
* DELETE = Delete


Verbs: Safe <--> Unsafe
-----------------------

HTTP verbs can be categorized as **safe** or **unsafe**, based on whether they
might change something on the server:

.. class:: incremental

* Safe HTTP Verbs
    * GET
* Unsafe HTTP Verbs
    * POST
    * PUT
    * DELETE

.. class:: incremental

This is a *normative* distinction, which is to say **be careful**


Verbs: Idempoent <--> ???
-------------------------

HTTP verbs can be categorized as **idempotent**, based on whether a given
request will always have the same result:

.. class:: incremental

* Idempotent HTTP Verbs
    * GET
    * PUT
    * DELETE
* Non-Idempotent HTTP Verbs
    * POST

.. class:: incremental

Again, *normative*. The developer is responsible for ensuring that it is true.


HTTP Requests: URI
------------------

``GET`` **/path/to/index.html** ``HTTP/1.1``

.. class:: incremental

* Every HTTP request must include a **URI** used to determine the **resource** to
  be returned

* URI??
  http://stackoverflow.com/questions/176264/whats-the-difference-between-a-uri-and-a-url/1984225#1984225

* Resource?  Files (html, img, .js, .css), but also:

    .. class:: incremental

    * Dynamic scripts
    * Raw data
    * API endpoints


HTTP Responses
--------------

In both HTTP 1.0 and 1.1, a proper response consists of an intial line,
followed by optional headers, a single blank line, and then optionally a
response body::

    HTTP/1.1 200 OK
    Content-Type: text/plain
    <CRLF>
    this is a pretty minimal response


HTTP Response Codes
-------------------

``HTTP/1.1`` **200 OK**

All HTTP responses must include a **response code** indicating the outcome of
the request.

.. class:: incremental

* 1xx (HTTP 1.1 only) - Informational message
* 2xx - Success of some kind
* 3xx - Redirection of some kind
* 4xx - Client Error of some kind
* 5xx - Server Error of some kind

.. class:: incremental

The text bit makes the code more human-readable


Common Response Codes
---------------------

There are certain HTTP response codes you are likely to see (and use) most
often:

.. class:: incremental

* ``200 OK`` - Everything is good
* ``301 Moved Permanently`` - You should update your link
* ``304 Not Modified`` - You should load this from cache
* ``404 Not Found`` - You've asked for something that doesn't exist
* ``500 Internal Server Error`` - Something bad happened

.. class:: incremental

Do not be afraid to use other, less common codes in building good RESTful
apps. There are a lot of them for a reason. See
http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html


HTTP Headers
------------

Both requests and responses can contain **headers** of the form ``Name: Value``

.. class:: incremental

* HTTP 1.0 has 16, 1.1 has 46
* Any number of spaces or tabs may separate the *name* from the *value*
* If a header line starts with spaces or tabs, it is considered part of the
  value for the previous header
* Header *names* are **not** case-sensitive, but *values* may be

.. class:: incremental

read more about HTTP headers: http://www.cs.tut.fi/~jkorpela/http.html


Content-Type Header
-------------------

A very common header used in HTTP responses is ``Content-Type``. It tells the
client what to expect.

.. class:: incremental

* uses **mime-type** (Multi-purpose Internet Mail Extensions)
* foo.jpeg - ``Content-Type: image/jpeg``
* foo.png - ``Content-Type: image/png``
* bar.txt - ``Content-Type: text/plain``
* baz.html - ``Content-Type: text/html``

.. class:: incremental

There are *many* mime-type identifiers:
http://www.webmaster-toolkit.com/mime-types.shtml


HTTP Debugging
--------------

When working on applications, it's nice to be able to see all this going back
and forth.  There are several apps that can help with this:

* windows: http://www.fiddler2.com/fiddler2/
* firefox: http://getfirebug.com/
* safari: built in 
* chrome: built in
* IE (7.0+): built in

.. class:: incremental

These tools can show you both request and response, headers and all. Very
useful.