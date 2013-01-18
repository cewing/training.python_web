#!/usr/bin/env python

import socket 

import httpdate


host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

print "point your browser to http://localhost:%i"%port

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

html = open("tiny_html.html").read()

def OK_response(entity):
    """
    returns an HTTP response: header and entity in a string
    """
    resp = []
    resp.append('HTTP/1.1 200 OK')
    resp.append(httpdate.httpdate_now())
    resp.append('Content-Type: text/html')
    resp.append('Content-Length: %i'%len(entity))
    resp.append('')
    resp.append(entity)

    return "\r\n".join(resp)

def parse_request(request):
    """
    parse an HTTP request 
    
    returns the URI asked for
    
    note: minimal parsing -- only supprt GET
    
    example:
    GET / HTTP/1.1
    Host: localhost:50000
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:12.0) Gecko/20100101 Firefox/12.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Cache-Control: max-age=0
    """
    # first line should be the method line:
    lines = request.split("\r\n")
    print lines
    
    method, URI, protocol = lines[0].split()
    print method
    print URI
    print protocol
    # a bit of checking:
    if method.strip() != "GET":
        raise ValueError("I can only process a GET request") 
    if protocol.split('/')[0] != "HTTP":
        raise ValueError("I can only process an HTTP request") 

    return URI

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    request = client.recv(size)
    if request: # if the connection was closed there would be no data
        print "received:", request
        URI = parse_request(request)
        print "URI requested is:", URI
        response = OK_response(html)
        print "sending:"
        print response[:120]
        client.send(response) 
        client.close()

