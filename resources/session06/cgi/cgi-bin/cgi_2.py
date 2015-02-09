#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import datetime


default = "No Value Present"


print "Content-Type: text/html"
print

body = """<html>
<head>
<title>Lab 1 - CGI experiments</title>
</head>
<body>
The server name or IP address is %s.<br>
<br>
The server is running on port %s.<br>
<br>
Your hostname is %s.  <br>
<br>
You are coming from  %s<br>
<br>
The currenly executing script is %s<br>
<br>
The request arrived at %s<br>

</body>
</html>""" % (
    os.environ.get('SERVER_NAME', default),  # Server Hostname or IP
    'aaaa',  # server port
    'bbbb',  # client hostname
    'cccc',  # client IP
    'dddd',  # this script name
    'eeee',  # time
)

print body,
