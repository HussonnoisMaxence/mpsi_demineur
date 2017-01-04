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
import time


## ACCUEIL JEU       

def menu_accueil():
    figure1.clf()
    #On paramètre ensuite l'affichage:
    figure1.subplots_adjust(top=0.95, bottom=0.05, right=0.95, left=0.05)
    figure1.patch.set_facecolor((1,1,1,1))
    plt.axis('off')
    plt.imshow(accueil_demineur)
    lecture_records()   
    reaction_souris = figure1.canvas.mpl_connect('button_press_event', onclick)
    plt.waitforbuttonpress(-1)
    if type(abscisse_clic)==np.float64 and type(ordonnee_clic)==np.float64 and 530<abscisse_clic<1110 and 472<ordonnee_clic<706 and bouton==1 :  
        figure1.canvas.mpl_disconnect(reaction_souris)
        return choix_niveau()
    elif type(abscisse_clic)==np.float64 and type(ordonnee_clic)==np.float64 and 626<abscisse_clic<990 and 812<ordonnee_clic<969 and bouton==1 :     
        figure1.canvas.mpl_disconnect(reaction_souris)
        affichage_records()
    else:
        return menu_accueil()



def lecture_records():
    global record_facile, record_intermediaire, record_difficile
    chdir(Dossier_source_scores)
    score_facile=open('Score_facile.txt',"r")
    record_facile=float(score_facile.readline())
    score_facile.close()
    score_intermediaire=open('Score_intermediaire.txt',"r")
    record_intermediaire=float(score_intermediaire.readline())
    score_intermediaire.close()
    score_difficile=open('Score_difficile.txt',"r")
    record_difficile=float(score_difficile.readline())
    score_difficile.close()
    
    
    
def affichage_records():
    figure1.clf()
    plt.axis([0,6,0,50])
    plt.axis('off')
    plt.text(3, 25,'FACILE:\n'+str(record_facile)+' s'+'\n\nINTERMEDIAIRE:\n'+str(record_intermediaire)+' s'+'\n\nDIFFICILE:\n'+str(record_difficile)+' s', fontsize=30, horizontalalignment='center', verticalalignment='center')
    plt.waitforbuttonpress(-1)
    return menu_accueil()


def choix_niveau():
    figure1.clf()
    plt.axis('off')
    plt.imshow(image_choix_niveau) 
    global niveau
    reaction_souris = figure1.canvas.mpl_connect('button_press_event', onclick)
    plt.waitforbuttonpress(-1)
    if type(abscisse_clic)==np.float64 and type(ordonnee_clic)==np.float64 and 673<abscisse_clic<969 and 496<ordonnee_clic<596 and bouton==1 :  
        figure1.canvas.mpl_disconnect(reaction_souris)

        niveau=1
        return mise_en_place_plateau_depart(1)
    elif type(abscisse_clic)==np.float64 and type(ordonnee_clic)==np.float64 and 589<abscisse_clic<1049 and 649<ordonnee_clic<762 and bouton==1 :     
        figure1.canvas.mpl_disconnect(reaction_souris)
        niveau=2
        return mise_en_place_plateau_depart(2)
    elif type(abscisse_clic)==np.float64 and type(ordonnee_clic)==np.float64 and 663<abscisse_clic<979 and 789<ordonnee_clic<906 and bouton==1 :  
        figure1.canvas.mpl_disconnect(reaction_souris)
        niveau=3
        return mise_en_place_plateau_depart(3)
    else:
        return choix_niveau()
        
        
        
def amenagement_Dossier_source(Dossier_source):
    global Dossier_source_images, Dossier_source_scores
    Dossier_source_images=Dossier_source+'\\Images'
    Dossier_source_scores=Dossier_source+'\\Scores'
    
    
    
def chargement_images(Dossier_source_images):
    global accueil_demineur, image_choix_niveau, gris, drapeau, drapeau_reussi, image_mine, liste_images_chiffres, image_chiffre_0, image_chiffre_1, image_chiffre_2, image_chiffre_3, image_chiffre_4, image_chiffre_5, image_chiffre_6, image_chiffre_7, image_chiffre_8, image_chiffre_9, liste_images_course, course_1, course_2, course_3, course_4, course_5, course_6, course_v_1, course_v_2, course_v_3, course_v_4, course_v_5, course_v_6, course_v_7, course_v_8, course_d_1
    chdir(Dossier_source_images)
    accueil_demineur = plt.imread("Accueil_Demineur.png")
    image_choix_niveau = plt.imread("Menu_Choix_Niveau.png")
    gris=mpimg.imread('Gris.png')
    drapeau=mpimg.imread('Drapeau.png')
    drapeau_reussi=mpimg.imread('Drapeau_reussi.png')
    image_mine=mpimg.imread('Mine.png')
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
    liste_images_course=[course_1, course_2, course_3, course_4, course_5, course_6, course_v_1, course_v_2, course_v_3, course_v_4, course_v_5, course_v_6, course_v_7, course_v_8]

    
    
def jeu():
    global figure1, axe
    figure1, axe=plt.subplots()
    amenagement_Dossier_source(Dossier_source)
    chargement_images(Dossier_source_images)
    return menu_accueil()



##      PARTIE MISE EN PLACE PLATEAU DE JEU

        
def equivalence_niveau(niveau):
    donnees_niveau=[[9,9,10,record_facile],[16,16,40,record_intermediaire],[16,30,99,record_difficile]]    #liste contenant les infos sur la taille et le nb de mines de chaque niveau
    donnees_niveau_actuel = donnees_niveau[niveau-1]
    global lignes,colonnes,nombre_de_mines,record      #global rend la vaiable "definie tt le tps"
    lignes=donnees_niveau_actuel[0]
    colonnes=donnees_niveau_actuel[1]
    nombre_de_mines=donnees_niveau_actuel[2]
    record=donnees_niveau_actuel[3]
    
    
    
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
    for k in range(0,lignes+2):        #Toujours 100 pour les bordures
        tableau_devoilement_cases[k,0]=100
        tableau_devoilement_cases[k,colonnes+1]=100
    for k in range(0,colonnes+2):
        tableau_devoilement_cases[0,k]=100
        tableau_devoilement_cases[lignes+1,k]=100
    
   
   
def mise_en_place_plateau_depart(niveau):       #Synthèse de ttes les fns precedentes
    figure1.clf()
    equivalence_niveau(niveau)
    affichage_grille(lignes,colonnes)
    affichage_fond(lignes,colonnes)
    creation_coordonnees_des_mines_aleatoirement(colonnes,lignes,nombre_de_mines)
    creation_tableau_devoilement_cases(lignes,colonnes)
    creation_tableau_gestion_plateau(lignes,colonnes,coordonnees_des_mines)
    global nombre_cases_masquees
    nombre_cases_masquees=lignes*colonnes
    plt.axis('scaled')      #(ortho)normage des axes
    plt.axis([0,colonnes,0,lignes])       #Zoom sur le plateau
    plt.ion()  #active l'interactivité, essentiel avant plt.show() pour pouvoir supperposer les images
    plt.axis('off')
    plt.show()
    global debutTemps
    debutTemps = 0
    return plateau_interactif()    #Totalement fonctionnel lorsque la fn plateau_interactif sera achevée   EFFECTUE LA TRANSITION VERS LA PARTIE INTERACTIVE
 
    
##     FIN PARTIE MISE EN PLACE DU PLATEAU DE JEU
 
 
 
##     DEBUT PARTIE INTERACTIVE    


def onclick(event):     #fonction qui renvoie les coordonnées et le numero du bouton du click souris    #clic droit=1, clic roulette=2, clic gauche=3
    global abscisse_clic, ordonnee_clic, bouton
    abscisse_clic, ordonnee_clic, bouton = event.xdata, event.ydata, int(event.button)
  
        
        
def plateau_interactif(): 
    if nombre_cases_masquees>nombre_de_mines:
        reaction_souris=figure1.canvas.mpl_connect('button_press_event', onclick)   #active la réaction à la souris
        
        plt.waitforbuttonpress(timeout=-1)      #Met le programme en pause jusqu'à ce qu'un bouton soit enfoncé
        global debutTemps
        if type(abscisse_clic)==np.float64 and type(ordonnee_clic)==np.float64 and 0<abscisse_clic<colonnes and 0<ordonnee_clic<lignes and (bouton==1 or bouton==3):     #Si le"clic" est dans la grille et est bien un clic...
            if debutTemps==0:
                debutTemps = time.time()
            figure1.canvas.mpl_disconnect(reaction_souris)      #On stoppe la réaction à la souris
            global Donnees_clic
            Donnees_clic=[abscisse_clic, ordonnee_clic, bouton]       #Et on stocke les coordonnées et le numéro du bouton
            return gestion_donnees_clic_souris(Donnees_clic)
        else:
            return plateau_interactif()        #Sinon on relance l'aquisition du clic souris
    else:
        return victoire(True)
    


def afficher_temps(debutTemps):
    global t
    t = int((t - debutTemps)*10)/10
    plt.axis([0,6,0,4])
    plt.axis('off')
    plt.text(3, 2,'TEMPS:\n\n'+str(t)+' s', fontsize=50, horizontalalignment='center', verticalalignment='center')




def gestion_donnees_clic_souris(Donnees_clic):
    colonne_du_clic=int(Donnees_clic[0]+1)
    ligne_du_clic=int(lignes+1-Donnees_clic[1])
    global Donnees_clic_arrangees
    Donnees_clic_arrangees=[ligne_du_clic,colonne_du_clic,bouton]
    if bouton==3:
        return afficher_drapeau(Donnees_clic_arrangees[:2])
    elif tableau_devoilement_cases[ligne_du_clic,colonne_du_clic]==1:
        return devoilement_plateau(Donnees_clic_arrangees[:2])
    return plateau_interactif()


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
    return plateau_interactif()



def devoilement_plateau(position_clic_droit):
    if 9<tableau_gestion_plateau[position_clic_droit[0],position_clic_droit[1]]<20:
        return afficher_mines(coordonnees_des_mines)
    else:
        return devoilement_cases([position_clic_droit])
    return plateau_interactif()



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
    return plateau_interactif()
    
 
        
def afficher_mines(position_mines):
    for mine in position_mines:
        abs=mine[1]-1
        ord=lignes-mine[0]
        if tableau_devoilement_cases[mine[0],mine[1]]==1:
            plt.imshow(image_mine,extent=(abs,abs+1,ord,ord+1))
            tableau_devoilement_cases[mine[0],mine[1]]=0
        if tableau_devoilement_cases[mine[0],mine[1]]==2:
            plt.imshow(drapeau_reussi,extent=(abs+0.2,abs+0.8,ord,ord+0.85))
    return victoire(False)


    
def victoire(victoire):
    global t
    t=time.time()
    if victoire==True:
        for mine in coordonnees_des_mines:
            abs=mine[1]-1
            ord=lignes-mine[0]
            plt.imshow(drapeau_reussi,extent=(abs+0.2,abs+0.8,ord,ord+0.85))
        figure1.patch.set_facecolor((0.05,0.88,0.05,1))
    else:        
        figure1.patch.set_facecolor((0.88,0.05,0.05,1))
    plt.waitforbuttonpress(-1)
    plt.clf()
    figure1.subplots_adjust(top=1, bottom=0, right=1, left=0)
    figure1.patch.set_facecolor((1,1,1,1))
    for k in range(5):
        plt.axis('off')
        plt.imshow(course_1, alpha=1)
        plt.pause(0.05)
        plt.clf()
        plt.axis('off')
        plt.imshow(course_2, alpha=1)
        plt.pause(0.05)
        plt.clf()
    for k in liste_images_course[2:6]:
        plt.axis('off')
        plt.imshow(k, alpha=1)
        plt.pause(0.05)
        plt.clf()
    if victoire==True: 
        for k in liste_images_course[6:14]:
            plt.clf()
            plt.axis('off')
            plt.imshow(k, alpha=1)
            plt.pause(0.05)
            
        plt.waitforbuttonpress(-1)       
        plt.clf()
        afficher_temps(debutTemps)
        plt.waitforbuttonpress(-1)
        plt.clf()
        edition_record()
        return menu_accueil()
    else:
        plt.axis('off')
        plt.imshow(course_d_1, alpha=1)
        plt.waitforbuttonpress(-1)
        plt.clf() 
        return menu_accueil()   
        
        
def edition_record():
    if t<record:
        plt.axis([0,6,0,4])
        plt.axis('off')
        plt.text(3, 2,'NOUVEAU\nRECORD\n\nFELICITATIONS', fontsize=50, horizontalalignment='center', verticalalignment='center', color='r')
        chdir(Dossier_source_scores)
        if niveau==1:
            score_facile=open('Score_facile.txt',"w")
            score_facile.write(str(t))
            score_facile.close()
        if niveau==2:
            score_intermediaire=open('Score_intermediaire.txt',"w")
            score_intermediaire.write(str(t))
            score_intermediaire.close()
        if niveau==3:
            score_difficile=open('Score_difficile.txt',"w")
            score_difficile.write(str(t))
            score_difficile.close()
        plt.waitforbuttonpress(-1)
        plt.clf()   
            
            
            
            
