import socket
import sys

# Create a TCP/IP socket

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)

try:
    # Send data
    message = 'This is the message.  It will be repeated.'

    # print the response

finally:
    # close the socket to clean up
