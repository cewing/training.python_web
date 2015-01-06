Web Service API Addenda
=======================

The following are provided as self-directed exercises. We just don't have the
time to cover them in depth in class.


XML-RPC
-------

Examples of XML-RPC using the Python Standard Library


XML-RPC Example - Server
------------------------

xmlrpc_server.py:

.. code-block:: python
    :class: small

    from SimpleXMLRPCServer import SimpleXMLRPCServer
    
    server = SimpleXMLRPCServer(('localhost', 50000))
    
    def multiply(a, b):
        return a * b
    server.register_function(multiply)
    
    try:
        print "Use Ctrl-C to Exit"
        server.serve_forever()
    except KeyboardInterrupt:
        print "Exiting"


XML-RPC Example - Client
------------------------

We can run a client from a terminal. First, open one terminal and run the
xmlrpc_server.py script:

    $ python xmlrcp_server.py

Then, open another terminal and start up python:

.. code-block:: python
    :class: small

    >>> import xmlrpclib
    >>> proxy = xmlrpclib.ServerProxy('http://localhost:50000', verbose=True)
    >>> proxy.multiply(3, 24)
    ...
    72


XML-RPC Request
---------------

``verbose=True`` allows us to see the request we sent:

.. class:: tiny

::

    POST /RPC2 HTTP/1.0
    Host: localhost:50000
    User-Agent: xmlrpclib.py/1.0.1 (by www.pythonware.com)
    Content-Type: text/xml
    Content-Length: 192
    
    <?xml version='1.0'?>
    <methodCall>
     <methodName>multiply</methodName>
     <params>
      <param>
       <value><int>3</int></value>
      </param>
      <param>
       <value><int>24</int></value>
      </param>
     </params>
    </methodCall>


XML-RPC Response
----------------

and we can see the response, too:

.. class:: tiny

::

    HTTP/1.0 200 OK
    Server: BaseHTTP/0.3 Python/2.6.1
    Date: Sun, 13 Jan 2013 03:38:00 GMT
    Content-type: text/xml
    Content-length: 121

    <?xml version='1.0'?>
    <methodResponse>
     <params>
      <param>
       <value><int>72</int></value>
      </param>
     </params>
    </methodResponse>


More XML-RPC
------------

Register an entire Python class as a service, exposing class methods::

    server.register_instance(MyClass())

Keep an instance method private    :

.. code-block:: python
    :class: tiny

    class MyServiceClass(object):
        ...
        def public_method(self, arg1, arg2):
            """this method is public"""
            pass
        
        def _private_method(self):
            """this method is private because it starts with '_'
            """
            pass


XML-RPC Introspection
---------------------

First, implement required methods on your service class:

.. code-block:: python
    :class: tiny

    from SimpleXMLRPCServer import list_public_methods
    
    class MyServiceClass(object):
        ...
        def _listMethods(self):
            """custom logic for presenting method names to users
            
            list_public_methods is a convenience function from the Python 
            library, but you can make your own logic if you wish.
            """
            return list_public_methods(self)
        
        def _methodHelp(self, method):
            """provide help text for an individual method
            """
            f = getattr(self, method)
            return f.__doc__


XML-RPC Introspection
---------------------

Then enable introspection via the server instance:

.. code-block:: python
    :class: small

    server.register_introspection_functions()

After this, a client proxy can call pre-defined methods to learn about what
your service offers:

.. code-block:: python
    :class: small

    >>> for name in proxy.system.listMethods():
    ...     help = proxy.system.methodHelp(name)
    ...     print name
    ...     print "\t%s" % help
    ... 
    public_method
        this method is public


Introspection Question
----------------------

I told you when we added the ``_private_method`` that any method that any
method whose name starts with ``_`` would be **private**.

.. class:: incremental

But we also added a ``_listMethods`` method and a ``_methodHelp`` method and
*those* methods are listed when you run ``proxy.system.listMethods()``

.. class:: incremental

Why is this?

.. class:: incremental

For a complete discussion of this, read `this MOTW post
<http://pymotw.com/2/SimpleXMLRPCServer/index.html#introspection-api>`_


SOAP
----

Example of Using SOAP via the ``suds`` package


Install Suds
------------

* Quit your python interpreter if you have it running.
* If you see (soupenv) at your command line prompt, cool.
* If you do not, type ``source /path/to/soupenv/bin/activate``
* Windows folks: ``> \path\to\soupenv\Scripts\activate``
* Once activated: ``pip install suds``


Creating a Suds Client
----------------------

Suds allows us to create a SOAP client object. SOAP uses WSDL to define a
service. All we need to do to set this up in python is load the URL of the
WSDL for the service we want to use:

.. code-block:: python
    :class: small

    (soupenv)$ python
    >>> from suds.client import Client
    >>> geo_client = Client('https://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderService_V03_01.asmx?wsdl')
    >>> geo_client
    <suds.client.Client object at 0x10041fc10>


Peeking at the Service
----------------------

Suds allows us to visually scan the service. Simply print the client object to
see what the service has to offer:

.. code-block:: python
    :class: small

    >>> print geo_client

    Suds ( https://fedorahosted.org/suds/ )  version: 0.4 GA  build: R699-20100913

    Service ( GeocoderService_V03_01 ) tns="https://geoservices.tamu.edu/"
       Prefixes (1)
          ns0 = "https://geoservices.tamu.edu/"
       Ports (2):
          (GeocoderService_V03_01Soap)
          Methods (4):
             ...
          Types (12):
             ...


Debugging Suds
--------------

Suds uses python logging to deal with debug information, so if you want to see
what's going on under the hood, you configure it via the Python logging
module:

.. code-block:: python

    >>> import logging
    >>> logging.basicConfig(level=logging.INFO)
    >>> logging.getLogger('suds.client').setLevel(logging.DEBUG)

.. class:: incremental

This will allow us to see the messages sent and received by our client.


Client Options
--------------

SOAP Servers can provide more than one *service* and each *service* might have
more than one *port*. Suds provides two ways to configure which *service* and
*port* you wish to use.  

Via subscription:

.. code-block:: python

    client.service['<service>']['<port>'].method(args)

Or the way we will do it, via configuration:

.. code-block:: python

    geo_client.set_options(service='GeocoderService_V03_01',
                           port='GeocoderService_V03_01Soap')


Providing Arguments
-------------------

Arguments to a method are set up as a dictionary.  Although some may not be 
required according to api documentation, it is safest to provide them all:

.. code-block:: python
    :class: small

    apiKey = '<fill this in>'
    args = {'apiKey': apiKey, }
    args['streetAddress'] = '1325 4th Avenue'
    args['city'] = 'Seattle'
    args['state'] = 'WA'
    args['zip'] = '98101'
    args['version'] = 3.01
    args['shouldReturnReferenceGeometry'] = True
    args['shouldNotStoreTransactionDetails'] = True
    args['shouldCalculateCensus'] = False
    args['censusYear'] = "TwoThousandTen"


Making the Call
---------------

Finally, once we've got the arguments all ready we can go ahead and make a call
to the server:

.. code-block:: python
    :class: small

    >>> res = geo_client.service.GeocodeAddressNonParsed(**args)
    DEBUG:suds.client:sending to 
    (https://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderService_V03_01.asmx)
    message:
    ...


What does it look like?
-----------------------

.. class:: tiny

::

    <?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:ns0="https://geoservices.tamu.edu/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
       <SOAP-ENV:Header/>
       <ns1:Body>
          <ns0:GeocodeAddressNonParsed>
             <ns0:streetAddress>1325 4th Avenue</ns0:streetAddress>
             <ns0:city>Seattle</ns0:city>
             <ns0:state>WA</ns0:state>
             <ns0:zip>98101</ns0:zip>
             <ns0:apiKey>a450a9181f85498598e21f8a39440e9a</ns0:apiKey>
             <ns0:version>3.01</ns0:version>
             <ns0:shouldCalculateCensus>false</ns0:shouldCalculateCensus>
             <ns0:censusYear>TwoThousandTen</ns0:censusYear>
             <ns0:shouldReturnReferenceGeometry>true</ns0:shouldReturnReferenceGeometry>
             <ns0:shouldNotStoreTransactionDetails>true</ns0:shouldNotStoreTransactionDetails>
          </ns0:GeocodeAddressNonParsed>
       </ns1:Body>
    </SOAP-ENV:Envelope>


And the Reply?
--------------

.. class:: tiny

::

    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
      <soap:Body>
        <GeocodeAddressNonParsedResponse xmlns="https://geoservices.tamu.edu/">
          <GeocodeAddressNonParsedResult>
            <TransactionId>6ef9c110-994c-4142-93d5-a55173526b64</TransactionId>
            <Latitude>47.6084110119244</Latitude>
            <Longitude>-122.3351592971042</Longitude>
            <Version>3.01</Version>
            <Quality>QUALITY_ADDRESS_RANGE_INTERPOLATION</Quality>
            <MatchedLocationType>LOCATION_TYPE_STREET_ADDRESS</MatchedLocationType>
            <MatchType>Exact</MatchType>
            <FeatureMatchingResultCount>1</FeatureMatchingResultCount>
            ...
            <FArea>2910.69420560356</FArea>
            <FAreaType>Meters</FAreaType>
            <FGeometrySRID>4269</FGeometrySRID>
            <FGeometry>&lt;?xml version="1.0" encoding="utf-8"?&gt;&lt;LineString xmlns="http://www.opengis.net/gml"&gt;&lt;posList&gt;-122.334868 47.608226 -122.335777 47.609219&lt;/posList&gt;&lt;/LineString&gt;</FGeometry>
            ...
          </GeocodeAddressNonParsedResult>
        </GeocodeAddressNonParsedResponse>
      </soap:Body>
    </soap:Envelope>


And What of Our Result?
-----------------------

The WSDL we started with should provide type definitions for both data we send
and results we receive. The ``res`` symbol we bound to our result earlier
should now be an instance of a *GeocodeAddressNonParsedResult*. Lets see what
that looks like:

.. code-block:: python

    >>> type(res)
    <type 'instance'>
    >>> dir(res)
    ['CensusTimeTaken', 'CensusYear', 'ErrorMessage', 'FArea',
     'FAreaType', 'FCity', 'FCounty', 'FCountySubRegion', 
     ...]
    >>> res.Latitude, res.Longitude
    (47.608411011924403, -122.3351592971042)


A Word on Debugging
-------------------

.. class:: center

**blerg**

.. class:: incremental

* Messages sent to the server are long XML strings
* Error messages are generally based on parsing errors in XML
* These error messages can be quite cryptic:
* "There is an error in XML document (1, 572). ---> The string '' is not a
  valid Boolean value.'

.. class:: incremental

Try this:

.. code-block:: python
    :class: small incremental

    >>> geo_client.last_sent().str().replace(" ","")[:573]
    '...</ns0:version>\n<ns0:shouldCalculateCensus/>'

