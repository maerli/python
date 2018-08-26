#criando um servidor ftp em python

from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
authorizer = DummyAuthorizer()

#adicionado um usuário chammado "user" com a senha "12345"
authorizer.add_user("user", "12345", "/", perm="elradfmwMT")

address = ("0.0.0.0", 21)  # listen on every IP on my machine on port 21
handler = FTPHandler
handler.authorizer = authorizer

server = servers.FTPServer(address, handler)
server.serve_forever()
