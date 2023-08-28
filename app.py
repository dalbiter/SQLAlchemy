from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'

db = SQLAlchemy()
db.app = app
db.init_app(app)

app.config['SECRET_KEY'] = 'secret-key'
app.config['DEBUG_TB_INTERECEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def show_home():
    """Shows home page"""
    return render_template('index.html')