from flask import Flask, url_for
from flask import render_template
from flask import json
import sqlite3

app = Flask(__name__)

# Définir un préfixe global pour la mise en production
PREFIX = '/flask'
# PREFIX = ''

@app.context_processor
def inject_prefix():
    # Rendre le préfixe accessible dans tous les templates
    return {'prefix': PREFIX}

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route('/contact/')
def MaPremiereAPI():
    return render_template('contact.html')

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/calcul_somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    return "<h2>La somme de vos valeurs est : </h2>" + str(valeur1 + valeur2)

# @app.route('/impaire/<int:valeur>')
# def impaire(valeur):
    

if __name__ == "__main__":
  app.run(debug=True)
