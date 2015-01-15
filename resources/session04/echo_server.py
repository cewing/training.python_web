import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = None
    # TODO: Set an option to allow the socket address to be reused immediately
    #       see the end of http://docs.python.org/2/library/socket.html

    # log that we are building a server
    print >>log_buffer, "making a server on {0}:{1}".format(*address)

    # TODO: bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print >>log_buffer, 'waiting for a connection'

            # TODO: make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of
            #       the client so we can report it below.  Replace the
            #       following line with your code. It is only here to prevent
            #       syntax errors
            addr = ('bar', 'baz')
            try:
                print >>log_buffer, 'connection - {0}:{1}'.format(*addr)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    # TODO: receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  Replace the
                    #       following line with your code.  It's only here as
                    #       a placeholder to prevent an error in string
                    #       formatting
                    data = ''
                    print >>log_buffer, 'received "{0}"'.format(data)
                    # TODO: you will need to check here to see if any data was
                    #       received.  If so, send the data you got back to
                    #       the client.  If not, exit the inner loop and wait
                    #       for a new connection from a client

            finally:
                # TODO: When the inner loop exits, this 'finally' clause will
                #       be hit. Use that opportunity to close the socket you
                #       created above when a client connected.  Replace the
                #       call to `pass` below, which is only there to prevent
                #       syntax problems
                pass

    except KeyboardInterrupt:
        # TODO: Use the python KeyboardIntterupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        pass


if __name__ == '__main__':
    server()
    sys.exit(0)
