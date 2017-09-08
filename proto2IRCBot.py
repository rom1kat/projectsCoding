import sys
import socket
import string
import random

HOST = "irc.freenode.net" #keep this the same
CHANNEL = "#bots" #keep this set to
PORT = 6667 #IRC's port, don't change
NICK = "Roparzh" #name of your bot
IDENT = "Roparzh" #more name of bot
REALNAME = "Roparzh" #bot bot bot
MASTER = "Arthur" #you
readbuffer = "" #can't touch this.

password = str(random.randint(0,1111)) + "CHANGEME" #change to anything
print (password) #this prints your randomly-generated password
cmd = "CHANGEME" #what the bot looks for to execute commands

#getting connected
s=socket.socket( )
s.connect((HOST, PORT))
s.send(bytes("NICK %s\r\n" % NICK, "latin1"))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "latin1"))
s.send(bytes("JOIN %s\r\n" % (CHANNEL), "latin1"));
s.send(bytes("PRIVMSG %s :Hello \r\n" % MASTER, "latin1"))

#what your bot does after its up and running
while 1:
    text = s.recv(2040).decode("latin1") #don't mess with this, idk what it does
    if text.find('PING') != -1:         #confirms connection to IRC
        s.send(bytes('PONG ' + text.split() [1] + '\r\n', "latin1"))

    if text.find('YO') != -1:
        s.send(bytes("PRIVMSG %s :Yo, ca fart ?\r\n" % MASTER, "latin1"))

    if text.find('Bonjour, Roparzh') != -1:
        s.send(bytes("PRIVMSG %s :Môssieur Sire, en chair et en personne !\r\n" % MASTER, "latin1"))

    # if



#quit bot when you type your cmd + quit + password(without space or +)
    if text.find(cmd + "quit" + str(password)) != -1:
        s.send(bytes("QUIT\r\n","latin1"))
        break
