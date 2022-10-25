from logging import logThreads
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from magic import getMagicNumber

class MyServer(SimpleXMLRPCServer):
    def serve_forever(self):
        self.quit = 0
        while not self.quit:
            self.handle_request()
def kill():
    server.quit = 1
    return 1

server = MyServer(('localhost',8080), logRequests=False)
server.register_introspection_functions()
server.register_function(getMagicNumber)
server.register_function(kill)
server.serve_forever()

