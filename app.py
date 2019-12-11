# app.py
from flask import Flask           # import flask
import os
import sqlite3
import pandas as pd

# Create a database
conn = sqlite3.connect('flowers2019.db')

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app