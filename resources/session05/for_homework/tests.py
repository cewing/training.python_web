import mimetypes
import os
import pathlib
import socket
import unittest


CRLF = '\r\n'
CRLF_BYTES = CRLF.encode('utf8')
KNOWN_TYPES = set(
    map(lambda x: x.encode('utf8'), mimetypes.types_map.values())
)


def extract_response_code(response):
    return response.split(CRLF_BYTES, 1)[0].split(b' ', 1)[1].strip()


def extract_response_protocol(response):
    return response.split(CRLF_BYTES, 1)[0].split(b' ', 1)[0].strip()


def extract_headers(response):
    return response.split(CRLF_BYTES*2, 1)[0].split(CRLF_BYTES)[1:]


def extract_body(response):
    return response.split(CRLF_BYTES*2, 1)[1]


class ResponseOkTestCase(unittest.TestCase):
    """unit tests for the response_ok method in our server

    Becase this is a unit test case, it does not require the server to be
    running.
    """

    def call_function_under_test(self, body=b"", mimetype=b"text/plain"):
        """call the `response_ok` function from our http_server module"""
        from http_server import response_ok
        return response_ok(body=body, mimetype=mimetype)

    def test_response_code(self):
        ok = self.call_function_under_test()
        expected = "200 OK"
        actual = extract_response_code(ok)
        self.assertEqual(expected.encode('utf8'), actual)

    def test_response_protocol(self):
        ok = self.call_function_under_test()
        expected = 'HTTP/1.1'
        actual = extract_response_protocol(ok)
        self.assertEqual(expected.encode('utf8'), actual)

    def test_response_has_content_type_header(self):
        ok = self.call_function_under_test()
        headers = extract_headers(ok)
        expected_name = 'content-type'.encode('utf8')
        has_header = False
        for header in headers:
            name, value = header.split(b':')
            actual_name = name.strip().lower()
            if actual_name == expected_name:
                has_header = True
                break
        self.assertTrue(has_header)

    def test_response_has_legitimate_content_type(self):
        ok = self.call_function_under_test()
        headers = extract_headers(ok)
        expected_name = 'content-type'.encode('utf8')
        for header in headers:
            name, value = header.split(b':')
            actual_name = name.strip().lower()
            if actual_name == expected_name:
                self.assertTrue(value.strip() in KNOWN_TYPES)
                return
        self.fail('no content type header found')

    def test_passed_mimetype_in_response(self):
        mimetypes = [
            b'image/jpeg', b'text/html', b'text/x-python',
        ]
        header_name = b'content-type'
        for expected in mimetypes:
            ok = self.call_function_under_test(mimetype=expected)
            headers = extract_headers(ok)
            for header in headers:
                name, value = header.split(b':')
                if header_name == name.strip().lower():
                    actual = value.strip()
                    self.assertEqual(
                        expected,
                        actual,
                        "expected {0}, got {1}".format(expected, actual)
                    )

    def test_passed_body_in_response(self):
        bodies = [
            b"a body",
            b"a longer body\nwith two lines",
            pathlib.Path("webroot/sample.txt").read_bytes(),
        ]
        for expected in bodies:
            ok = self.call_function_under_test(body=expected)
            actual = extract_body(ok)
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
        actual = extract_response_code(resp)
        self.assertEqual(expected.encode('utf8'), actual)

    def test_response_method(self):
        resp = self.call_function_under_test()
        expected = 'HTTP/1.1'
        actual = extract_response_protocol(resp)
        self.assertEqual(expected.encode('utf8'), actual)


class ResponseNotFoundTestCase(unittest.TestCase):
    """unit tests for the response_not_found function"""

    def call_function_under_test(self):
        """call the 'response_not_found' function"""
        from http_server import response_not_found
        return response_not_found()

    def test_response_code(self):
        resp = self.call_function_under_test()
        expected = "404 Not Found"
        actual = extract_response_code(resp)
        self.assertEqual(expected.encode('utf8'), actual)

    def test_response_method(self):
        resp = self.call_function_under_test()
        expected = 'HTTP/1.1'
        actual = extract_response_protocol(resp)
        self.assertEqual(expected.encode('utf8'), actual)


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
        except (NotImplementedError, Exception) as e:
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
        content, mime_type = resolve_uri(uri)
        return content, mime_type.decode('utf8')

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
        actual_body = actual_body.decode('utf8')
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
            path = pathlib.Path("webroot{0}".format(uri))
            expected_body = path.read_bytes()
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
            path = pathlib.Path("webroot{0}".format(uri))
            expected_body = path.read_bytes()
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
        self.assertRaises(NameError, self.call_function_under_test, uri)


class HTTPServerFunctionalTestCase(unittest.TestCase):
    """functional tests of the HTTP Server

    This test case interacts with the http server, and as such requires it to
    be running in order for the tests to pass
    """

    def send_message(self, message, use_bytes=False):
        """Attempt to send a message using the client and the test buffer

        In case of a socket error, fail and report the problem
        """
        response = ''            
        if not use_bytes:
            from simple_client import client
        else:
            from simple_client import bytes_client as client

        try:
            response = client(message)
        except socket.error as e:
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
        root = pathlib.Path("webroot")
        for file_path in root.iterdir():
            # set up expectations for this file
            if file_path.is_dir():
                continue
            expected_body = file_path.read_bytes().decode('utf8')
            expected_mimetype = mimetypes.types_map[
                os.path.splitext(str(file_path))[1]
            ]
            file_uri = str(file_path)[len(str(root)):]
            message = message_tmpl.format(file_uri)
            actual = self.send_message(message)
            self.assertTrue(
                "200 OK" in actual,
                "request for {0} did not result in OK".format(
                    file_uri
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

    def test_webroot_image_uris(self):
        """verify that image uris are properly served

        requires using a client that does not attempt to decode the response
        body
        """
        message_tmpl = CRLF.join(['GET {0} HTTP/1.1', 'Host: example.com', ''])
        root = pathlib.Path("webroot")
        images_path = root / 'images'
        for file_path in images_path.iterdir():
            # set up expectations for this file
            if file_path.is_dir():
                continue
            expected_body = file_path.read_bytes()
            expected_mimetype = mimetypes.types_map[
                os.path.splitext(str(file_path))[1]
            ]
            file_uri = str(file_path)[len(str(root)):]
            message = message_tmpl.format(file_uri)
            actual = self.send_message(message, use_bytes=True)
            self.assertTrue(
                b"200 OK" in actual,
                "request for {0} did not result in OK".format(
                    file_uri
                )
            )
            self.assertTrue(
                expected_mimetype.encode('utf8') in actual,
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
