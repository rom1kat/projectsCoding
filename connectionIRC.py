import sys
import socket
import string
import random

class ConnectionIRC():

    def __init__(self, _chan, _nick, _ident, _realname):
        self.HOST = "irc.freenode.net" #keep this the same
        self.CHANNEL = _chan #"#bots" #keep this set to
        self.PORT = 6667 #IRC's port, don't change
        self.NICK = _nick #"Roparzh" #name of your bot
        self.IDENT = _ident #"Roparzh" #more name of bot
        self.REALNAME = _realname #"Roparzh" #bot bot bot
        self.MASTER = "ArthurPendragonR" #you
        self.readbuffer = "" #can't touch this.
        self.password = str(random.randint(0,1111)) + "acre" #change to anything
        print (self.password) #this prints your randomly-generated password
        self.cmd = "apre" #what the bot looks for to execute commands

#getting connected
    def connec(self):
        self.s=socket.socket( )
        self.s.connect((self.HOST, self.PORT))
        self.s.send(bytes("NICK %s\r\n" % self.NICK, "latin1"))
        self.s.send(bytes("USER %s %s bla :%s\r\n" % (self.IDENT, self.HOST, self.REALNAME), "latin1"))
        self.s.send(bytes("JOIN %s\r\n" % (self.CHANNEL), "latin1"));
        self.s.send(bytes("PRIVMSG %s :Hello \r\n" % self.MASTER, "latin1"))
