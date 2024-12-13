# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:25:44 2023

@author: NSI Première
"""

def recherche(element,liste):
    trouve=False
    indice_debut=0
    indice_fin=(len(liste))-1
    while trouve==False and indice_debut<=indice_fin:
        indice_centre= (indice_debut+indice_fin)//2
        if liste[indice_centre]== element:
            trouve=True
        else:
            if element>liste[indice_centre]:
                indice_debut=indice_centre+1
            else:
                indice_fin=indice_centre-1
    return trouve
    
def nb_de_tour(n):
    k=0
    while 2**k<n:
        k=k+1
    return k


    
liste=[x for x in range (1,101)]
element=5
nombre_tour=nb_de_tour(len(liste))
print(nombre_tour)
rech= recherche(element,liste)
if rech==False:
    print("l'élément ne fait pas partie du tableau")
else:
    print("il se trouve bien dans le tableau")