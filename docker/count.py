#!/bin/python3

import sqlite3
import glob
from os import listdir

# TODO: Tel in de documenten in de container hoevaak de variabele die doorgegeven is door CoCo voorkomt

# TODO: Voeg de opgehaalde informatie toe aan de index in de sqlite database
conn = sqlite3.connect('Wordlist.db')
c = conn.cursor()

# TODO: Zoekterm aanleveren
searchterm = "hallo"

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
                if searchterm in contents:
                    txtfiles = txtfiles + file
                    quantity = quantity + 1
        i = i + 1
    c.execute("""INSERT INTO wordlist(term, quantity, docnr) VALUES (?,?,?)""", (searchterm, quantity, txtfiles))

conn.commit()
conn.close()
