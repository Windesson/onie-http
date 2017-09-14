#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import logging

PORT = 80

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers);
        isOnieEth = self.headers.get("ONIE-ETH-ADDR",False);

        if(isOnieEth):
            ETH = isOnieEth.replace(":","-");
            new_path = "/%s%s" % (ETH,self.path);
            print("redirect path  %s  -> %s" % (self.path,new_path));
            self.path = new_path;

        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
