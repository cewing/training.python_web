import mimetypes
import socket
import unittest


CRLF = '\r\n'
KNOWN_TYPES = set(mimetypes.types_map.values())


class ResponseOkTestCase(unittest.TestCase):
    """unit tests for the response_ok method in our server

    Becase this is a unit test case, it does not require the server to be
    running.
    """

    def call_function_under_test(self):
        """call the `response_ok` function from our http_server module"""
        from http_server import response_ok
        return response_ok()

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


class ParseRequestTestCase(unittest.TestCase):
    """unit tests for the parse_request method"""

    def call_function_under_test(self, request):
        """call the `parse_request` function"""
        from http_server import parse_request
        return parse_request(request)

    def test_get_method(self):
        request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
        try:
            self.call_function_under_test(request)
        except (NotImplementedError, Exception), e:
            self.fail('GET method raises an error {0}'.format(str(e)))

    def test_bad_http_methods(self):
        methods = ['POST', 'PUT', 'DELETE', 'HEAD']
        request_template = "{0} / HTTP/1.1\r\nHost: example.com\r\n\r\n"
        for method in methods:
            request = request_template.format(method)
            self.assertRaises(
                NotImplementedError, self.call_function_under_test, request
            )

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


if __name__ == '__main__':
    unittest.main()
