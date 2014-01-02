import mimetypes
import os
import socket
import unittest


CRLF = '\r\n'
KNOWN_TYPES = set(mimetypes.types_map.values())


class ResponseOkTestCase(unittest.TestCase):
    """unit tests for the response_ok method in our server

    Becase this is a unit test case, it does not require the server to be
    running.
    """

    def call_function_under_test(self, body="", mimetype="text/plain"):
        """call the `response_ok` function from our http_server module"""
        from http_server import response_ok
        return response_ok(body=body, mimetype=mimetype)

    def test_response_code(self):
        ok = self.call_function_under_test()
        expected = "200 OK"
        actual = ok.split(CRLF)[0].split(' ', 1)[1].strip()
        self.assertEqual(expected, actual)

    def test_response_method(self):
        ok = self.call_function_under_test()
        expected = 'HTTP/1.1'
        actual = ok.split(CRLF)[0].split(' ', 1)[0].strip()
        self.assertEqual(expected, actual)

    def test_response_has_content_type_header(self):
        ok = self.call_function_under_test()
        headers = ok.split(CRLF+CRLF, 1)[0].split(CRLF)[1:]
        expected_name = 'content-type'
        has_header = False
        for header in headers:
            name, value = header.split(':')
            actual_name = name.strip().lower()
            if actual_name == expected_name:
                has_header = True
                break
        self.assertTrue(has_header)

    def test_response_has_legitimate_content_type(self):
        ok = self.call_function_under_test()
        headers = ok.split(CRLF+CRLF, 1)[0].split(CRLF)[1:]
        expected_name = 'content-type'
        for header in headers:
            name, value = header.split(':')
            actual_name = name.strip().lower()
            if actual_name == expected_name:
                self.assertTrue(value.strip() in KNOWN_TYPES)
                return
        self.fail('no content type header found')

    def test_passed_mimetype_in_response(self):
        mimetypes = [
            'image/jpeg', 'text/html', 'text/x-python',
        ]
        header_name = 'content-type'
        for expected in mimetypes:
            ok = self.call_function_under_test(mimetype=expected)
            headers = ok.split(CRLF+CRLF, 1)[0].split(CRLF)[1:]
            for header in headers:
                name, value = header.split(':')
                if header_name == name.strip().lower():
                    actual = value.strip()
                    self.assertEqual(
                        expected,
                        actual,
                        "expected {0}, got {1}".format(expected, actual)
                    )

    def test_passed_body_in_response(self):
        bodies = [
            "a body", 
            "a longer body\nwith two lines",
            open("webroot/sample.txt", 'r').read(),
        ]
        for expected in bodies:
            ok = self.call_function_under_test(body=expected)
            actual = ok.split(CRLF+CRLF, 1)[1]
            self.assertEqual(
                expected,
                actual,
                "expected {0}, got {1}".format(expected, actual))


class ResponseMethodNotAllowedTestCase(unittest.TestCase):
    """unit tests for the response_method_not_allowed function"""

    def call_function_under_test(self):
        """call the `response_method_not_allowed` function"""
        from http_server import response_method_not_allowed
        return response_method_not_allowed()

    def test_response_code(self):
        resp = self.call_function_under_test()
        expected = "405 Method Not Allowed"
        actual = resp.split(CRLF)[0].split(' ', 1)[1].strip()
        self.assertEqual(expected, actual)

    def test_response_method(self):
        resp = self.call_function_under_test()
        expected = 'HTTP/1.1'
        actual = resp.split(CRLF)[0].split(' ', 1)[0].strip()
        self.assertEqual(expected, actual)


class ResponseNotFoundTestCase(unittest.TestCase):
    """unit tests for the response_not_found function"""

    def call_function_under_test(self):
        """call the 'response_not_found' function"""
        from http_server import response_not_found
        return response_not_found()

    def test_response_code(self):
        resp = self.call_function_under_test()
        expected = "404 Not Found"
        actual = resp.split(CRLF)[0].split(' ', 1)[1].strip()
        self.assertEqual(expected, actual)

    def test_response_method(self):
        resp = self.call_function_under_test()
        expected = 'HTTP/1.1'
        actual = resp.split(CRLF)[0].split(' ', 1)[0].strip()
        self.assertEqual(expected, actual)


class ParseRequestTestCase(unittest.TestCase):
    """unit tests for the parse_request method"""

    def call_function_under_test(self, request):
        """call the `parse_request` function"""
        from http_server import parse_request
        return parse_request(request)

    def test_get_method(self):
        """verify that GET HTTP requests do not raise an error"""
        request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
        try:
            self.call_function_under_test(request)
        except (NotImplementedError, Exception), e:
            self.fail('GET method raises an error {0}'.format(str(e)))

    def test_bad_http_methods(self):
        """verify that non-GET HTTP methods raise a NotImplementedError"""
        methods = ['POST', 'PUT', 'DELETE', 'HEAD']
        request_template = "{0} / HTTP/1.1\r\nHost: example.com\r\n\r\n"
        for method in methods:
            request = request_template.format(method)
            self.assertRaises(
                NotImplementedError, self.call_function_under_test, request
            )

    def test_uri_returned(self):
        """verify that the parse_request function returns a URI"""
        URIs = [
            '/', '/a_web_page.html', '/sample.txt', '/images/sample_1.png',
        ]
        request_tmplt = "GET {0} HTTP/1.1"
        for expected in URIs:
            request = request_tmplt.format(expected)
            actual = self.call_function_under_test(request)
            self.assertEqual(
                expected,
                actual,
                "expected {0}, got {1}".format(expected, actual)
            )


class ResolveURITestCase(unittest.TestCase):
    """unit tests for the resolve_uri function"""

    def call_function_under_test(self, uri):
        """call the resolve_uri function"""
        from http_server import resolve_uri
        return resolve_uri(uri)

    def test_directory_resource(self):
        uri = '/'
        expected_names = [
            'a_web_page.html', 'images', 'make_time.py', 'sample.txt',
        ]
        expected_mimetype = "text/plain"
        actual_body, actual_mimetype = self.call_function_under_test(uri)
        self.assertEqual(
            expected_mimetype,
            actual_mimetype,
            'expected {0} got {1}'.format(expected_mimetype, actual_mimetype)
        )
        for expected in expected_names:
            self.assertTrue(
                expected in actual_body,
                '"{0}" not in "{1}"'.format(expected, actual_body)
            )

    def test_file_resource(self):
        uris_types = {
            '/a_web_page.html': 'text/html',
            '/make_time.py': 'text/x-python',
            '/sample.txt': 'text/plain',
        }
        for uri, expected_mimetype in uris_types.items():
            path = "webroot{0}".format(uri)
            expected_body = open(path, 'rb').read()
            actual_body, actual_mimetype = self.call_function_under_test(uri)
            self.assertEqual(
                expected_mimetype,
                actual_mimetype,
                'expected {0} got {1}'.format(
                    expected_mimetype, actual_mimetype
                )
            )
            self.assertEqual(
                expected_body,
                actual_body,
                'expected {0} got {1}'.format(
                    expected_mimetype, actual_mimetype
                )
            )

    def test_image_resource(self):
        names_types = {
            'JPEG_example.jpg': 'image/jpeg',
            'sample_1.png': 'image/png',
        }
        for filename, expected_mimetype in names_types.items():
            uri = "/images/{0}".format(filename)
            path = "webroot{0}".format(uri)
            expected_body = open(path, 'rb').read()
            actual_body, actual_mimetype = self.call_function_under_test(uri)
            self.assertEqual(
                expected_mimetype,
                actual_mimetype,
                'expected {0} got {1}'.format(
                    expected_mimetype, actual_mimetype
                )
            )
            self.assertEqual(
                expected_body,
                actual_body,
                'expected {0} got {1}'.format(
                    expected_mimetype, actual_mimetype
                )
            )

    def test_missing_resource(self):
        uri = "/missing.html"
        self.assertRaises(ValueError, self.call_function_under_test, uri)


class HTTPServerFunctionalTestCase(unittest.TestCase):
    """functional tests of the HTTP Server

    This test case interacts with the http server, and as such requires it to
    be running in order for the tests to pass
    """

    def send_message(self, message):
        """Attempt to send a message using the client and the test buffer

        In case of a socket error, fail and report the problem
        """
        from simple_client import client
        response = ''
        try:
            response = client(message)
        except socket.error, e:
            if e.errno == 61:
                msg = "Error: {0}, is the server running?"
                self.fail(msg.format(e.strerror))
            else:
                self.fail("Unexpected Error: {0}".format(str(e)))
        return response

    def test_get_request(self):
        message = CRLF.join(['GET / HTTP/1.1', 'Host: example.com', ''])
        expected = '200 OK'
        actual = self.send_message(message)
        self.assertTrue(
            expected in actual, '"{0}" not in "{1}"'.format(expected, actual)
        )

    def test_post_request(self):
        message = CRLF.join(['POST / HTTP/1.1', 'Host: example.com', ''])
        expected = '405 Method Not Allowed'
        actual = self.send_message(message)
        self.assertTrue(
            expected in actual, '"{0}" not in "{1}"'.format(expected, actual)
        )

    def test_webroot_directory_resources(self):
        """verify that directory uris are properly served"""
        message_tmpl = CRLF.join(['GET {0} HTTP/1.1', 'Host: example.com', ''])
        root = "webroot"
        for directory, directories, files in os.walk(root):
            directory_uri = "/{0}".format(directory[len(root):])
            message = message_tmpl.format(directory_uri)
            actual = self.send_message(message)
            # verify that directory listings are correct
            self.assertTrue(
                "200 OK" in actual,
                "request for {0} did not result in OK".format(directory_uri))
            for expected in directories + files:
                self.assertTrue(
                    expected in actual,
                    '"{0}" not in "{1}"'.format(expected, actual)
                )

    def test_webroot_file_uris(self):
        """verify that file uris are properly served"""
        message_tmpl = CRLF.join(['GET {0} HTTP/1.1', 'Host: example.com', ''])
        root = "webroot"
        for directory, directories, files in os.walk(root):
            directory_uri = "/{0}".format(directory[len(root):])
            # verify that all files are delivered correctly
            for filename in files:
                # file as local resource and as web URI
                file_path = os.path.sep.join([directory, filename])
                if directory_uri != '/':
                    file_uri = '/'.join([directory_uri, filename])
                else:
                    file_uri = '/{0}'.format(filename)
                # set up expectations for this file
                expected_body = open(file_path, 'rb').read()
                expected_mimetype = mimetypes.types_map[
                    os.path.splitext(filename)[1]
                ]
                # make a request for this file as a uri
                message = message_tmpl.format(file_uri)
                actual = self.send_message(message)
                # verify that request is OK
                self.assertTrue(
                    "200 OK" in actual,
                    "request for {0} did not result in OK".format(
                        directory_uri
                    )
                )
                self.assertTrue(
                    expected_mimetype in actual,
                    "mimetype {0} not in response for {1}".format(
                        expected_mimetype, file_uri
                    )
                )
                self.assertTrue(
                    expected_body in actual,
                    "body of {0} not in response for {1}".format(
                        file_path, file_uri
                    )
                )

    def test_missing_resource(self):
        message = CRLF.join(
            ['GET /missing.html HTTP/1.1', 'Host: example.com', '']
        )
        expected = '404 Not Found'
        actual = self.send_message(message)
        self.assertTrue(
            expected in actual, '"{0}" not in "{1}"'.format(expected, actual)
        )


if __name__ == '__main__':
    unittest.main()
