Python Web Programming
======================

.. image:: img/protocol.png
    :align: left
    :width: 45%

Session 2: Web Protocols

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
     ...
     'socket', 'ssl', 'sys', 'time']
    >>> imaplib.Debug = 4

.. class:: incremental

Setting ``imap.Debug`` shows us what is sent and received


IMAP in Python
--------------

I've prepared a server for us to use, we'll need to set up a client to speak
to it. Our server requires SSL for connecting to IMAP servers, so let's
initialize an IMAP4_SSL client and authenticate::

    >>> conn = imaplib.IMAP4_SSL('mail.webfaction.com')
      57:04.83 imaplib version 2.58
      57:04.83 new IMAP4 connection, tag=FNHG
      ...
    >>> conn.login(username, password)
      12:16.50 > IMAD1 LOGIN username password
      12:18.52 < IMAD1 OK Logged in.
    ('OK', ['Logged in.'])


IMAP in Python
--------------

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

    >>> conn.search(None, '(FROM "cris")')
      18:25.41 > FNHG5 SEARCH (FROM "cris")
      18:25.54 < * SEARCH 1
      18:25.54 < FNHG5 OK Search completed.
    ('OK', ['1'])
    >>>


IMAP in Python
--------------

Once we've found a message we want to look at, we can use the ``fetch``
command to read it from the server. IMAP allows fetching each part of
a message independently::

    >>> conn.fetch('1', '(BODY[HEADER])')
    ...
    >>> conn.fetch('1', '(BODY[TEXT])')
    ...
    >>> conn.fetch('1', '(FLAGS)')


Python Means Batteries Included
-------------------------------

So we can download an entire message and then make a Python email message
object

.. class:: small

::

    >>> import email
    >>> typ, data = conn.fetch('1', '(RFC822)')
      28:08.40 > FNHG8 FETCH 1 (RFC822)
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

Once we have that, we can play with the resulting email object:

.. class:: small

::

    >>> msg.keys()
    ['Return-Path', 'X-Original-To', 'Delivered-To', 'Received', 
     ...
     'To', 'Mime-Version', 'X-Mailer']
    >>> msg['To']
    'demo@crisewing.com'
    >>> print msg.get_payload()[0]
    If you are reading this email, ...

.. class:: incremental center

**Neat, huh?**


What Have We Learned?
---------------------

.. class:: incremental

* Protocols are just a set of rules for how to communicate

* Protocols tell us how to parse and delimit messages

* Protocols tell us what messages are valid

* If we properly format request messages to a server, we can get response
  messages

* Python supports a number of these protocols

* So we don't have to remember how to format the commands ourselves

.. class:: incremental

But in every case we've seen, we could do the same thing with a socket and
some strings


Break Time
----------

Let's take a few minutes here to clear our heads.

.. class:: incremental

See you back here in 10 minutes.


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
* A required initial line (a command or a response code)
* A (mostly) optional set of headers, one per line
* A blank line
* An optional body


HTTP In Real Life
-----------------

Let's investigate the HTTP protocol a bit in real life.  

.. class:: incremental

We'll do so by building a simplified HTTP server, one step at a time.

.. class:: incremental

There is a copy of the echo server from last time in ``resources/session02``.
It's called ``http_server.py``.

.. class:: incremental

In a terminal, move into that directory. We'll be doing our work here for the
rest of the session


TDD IRL (a quick aside)
-----------------------

Test Driven Development (TDD) is all the rage these days.

.. class:: incremental

It means that before you write code, you first write tests demonstrating what
you want your code to do.

.. class:: incremental

When all your tests pass, you are finished. You did this for your last
assignment.

.. class:: incremental

We'll be doing it again today.


Run the Tests
-------------

From inside ``resources/session02`` start a second python interpreter and run
``$ python http_server.py``

.. container:: incremental
    
    In your first interpreter run the tests. You should see similar output:
    
    .. class:: small
    
    ::
    
        $ python tests.py
        [...]
        Ran 10 tests in 0.003s

        FAILED (failures=3, errors=7)


.. class:: incremental

Let's take a few minutes here to look at these tests and understand them.


Viewing an HTTP Request
-----------------------

Our job is to make all those tests pass.

.. class:: incremental

First, though, let's pretend this server really is a functional HTTP server.

.. class:: incremental

This time, instead of using the echo client to make a connection to the
server, let's use a web browser!

.. class:: incremental

Point your favorite browser at ``http://localhost:10000``


A Bad Interaction
-----------------

First, look at the printed output from your echo server.

.. class:: incremental

Second, note that your browser is still waiting to finish loading the page

.. class:: incremental

Moreover, your server should also be hung, waiting for more from the 'client'

.. class:: incremental

This is because we are not yet following the right protocol.


Echoing A Request
-----------------

Kill your server with ``ctrl-c`` (the keyboard interrupt) and you should see
some printed content:

.. class:: small incremental

::

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

.. class:: incremental

Your results will vary from mine.

HTTP Debugging
--------------

When working on applications, it's nice to be able to see all this going back
and forth.  

.. container:: incremental

    Good browsers support this with a set of developer tools built-in.

    .. class:: small incremental

    * firefox -> ctrl-shift-K or cmd-opt-K (os X)
    * safari -> enable in preferences:advanced then cmd-opt-i
    * chrome -> ctrl-shift-i or cmd-opt-i (os X)
    * IE (7.0+) -> F12 or tools menu -> developer tools

.. class:: incremental

The 'Net(work)' pane of these tools can show you both request and response,
headers and all. Very useful.


Stop! Demo Time
---------------

.. class:: big-centered

Let's take a quick look


Other Debugging Options
-----------------------

Sometimes you need or want to debug http requests that are not going through
your browser.

.. class:: incremental

Or perhaps you need functionality that is not supported by in-browser tools
(request munging, header mangling, decryption of https request/responses)

.. container:: incremental

    Then it might be time for an HTTP debugging proxy:

    * windows: http://www.fiddler2.com/fiddler2/
    * win/osx/linux: http://www.charlesproxy.com/


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


HTTP Responses
--------------

In both HTTP 1.0 and 1.1, a proper response consists of an intial line,
followed by optional headers, a single blank line, and then optionally a
response body::

    HTTP/1.1 200 OK
    Content-Type: text/plain
    <CRLF>
    this is a pretty minimal response

.. class:: incremental

Let's update our server to return such a response.


Basic HTTP Protocol
-------------------

Begin by implementing a new function in your ``http_server.py`` script called
`response_ok`.

.. class:: incremental

It can be super-simple for now.  We'll improve it later.

.. container:: incremental

    It needs to return our minimal response from above:

    .. class:: small
    
    ::
    
        HTTP/1.1 200 OK
        Content-Type: text/plain
        <CRLF>
        this is a pretty minimal response

.. class:: incremental small

**Remember, <CRLF> is a placeholder for an intentionally blank line**


My Solution
-----------

.. code-block:: python
    :class: incremental

    def response_ok():
        """returns a basic HTTP response"""
        resp = []
        resp.append("HTTP/1.1 200 OK")
        resp.append("Content-Type: text/plain")
        resp.append("")
        resp.append("this is a pretty minimal response")
        return "\r\n".join(resp)


Run The Tests
-------------

We've now implemented a function that is tested by our tests. Let's run them
again:

.. class:: incremental small

::

    $ python tests.py
    [...]
    ----------------------------------------------------------------------
    Ran 10 tests in 0.002s

    FAILED (failures=3, errors=3)

.. class:: incremental

Great!  We've now got 4 tests that pass.  Good work.

Server Modifications
--------------------

Next, we need to rebuild the server loop from our echo server for it's new
purpose:

.. class:: incremental

It should now wait for an incoming request to be *finished*, *then* send a
response back to the client.

.. class:: incremental

The response it sends can be the result of calling our new ``response_ok``
function for now.

.. class:: incremental

We could also bump up the ``recv`` buffer size to something more reasonable
for HTTP traffic, say 1024.

My Solution
-----------

.. code-block:: python
    :class: incremental small

    # ...
    try:
        while True:
            print >>log_buffer, 'waiting for a connection'
            conn, addr = sock.accept() # blocking
            try:
                print >>log_buffer, 'connection - {0}{1}'.format(*addr)
                while True:
                    data = conn.recv(1024)
                    if len(data) < 1024:
                        break
                
                print >>log_buffer, 'sending response'
                response = response_ok()
                conn.sendall(response)
            finally:
                conn.close()
    # ...


Run The Tests
-------------

Once you've got that set, restart your server::

    $ python http_server.py

.. container:: incremental

    Then you can re-run your tests:

    .. class:: small

    ::

        $ python tests.py
        [...]
        ----------------------------------------------------------------------
        Ran 10 tests in 0.003s

        FAILED (failures=2, errors=3)

.. class:: incremental

Five tests now pass!

Parts of a Request
------------------

Every HTTP request **must** begin with a single line, broken by whitespace into
three parts::

    GET /path/to/index.html HTTP/1.1

.. class:: incremental

The three parts are the *method*, the *URI*, and the *protocol*

.. class:: incremental

Let's look at each in turn.


HTTP Methods
------------

**GET** ``/path/to/index.html HTTP/1.1``

.. class:: incremental

* Every HTTP request must start with a *method*
* There are four main HTTP methods:

    .. class:: incremental

    * GET
    * POST
    * PUT
    * DELETE

.. class:: incremental

* There are others, notably HEAD, but you won't see them too much


HTTP Methods
------------

These four methods are mapped to the four basic steps (*CRUD*) of persistent
storage:

.. class:: incremental

* POST = Create
* GET = Read
* PUT = Update
* DELETE = Delete


Methods: Safe <--> Unsafe
-------------------------

HTTP methods can be categorized as **safe** or **unsafe**, based on whether
they might change something on the server:

.. class:: incremental

* Safe HTTP Methods
    * GET
* Unsafe HTTP Methods
    * POST
    * PUT
    * DELETE

.. class:: incremental

This is a *normative* distinction, which is to say **be careful**


Methods: Idempotent <--> ???
----------------------------

HTTP methods can be categorized as **idempotent**, based on whether a given
request will always have the same result:

.. class:: incremental

* Idempotent HTTP Methods
    * GET
    * PUT
    * DELETE
* Non-Idempotent HTTP Methods
    * POST

.. class:: incremental

Again, *normative*. The developer is responsible for ensuring that it is true.


HTTP Method Handling
--------------------

Let's keep things simple, our server will only respond to *GET* requests.

.. class:: incremental

We need to create a function that parses a request and determines if we can
respond to it: ``parse_request``.

.. class:: incremental

If the request method is not *GET*, our method should raise an error

.. class:: incremental

Remember, although a request is more than one line long, all we care about
here is the first line


My Solution
-----------

.. code-block:: python
    :class: incremental

    def parse_request(request):
        first_line = request.split("\r\n", 1)[0]
        method, uri, protocol = first_line.split()
        if method != "GET":
            raise NotImplementedError("We only accept GET")
        print >>sys.stderr, 'request is okay'


Update the Server
-----------------

We'll also need to update the server code. It should

.. class:: incremental

* save the request as it comes in
* check the request using our new function
* send an OK response if things go well


My Solution
-----------

.. code-block:: python
    :class: incremental small

    # ...
    conn, addr = sock.accept() # blocking
    try:
        print >>log_buffer, 'connection - {0}{1}'.format(*addr)
        request = ""
        while True:
            data = conn.recv(1024)
            request += data
            if len(data) < 1024 or not data:
                break

        parse_request(request)
        print >>log_buffer, 'sending response'
        response = response_ok()
        conn.sendall(response)
    finally:
        conn.close()
    # ...


Run The Tests
-------------

Quit and restart your server now that you've updated the code::

    $ python http_server.py

.. container:: incremental

    At this point, we should have seven tests passing:
    
    .. class:: small
    
    ::
    
        $ python tests.py
        Ran 10 tests in 0.002s
        
        FAILED (failures=1, errors=2)


What About a Browser?
---------------------

Quit and restart your server, now that you've updated the code.

.. class:: incremental

Reload your browser.  It should work fine.

.. class:: incremental

We can use the ``simple_client.py`` script in our resources to test our error
condition.  In a second terminal window run the script like so:

.. class:: incremental

:: 

    $ python simple_client.py "POST / HTTP/1.0\r\n\r\n"

.. class:: incremental

You'll have to quit the client pretty quickly with ``ctrl-c``


Error Responses
---------------

Okay, so the outcome there was pretty ugly. The client went off the rails, and
our server has terminated as well.

.. class:: incremental

The HTTP protocol allows us to handle errors like this more gracefully.

.. class:: incremental center

**Enter the Response Code**


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

Do not be afraid to use other, less common codes in building good apps. There
are a lot of them for a reason. See
http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html


Handling our Error
------------------

Luckily, there's an error code that is tailor-made for this situation.

..  class:: incremental

The client has made a request using a method we do not support

.. class:: incremental

``405 Method Not Allowed``

.. class:: incremental

Let's add a new function that returns this error code. It should be called
``response_method_not_allowed``


My Solution
-----------

.. code-block:: python
    :class: incremental

    def response_method_not_allowed():
        """returns a 405 Method Not Allowed response"""
        resp = []
        resp.append("HTTP/1.1 405 Method Not Allowed")
        resp.append("")
        return "\r\n".join(resp)


Server Updates
--------------

Again, we'll need to update the server to handle this error condition
correctly.  It should

.. class:: incremental

* catch the exception raised by the ``parse_request`` function
* return our new error response as a result
* if no exception is raised, then return the OK response

My Solution
-----------

.. code-block:: python
    :class: incremental small

    # ...
    while True:
        data = conn.recv(1024)
        request += data
        if len(data) < 1024 or not data:
            break

    try:
        parse_request(request)
    except NotImplementedError:
        response = response_method_not_allowed()
    else:
        response = response_ok()

    print >>sys.stderr, 'sending response'
    conn.sendall(response)
    # ...


Run The Tests
-------------

Start your server (or restart it if by some miracle it's still going).

.. container:: incremental

    Then run the tests again:
    
    .. class:: small
    
    ::
    
        $ python tests.py
        [...]
        Ran 10 tests in 0.002s
        
        OK

.. class:: incremental

Wahoo! All our tests are passing. That means we are done writing code for now.


HTTP - Resources
----------------

We've got a very simple server that accepts a request and sends a response.
But what happens if we make a different request?

.. container:: incremental

    In your web browser, enter the following URL::

        http://localhost:10000/page

.. container:: incremental

    What happened? What happens if you use this URL::

        http://localhost:10000/section/page?


HTTP - Resources
----------------

We expect different urls to result in different responses.

.. class:: incremental

But this isn't happening with our server, for obvious reasons.

.. class:: incremental

It brings us back to the second element of that first line of an HTTP request.

.. class:: incremental center

**The Return of the URI**


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


Homework
--------

For your homework this week you will expand your server's capabilities so that
it can make different responses to different URIs.

.. class:: incremental

You'll allow your server to serve up directories and files from your own
filesystem.

.. class:: incremental

You'll be starting from the ``http_server.py`` script that is currently in the
``assignments/session02`` directory. It should be pretty much the same as what
you've created here.


One Step At A Time
------------------

Take the following steps one at a time. Run the tests in
``assignments/session02`` between to ensure that you are getting it right.

.. class:: incremental

* Update ``parse_request`` to return the URI it parses from the request.

* Update ``response_ok`` so that it uses the resource and mimetype identified
  by the URI.

* Write a new function ``resolve_uri`` that handles looking up resources on
  disk using the URI.

* Write a new function ``response_not_found`` that returns a 404 response if the
  resource does not exist.


HTTP Headers
------------

Along the way, you'll discover that simply returning as the body in
response_ok is insufficient. Different *types* of content need to be
identified to your browser

.. class:: incremental

We can fix this by passing information about exactly what we are returning as
part of the response.

.. class:: incremental

HTTP provides for this type of thing with the generic idea of *Headers*


HTTP Headers
------------

Both requests and responses can contain **headers** of the form ``Name: Value``

.. class:: incremental

* HTTP 1.0 has 16 valid headers, 1.1 has 46
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


Mapping Mime-types
------------------

By mapping a given file to a mime-type, we can write a header.

.. class:: incremental

The standard lib module ``mimetypes`` does just this.

.. container:: incremental

  We can guess the mime-type of a file based on the filename or map a file
  extension to a type:

  .. code-block:: python 
      :class: small

      >>> import mimetypes
      >>> mimetypes.guess_type('file.txt')
      ('text/plain', None)
      >>> mimetypes.types_map['.txt']
      'text/plain'


Resolving a URI
---------------

Your ``resolve_uri`` function will need to accomplish the following tasks:

.. class:: incremental

* It should take a URI as the sole argument

* It should map the pathname represented by the URI to a filesystem location.

* It should have a 'home directory', and look only in that location.

* If the URI is a directory, it should return a plain-text listing and the
  mimetype ``text/plain``.

* If the URI is a file, it should return the contents of that file and its
  correct mimetype.

* If the URI does not map to a real location, it should raise an exception
  that the server can catch to return a 404 response.


Use Your Tests
--------------

One of the benefits of test-driven development is that the tests that are
failing should tell you what code you need to write.

.. class:: incremental

As you work your way through the steps outlined above, look at your tests.
Write code that makes them pass.

.. class:: incremental

If all the tests in ``assignments/session02/tests.py`` are passing, you've
completed the assignment.


Submitting Your Homework
------------------------

To submit your homework:

* Do your work in the ``assignments/session02`` directory of **your fork** of
  the class respository

* When you have all tests passing, push your work to **your fork** in github.

* Using the github web interface, send me a pull request.

.. class:: incremental

I will review your work when I receive your pull requests, make comments on it
there, and then close the pull request.


A Few Steps Further
-------------------

If you are able to finish the above in less than 4-6 hours, consider taking on
one or more of the following challenges:

.. class:: incremental

* Format directory listings as HTML, so you can link to files.
* Add a GMT ``Date:`` header in the proper format (RFC-1123) to responses.
  *hint: see email.utils.formatdate in the python standard library*
* Add a ``Content-Length:`` header for ``OK`` responses that provides a
  correct value.
* Protect your server against errors by providing, and using, a function that
  returns a ``500 Internal Server Error`` response.
* Instead of returning the python script in ``webroot`` as plain text, execute
  the file and return the results as HTML.
