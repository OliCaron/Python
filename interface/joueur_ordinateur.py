"""
La classe JoueurOrdinateur

Hérite de Joueur et contient une "intelligence artificielle" extrêmement rudimentaire.
"""

from random import randint, choice, shuffle
from jeu.joueur import Joueur


#### DÉBUT DÉFI JOUEUR ORDINATEUR ####

class JoueurOrdinateur(Joueur):  # N'oubliez pas d'hériter de Joueur !!
    def __init__(self, numero_joueur, des_initiaux, arene):
        """
                Constructeur de la classe JoueurOrdinateur.

                Args:
                    numero_joueur (int): Le numéro identifiant le joueur
                    des_initiaux (list): Les dés en possession du joueur en début de partie
                    arene (Arene): l'arène du jeu
                """
        super().__init__(numero_joueur, des_initiaux, arene)
    # Écrivez les 4 méthodes demandées.
    def decision_continuer(self):
        """
        Détermine si le joueur souhaite continuer son tour.
        Doit être implémenté par la classe JoueurOrdinateur.
        """
        #  select par choix random de 1 parmi 16 contenant 25% de false
        _liste_choix = [True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False]
        shuffle(_liste_choix)  # pour ameliorer le randomness
        return choice(_liste_choix)
        # Une version du code decision_continuer
 #  def decision_continuer(self):
     #  values = [True, False, True, True]
     #  index = randint(0, 3)
     #  return values[index]
        
        
        
       
    
    def choisir_coordonnees(self):
        """
        Détermine comment le joueur choisit les coordonnées de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        return self.piger_coordonnees()

    def choisir_angle(self):
        """
        Détermine comment le joueur choisit l'angle de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        return self.piger_angle()

    def choisir_puissance(self):
        """
        Détermine comment le joueur choisit la puissance de son lancer.
        Doit être implémenté par les classes enfant de Joueur.
        """
        return self.piger_puissance()
#### FIN DÉFI JOUEUR ORDINATEUR ####
