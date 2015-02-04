import socket
import sys


def client(msg):
    server_address = ('localhost', 10000)
    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
    )
    print >>sys.stderr, 'connecting to {0} port {1}'.format(*server_address)
    sock.connect(server_address)
    response = ''
    done = False
    bufsize = 1024
    try:
        print >>sys.stderr, 'sending "{0}"'.format(msg)
        sock.sendall(msg)
        while not done:
            chunk = sock.recv(bufsize)
            if len(chunk) < bufsize:
                done = True
            response += chunk
        print >>sys.stderr, 'received "{0}"'.format(response)
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
    return response


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print >>sys.stderr, usg
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
