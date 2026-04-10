def creer_potence(): 
    # Création d'une fenêtre 
    global fenetre, canevas, image 
    fenetre = Tk() 
    fenetre.geometry('500x610') 
    fenetre.title('Jeu du Pendu') 
    canevas = Canvas(fenetre, width = 500, height = 570) 
    canevas.pack(fill = BOTH, expand = 1) 
    canevas.create_text(0, 20, text = '', anchor = W) 
    # Affichage potence 
    image = PhotoImage(file = 'PotenceDuPendu.png') 
    canevas.create_image(0, 0, image = image, anchor = NW) 
    # Création d'un bouton "Quitter" 
    bouton_Quitter = Button(fenetre, text ='Quitter', command = fenetre.destroy) 
    # Ajout l'affichage du bouton dans la fenêtre 
    bouton_Quitter.pack() 
    # Mise à jour 
    fenetre.update() 


def inscrire(ordre):
    """ Inscris un joueur avec  son pseudo en lui affectant un score de 0
    # Précondtion : "ordre" texte indiquant en lettre l'ordre du joueur
    # Postcondition : retourne une liste contenant un pseudo (type chr) et un score (type int)"""
    pseudo = input("Saisie ton pseudo, " + ordre + " joueur ")
    joueur  = [pseudo, 0]# Crée une variable "joueur" de type liste contenant le pseudo saisi et le score initial de 0
    return joueur


def jouer_pendu(joueur_pose, joueur_cherche):
    """ Joue au pendu avec un joueur qui pose un mot à deviner et un second qui cherche
    # Précondtion : une liste par joueur contenant son pseudo (type chr) et son score (type int)
    # Postcondition : retourne un tuple de deux items (Premier item type booléen : True si gagné et False si pendu
        / Deuxième item type int : nombre d'erreurs commises """
    mot = (input(joueur_pose[0] + ", saisis ton mot à deviner : ")).lower()    # Saisie du mot à deviner par le joueur qui pose
    liste_mot_a_deviner = []        # Contiendra le mot à deviner sous forme d'une liste de caractères
    liste_mot_trouve = []           # Contiendra le mot trouvé sous forme d'une liste de caractères

    for lettre in mot:
        liste_mot_a_deviner.append(lettre)# Forme de la liste contenant le mot à deviner
        liste_mot_trouve.append("*")# Forme de la liste contenant un nombre d'étoiles identique au nombre n de lettres du mot à deviner

    print("".join(liste_mot_trouve))    # Affiche les n étoiles

    nb_erreur = 0
    while nb_erreur < 8:                  # Répétition tant que le nombre d'erreurs est inférieur à 8
        lettre = input(joueur_cherche[0] + ", propose une lettre ").lower()    # Saisie un lettre par le joueur qui cherche
        lettre_trouvee = False
        for (index_lettre, lettre_du_mot_a_deviner) in enumerate(liste_mot_a_deviner): # Boucle bornée lettre par lettre de la liste du mot à deviner
            if lettre_du_mot_a_deviner ==  lettre: # Test si la lettre est devinée
                lettre_trouvee = True
                liste_mot_trouve[index_lettre] = lettre # Remplace l'étoile par la lettre trouvée
            mot_en_cours = "".join(liste_mot_trouve)  # convertit la liste en mot

        if liste_mot_a_deviner == liste_mot_trouve:   # Teste si le mot est trouvé
            print(f"Bravo {joueur_cherche[0]}, tu as trouvé le mot : {mot} !")
            return (True, nb_erreur)  # Retourne le tuple (issue du jeu et nombre d'erreurs)

        elif lettre_trouvee:
            print("Bonne lettre ! Le résultat :", mot_en_cours)

        else:
            nb_erreur += 1# Incrémente le nombre d'erreurs
            print("Mauvaise lettre, il te reste ", (9 - nb_erreur), " essais ")
            print("Le résultat :", mot_en_cours)

    print("Tu es PENDU, le mot était : ",mot)
    return (False, nb_erreur)# Retourne le tuple (issue du jeu et nombre d'erreurs)

def etablir_score(joueur):
    """ Etablit le score du joueur
    # Précondtion : la liste du joueur contenant son pseudo (type chr) et son score (type int)
    # Postcondition : modifie l'item "score" de la liste"""
    if gagne:
        score = 10 - nombre_erreurs
        joueur[1] += score# modifie le score du joueur

# Variable globale
liste_joueurs = []

# Programme principal
try:
    liste_joueurs.append(inscrire("premier"))   # premier joueur
    liste_joueurs.append(inscrire("deuxième"))  # deuxième joueur
    while True: # Boucle infinie
        gagne,nombre_erreurs = jouer_pendu(liste_joueurs[0], liste_joueurs[1])
        etablir_score(liste_joueurs[1])
        print(f"{liste_joueurs[1][0]}, ton score est de : {liste_joueurs[1][1]} ")

        gagne,nombre_erreurs = jouer_pendu(liste_joueurs[0], liste_joueurs[1])
        etablir_score(liste_joueurs[0])
        print(f"{liste_joueurs[0][0]}, ton score est de : {liste_joueurs[0][1]} ")

except KeyboardInterrupt:   # Si Annulation
   dico_joueurs = dict(liste_joueurs)
   for element in dico_joueurs.items():
       print (element)
   print (dico_joueurs)
   print("Fin")

