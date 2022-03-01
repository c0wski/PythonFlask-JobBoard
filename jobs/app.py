from flask import Flask, render_template, g
import sqlite3

PATH = db/jobs.sqlite

app = Flask(__name__)

def open_connection()
    getattr(g, _connection, None)
        return connection
    if connection == None:
        sqlite3.connect(PATH) = connection, g._connection
    connection.row_factory = sqlite3.Row
    return connection



@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
