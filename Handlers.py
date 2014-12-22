import SimpleHTTPServer
class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	requests = []
	msg = "<html><body><p>Too many requests</p></body></html>"

	def do_GET(self):
		client_ip = self.client_address[0]

		if len(self.requests)<20:
			self.requests.append(client_ip)
		else:
			self.requests.pop(0)
			self.requests.append(client_ip)

		if self.requests.count(client_ip) > 5:
			self.send_response(429)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(self.msg)
		else:
			return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

