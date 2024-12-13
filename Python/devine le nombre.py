# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:45:53 2023

@author: NSI Première
"""

# -*- coding: utf-8 -*-

def jeu():
    global reponse, reponse_ordi, indice_centre, indice_debut, indice_fin, trouve, compteur
    print("Proposition de l'ordinateur : ",reponse_ordi)
    while trouve==False:  
        reponse=input("répondre : \n+\n-\n=\n:")
        print("reponse : ", reponse)
        if reponse == "+":
            indice_debut = indice_centre + 1
        elif reponse == "-":
            indice_fin = indice_centre - 1
        elif reponse == "=":
            trouve = True
            compteur -= 1
        else:
            print("vous vous êtes trompé\n")
            compteur -= 1
        compteur += 1
        indice_centre = (indice_debut+indice_fin)//2
        reponse_ordi = tab[indice_centre]
        print("Proposition de l'ordinateur : ",reponse_ordi)
        if trouve == True:
            print("Lordinateur a utilisé ",compteur," coups pour trouver le nombre caché !")
            print("L'élément caché est :", reponse_ordi)
        
tab=[x for x in range(101)]		# création d'un tableau de 101 valeurs (de 0 à 100)
reponse = ""			# déclaration d'une variable de type texte qui contiendra le texte entré par le joueur
indice_debut=0			# premier indice du tableau à analyser
indice_fin=len(tab)-1		# dernier indice du tableau à analyser
indice_centre=(indice_fin+indice_debut)//2 		# calcul de l'indice du milieu
reponse_ordi = tab[indice_centre]			# valeur du tableau d'indice du milieu (le même que l'indice ici)
compteur=0					# initialisation d'un compteur
trouve=False					# variable indiquant quand le nombre a été trouvé

jeu()						# appel à la fonction jeu()