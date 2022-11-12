#! /usr/bin/etc  python3
#-*- coding: utf-8 -*-

from flask  import Flask, render_template
from config import config
from flask_mysqldb import MySQL


app = Flask(__name__)
conexion = MySQL(app)

@app.route('/')
def index():
    return "HOLA MUNDO DESDE FLASK"

@app.route('/login')
def login():
    try:
        return "OK"
    except Exception as ex:
        return "ERROR"

if __name__ == '__main__':
    app.config.from_object(config["desarrollo"])
    app.run()