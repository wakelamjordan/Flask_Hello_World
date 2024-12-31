from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./flask/exercices/'>Ici</a></p><p><a href='./flask/contact/'>Contact</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route('/contact/')
def MaPremiereAPI():
    return render_template('contact.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
