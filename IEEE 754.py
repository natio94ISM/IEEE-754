#Projet développé par Nathan, Anthony et Flora (CBP)

#4.1.1:Flora
#4.1.2:Nathan
#4.1.3:Flora
#4.1.4:Anthony
#4.1.5:Anthony
#4.1.6:Anthony
#4.1.7:Flora
#4.1.8:Nathan
#4.1.9:Nathan

from math import *
def signe(nb_decimal):
  if nb_decimal >=0: 
       return "0"
  else:
      return "1"

def base10_2_entier(entier_base10): #le rôle de cette fonction est de convertir un entier décimal (x) en binaire par divisions successives de (x) par 2 jusqu'à ce que (x) == 0
    resultat = ""
    while entier_base10 != 0: #tant que l'entier en base 10 (x) n'est pas égal à 0, r prend la valeur du reste de la division de (x) par 2 et le programme recommence la division,( mais de r par 2 ) et ainsi de suite
      r = entier_base10 % 2
      resultat = str(r) + resultat #quand entier_base10 == 0, le résultat final donc sa valeur binaire, est égal à l'addition de tous les restes dans l'ordre inverse 
      entier_base10 = entier_base10 // 2

    return resultat

def calibre_gauche(chaine,nb_car): #cette fonction sert a ajouter autant de 0 à gauche qu'il faut pour que la chaine fournie atteigne la longueur demandé
    while len(chaine) != nb_car :
        chaine="0"+chaine
    return chaine

def puissance_de_deux(nb_decimal): #cette fonction renvoie la puissance de deux la plus proche de la valeur fournie. Elle doit etre superieure ou egale a la valeur demandée
    if nb_decimal<0:
        nb_decimal=-nb_decimal
    if nb_decimal==0:
        return 0
    for i in range(-128,127):
        a=2**i
        if a > nb_decimal:
            return i-1
        elif a== nb_decimal:
            return i

def base2_16(chaine_nb_base_2): #cette fonction renvoie un nombreen base binaire convertit en base hexdecimal
    pos2=len(chaine_nb_base_2) #pos1 et pos2 servent a recuperer a chaque fois un groupe de quatre nombre binaire
    pos1=pos2-4
    chaine_hexadecimale=""
    for i in range(0,(len(chaine_nb_base_2)//2)-1):
        partie_de_chaine=chaine_nb_base_2[pos1:pos2]
        pos1-=4
        pos2-=4
        nb_hexa=0
        if pos1<0:
          pos1=0
        if pos2<0:
            break
        for x in range (0,len(partie_de_chaine)):
          n=len(partie_de_chaine)-(x+1)
          a=int(partie_de_chaine[x])
          a=a*2**n
          nb_hexa+=a
        chaine_hexadecimale=str(nb_hexa)+chaine_hexadecimale
    for i in range(0,len(chaine_hexadecimale)): # cette partie convertit les nombres superieur a  9 en lettre
      chaine_hexadecimale=chaine_hexadecimale.replace("10","A")
      chaine_hexadecimale=chaine_hexadecimale.replace("11","B")
      chaine_hexadecimale=chaine_hexadecimale.replace("12","C")
      chaine_hexadecimale=chaine_hexadecimale.replace("13","D")
      chaine_hexadecimale=chaine_hexadecimale.replace("14","E")
      chaine_hexadecimale=chaine_hexadecimale.replace("15","F")
      "".join(chaine_hexadecimale)
    return chaine_hexadecimale

def base10_to_2_decimal(Float,nb_chiffres_ap_virg): #cette fonction convertit la partie decimal d'un nombre en base 10, en base 2 sur 23 bits
  partie_entiere=floor(Float)
  partie_entiere_base2=base10_2_entier(partie_entiere)
  partie_decimale=Float-partie_entiere #sur ces trois premiere ligne on cherche a retirer la partie entiere du nombre de depart
  nbdecimal_base2=""
  while True: #ici on cree une boucle "while" infinie pour repeter la convertion en base 2 
      partie_decimale=partie_decimale*2
      partie_entiere=floor(partie_decimale)
      nbdecimal_base2+=str(partie_entiere)
      partie_decimale-=partie_entiere
      if  partie_decimale==0 or len(nbdecimal_base2)>=nb_chiffres_ap_virg: #on arrete le programme quand la partie decimale est nulle ou que l'on atteint la taille demandée
          break
  nbdecimal_base2=partie_entiere_base2+nbdecimal_base2
  nbdecimal_base2=nbdecimal_base2[1:len(nbdecimal_base2)]
  return nbdecimal_base2

def calibre_droite(chaine,nb_car): #cette fonction retourne une chaine de caractere qui permet de compléter la mantisse a droite par des "0" pour qu'elle soit composé de 23 bits
  while len(chaine)<nb_car:
    chaine=chaine+"0"
  return chaine

def translate_127(nb,sens): #cette fonction sert à biaiser un nombre c'est à dire ajouter 0. Elle fait aussi l'inverse
    if sens == "+": #biaise
        assert nb <=128 and nb >=-127 #declenche un erreur si le nombre est inferieur a -127 ou superieur a 128
        return base10_2_entier(nb+127)
    elif sens == "-": #debiaise
        assert nb <=255 and nb >=0 #declenche un erreur si le nombre est inferieur a 0 ou superieur a 255
        return base10_2_entier(nb-127)
    else:
        raise AssertionError #declenche une erreur si le sens a une autre valeur que "+" ou "-"
        
def presentation_result_base2(chaine_nb_base_2):
    return chaine_nb_base_2[0]+" "+chaine_nb_base_2[0:9]+" "+chaine_nb_base_2[9:33]

def IEE754(nb): # permet de regrouper toutes les fonctions en une
  if nb==0:
      print("bit : 0 00000000 00000000000000000000000")
      print("hexadecimal : 00000000")
  else:
      signenb=signe(nb)
      if signenb=="1":
          nb=-nb
      exposant=puissance_de_deux(nb)
      exposant_base2=translate_127(exposant,"+")
      if type(nb) is float:
          nb_base2=base10_to_2_decimal(nb,50)
          exposant_base2=calibre_gauche(exposant_base2,8)
          if len(nb_base2)>=24: #cette partie sert a detecter les nombres infinis (comme 0.1)
              for i in range(23,50):
                  if nb_base2[i]=="1":
                      nb_base2=nb_base2[3:26]
                      nb_final=str(signenb)+str(exposant_base2)+str(nb_base2)
                      break
          nb_final=str(signenb)+str(exposant_base2)+str(calibre_droite(nb_base2,23))
          nb_final=nb_final[0:33]
      else:
          print()
          nb_base2=base10_2_entier(nb)
          exposant_base2=calibre_gauche(exposant_base2,8)
          nb_final=str(signenb)+str(exposant_base2)+str(calibre_droite(nb_base2[1:len(nb_base2)],23))
      print("bit : "+presentation_result_base2(nb_final))
      print("hexadecimal : "+calibre_droite(base2_16(nb_final),8))

def fonction_depart(): #permet de faire en sorte de recommencer le code si une erreur est provoquée
    try:
        print("Quel nombre_voulez vous convertir ?")
        nb=float(input())
        IEE754(nb)
        print("Voulez-vous recommencer ?")
        rep=input()
        if rep=="oui" or rep=="Oui":
            fonction_depart()
        else:
            print("Au revoir")
    except:
        print("Veuillez recommencer !")
        fonction_depart()
fonction_depart()
