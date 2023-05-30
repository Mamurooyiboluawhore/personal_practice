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

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == "POST":
        return "this is a post request"
    else:
        return "this is a get request"


if __name__ == "__main__":
    app.run()
