import socket
import sys


def client(msg):
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    try:
        # Send data
        print >>sys.stderr, 'sending "%s"' % msg
        sock.sendall(msg)
        # Look for the response
        amount_received = 0
        amount_expected = len(msg)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print >>sys.stderr, usg
        sys.exit(1)
    
    msg = sys.argv[1]
    client(msg)