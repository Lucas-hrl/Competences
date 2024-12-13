# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:45:54 2024

@author: lherchuel
"""

# -*- coding: utf-8 -*-

   
def trifusion(l):
    if len(l)>1:
        a=len(l)//2
        b=len(l)
        ld=l[0:a] #on coupe en 2
        lg=l[a:b]
        
        trifusion(ld) # on recoupe tant que len(l)>1 la liste de droite
        trifusion(lg) # on recoupe tant que len(l)>1 la liste de gauche
        ig=0
        id=0
        il=0
        while ig<len(lg) and id<len(ld): #On range convenablement les 1er
            if lg[ig]<ld[id]:
                l[il]=lg[ig]
                #♀print("lg11: ",lg)
                ig+=1
            else:
                l[il]=ld[id]
                #print("ld11: ",ld)
                id+=1
            il+=1
        while id<len(ld): #puis ceux qui restent (la liste etant deja classee)
            l[il]=ld[id]
            #print("ld12: ",ld)
            id+=1
            il+=1
            
        while ig<len(lg):
            l[il]=lg[ig]
            #print("lg12: ",lg)
            ig+=1
            il+=1


L = [57,2,4,6,5]
print("liste départ:",L)
trifusion(L)
print("affichage de la liste triee :")
print(L)