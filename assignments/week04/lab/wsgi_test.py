#!/usr/bin/python

# copied from: 
# http://webpython.codepoint.net/wsgi_application_interface
#
# This is our application object. It could have any name,
# except when using mod_wsgi where it must be "application"
def application(environ, start_response):

    # build the response body possibly using the environ dictionary
    response_body = 'The request method was %s' % environ['REQUEST_METHOD']

    # HTTP response code and message
    status = '200 OK'

    # These are HTTP headers expected by the client.
    # They must be wrapped as a list of tupled pairs:
    # [(Header name, Header value)].
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]

    # Send them to the server using the supplied function
    start_response(status, response_headers)

    # Return the response body.
    # Notice it is wrapped in a list although it could be any iterable.
    return [response_body]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()