#Attention à ne pas utiliser d'accents dans le programme
#Avant de lancer le programme, installer le dossier Projet_Python sur votre bureau svp (c'est temporaire mais ça a le mérite de fonctionner sans être trop chiant)
#Pour lancer le programme utiliser la fonction mise_en_place_plateau(niveau) avec 1,2 ou 3 comme niveau
#Bonne channce pour la lecture!

#PS: On va vous broyer au prochain TP de Physique

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 
from os import chdir    #Pour le moment le dossier "source" doit etre modifier dans le code ,chercher solution si elle existe
import random

##      PARTIE MISE EN PLACE PLATEAU DE JEU


def equivalence_niveau(niveau):
    donnees_niveau=[[9,9,10],[16,16,40],[16,30,99]]     #liste contenant les infos sur la taille et le nb de mines de chaque niveau
    donnees_niveau_actuel = donnees_niveau[niveau-1]
    global lignes,colonnes,nombre_de_mines      #global rend la vaiable "definie tt le tps"
    lignes=donnees_niveau_actuel[0]
    colonnes=donnees_niveau_actuel[1]
    nombre_de_mines=donnees_niveau_actuel[2]
    # return donnees_niveau_actuel
    
    
    
def affichage_grille(lignes,colonnes):        #On trace des lignes
    for k in range(colonnes+1):
        plt.plot([k,k],[0,lignes],color=(0.3,0.3,0.3,1),linewidth=4)
    for k in range(lignes+1):
        plt.plot([0,colonnes],[k,k],color=(0.3,0.3,0.3,1),linewidth=4)



def affichage_fond(lignes,colonnes):        #On affiche le fond
    chdir('C:\\Users\\Jeremy\\Desktop\\Projet_Demineur\\Images')
    fond=mpimg.imread('gros_cochon_noir.png')
    plt.imshow(fond,extent=(0,colonnes,0,lignes))



##POTENTIELLEMENT INUTILE SI LE CLICK SOURIS FONCTIONNE
# def coordonnees_apparentes(n):
#     for i in range(0,n):
#         plt.text(-0.2,i+0.3,str(n-i),horizontalalignment='right',color='r',fontsize=20)
#         plt.text(i+0.5,n+0.3,str(i),horizontalalignment='center',color='b',fontsize=20)
##



def creation_coordonnees_des_mines_aleatoirement(lignes,colonnes,nombre_de_mines):
    compteur=0
    global coordonnees_des_mines
    coordonnees_des_mines=[]
    ordonnee_limite = lignes
    abscisse_limite = colonnes
        
    while compteur < nombre_de_mines:       #boucle de creation des mines. C'est surement possible de le faire avec un for, mais je suis moins à l'aise avec     #C'est parfait comme ça
        coordonnee_de_la_mine = [random.randint(1,abscisse_limite),random.randint(1,ordonnee_limite)]         #random.randint prend un entier aléatoire entre (a,b)
        if  coordonnee_de_la_mine in coordonnees_des_mines:       #test pour ne pas avoir deux mines au même endroit
            compteur =compteur
        else:
            coordonnees_des_mines.append(coordonnee_de_la_mine)
            compteur =compteur+1
    


def creation_tableau_gestion_plateau(lignes,colonnes,coordonnees_des_mines):        #tableau pour connaître la position des mines et le nombre de mines aux alentours d'une case
   
    tableau_depart=np.zeros((lignes+2,colonnes+2),int)
    for k in coordonnees_des_mines:
        tableau_depart[k[0],k[1]]=10
        for i in range(int(k[0])-1,int(k[0])+2):
            for j in range(int(k[1])-1,int(k[1])+2):
                tableau_depart[i,j]+=1
    for k in range(0,lignes+2):
        tableau_depart[k,0]=100
        tableau_depart[k,colonnes+1]=100
    for k in range(0,colonnes+2):
        tableau_depart[0,k]=100  
        tableau_depart[lignes+1,k]=100      #On a rempli le tableau avec les nombres qui devront apparaître sur la grille de demineur, où un indice >10 représente une mine et un indice >99 represente un bordure
    
    
def creation_tableau_devoilement_cases(lignes,colonnes):        #Si une case a été dévoilée son numéro vaut 0, sinon son numero vaut 1       
    tableau_devoilement_cases=np.ones((lignes+2,colonnes+2),int)
    for k in range(0,lignes+2):         #Toujours 100 pour les bordures
        tableau_devoilement_cases[k,0]=100
        tableau_devoilement_cases[k,colonnes+1]=100
    for k in range(0,colonnes+2):
        tableau_devoilement_cases[0,k]=100  
        tableau_devoilement_cases[lignes+1,k]=100
    
    
    
def mise_en_place_plateau_depart(niveau):       #Synthèse de ttes les fns precedentes
    global figure1
    figure1=plt.figure()
    donnees_niveau_actuel=equivalence_niveau(niveau)
    affichage_grille(lignes,colonnes)
    affichage_fond(lignes,colonnes)
    creation_coordonnees_des_mines_aleatoirement(colonnes,lignes,nombre_de_mines)
    creation_tableau_devoilement_cases(lignes,colonnes)
    creation_tableau_gestion_plateau(lignes,colonnes,coordonnees_des_mines)
    plt.axis('scaled')      #(ortho)normage des axes
    plt.axis([-0.5,colonnes+0.5,-0.5,lignes+0.5])       #Zoom sur le plateau
#    plt.ion()       #active l'interactivité, essentiel avant plt.show()
    plt.show()
    plateau_interactif()    #Totalement fonctionnel lorsque la fn plateau_interactif sera achevée   EFFECTUE LA TRANSITION VERS LA PARTIE INTERACTIVE
 
    
##     FIN PARTIE MISE EN PLACE DU PLATEAU DE JEU
 
 
 
##     DEBUT PARTIE INTERACTIVE    


def onclick(event):     #fonction qui renvoie les coordonnées et le numero du bouton du click souris    #clic droit=1, clic roulette=2, clic gauche=3
        global xdata, ydata, button
        xdata, ydata, button = event.xdata, event.ydata, int(event.button)
  
        
        
def plateau_interactif(): 
    reaction_souris=figure1.canvas.mpl_connect('button_press_event', onclick)   #active la réaction à la souris
    
    plt.waitforbuttonpress(timeout=-1)      #Met le programme en pause jusqu'à ce qu'un bouton soit enfoncé
    
    if 0<xdata<colonnes and 0<ydata<lignes and (button==1 or button==3):     #Si le"clic" est dans la grille...
        figure1.canvas.mpl_disconnect(reaction_souris)      #On stoppe la réaction à la souris
        global Donnees_clic
        Donnees_clic=[xdata,ydata,button]
        print("abscisse(±colonne du clic): ", Donnees_clic[0], "   ordonnée(±12-ligne du clic): ", Donnees_clic[1], "   Numero du bouton: ", Donnees_clic[2])        #Et on retourne les coordonnées et le numéro du bouton
        gestion_donnees_clic_souris(Donnees_clic)
    else:
        plateau_interactif()        #Sinon on relance l'aquisition du clic souris
        
        

def gestion_donnees_clic_souris(Donnees_clic):
    colonne_du_clic=int(Donnees_clic[0]+1)
    ligne_du_clic=int(lignes+1-Donnees_clic[1])
    global Donnees_clic_arrangees
    Donnees_clic_arrangees=[ligne_du_clic,colonne_du_clic,button]
    print(Donnees_clic_arrangees)
    afficher_mine(ligne_du_clic,colonne_du_clic)
        
def afficher_case(ligne_de_la_case,colonne_de_la_case):
    aez
 
 
def devoilement_plateau(données_clic_arrangees):
    zdde
 
        
def afficher_mine(ligne_de_la_mine,colonne_de_la_mine):
    chdir('C:\\Users\\Jeremy\\Desktop\\Projet_Demineur\\Images')
    mine_fond_blanc=mpimg.imread('Mine_contour_blanc.png')
    abs=colonne_de_la_mine-1
    ord=lignes-ligne_de_la_mine
    plt.imshow(mine_fond_blanc,extent=(abs+0.02,abs+0.98,ord+0.02,ord+0.98))
    plateau_interactif()