#!/bin/env python
# multithreaded web server
# multiweb.py
# From https://kdecherf.com/blog/2012/07/29/multithreaded-python-simple-http-server 
import SocketServer
import BaseHTTPServer
import SimpleHTTPServer
class ThreadingSimpleServer(SocketServer.ThreadingMixIn,
                   BaseHTTPServer.HTTPServer):
    pass
import sys
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server = ThreadingSimpleServer(('', port), SimpleHTTPServer.SimpleHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print "Finished"
