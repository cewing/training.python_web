import socket


def get_constants(prefix):
    return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')


def get_address_info(host, port):
    for response in socket.getaddrinfo(host, port):
        fam, typ, pro, nam, add = response
        print('family: {}'.format(families[fam]))
        print('type: {}'.format(types[typ]))
        print('protocol: {}'.format(protocols[pro]))
        print('canonical name: {}'.format(nam))
        print('socket address: {}'.format(add))
        print()
