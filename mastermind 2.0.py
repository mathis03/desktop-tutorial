import random

compteur_chances=0

print("Ce jeu est un Mastermind on a remplacé les couleurs par des lettres")
print("")
print("Quelques renseignements:")
print("Les lettres doivent être enregistrées en majuscules")
print("O= lettre appartenant à la liste mais mal placée")
print("X= lettre appartenant à la liste et bien placée")
print("faux= lettre n'appartenant pas à la liste")
print("")
print("Tu as une possibilité de 8 lettres: A B C D E F G H")
print("")

nombre_chiffre_codes=int(input("combien de chiffres doit avoir le code?"))
code=[random.choice(['A','B','C','D','E','F','G','H']) for i in range (nombre_chiffre_codes)]
chances=int(input("combien de chances aurez vous pour deviner le code?"))





while compteur_chances<chances:
    compteur_chances=compteur_chances+1
    reponse=[input("faites votre proposition")]
    print (reponse)
    

