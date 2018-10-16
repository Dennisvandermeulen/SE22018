#!/bin/python3

import sqlite3

conn = sqlite3.connect('Wordlist.db')
c = conn.cursor()

searchterm = "hallo" # TODO: zoekterm doorgeven vanuit CoCo
totalcount = 2  # TODO: som van voorgaande containers
containerlist = [101, 102, 103, 104, 106, 110, 125]  # TODO: Array met containers die nog moeten

# Haal het resultaat op dat gevonden is in checkterm.py

c.execute("""SELECT quantity FROM wordlist WHERE term = ?""", (searchterm, ))
quantity = c.fetchone()[0]

# Tel de variabele op bij de huidige totalcount

totalcount = totalcount + quantity

# Geef door aan volgende container
containerlist.pop(0)

# TODO: geef variabele door
