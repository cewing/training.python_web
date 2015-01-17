import socket
import sys


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print >>log_buffer, "making a server on {0}:{1}".format(*address)
    sock.bind(address)
    sock.listen(1)

    try:
        while True:
            print >>log_buffer, 'waiting for a connection'
            conn, addr = sock.accept() # blocking
            try:
                print >>log_buffer, 'connection - {0}:{1}'.format(*addr)
                while True:
                    data = conn.recv(16)
                    print >>log_buffer, 'received "{0}"'.format(data)
                    if data:
                        msg = 'sending data back to client'
                        print >>log_buffer, msg
                        conn.sendall(data)
                    else:
                        msg = 'no more data from {0}:{1}'.format(*addr)
                        print >>log_buffer, msg
                        break
            finally:
                conn.close()

    except KeyboardInterrupt:
        sock.close()
        return


if __name__ == '__main__':
    server()
    sys.exit(0)
