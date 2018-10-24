from flask import Flask, jsonify, request
from os import listdir
import sqlite3

app = Flask(__name__)

@app.route('/find/<string:query>/<int:amount>')
@app.route('/count/<string:query>', methods=['post'])
def count(query):
    conn = sqlite3.connect('Wordlist.db')
    c = conn.cursor()
    c.execute("""SELECT quantity FROM wordlist WHERE term = ?""", (query,))
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
                    if query.lower() in contents.lower():
                        txtfiles = txtfiles + file + '#'
                        quantity = quantity + 1
            i = i + 1
        c.execute("""INSERT INTO wordlist(term, quantity, cdocs) VALUES (?,?,?)""", (query, quantity, txtfiles))

    conn.commit()
    conn.close()
    return 'Done'

@app.route('/reduce-count/<string:query>/<int:totalcount>', methods = ['get'])
def reducecount(query,totalcount):
    conn = sqlite3.connect('Wordlist.db')
    c = conn.cursor()
    c.execute("""SELECT quantity FROM wordlist WHERE term = ?""", (query,))
    quantity = c.fetchone()[0]
    totalcount = totalcount + quantity
    print(totalcount)

    return 'NEXT'

# @app.route('/reduce-count/<string:query>')
# def reducecount2(query):
#     conn = sqlite3.connect('Wordlist.db')
#     c = conn.cursor()
#     c.execute("""SELECT quantity FROM wordlist WHERE term = ?""", (query,))
#     quantity = c.fetchone()[0]
#     totalcount = totalcount + quantity
#     print(totalcount)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5001")