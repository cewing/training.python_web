#!/usr/bin/python
import cgi
import cgitb
import time
import json

cgitb.enable()

data = {'time' : time.time() 
       }

fs = cgi.FieldStorage()
a = fs['a']
b = fs['b']
a = int(a.value)
b = int(b.value)
result = a + b
data['result'] = result

print "Content-Type: application/json"
print
print json.dumps(data, indent=4)

