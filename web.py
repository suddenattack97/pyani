from flask import Flask, render_template, jsonify, Response
from flask import request, redirect, url_for, session, send_file ,abort
from datetime import datetime
import sqlite3
from io import BytesIO

app = Flask(__name__)

DATABASE = 'animal.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_animals():
    conn = get_db_connection()
    animals = conn.execute('SELECT * FROM animal').fetchall()
    conn.close()
    return animals

@app.route('/')
def index():
    animals = get_animals()
    return render_template('index.html', animals=animals)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6700, debug=True)
