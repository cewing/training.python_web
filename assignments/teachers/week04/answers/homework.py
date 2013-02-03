#!/usr/bin/python
import re


class MyApplication(object):
    page_template = """
<!DOCTYPE html>
<html>
    <head><title>%(page_title)s</title></head>
    <body>
        %(page_body)s
    </body>
</html>
"""
    
    def __init__(self, db, urls):
        self.db = db
        self.urls = urls

    def __call__(self, environ, start_response):
        headers = [('Content-type', 'text/html')]
        import pdb; pdb.set_trace( )
        try:
            path = environ.get('PATH_INFO', None)
            if path is None:
                raise NameError
            func, args = self._get_callable(path.lstrip('/'))
            body = func(*args)
            status = "200 OK"
            headers.append(('Content-length', str(len(body))))
        except NameError:
            status = "404 Not Found"
            body = self.page_template % {'page_title': 'Not Found',
                                         'page_body': '404 Not Found'}
        except ValueError:
            status = "501 Not Implemented"
            body = 'That URI is not implemented'
        except:
            status = "500 Internal Server Error"
            body = 'There has been an error, try again later'
        finally:
            start_response(status, headers)
            return [body]

    def books(self):
        core = ['<h1>Book Database</h1>',
                '<ul>']
        tmpl = '<li><a href="book/%(id)s">%(title)s</a></li>'
        for data in self.db.titles():
            core.append(tmpl % data)
        core.append('</ul>')
        body = "\n".join(core)
        context = {'page_title': "Book Database",
                   'page_body': body}
        return self.page_template % context

    def book(self, id):
        tmpl = """
<h1>%(title)s</h1>
<dl>
  <dt>ISBN</dt>
  <dd>%(isbn)s</dd>
  <dt>Author(s)</dt>
  <dd>%(author)s</dd>
  <dt>Publisher</dt>
  <dd>%(publisher)s</dd>
</dl>
<p><a href="../">More Books</a></p>
"""
        try:
            book = self.db.title_info(id)
        except KeyError:
            raise NameError('book not found')
        title = "Book Database: %s" % book['isbn']
        context = {'page_title': title,
                   'page_body': tmpl % book}
        return self.page_template % context

    def _get_callable(self, path):
        for regexp, funcname in self.urls:
            match = re.match(regexp, path)
            # if there is no match for the path, it's a 404 error
            if match is None:
                continue
            # if the match names a method that does not exist, its a 501
            func = getattr(self, funcname, None)
            if func is None:
                raise ValueError
            # get all subgroup matches from the regexp as args
            args = match.groups([])
            return func, args
        raise NameError



URLS = [(r'^$', 'books'),
        (r'^book/(id[\d]{1,2})$', 'book'), ]


if __name__ == '__main__':
    # this block will be called when the script is run directly
    from wsgiref.simple_server import make_server
    import bookdb
    application = MyApplication(bookdb.BookDB(), URLS)
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
else:
    # this block will be called when the script is run on a VM via mod_wsgi
    # 
    # we need to place bookdb.py in some location on the server, and then 
    # add that location to the sys.path variable in order to allow mod_wsgi
    # to import bookdb
    # 
    # in addition, apache must be configured with the following:
    # WSGIScriptAlias /books /path/on/server/to/homework.py
    import sys
    sys.path.append('/path/to/directory/containing/bookdb/on/server')
    import bookdb
    application = MyApplication(bookdb.BookDB(), URLS)
