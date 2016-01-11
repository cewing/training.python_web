.. |br| raw:: html

    <br />

**********
Session 02
**********

.. figure:: /_static/protocol.png
    :align: center
    :width: 40%

    Web Protocols

The Languages Computers Speak
=============================

.. rst-class:: build left
.. container::

    Programming languages like Python are the languages we speak to computers.

    *Protocols* are the languages that computers speak to each-other.

    This sesson we'll look at a few of them and

    .. rst-class:: build

    * Learn what makes them similar
    * Learn what makes them different
    * Learn about Python's tools for speaking them
    * Learn how to speak one (HTTP) ourselves


But First
----------

.. rst-class:: large centered

Questions from the Homework?


.. nextslide::

.. rst-class:: large centered

Examples of an echo server using ``select``


What is a Protocol?
-------------------

.. rst-class:: build large centered
.. container::

    **a set of rules or conventions**

    **governing communications**


.. nextslide:: Protocols IRL

Life has lots of sets of rules for how to do things.

.. rst-class:: build

* What do you say when you get on the elevator?

* What do you do on a first date?

* What do you wear to a job interview?

* What do (and don't) you talk about at a dinner party?

* ...?


.. nextslide:: Protocols IRL

.. figure:: /_static/icup.png
    :align: center
    :width: 65%

    http://blog.xkcd.com/2009/09/02/urinal-protocol-vulnerability/


.. nextslide:: Protocols In Computers

Digital life has lots of rules too:

.. rst-class:: build

* how to say hello

* how to identify yourself

* how to ask for information

* how to provide answers

* how to say goodbye


Real Protocol Examples
----------------------

What does this look like in practice?

.. rst-class:: build

* SMTP (Simple Message Transfer Protocol) |br|
  http://tools.ietf.org/html/rfc5321#appendix-D

* POP3 (Post Office Protocol) |br|
  http://www.faqs.org/docs/artu/ch05s03.html

* IMAP (Internet Message Access Protocol) |br|
  http://www.faqs.org/docs/artu/ch05s03.html

* HTTP (Hyper-Text Transfer Protocol) |br|
  http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol


.. nextslide:: A Word on Typography

Over the next few slides we'll be looking at server/client interactions.

.. rst-class:: build
.. container::

    Each interaction is line-based, each line represents one message.

    Messages from the Server to the Client are prefaced with ``S (<--)``

    Messages from the Client to the Server are prefaced with ``C (-->)``

    **All** lines end with the character sequence ``<CRLF>`` (``\r\n``)


SMTP
----

What does SMTP look like?

.. rst-class:: build
.. container::

    SMTP (Say hello and identify yourself)::

        S (<--): 220 foo.com Simple Mail Transfer Service Ready
        C (-->): EHLO bar.com
        S (<--): 250-foo.com greets bar.com
        S (<--): 250-8BITMIME
        S (<--): 250-SIZE
        S (<--): 250-DSN
        S (<--): 250 HELP


.. nextslide::

.. ifslides::

    What does SMTP look like?

SMTP (Ask for information, provide answers)::

    C (-->): MAIL FROM:<Smith@bar.com>
    S (<--): 250 OK
    C (-->): RCPT TO:<Jones@foo.com>
    S (<--): 250 OK
    C (-->): RCPT TO:<Green@foo.com>
    S (<--): 550 No such user here
    C (-->): DATA
    S (<--): 354 Start mail input; end with <CRLF>.<CRLF>
    C (-->): Blah blah blah...
    C (-->): ...etc. etc. etc.
    C (-->): .
    S (<--): 250 OK

.. nextslide::

.. ifslides::

    What does SMTP look like?

SMTP (Say goodbye)::

    C (-->): QUIT
    S (<--): 221 foo.com Service closing transmission channel


.. nextslide:: SMTP Characteristics

.. rst-class:: build

* Interaction consists of commands and replies
* Each command or reply is *one line* terminated by <CRLF> |br|
  (there are exceptions, see the ``250`` reply to ``EHLO`` above)
* The exception is message payload, terminated by <CRLF>.<CRLF>
* Each command has a *verb* and one or more *arguments*
* Each reply has a formal *code* and an informal *explanation*


POP3
----

What does POP3 look like?

.. rst-class:: build
.. container::

    POP3 (Say hello and identify yourself)::

        C (-->): <client connects to service port 110>
        S (<--): +OK POP3 server ready <1896.6971@mailgate.dobbs.org>
        C (-->): USER bob
        S (<--): +OK bob
        C (-->): PASS redqueen
        S (<--): +OK bob's maildrop has 2 messages (320 octets)


.. nextslide::

.. ifslides::

    What does POP3 look like?

POP3 (Ask for information, provide answers)::

    C (-->): STAT
    S (<--): +OK 2 320
    C (-->): LIST
    S (<--): +OK 1 messages (120 octets)
    S (<--): 1 120
    S (<--): .


.. nextslide::

.. ifslides::

    What does POP3 look like?

POP3 (Ask for information, provide answers)::

    C (-->): RETR 1
    S (<--): +OK 120 octets
    S (<--): <server sends the text of message 1>
    S (<--): .
    C (-->): DELE 1
    S (<--): +OK message 1 deleted


.. nextslide::

.. ifslides::

    What does POP3 look like?

POP3 (Say goodbye)::

    C (-->): QUIT
    S (<--): +OK dewey POP3 server signing off (maildrop empty)
    C (-->): <client hangs up>


.. nextslide:: POP3 Characteristics

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Interaction consists of commands and replies
    * Each command or reply is *one line* terminated by <CRLF>
    * The exception is message payload, terminated by <CRLF>.<CRLF>
    * Each command has a *verb* and one or more *arguments*
    * Each reply has a formal *code* and an informal *explanation*

    The codes don't really look the same, though, do they?


.. nextslide:: One Other Difference

The exception to the one-line-per-message rule is *payload*

.. rst-class:: build
.. container::

    In both SMTP and POP3 this is terminated by <CRLF>.<CRLF>

    In SMTP, the *client* has this ability

    But in POP3, it belongs to the *server*.

    .. rst-class:: large centered

        Why?

IMAP
----

What does IMAP look like?

.. rst-class:: build
.. container::

    IMAP (Say hello and identify yourself)::

        C (-->): <client connects to service port 143>
        S (<--): * OK example.com IMAP4rev1 v12.264 server ready
        C (-->): A0001 USER "frobozz" "xyzzy"
        S (<--): * OK User frobozz authenticated


.. nextslide::

.. ifslides::

    What does IMAP look like?

IMAP (Ask for information, provide answers [connect to an inbox])::

    C (-->): A0002 SELECT INBOX
    S (<--): * 1 EXISTS
    S (<--): * 1 RECENT
    S (<--): * FLAGS (\Answered \Flagged \Deleted \Draft \Seen)
    S (<--): * OK [UNSEEN 1] first unseen message in /var/spool/mail/esr
    S (<--): A0002 OK [READ-WRITE] SELECT completed


.. nextslide::

.. ifslides::

    What does IMAP look like?

IMAP (Ask for information, provide answers [Get message sizes])::

    C (-->): A0003 FETCH 1 RFC822.SIZE
    S (<--): * 1 FETCH (RFC822.SIZE 2545)
    S (<--): A0003 OK FETCH completed


.. nextslide::

.. ifslides::

    What does IMAP look like?

IMAP (Ask for information, provide answers [Get first message header])::

    C (-->): A0004 FETCH 1 BODY[HEADER]
    S (<--): * 1 FETCH (RFC822.HEADER {1425}
    <server sends 1425 octets of message payload>
    S (<--): )
    S (<--): A0004 OK FETCH completed


.. nextslide::

.. ifslides::

    What does IMAP look like?

IMAP (Ask for information, provide answers [Get first message body])::

    C (-->): A0005 FETCH 1 BODY[TEXT]
    S (<--): * 1 FETCH (BODY[TEXT] {1120}
    <server sends 1120 octets of message payload>
    S (<--): )
    S (<--): * 1 FETCH (FLAGS (\Recent \Seen))
    S (<--): A0005 OK FETCH completed

.. nextslide::

.. ifslides::

    What does IMAP look like?

IMAP (Say goodbye)::

    C (-->): A0006 LOGOUT
    S (<--): * BYE example.com IMAP4rev1 server terminating connection
    S (<--): A0006 OK LOGOUT completed
    C (-->): <client hangs up>


.. nextslide:: IMAP Characteristics

.. rst-class:: build

* Interaction consists of commands and replies
* Each command or reply is *one line* terminated by <CRLF>
* Each command has a *verb* and one or more *arguments*
* Each reply has a formal *code* and an informal *explanation*


.. nextslide:: IMAP Differences

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Commands and replies are prefixed by 'sequence identifier'
    * Payloads are prefixed by message size, rather than terminated by reserved
      sequence

    Compared with POP3, what do these differences suggest?


Using IMAP in Python
--------------------

Let's try this out for ourselves!

.. rst-class:: build
.. container::

    .. container::

        Fire up your python interpreters and prepare to type.


.. nextslide::

Begin by importing the ``imaplib`` module from the Python Standard Library:

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [1]: import imaplib
        In [2]: dir(imaplib)
        Out[2]:
        ['AllowedVersions',
         'CRLF',
         'Commands',
        ...
         'timedelta',
         'timezone']
        In [3]: imaplib.Debug = 4

    Setting ``imap.Debug`` shows us what is sent and received


.. nextslide::

I've prepared a server for us to use, but we'll need to set up a client to
speak to it.

.. rst-class:: build
.. container::

    Our server requires SSL (Secure Socket Layer) for connecting to IMAP
    servers, so let's initialize an IMAP4_SSL client and authenticate:

    .. code-block:: ipython

        In [4]: conn = imaplib.IMAP4_SSL('mail.webfaction.com')
          22:40.32 imaplib version 2.58
          22:40.32 new IMAP4 connection, tag=b'IMKC'
          22:40.38 < b'* OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN] Dovecot ready.'
          22:40.38 > b'IMKC0 CAPABILITY'
          22:40.45 < b'* CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN'
          22:40.45 < b'IMKC0 OK Capability completed.'
          22:40.45 CAPABILITIES: ('IMAP4REV1', 'LITERAL+', 'SASL-IR', 'LOGIN-REFERRALS', 'ID', 'ENABLE', 'IDLE', 'AUTH=PLAIN')
        In [5]: conn.login('crisewing_demobox', 's00p3rs3cr3t')
          22:59.92 > b'IMKC1 LOGIN crisewing_demobox "s00p3rs3cr3t"'
          23:01.79 < b'* CAPABILITY IMAP4rev1 SASL-IR SORT THREAD=REFERENCES MULTIAPPEND UNSELECT LITERAL+ IDLE CHILDREN NAMESPACE LOGIN-REFERRALS STARTTLS AUTH=PLAIN'
          23:01.79 < b'IMKC1 OK Logged in.'
        Out[5]: ('OK', [b'Logged in.'])

.. nextslide::

We can start by listing the mailboxes we have on the server:

.. code-block:: ipython

    In [6]: conn.list()
      26:30.64 > b'IMKC2 LIST "" *'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "Trash"'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "Drafts"'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "Sent"'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "Junk"'
      26:30.72 < b'* LIST (\\HasNoChildren) "." "INBOX"'
      26:30.72 < b'IMKC2 OK List completed.'
    Out[6]:
    ('OK',
     [b'(\\HasNoChildren) "." "Trash"',
      b'(\\HasNoChildren) "." "Drafts"',
      b'(\\HasNoChildren) "." "Sent"',
      b'(\\HasNoChildren) "." "Junk"',
      b'(\\HasNoChildren) "." "INBOX"'])


.. nextslide::

To interact with our email, we must select a mailbox from the list we received
earlier:

.. code-block:: ipython

    In [7]: conn.select('INBOX')
      27:20.96 > b'IMKC3 SELECT INBOX'
      27:21.04 < b'* FLAGS (\\Answered \\Flagged \\Deleted \\Seen \\Draft)'
      27:21.04 < b'* OK [PERMANENTFLAGS (\\Answered \\Flagged \\Deleted \\Seen \\Draft \\*)] Flags permitted.'
      27:21.04 < b'* 1 EXISTS'
      27:21.04 < b'* 0 RECENT'
      27:21.04 < b'* OK [UNSEEN 1] First unseen.'
      27:21.04 < b'* OK [UIDVALIDITY 1357449499] UIDs valid'
      27:21.04 < b'* OK [UIDNEXT 24] Predicted next UID'
      27:21.04 < b'IMKC3 OK [READ-WRITE] Select completed.'
    Out[7]: ('OK', [b'1'])


.. nextslide::

We can search our selected mailbox for messages matching one or more criteria.

.. rst-class:: build
.. container::

    The return value is a list of bytestrings containing the UIDs of messages
    that match our search:

    .. code-block:: ipython

        In [8]: conn.search(None, '(FROM "cris")')
          28:43.02 > b'IMKC4 SEARCH (FROM "cris")'
          28:43.09 < b'* SEARCH 1'
          28:43.09 < b'IMKC4 OK Search completed.'
        Out[8]: ('OK', [b'1'])

.. nextslide::

Once we've found a message we want to look at, we can use the ``fetch``
command to read it from the server.

.. rst-class:: build
.. container::

    IMAP allows fetching each part of a message independently:

    .. code-block:: ipython

        In [9]: conn.fetch('1', 'BODY[HEADER]')
          ...
        Out[9]: ('OK', ...)

        In [10]: conn.fetch('1', 'FLAGS')
          ...
        Out[10]: ('OK', [b'1 (FLAGS (\\Seen))'])

        In [11]: conn.fetch('1', 'BODY[TEXT]')
          ...
        Out[11]: ('OK', ...)

    What does the message say?

.. nextslide:: Batteries Included

Python even includes an *email* library that would allow us to interact with
this message in an *OO* style.

.. rst-class:: build

.. container::

    *Neat, Huh?*

What Have We Learned?
---------------------

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Protocols are just a set of rules for how to communicate

    * Protocols tell us how to parse and delimit messages

    * Protocols tell us what messages are valid

    * If we properly format request messages to a server, we can get response
      messages

    * Python supports a number of these protocols

    * So we don't have to remember how to format the commands ourselves

    But in every case we've seen, we could do the same thing with a socket and
    some strings


Break Time
----------

Let's take a few minutes here to clear our heads.

.. rst-class:: build
.. container::

    When we return, we'll learn about the king of protocols,

    .. rst-class:: large centered

    HTTP


HTTP
====

.. rst-class:: left
.. container::

    HTTP is no different

    .. rst-class:: build
    .. container::

        HTTP is also message-centered, with two-way communications:

        .. rst-class:: build

        * Requests (Asking for information)
        * Responses (Providing answers)


What does HTTP look like?
-------------------------

HTTP (Ask for information):

.. code-block:: http

    GET /index.html HTTP/1.1<CRLF>
    Host: www.example.com<CRLF>
    <CRLF>

.. ifnotslides::

    .. note:: the ``<CRLF>`` you see here is a visualization of the ``\r\n``
              character sequence.

.. ifslides::

    **note**: the ``<CRLF>`` you see here is a visualization of the ``\r\n``
    character sequence.


.. nextslide::

HTTP (Provide answers):

.. code-block:: http

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
    <!DOCTYPE html>\n<html>\n  <head>\n    <title>This is a .... </html>

Pay particular attention to the ``<CRLF>`` on a line by itself.


.. nextslide:: HTTP Core Format

In HTTP, both *request* and *response* share a common basic format:

.. rst-class:: build

* Line separators are <CRLF> (familiar, no?)
* A required initial line (a command or a response code)
* A (mostly) optional set of headers, one per line
* A blank line
* An optional body


Implementing HTTP
-----------------

Let's investigate the HTTP protocol a bit in real life.

.. rst-class:: build
.. container::

    We'll do so by building a simplified HTTP server, one step at a time.

    There is a copy of the echo server from last time in
    ``resources/session02``. It's called ``http_server.py``.

    In a terminal, move into that directory. We'll be doing our work here for
    the rest of the session


.. nextslide:: TDD IRL (a quick aside)

Test Driven Development (TDD) is all the rage these days.

.. rst-class:: build
.. container::

    It means that before you write code, you first write tests demonstrating
    what you want your code to do.

    When all your tests pass, you are finished. You did this for your last
    assignment.

    We'll be doing it again today.


.. nextslide:: Run the Tests

From inside ``resources/session02`` start a second python interpreter and run
``$ python http_server.py``

.. rst-class:: build
.. container::

    In your first interpreter run the tests. You should see similar output:

    .. code-block:: bash

        $ python tests.py
        [...]
        Ran 10 tests in 0.054s

        FAILED (failures=3, errors=7)

    Let's take a few minutes here to look at these tests and understand them.


.. nextslide:: Viewing an HTTP Request

Our job is to make all those tests pass.

.. rst-class:: build
.. container::

    First, though, let's pretend this server really is a functional HTTP
    server.

    This time, instead of using the echo client to make a connection to the
    server, let's use a web browser!

    Point your favorite browser at ``http://localhost:10000``


.. nextslide:: A Bad Interaction

First, look at the printed output from your echo server.

.. rst-class:: build
.. container::

    Second, note that your browser is still waiting to finish loading the page

    Moreover, your server should also be hung, waiting for more from the
    'client'

    This is because the server is waiting for the browser to respond

    And at the same time, the browser is waiting for the server to indicate it
    is done.

    Our server does not yet speak the HTTP protocol, but the browser is
    expecting it.

.. nextslide:: Echoing A Request

Kill your server with ``ctrl-c`` (the keyboard interrupt) and you should see
some printed content in your browser:

.. rst-class:: build
.. container::

    .. code-block:: http

        GET / HTTP/1.1
        Host: localhost:10000
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:22.0) Gecko/20100101 Firefox/22.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate
        DNT: 1
        Cookie: __utma=111872281.383966302.1364503233.1364503233.1364503233.1; __utmz=111872281.1364503233.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); csrftoken=uiqj579iGRbReBHmJQNTH8PFfAz2qRJS
        Connection: keep-alive
        Cache-Control: max-age=0

    Your server is simply echoing what it receives, so this is an *HTTP
    Request* as sent by your browser.

.. nextslide:: HTTP Debugging


When working on HTTP applications, it's nice to be able to see all this going back
and forth.

.. rst-class:: build
.. container::

    Good browsers support this with a set of developer tools built-in.

    .. rst-class:: build

    * firefox -> ctrl-shift-K or cmd-opt-K (os X)
    * safari -> enable in preferences:advanced then cmd-opt-i
    * chrome -> ctrl-shift-i or cmd-opt-i (os X)
    * IE (7.0+) -> F12 or tools menu -> developer tools

    The 'Net(work)' pane of these tools can show you both request and response,
    headers and all. Very useful.


.. nextslide:: Stop! Demo Time

.. rst-class:: centered

**Let's take a quick look**


.. nextslide:: Other Debugging Options

Sometimes you need or want to debug http requests that are not going through
your browser.

.. rst-class:: build
.. container::

    Or perhaps you need functionality that is not supported by in-browser tools
    (request munging, header mangling, decryption of https request/responses)

    Then it might be time for an HTTP debugging proxy:

    .. rst-class:: build

    * windows: http://www.fiddler2.com/fiddler2/
    * win/osx/linux: http://www.charlesproxy.com/

    We won't cover any of these tools here today.  But you can check them out
    when you have the time.


Step 1: Basic HTTP Protocol
---------------------------

In HTTP 1.0, the only required line in an HTTP request is this:

.. code-block:: http

    GET /path/to/index.html HTTP/1.0<CRLF>
    <CRLF>

.. rst-class:: build
.. container::

    As virtual hosting grew more common, that was not enough, so HTTP 1.1 adds
    a single required *header*, **Host**:

    .. code-block:: http

        GET /path/to/index.html HTTP/1.1<CRLF>
        Host: www.mysite1.com:80<CRLF>
        <CRLF>


.. nextslide:: HTTP Responses

In both HTTP 1.0 and 1.1, a proper response consists of an intial line,
followed by optional headers, a single blank line, and then optionally a
response body:

.. rst-class:: build
.. container::

    .. code-block:: http

        HTTP/1.1 200 OK<CRLF>
        Content-Type: text/plain<CRLF>
        <CRLF>
        this is a pretty minimal response

    Let's update our server to return such a response.

.. nextslide:: Returning a Canned HTTP Response

Begin by implementing a new function in your ``http_server.py`` script called
`response_ok`.

.. rst-class:: build
.. container::

    It can be super-simple for now.  We'll improve it later.

    .. container::

        It needs to return our minimal response from above:

        .. code-block:: http

            HTTP/1.1 200 OK<CRLF>
            Content-Type: text/plain<CRLF>
            <CRLF>
            this is a pretty minimal response

    **Remember, <CRLF> is a placeholder for the** ``\r\n`` **character sequence**


.. nextslide:: My Solution

.. code-block:: python

    def response_ok():
        """returns a basic HTTP response"""
        resp = []
        resp.append(b"HTTP/1.1 200 OK")
        resp.append(b"Content-Type: text/plain")
        resp.append(b"")
        resp.append(b"this is a pretty minimal response")
        return b"\r\n".join(resp)

Did you remember that sockets only accept bytes?


.. nextslide:: Run The Tests

We've now implemented a function that is tested by our tests. Let's run them
again:

.. rst-class:: build
.. container::

    .. code-block:: bash

        $ python tests.py
        [...]
        ----------------------------------------------------------------------
        Ran 10 tests in 0.002s

        FAILED (failures=3, errors=3)

    Great!  We've now got 4 tests that pass.  Good work.

.. nextslide:: Server Modifications

Next, we need to rebuild the server loop from our echo server for it's new
purpose:

.. rst-class:: build
.. container::

    It should now wait for an incoming request to be *finished*, *then* send a
    response back to the client.

    The response it sends can be the result of calling our new ``response_ok``
    function for now.

    We could also bump up the ``recv`` buffer size to something more reasonable
    for HTTP traffic, say 1024.

.. nextslide:: My Solution

.. code-block:: python

    # ...
    try:
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()  # blocking
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                while True:
                    data = conn.recv(1024)
                    if len(data) < 1024:
                        break
                print('sending response', file=log_buffer)
                response = response_ok()
                conn.sendall(response)
            finally:
                conn.close()
    # ...


.. nextslide:: Run The Tests

Once you've got that set, restart your server::

    $ python http_server.py

.. rst-class:: build
.. container::

    Then you can re-run your tests:

    .. code-block:: bash

        $ python tests.py
        [...]
        ----------------------------------------------------------------------
        Ran 10 tests in 0.003s

        FAILED (failures=2, errors=3)

    Five tests now pass!

Step 2: Handling HTTP Methods
-----------------------------

Every HTTP request **must** begin with a single line, broken by whitespace into
three parts:

.. code-block:: http

    GET /path/to/index.html HTTP/1.1

.. rst-class:: build
.. container::

    The three parts are the *method*, the *URI*, and the *protocol*

    Let's look at each in turn.


.. nextslide:: HTTP Methods

**GET** ``/path/to/index.html HTTP/1.1``

.. rst-class:: build

* Every HTTP request must start with a *method*
* There are four main HTTP methods:

  .. rst-class:: build

  * GET
  * POST
  * PUT
  * DELETE

* There are others, notably HEAD, but you won't see them too much


.. nextslide:: HTTP Methods

These four methods are mapped to the four basic steps (*CRUD*) of persistent
storage:

.. rst-class:: build

* POST = Create
* GET = Read
* PUT = Update
* DELETE = Delete


.. nextslide:: Methods: Safe <--> Unsafe

HTTP methods can be categorized as **safe** or **unsafe**, based on whether
they might change something on the server:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Safe HTTP Methods

      * GET

    * Unsafe HTTP Methods

      * POST
      * PUT
      * DELETE

    This is a *normative* distinction, which is to say **be careful**


.. nextslide:: Methods: Idempotent <--> ???

HTTP methods can be categorized as **idempotent**.

.. rst-class:: build
.. container::

    This means that a given request will always have the same result:

    .. rst-class:: build

    * Idempotent HTTP Methods

      * GET
      * PUT
      * DELETE

    * Non-Idempotent HTTP Methods

      * POST

    Again, *normative*. The developer is responsible for ensuring that it is true.


.. nextslide:: HTTP Method Handling

Let's keep things simple, our server will only respond to *GET* requests.

.. rst-class:: build
.. container::

    We need to create a function that parses a request and determines if we can
    respond to it: ``parse_request``.

    If the request method is not *GET*, our method should raise an error

    Remember, although a request is more than one line long, all we care about
    here is the first line


.. nextslide:: My Solution

.. code-block:: python

    def parse_request(request):
        first_line = request.split("\r\n", 1)[0]
        method, uri, protocol = first_line.split()
        if method != "GET":
            raise NotImplementedError("We only accept GET")
        print('request is okay', file=sys.stderr)


.. nextslide:: Update the Server

We'll also need to update the server code. It should

.. rst-class:: build

* save the request as it comes in
* check the request using our new function
* send an OK response if things go well


.. nextslide:: My Solution

.. code-block:: python

    # ...
    conn, addr = sock.accept() # blocking
    try:
        print('connection - {0}:{1}'.format(*addr), file=log_buffer)
        request = ""
        while True:
            data = conn.recv(1024)
            request += data.decode('utf8')
            if len(data) < 1024 or not data:
                break

        parse_request(request)
        print('sending response', file=log_buffer)
        response = response_ok()
        conn.sendall(response)
    finally:
        conn.close()
    # ...


.. nextslide:: Run The Tests

Quit and restart your server now that you've updated the code::

    $ python http_server.py

.. rst-class:: build
.. container::

    At this point, we should have seven tests passing:

    .. code-block:: bash

        $ python tests.py
        Ran 10 tests in 0.002s

        FAILED (failures=1, errors=2)


.. nextslide:: What About a Browser?

Quit and restart your server, now that you've updated the code.

.. rst-class:: build
.. container::

    Reload your browser.  It should work fine.

    We can use the ``simple_client.py`` script in our resources to test our
    error condition.  In a second terminal window run the script like so::

        $ python simple_client.py "POST / HTTP/1.0\r\n\r\n"

    You'll have to quit the client pretty quickly with ``ctrl-c``


Step 3: Error Responses
-----------------------

Okay, so the outcome there was pretty ugly. The client went off the rails, and
our server has terminated as well.

.. rst-class:: build
.. container::

    .. rst-class:: centered

        **why?**

    The HTTP protocol allows us to handle errors like this more gracefully.

    .. rst-class:: centered

    **Enter the Response Code**


.. nextslide:: HTTP Response Codes

``HTTP/1.1`` **200 OK**

All HTTP responses must include a **response code** indicating the outcome of
the request.

.. rst-class:: build
.. container::

    .. rst-class:: build

    * 1xx (HTTP 1.1 only) - Informational message
    * 2xx - Success of some kind
    * 3xx - Redirection of some kind
    * 4xx - Client Error of some kind
    * 5xx - Server Error of some kind

    The text bit makes the code more human-readable


.. nextslide:: Common Response Codes

There are certain HTTP response codes you are likely to see (and use) most
often:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * ``200 OK`` - Everything is good
    * ``301 Moved Permanently`` - You should update your link
    * ``304 Not Modified`` - You should load this from cache
    * ``404 Not Found`` - You've asked for something that doesn't exist
    * ``500 Internal Server Error`` - Something bad happened

    Do not be afraid to use other, less common codes in building good apps.
    There are a lot of them for a reason.

    See http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html


.. nextslide:: Handling our Error

Luckily, there's an error code that is tailor-made for this situation.

.. rst-class:: build
.. container::

    The client has made a request using a method we do not support

    ``405 Method Not Allowed``

    Let's add a new function that returns this error code. It should be called
    ``response_method_not_allowed``

    Remember, it must be a complete HTTP Response with the correct *code*


.. nextslide:: My Solution

.. code-block:: python

    def response_method_not_allowed():
        """returns a 405 Method Not Allowed response"""
        resp = []
        resp.append("HTTP/1.1 405 Method Not Allowed")
        resp.append("")
        return "\r\n".join(resp)


.. nextslide:: Server Updates

Again, we'll need to update the server to handle this error condition
correctly.  It should

.. rst-class:: build

* catch the exception raised by the ``parse_request`` function
* create our new error response as a result
* if no exception is raised, then create the OK response
* return the generated response to the user

.. nextslide:: My Solution

.. code-block:: python

    # ...
    while True:
        data = conn.recv(1024)
        request += data.decode('utf8')
        if len(data) < 1024:
            break

    try:
        parse_request(request)
    except NotImplementedError:
        response = response_method_not_allowed()
    else:
        response = response_ok()

    print('sending response', file=log_buffer)
    conn.sendall(response.encode('utf8'))
    # ...


.. nextslide:: Run The Tests

Start your server (or restart it if by some miracle it's still going).

.. rst-class:: build
.. container::

    Then run the tests again::

        $ python tests.py
        [...]
        Ran 10 tests in 0.002s

        OK

    Wahoo! All our tests are passing. That means we are done writing code for
    now.


Step 4: Serving Resources
-------------------------

We've got a very simple server that accepts a request and sends a response.
But what happens if we make a different request?

.. rst-class:: build
.. container::

    .. container::

        In your web browser, enter the following URL::

            http://localhost:10000/page

    .. container::

        What happened? What happens if you use this URL::

            http://localhost:10000/section/page?


.. nextslide:: Determining a Resource

We expect different urls to result in different responses.

.. rst-class:: build
.. container::

    Each separate *path* provided should map to a *resource*

    But this isn't happening with our server, for obvious reasons.

    It brings us back to the second element of that first line of an HTTP
    request.

    .. rst-class:: centered

    **The Return of the URI**


.. nextslide:: HTTP Requests: URI

``GET`` **/path/to/index.html** ``HTTP/1.1``

.. rst-class:: build

* Every HTTP request must include a **URI** used to determine the **resource** to
  be returned

* URI??
  http://stackoverflow.com/questions/176264/whats-the-difference-between-a-uri-and-a-url/1984225#1984225

* Resource?  Files (html, img, .js, .css), but also:

  .. rst-class:: build

  * Dynamic scripts
  * Raw data
  * API endpoints

.. nextslide:: Parsing a Request

Our ``parse_request`` method actually already finds the ``uri`` in the first
line of a request

.. rst-class:: build
.. container::

    All we need to do is update the method so that it *returns* that uri

    Then we can use it.

.. nextslide:: My Solution

.. code-block:: python

    def parse_request(request):
        first_line = request.split("\r\n", 1)[0]
        method, uri, protocol = first_line.split()
        if method != "GET":
            raise NotImplementedError("We only accept GET")
        print >>sys.stderr, 'request is okay'
        # add the following line:
        return uri

.. nextslide:: Pass It Along

Now we can update our server code so that it uses the return value of
``parse_request``.

.. rst-class:: build
.. container::

    That's a pretty simple change:

    .. code-block:: python

        try:
            uri = parse_request(request)  # update this line
        except NotImplementedError:
            response = response_method_not_allowed()
        else:
            # and modify this block
            try:
                content, mime_type = resolve_uri(url)
            except NameError:
                response = response_not_found()
            else:
                response = response_ok(content, mime_type)

Homework
========

.. rst-class:: left
.. container::

    You may have noticed that we just added calls to functions that don't yet
    exist

    .. rst-class:: build
    .. container::

        It's a program that shows you what you want to do, but won't actually
        run.

        For your homework this week you will create these functions, completing
        the HTTP server.

        Your starting point will be what we've made here in class.

        I've added a directory to ``resources/session02`` called ``homework``.

        In it, you'll find this ``http_server.py`` file we've just written in
        class.

        That file also contains enough stub code for the missing functions to
        let the server run.

        And there are more tests for you to make pass!

One Step At A Time
------------------

Take the following steps one at a time. Run the tests in
``assignments/session02/homework`` between to ensure that you are getting it
right.

.. rst-class:: build

* Complete the stub ``resolve_uri`` function so that it handles looking up
  resources on disk using the URI returned by ``parse_request``.

* Make sure that if the URI does not map to a file that exists, it raises an
  appropriate error for our server to handle.

* Complete the ``response_not_found`` function stub so that it returns a 404
  response.

* Update ``response_ok`` so that it uses the values returned by ``resolve_uri``
  by the URI. (these have already been added to the function signature)

* You'll plug those values into the response you generate in the way required
  by the protocol


HTTP Headers
------------

Along the way, you'll discover that simply returning the content of a file as
an HTTP response body is insufficient. Different *types* of content need to
be identified to your browser

.. rst-class:: build
.. container::

    We can fix this by passing information about exactly what we are returning
    as part of the response.

    HTTP provides for this type of thing with the generic idea of *Headers*


HTTP Headers
------------

Both requests and responses can contain **headers** of the form ``Name: Value``

.. rst-class:: build
.. container::

    .. rst-class:: build

    * HTTP 1.0 has 16 valid headers, 1.1 has 46
    * Any number of spaces or tabs may separate the *name* from the *value*
    * If a header line starts with spaces or tabs, it is considered part of the
      value for the previous header
    * Header *names* are **not** case-sensitive, but *values* may be

    read more about HTTP headers: http://www.cs.tut.fi/~jkorpela/http.html


Content-Type Header
-------------------

A very common header used in HTTP responses is ``Content-Type``. It tells the
client what to expect.

.. rst-class:: build
.. container::

    .. rst-class:: build

    * uses **mime-type** (Multi-purpose Internet Mail Extensions)
    * foo.jpeg - ``Content-Type: image/jpeg``
    * foo.png - ``Content-Type: image/png``
    * bar.txt - ``Content-Type: text/plain``
    * baz.html - ``Content-Type: text/html``

    There are *many* mime-type identifiers:
    http://www.webmaster-toolkit.com/mime-types.shtml


Mapping Mime-types
------------------

By mapping a given file to a mime-type, we can write a header.

.. rst-class:: build
.. container::

    The standard lib module ``mimetypes`` does just this.

    We can guess the mime-type of a file based on the filename or map a file
    extension to a type:

    .. code-block:: pycon

        >>> import mimetypes
        >>> mimetypes.guess_type('file.txt')
        ('text/plain', None)
        >>> mimetypes.types_map['.txt']
        'text/plain'


Resolving a URI
---------------

Your ``resolve_uri`` function will need to accomplish the following tasks:

.. rst-class:: build

* It should take a URI as the sole argument

* It should map the pathname represented by the URI to a filesystem location.

* It should have a 'home directory', and look only in that location.

* If the URI is a directory, it should return a plain-text listing of the
  directory contents and the mimetype ``text/plain``.

* If the URI is a file, it should return the contents of that file and its
  correct mimetype.

* If the URI does not map to a real location, it should raise an exception
  that the server can catch to return a 404 response.


Use Your Tests
--------------

One of the benefits of test-driven development is that the tests that are
failing should tell you what code you need to write.

.. rst-class:: build
.. container::

    As you work your way through the steps outlined above, look at your tests.
    Write code that makes them pass.

    If all the tests in ``assignments/session02/tests.py`` are passing, you've
    completed the assignment.


Submitting Your Homework
------------------------

To submit your homework:

.. rst-class:: build
.. container::

    .. rst-class:: build

    * Do your work in the ``assignments/session02`` directory of **your fork** of
      the class respository

    * When you have all tests passing, push your work to **your fork** in github.

    * Using the github web interface, send me a pull request.

    I will review your work when I receive your pull requests, make comments on
    it there, and then close the pull request.


A Few Steps Further
-------------------

If you are able to finish the above in less than 4-6 hours, consider taking on
one or more of the following challenges:

.. rst-class:: build

* Format directory listings as HTML, so you can link to files.
* Add a GMT ``Date:`` header in the proper format (RFC-1123) to responses.
  *hint: see email.utils.formatdate in the python standard library*
* Add a ``Content-Length:`` header for ``OK`` responses that provides a
  correct value.
* Protect your server against errors by providing, and using, a function that
  returns a ``500 Internal Server Error`` response.
* Instead of returning the python script in ``webroot`` as plain text, execute
  the file and return the results as HTML.
