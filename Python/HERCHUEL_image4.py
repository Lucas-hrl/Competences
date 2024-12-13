# -*- coding: utf-8 -*-
"""
Created on Fri Jul 04 15:38:25 2014
@author: raul
"""

from PIL import Image

# ouverture d’une image au format pgm binaire :
imageSource=Image.open("1-arbre_bin.pgm")
# remarque : imageSource est un nom de variable, vous pouvez mettre un autre nom à la place .
# sa largeur et sa hauteur en pixels :
largeur , hauteur=imageSource.size
# ouverture d’une nouvelle image
# pour l’option "L", voir http://www.pythonware.com/library/pil/handbook/concepts.htm
# et pour Image.new( ), voir http://www.pythonware.com/library/pil/handbook/image.htm
imageFin=Image.new("L",(largeur,hauteur))
# remarque : imageFin est un nom de variable, vous pouvez mettre un autre nom à la place .
def filtre2():
    for y in range(hauteur):               #parcourt les pixels en  hauteur un par un
        for x in range(largeur):           #parcourt les pixels en  largeur un par un
            p= imageSource.getpixel((x,y)) #définition d'une variable p contenant le pixel récupéré de l'image source
            p2= 100*(p-128)        #calcul du nouveau pixel
            imageFin.putpixel((x,y),p2)    #placement du nouveau pixel sur la nouvelle image à la même hauteur et largeur que sur la première



filtre2()

    




# sauvegarde de l ’image créée :
imageFin.save("1-test_bin_InversionAvecPil.pgm")
imageSource.show()
# on montre l ’image :
imageFin.show()