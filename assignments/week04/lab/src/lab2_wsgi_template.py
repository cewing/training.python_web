#!/usr/bin/python
import datetime

body = """<html>
<head>
<title>Lab 2 - WSGI experiments</title>
</head>
<body>

The server name is %s. (if an IP address, then a DNS problem) <br>
<br>
The server address is %s:%s.<br>
<br>
You are coming from  %s:%s.<br>
<br>
The URI we are serving is %s.<br>
<br>
The request arrived at %s<br>

</body>
</html>"""

def application(environ, start_response):
    response_body = body % (
         environ.get('SERVER_NAME', 'Unset'), # server name
         'aaaa', # server IP
         'bbbb', # server port
         'cccc', # client IP
         'dddd', # client port
         'eeee', # this script name
         'ffff', # time
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
