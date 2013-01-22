#!/usr/bin/python
import datetime

body = """<html>
<head>
<title>Lab A - CGI experiments</title>
</head>
<body>

The server address is %s.<br>
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
</html>"""

def application(environ, start_response):
    response_body = body % (
         environ['HTTP_HOST'], # server IP
         'bbbb', # client IP
         'cccc', # client port
         'dddd', # client hostname
         'eeee', # server hostname
         'ffff', # this script name
         'gggg', # time
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
