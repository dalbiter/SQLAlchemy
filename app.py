from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
from models import db, connect_db, Pet

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
# Below line may be necessary in older versions of SQLA, if you run in ipython and get warning...
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Below line is helpful while we are learning for debugging, SQLALCHEMY_ECHO to True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret-key'
app.config['DEBUG_TB_INTERECEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home():
    """Shows list of all pets in db"""

    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """show details about a single pet"""

    pet = Pet.query.get_or_404(pet_id)

    return render_template('details.html', pet=pet)    
