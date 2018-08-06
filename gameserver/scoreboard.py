#!/usr/bin/env python 
import SocketServer
import os
import socket
class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
       fo = open("teams.list", "r")
       self.request.send("team  |score\n")
       teams=[]
       for team in fo.readlines():
           teams.append(team[:-1])
       print teams
       for team in teams:
           off=0
           deff=0
           if os.path.isfile("./flag/"+team+".score"):
               ff = open("./flag/"+team+".score", "r")
               off=ff.readline().count('+');
               ff.close();
           self.request.send(team+" |"+str(off)+"\n")#"  |"+str(deff)+"\n")


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9990
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
