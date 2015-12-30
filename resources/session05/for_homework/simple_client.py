import socket
import sys


def bytes_client(msg):
    server_address = ('localhost', 10000)
    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
    )
    print(
        'connecting to {0} port {1}'.format(*server_address),
        file=sys.stderr
    )
    sock.connect(server_address)
    response = b''
    done = False
    bufsize = 1024
    try:
        print('sending "{0}"'.format(msg), file=sys.stderr)
        sock.sendall(msg.encode('utf8'))
        while not done:
            chunk = sock.recv(bufsize)
            if len(chunk) < bufsize:
                done = True
            response += chunk
        print('received "{0}"'.format(response), file=sys.stderr)
    finally:
        print('closing socket', file=sys.stderr)
        sock.close()
    return response


def client(msg):
    return bytes_client(msg).decode('utf8')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print(usg, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
