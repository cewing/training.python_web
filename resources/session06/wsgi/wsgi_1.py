#!/usr/bin/python
import datetime

default = "No Value Set"

body = """<html>
<head>
<title>Lab 2 - WSGI experiments</title>
</head>
<body>

The server name or address is %s. <br>
<br>
The server is running on port %s.<br>
<br>
You are coming from %s.<br>
<br>
The URI we are serving is %s.<br>
<br>
The request arrived at %s<br>

</body>
</html>"""

def application(environ, start_response):
    import pprint
    pprint.pprint(environ)
    response_body = body % (
        environ.get('SERVER_NAME', default),  # server name
        'bbbb',  # server port
        'cccc',  # client IP
        'eeee',  # the URI path
        'ffff',  # time
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
