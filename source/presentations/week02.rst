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

Clean Up After Yourself
-----------------------

very few of you closed your server socket before exiting the server script:

.. class:: small

::

    server = socket.socket()
    # set up
    try:
        while True
            # do server stuff
    except KeyboardInterrupt:
        server.close()
        sys.exit()

Use Module Constants
--------------------

Constants are provided to help us 'do the right thing' without needing to
remember what the right thing is, exactly.  So, instead of::

    socket.socket(2,1,0)

use::

    socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM,
                  socket.IPPROTO_IP)

Interaction Can Be Good
-----------------------

.. class:: tiny

::

    try:
        # generate two numbers
        while True:
            try:
                number_one = int(raw_input("Enter the first number in the sum: "))
                break
            except ValueError:
                print "Oops!  That was no valid number.  Try again..."
    
        while True:
            try:
                number_two = int(raw_input("Enter the second number in the sum: "))
                break
            except ValueError:
                print "Oops!  That was no valid number.  Try again..."

A Tricksy Bug
-------------

.. class:: small

::

    ...
    while 1:
        conn, addr = server_socket.accept()
        print "Connection Established."
        # Keep connection alive.
        while 1:
            data = conn.recv(4096)
            listIn = literal_eval(data)
            print 'Values: %s, Type: %s' % (listIn, type(listIn))
            conn.sendall('Sum: %s\n' % sum(listIn))

    conn.close()
    server_socket.close()

The Result
----------

Client: prints correct value

Server: prints ``Values: [0, 1, 2, 3], Type: <type 'list'>``

Server:

.. class:: tiny incremental

::

    Traceback (most recent call last):
      File "training.python_web/assignments/week01/athome/number_server.py", line 34, in <module>
        listIn = literal_eval(data)
      File "/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/ast.py", line 49, in literal_eval
        node_or_string = parse(node_or_string, mode='eval')
      File "/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/ast.py", line 37, in parse
        return compile(expr, filename, mode, PyCF_ONLY_AST)
      File "<unknown>", line 0
    
        ^
    SyntaxError: unexpected EOF while parsing

Screen
------

For running scripts on a \*nix server and keeping them running, even after you
disconnect::

    $ screen
    $ start_process
    <ctrl-a ctrl-d>
    Screen Detached
    $ screen -ls # lists your screens
    $ screen -r connects to only running screen

And Second
----------

.. class:: big-centered

Questions from the Reading?

And Third
---------

.. class:: big-centered

Dan Explains Git!!!

And Now...
----------

.. image:: img/protocol_sea.png
    :align: center
    :width: 48%

.. class:: image-credit

image exerpted from: http://xkcd.com/802/

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

* What do you do on a first date?

* What do you do in a job interview?

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

* how to identify yourself

* how to find a conversation partner

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

SMTP (Identify yourself and find a partner)::

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

What does POP3 look like?
-------------------------

POP3 (Identify yourself and find a partner)::

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
    S: +OK 2 messages (320 octets)
    S: 1 120
    S: 2 200
    S: .

What does POP3 look like?
-------------------------

POP3 (Ask for information, provide answers)::

    C: RETR 1
    S: +OK 120 octets
    S: <the POP3 server sends the text of message 1>
    S: .
    C: DELE 1
    S: +OK message 1 deleted
    C: RETR 2
    S: +OK 200 octets
    S: <the POP3 server sends the text of message 2>
    S: .
    C: DELE 2
    S: +OK message 2 deleted

What does POP3 look like?
-------------------------

POP3 (Say goodbye)::

    C: QUIT
    S: +OK dewey POP3 server signing off (maildrop empty)
    C: <client hangs up>

What does IMAP look like?
-------------------------

IMAP (Identify yourself and find a partner)::

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

Notice Any Difference?
----------------------

POP3 Commands:

.. class:: incremental

* STAT
* LIST
* RETR 1
* DELE 1
* QUIT

Notice Any Difference?
----------------------

IMAP Commands:

.. class:: incremental

* A0001 USER "frobozz" "xyzzy"
* A0002 SELECT INBOX
* A0003 FETCH 1 RFC822.SIZE
* A0004 FETCH 1 BODY[HEADER]
* A0005 FETCH 1 BODY[TEXT]
* A0006 LOGOUT

Notice Any Difference?
----------------------

Sequence Identifiers allow the client to send commands without waiting for
responses.  

Re-ordered IMAP Interaction
---------------------------

::

    C: A0001 USER "frobozz" "xyzzy"
    S: * OK User frobozz authenticated
    C: A0002 SELECT INBOX
    S: ...
    S: A0002 OK [READ-WRITE] SELECT completed
    C: A0003 FETCH 1 RFC822.SIZE
    C: A0004 FETCH 1 BODY[HEADER]
    C: A0005 FETCH 1 BODY[TEXT]
    S: * 1 FETCH (RFC822.SIZE 2545)
    S: A0003 OK FETCH completed
    ...
    ...
    C: A0006 LOGOUT
    ...

Which Protocol do you Choose?
-----------------------------

Stacking commands is more efficient, but would it work for POP3?

.. class:: incremental

Why not?

What does HTTP look like?
-------------------------

HTTP (Ask for information)::

    GET /index.html HTTP/1.1
    Host: www.example.com
    \r\n

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
    \r\n
    <438 bytes of content>

Protocols in Python
-------------------

.. class:: big-centered

Let's try this out for ourselves!

Protocols in Python
-------------------

.. class:: big-centered

Fire up a Python interpreter

SMTP in Python
--------------

Start by importing smtplib (part of the standard library)::

    >>> import smtplib
    >>> dir(smtplib)
    ['CRLF', 'LMTP', 'LMTP_PORT', 'OLDSTYLE_AUTH',
     'SMTP', 'SMTPAuthenticationError', 'SMTPConnectError', 
     'SMTPDataError', 'SMTPException', 'SMTPHeloError', 
     'SMTPRecipientsRefused', 'SMTPResponseException', 
     'SMTPSenderRefused', 'SMTPServerDisconnected', 
     'SMTP_PORT', 'SMTP_SSL', 'SMTP_SSL_PORT', 'SSLFakeFile', 
     '__all__', '__builtins__', '__doc__', '__file__', 
     '__name__', '__package__', '_have_ssl', 'base64', 'email', 
     'encode_base64', 'hmac', 'quoteaddr', 'quotedata', 're', 
     'socket', 'ssl', 'stderr']

SMTP in Python
--------------

Let's make a connection to a server. We'll use one I've set up in advance to
avoid needing to create one of our own::

    >>> server = smtplib.SMTP('smtp.webfaction.com', 587)
    >>> server.set_debuglevel(True) # to see interaction
    >>> server.ehlo()
    send: 'ehlo heffalump.local\r\n'
    reply: '250-smtp.webfaction.com\r\n'
    reply: '250-PIPELINING\r\n'
    reply: '250-SIZE 20971520\r\n'
    reply: '250-VRFY\r\n'
    reply: '250-ETRN\r\n'
    reply: '250-STARTTLS\r\n'
    ...

SMTP in Python
--------------

Does our server support TLS (secure transmissions?)::

    >>> server.has_extn('STARTTLS')
    True

What other extensions are available?::

    >>> server.esmpt_features.keys()
    ['enhancedstatuscodes', 'etrn', 'starttls', 
     'auth', 'dsn', '8bitmime', 'pipelining', 
     'size', 'vrfy']

SMTP in Python
--------------

Some SMTP servers require authentication. This is one such server. Before
passing our username and password, though, we should turn on TLS for the sake
of security::

    >>> server.starttls()
    >>> server.ehlo() # re-identify after TLS begins
    >>> server.login(username, password)

SMTP in Python
--------------

Let's prepare a message to be sent to our server::

    >>> from_addr = "YOUR NAME <fill in this address>"
    >>> to_addrs = "demo@crisewing.com"
    >>> subject = "this is a test"
    >>> message = "a message from python smtplib"

SMTP in Python
--------------

Email sent via SMTP requires certain formatting. It's part of the Protocol. In
particular, note that the headers are separated by CRLF sequences.  This is
very common across internet protocols::

    >>> template = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
    >>> headers = template % (from_addr, to_addrs, subject)

SMTP in Python
--------------

A message is the headers, plus the body of the message::

    >>> email_body = headers + message

Sending the email is accomplished by calling the ``sendmail`` method on our
server object, after which we should close the connection::

    >>> server.sendmail(from_addr, [to_addrs, ], email_body)
    >>> server.close()

Putting it all Together
-----------------------

::

    >>> from_addr = "YOUR NAME <fill in this address>"
    >>> to_addrs = "demo@crisewing.com"
    >>> subject = "this is a test"
    >>> message = "a message from python smtplib"
    >>> template = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
    >>> headers = template % (from_addr, to_addrs, subject)

Putting it all Together
-----------------------

::

    >>> server = smtplib.SMTP('smtp.webfaction.com', 587)
    >>> server.set_debuglevel(True)
    >>> server.ehlo()
    >>> server.starttls()
    >>> server.ehlo() # re-identify after TLS begins
    >>> server.login(username, password)
    >>> email_body = headers + message
    >>> server.sendmail(from_addr, [to_addrs, ], email_body)
    >>> server.close()

Python Means Batteries Included
-------------------------------

So in fact we have a module in the standard library for email support::

    >>> import email.utils
    >>> from email.mime.text import MIMEText
    >>> from_addr = "addr@host.com"
    >>> to_addrs = "other@another.com"
    >>> msg = MIMEText("This is an email message")
    >>> msg['From'] = email.utils.formataddr(("Name", from_addr))
    >>> msg['To'] = email.utils.formataddr(("Name", to_addrs))
    >>> msg['Subject'] = "Simple Test"
    >>> server.sendmail(from_addr, [to_addrs, ], msg.as_string())

IMAP in Python
--------------

.. class:: big-centered

Let's read that email we just sent

IMAP in Python
--------------

Again, begin by importing the module from the Python Standard Library::

    >>> import imaplib
    >>> dir(imaplib)
    ['AllowedVersions', 'CRLF', 'Commands', 
     'Continuation', 'Debug', 'Flags', 'IMAP4', 
     'IMAP4_PORT', 'IMAP4_SSL', 'IMAP4_SSL_PORT', 
     'IMAP4_stream', 'Int2AP', 'InternalDate', 
     'Internaldate2tuple', 'Literal', 'MapCRLF', 
     'Mon2num', 'ParseFlags', 'Response_code', 
     'Time2Internaldate', 'Untagged_response', 
     'Untagged_status', '_Authenticator', ...]

IMAP in Python
--------------

We set up a client object.  WebFaction requires SSL for connecting to IMAP
servers, so let's initialize an IMAP4_SSL client and authenticate::

    >>> conn = imaplib.IMAP4_SSL('mail.webfaction.com')
      57:04.83 imaplib version 2.58
      57:04.83 new IMAP4 connection, tag=FNHG
    >>> conn.login(username, password)
    ('OK', ['Logged in.'])

IMAP in Python
--------------

Let's set up debugging here too, so that we can see the communication back and
forth between client and server::

    >>> conn.debug = 4 # >3 prints all messages

We can start by listing the mailboxes we have on the server::

    >>> conn.list()
      00:41.91 > FNHG3 LIST "" *
      00:41.99 < * LIST (\HasNoChildren) "." "INBOX"
      00:41.99 < FNHG3 OK List completed.
    ('OK', ['(\\HasNoChildren) "." "INBOX"'])

IMAP in Python
--------------

We can find out about the mail on our server. We do this by querying for
`status`. IMAP provides a few different status values, let's ask for them
all::

    >>> vals = '(MESSAGES RECENT UIDNEXT'
    >>> vals += ' UIDVALIDITY UNSEEN)'
    >>> conn.status('INBOX', vals)
      12:03.91 > FNHG4 STATUS INBOX (MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)
      12:04.01 < * STATUS "INBOX" (MESSAGES 2 RECENT 0 UIDNEXT 3 UIDVALIDITY 1357449499 UNSEEN 1)
      12:04.01 < FNHG4 OK Status completed.
    ('OK', ['"INBOX" (MESSAGES 2 RECENT 0 
                      UIDNEXT 3 UIDVALIDITY 1357449499 
                      UNSEEN 1)'])

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

IMAP in Python
--------------

It is even possible to download an entire message in raw format, and load that
into a python email message object::

    >>> import email
    >>> typ, data = conn.fetch('2', '(RFC822)')
      28:08.40 > FNHG8 FETCH 2 (RFC822)
      ...
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

IMAP in Python
--------------

.. class:: big-centered

Neat, huh?

What Have We Learned?
---------------------

.. class:: incremental

* Protocols are just a set of rules for how to communicate

* A given protocol has a set of commands it knows

* If we properly format requests to a server, we can get answers

* Python supports a number of these protocols

    * So we don't have to remember how to format the commands ourselves

    .. class:: incremental

     * But in every case we've seen so far, we could do the same thing with a
       socket and some strings

HTTP
----

.. class:: big-centered

HTTP is no different

HTTP
----

We are concerned with two things in HTTP:

.. class:: incremental

* Requests (Asking for information)
* Responses (Providing answers)

HTTP Req/Resp Format
--------------------

Both share a common basic format:

.. class:: incremental

* Line separators are <CRLF>
* An required initial line
* A (mostly) optional set of headers, one per line
* A blank line
* An optional body

.. class:: incremental

"Be strict in what you send and tolerant in what you receive"

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

These four verbs are mapped to the four basic steps of a *CRUD* content management
cycle:

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

Lab Time
--------

For this lab, we'll be building a basic HTTP server.

* update your fork of the class repository by pulling from the ``upstream`` remote

* find the folder ``assignments/week02/lab`` and open ``echo_server.py``

    * this is a canonical example of what we built last week

* We'll move in steps to turn this into an HTTP server.

Lab Time - Step 1
-----------------

First, echo an HTTP request

* Run `echo_server.py` in a terminal

* Point your browser at ``http://localhost:5000``, what do you get back?

* Save the script as ``http_serve1.py``, then edit it to make it return the
  HTML you find in ``tiny_html.html``

* What does this look like?

Lab Time - Step 2
-----------------

Return a proper HTTP response:

* Save the file as ``http_serve2.py``

* Add a new method that takes a string 'body' and returns a proper ``200 OK``
  HTTP response.  Call the method ``ok_response``.

* Bonus Points: add a GMT ``Date:`` header in the proper format (RFC-1123).
  *hint: see email.utils.formatdate in the python standard library*

* How does the returned HTML look now?

Lab Time - Step 3
-----------------

Parse an incoming request to get the URI:

* Save the file as ``http_serve3.py``

* Add a new method called ``parse_request`` that takes a request and returns a
  URI. Have the server print the URI to the console (rudimentary logging).

* Make sure that the method validates that the incoming request is HTTP and
  that the verb is ``GET``. If either is not true, it should raise a
  ValueError

* Bonus points: add an ``client_error_response`` method that returns an
  appropriate HTTP code if the validation from ``parse_request`` fails. What
  is the right response code?

Lab Time - Step 4
-----------------

Serve directory listings:

* Save the file as ``http_serve4.py`` * Add a method called ``resolve_uri``
  which takes as an argument the URI returned from our previous step and
  returns an HTTP response. The method should start from a given directory
  ('web') and check the URI:

    * If the URI names a directory, return the content listing as a ``200 OK``
    
    * If the URI names a file, raise a NotImplementedError (coming soon)
    
    * If the URI does not exist, raise a ValueError

* Bonus points: add a ``notfound_response`` method that returns a proper ``404
  Not Found`` response to the client. Use it when appropriate. (where is
  that?)

Lab Time - Step 5
-----------------

Serve different types of files:

* Save the file as ``http_serve5.py``

* Update the ``resolve_uri`` method. If the URI names a file, return it as the
  body of a ``200 OK`` response.

* You'll need a way to return the approprate ``Content-Type:`` header.

* Support at least ``.html``, ``.txt``, ``.jpeg``, and ``.png`` files

* Try it out.

.. class:: incremental

You've now got a reasonably functional HTTP web server.  Congratulations!

Assignment
----------

Using what you've learned this week, take your new webserver to the next
level. Accomplish as many of the following as you can:

* If you were unable to complete the first five steps in class, circle back
  and finish them

* Complete the 'Bonus point' parts from the first five steps, if you haven't
  already done so

* Format your directory listing as HTML

* In the HTML directory listing, make the files clickable links

* Add a new, dynamic endpoint. If the URI /time-page is requested, return an
  HTML page with the current time displayed.

Submitting the Assignment
-------------------------

* Copy your final html server into the ``assignments/week02/athome``
  directory in your fork of the repository.

* Copy the ``assignments/week02/lab/web`` directory into
  ``assignments/week02/at_home``

* Make a new plain-text file at the top level of the web directory. Tell me
  what you did in it.

* Make a new pull request for the week02 assignments.

* I should be able to run the server on my local machine, open your plain text
  file in my browser, and evaluate your work from there.

* For bonus points, set the server running on your VM, with the ``web`` home
  directory. I should be able to load http://yourserver.bluboxgrid.com:50000
  in my web browser and evaluate your results.

Lightning Talks
---------------

.. class:: big-centered

Ready, Steady, GO!