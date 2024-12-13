# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:36:25 2022

@author: NSI Première
"""
#définition de la fonction menu
def menu():                                      #définition de la fonction menu
    reponse = int(input("0-quitter\n1-écrire dans le répertoire\n2-rechercher dans le répertoire\nVotre choix ? "))
    return(reponse)                              #renvoie la variable reponse dans le pprogramme principal
         
#définition de la fonction écriture 
def ecriture():
    print("Entrer 0 pour annuler ou entrer un nom pour ajouter un nouveau contact ")
    nom=input("Votre choix : ")
    if nom == "0":
        print("Retour menu")                     
    else:
        numero = input("Entrer un numéro de téléphone : ") 
        with open ('repertoire.txt','a') as f :  #ajouter un contact dans un fichier texte
            f.write (nom + "\n" + numero + "\n")
            print("Votre contact a bien été ajouté au répertoire\n")
            ecriture()                            #appel de la fonction écriture

#définition de la fonction lecture 
def lecture():
    pair = True                                  #definition de la variable pair comme vrai
    with open ('repertoire.txt', "r") as f:      #ouvrir le fichier pour lire dedans
        for line in f:
            line = line.replace("\n", "")        #on remplace \n par rien 
            if pair == True:                     #test si pair est vrai 
                pair = False                     #alors pair devient faux
                nom = line                       #la variable nom contient la ligne
            else:
                pair = True                      #sinon pair devient vrai
                num = line                       #la variable num contient la ligne 
                repertoire[nom] = num            #définition du dictionnaire repertoire avec comme clé le nom et la valeur num
    return repertoire


#programme principal
fin= False
repertoire = {}                                       #définition d'une variable fin sur faux
while fin == False :                             #boucle tant que fin est faux
    choix=menu()                                 #la variable choix contient la variable reponse renvoyé dans la fonction menu
    if choix==0:
        print("fin du programme à bientôt")
        fin = True                               #fin prend la valeur vrai et le programme s'arrete   
    elif choix==1:
        ecriture()                               #appel de la fonction ecriture
    elif choix==2:
        recherche = input("Entrer 0 pour annuler ou entrer un nom pour rechercher son numéro\nVotre choix : ")
        if recherche=="0":
            print("Retour au menu")
        else:
            dico = lecture()                     #la variable dico contient le dictionnaire repertoire renvoyé dans la fonction lecture
            if recherche in dico:
                print(recherche + ": " + dico[recherche])
            else:
                print("La personne souhaité n'est pas enregistré")
                