# Code & Coffee project by Jane 
# thanks for the cake Tim!
# based on Jon Berg Making a simple web server in Python fragments.turtlemeat.com/pythonwebserver.php
# Make a simple on off buttom that sends a request to the python server, this request can trigger switch on a music stream e.g. mplayer 

# July 2012 Edinburgh Hacklab

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler) :
	def do_GET(self) :
		try:
			if self.path.endswith(".html"):
				f = open(curdir + sep + self.path) # access my python server and read from this file
				self.send_response(200)
				self.send_header('Content-type',	'text/html') #what is the reason for the tab?
				self.end_headers()
				self.wfile.write("Hello today: ") + str(time.localtime([7]))
				return
				
			return
	
		except IOError:
			self.send_error(404, 'Sorry, I can\'t find the file %s' % self.path)
	
	def do_POST(self):
		global rootnode
		try:
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type')) # I don't understand this part
			if ctype == 'multipart/form-data':
				query=cgi.parse_multipart(self.rfile, pdict)
			self.send_response(301)
			
			self.end_headers()
			upfilecontent = query.get('upfile')
			print "filecontent", upfilecontent[0]
			self.wfile.write("<html>Post done okay</br>"); # Is it that what I do here is something fancy to send a POST request and opens an html doc (and never close it)? 
			self.wfile.write(upfilecontent[0]);
			
		except :
			pass

def main():
		try:
			server = HTTPServer(('', 80), MyHandler)
			print 'started first httpserver pony...'
			server.serve_forever()
		except KeyboardInterrupt:
			print '^C received, shutting down server'
			server.socket.close()

if __name__ == '__main__':
	main()		
	
