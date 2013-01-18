#!/usr/bin/env python

import socket 
import os

import httpdate

import subprocess

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

root_dir = 'web' # must be run from code dir...

print "point your browser to http://localhost:%i/make_time.py"%port

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

html = open("tiny_html.html").read()

mime_types={}
mime_types['html'] =  "text/html"
mime_types['htm']  =  "text/html"
mime_types['txt']  =  "text/plain"
mime_types['png']  =  "image/png"
mime_types['jpeg'] =  "image/jpg"
mime_types['jpg']  =  "image/jpg"

def OK_response(entity, extension='html'):
    """
    returns an HTTP response: header and entity in a string
    """
    resp = []
    resp.append('HTTP/1.1 200 OK')
    resp.append(httpdate.httpdate_now())
    type = mime_types.get(extension, 'text/plain')
    resp.append( 'Content-Type: %s'%type )
    resp.append('Content-Length: %i'%len(entity))
    resp.append('')
    resp.append(entity)

    return "\r\n".join(resp)

def Error_response(URI, error_code=404):
    """
    returns an HTTP 404 Not Found Error response:
    
    URI is the name of the entity not found 
    """
    errors = {500: "Server Error",
              404: "Not Found",
              301: "Moved Permanently",
              302: "Moved Temporarily",
              303: "See Other"
              }
    
    resp = []
    resp.append('HTTP/1.1 %i %s'%(error_code, errors[error_code]))
    resp.append(httpdate.httpdate_now())
    resp.append('Content-Type: text/plain')
    
    msg = "%i Error:\n %s \n %s"%( error_code, URI, errors[error_code] )    

    resp.append('Content-Length: %i'%( len(msg) ) )
    resp.append('')
    resp.append(msg)

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
    
    method, URI, protocol = lines[0].split()

    # a bit of checking:
    if method.strip() != "GET":
        raise ValueError("I can only process a GET request") 
    if protocol.split('/')[0] != "HTTP":
        raise ValueError("I can only process an HTTP request") 

    return URI

def format_dir_list(URI):
    """
    format the contests of dir as HTML with links
    """
    dir = os.path.join(root_dir, URI)
    names = os.listdir(dir)

    dirs = [d for d in names if os.path.isdir(os.path.join(dir,d))]
    files = [d for d in names if os.path.isfile(os.path.join(dir,d))]

    html =[]
    html.append("<http> <body>")
    html.append("<h2>%s</h2>"%URI)
    print "URI:", URI
    if URI: # don't need the parent dir at the root
        html.append('<a href="..">Parent</a>' )
    html.append("<h3>Directories:</h3>")
    html.append("  <ul>")
    for d in dirs:
        html.append('    <li> <a href="%s">%s </a></li>'%(os.path.join(URI,d), d))
    html.append("  </ul>")
    html.append("<h3>Files:</h3>")
    html.append("  <ul>")
    for f in files:
        html.append('    <li> <a href="%s"> %s </a> </li>'%(os.path.join(URI,f), f) )
    html.append("  </ul>")
    html.append("</body> </http>")
    return "\n".join(html)

def get_time_page():
    """
    returns and html page with the current time in it
    """
    time = httpdate.httpdate_now()
    html = "<html>  <body>  <h1> %s </h1> </body> </html>"%time
    return html

def run_python_script(URI):
    """
    runs the python script in the URI
    
    returns std out from running the script
    
    raises a subprocess.CalledProcessError if something goes wrong
    """
    script = os.path.join(root_dir, URI)
    result = subprocess.check_output(["python", script])
    return result
    

def get_file(URI):
    """
    returns the contents of the file in the URI -- and a file extension for the mime type.
    """
    URI = URI.strip('/') #os.path.join does not like a leading slash
    # check if this is the time server option
    if URI.lower() == "get_time":
        return get_time_page(), 'html'
    # check if it's a python file
    if os.path.splitext(URI)[1] == ".py":
        return run_python_script(URI), 'html'            
    else:
        filename = os.path.join( root_dir, URI)
        if os.path.isfile(filename):
            contents = open(filename, 'rb').read()
            ext = os.path.splitext(filename)[1].strip('.')
            return contents, ext
        elif os.path.isdir(filename):
            return format_dir_list(URI), 'htm'
        else:
            raise ValueError("there is nothing by that name")
    

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    request = client.recv(size)
    if request: # if the connection was closed there would be no data
        print "received:", request
        URI = parse_request(request)
        try:
            file_data, ext = get_file(URI)
            response = OK_response(file_data, ext)
        except ValueError: # file not found
            response = Error_response(URI)
        except subprocess.CalledProcessError: # somethign wrong with the python script
            response = Error_response(URI, 500)
        client.send(response) 
        client.close()

