from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/workers/idle', methods=['get'])
def idleworkers():
    conn = sqlite3.connect('Containers.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM containers""")
    allworkers = c.fetchall()
    print(allworkers)
    idleworkers = [num for num in allworkers if num[1] == 0]
    countidleworkers = len(idleworkers)
    return jsonify(countidleworkers)


@app.route('/workers/total', methods=['get'])
def totalworkers():
    conn = sqlite3.connect('Containers.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM containers""")
    allworkers = c.fetchall()
    print(allworkers)
    totalworkers = [num for num in allworkers if num[1] == 0 or num[1] == 1]
    counttotalworkers = len(totalworkers)
    return jsonify(counttotalworkers)


@app.route('/documents/total', methods=['get'])
def totaldocuments():
    conn = sqlite3.connect('Containers.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM containers""")
    alldocuments = c.fetchall()
    print(alldocuments)
    totaldocs = sum(num[2] for num in alldocuments)
    return jsonify(totaldocs)


@app.route('/documents/servers', methods=['get'])
def documents():
    conn = sqlite3.connect('Containers.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM containers""")
    alldocuments = c.fetchall()
    print(alldocuments)
    serverdocs = [[num[0], num[2]] for num in alldocuments]
    return jsonify(serverdocs)


@app.route('/documents/upload', methods=['post'])
def uploaddocuments():
    return jsonify()


@app.route('/count/<string:query>', methods=['get'])
def count(query):
    conn = sqlite3.connect('Containers.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM containers""")
    return jsonify()


@app.route('/find/<string:query>/<int:amount>', methods=['get'])
def find(query, amount):
    return jsonify()


if __name__ == '__main__':
    app.run()