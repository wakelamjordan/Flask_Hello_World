from flask import Flask, url_for
from flask import render_template
from flask import json, jsonify, request
import sqlite3

app = Flask(__name__)

# Définir un préfixe global pour la mise en production
# PREFIX = '/flask'
# PREFIX = ''

# @app.context_processor
# def inject_prefix():
#     # Rendre le préfixe accessible dans tous les templates
#     return {'prefix': PREFIX}

@app.route('/')
def doc():
    doc_data = {
    "title": "Documentation de l'API",
    "endpoints": [
        {
        "url": "/",
        "method": "GET",
        "description": "Affiche la documentation de l'API en format JSON."
        },
        {
        "url": "/exercices/",
        "method": "GET",
        "description": "Affiche la page HTML des exercices (template Flask)."
        },
        {
        "url": "/calcul_carre/<val_user>",
        "method": "GET",
        "parameters": {
            "val_user": {
            "type": "int",
            "description": "Nombre entier pour lequel on veut calculer le carré."
            }
        },
        "description": "Calcule le carré d'un nombre entier fourni dans l'URL."
        },
        {
        "url": "/calcul_somme/",
        "method": "GET",
        "parameters": {
            "query_params": {
            "type": "list",
            "description": "Liste de nombres entiers passés en paramètres GET pour calculer leur somme."
            }
        },
        "description": "Calcule la somme des nombres passés en paramètres GET."
        },
        {
        "url": "/impaire/<valeur>",
        "method": "GET",
        "parameters": {
            "valeur": {
            "type": "int",
            "description": "Nombre entier à vérifier s'il est pair ou impair."
            }
        },
        "description": "Détermine si un nombre entier est pair ou impair."
        },
        {
        "url": "/valeur_max/",
        "method": "GET",
        "parameters": {
            "query_params": {
            "type": "list",
            "description": "Liste de nombres entiers passés en paramètres GET pour déterminer le maximum."
            }
        },
        "description": "Renvoie la valeur maximale parmi les nombres passés en paramètres GET."
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

@app.route('/calcul_somme/', methods=['GET'])
def somme():

    params = request.args.to_dict()
    
    result = 0
    
    valeurs = ""
    
    if params == {}: 
        return jsonify({"error": "Aucun paramètre n'a été fourni"}), 400

    for value in params.values():
        if not value.isdigit() or value == "":
            return jsonify({"error": "Tous les paramètres doivent être des nombres entiers"}), 400

        result += int(value)
        
        if valeurs == "":
            valeurs += value
        else:
            valeurs += "+" + value

    # Construire la réponse
    data_somme = {
        "valeurs": valeurs,
        "somme": result
    }
    return jsonify(data_somme)
    # return jsonify(data_somme)
# @app.route('/calcul_somme/<int:valeur1>/<int:valeur2>')
# def somme(valeur1, valeur2):
#     data_somme = {
#         "valeur1": valeur1,
#         "valeur2": valeur2,
#         "somme": valeur1 + valeur2
#     }
#     return jsonify(data_somme)

@app.route('/impaire/<int:valeur>')
def impaire(valeur):
    if valeur % 2 == 0:
        response = "paire"
    else:
        response = "impaire"
    
    data_impaire = {
        "valeur": valeur,
        "reponse": response
    }
    
    return jsonify(data_impaire)
    
    
@app.route('/valeur_max/', methods=['GET'])
def valeur_max():
    params = request.args.to_dict()
    
    best_value = 0
    
    valeurs = ""
    
    if params == {}: 
        return jsonify({"error": "Aucun paramètre n'a été fourni"}), 400
    
    for value in params.values():
        if not value.isdigit() or value == "":
            return jsonify({"error": "Tous les paramètres doivent être des nombres entiers"}), 400

        if int(value) > best_value:
            best_value = int(value)
            
        if valeurs == "":
            valeurs += value
        else:
            valeurs += "," + value
    
    data_max = {
        "valeurs": valeurs,
        "max": best_value
    }
    
    return jsonify(data_max)


if __name__ == "__main__":
  app.run(debug=True)
