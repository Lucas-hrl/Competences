'''*******************************************************************************
*** Programme de TU Vivarium_V1
******************************************************************************'''

'''************************************************
L'entete
****************************************************************'''

#Importation des packages de methodes
import esp_rgb_lcd_grove    #import des methodes lcd BackLight
import time                 #import des methodes de pause
from machine import Pin, ADC     #impirt des methodes de broches et ADC

#Creation de l'objet lcd de LCD I2C BackLight
lcd = esp_rgb_lcd_grove.esp_afficheur_lcd()

#Initialisation de l'afficheur
lcd.__init__()
lcd.color(0, 255, 0)
lcd.clear()
time.sleep_ms(10)
lcd.setCursor(0,0)
lcd.write("REGULATION")
lcd.setCursor(0,1)
lcd.write("DE TEMPERATURE")
time.sleep(2)

# Creation des objets entrees analogiques
E_Cons = ADC(Pin(36))               # Creation de l'objet E_Cons comme etant la patte 39 de l'esp en entree analogique (S1 de la carte)
E_Cons.atten(ADC.ATTN_11DB)         # Application de la methode attenuation 11dB pour lire une tension entre 0 et 3.6V
E_Temp = ADC(Pin(39))               # Creation de l'objet E_Cons comme etant la patte 32 de l'esp en entree analogique (S1 de la carte)
E_Temp.atten(ADC.ATTN_11DB)         # Application de la methode attenuation 11dB pour lire une tension entre 0 et 3.6V

# Creation des objets sorties
S_Chauf=Pin(13,Pin.OUT)



# declarations des variables globales
V_Cons=0.0
V_Temp=0.0
V_Chauf=False

'''****************************************************************
Les fonctions
****************************************************************'''
def acq_consigne():
  global V_Cons
  print("acquisition consigne-------------------")
  time.sleep_ms(100)
  # declaration des variables locales
  V_Ncons=0     # V_Ncons represente le nombre issu de la conversion
  V_Vcons=0.0   # V_Vcons represente la tension a l'entrée du convertisseur
  
  # acquisition de la consigne de temperature
  V_Ncons=E_Cons.read()       #acquisition de nombre issu de la conversion
  print("le nombre issu de la conversion =",V_Ncons)
  time.sleep_ms(100)
  V_Vcons=V_Ncons*3.3/4095    #calcul de la tension a l'entree du convertisseur
  print("la tension sur la broche E_Cons =",V_Vcons," Volts")
  time.sleep_ms(100)
  V_Cons=(V_Vcons*20/3.3)+15  #Transformation de la tension du potentiometre en consigne en degres
  print("La consigne de temperature est de ",V_Cons," degres")
  time.sleep_ms(10)
 
 
def acq_temperature():
  global V_Temp
  print("temperature----------------------")
  time.sleep_ms(100)
  # declaration des variables locales
  V_Ntemp=0     # V_Ntemp represente le nombre issu de la conversion
  V_Vtemp=0.0   # V_Vtemp represente la tension 脿 l'entr茅e du convertisseur
  
  # acquisition de la temperature
  V_Ntemp=E_Temp.read()       #acquisition de nombre issu de la conversion
  print("le nombre issu de la conversion =",V_Ntemp)
  time.sleep_ms(100)
  V_Vtemp=V_Ntemp*3.3/4095    #calcul de la tension a l'entree du convertisseur
  print("la tension sur la broche E_Temp =",V_Vtemp," Volts")
  time.sleep_ms(100)
  V_Temp=(V_Vtemp-2.73)/0.01  #Transformation de la tension du potentiometre en consigne en degres
  print("La consigne de temperature est de ",V_Temp," degres")
  time.sleep_ms(10)
  

def traitement():
  global V_Cons
  global V_Temp
  global V_Chauf
  print("traitement------------------------")
  if V_Cons > V_Temp: #Compare la consigne et la température
    V_Chauf = True #Met la variable à True si il faut chauffer
    print("Il faut chauffer")
  else:
    V_Chauf = False #Met la variable à False si il ne faut pas chauffer
    print("Il ne faut pas chauffer")
  time.sleep_ms(10)
  
def com_utilisateur():
  global V_Cons
  global V_Temp
  print("utilisateur-----------------------")
  #Affichage de la temp et de la consigne
  lcd.clear()
  time.sleep_ms(10)
  lcd.setCursor(0,0)
  lcd.write("Consigne: ")      
  lcd.write(V_Cons)
  lcd.setCursor(0,1)
  lcd.write("Temp: ")
  lcd.write(V_Temp)
  time.sleep(2)
  time.sleep_ms(10)
  
  
def com_energie():
  global V_Chauf
  print("energie---------------------------")
  if V_Chauf == True: #Allume la led si la variable est True
    S_Chauf(1)
  else:
    S_Chauf(0)
  time.sleep_ms(10)
  
  
''' ************************************************************
Le corps du programme
*************************************************************'''

while True:
  acq_consigne()
  acq_temperature()
  traitement()
  com_utilisateur()
  com_energie()
  time.sleep(1)
  
  
  









