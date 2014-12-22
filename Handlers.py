import SimpleHTTPServer
class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	requests = []
	msg = "<html><body><p>Too many requests</p></body></html>"
	MAX_SIZE = 20
	MAX_REQ = 5

	def do_GET(self):
		client_ip = self.client_address[0]

		if len(self.requests) < self.MAX_SIZE:
			self.requests.append(client_ip)
		else:
			self.requests.pop(0)
			self.requests.append(client_ip)

		if self.requests.count(client_ip) > self.MAX_REQ:
			self.send_response(429)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(self.msg)
		else:
			return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

