import socket


def get_constants(prefix):
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix))


def get_address_info(host, port):
    families = get_constants('AF_')
    types = get_constants('SOCK_')
    protocols = get_constants('IPPROTO_')
    for response in socket.getaddrinfo(host, port):
        fam, typ, pro, nam, add = response
        print 'family: ', families[fam]
        print 'type: ', types[typ]
        print 'protocol: ', protocols[pro]
        print 'canonical name: ', nam
        print 'socket address: ', add
        print
