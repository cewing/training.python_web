Internet Programming with Python
================================

.. image:: img/python.png
    :align: left
    :width: 33%

Week 1: Networking and Sockets

.. class:: intro-blurb

Wherein we learn about the basic structure of the internet and explore the
building blocks that make it possible.

But First
---------

.. class:: big-centered

Mumbo-Jumbo

But First
---------

Class presentations are available online for your use

http://github.com/cewing/training.python_web

Licensed with Creative Commons BY-NC-SA

* You must attribute the work
* You may not use the work for commercial purposes
* You have to share your versions just like this one

Find mistakes? See improvements? Make a pull request.

But First
---------

Class Structure

* ~20 minutes of Review and Discussion

* 5 minute break

* ~1 hour of Lecture and Exercises

* 10 minute break

* ~1 hour of Lab Time

* 5 minute break

* ~20 minutes of Lightning Talks

But First
---------

I'll spend a lot of time talking

.. class:: incremental

Don't make the mistake of thinking this means I know everything

.. class:: incremental

Each of us has domain expertise, share it

But First
---------

.. class:: big-centered

Introductions

Finally
-------

.. class:: big-centered

    And now, let us begin!

Questions From the Reading?
---------------------------

.. class:: big-centered

do you have any?

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

* Primarily uses the Network Interface Card (NIC) in your computer

The TCP/IP Stack - Internet
---------------------------

Moving up, we have the 'Internet Layer'

.. class:: incremental

* Deals with addressing and routing

  * Where are we going?

  * What path do we take to get there?

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

.. class:: small

(see http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)

The TCP/IP Stack - Transport
----------------------------

Ports are grouped into a few different classes

.. class:: incremental

* Ports numbered 0 - 1023 are *reserved* 

* Ports numbered 1024 - 65535 are *open*

* Ports numbered 49152 - 65535 are generally considered *ephemeral*

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
receive data at a given IP address and Port.

Sockets in Python
-----------------

Python provides a standard library module which provides socket functionality.
It is called **socket**.  Let's spend a few minutes getting to know this
module.

We're going to do this next part together, so open up a terminal and start
python.

Sockets in Python
-----------------

The sockets library provides tools for finding out information about hosts on
the network. For example, you can find out about the machine you are currently
using::

    >>> import socket
    >>> socket.gethostname()
    'heffalump.local'
    >>> socket.gethostbyname(socket.gethostname())
    '10.211.55.2'
    >>> socket.gethostbyname_ex(socket.gethosthame())
    ('heffalump.local', [], ['10.211.55.2', '10.37.129.2', '192.168.1.102'])

Sockets in Python
-----------------

You can also find out about machines that are located elsewhere, for example::

    >>> socket.gethostbyname_ex('google.com')
    ('google.com', [], ['173.194.33.9', '173.194.33.14', 
                        ...
                        '173.194.33.6', '173.194.33.7', 
                        '173.194.33.8'])
    >>> socket.gethostbyname_ex('www.rad.washington.edu')
    ('elladan.rad.washington.edu', # <- canonical hostname
     ['www.rad.washington.edu'], # <- any aliases
     ['128.95.247.84']) # <- all active IP addresses

Sockets in Python
-----------------

To create a socket, you use the **socket** method of the ``socket`` library::

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

Socket Families
---------------

Think back a moment to our discussion of the *Internet* layer of the TCP/IP
stack.  There were a couple of different types of IP addresses:

.. class:: incremental

* IPv4 ('192.168.1.100')

* IPv6 ('2001:0db8:85a3:0042:0000:8a2e:0370:7334')

.. class:: incremental

The *family* of a socket corresponds to the type of address you use to make a
connection to it.

A quick utility method
----------------------

Let's explore these families for a moment.  To do so, we're going to define
a method we can use to read contstants from the ``socket`` library.  It will 
take a single argument, the shared prefix for a defined set of constants::

    >>> def get_constants(prefix):
    ...     """mapping of socket module constants to their names."""
    ...     return dict( (getattr(socket, n), n)
    ...                  for n in dir(socket)
    ...                  if n.startswith(prefix)
    ...                  )
    ...
    >>>

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

Socket Families
---------------

What is the *default* family for the socket we created just a moment ago?

.. class:: incremental

(remember we bound the socket to the symbol ``foo``)

Socket Types
------------

The socket type determines how the socket handles connections. Socket type
constants defined in the ``socket`` library are prefixed by ``SOCK_``::

    >>> types = get_constants('SOCK_')
    >>> types
    {1: 'SOCK_STREAM', 2: 'SOCK_DGRAM',
     ...}

.. class:: incremental

In general, the only two of these that are widely useful are ``1``
(representing TCP type connections) and ``2`` (representing UDP type
connections).

Socket Types
------------

What is the *default* type for our generic socket, ``foo``?

Socket Protocols
----------------

A socket also has a designated *protocol*. The constants for these are
prefixed by ``IPPROTO``::

    >>> protocols = get_constants('IPPROTO_')
    >>> protocols
    {0: 'IPPROTO_IP', 1: 'IPPROTO_ICMP',
     ...,
     255: 'IPPROTO_RAW'}

.. class:: incremental

The choice of which protocol to use for a socket is determined by the type of
activity the socket is intended to support.  What messages are you needing to
send?

Socket Protocols
----------------

What is the *default* protocol used by our generic socket, ``foo``?

Address Information
-------------------

When creating a socket, you can provide ``family``, ``type`` and ``protocol``
as arguments to the constructor::

    >>> bar = socket.socket(socket.AF_INET,
    ...                     socket.SOCK_STREAM, 
    ...                     socket.IPPROTO_IP)
    ...
    >>> bar
    <socket._socketobject object at 0x1005b8b40>

Address Information
-------------------

But how do you find out the *right* values?

.. class:: incremental

You ask.

A quick utility method
----------------------

Create the following function::

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

On Your Own Machine
-------------------

Now, ask your own machine what services are available on 'http'::

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

    >>> get_address_info('www.google.com', 'http')
    family:  AF_INET
    type:  SOCK_STREAM
    protocol:  IPPROTO_TCP
    canonical name:  
    socket address:  ('74.125.129.105', 80)
    
    family:  AF_INET
    ...
    >>>

.. class:: incremental

Try a few other servers you know about.

First Steps
-----------

.. class:: big-centered

Let's put this to use

Client Connections
------------------

The information returned by a call to ``socket.getaddrinfo`` is all you need
to make a proper connection to a socket on a remote host.  The value returned
is a tuple of

.. class:: incremental

* socket family
* socket type
* socket protocol
* canonical name
* socket address

Construct a Socket
------------------

We've already made a socket ``foo`` using the generic constructor without any
arguments.  We can make a better one now by using real address information from
a real server online::

    >>> all = socket.getaddrinfo('www.google.com', 'http')
    >>> info = all[0]
    >>> info
    (2, 1, 6, '', ('173.194.79.104', 80))
    >>> google_socket = socket.socket(*info[:3])
    

Connecting a Socket
-------------------

Once the socket is constructed with the appropriate *family*, *type* and
*protocol*, we can connect it to the address of our remote server::

    >>> google_socket.connect(info[-1])
    >>> 

.. class:: incremental

* a successful connection returns ``None``

* a failed connection raises an error

* you can use the *type* of error returned to tell why the connection failed.

Sending a Message
-----------------

We can send a message to the server on the other end of our connection::

    >>> msg = "GET / HTTP/1.1\r\n\r\n"
    >>> google_socket.sendall(msg)
    >>>

.. class:: incremental

* the transmission continues until all data is sent or an error occurs

* success returns ``None``

* failure to send raises an error 

* you can use the type of error to figure out why the transmission failed

* you cannot know how much, if any, of your data was sent

Receiving an Reply
------------------

Whatever reply we get is received by the socket we created. We can read it
back out::

    >>> response = google_socket.recv(4096)
    >>> response
    'HTTP/1.1 200 OK\r\nDate: Thu, 03 Jan 2013 05:56:53
    ...

.. class:: incremental

* The sole required argument is a buffer size, it should be a power of 2 and
  smallish

* the returned value will be a string of buffer size (or smaller if less data
  was received)


Cleaning Up
-----------

When you are finished with a connection, you should always close it::

    >>> google_socket.close()

Putting it all together
-----------------------

::

    >>> all = socket.getaddrinfo('google.com', 'http')
    >>> info = all[0]
    >>> gs = socket.socket(*info[:3])
    >>> gs.connect(info[-1])
    >>> msg = "GET / HTTP/1.1\r\n\r\n"
    >>> gs.sendall(msg)
    >>> response = gs.recv(4096)
    >>> response
    ... 'HTTP/1.1 200 OK\r\n...
    >>> gs.close()

Server Side
-----------

.. class:: big-centered

What about the other half of the equation?

Construct a Socket
------------------

For the moment, stop typing this into your interpreter.

Again, we begin by constructing a socket. Since we are actually the server
this time, we get to choose family, type and protocol::

    >>> server_socket = socket.socket(
    ...     socket.AF_INET,
    ...     socket.SOCK_STREAM,
    ...     socket.IPPROTO_IP)
    ... 
    >>> server_socket
    <socket._socketobject object at 0x100563c90>

Bind the Socket
---------------

Our server socket needs to be bound to an address. This is the IP Address and
Port to which clients must connect::

    >>> address = ('127.0.0.1', 50000)
    >>> server_socket.bind(address)

Listen for Connections
----------------------

Once our socket is created, we use it to listen for attempted connections::

    >>> server_socket.listen(1)

.. class:: incremental

* the argument to ``listen`` is the *backlog*

* the *backlog* is the maximum number of connections that the socket will queue

* once the limit is reached, the socket refuses new connections


Accept Incoming Messages
------------------------

When a socket is listening, it can receive incoming messages::

    >>> connection, client_address = server_socket.accept()
    ... # note that nothing happens here until a client sends something
    >>> connection.recv(16)

.. class:: incremental

* the ``connection`` returned by a call to ``accept`` is a **new socket**

* you do not need to know what port it uses, this is managed

* the ``client_address`` is a two-tuple of IP Address and Port (very familiar)

* ``backlog`` represents the maximum number of ``connection`` sockets that a
  server can spin off

* close a ``connection`` socket to accept a new connection once the max is
  reached

Send a Reply
------------

You can use the ``connection`` socket spun off by ``accept`` to send a reply
back to the client socket::

    >>> connection.sendall("messasge received")

Clean Up
--------

Once a transaction between the client and server is complete, the
``connection`` socket should be closed so that new connections can be made::

    >>> connection.close()

Putting it all together
-----------------------

Open a second terminal next to your first, and let's try out the full
connection:

.. image:: img/socket_interaction.png
    :align: center
    :width: 100%


Lab Time
--------

For our class lab time today, let's explore what we've learned. First, we'll
need the samples:

.. class:: incremental

* visit the class repository (http://github.com/cewing/training.python_web)

* `create a fork`_ of the repository in your own git account

* clone your fork to your local machine

.. _create a fork: http://help.github.com/articles/fork-a-repo

Lab Time
--------

In the repository you've just cloned, you'll find a directory called
``assignments``. This is where all our class lab and take-home assignments
will be located.

.. class:: incremental

* Find ``assignments/week01/lab``

* Open ``echo_server.py`` and ``echo_client.py``

* Using what you've learned today, complete the server and client by replacing
  comments with real code

* Start the server on your local machine, run the client and send some messages

* If you complete that, then copy the server to your Blue Box VM. Run it
  remotely and use the client to send it some messages

* What do you have to change to make that work?

Assignment
----------

Using what you've learned, expand on the client/server relationship. Create a
server which accepts two numbers, adds them, and returns the result to the
client.

Submitting the Assignment
-------------------------

* Add ``sum_server.py`` and ``sum_client.py`` to the
  ``assignments/week01/athome/`` directory of your fork of the class
  repository.

* When you are satisfied with your code, `make a pull request`_

* I should be able to run the server and client scripts on my local machine
  and get results.

* For bonus points, set the server running on your VM. I should be able to run
  your client script from my local machine and get the expected reply.

* Due by Sunday morning if you want me to review it :)

.. _make a pull request: http://help.github.com/articles/using-pull-requests