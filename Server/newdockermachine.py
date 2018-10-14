#!/bin/python3

# cstate 0 = idle
# cstate 1 = busy
# cstate 2 = killed

import docker
import sqlite3
# TODO opdracht doorgeven van de REST server

client = docker.from_env()
conn = sqlite3.connect('Containers.db')
c = conn.cursor()

#####################################################
# Beslis welke poort toe te wijzen aan de container #
#####################################################

# Check of cstate 0 is (poort beschikbaar, container nog actief)

# TODO: toevoegen cstate 0

# Check of cstate 2 is (poort beschikbaar, container uitgeschakeld, al in database)

c.execute("""SELECT * FROM containers  WHERE cstate=2 ORDER BY cport""")
statetwo = c.fetchall()

# Als alle tussenliggende poorten in gebruik zijn voegen we een nieuwe entry toe aan de database met het laatste poortnummer +1
if len(statetwo) is 0:
    c.execute("""SELECT cport FROM containers ORDER BY cport DESC LIMIT 1""")
    oldport = c.fetchone()[0]
    newport = oldport + 1
    c.execute("""INSERT INTO containers(cport, cstate) VALUES (?, ?)""", (newport, 1))

# Als er ergens een ruimte is in de tussenliggende poorten gebruiken we die
else :
    c.execute("""SELECT * FROM containers  WHERE cstate=2 ORDER BY cport LIMIT 1 """)
    newport = c.fetchone()[0]
    c.execute("""UPDATE containers SET cstate = ? WHERE cport = ?""", (1, newport))

print("De poort voor de machine is " + str(newport))

conn.commit()
conn.close()

####################
# Start de Machine #
####################

# cname, ports, networks?
client.containers.run('alpine', ports={str(newport) + "/tcp":newport})