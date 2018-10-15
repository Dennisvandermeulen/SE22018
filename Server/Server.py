from flask import Flask
from flask import api
app = Flask(__name__)

@app.route('/action/find/')
def find():
    return 'find'

@app.route('/action/count/')
def count():
    return 'count'

if __name__ == '__main__':
    app.run()
