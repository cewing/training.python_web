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

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    request = client.recv(size)
    if request: # if the connection was closed there would be no data
        print "received:"
        print request
        response = OK_response(html)
        print "sending:"
        print response[:120]
        client.send(response) 
        client.close()

