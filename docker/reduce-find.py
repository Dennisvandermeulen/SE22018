#!/bin/python3

import sqlite3

conn = sqlite3.connect('Wordlist.db')
c = conn.cursor()

searchterm = " OM " # TODO: zoekterm doorgeven vanuit CoCo !!!!!SPATIE VOOR EN ACHTER PLAATSEN BIJ ORIGINELE QUERY!!!!!
amountleft = 2  # TODO: maximumaantal aanleveren vanuit CoCo
containerlist = [101, 102, 103, 104, 106, 110, 125]  # TODO: Array met containers die nog moeten

# Haal het resultaat op dat gevonden is in checkterm.py

c.execute("""SELECT quantity,cdocs FROM wordlist WHERE term = ?""", (searchterm, ))
results = c.fetchone()

quantity = results[0]
docnames = results[1].split('#')

# Tel de variabele op bij de huidige totalcount

amountleft = amountleft - quantity

if amountleft <= 0:
    # TODO: geef door aan CoCo in plaats van volgende container
    print("test")

else:
    containerlist.pop(0)
    # Geef door aan volgende container

# TODO: geef opdracht dezelfde opdracht door aan het volgende poortnummer

# TODO: Als laatste containerpoortnummer bereikt is, geef het door aan CoCo, zodat het resultaat gegeven kan worden