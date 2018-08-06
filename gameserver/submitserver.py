#!/usr/bin/env python 
import SocketServer
import os
import socket
import requests
allflags=[]
sentFlag=[]
fo = open('teams.list', 'r')
teams=[]
for team in fo.readlines():
    teams.append(team[:-1])    

for teamflag in teams:
    allf=open("./flag/"+teamflag+".flag", "r").readlines()
    s=''
    s += allf[0]
    allflags.append(s.strip())


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        self.request.send("please send us your team name\n")
        getTeam = self.request.recv(1024).strip()
	if not os.path.isfile('./flag/'+getTeam+'.flag'):
		self.request.send('No such team\n')
		self.request.close()
	self.request.send("please send us the flag\n")
        getFlag = self.request.recv(1024).strip()
        ff = open("./flag/"+getTeam+".sent", "r")
        sentFlag=[]
        for flaged in ff.readlines():
            sentFlag.append(flaged.rstrip())
        #if flag in flags:
        if getFlag in allflags and getFlag not in sentFlag:
            ff = open("./flag/"+getTeam+".score", "a")
            ff.write("+")
            fg = open("./flag/"+getTeam+".sent", "a")
            fg.write(getFlag+"\n")
            ff.close()
            fg.close()
            self.request.send("scored!\n")
	
        else:
            self.request.send("error!\n")
       
        ff.close()
        
        

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
