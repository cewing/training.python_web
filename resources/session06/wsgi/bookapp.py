import re

from bookdb import BookDB

DB = BookDB()


def book(book_id):
    return "<h1>a book with id %s</h1>" % book_id


def books():
    return "<h1>a list of books</h1>"


def application(environ, start_response):
    status = "200 OK"
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return ["<h1>No Progress Yet</h1>".encode('utf8')]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
