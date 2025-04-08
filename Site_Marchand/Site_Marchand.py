#Programme réalisé par BOUKLIKHA Mohamed-Amine => PC : 5
from tkinter import*

#Creation de la fenetre
fenetre=Tk()
fenetre.title('BOUKLIKHA Mohamed-Amine')
fenetre.config(width=1100, height=620, bg='white')

#Bannière du site:
Base = Canvas(fenetre,width=1110, height=620, bg='white')
Base.create_line(0,0,1300,0,fill="black",width=200)                    #Pour faire la base du site
Base.place(x=-3,y=-3)

#Importation du et placement du logo du site
Logo = PhotoImage(file='Logo_Montre.png')
Base.create_image(100,50,image=Logo)

#Importation des Icones du haut pour le décor de l'Accueil, S'inscrire, panier ...
Accueil = PhotoImage(file='Accueil.png')
Base.create_image(350,30,image=Accueil)

icone_inscrire = PhotoImage(file='Inscrire.png')
Base.create_image(560,30,image=icone_inscrire)

icone_connexion = PhotoImage(file='Connexion.png')
Base.create_image(770,30,image=icone_connexion)

icone_panier = PhotoImage(file='Panier.png')
Base.create_image(955,25,image=icone_panier)

Affiche = PhotoImage(file='Affiche.png')
Base.create_image(875,360,image=Affiche)


############################################################

#Importation et placement des images des produits à vendre

#Montre1
M1 = Canvas(fenetre,width=190, height=220, bg='white')
M1.place(x=20,y=115)
Montre1 = PhotoImage(file='Montre1.png')
M1.create_image(90,86,image=Montre1)
M1.create_line(0,160,200,160,fill="grey",width=2)                              #Séparer l'image du prix,Titre et bouton
M1.create_text(72,175,text='Montre Silicone :',font=('arial',13,'bold'))
M1.create_text(24,200,text='200 €',font=('times',11,'bold'))


#Montre2
M2 = Canvas(fenetre,width=190, height=220, bg='white')
M2.place(x=230,y=115)
Montre2 = PhotoImage(file='Montre2.png')
M2.create_image(90,85,image=Montre2)
M2.create_line(0,160,200,160,fill="grey",width=2)
M2.create_text(70,175,text='Montre Argent :',font=('arial',13,'bold'))
M2.create_text(26,200,text='300 €',font=('times',11,'bold'))

#Montre3
M3 = Canvas(fenetre,width=190, height=220, bg='white')
M3.place(x=440,y=115)
Montre3 = PhotoImage(file='Montre3.png')
M3.create_image(90,85,image=Montre3)
M3.create_line(0,160,200,160,fill="grey",width=2)
M3.create_text(95,175,text='Montre Argent-Beige :',font=('arial',13,'bold'))
M3.create_text(26,200,text='400 €',font=('times',11,'bold'))

#Montre4
M4 = Canvas(fenetre,width=190, height=220, bg='white')
M4.place(x=20,y=380)
Montre4 = PhotoImage(file='Montre4.png')
M4.create_image(90,85,image=Montre4)
M4.create_line(0,160,200,160,fill="grey",width=2)
M4.create_text(60,175,text='Montre Noir : ',font=('arial',13,'bold'))
M4.create_text(25,200,text='600 €',font=('times',11,'bold'))

#Montre5
M5 = Canvas(fenetre,width=190, height=220, bg='white')
M5.place(x= 230,y=380)
Montre5 = PhotoImage(file='Montre5.png')
M5.create_image(90,85,image=Montre5)
M5.create_line(0,160,200,160,fill="grey",width=2)
M5.create_text(53,175,text='Montre Or :',font=('arial',13,'bold'))
M5.create_text(26,200,text='800 €',font=('times',11,'bold'))

#Montre6
M6 = Canvas(fenetre,width=190, height=220, bg='white')
M6.place(x=440,y=380)
Montre6 = PhotoImage(file='Montre6.png')
M6.create_image(90,85,image=Montre6)
M6.create_line(0,160,200,160,fill="grey",width=2)
M6.create_text(90,175,text='Montre Or-Noir Pro :',font=('arial',13,'bold'))
M6.create_text(30,200,text='1000 €',font=('times',11,'bold'))


###############################################
#Fonction pour revenir sur la page d'Accueil
def accueil():
    Inscription.place_forget()                               #Supprime le canvas de l'inscription pour revenir sur l'accueil
    Connexion.place_forget()                                 #Supprime le canvas de la connexion pour revenir sur l'accueil
    Panier.place_forget()                                    #Supprime le canvas du panier pour revenir sur l'accueil
    Payement.place_forget()
    Interface_CB.place_forget()
B1 = Button(fenetre,text="ACCUEIL",command=accueil)
B1.place(x=320,y=60)

#######################################################

#Pour s'inscrire
Inscription = Canvas(fenetre,width=650, height=450, bg='grey')
titre_id = Label(Inscription,text='INSCRIPTION',font=('arial',15,'bold'))
Login = Entry(Inscription)
id = Label(Inscription, text='Choisissez un Identifiant : ', bg='grey', font=('times', 10, 'bold'))
md = Label(Inscription, text='Choisissez un Mot de Passe : ', bg='grey', font=('times', 10, 'bold'))
mdp = Entry(Inscription,show='*')                                #(show) Pour cacher et remplacer le mot de passe par le caractère '*

#Fonction pour afficher la page d'inscription
def inscrire():
    Inscription.place(x=223,y=120)                          #placement du canvas de la page
    titre_id.place(x=264,y=30)                              #placement du titre "Inscription"
    id.place(x=257,y=118)                                   #placement du label pour indiquer de choisir un Login
    Login.place(x=264,y=150)                                #placement de l'entry pour le Login

    md.place(x=248,y=220)                                   #placement du label pour indiquer de choisir un mdp
    mdp.place(x=264,y=250)                                  #placement de l'entry pour le mdp

#Fonction qui supprime toutes les indications et entry de l'inscription et affiche la bienvenue au client
def RecuperationLogin():
    titre_id.place_forget()
    Login.place_forget()
    id.place_forget()
    md.place_forget()
    mdp.place_forget()
    ReponseUtilisateur=Login.get()                                      #Recupere le Login crée par le client
    Inscription.create_text(280,190,text='Bienvenue   ' + ReponseUtilisateur ,font=('times',30,'bold'))              #Texte de Bienvenue au client accompagnée de son Login crée
    Confirmer1.place_forget()

#Bouton pour confirmer l'inscription
Confirmer1 = Button(Inscription,text="Confirmer",bg='green', font=('times',10,'bold'),command=RecuperationLogin)
Confirmer1.place(x=290,y=320)
Confirmer1.config(width= 9, height=2)

#Pour supprimer le canvas de l'inscription à l'aide du petite croix rouge
def inscription_delete():
    Inscription.place_forget()

#Boutons de l'icone s'inscrire ainsi que la croix pour fermer la page inscription
B2 = Button(fenetre,text="S'INSCRIRE",command=inscrire)
B2.place(x=520,y=60)
B3 = Button(Inscription,text="x",command=inscription_delete)
B3.place(x=621,y=2)
B3.config(bg='red',fg='white',width=3,height=0,font=('ARIAL',8,'bold'))


##################################################################

#Pour se connecter:
Connexion = Canvas(fenetre, width=650, height=450, bg='grey')
titre_id_2 = Label(Connexion, text='SE CONNECTER', font=('arial', 15, 'bold'))
id_2 = Label(Connexion, text='Identifiant : ', bg='grey', font=('times', 10, 'bold'))
Login_2 = Entry(Connexion)
md_2 = Label(Connexion, text='Mot de Passe : ', bg='grey', font=('times', 10, 'bold'))
mdp_2 = Entry(Connexion,show='*')                                        #(show) Pour cacher et remplacer le mot de passe par le caractère '*

#Fonction pour afficher la page d'inscription
def connexion():
    Connexion.place(x=223,y=120)                               #placement du canvas de la page
    titre_id_2.place(x=250, y=30)                              #placement du titre "SE CONNECTER"
    id_2.place(x=290, y=118)                                   #placement du label pour indiquer de choisir un Login
    Login_2.place(x=264, y=150)                                #placement de l'entry pour le Login

    md_2.place(x=287, y=220)                                   #placement du label pour indiquer de choisir un mdp
    mdp_2.place(x=264, y=250)                                  #placement de l'entry pour le mdp



Confirmer2 = Button(Connexion,text="Confirmer",bg='green', font=('times',10,'bold'))
Confirmer2.place(x=290,y=320)
Confirmer2.config(width= 9, height=2)

#Pour supprimer le canvas de la connexion à l'aide du petite croix rouge
def connexion_delete():
    Connexion.place_forget()

#Boutons de l'icone se connecter ainsi que la croix pour fermer la page connexion
B3 = Button(fenetre,text="SE CONNECTER",command=connexion)
B3.place(x=720,y=60)
B4 = Button(Connexion,text="x",command=connexion_delete)
B4.place(x=621,y=2)
B4.config(bg='red',fg='white',width=3,height=0,font=('ARIAL',8,'bold'))

###########################################################################

#Panier

#Creation du Canvas du Panier
Panier = Canvas(fenetre, width=1110, height=550, bg='white')

#Fonction pour aller sur la page du panier à partir du bouton et de l'icone panier
def panier():
    Panier.place(x=0,y=97)
    titre_id = Label(Panier,text='PANIER',font=('arial',15,'bold'))
    titre_id.place(x=360,y=30)
    Payement.place_forget()
    Interface_CB.place_forget()

B5 = Button(fenetre,text="PANIER",command=panier)
B5.place(x=930,y=60)

#Canvas pour decrire le site
message_canvas = Canvas(Panier,width=370,height=620,bg='black')
message_canvas.place(x=730,y=-2)
message = Label(message_canvas,text='QUI SOMMES NOUS ?',fg='black',bg='white',font=('Verdana',10,'bold'))
message.place(x=20,y=20)
message2 = Label(message_canvas,text="Nous expédions partout dans le monde.",fg='white',bg='black',font=('Verdana',10,'bold'))
message2.place(x=20,y=80)
message3 = Label(message_canvas,text="Il faut environ 5-7 jours ouvrables après votre \n commande  jusqu'à ce que votre produit arrive.",fg='white',bg='black',font=('Verdana',10,'bold'))
message3.place(x=20,y=110)
message4 = Label(message_canvas,text="L'expédition vers la France prend environ 2 à 3 \njours ouvrables.",fg='white',bg='black',font=('Verdana',10,'bold'))
message4.place(x=20,y=160)
message5 = Label(message_canvas,text="Non, nos montres ne sont pas disponibles sur \n Amazon !",fg='white',bg='black',font=('Verdana',10,'bold'))
message5.place(x=20,y=200)
message6 = Label(message_canvas,text="Vous pouvez joindre L'équipe MB Watch : \n au 06 34 76 23 45 !",fg='gold',bg='black',font=('Verdana',10,'bold'))
message6.place(x=20,y=300)

############################################################################""

# Créez une zone de texte pour afficher le contenu du panier
zone_panier = Canvas(Panier, width=665, height=380,bg='lightgrey')
zone_panier.place(x=30, y=70)

# Créez une liste vide pour le panier
panier = []

# Fonction pour mettre à jour le prix total a payer
def actualisation_du_prix_total():
    global prix_total
    prix_total = 0
    for i in panier:
        prix_total = prix_total + i['prix_total']
    afficher_articles()

# Fonction pour ajouter un article au panier avec une certaine quantité
def ajouter_au_panier(nom, prix, quantite):
    global prix_total
    article_existant = False

    for i in panier:                                           # Recherchez si l'article est déjà dans le panier
        if i['nom'] == nom:
            i['quantite'] = i['quantite'] + quantite
            i['prix_total'] =  i['prix_total'] + prix * quantite
            article_existant = True


    if not article_existant:                                   # Ajoutez l'article si il n'est pas déjà dans le panier
        panier.append({"nom": nom, "prix_unitaire": prix, "quantite": quantite, "prix_total": prix * quantite})

    actualisation_du_prix_total()


# Fonction pour ajouter les articles au fur et à mesure
def afficher_articles():
    zone_panier.delete('all')                 # Effacez tout le contenu précédent enregistrer de la zone_panier
    y = 20
    for article in panier:
        zone_panier.create_text(190, y,text=" • " + article['nom'] + " - Prix : " + str(article['prix_unitaire']) +"€ - Quantité : " + str(article['quantite']) + " - Total : " +str(article['prix_total']) + "€")
        y = y + 20

    # Affichez le prix total à Payer
    zone_panier.create_text(570, 360, text="Prix Total à Payer : " + str(prix_total) + "€", font=("Arial", 10, "bold"))


#Fonction pour retrirer un artcile du panier   (J'ai essayé mais ne fonctionne pas)
'''def supprimer_article():
    global prix_total
    # Soustrayez le prix total de l'article supprimé du prix total général

    # Supprimez l'article du panier

    # Mettez à jour l'affichage des articles
    afficher_articles()

BR = Button(Panier, text='RETOUR', fg='white', bg='green', font=('Arial', 8, 'bold'),command=supprimer_article)
BR.place(x=460,y=190)'''


# Fonction pour ajouter Montre1 au panier
def ajouter_montre1_au_panier():
    ajouter_au_panier("Montre Silicone", 200, 1)

# Fonction pour ajouter Montre2 au panier
def ajouter_montre2_au_panier():
    ajouter_au_panier("Montre Argent", 300, 1)

# Fonction pour ajouter Montre3 au panier
def ajouter_montre3_au_panier():
    ajouter_au_panier("Montre Argent-Beige", 400, 1)

# Fonction pour ajouter Montre4 au panier
def ajouter_montre4_au_panier():
    ajouter_au_panier("Montre Noir", 600, 1)

# Fonction pour ajouter Montre6 au panier
def ajouter_montre5_au_panier():
    ajouter_au_panier("Montre Or", 800, 1)

# Fonction pour ajouter Montre6 au panier
def ajouter_montre6_au_panier():
    ajouter_au_panier("Montre Or-Noir-Pro", 1000, 1)


#Tout les Boutons de chaque montre pour ajouter au panier
B1 = Button(M1, text='AJOUTER AU PANIER', fg='white', bg='green', font=('Arial', 8, 'bold'),command=ajouter_montre1_au_panier)
B1.place(x=60,y=190)
B2 = Button(M2, text='AJOUTER AU PANIER',fg='white',bg='green',font=('Arial',8,'bold'),command=ajouter_montre2_au_panier)
B2.place(x=60,y=190)
B3 = Button(M3, text='AJOUTER AU PANIER',fg='white',bg='green',font=('Arial',8,'bold'),command=ajouter_montre3_au_panier)
B3.place(x=60,y=190)
B4 = Button(M4, text='AJOUTER AU PANIER',fg='white',bg='green',font=('Arial',8,'bold'),command=ajouter_montre4_au_panier)
B4.place(x=60,y=190)
B5 = Button(M5, text='AJOUTER AU PANIER',fg='white',bg='green',font=('Arial',8,'bold'),command=ajouter_montre5_au_panier)
B5.place(x=60,y=190)
B6 = Button(M6, text='AJOUTER AU PANIER',fg='white',bg='green',font=('Arial',8,'bold'),command=ajouter_montre6_au_panier)
B6.place(x=60,y=190)


#Payer

#Creation du Canvas du Panier
Payement = Canvas(fenetre, width=1110, height=550, bg='skyblue')
Interface_CB = Canvas(fenetre, width=310, height=450, bg='white')
PE = Label(Interface_CB,text='PAYER EN LIGNE',fg='white',bg='black',font=('arial',15,'bold'))
Nom = Label(Interface_CB,text='Nom sur la carte',bg='white',font=('arial',10,'bold'))
Nom_entry = Entry(Interface_CB)
CB = Label(Interface_CB, text='N° de carte ',bg='white', font=('times', 10, 'bold'))
CB_entry = Entry(Interface_CB,width=40)
Date = Label(Interface_CB, text="Date d'expiration ",bg='white', font=('times', 10, 'bold'))
Date_entry = Entry(Interface_CB,width=10)
Crypto = Label(Interface_CB, text="Date d'expiration ",bg='white', font=('times', 10, 'bold'))
Crypto_entry = Entry(Interface_CB,width=8)

def payer():
    Payement.place(x=0,y=97)
    Interface_CB.place(x=70,y=130)
    PE.place(x=20,y=20)
    Nom.place(x=20,y=100)
    Nom_entry.place(x=20, y=130)
    CB.place(x=20, y=200)
    CB_entry.place(x=20, y=230)
    Date.place(x=20, y=300)
    Date_entry.place(x=20, y=330)
    Crypto.place(x=180, y=300)
    Crypto_entry.place(x=180, y=330)


Payer = Button(zone_panier, text='PASSER LA COMMANDE',fg='white',bg='green',font=('Arial',8,'bold'),height=2,command=payer)
Payer.place(x=500,y=290)

def payement_final():
    accepte = Label(Payement, text=" Payement Accepté ",bg='skyblue',fg='green', font=('times', 20, 'bold'))
    accepte.place(x=600,y=180)
    livraison = Label(Payement, text=" Votre colis sera livré dans les prochain jours ",bg='skyblue',fg='black', font=('times', 12, 'bold'))
    livraison.place(x=570,y=220)

B7 = Button(Interface_CB, text='PAYER',fg='white',bg='blue',font=('Arial',8,'bold'),height=2,width=10,command=payement_final)
B7.place(x=70,y=380)

fenetre.mainloop()







