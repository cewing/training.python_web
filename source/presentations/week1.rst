Internet Programming with Python
================================

.. image:: ../../../img/python.png
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

If you find mistakes, or see improvements, feel free to make a pull request

But First
---------

.. class:: big-centered

Classroom Mechanics

But First
---------

* ~1 hour of Lecture and Discussion

* 10 minute break

* ~1 hour of Lab Time

* 10 minute break

* ~30 minutes of Lightning Talks

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

.. image:: ../../../img/network_topology.png
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

.. image:: ../../../img/data_in_tcpip_stack.png
    :align: left
    :width: 50%

.. class:: incremental

* We divide the process into 'layers'

* 'Layers' are mostly arbitrary descriptions

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
