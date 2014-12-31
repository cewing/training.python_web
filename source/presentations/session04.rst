Python Web Programming
======================

.. image:: img/python.png
    :align: left
    :width: 33%

Session 1: Networking and Sockets

.. class:: intro-blurb

Wherein we learn about the basic structure of the internet and explore the
building blocks that make it possible.


But First
---------

Class presentations are available online for your use

.. class:: small

https://github.com/UWPCE-PythonCert/training.python_web

.. class:: incremental

Licensed with Creative Commons BY-NC-SA

.. class:: small incremental

* You must attribute the work
* You may not use the work for commercial purposes
* You have to share your versions just like this one

.. class:: incremental

Find mistakes? See improvements? Make a pull request.


But First
---------

Classroom Protocol

.. class:: incremental

Questions to ask:

.. class:: incremental

* What did you just say?
* Please explain what we just did again?
* Why didn't that work for me?
* Is that a typo?


But First
---------

Classroom Protocol

.. class:: incremental

Questions **not** to ask:

.. class:: incremental

* **Hypotheticals**: What happens if I do X?
* **Research**: Can Python do Y?
* **Syllabus**: Are we going to cover Z in class?
* **Marketing questions**: please just don't.
* **Performance questions**: Is Python fast enough?
* **Unpythonic**: Why doesn't Python do it some other way?
* **Show off**: Look what I just did!


But First
---------

.. class:: big-centered

Introductions


Computer Communications
-----------------------

.. image:: img/network_topology.png
    :align: left
    :width: 40%

.. class:: incremental

* processes can communicate

* inside one machine

* between two machines

* among many machines

.. class:: image-credit

image: http://en.wikipedia.org/wiki/Internet_Protocol_Suite


Computer Communications
-----------------------

.. image:: img/data_in_tcpip_stack.png
    :align: left
    :width: 55%

.. class:: incremental

* Process divided into 'layers'

* 'Layers' are mostly arbitrary

* Different descriptions have different layers

* Most common is the 'TCP/IP Stack'

.. class:: image-credit

image: http://en.wikipedia.org/wiki/Internet_Protocol_Suite


The TCP/IP Stack - Link
-----------------------

The bottom layer is the 'Link Layer'

.. class:: incremental

* Deals with the physical connections between machines, 'the wire'

* Packages data for physical transport

* Executes transmission over a physical medium

  * what that medium is is arbitrary

* Implemented in the Network Interface Card(s) (NIC) in your computer


The TCP/IP Stack - Internet
---------------------------

Moving up, we have the 'Internet Layer'

.. class:: incremental

* Deals with addressing and routing

  * Where are we going and how do we get there?

* Agnostic as to physical medium (IP over Avian Carrier - IPoAC)

* Makes no promises of reliability

* Two addressing systems

  .. class:: incremental

  * IPv4 (current, limited '192.168.1.100')

  * IPv6 (future, 3.4 x 10^38 addresses, '2001:0db8:85a3:0042:0000:8a2e:0370:7334')


The TCP/IP Stack - Internet
---------------------------

.. class:: big-centered

That's 4.3 x 10^28 addresses *per person alive today*


The TCP/IP Stack - Transport
----------------------------

Next up is the 'Transport Layer'

.. class:: incremental

* Deals with transmission and reception of data

  * error correction, flow control, congestion management

* Common protocols include TCP & UDP

  * TCP: Tranmission Control Protocol

  * UDP: User Datagram Protocol

* Not all Transport Protocols are 'reliable'

  .. class:: incremental

  * TCP ensures that dropped packets are resent

  * UDP makes no such assurance
  
  * Reliability is slow and expensive


The TCP/IP Stack - Transport
----------------------------

The 'Transport Layer' also establishes the concept of a **port**

.. class:: incremental

* IP Addresses designate a specific *machine* on the network

* A **port** provides addressing for individual *applications* in a single host

* 192.168.1.100:80  (the *:80* part is the **port**)

* [2001:db8:85a3:8d3:1319:8a2e:370:7348]:443 (*:443* is the **port**)

.. class:: incremental

This means that you don't have to worry about information intended for your
web browser being accidentally read by your email client.


The TCP/IP Stack - Transport
----------------------------

There are certain **ports** which are commonly understood to belong to given
applications or protocols:

.. class:: incremental

* 80/443 - HTTP/HTTPS
* 20 - FTP
* 22 - SSH
* 23 - Telnet
* 25 - SMTP
* ...

.. class:: incremental

These ports are often referred to as **well-known ports**

.. class:: small

(see http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)


The TCP/IP Stack - Transport
----------------------------

Ports are grouped into a few different classes

.. class:: incremental

* Ports numbered 0 - 1023 are *reserved*

* Ports numbered 1024 - 65535 are *open*

* Ports numbered 1024 - 49151 may be *registered*

* Ports numbered 49152 - 65535 are called *ephemeral*


The TCP/IP Stack - Application
------------------------------

The topmost layer is the 'Application Layer'

.. class:: incremental

* Deals directly with data produced or consumed by an application

* Reads or writes data using a set of understood, well-defined **protocols**

  * HTTP, SMTP, FTP etc.

* Does not know (or need to know) about lower layer functionality

  * The exception to this rule is **endpoint** data (or IP:Port)


The TCP/IP Stack - Application
------------------------------

.. class:: big-centered

this is where we live and work


Sockets
-------

Think back for a second to what we just finished discussing, the TCP/IP stack.

.. class:: incremental

* The *Internet* layer gives us an **IP Address**

* The *Transport* layer establishes the idea of a **port**.

* The *Application* layer doesn't care about what happens below...

* *Except for* **endpoint data** (IP:Port)

.. class:: incremental

A **Socket** is the software representation of that endpoint.

.. class:: incremental

Opening a **socket** creates a kind of transceiver that can send and/or
receive *bytes* at a given IP address and Port.


Sockets in Python
-----------------

Python provides a standard library module which provides socket functionality.
It is called **socket**.  

.. class:: incremental

The library is really just a very thin wrapper around the system
implementation of *BSD Sockets*

.. class:: incremental

Let's spend a few minutes getting to know this module.

.. class:: incremental

We're going to do this next part together, so open up a terminal and start a
python interpreter


Sockets in Python
-----------------

The Python sockets library allows us to find out what port a *service* uses:

.. class:: small

    >>> import socket
    >>> socket.getservbyname('ssh')
    22

.. class:: incremental

You can also do a *reverse lookup*, finding what service uses a given *port*:

.. class:: incremental small

    >>> socket.getservbyport(80)
    'http'


Sockets in Python
-----------------

The sockets library also provides tools for finding out information about
*hosts*. For example, you can find out about the hostname and IP address of
the machine you are currently using::

    >>> socket.gethostname()
    'heffalump.local'
    >>> socket.gethostbyname(socket.gethostname())
    '10.211.55.2'


Sockets in Python
-----------------

You can also find out about machines that are located elsewhere, assuming you
know their hostname. For example::

    >>> socket.gethostbyname('google.com')
    '173.194.33.4'
    >>> socket.gethostbyname('uw.edu')
    '128.95.155.135'
    >>> socket.gethostbyname('crisewing.com')
    '108.59.11.99'


Sockets in Python
-----------------

The ``gethostbyname_ex`` method of the ``socket`` library provides more
information about the machines we are exploring::

    >>> socket.gethostbyname_ex('google.com')
    ('google.com', [], ['173.194.33.9', '173.194.33.14',
                        ...
                        '173.194.33.6', '173.194.33.7',
                        '173.194.33.8'])
    >>> socket.gethostbyname_ex('crisewing.com')
    ('crisewing.com', [], ['108.59.11.99'])
    >>> socket.gethostbyname_ex('www.rad.washington.edu')
    ('elladan.rad.washington.edu', # <- canonical hostname
     ['www.rad.washington.edu'], # <- any machine aliases
     ['128.95.247.84']) # <- all active IP addresses


Sockets in Python
-----------------

To create a socket, you use the **socket** method of the ``socket`` library.
It takes up to three optional positional arguments (here we use none to get
the default behavior)::

    >>> foo = socket.socket()
    >>> foo
    <socket._socketobject object at 0x10046cec0>


Sockets in Python
-----------------

A socket has some properties that are immediately important to us. These
include the *family*, *type* and *protocol* of the socket::

    >>> foo.family
    2
    >>> foo.type
    1
    >>> foo.proto
    0

.. class:: incremental

You might notice that the values for these properties are integers.  In fact, 
these integers are **constants** defined in the socket library.


A quick utility method
----------------------

Let's define a method in place to help us see these constants. It will take a
single argument, the shared prefix for a defined set of constants:

.. class:: small

::

    >>> def get_constants(prefix):
    ...     """mapping of socket module constants to their names."""
    ...     return dict(
    ...         (getattr(socket, n), n)
    ...         for n in dir(socket)
    ...         if n.startswith(prefix)
    ...     )
    ...
    >>>

.. class:: small

(you can also find this in ``resources/session01/session1.py``)


Socket Families
---------------

Think back a moment to our discussion of the *Internet* layer of the TCP/IP
stack.  There were a couple of different types of IP addresses:

.. class:: incremental

* IPv4 ('192.168.1.100')

* IPv6 ('2001:0db8:85a3:0042:0000:8a2e:0370:7334')

.. class:: incremental

The **family** of a socket corresponds to the *addressing system* it uses for
connecting.


Socket Families
---------------

Families defined in the ``socket`` library are prefixed by ``AF_``::

    >>> families = get_constants('AF_')
    >>> families
    {0: 'AF_UNSPEC', 1: 'AF_UNIX', 2: 'AF_INET',
     11: 'AF_SNA', 12: 'AF_DECnet', 16: 'AF_APPLETALK',
     17: 'AF_ROUTE', 23: 'AF_IPX', 30: 'AF_INET6'}

.. class:: small incremental

*Your results may vary*

.. class:: incremental

Of all of these, the ones we care most about are ``2`` (IPv4) and ``30`` (IPv6).


Unix Domain Sockets
-------------------

When you are on a machine with an operating system that is Unix-like, you will
find another generally useful socket family: ``AF_UNIX``, or Unix Domain
Sockets. Sockets in this family:

.. class:: incremental

* connect processes **on the same machine**

* are generally a bit slower than IPC connnections

* have the benefit of allowing the same API for programs that might run on one
  machine __or__ across the network

* use an 'address' that looks like a pathname ('/tmp/foo.sock')


Test your skills
----------------

What is the *default* family for the socket we created just a moment ago?

.. class:: incremental

(remember we bound the socket to the symbol ``foo``)

.. class:: incremental center

How did you figure this out?


Socket Types
------------

The socket *type* determines the semantics of socket communications.

Look up socket type constants with the ``SOCK_`` prefix::

    >>> types = get_constants('SOCK_')
    >>> types
    {1: 'SOCK_STREAM', 2: 'SOCK_DGRAM',
     ...}

.. class:: incremental

The most common are ``1`` (Stream communication (TCP)) and ``2`` (Datagram
communication (UDP)).


Test your skills
----------------

What is the *default* type for our generic socket, ``foo``?


Socket Protocols
----------------

A socket also has a designated *protocol*. The constants for these are
prefixed by ``IPPROTO_``::

    >>> protocols = get_constants('IPPROTO_')
    >>> protocols
    {0: 'IPPROTO_IP', 1: 'IPPROTO_ICMP',
     ...,
     255: 'IPPROTO_RAW'}

.. class:: incremental

The choice of which protocol to use for a socket is determined by the
*internet layer* protocol you intend to use. ``TCP``? ``UDP``? ``ICMP``?
``IGMP``?


Test your skills
----------------

What is the *default* protocol used by our generic socket, ``foo``?


Custom Sockets
--------------

These three properties of a socket correspond to the three positional
arguments you may pass to the socket constructor. 

.. container:: incremental

    Using them allows you to create sockets with specific communications
    profiles::
    
        >>> bar = socket.socket(socket.AF_INET,
        ...                     socket.SOCK_DGRAM, 
        ...                     socket.IPPROTO_UDP)
        ...
        >>> bar
        <socket._socketobject object at 0x1005b8b40>


Break Time
----------

So far we have:

.. class:: incremental

* learned about the "layers" of the TCP/IP Stack
* discussed *families*, *types* and *protocols* in sockets
* learned how to create sockets with a specific communications profile.

.. class:: incremental

When we return we'll learn how to find the communcations profiles of remote
sockets, how to connect to them, and how to send and receive messages.

.. class:: incremental

Take a few minutes now to clear your head (do not quit your python
interpreter).


Address Information
-------------------

When you are creating a socket to communicate with a remote service, the
remote socket will have a specific communications profile.

.. class:: incremental

The local socket you create must match that communications profile.

.. class:: incremental

How can you determine the *correct* values to use?

.. class:: incremental center

You ask.


Address Information
-------------------

The function ``socket.getaddrinfo`` provides information about available
connections on a given host.

.. code-block:: python
    :class: small

    socket.getaddrinfo('127.0.0.1', 80)

.. class:: incremental

This provides all you need to make a proper connection to a socket on a remote
host. The value returned is a tuple of:

.. class:: incremental

* socket family
* socket type
* socket protocol
* canonical name (usually empty, unless requested by flag)
* socket address (tuple of IP and Port)


A quick utility method
----------------------

Again, let's create a utility method in-place so we can see this in action:

.. class:: small

::

    >>> def get_address_info(host, port):
    ...     for response in socket.getaddrinfo(host, port):
    ...         fam, typ, pro, nam, add = response
    ...         print 'family: ', families[fam]
    ...         print 'type: ', types[typ]
    ...         print 'protocol: ', protocols[pro]
    ...         print 'canonical name: ', nam
    ...         print 'socket address: ', add
    ...         print
    ...
    >>>

.. class:: small

(you can also find this in ``resources/session01/session1.py``)


On Your Own Machine
-------------------

Now, ask your own machine what possible connections are available for 'http'::

    >>> get_address_info(socket.gethostname(), 'http')
    family:  AF_INET
    type:  SOCK_DGRAM
    protocol:  IPPROTO_UDP
    canonical name:  
    socket address:  ('10.211.55.2', 80)
    
    family:  AF_INET
    ...
    >>>

.. class:: incremental

What answers do you get?


On the Internet
---------------

::

    >>> get_address_info('crisewing.com', 'http')
    family:  AF_INET
    type:  SOCK_DGRAM
    ...

    family:  AF_INET
    type:  SOCK_STREAM
    ...
    >>>

.. class:: incremental

Try a few other servers you know about.


First Steps
-----------

.. class:: big-centered

Let's put this to use


Construct a Socket
------------------

We've already made a socket ``foo`` using the generic constructor without any
arguments.  We can make a better one now by using real address information from
a real server online [**do not type this yet**]:

.. class:: small

::

    >>> streams = [info
    ...     for info in socket.getaddrinfo('crisewing.com', 'http')
    ...     if info[1] == socket.SOCK_STREAM]
    >>> streams
    [(2, 1, 6, '', ('108.59.11.99', 80))]
    >>> info = streams[0]
    >>> cewing_socket = socket.socket(*info[:3])


Connecting a Socket
-------------------

Once the socket is constructed with the appropriate *family*, *type* and
*protocol*, we can connect it to the address of our remote server::

    >>> cewing_socket.connect(info[-1])
    >>> 

.. class:: incremental

* a successful connection returns ``None``

* a failed connection raises an error

* you can use the *type* of error returned to tell why the connection failed.


Sending a Message
-----------------

Send a message to the server on the other end of our connection (we'll
learn in session 2 about the message we are sending)::

    >>> msg = "GET / HTTP/1.1\r\n"
    >>> msg += "Host: crisewing.com\r\n\r\n"
    >>> cewing_socket.sendall(msg)
    >>>

.. class:: incremental small

* the transmission continues until all data is sent or an error occurs

* success returns ``None``

* failure to send raises an error

* you can use the type of error to figure out why the transmission failed

* if an error occurs you **cannot** know how much, if any, of your data was
  sent


Receiving a Reply
-----------------

Whatever reply we get is received by the socket we created. We can read it
back out (again, **do not type this yet**)::

    >>> response = cewing_socket.recv(4096)
    >>> response
    'HTTP/1.1 200 OK\r\nDate: Thu, 03 Jan 2013 05:56:53
    ...

.. class:: incremental small

* The sole required argument is ``buffer_size`` (an integer). It should be a
  power of 2 and smallish (~4096)
* It returns a byte string of ``buffer_size`` (or smaller if less data was
  received)
* If the response is longer than ``buffer size``, you can call the method
  repeatedly. The last bunch will be less than ``buffer size``.


Cleaning Up
-----------

When you are finished with a connection, you should always close it::

  >>> cewing_socket.close()


Putting it all together
-----------------------

First, connect and send a message:

.. class:: small

::

    >>> streams = [info
    ...     for info in socket.getaddrinfo('crisewing.com', 'http')
    ...     if info[1] == socket.SOCK_STREAM]
    >>> info = streams[0]
    >>> cewing_socket = socket.socket(*info[:3])
    >>> cewing_socket.connect(info[-1])
    >>> msg = "GET / HTTP/1.1\r\n"
    >>> msg += "Host: crisewing.com\r\n\r\n"
    >>> cewing_socket.sendall(msg)


Putting it all together
-----------------------

Then, receive a reply, iterating until it is complete:

::

    >>> buffsize = 4096
    >>> response = ''
    >>> done = False
    >>> while not done:
    ...     msg_part = cewing_socket.recv(buffsize)
    ...     if len(msg_part) < buffsize:
    ...         done = True
    ...         cewing_socket.close()
    ...     response += msg_part
    ...     
    >>> len(response)
    19427


Server Side
-----------

.. class:: big-centered

What about the other half of the equation?

Construct a Socket
------------------

**For the moment, stop typing this into your interpreter.**

.. container:: incremental

    Again, we begin by constructing a socket. Since we are actually the server
    this time, we get to choose family, type and protocol::

        >>> server_socket = socket.socket(
        ...     socket.AF_INET,
        ...     socket.SOCK_STREAM,
        ...     socket.IPPROTO_TCP)
        ... 
        >>> server_socket
        <socket._socketobject object at 0x100563c90>


Bind the Socket
---------------

Our server socket needs to be bound to an address. This is the IP Address and
Port to which clients must connect::

    >>> address = ('127.0.0.1', 50000)
    >>> server_socket.bind(address)

.. class:: incremental

**Terminology Note**: In a server/client relationship, the server *binds* to
an address and port. The client *connects*


Listen for Connections
----------------------

Once our socket is bound to an address, we can listen for attempted
connections::

    >>> server_socket.listen(1)

.. class:: incremental

* The argument to ``listen`` is the *backlog*

* The *backlog* is the **maximum** number of connection requests that the
  socket will queue

* Once the limit is reached, the socket refuses new connections.


Accept Incoming Messages
------------------------

When a socket is listening, it can receive incoming connection requests::

    >>> connection, client_address = server_socket.accept()
    ... # this blocks until a client connects
    >>> connection.recv(16)

.. class:: incremental

* The ``connection`` returned by a call to ``accept`` is a **new socket**.
  This new socket is used to communicate with the client

* The ``client_address`` is a two-tuple of IP Address and Port for the client
  socket

* When a connection request is 'accepted', it is removed from the backlog
  queue.


Send a Reply
------------

The same socket that received a message from the client may be used to return
a reply::

    >>> connection.sendall("message received")


Clean Up
--------

Once a transaction between the client and server is complete, the
``connection`` socket should be closed::

    >>> connection.close()

.. class:: incremental

Note that the ``server_socket`` is *never* closed as long as the server
continues to run.


Getting the Flow
----------------

The flow of this interaction can be a bit confusing.  Let's see it in action
step-by-step.

.. class:: incremental

Open a second python interpreter and place it next to your first so you can
see both of them at the same time.


Create a Server
---------------

In your first python interpreter, create a server socket and prepare it for
connections::

    >>> server_socket = socket.socket(
    ...     socket.AF_INET,
    ...     socket.SOCK_STREAM,
    ...     socket.IPPROTO_IP)
    >>> server_socket.bind(('127.0.0.1', 50000))
    >>> server_socket.listen(1)
    >>> conn, addr = server_socket.accept()
    
.. class:: incremental

At this point, you should **not** get back a prompt. The server socket is
waiting for a connection to be made.


Create a Client
---------------

In your second interpreter, create a client socket and prepare to send a
message::

    >>> import socket
    >>> client_socket = socket.socket(
    ...     socket.AF_INET,
    ...     socket.SOCK_STREAM,
    ...     socket.IPPROTO_IP)

.. container:: incremental

    Before connecting, keep your eye on the server interpreter::

        >>> client_socket.connect(('127.0.0.1', 50000))


Send a Message Client->Server
-----------------------------

As soon as you made the connection above, you should have seen the prompt
return in your server interpreter. The ``accept`` method finally returned a
new connection socket.

.. class:: incremental

When you're ready, type the following in the *client* interpreter.

.. class:: incremental

::

    >>> client_socket.sendall("Hey, can you hear me?")


Receive and Respond
-------------------

Back in your server interpreter, go ahead and receive the message from your
client::

    >>> conn.recv(32)
    'Hey, can you hear me?'

Send a message back, and then close up your connection::

    >>> conn.sendall("Yes, I hear you.")
    >>> conn.close()


Finish Up
---------

Back in your client interpreter, take a look at the response to your message,
then be sure to close your client socket too::

    >>> client_socket.recv(32)
    'Yes, I hear you.'
    >>> client_socket.close()

And now that we're done, we can close up the server too (back in the server
interpreter)::

    >>> server_socket.close()


Congratulations!
----------------

.. class:: big-centered

You've run your first client-server interaction


Homework
--------

Your homework assignment for this week is to take what you've learned here
and build a simple "echo" server.

.. class:: incremental

The server should automatically return to any client that connects *exactly*
what it receives (it should **echo** all messages).

.. class:: incremental

You will also write a python script that, when run, will send a message to the
server and receive the reply, printing it to ``stdout``.

.. class:: incremental

Finally, you'll do all of this so that it can be tested.


What You Have
-------------

In our class repository, there is a folder ``assignments/session01``.

.. class:: incremental

Inside that folder, you should find:

.. class:: incremental

* A file ``tasks.txt`` that contains these instructions

* A skeleton for your server in ``echo_server.py``

* A skeleton for your client script in ``echo_client.py``

* Some simple tests in ``tests.py``

.. class:: incremental

Your task is to make the tests pass.


Running the tests
-----------------

To run the tests, you'll have to set the server running in one terminal:

.. class:: small

::

    $ python echo_server.py

.. container:: incremental

    Then, in a second terminal, you will execute the tests:
    
    .. class:: small
    
    ::
    
        $ python tests.py

.. container:: incremental

    You should see output like this:
    
    .. class:: small
    
    ::
    
        [...]
        FAILED (failures=2)


Submitting Your Homework
------------------------

To submit your homework:

.. class:: incremental

* In github, make a fork of my repository into *your* account.

* Clone your fork of my repository to your computer.

* Do your work in the ``assignments/session01/`` folder on your computer and
  commit your changes to your fork.

* When you are finished and your tests are passing, you will open a pull
  request in github.com from your fork to mine.

.. class:: incremental

I will review your work when I receive your pull requests, make comments on it
there, and then close the pull request.


Going Further
-------------

In ``assignments/session01/tasks.txt`` you'll find a few extra problems to try.

.. class:: incremental

If you finish the first part of the homework in less than 3-4 hours give one
or more of these a whirl.

.. class:: incremental

They are not required, but if you include solutions in your pull request, I'll
review your work.
