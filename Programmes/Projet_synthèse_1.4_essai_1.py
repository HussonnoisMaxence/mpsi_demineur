#Attention à ne pas utiliser d'accents dans le programme
#Avant de lancer le programme, installer le dossier Projet_Python sur votre bureau svp (c'est temporaire mais ça a le mérite de fonctionner sans être trop chiant)
#Pour lancer le programme utiliser la fonction mise_en_place_plateau(niveau) avec 1,2 ou 3 comme niveau
#Bonne channce pour la lecture!

#PS: On va vous broyer au prochain TP de Physique


#Dossier source: indiquer son emplacement
Dossier_source='C:\\Users\\Jeremy\\Desktop\\Projet_Demineur'


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 
from os import chdir
import random



##      PARTIE MISE EN PLACE PLATEAU DE JEU


def amenagement_Dossier_source(Dossier_source):
    global Dossier_source_images, Dossier_source_scores
    Dossier_source_images=Dossier_source+'\\Images'
    Dossier_source_scores=Dossier_source+'\\Scores'
    
    
    
def chargement_images(Dossier_source_images):
    global gris, drapeau, mine_fond_blanc
    chdir(Dossier_source_images)
    fond=mpimg.imread('Gris.png')
    drapeau=mpimg.imread('Drapeau.png')
    mine_fond_blanc=mpimg.imread('Mine_fond_blanc.png')
    for k in range(0,10):
        'image_chiffre_'+str(k)=mpimg.imread('Case_chiffre_'+str(k)+'.png')


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
    plt.imshow(gris,extent=(0,colonnes,0,lignes))



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
    global tableau_gestion_plateau
    tableau_gestion_plateau=np.zeros((lignes+2,colonnes+2),int)
    for k in coordonnees_des_mines:
        tableau_gestion_plateau[k[0],k[1]]=10
        for i in range(int(k[0])-1,int(k[0])+2):
            for j in range(int(k[1])-1,int(k[1])+2):
                tableau_gestion_plateau[i,j]+=1
    for k in range(0,lignes+2):
        tableau_gestion_plateau[k,0]=100
        tableau_gestion_plateau[k,colonnes+1]=100
    for k in range(0,colonnes+2):
        tableau_gestion_plateau[0,k]=100  
        tableau_gestion_plateau[lignes+1,k]=100      #On a rempli le tableau avec les nombres qui devront apparaître sur la grille de demineur, où un indice >10 représente une mine et un indice >99 represente un bordure
    
    
def creation_tableau_devoilement_cases(lignes,colonnes):        #Si une case a été dévoilée son numéro vaut 0, si il y a un drapeau son numero vaut 2, sinon son drapeau son numero vaut 1       
    global tableau_devoilement_cases
    tableau_devoilement_cases=np.ones((lignes+2,colonnes+2),int)
    for k in range(0,lignes+2):         #Toujours 100 pour les bordures
        tableau_devoilement_cases[k,0]=100
        tableau_devoilement_cases[k,colonnes+1]=100
    for k in range(0,colonnes+2):
        tableau_devoilement_cases[0,k]=100  
        tableau_devoilement_cases[lignes+1,k]=100
    global nombre_cases_masquees
    nombre_cases_masquees=lignes*colonnes
    
   
   
def mise_en_place_plateau_depart(niveau):       #Synthèse de ttes les fns precedentes
    global figure1
    figure1=plt.figure()
    amenagement_Dossier_source(Dossier_source)
    donnees_niveau_actuel=equivalence_niveau(niveau)
    affichage_grille(lignes,colonnes)
    affichage_fond(lignes,colonnes)
    creation_coordonnees_des_mines_aleatoirement(colonnes,lignes,nombre_de_mines)
    creation_tableau_devoilement_cases(lignes,colonnes)
    creation_tableau_gestion_plateau(lignes,colonnes,coordonnees_des_mines)
    plt.axis('scaled')      #(ortho)normage des axes
    plt.axis([-0.5,colonnes+0.5,-0.5,lignes+0.5])       #Zoom sur le plateau
    plt.ion()       #active l'interactivité, essentiel avant plt.show() pour pouvoir supperposer les images
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
    
    if 0<xdata<colonnes and 0<ydata<lignes and (button==1 or button==3):     #Si le"clic" est dans la grille et est bien un clic...
        figure1.canvas.mpl_disconnect(reaction_souris)      #On stoppe la réaction à la souris
        global Donnees_clic
        Donnees_clic=[xdata,ydata,button]       #Et on stocke les coordonnées et le numéro du bouton
        gestion_donnees_clic_souris(Donnees_clic)
    else:
        plateau_interactif()        #Sinon on relance l'aquisition du clic souris
        
        

def gestion_donnees_clic_souris(Donnees_clic):
    colonne_du_clic=int(Donnees_clic[0]+1)
    ligne_du_clic=int(lignes+1-Donnees_clic[1])
    global Donnees_clic_arrangees
    Donnees_clic_arrangees=[ligne_du_clic,colonne_du_clic,button]
    if button==3:
        afficher_drapeau(Donnees_clic_arrangees[:2])
    elif tableau_devoilement_cases[ligne_du_clic,colonne_du_clic]!=0:
        devoilement_plateau(Donnees_clic_arrangees[:2])
        


def afficher_drapeau(position_drapeau):
    chdir(Dossier_source_images)
    drapeau=mpimg.imread('Drapeau.png')
    gris=mpimg.imread('Gris.png')
    abs=position_drapeau[1]-1
    ord=lignes-position_drapeau[0]
    if tableau_devoilement_cases[position_drapeau[0],position_drapeau[1]]==2:
        plt.imshow(gris,extent=(abs,abs+1,ord,ord+1))
        tableau_devoilement_cases[position_drapeau[0],position_drapeau[1]]=1
    elif tableau_devoilement_cases[position_drapeau[0],position_drapeau[1]]==1:
        plt.imshow(drapeau,extent=(abs+0.2,abs+0.8,ord,ord+0.85))
        tableau_devoilement_cases[position_drapeau[0],position_drapeau[1]]=2
    plateau_interactif()



def devoilement_plateau(position_clic_droit):
    if 9<tableau_gestion_plateau[position_clic_droit[0],position_clic_droit[1]]<20:
        afficher_mines(coordonnees_des_mines)
    else:
        ligne_de_la_case=position_clic_droit[0]
        colonne_de_la_case=position_clic_droit[1]
        afficher_case(ligne_de_la_case,colonne_de_la_case)
    plateau_interactif()



def afficher_case(ligne_de_la_case,colonne_de_la_case):
    chiffre_case=tableau_gestion_plateau[ligne_de_la_case,colonne_de_la_case]
    chdir(Dossier_source_images)    
    abs=colonne_de_la_case-1
    ord=lignes-ligne_de_la_case
    plt.imshow('image_chiffre_'+str(chiffre_case),extent=(abs,abs+1,ord,ord+1))
    tableau_devoilement_cases[ligne_de_la_case,colonne_de_la_case]=0
    if tableau_gestion_plateau[ligne_de_la_case-1,colonne_de_la_case]<10:
        afficher_case(ligne_de_la_case-1,colonne_de_la_case)
    if tableau_gestion_plateau[ligne_de_la_case,colonne_de_la_case-1]<10:
        afficher_case(ligne_de_la_case,colonne_de_la_case-1)
    if tableau_gestion_plateau[ligne_de_la_case+1,colonne_de_la_case]<10:
        afficher_case(ligne_de_la_case+1,colonne_de_la_case)
    if tableau_gestion_plateau[ligne_de_la_case,colonne_de_la_case+1]<10:
        afficher_case(ligne_de_la_case,colonne_de_la_case+1)
    # if tableau_gestion_plateau[ligne_de_la_case-1,colonne_de_la_case]==0:
    #     afficher_case(ligne_de_la_case-1,colonne_de_la_case)
    # if tableau_gestion_plateau[ligne_de_la_case,colonne_de_la_case-1]==0:
    #     afficher_case(ligne_de_la_case,colonne_de_la_case-1)
    # if tableau_gestion_plateau[ligne_de_la_case+1,colonne_de_la_case]==0:
    #     afficher_case(ligne_de_la_case+1,colonne_de_la_case)
    # if tableau_gestion_plateau[ligne_de_la_case,colonne_de_la_case+1]==0:
    #     afficher_case(ligne_de_la_case,colonne_de_la_case+1)
    plateau_interactif()
    
 
        
def afficher_mines(position_mines):
    chdir(Dossier_source_images)
    mine_fond_blanc=mpimg.imread('Mine_contour_blanc.png')
    for mine in position_mines:
        chdir(Dossier_source_images)
        mine_fond_blanc=mpimg.imread('Mine_contour_blanc.png')
        abs=mine[1]-1
        ord=lignes-mine[0]
        if tableau_devoilement_cases[mine[0],mine[1]]==1:
            plt.imshow(mine_fond_blanc,extent=(abs,abs+1,ord,ord+1))
            tableau_devoilement_cases[mine[0],mine[1]]=0
    