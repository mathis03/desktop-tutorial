# Variables
aligne=False
joueur=1
tableau=[[" " for j in range(7)] for i in range(6)]

# Fonctions
def Demander_Colonne():
    colonne=int(input("Dans quelle colonne voulez-vous mettre votre jeton ? ")) # il faut protéger pour ne mettre que des int et ne pas prendre en compte les autres possibilités
    return colonne
    
def Mettre_Jeton(colonne, joueur, tableau):
    i=5
    while tableau[i][colonne-1]!=" ":
        i=i-1
    if joueur==1:
        tableau[i][colonne-1]="X"
    else:
        tableau[i][colonne-1]="O"
    ligne=i
    return ligne

def Afficher_Tableau(tableau):
    for i in range(6):
        print(tableau[i])

def Tester_Alignement(tableau, ligne, colonne, joueur):
    ligne_joue=ligne
    # test alignement vertical
    compteur=1
    while ligne < 5 and tableau[ligne][colonne-1]==tableau[ligne+1][colonne-1]:
        compteur=compteur+1
        ligne=ligne+1
    if compteur==4:
        return True
    
    # test alignement horizontal
    
    compteur=1
    colonne_joue=colonne
    while colonne>1 and tableau[ligne][colonne-1]==tableau[ligne][colonne-2]:
        compteur=compteur+1
        colonne=colonne-1
        
        
    ligne=ligne_joue    
    colonne=colonne_joue    
    while colonne<7 and tableau[ligne][colonne-1]==tableau[ligne][colonne]:
        compteur=compteur+1
        colonne=colonne+1
        
        
    if compteur>=4:
        return True
    
    #test alignement diagonale gauche et droite
     compteur=1
    colonne_joue=colonne
    while colonne>1  and tableau[ligne][colonne-1]==tableau[ligne][colonne-2]:
        compteur=compteur+1
        colonne=colonne-1
        
        
    ligne=ligne_joue    
    colonne=colonne_joue    
    while colonne<7 and tableau[ligne][colonne-1]==tableau[ligne][colonne]:
        compteur=compteur+1
        colonne=colonne+1
        
        
    if compteur>=4:
        return True
    
    
    
def Changer_Joueur(joueur):
    if joueur==1:
        joueur=2
    else:
        joueur=1
    return joueur

def Afficher_Vainqueur(joueur):
    print("Bravo : ",joueur)
#######################
# Programme principal #
#######################
Afficher_Tableau(tableau)

while not aligne :
    colonne=Demander_Colonne()
    
    ligne=Mettre_Jeton(colonne, joueur, tableau)
    
    Afficher_Tableau(tableau)
    
    aligne=Tester_Alignement(tableau, ligne, colonne, joueur)
    
    joueur=Changer_Joueur(joueur)

Afficher_Vainqueur(joueur)
  
