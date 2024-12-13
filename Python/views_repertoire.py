# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:32:31 2022

@author: NSI Première
"""

from flask import Flask, render_template, request          #importe bibliothque pour serveur web 

app= Flask(__name__)                                       #création d'un objet app

@app.route('/')                                            #chemin d'accès grâce à un décorateur
def index_rpertoire():                                     #definition de index_rpertoire
    return render_template("index_repertoire.html")        #renvoie vers le client la page index_repertoire.html

@app.route('/ajout_contact.html')                          #chemin d'accès grâce à un décorateur
def ajout_contact():
    return render_template("ajout_contact.html")           #renvoie vers le client la page ajout_contact.html

@app.route(('/contact_ajouté.html') ,methods=['POST'])     #chemin d'accès grâce à un décorateur
def contact_ajoute():
    result=request.form                                    #création d'une variable result contenant les arguments rçus par la requête                             
    n=result['nom']                                        #création d'une variable n contenant le nom entré par l'utilisateur(celui de la requête)
    num=result['numero']                                   #création d'une variable num contenant le numéro entré par l'utilisateur(celui de la requête)
    with open ('repertoire.txt','a') as f :                #ajouter un contact dans un fichier texte
        f.write (n + "\n" + num + "\n")                    #écriture du nom entré par l'utilisateur, retour à la ligne puis le numéro puis retour à la ligne
    return render_template("contact_ajouté.html", nom=n, numero=num)  #renvoie vers le client la page contact_ajouté.html et le nom et numéro ajouté

@app.route('/recherche_contact.html')                      #chemin d'accès grâce à un décorateur
def rech_contact():
    return render_template("recherche_contact.html")  #renvoie vers le client la page recherche_contact.html

@app.route(('/resultat_rech.html'),methods=['POST'])       #chemin d'accès grâce à un décorateur
def result_rech():
    dic_repertoire = {}                          #definition d'un dictionnaire vide
    result=request.form                          #création d'une variable result contenant les arguments rçus par la requête
    n=result['nom']                              #création d'une variable n contenant le nom recherché par l'utilisateur(celui de la requête)
    pair = True                                  #definition de la variable pair comme vrai
    with open ('repertoire.txt', "r") as f:      #ouvrir le fichier pour lire dedans
        for line in f:
            line = line.replace("\n", "")        #on remplace \n par rien 
            if pair == True:                     #test si pair est vrai 
                pair = False                     #alors pair devient faux
                name = line                      #la variable name contient la ligne
            else:
                pair = True                      #sinon pair devient vrai
                num = line                       #la variable num contient la ligne 
                dic_repertoire[name] = num       #définition du dictionnaire repertoire avec comme clé le name et la valeur num
        if (n in dic_repertoire):                #si n(le nom recherché) est dans le dictionnaire 
            num_tel= dic_repertoire[n]           #num_tel est la valeur associé à la clé donc au nom recherché
        else:
            num_tel="inconnu"
        num=num_tel
        return render_template("resultat_rech.html",numero=num, nom=n)  #renvoie vers le client la page resultat_rech.html et le numéro et le nom recherché
    
app.run(debug=True)                      #lancer le serveur