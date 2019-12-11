from flask import Flask
from flask import render_template
from flask import request
import os
import sqlite3
from sighting import Sighting

# Create/Connect a database
conn = sqlite3.connect('flowers2019.db')

# Create cursor to execute SQL commands
c = conn.cursor()

# sight_1 = Sighting('', '', '', '')
#
# c.execute("INSERT INTO Sightings Values (:name, :person, :location, :sighted)", {'name': sight_1.name, 'person': sight_1.person, 'location': sight_1.location, 'sighted': sight_1.sighted})

# Select all entries in the table Flowers from 'flowers2019.db'
c.execute("SELECT * FROM Flowers")

# fetch all entries returned by the SQL query
print(c.fetchall())

# Save query
conn.commit()

conn.close()

# create an app instance
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])                # at the end point /
def home():                      # call method home
    if request.form:
        print(request.form)
    return render_template("home.html")       # which returns 'home.html' template
if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app