import sys
import socket
import string
import random
import time
from connectionIRC import *

conn = ConnectionIRC("#laquintejuste", "Roparzh", "Roparzh", "Roparzh")
conn.connec()
#what your bot does after its up and running
while 1:
    text = conn.s.recv(2040).decode("UTF-8") #don't mess with this, idk what it does
    if text.find('PING') != -1:         #confirms connection to IRC
        conn.s.send(bytes('PONG ' + text.split() [1] + '\r\n', "UTF-8"))

    if text.find('YO') != -1:
        conn.s.send(bytes("PRIVMSG %s :Yo, ca fart ?\r\n" % conn.MASTER, "UTF-8"))

    if text.find('Bonjour, Roparzh') != -1:
        time.sleep( 2 )
        conn.s.send(bytes("PRIVMSG #laquintejuste :Môssieur Sire, en chair et en personne !\r\n" , "UTF-8"))

    if text.find("Excusez, y a moyen de vous entretenir deux secondes ?") != -1:
        time.sleep( 2 )
        conn.s.send(bytes("PRIVMSG #laquintejuste :Oui c est a quel sujet ?\n" , "UTF-8"))

    if text.find("Non c est parce que je suis passé par hasard hier matin devant vos enclos.") != -1:
        time.sleep( 2 )
        conn.s.send(bytes("PRIVMSG #laquintejuste :Oui tout à fait.\n" , "UTF-8"))

    if text.find("Et j ai vu que vous avez une jolie petite poule blanche là.") != -1:
        time.sleep( 2 )
        conn.s.send(bytes("PRIVMSG #laquintejuste :Une poule blanche oui.\n" , "UTF-8"))

    if text.find(" Oui une poule blanche bien mignonne voyez le bel animal.") != -1:
        time.sleep( 3 )
        conn.s.send(bytes("PRIVMSG #laquintejuste : Bien sûr, c’est au sujet quoi t’est-ce ?\n" , "UTF-8"))

    if text.find("C’est au sujet qu’en fait c’est la mienne et je vais vous mettre un pain dans la gueule mais quelque chose de….violent.") != -1:
        time.sleep( 4 )

        conn.s.send(bytes("PRIVMSG #laquintejuste : Mais tout à fait ! Hé ben je dirais également que le genou peut partir dans les noix de manière assez soudaine et que ça pourrait éventuellement vous faire sortir les baloches par les oreilles. N’y voyez aucune malice !\n" , "UTF-8"))

#quit bot when you type your cmd + quit + password(without space or +)
    if text.find(conn.cmd + "quit" + str(conn.password)) != -1:
        conn.s.send(bytes("QUIT\r\n","UTF-8"))
        break
