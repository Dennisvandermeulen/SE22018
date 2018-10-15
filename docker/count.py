#!/bin/python3

import sqlite3
from os import listdir

# TODO: Tel in de documenten in de container hoevaak de variabele die doorgegeven is door CoCo voorkomt

# TODO: Voeg de opgehaalde informatie toe aan de index in de sqlite database
conn = sqlite3.connect('Wordlist.db')
c = conn.cursor()

term = "hoi" # TODO: Zoekterm aanleveren

# Controleer of de zoekterm al in de database staat
c.execute("""SELECT quantity FROM wordlist WHERE term = ?"""), term
indb = c.fetchall()
if len(indb) is 0:
    # TODO Woorden tellen in de textbestanden in de
    listdir("/files/file*.txt")

    file=open("/files/")
    c.execute("""INSERT INTO wordlist(term, quantity, docnr) VALUES (?,?,?)""")

conn.commit()
conn.close()
