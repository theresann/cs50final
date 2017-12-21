import os
import re
import collections
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from datetime import datetime

from helpers import *

UPLOAD_FOLDER = "uploads"


# configure application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

# save most commonly used words in the english language in an array
f = open("commonwords.txt", "r")
common_words = f.read().split()
f.close()

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index1.html")
    if request.method == "POST":
        file = request.files['file']
        # if the file doesn't exist or is of the wrong type, the apology is rendered
        if file.filename == "" or file.filename.split(".")[1]!="txt":
            return render_template("apology.html")
            
        # open the file in the uploads folder to write to it
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], file.filename), 'a')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        f.close()
        # save the text in the file as a variable named contents to be passed to suggestions.html
        with open(os.path.join(app.config['UPLOAD_FOLDER'], file.filename), 'r') as t:
            contents = t.read()
            t.close()
        # create an array with just the words in the file, all in lowercase
        words = re.findall(r'\w+', open("test.txt").read().lower())
        # find 12 most commonly used words in the file
        freq = collections.Counter(words).most_common(12)
        redundancies = []
        # take out words that are generally commonly used because they are necessary for sentences
        for word in freq:
            if word[0] not in common_words:
                redundancies.append(word[0])
        return render_template("suggestions.html", text=contents, common = " ".join(redundancies))
