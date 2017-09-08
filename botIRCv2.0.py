import sys
import socket
import string
import random
import time
from connectionIRC import *

conn = ConnectionIRC("#laquintejuste", "Guethenoc", "Guethenoc", "Guethenoc")
conn.connec()
#what your bot does after its up and running
while 1:
    print("boucle")
    text = conn.s.recv(2040).decode("UTF-8") #don't mess with this, idk what it does
    if text.find('PING') != -1:         #confirms connection to IRC
        conn.s.send(bytes('PONG ' + text.split() [1] + '\r\n', "UTF-8"))

    if text.find('YO') != -1:
        conn.s.send(bytes("PRIVMSG %s :Yo, ca fart ?\r\n" % conn.MASTER, "UTF-8"))

    if text.find('Bonjour, Guethenoc') != -1:
        conn.s.send(bytes("PRIVMSG #laquintejuste :Ces bourgeois, ils savent plus quoi inventer ! A force de lire et d'écrire, ils deviennent tous plus cons les uns qu'les autres.\r\n" , "UTF-8"))

    if text.find('A roulette !') != -1:
        print("roulette")
        conn.s.send(bytes("PRIVMSG #laquintejuste :Excusez, y a moyen de vous entretenir deux secondes ?\r\n" , "UTF-8"))

    if text.find("Oui c est a quel sujet") != -1:
        time.sleep( 2 )
        conn.s.send(bytes("PRIVMSG #laquintejuste :Non c est parce que je suis passé par hasard hier matin devant vos enclos.\n" , "UTF-8"))

    if text.find("Oui tout à fait.") != -1:
        time.sleep( 2 )
        conn.s.send(bytes("PRIVMSG #laquintejuste :Et j ai vu que vous avez une jolie petite poule blanche là.\n" , "UTF-8"))

    if text.find("Une poule blanche oui.") != -1:
        time.sleep( 3 )
        conn.s.send(bytes("PRIVMSG #laquintejuste : Oui une poule blanche bien mignonne voyez le bel animal.\n" , "UTF-8"))

    if text.find(" Bien sûr, c’est au sujet quoi t’est-ce ?") != -1:
        time.sleep( 5 )
        conn.s.send(bytes("PRIVMSG #laquintejuste :C’est au sujet qu’en fait c’est la mienne et je vais vous mettre un pain dans la gueule mais quelque chose de….violent.\n" , "UTF-8"))

#quit bot when you type your cmd + quit + password(without space or +)
    if text.find(conn.cmd + "quit" + str(conn.password)) != -1:
        conn.s.send(bytes("QUIT\r\n","UTF-8"))
        break
