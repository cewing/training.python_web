from cStringIO import StringIO
from echo_client import client
import socket
import unittest


def make_buffers(string, buffsize=16):
    for start in range(0, len(string), buffsize):
        yield string[start:start+buffsize]


class EchoTestCase(unittest.TestCase):
    """tests for the echo server and client"""
    connection_msg = 'connecting to localhost port 10000'
    sending_msg = 'sending "{0}"'
    received_msg = 'received "{0}"'
    closing_msg = 'closing socket'

    def setUp(self):
        """set up our tests"""
        if not hasattr(self, 'buff'):
            # ensure we have a buffer for the client to write to
            self.log = StringIO()
        else:
            # ensure that the buffer is set to the start for the next test
            self.log.seek(0)

    def tearDown(self):
        """clean up after ourselves"""
        if hasattr(self, 'buff'):
            # clear our buffer for the next test
            self.log.seek(0)
            self.log.truncate()

    def send_message(self, message):
        """Attempt to send a message using the client and the test buffer

        In case of a socket error, fail and report the problem
        """
        try:
            client(message, self.log)
        except socket.error, e:
            if e.errno == 61:
                msg = "Error: {0}, is the server running?"
                self.fail(msg.format(e.strerror))
            else:
                self.fail("Unexpected Error: {0}".format(str(e)))

    def process_log(self):
        """process the buffer used by the client for logging

        The first and last lines of output will be checked to ensure that the
        client started and terminated in the expected way

        The 'sending' message will be separated from the echoed message
        returned from the server.

        Finally, the sending message, and the list of returned buffer lines
        will be returned
        """
        if self.log.tell() == 0:
            self.fail("No bytes written to buffer")

        self.log.seek(0)
        client_output = self.log.read()
        lines = client_output.strip().split('\n')
        first_line = lines.pop(0)
        self.assertEqual(first_line, self.connection_msg,
                         "Unexpected connection message")
        send_msg = lines.pop(0)
        last_line = lines.pop()
        self.assertEqual(last_line, self.closing_msg,
                         "Unexpected closing message")
        return send_msg, lines

    def test_short_message_echo(self):
        """test that a message short than 16 bytes echoes cleanly"""
        short_message = "short message"
        self.send_message(short_message)
        actual_sent, actual_reply = self.process_log()
        expected_sent = self.sending_msg.format(short_message)
        self.assertEqual(
            expected_sent,
            actual_sent,
            "expected {0}, got {1}".format(expected_sent, actual_sent)
        )

        self.assertEqual(len(actual_reply), 1,
                         "Short message was split unexpectedly")

        actual_line = actual_reply[0]
        expected_line = self.received_msg.format(short_message)
        self.assertEqual(
            expected_line,
            actual_line,
            "expected {0} got {1}".format(expected_line, actual_line))

    def test_long_message_echo(self):
        """test that a message longer than 16 bytes echoes in 16-byte chunks"""
        long_message = "Four score and seven years ago our fathers did stuff"
        self.send_message(long_message)
        actual_sent, actual_reply = self.process_log()

        expected_sent = self.sending_msg.format(long_message)
        self.assertEqual(
            expected_sent,
            actual_sent,
            "expected {0}, got {1}".format(expected_sent, actual_sent)
        )

        expected_buffers = make_buffers(long_message, 16)
        for line_num, buff in enumerate(expected_buffers):
            expected_line = self.received_msg.format(buff)
            actual_line = actual_reply[line_num]
            self.assertEqual(
                expected_line,
                actual_line,
                "expected {0}, got {1}".format(expected_line, actual_line)
            )


if __name__ == '__main__':
    unittest.main()
