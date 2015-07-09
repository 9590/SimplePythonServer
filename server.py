import SimpleHTTPServer
import SocketServer
import Handlers

PORT = 80

Handler = Handlers.RequestHandler
Address = ("",PORT)
httpd = SocketServer.TCPServer(Address, Handler)

print "serving at port", PORT
httpd.serve_forever()

