#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import datetime


print "Content-Type: text/html"
print

body = """<html>
<head>
<title>Lab 1 - CGI experiments</title>
</head>
<body>
The server name is %s. (if an IP address, then a DNS problem) <br>
<br>
The server address is %s:%s.<br>
<br>
Your hostname is %s.  <br>
<br>
You are coming from  %s:%s.<br>
<br>
The currenly executing script is %s<br>
<br>
The request arrived at %s<br>

</body>
</html>""" % (
        os.environ['SERVER_NAME'], # Server Hostname
        'aaaa', # server IP
        'bbbb', # server port
        'cccc', # client hostname
        'dddd', # client IP
        'eeee', # client port
        'ffff', # this script name
        'gggg', # time
        )

print body,
