#!/usr/bin/python
import time
import datetime

now = time.time()

html = """<html>
<head></head>
    <body>
        <p>Here is the time: %s</p>
        <p>and again: %s</p>
        <p>and in ISO format: %s</p>
    </body>
</html>
""" % (now,
       datetime.datetime.fromtimestamp(now),
       datetime.datetime.fromtimestamp(now).isoformat())

print "Content-Type: text/html"
print "Content-length: %s" % len(html)
print
print html
