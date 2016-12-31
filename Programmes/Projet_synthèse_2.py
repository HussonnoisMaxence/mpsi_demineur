#Attention à ne pas utiliser d'accents dans le programme
#Avant de lancer le programme, installer le dossier Projet_Python sur votre bureau svp (c'est temporaire mais ça a le mérite de fonctionner sans être trop chiant)
#Pour lancer le programme utiliser la fonction mise_en_place_plateau(niveau) avec 1,2 ou 3 comme niveau
#Bonne channce pour la lecture!

#PS: On va vous broyer au prochain TP de Physique


#Dossier source: indiquer son emplacement
Dossier_source='C:\\Users\\Maxence\\Desktop\\Projet_Demineur'


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 
from os import chdir
import random
import time



## AFFICHAGE MENU DU JEU...
# fini les vacances, voila ma partie, du coup y'a qu'a taper jeu() dans la console et voila
#je remercie toute mon equipe qui m'a aidé a coder cette partie... Manu a la technique, Bruno au graphisme, et tous les autres !


def choix_niveau():
    figure1.clf()
    plt.imshow(image_choix_niveau)    
    reaction_souris = figure1.canvas.mpl_connect('button_press_event', onclick)
    plt.waitforbuttonpress(-1)
    if 673<absisse_clic<969 and 496<ordonnee_clic<596 and bouton==1 :  
        figure1.canvas.mpl_disconnect(reaction_souris)
        mise_en_place_plateau_depart(1)
    elif 589<absisse_clic<1049 and 649<ordonnee_clic<762 and bouton==1 :     
        figure1.canvas.mpl_disconnect(reaction_souris)
        mise_en_place_plateau_depart(2)
    elif 663<absisse_clic<979 and 789<ordonnee_clic<906 and bouton==1 :  
        figure1.canvas.mpl_disconnect(reaction_souris)
        mise_en_place_plateau_depart(3)
    else:
        choix_niveau()
        
        
        
def amenagement_Dossier_source(Dossier_source):
    global Dossier_source_images, Dossier_source_scores
    Dossier_source_images=Dossier_source+'\\Images'
    Dossier_source_scores=Dossier_source+'\\Scores'
    
    
    
def chargement_images(Dossier_source_images):
    global image_choix_niveau, gris, drapeau, drapeau_reussi, mine_fond_blanc, liste_images_chiffres, image_chiffre_0, image_chiffre_1, image_chiffre_2, image_chiffre_3, image_chiffre_4, image_chiffre_5, image_chiffre_6, image_chiffre_7, image_chiffre_8, image_chiffre_9, course_1, course_2, course_3, course_4, course_5, course_6, course_v_1, course_v_2, course_v_3, course_v_4, course_v_5, course_v_6, course_v_7, course_v_8, course_d_1
    chdir(Dossier_source_images)
    image_choix_niveau = plt.imread("menu_choix_niveau.png")
    gris=mpimg.imread('Gris.png')
    drapeau=mpimg.imread('Drapeau.png')
    drapeau_reussi=mpimg.imread('Drapeau_reussi.png')
    mine_fond_blanc=mpimg.imread('Mine_contour_blanc.png')
    image_chiffre_0 = mpimg.imread('Case_chiffre_0.png')
    image_chiffre_1 = mpimg.imread('Case_chiffre_1.png')
    image_chiffre_2 = mpimg.imread('Case_chiffre_2.png')
    image_chiffre_3 = mpimg.imread('Case_chiffre_3.png')
    image_chiffre_4 = mpimg.imread('Case_chiffre_4.png')
    image_chiffre_5 = mpimg.imread('Case_chiffre_5.png')
    image_chiffre_6 = mpimg.imread('Case_chiffre_6.png')
    image_chiffre_7 = mpimg.imread('Case_chiffre_7.png')
    image_chiffre_8 = mpimg.imread('Case_chiffre_8.png')
    image_chiffre_9 = mpimg.imread('Case_chiffre_9.png')
    liste_images_chiffres=[image_chiffre_0,image_chiffre_1,image_chiffre_2,image_chiffre_3,image_chiffre_4,image_chiffre_5,image_chiffre_6,image_chiffre_7,image_chiffre_8,image_chiffre_9]
    course_1 = mpimg.imread('Course_1.png')
    course_2 = mpimg.imread('Course_2.png')
    course_3 = mpimg.imread('Course_3.png')
    course_4 = mpimg.imread('Course_4.png')
    course_5 = mpimg.imread('Course_5.png')
    course_6 = mpimg.imread('Course_6.png')
    course_v_1 = mpimg.imread('Course_V_1.png')
    course_v_2 = mpimg.imread('Course_V_2.png')
    course_v_3 = mpimg.imread('Course_V_3.png')
    course_v_4 = mpimg.imread('Course_V_4.png')
    course_v_5 = mpimg.imread('Course_V_5.png')
    course_v_6 = mpimg.imread('Course_V_6.png')
    course_v_7 = mpimg.imread('Course_V_7.png')
    course_v_8 = mpimg.imread('Course_V_8.png')
    course_d_1 = mpimg.imread('Course_D_1.png')
    
    
    
def jeu():
    global figure1
    figure1=plt.figure()
    amenagement_Dossier_source(Dossier_source)
    chargement_images(Dossier_source_images)
    menu_accueil()



##      PARTIE MISE EN PLACE PLATEAU DE JEU


def equivalence_niveau(niveau):
    donnees_niveau=[[9,9,10],[16,16,40],[16,30,99]]     #liste contenant les infos sur la taille et le nb de mines de chaque niveau
    donnees_niveau_actuel = donnees_niveau[niveau-1]
    global lignes,colonnes,nombre_de_mines      #global rend la vaiable "definie tt le tps"
    lignes=donnees_niveau_actuel[0]
    colonnes=donnees_niveau_actuel[1]
    nombre_de_mines=donnees_niveau_actuel[2]
    
    
    
def affichage_grille(lignes,colonnes):        #On trace des lignes
    for k in range(colonnes+1):
        plt.plot([k,k],[0,lignes],color=(0.3,0.3,0.3,1),linewidth=4)
    for k in range(lignes+1):
        plt.plot([0,colonnes],[k,k],color=(0.3,0.3,0.3,1),linewidth=4)



def affichage_fond(lignes,colonnes):        #On affiche le fond
    plt.imshow(gris,extent=(0,colonnes,0,lignes))



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
    
   
   
def mise_en_place_plateau_depart(niveau):       #Synthèse de ttes les fns precedentes
    figure1.clf()
    donnees_niveau_actuel=equivalence_niveau(niveau)
    affichage_grille(lignes,colonnes)
    affichage_fond(lignes,colonnes)
    creation_coordonnees_des_mines_aleatoirement(colonnes,lignes,nombre_de_mines)
    creation_tableau_devoilement_cases(lignes,colonnes)
    creation_tableau_gestion_plateau(lignes,colonnes,coordonnees_des_mines)
    global nombre_cases_masquees
    nombre_cases_masquees=lignes*colonnes
    plt.axis('scaled')      #(ortho)normage des axes
    plt.axis([-0.5,colonnes+0.5,-0.5,lignes+0.5])       #Zoom sur le plateau
    plt.ion()       #active l'interactivité, essentiel avant plt.show() pour pouvoir supperposer les images
    plt.show()
    plateau_interactif()    #Totalement fonctionnel lorsque la fn plateau_interactif sera achevée   EFFECTUE LA TRANSITION VERS LA PARTIE INTERACTIVE
 
    
##     FIN PARTIE MISE EN PLACE DU PLATEAU DE JEU
 
 
 
##     DEBUT PARTIE INTERACTIVE    


def onclick(event):     #fonction qui renvoie les coordonnées et le numero du bouton du click souris    #clic droit=1, clic roulette=2, clic gauche=3
    global absisse_clic, ordonnee_clic, bouton
    absisse_clic, ordonnee_clic, bouton = event.xdata, event.ydata, int(event.button)
  
        
        
def plateau_interactif(): 
    if nombre_cases_masquees>nombre_de_mines:
        reaction_souris=figure1.canvas.mpl_connect('button_press_event', onclick)   #active la réaction à la souris
        
        plt.waitforbuttonpress(timeout=-1)      #Met le programme en pause jusqu'à ce qu'un bouton soit enfoncé
        
        if 0<absisse_clic<colonnes and 0<ordonnee_clic<lignes and (bouton==1 or bouton==3):     #Si le"clic" est dans la grille et est bien un clic...
            figure1.canvas.mpl_disconnect(reaction_souris)      #On stoppe la réaction à la souris
            global Donnees_clic
            Donnees_clic=[absisse_clic, ordonnee_clic, bouton]       #Et on stocke les coordonnées et le numéro du bouton
            gestion_donnees_clic_souris(Donnees_clic)
        else:
            plateau_interactif()        #Sinon on relance l'aquisition du clic souris
    
    victoire(True)
    

def gestion_donnees_clic_souris(Donnees_clic):
    colonne_du_clic=int(Donnees_clic[0]+1)
    ligne_du_clic=int(lignes+1-Donnees_clic[1])
    global Donnees_clic_arrangees
    Donnees_clic_arrangees=[ligne_du_clic,colonne_du_clic,bouton]
    if bouton==3:
        afficher_drapeau(Donnees_clic_arrangees[:2])
    elif tableau_devoilement_cases[ligne_du_clic,colonne_du_clic]==1:
        devoilement_plateau(Donnees_clic_arrangees[:2])
    plateau_interactif()


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
        devoilement_cases([position_clic_droit])
    plateau_interactif()



def afficher_case(ligne_de_la_case,colonne_de_la_case,chiffre_case):
    abs=colonne_de_la_case-1
    ord=lignes-ligne_de_la_case
    plt.imshow(liste_images_chiffres[chiffre_case],extent=(abs,abs+1,ord,ord+1))
    tableau_devoilement_cases[ligne_de_la_case,colonne_de_la_case]=0
    global nombre_cases_masquees
    nombre_cases_masquees-=1
    
    
    
def devoilement_cases(liste_cases_a_devoiler):    
    for k in liste_cases_a_devoiler:
        ligne_case=k[0]
        colonne_case=k[1]
        chiffre_case=tableau_gestion_plateau[k[0],k[1]]
        if 0<chiffre_case<10 and tableau_devoilement_cases[ligne_case,colonne_case]==1:
            afficher_case(ligne_case,colonne_case,chiffre_case)
        elif chiffre_case==0:
            for i in range(ligne_case-1,ligne_case+2):
                for j in range(colonne_case-1,colonne_case+2):
                    if tableau_devoilement_cases[i,j]==1 and tableau_gestion_plateau[i,j]<10:
                        afficher_case(i,j,tableau_gestion_plateau[i,j])
                        if tableau_gestion_plateau[i,j]==0:
                            liste_cases_a_devoiler+=[[i,j]]
    plateau_interactif()
    
 
        
def afficher_mines(position_mines):
    for mine in position_mines:
        abs=mine[1]-1
        ord=lignes-mine[0]
        if tableau_devoilement_cases[mine[0],mine[1]]==1:
            plt.imshow(mine_fond_blanc,extent=(abs,abs+1,ord,ord+1))
            tableau_devoilement_cases[mine[0],mine[1]]=0
        if tableau_devoilement_cases[mine[0],mine[1]]==2:
            plt.imshow(drapeau_reussi,extent=(abs+0.2,abs+0.8,ord,ord+0.85))
    victoire(False)

    
def victoire(victoire):
    global course_1,course_2
    chdir(Dossier_source_images)
    course_1=mpimg.imread('Course_1.png')
    course_2=mpimg.imread('Course_2.png')
    if victoire==True:
        for mine in coordonnees_des_mines:
            abs=mine[1]-1
            ord=lignes-mine[0]
            plt.imshow(drapeau_reussi,extent=(abs+0.2,abs+0.8,ord,ord+0.85))
    plt.show()
    plt.waitforbuttonpress(30)
    plt.clf()
    plt.axis([0,15,0,12])
    for k in range(8):
        plt.imshow(course_1,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
        plt.imshow(course_2,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
    
    plt.imshow(course_3,extent=(0,15,0,12))
    plt.pause(0.001)
    plt.clf()
    plt.imshow(course_4,extent=(0,15,0,12))
    plt.pause(0.001)
    plt.clf()
    plt.imshow(course_5,extent=(0,15,0,12))
    plt.pause(0.001)
    plt.clf()
    plt.imshow(course_6,extent=(0,15,0,12))
    plt.pause(0.001)
    plt.clf()
    if victoire==True:    
        plt.imshow(course_v_1,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
        plt.imshow(course_v_2,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
        plt.imshow(course_v_3,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
        plt.imshow(course_v_4,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
        plt.imshow(course_v_5,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
        plt.imshow(course_v_6,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
        plt.imshow(course_v_7,extent=(0,15,0,12))
        plt.pause(0.001)
        plt.clf()
        plt.imshow(course_v_8,extent=(0,15,0,12))
        plt.waitforbuttonpress(-1)
        plt.clf()
#        edition_score()
        choix_niveau()
    else:
        plt.imshow(course_d_1,extent=(0,15,0,12))
        plt.waitforbuttonpress(-1)
        plt.clf() 
#        edition_score()
        choix_niveau()   
        
        
## accueil jeu        


def menu_accueil():
    
    accueil_demineur = plt.imread("accueil_demineur.png")
    figure1.clf()
    plt.imshow(accueil_demineur)    
    reaction_souris = figure1.canvas.mpl_connect('button_press_event', onclick)
    plt.waitforbuttonpress(-1)
    if 530<absisse_clic<1110 and 472<ordonnee_clic<706 and bouton==1 :  
        figure1.canvas.mpl_disconnect(reaction_souris)
        choix_niveau()
    elif 626<absisse_clic<990 and 812<ordonnee_clic<969 and bouton==1 :     
        figure1.canvas.mpl_disconnect(reaction_souris)
        print('pas de score connard')
    else:
        menu_accueil()