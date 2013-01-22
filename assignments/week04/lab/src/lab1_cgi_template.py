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
<title>Lab A - CGI experiments</title>
</head>
<body>

The server IP address is %s:%s.<br>
<br>
The server name is %s. (if an IP address, then a DNS problem) <br>
<br>
You are coming from  %s:%s.<br>
<br>
Your hostname is %s.  <br>
<br>
The currenly executing script is %s<br>
<br>
The request arrived at %s<br>


</body>
</html>""" % (
        os.environ['SERVER_ADDR'], # server IP
        'bbbb', # server port
        'cccc', # client IP
        'dddd', # client port
        'eeee', # client hostname
        'ffff', # server hostname
        'gggg', # this script name
        'hhhh', # time
        )

print body,
