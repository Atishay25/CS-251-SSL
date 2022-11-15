from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from magic import getMagicNumber

class MyServer(SimpleXMLRPCServer):         # My Server class with feature of handling requests
    def serve_forever(self):                # and killing itself when kill function is called from client side
        self.quit = 0
        while not self.quit:
            self.handle_request()
def kill():
    server.quit = 1
    return 1

server = MyServer(('localhost',8080), logRequests=False)        # Using localhost 8080 port
server.register_introspection_functions()
server.register_function(getMagicNumber)
server.register_function(kill)
server.serve_forever()

