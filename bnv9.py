from tkinter import *
import tkinter as tk
from PIL import Image #pour les images
from PIL import ImageTk
import threading #pour le timer
import random
import json #pour la labgye
from threading import Thread #pour le timer
from time import sleep #pour le timer

dlangue = json.load(open('langue/fr.json'))

root=Tk()

#Fenêtre
largeur = 1920 #largeur de la fenêtre
hauteur = 1080 #hauteur de la fenêtre

cnv = Canvas(root, width=largeur, height=hauteur, bg='ivory')
pdr = "cours" #pack de ressource

instant = "menu" #pour dire au programme à quel moment du jeu il en est c'est pour les bind en bas

croicle = [] #croix/carrés du joueur 1
croicle2 = [] #croix/carrés du joueur 2

#Paramètres de la grille et de la feuille
cote = 10 #taille côté de la grille, 10 c'est la taille réglementaire
tour = 0

#Création des images nécessaires pour le menu
sfeuille = ImageTk.PhotoImage(Image.open(pdr+"/feuille.png"))
sentoure = ImageTk.PhotoImage(Image.open(pdr+"/entoure.png"))
spas_entoure = ImageTk.PhotoImage(Image.open(pdr+"/pas_entoure.png"))
posourisx2 = 0
posourisy2 = 0

global grillex, grilley, taille_marge, marge, milieu, tc, car, car2, car3, car4, car5, car6, car7, car8, car9, case, case2, case3, case4, case5, case6, case7, case8, case9, croix_rouge, croix_noir, cercle, cercle_rouge, carre, selectj, selectr, ligner, ligner2, ligner3, ligner4, ligner5, ligner6, ligner7, ligner8, lignev, lignev2, lignev3, lignev4, lignev5, lignev6, lignev7, lignev8, bat5, bat4, bat3, bat2, horizontale, position_valide, porte_avion, croiseur, contre_torpilleur, torpilleur, types_bateaux
tc = (int)(hauteur/(cote+3)) #taille des carreaux
taille_marge = hauteur/2 #largeur de la marge
marge = (int)((largeur-(taille_marge))/tc)*tc #coordonnée x ou y de la marge selon l'orientation de la grille
if ((int)(marge/tc)%2==1 and cote%2==0):
    marge = marge -tc
if ((int)(marge/tc)%2==0 and cote%2==1):
    marge = marge -tc
milieu = marge/2 #milieu de la largeur de la feuille EN NE COMPTANT PAS LA MARGE


grillex = milieu-((cote/2)*tc) #x du haut gauche de la grille
grilley = tc #y du haut gauche de la grille

#Création des images
#pour les carreaux
car = ImageTk.PhotoImage(Image.open(pdr+"/carreau.png").resize((tc, tc)))
car2 = ImageTk.PhotoImage(Image.open(pdr+"/carreau2.png").resize((tc, tc)))
car3 = ImageTk.PhotoImage(Image.open(pdr+"/carreau3.png").resize((tc, tc)))
car4 = ImageTk.PhotoImage(Image.open(pdr+"/carreau4.png").resize((tc, tc)))
car5 = ImageTk.PhotoImage(Image.open(pdr+"/carreau5.png").resize((tc, tc)))
car6 = ImageTk.PhotoImage(Image.open(pdr+"/carreau6.png").resize((tc, tc)))
car7 = ImageTk.PhotoImage(Image.open(pdr+"/carreau7.png").resize((tc, tc)))
car8 = ImageTk.PhotoImage(Image.open(pdr+"/carreau8.png").resize((tc, tc)))
car9 = ImageTk.PhotoImage(Image.open(pdr+"/carreau9.png").resize((tc, tc)))
#pour les cases
case = ImageTk.PhotoImage(Image.open(pdr+"/case.png").resize((tc, tc)))
case2 = ImageTk.PhotoImage(Image.open(pdr+"/case2.png").resize((tc, tc)))
case3 = ImageTk.PhotoImage(Image.open(pdr+"/case3.png").resize((tc, tc)))
case4 = ImageTk.PhotoImage(Image.open(pdr+"/case4.png").resize((tc, tc)))
case5 = ImageTk.PhotoImage(Image.open(pdr+"/case5.png").resize((tc, tc)))
case6 = ImageTk.PhotoImage(Image.open(pdr+"/case6.png").resize((tc, tc)))
case7 = ImageTk.PhotoImage(Image.open(pdr+"/case7.png").resize((tc, tc)))
case8 = ImageTk.PhotoImage(Image.open(pdr+"/case8.png").resize((tc, tc)))
case9 = ImageTk.PhotoImage(Image.open(pdr+"/case9.png").resize((tc, tc)))
#croix/cercle
croix_rouge = ImageTk.PhotoImage(Image.open(pdr+"/croix.png").resize((tc, tc)))
croix_noir = ImageTk.PhotoImage(Image.open(pdr+"/croixn.png").resize((tc, tc)))
cercle_bleu = ImageTk.PhotoImage(Image.open(pdr+"/cercle.png").resize((tc, tc)))
cercle_rouge = ImageTk.PhotoImage(Image.open(pdr+"/dercle.png").resize((tc, tc)))
carre = ImageTk.PhotoImage(Image.open(pdr+"/carre.png").resize((tc, tc)))
selectj = ImageTk.PhotoImage(Image.open(pdr+"/selectj.png").resize((tc, tc)))
selectr = ImageTk.PhotoImage(Image.open(pdr+"/selectr.png").resize((tc, tc)))
#ligne
ligner = ImageTk.PhotoImage(Image.open(pdr+"/ligner.png").resize((tc, tc)))
ligner2 = ImageTk.PhotoImage(Image.open(pdr+"/ligner2.png").resize((tc, tc)))
ligner3 = ImageTk.PhotoImage(Image.open(pdr+"/ligner3.png").resize((tc, tc)))
ligner4 = ImageTk.PhotoImage(Image.open(pdr+"/ligner2.png").resize((tc, tc)).rotate(180))
ligner5 = ImageTk.PhotoImage(Image.open(pdr+"/ligner.png").resize((tc, tc)).rotate(90))
ligner6 = ImageTk.PhotoImage(Image.open(pdr+"/ligner2.png").resize((tc, tc)).rotate(90))
ligner7 = ImageTk.PhotoImage(Image.open(pdr+"/ligner3.png").resize((tc, tc)).rotate(90))
ligner8 = ImageTk.PhotoImage(Image.open(pdr+"/ligner2.png").resize((tc, tc)).rotate(270))
lignev = ImageTk.PhotoImage(Image.open(pdr+"/lignev.png").resize((tc, tc)))
lignev2 = ImageTk.PhotoImage(Image.open(pdr+"/lignev2.png").resize((tc, tc)))
lignev3 = ImageTk.PhotoImage(Image.open(pdr+"/lignev3.png").resize((tc, tc)))
lignev4 = ImageTk.PhotoImage(Image.open(pdr+"/lignev2.png").resize((tc, tc)).rotate(180))
lignev5 = ImageTk.PhotoImage(Image.open(pdr+"/lignev.png").resize((tc, tc)).rotate(90))
lignev6 = ImageTk.PhotoImage(Image.open(pdr+"/lignev2.png").resize((tc, tc)).rotate(90))
lignev7 = ImageTk.PhotoImage(Image.open(pdr+"/lignev3.png").resize((tc, tc)).rotate(90))
lignev8 = ImageTk.PhotoImage(Image.open(pdr+"/lignev2.png").resize((tc, tc)).rotate(270))
#Bateau
bat5 = ImageTk.PhotoImage(Image.open(pdr+"/bat5.png").resize((tc*5, tc)))
bat4 = ImageTk.PhotoImage(Image.open(pdr+"/bat4.png").resize((tc*4, tc)))
bat3 = ImageTk.PhotoImage(Image.open(pdr+"/bat3.png").resize((tc*3, tc)))
bat2 = ImageTk.PhotoImage(Image.open(pdr+"/bat2.png").resize((tc*2, tc)))
bat5b = ImageTk.PhotoImage(Image.open(pdr+"/bat5b.png").resize((tc, tc*5)))
bat4b = ImageTk.PhotoImage(Image.open(pdr+"/bat4b.png").resize((tc, tc*4)))
bat3b = ImageTk.PhotoImage(Image.open(pdr+"/bat3b.png").resize((tc, tc*3)))
bat2b = ImageTk.PhotoImage(Image.open(pdr+"/bat2b.png").resize((tc, tc*2)))
bat2big = ImageTk.PhotoImage(Image.open(pdr+"/bat2b.png").resize((tc*2, tc*4)))
bat3big = ImageTk.PhotoImage(Image.open(pdr+"/bat3b.png").resize((tc*2, tc*6)))
bat4big = ImageTk.PhotoImage(Image.open(pdr+"/bat4b.png").resize((tc*2, tc*7)))
bat5big = ImageTk.PhotoImage(Image.open(pdr+"/bat5b.png").resize((tc*2, tc*8)))
#Humain
humain_content = ImageTk.PhotoImage(Image.open(pdr+"/humain_content.png").resize((200, 200)))
humain_triste = ImageTk.PhotoImage(Image.open(pdr+"/humain_triste.png").resize((200, 200)))
#Machine
machine_content = ImageTk.PhotoImage(Image.open(pdr+"/machine_content.png").resize((200, 200)))
machine_triste = ImageTk.PhotoImage(Image.open(pdr+"/machine_triste.png").resize((200, 200)))

horizontale = False
position_valide = False

#d'accord
positionX_origin = 1400
positionY_origin = 250
positionX = 0
positionY = 0

def lancer_partie():
    global tour, tc, grillex, grilley, grille, grille2, bateau, bateau2,nbat, nbat1, nbat2, bloquer_la_grille, grille3, grille4, positionX, positionY, type_bateau, horizontale, position_valide
    grille = [[0 for i in range(cote)] for j in range(cote)] #Joueur 1, 0: rien, 1:bateau, 2: bâteau touché, 3: tir raté, 4: bateau coulé
    grille2 = [[0 for i in range(cote)] for j in range(cote)] #Joueur 2 [[x0y0, x1y0, x3y0..],[x0y1, x1y1, x2y1..]
    grille3 = [[2 for i in range(cote)] for j in range(cote)] #grille de réflexion du joueur 1, 0: bateau coulé ou 100% rien, 1: bateau touché, 2: sais pas
    grille4 = [[2 for i in range(cote)] for j in range(cote)] #grille de réflexion du joueur 2
    bateau = [0, 0,1,2,1,1] #nombre de bateaux d'une certaine longueur, minimum de deux svp [0,1,2,3,4,etc]
    bateau2 = bateau
    nbat = 0
    for i in range(len(bateau)):
        nbat = nbat + bateau[i]
    nbat1 = nbat #nombre de bateaux du joueur 1
    nbat2 = nbat #nombre de bateaux du joueur 2

    #placement aléatoire des bateaux sur la grille
    grille_bateau(grille2)

    cnv.delete("all")
    afficher_feuille()
    afficher_grille()
    #boucle pour afficher les grilles sur la console
    for i in range (cote):
        for j in range (cote):
            if (grille[j][i]!=0):
                if (grille[j][i]==1):
                    print((int)(grille[j][i]), end=" ")
                else:
                    print((int)(grille[j][i]*10-10), end=" ")
            else:
                print(grille[j][i], end=" ")
        print()
    print()
    for i in range (cote):
        for j in range (cote):
            if (grille2[j][i]!=0):
                if (grille2[j][i]==1):
                    print((int)(grille2[j][i]), end=" ")
                else:
                    print((int)(grille2[j][i]*10-10), end=" ")
            else:
                print(grille2[j][i], end=" ")
        print()
    print()

    placer_bateau()
    position_valide = False
    definir_type_bateau()

def definir_type_bateau():
    global bateau, bateau_actuel_image, type_bateau, position_valide, bateau_a_placer
    bateau_a_placer = bateau
    type_bateau = 0
    position_valide = False
    for i in range(len(bateau_a_placer)):
        if (type_bateau < bateau_a_placer[i]):
            type_bateau = i
    bateau_actuel = bat2big
    if (type_bateau == 3):
        bateau_actuel = bat3big
    elif(type_bateau == 4):
        bateau_actuel = bat4big
    elif(type_bateau == 5):
        bateau_actuel = bat5big
    if (type_bateau != 0):    
        bateau_actuel_image = cnv.create_image(positionX_origin, positionY_origin+5, anchor=NW, image=bateau_actuel)


def placer_bateau():
    global tplacer, cplacer
    tplacer = cnv.create_text((largeur/7)*6, (hauteur/8)*1, text=dlangue['cagepla'], fill="#2439B5", font=("Distrait", 80, "bold"))

def partie_commence():
    global tour, humain, machine, tbatres, tbatres2, tindication1, tindication2, expression, expression2, tbatresn, tbatresn2
    cnv.delete(tplacer)
    expression = 0 #0: heureux 1: triste
    expression2 = 0 #pareil pour le joueur 2
    humain = cnv.create_image((largeur/7)*5, (hauteur/16)*2, anchor=NW, image=humain_content)
    machine = cnv.create_image((largeur/7)*5, (hauteur/16)*10, anchor=NW, image=machine_content)
    tindication1 = cnv.create_text((largeur/7)*6, (hauteur/16)*3, text="", fill="#2439B5", font=("Distrait", 65, "bold"))
    tindication2 = cnv.create_text((largeur/7)*6, (hauteur/16)*11, text="", fill="#2439B5", font=("Distrait", 65, "bold"))
    tjoueur1 = cnv.create_text((largeur/7)*6, (hauteur/16)*1, text=dlangue['jou_eur']+" 1:", fill="#2439B5", font=("Distrait", 80, "bold"))
    tbatres = cnv.create_text((largeur/20)*14, (hauteur/16)*5, text=dlangue['batres'], fill="#161616", anchor=NW, font=("Distrait", 60, "bold"))
    tbatresn = cnv.create_text((largeur/20)*17, (hauteur/16)*6, text=nbat1, fill="#161616", anchor=NW, font=("Distrait", 65, "bold"))
    tjoueur2 = cnv.create_text((largeur/7)*6, (hauteur/16)*9, text=dlangue['jou_eur']+" 2:", fill="#2439B5", font=("Distrait", 80, "bold"))
    tbatres2 = cnv.create_text((largeur/20)*14, (hauteur/16)*13, text=dlangue['batres'], fill="#161616", anchor=NW, font=("Distrait", 60, "bold"))
    tbatresn2 = cnv.create_text((largeur/20)*17, (hauteur/16)*14, text=nbat2, fill="#161616", anchor=NW, font=("Distrait", 65, "bold"))
    tour = 1
    cnv.itemconfig(tindication1, state='hidden')
    cnv.itemconfig(tindication2, state='hidden')

#pour placer les bateaux aléatoirement sur la grille
def grille_bateau(grille):
    rx = 0
    ry = 0
    directionx = 0
    directiony = 0
    grille3 = [[0 for i in range(cote+2)] for j in range(cote+2)]
    limiteur = 0

    for i in range(len(bateau)): #longueur des bateaux à placer
        for j in range(bateau[i]): #bateaux de longueur i à placer
            boule = False
            limiteur = 0
            while(boule==False and limiteur<1000): #se répète tant que le bateau ne s'est pas placé correctement
                rx = random.randrange(cote-i+1) #le x d'une case au pif pour placer un bout du bateau
                ry = random.randrange(cote-i+1) #le y d'une case au pif pour placer un bout du bateau
                directionx = random.randrange(2) #horizontal (directionx=1) ou vertical (directiony=1)
                directiony = 1-directionx
                boule=True
                for k in range(i):
                    if (grille[ry+k*directiony][rx+k*directionx]==2):
                        boule=False
                if (boule==False):
                    limiteur = limiteur+1
            if (ry+(-1)*directiony<cote and ry+(-1)*directiony>=0 and rx+(-1)*directionx<cote and rx+(-1)*directionx>=0):
                grille[ry+(-1)*directiony][rx+(-1)*directionx] = 2
            if (ry+(i)*directiony<cote and ry+(i)*directiony>=0 and rx+(i)*directionx<cote and rx+(i)*directionx>=0):
                grille[ry+(i)*directiony][rx+(i)*directionx] = 2
            for k in range(i):
                if (ry+k*directiony-1*directionx<cote and ry+k*directiony-1*directionx>=0 and rx+k*directionx-1*directiony<cote and rx+k*directionx-1*directiony>=0):
                    grille[ry+k*directiony-1*directionx][rx+k*directionx-1*directiony]=2
            for k in range(i):
                if (ry+k*directiony+1*directionx<cote and ry+k*directiony+1*directionx>=0 and rx+k*directionx+1*directiony<cote and rx+k*directionx+1*directiony>=0):
                    grille[ry+k*directiony+1*directionx][rx+k*directionx+1*directiony]=2
            grille[ry][rx] = 1 #premier bout du bateau
            for k in range(1,i-1,1): #milieux du bateau
                grille[ry+k*directiony][rx+k*directionx] = 1
            grille[ry+(i-1)*directiony][rx+(i-1)*directionx] = 1 #fin du bateau
    for i in range(cote):
        for j in range(cote):
            if (grille[j][i]==2):
                grille[j][i]=0

def afficher_feuille():
    for i in range (((int)(hauteur/tc))+1): #de haut en bas
        for j in range (((int)(largeur/tc)), 0-1, -1): #de droite à gauche
            if (i==0):
                if (j>(int)((marge)/tc)):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car9)
                elif (j==(int)((marge)/tc)):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car8)
                else:
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car7)
            else:
                if (j>(int)((marge)/tc)):
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car3)
                elif (j==(int)((marge)/tc)):
                    print(j)
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car2)
                else:
                    cnv.create_image(j*tc, i*tc, anchor=NW, image=car)

def afficher_grille():
    global select
    select = cnv.create_image(1920, 1080, anchor=NW, image=selectj)
    #Dessin de la grille
    for i in range (cote+2): #y
        for j in range (cote+2): #x
            placementx = grillex-tc+j*tc
            placementy = grilley+-tc+i*tc
            if (i==0 and j==0):
                cnv.create_image(placementx, placementy, anchor=NW, image=case2)
            elif (i==0 and j==cote+1):
                cnv.create_image(placementx, placementy, anchor=NW, image=case4)
            elif (i==cote+1 and j==0):
                cnv.create_image(placementx, placementy, anchor=NW, image=case7)
            elif (i==cote+1 and j==cote+1):
                cnv.create_image(placementx, placementy, anchor=NW, image=case9)
            elif (i==0):
                cnv.create_image(placementx, placementy, anchor=NW, image=case3)
                cnv.create_text(placementx+tc/2, placementy+tc/2+tc/8, text=j, fill="#2439B5", font=("Distrait", tc, "bold"))
            elif (j==0):
                cnv.create_image(placementx, placementy, anchor=NW, image=case5)
                if (cote<=26):
                    cnv.create_text(placementx+tc/2, placementy+tc/2+tc/8, text=chr(i+64), fill="#2439B5", font=("Distrait", tc, "bold"))
                else:
                    cnv.create_text(placementx+tc/2-tc/3, placementy+tc/2+tc/8, text=chr((int)((i-1)/26+1+64))+chr((i-1)%26+1+64), fill="#2439B5", font=("Distrait", tc, "bold"))
            elif (j==cote+1):
                cnv.create_image(placementx, placementy, anchor=NW, image=case6)
            elif (i==cote+1):
                cnv.create_image(placementx, placementy, anchor=NW, image=case8)
            else:
                cnv.create_image(placementx, placementy, anchor=NW, image=case)



def videur(x,y,a,b,**options):
   image = Image.new('RGBA', (a-x, b-y), 0)
   images.append(ImageTk.PhotoImage(image))
   cnv.create_image(x, y, image=images[-1], anchor='nw')
   cnv.create_rectangle(x, y,a,b, **options)

def cercle(truc):
    global cnv
    cnv.itemconfig(truc, image=sentoure)

def pascercle(truc):
    global cnv
    cnv.itemconfig(truc, image=spas_entoure)

def origine(eventorigin):
      x = eventorigin.x
      y = eventorigin.y
      if (tour > 0):
          if (x>grillex and x<(grillex+cote*tc) and y>grilley and y<(grilley+cote*tc)):
              if (tour == 1 and grille2[(int)((x-grillex)/tc)][(int)((y-grilley)/tc)]!=2 and grille2[(int)((x-grillex)/tc)][(int)((y-grilley)/tc)]!=3 and grille2[(int)((x-grillex)/tc)][(int)((y-grilley)/tc)]!=4):
                  cnv.coords(select, grillex+((int)((x-grillex)/tc))*tc, grilley+((int)((y-grilley)/tc))*tc)
              else:
                  cnv.coords(select, 1920, 1080)
          else:
              cnv.coords(select, 1920, 1080)

def origine_clic(eventorigin):
      x = eventorigin.x
      y = eventorigin.y
      if (tour == 1):
          if (x>grillex and x<(grillex+cote*tc) and y>grilley and y<(grilley+cote*tc)):
              placer_croix((int)((x-grillex)/tc),(int)((y-grilley)/tc))

def placer_cercle(cx,cy):
    global grille, horizontale, type_bateau
    if (grille[cx][cy]==0):
       croicle2.append(cnv.create_image((cx+(grillex/tc))*tc, (cy+(grilley/tc))*tc, anchor=NW, image=cercle_bleu))
       grille[cx][cy] = 1

def placer_croix(cx,cy):
     global grille, grille2, tour, nbat1, nbat2, bateau, bateau2
     #print("j:",tour)
     if (tour > 0):
         if (grille2[cx][cy]>=1 and grille2[cx][cy]<2):
             croicle.append(cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=carre))
             expression2=1
             cnv.itemconfig(tindication2, text="Touché")
             grille2[cx][cy]=2
             #nbat2 = nbat2 - 1
             print(bateau2)
             bateau2 = compteur_bato(grille2,bateau2)
             print(bateau2)
             nbat2 = 0
             for i in range(len(bateau2)):
                 nbat2 = nbat2 + bateau2[i]
             if (nbat2 == 0):
                 victoire()
             else:
                 joueur2()
         elif (grille2[cx][cy]==0):
             croicle.append(cnv.create_image(grillex+cx*tc, grilley+cy*tc, anchor=NW, image=croix_rouge))
             expression2=0
             cnv.itemconfig(tindication2, text="Raté")
             #print(grillex+cx*tc, grilley+cy*tc)
             grille2[cx][cy]=3
             joueur2()

def joueur2():
     global grille, grille2, tour, nbat1, nbat2, bateau, bateau2, grille3, grille4,rx,ry
     tour = 2
     boule = False #pour savoir si l'image a pu être placée
     while (boule == False):
         ra = strat57(grille,grille4)
         rx = ra[0]
         ry = ra[1]
         if (grille[rx][ry]== 0 or grille[rx][ry]==1):
             boule = True
     if (grille[rx][ry]==1):
         grille[rx][ry]=2
         refresh()
         croicle2.append(cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=cercle_rouge))
         cnv.itemconfig(croicle2[len(croicle2)-1], state='hidden')
         expression1=1
         cnv.itemconfig(tindication1, text="Touché")
         bateau = compteur_bato(grille,bateau)
         nbat1 = 0
         for i in range(len(bateau)):
             nbat1 = nbat1 + bateau[i]
         if (nbat1 == 0):
             defaite()
     elif (grille[rx][ry]==0):
        grille[rx][ry]=3
        croicle2.append(cnv.create_image(grillex+rx*tc, grilley+ry*tc, anchor=NW, image=croix_noir))
        cnv.itemconfig(croicle2[len(croicle2)-1], state='hidden')
        expression=0
        cnv.itemconfig(tindication1, text="Raté")
     xamer = threading.Thread(target=timer)
     xamer.start()

def strat57(grille,griller): #griller: grille de réflexion
    lde3 = [] #nombre de 3 dans la grille de réflexion
    #deux liste de 2 pour faire du une case sur 2
    lde2 = [] #nombre de 2 première partie damier dans la grille de réflexion
    lde2b = [] #nombre de 2 première partie damier dans la grille de réflexion
    for i in range(cote):
        for j in range(cote):
            #collecte des données de grille par griller
            if (grille[j][i]==3): #bateau posé, raté
                griller[j][i]=0 #case éliminée
            if (grille[j][i]==4): #bateau coulé
                griller[j][i]=0 #case éliminée
                if(j-1>=0):
                    griller[j-1][i]=0
                if(i-1>=0):
                    griller[j][i-1]=0
                if(j+1<cote):
                    griller[j+1][i]=0
                if(i+1<cote):
                    griller[j][i+1]=0
            if ((grille[j][i]==2 and griller[j][i]==2) or (grille[j][i]==2 and griller[j][i]==3)): #bateau touché
                griller[j][i]=1 #case avec un nouveau bateau touché dedans
                #check les 4 cases adjacentes pour voir s'il y a un autre bateau touché
                batad = 0 #1: il y a un bateau touché adjacent horizontalement,2:verticalement
                batadx = 0 #coordonnées du bateau adjacent
                batady = 0
                if(j-1>=0):
                    if(griller[j-1][i]==4):
                        batad = 1
                        batadx = j-1
                        batady = i
                if(i-1>=0):
                    if(griller[j][i-1]==4):
                        batad = 2
                        batadx = j
                        batady = i-1
                if(j+1<cote):
                    if(griller[j+1][i]==4):
                        batad = 1
                        batadx = j+1
                        batady = i
                if(i+1<cote):
                    if(griller[j][i+1]==4):
                       batad = 2
                       batadx = j
                       batady = i+1
                #recheck les 4 cases adjacentes, et les dénomine comme possiblement détentrices de bateaux adverses
                if(j-1>=0):
                    if(griller[j-1][i]==2):
                        if (batad == 2):
                            griller[j-1][i] = 0
                            griller[batadx-1][batady] = 0
                        else:
                            griller[j-1][i] = 3
                if(i-1>=0):
                    if(griller[j][i-1]==2):
                        if (batad == 1):
                            griller[j][i-1] = 0
                            griller[batadx][batady-1] = 0
                        else:
                            griller[j][i-1] = 3
                if(j+1<cote):
                    if(griller[j+1][i]==2):
                        if (batad == 2):
                            griller[j+1][i] = 0
                            griller[batadx+1][batady] = 0
                        else:
                            griller[j+1][i] = 3
                if(i+1<cote):
                    if(griller[j][i+1]==2):
                       if (batad == 1):
                           griller[j][i+1] = 0
                           griller[batadx][batady+1] = 0
                       else:
                           griller[j][i+1] = 3
                #check en dessous/au dessus, à gauche/à droite pour un autre bateau touché
                griller[j][i]=4 #deviens un vieux bateau coulé
    for i in range(cote):
        for j in range(cote):
            if (griller[j][i]==3):
                lde3.append([j,i])
            if (griller[j][i]==2):
                if ((i+j)%2==1):
                    lde2.append([j,i])
                else:
                    lde2b.append([j,i])
    if (len(lde3)>0):
        randoma = random.randrange(len(lde3))
        rx = lde3[randoma][0]
        ry = lde3[randoma][1]
    else:
        randoma = random.randrange(len(lde2))
        rx = lde2[randoma][0]
        ry = lde2[randoma][1]
    for i in range (cote):
        for j in range (cote):
            print(grille[j][i],end=" ")
        print()
    print()
    for i in range (cote):
        for j in range (cote):
            print(griller[j][i],end=" ")
        print()
    ra = [rx,ry]
    return ra

def compteur_bato(grille, bateau): #compte le nombre de bateau
    c = 0 #compteur de bouts de bateau
    d = 0 #compteur de bouts bateau touchés
    for i in range(len(bateau)):
        bateau[i]=0
    nbat=0
    for i in range(cote): #y
        for j in range(cote): #x
            if (grille[j][i]==0 or grille[j][i]==3):
                if (c>1 and c!=d):
                    bateau[c]=bateau[c]+1
                if (c>1 and c==d):
                    bateau_mort(c,j-1,i,1,0)
                c=0
                d=0
            if (grille[j][i]==1 or grille[j][i]==2):
                c=c+1
            if (grille[j][i]==2):
                d=d+1
        if (c>1 and c!=d):
            bateau[c]=bateau[c]+1
        if (c>1 and c==d):
            bateau_mort(c,j,i,1,0)
        c=0
        d=0
    for j in range(cote): #x
        for i in range(cote): #y
            if (grille[j][i]==0 or grille[j][i]==3):
                if (c>1 and c!=d):
                    bateau[c]=bateau[c]+1
                if (c>1 and c==d):
                    bateau_mort(c,j,i-1,0,1)
                c=0
                d=0
            if (grille[j][i]==1 or grille[j][i]==2):
                c=c+1
            if (grille[j][i]==2):
                d=d+1
        if (c>1 and c!=d):
            bateau[c]=bateau[c]+1
        if (c>1 and c==d):
            bateau_mort(c,j,i,0,1)
        c=0
        d=0
    return bateau

def bateau_mort(n,rx,ry,dirx,diry):
    global grille, grille2, tour, croicle2, tbatresn, tbatresn2, nbat1, nbat2
    if (tour==1):
       cnv.itemconfig(tindication2, text="Coulé")
       nbat2=nbat2-1
       cnv.itemconfig(tbatresn2, text=nbat2)
    else:
       cnv.itemconfig(tindication1, text="Coulé")
       nbat1=nbat1-1
       cnv.itemconfig(tbatresn, text=nbat1)
    #modifie le nombre de bateaux restants
    for k in range(n):
        placx = grillex+rx*tc-k*tc*dirx
        placy = grilley+ry*tc-k*tc*diry
        if (tour == 1):
            grille2[rx-dirx*k][ry-diry*k] = 4
            if (k==0): #joueur 1 a détruit un bateau du joueur 2
                if (dirx==1):
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev4))
                else:
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev6))
            elif (k==n-1):
                if (dirx==1):
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev2))
                else:
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev8))
            else:
                if (dirx==1):
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev3))
                else:
                    croicle.append(cnv.create_image(placx, placy, anchor=NW, image=lignev7))
        if (tour == 2): #joueur 2 a détruit un bateau du joueur 1
            grille[rx-dirx*k][ry-diry*k] = 4
            nbat2 -=1
            #cnv.itemconfig(tbatresn2, text=nbat2)
            if (k==0):
                if (dirx==1):
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner4))
                else:
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner6))
            elif (k==n-1):
                if (dirx==1):
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner2))
                else:
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner8))
            else:
                if (dirx==1):
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner3))
                else:
                    croicle2.append(cnv.create_image(placx, placy, anchor=NW, image=ligner7))
            cnv.itemconfig(croicle2[len(croicle2)-1], state='hidden')

def timer():
    global tour, posourisx2, posourisy2
    if (expression2==0):
        cnv.itemconfig(machine, image=machine_content)
    else:
        cnv.itemconfig(machine, image=machine_triste)
    cnv.itemconfig(tindication2, state='normal')
    tour = 2
    sleep(1)
    cnv.itemconfig(tindication2, state='hidden')
    refreshb()
    sleep(0.05)
    refreshn()
    if (rx-posourisx2<0):
        dirx = -1
    else:
        dirx = 1
    if (ry-posourisy2<0):
        diry = -1
    else:
        diry=1
    gx=posourisx2
    gy=posourisy2
    sleep(0.2)
    rouge = cnv.create_image(grillex+posourisx2*tc, grilley+posourisy2*tc, anchor=NW, image=selectr)
    ioni = 0
    vitesse_souris = random.randrange(5)/10+0.1
    while(gx!=rx or gy!=ry):
        ioni=ioni+1
        boule = False
        if (gx==rx or gy==ry):
            if (gx==rx):
                gy = gy+diry
            else:
                gx = gx+dirx
        else:
            randoma = random.randrange(3)
            if (randoma==0):
                gx = gx+dirx
            if (randoma==1):
                gy = gy+diry
            if (randoma==2):
                gx = gx+dirx
                gy = gy+diry
        vitesse_sourisb = random.randrange(5)/10+0.1
        if (vitesse_sourisb<vitesse_souris):
            vitesse_souris = vitesse_sourisb
        sleep(vitesse_souris)
        cnv.delete(rouge)
        rouge = cnv.create_image(grillex+gx*tc, grilley+gy*tc, anchor=NW, image=selectr)


    posourisx2=rx
    posourisy2=ry
    for i in range(len(croicle2)):
        cnv.itemconfig(croicle2[len(croicle2)-1], state='normal')
    cnv.delete(rouge)

    cnv.itemconfig(tindication1, state='normal')

    if (expression==0):
        cnv.itemconfig(humain, image=humain_content)
    else:
        cnv.itemconfig(humain, image=humain_triste)

    sleep(0.1)
    tour = 1
    refreshb()
    sleep(0.4)

    cnv.itemconfig(tindication1, state='hidden')

    cnv.itemconfig(tindication1, text="")
    refreshn()

#pour recharger la feuille
def refresh():
    for i in range(len(croicle)):
        if (tour == 1):
            cnv.itemconfig(croicle[i], state='normal')
        if (tour == 2):
            cnv.itemconfig(croicle[i], state='hidden')
    for i in range(len(croicle2)):
        if (tour == 1):
            cnv.itemconfig(croicle2[i], state='hidden')
        if (tour == 2):
            cnv.itemconfig(croicle2[i], state='normal')

def refreshb():
    for i in range(len(croicle)):
        if (tour == 2):
            cnv.itemconfig(croicle[i], state='hidden')
    for i in range(len(croicle2)):
        if (tour == 1):
            cnv.itemconfig(croicle2[i], state='hidden')

def refreshn():
    for i in range(len(croicle)):
        if (tour == 1):
            cnv.itemconfig(croicle[i], state='normal')
    for i in range(len(croicle2)-1):
        if (tour == 2):
            cnv.itemconfig(croicle2[i], state='normal')

def refreshn2():
    for i in range(len(croicle)):
        if (tour == 1):
            cnv.itemconfig(croicle[i], state='normal')
    for i in range(len(croicle2)):
        if (tour == 2):
            cnv.itemconfig(croicle2[i], state='normal')

def victoire():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="Bravo, tu as gagné", fill="#FFC300", font=('Distrait 100 bold'))

def defaite():
    global tour
    tour = 3
    cnv.create_text(960, 540, text="Quel dommage ! tu as perdu", fill="#00A513", font=('Distrait 200 bold'))

def glisser_deposer_gauche(event):
    global bateau_attrape, positionX, positionY, type_bateau, horizontale, position_valide, bateau_actuel_image
    cnv.delete(bateau_actuel_image)
    if (type_bateau != 0):
        if (horizontale):
            bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+".png").resize((tc*type_bateau,tc)))
        else:
            bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+"b.png").resize((tc, tc*type_bateau)))
        position(event, bateau_attrape)

#"bouge" l'image
def position(event, image):
    global position_valide, bato, positionX, positionY, horizontale, type_bateau, bateau_attrape
    if ((horizontale == True and (event.x <= grillex+tc*cote-(tc*(type_bateau-1)) and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote)) 
    or (horizontale == False and (event.x <= grillex+tc*cote and event.x >=grillex and event.y>=grilley and event.y<=grilley+tc*cote-tc*(type_bateau-1)))):
        positionX = grillex+((int)((event.x-grillex)/tc))*tc
        positionY = grilley+((int)((event.y-grilley)/tc))*tc
        position_valide = True
    else:
        positionX = event.x
        positionY = event.y
        position_valide = False
    bato = cnv.create_image(positionX, positionY, image=image,anchor=NW)

#activé par le clic droit, tourne le bateau de 90 degrés
def rotation(event):
    global horizontale, positionX, positionY, bato, type_bateau, position_valide, bateau_attrape, bateau_actuel_image
    cnv.delete(bateau_actuel_image)
    horizontale = not horizontale
        
    if (type_bateau != 0):
        if (horizontale):
            bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+".png").resize((tc*type_bateau,tc)))
        else:
            bateau_attrape = ImageTk.PhotoImage(Image.open(pdr+"/bat"+str(type_bateau)+"b.png").resize((tc, tc*type_bateau)))
        bato = cnv.create_image(grillex+((int)((event.x-grillex)/tc))*tc, grilley+((int)((event.y-grilley)/tc))*tc, image=bateau_attrape, anchor=NW)

#activé quand le clic gauche est relâché
def valide(event):
    global tour, position_valide, positionX, positionY, type_bateau, horizontale, bato, grillex, grilley, bateau_actuel_image
    if (position_valide==True and type_bateau!=0):
        for i in range(type_bateau):
            if ((horizontale and (grille[int((positionX-grillex)/tc)+i][int((positionY-grilley)/tc)]!=0 or (int((positionY-grilley)/tc)+1 <= cote-1 and grille[int((positionX-grillex)/tc)+i][int((positionY-grilley)/tc)+1] != 0) or grille[int((positionX-grillex)/tc)+i][int((positionY-grilley)/tc)-1] != 0 or (int((positionX-grillex)/tc)+i+1 <=cote-1 and grille[int((positionX-grillex)/tc)+i+1][int((positionY-grilley)/tc)]!=0) or grille[int((positionX-grillex)/tc)+i-1][int((positionY-grilley)/tc)]!=0)) 
            or (not(horizontale) and (grille[int((positionX-grillex)/tc)][int((positionY-grilley)/tc)+i]!=0 or (int((positionX-grillex)/tc)+1 <= cote-1 and grille[int((positionX-grillex)/tc)+1][int((positionY-grilley)/tc)+i] !=0) or grille[int((positionX-grillex)/tc)-1][int((positionY-grilley)/tc)+i] !=0 or (int((positionY-grilley)/tc)+i+1 <=cote-1 and grille[int((positionX-grillex)/tc)][int((positionY-grilley)/tc)+i+1]!=0) or grille[int((positionX-grillex)/tc)][int((positionY-grilley)/tc)+i-1]!=0))):
                position_valide=False
        if position_valide :
            bateau_a_placer[type_bateau] -=1
            for i in range(type_bateau):
                if horizontale:
                    placer_cercle(int((positionX-grillex)/tc)+i, int((positionY-grilley)/tc)) 
                else:
                    placer_cercle(int((positionX-grillex)/tc), int((positionY-grilley)/tc)+i)
                cnv.delete(bato)
                cnv.delete(bateau_actuel_image)
                definir_type_bateau()
            horizontale = False
        if (type_bateau == 0):
            partie_commence()
            refresh()
            
lancer_partie()
root.bind('<Motion>', origine) #détecte le mouvement de la souris
root.bind("<Button 1>",origine_clic) #détecte le clic gauche
root.bind("<Button 3>",rotation)
root.bind("<B1-Motion>", glisser_deposer_gauche) #motion gauche
root.bind("<ButtonRelease-1>", valide)  
cnv.pack()
root.mainloop()