"""
Module contenant des frames utilitaires présents dans la fenêtre principale.
"""

from tkinter import Frame, Label, Button, Scale, VERTICAL, IntVar

from interface.joueur_ordinateur import JoueurOrdinateur


class FrameDescription(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameDescription. Affiche un descriptif
        de ce qui se passe dans le jeu.

        Args:
            master (Tk): La fenêtre dans laquelle ce frame s'insert.
        """
        super().__init__(master)
        self.label_description = Label(self, text="")
        self.label_description.grid(row=0, column=0)

    def populer(self, texte, temps_attente, suite):
        """
        Cette méthode affiche les informations sur le jeu.

        Args:
            texte (str): Le message à afficher
            temps_attente (int): Temps en millisecondes avant d'exécuter la suite
            suite (fonction): La fonction à exécuter après
        """
        self.label_description['text'] = texte
        self.after(temps_attente, suite)

    def vider(self):
        """
        Cette méthode enlève l'affichage.
        """
        self.label_description['text'] = ""


class FrameJoueurActif(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameJoueurActif. Affiche les informations relatives au
        joueur dont c'est le tour.

        Args:
            master (Tk): La fenêtre dans laquelle ce frame s'insert.
        """
        super().__init__(master)

        self.label_nom_joueur = Label(self, text="")
        self.label_nombre_des = Label(self, text="")

        self.label_nom_joueur.grid(row=0, column=0)
        self.label_nombre_des.grid(row=1, column=0)

        self.clic_bouton = lambda: None
        self.bouton_terminer_tour = Button(self, text="Terminer le tour", command=self.appui_bouton)
        self.bouton_terminer_tour.grid(row=1, column=1)
        self.bouton_terminer_tour["state"] = "disabled"

        self.couleurs = [
            'blue', 'green', 'red', 'orange', 'purple'
        ]

    def populer(self, joueur):
        """
        Ajoute les informations d'un joueur dans le frame.

        Args:
            joueur (Joueur): le joueur dont c'est le tour
        """
        self.label_nom_joueur["text"] = f"Joueur # {joueur.numero_joueur}"
        self.label_nombre_des["text"] = f"{len(joueur.des)} dés"
        self.label_nom_joueur["fg"] = self.couleurs[joueur.numero_joueur - 1]
        self.label_nombre_des["fg"] = self.couleurs[joueur.numero_joueur - 1]

    def activer_bouton(self, fonction):
        """
        Permet de cliquer sur le bouton fin du tour, et associe la fonction au clic.

        Args:
            fonction (fonction): La fonction à exécuter suite au clic de bouton
        """
        self.bouton_terminer_tour["state"] = "normal"
        self.clic_bouton = fonction

    def appui_bouton(self):
        """
        Effectue la fonction à exécuter suite au clic de bouton, et grise le bouton.
        """
        self.bouton_terminer_tour["state"] = "disabled"
        self.clic_bouton()


class FrameTableauJoueurs(Frame):
    def __init__(self, master):
        super().__init__(master)

        #### DÉBUT DÉFI TABLEAU DES JOUEURS ####
        
        self.labels_joueurs = [] # initialisation de ma liste de labels
        
        # boucle pour inclure les bonnes informations dans chaque label de ma liste et les afficher avec le .grid()
        for joueur in self.master.joueurs:
            self.labels_joueurs.append(Label(self,
                                             text=f"Joueur {joueur.numero_joueur} : {len(joueur.des)} dé(s)",
                                             fg=self.master.frame_joueur.couleurs[joueur.numero_joueur - 1]))
            self.labels_joueurs[joueur.numero_joueur - 1].grid()

    def mise_a_jour(self):

        _i = 0
        
        # boucle pour mettre à jour le nombre de dés du joueur ou afficher que le joueur est éliminé
        for label in self.labels_joueurs:
            if self.master.joueurs[_i].est_elimine():
                label.config(text=f"Joueur {self.master.joueurs[_i].numero_joueur} : ÉLIMINÉ")
            else:
                label.config( text=f"Joueur {self.master.joueurs[_i].numero_joueur} "
                                   f": {len(self.master.joueurs[_i].des)}  dé(s)")
            _i = _i + 1
            
        #### FIN DÉFI TABLEAU DES JOUEURS ####


class FrameTempsAttente(Frame):
    def __init__(self, master):
        super().__init__(master)
        #### DÉBUT DÉFI TEMPS ATTENTE ####
        self.vitesse = IntVar(value=250)
        Scale(self, from_=500, to=10, variable=self.vitesse).pack()
        master.gestionnaire_io.temps_attente = self.obtenir_vitesse

    def obtenir_vitesse(self):
        return self.vitesse.get()

        #### FIN DÉFI TEMPS ATTENTE ####
