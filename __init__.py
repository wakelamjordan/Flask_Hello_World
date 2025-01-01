from flask import Flask, url_for
from flask import render_template
from flask import json, jsonify
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
def doc():
    doc_data = {
        "title": "ddDocumentation de l'API",
        "endpoints": [
            # {
            #     "url": url_for('MaPremiereAPI', _external=True),
            #     "description": "Renvoie un message de bienvenue"
            # },
            {
                "url": url_for('carre', val_user=5, _external=True),
                "description": "Calcule le carré d'un nombre"
            },
            {
                "url": url_for('somme', valeur1=5, valeur2=10, _external=True),
                "description": "Calcule la somme de deux nombres"
            }
        ]
    }
    return jsonify(doc_data)

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

# @app.route('/contact/')
# def MaPremiereAPI():
#     return render_template('contact.html')

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    data_carre = {
        "valeur": val_user,
        "carre": val_user * val_user
    }
    return jsonify(data_carre)

@app.route('/calcul_somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    data_somme = {
        "valeur1": valeur1,
        "valeur2": valeur2,
        "somme": valeur1 + valeur2
    }
    return jsonify(data_somme)

# @app.route('/impaire/<int:valeur>')
# def impaire(valeur):
    

if __name__ == "__main__":
  app.run(debug=True)
