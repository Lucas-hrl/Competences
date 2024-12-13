#***************************************************
#Fonction traitement du store SOMFY V52
#***************************************************

#import des modules***************************************************
from machine import Pin     #import du module broche
import time                 #import du module time

#Nomination et parametrage des broches******************************************

#En entrees numeriques*****************************
E_BPM=Pin(12,Pin.IN,Pin.PULL_DOWN) #Declaration d'une entree E_BPM sur la broche 12 du micro(D2 de la carte)
E_BPD=Pin(13,Pin.IN,Pin.PULL_DOWN) #Declaration d'une entree E_BPD sur la broche 13 du micro(D3 de la carte)
E_FDCH=Pin(14,Pin.IN,Pin.PULL_DOWN) #Declaration d'une entree E_FDCH sur la broche 12 du micro(D4 de la carte)
E_FDCB=Pin(15,Pin.IN,Pin.PULL_DOWN) #Declaration d'une entree E_FDCB sur la broche 12 du micro(D5 de la carte)
#En entrees analogiques ***************************

#En sorties numeriques****************************
S_LV=Pin(2,Pin.OUT)              #Declaration d'une sortie S_ledV sur la broche 2 du micro(D8 de la carte)
S_LR=Pin(17,Pin.OUT)             #Declaration d'une sortie S_ledR sur la broche 17 du micro(D7 de la carte)
#*********************************************************
# Programmme principal
#*********************************************************
while True:
  if ((E_BPM.value()==0)&(E_BPD.value()==0)):            # Si BPM inactif et BPD inactif
    
  










