#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/mamus")
def Welcome():
    return 'my flask app'
 

@app.route("/Oyibo")
def Test():
    return "I'\m just testing this"

@app.route("/Mamuro")
def Testing():
    return "last page"


app.run()
