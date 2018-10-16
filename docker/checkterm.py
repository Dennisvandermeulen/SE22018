#!/bin/python3

# If the user enters a query this file will check whether the current machine needs to look up the entered query

import sqlite3
from os import listdir

conn = sqlite3.connect('Wordlist.db')
c = conn.cursor()

# TODO: Zoekterm aanleveren vanuit CoCo SPATIES VOOR EN ACHTER INVOEGEN
searchterm = " OM "

# Controleer of de zoekterm al in de database staat
c.execute("""SELECT quantity FROM wordlist WHERE term = ?""", (searchterm, ))
indb = c.fetchall()
# Als de zoekterm niet in de database voor komt zoeken we door de files heen
if len(indb) is 0:
    i = 0
    quantity = 0
    txtfiles = ''
    for file in listdir('files'):
        if file.endswith(".txt"):
            with open('files/' + file) as f:
                contents = f.read()
                if searchterm.lower() in contents.lower():
                    txtfiles = txtfiles + file + '#'
                    quantity = quantity + 1
        i = i + 1
    c.execute("""INSERT INTO wordlist(term, quantity, cdocs) VALUES (?,?,?)""", (searchterm, quantity, txtfiles))

conn.commit()
conn.close()
