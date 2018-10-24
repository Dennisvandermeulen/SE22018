from flask import Flask, g, jsonify, session
from os import listdir
import requests
import sqlite3

port = 0

app = Flask(__name__)

@app.route('/find/<string:query>/<string:nextport>/<int:amount>', methods=['post'])
@app.route('/count/<string:query>/<string:nextport>', methods=['post'])
def count(query, nextport):
    print('counting ' + query + ' in worker')
    conn = sqlite3.connect('Wordlist.db')
    c = conn.cursor()
    c.execute("""SELECT quantity FROM wordlist WHERE term = ?""", (query,))
    indb = c.fetchall()
    # Als de zoekterm niet in de database voor komt zoeken we door de files heen
    if len(indb) is 0:
        print('query not counted before')
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
    print('The port of the next machine is: ' + str(nextport))
    global port
    port = nextport
    return 'Done'


@app.route('/reduce-count/<string:query>/<int:totalcount>', methods = ['get'])
def reducecount(query,totalcount):
    print('iterating through reduce-count')
    conn = sqlite3.connect('Wordlist.db')
    c = conn.cursor()
    c.execute("""SELECT quantity FROM wordlist WHERE term = ?""", (query,))
    quantity = c.fetchone()[0]
    totalcount = totalcount + quantity
    print('The current total amount is ' + str(totalcount))
    global port
    url = 'http://127.0.0.1:' + str(port) + '/reduce-count/' + str(query)
    response = requests.get(url)
    return 'NEXT'


@app.route('/reduce-count/<string:query>')
def reducecount2(query):
    print('initialising reduce-count')
    conn = sqlite3.connect('Wordlist.db')
    c = conn.cursor()
    c.execute("""SELECT quantity FROM wordlist WHERE term = ?""", (query,))
    quantity = c.fetchone()[0]
    totalcount = quantity
    print('The current total amount is ' + str(totalcount))
    global port
    url = 'http://127.0.0.1:' + str(port) + '/reduce-count/' + str(query) + '/' + str(totalcount)
    # response = requests.get(url)
    # if port == 5000:
    #     return totalcount
    # else
    #     return 'PLACEHOLDER'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5001")