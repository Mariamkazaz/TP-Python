#Exercice1:
from abc import ABC, abstractmethod
import math
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    def calculer_surface(self):
        return math.pi * self.rayon ** 2
class Rectangle(Forme):
    def __init__(self, Largeur, longeur):
        self.Largeur = Largeur
        self.longeur = longeur
    def calculer_surface(self):
        return self.Largeur * self.longeur
    
cercle = Cercle(5)
rectangle = Rectangle(4, 6)

# Affichage des résultats
print(cercle.calculer_surface())
print(rectangle.calculer_surface())

#Exercice 2:
class Personne: 
    def __init__(self, nom, prenom, age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
@property
def nom(self):
    return self.__nom
@property
def prenom(self):
    return self.__prenom
@property
def age(self):
    return self.__age
@age.setter
def age (self, age ):
    if age >0:
        self.__age=age
    else:
        print("Erreur, l'age doit etre positif")
#affichage 
P1=Personne("Mariam","Kazaz",21)
print(P1.nom,P1.prenom,P1.age)

#Exercice 3:

from abc import ABC, abstractmethod
import math
class Form(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    def calculer_surface(self):
        return math.pi * self.rayon ** 2
class Rectangle(Forme):
    def __init__(self, Largeur, longeur):
        self.Largeur = Largeur
        self.longeur = longeur
    def calculer_surface(self):
        return self.Largeur * self.longeur
def afficher_surface(forms):
    for form in forms:
        print(f"la surface:{form.calculer_surface()}")
cercle = Cercle(5)
rectangle = Rectangle(4, 6)
forms=[cercle,rectangle]
afficher_surface(forms)

#Exercice 4:
class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
            self.__prix = prix
    def calculer_remise(self, remise, seuil):
        if self.__prix >= seuil:
            return self.__prix * (1 - remise)
        else:
            return f"Aucune remise, le prix doit être supérieur ou égal à {seuil}."
        
P1 = Produit("PC", 4500)
print(P1.calculer_remise(0.1, 1500))  

#Exercice 5:
class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
    def __str__(self):
        return f"{self.nom} {self.prenom} ; salaire :{self.salaire}"
class Menage(Employe):
    def __init__(self,nom,prenom,salaire):
        super().__init__(nom,prenom,salaire)
        self.employees=[]
    def ajouter_employe(self,employe):
            return self.employees.append(employe)
    def affichage(self):
        if not self.employees:
           print("aucun employe")
        else:
            for employe in self.employees:
                print(f"{employe.nom} {employe.prenom} - Salaire : {employe.salaire}")
emp1=Employe("A","B",1500)
emp2=Employe("C","D",2000)
mng=Menage("E","F",8000)
mng.ajouter_employe(emp1)
mng.ajouter_employe(emp2)
mng.affichage()

#Exercice 6:
class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def get_prix(self):
        return self.__prix

    def get_nom(self):
        return self.__nom


class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def total_commande(self):
        return self.produit.get_prix() * self.quantite


class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        total = sum(commande.total_commande() for commande in self.commandes)
        return total


# Exemple d'utilisation
if __name__ == "__main__":
    produit1 = Produit("Ordinateur", 120)
    produit2 = Produit("Souris", 20)

    commande1 = Commande(produit1, 2)  # 2 ordinateurs
    commande2 = Commande(produit2, 3)  # 3 souris

    panier = Panier()
    panier.ajouter_commande(commande1)
    panier.ajouter_commande(commande2)

    print(f"Total du panier : {panier.calculer_total():.2f}")

#Exercice 7:
from abc import ABC, abstractmethod

# Classe abstraite Vehicule
class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass
class Voiture(Vehicule):
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def deplacer(self):
        return f"La voiture {self.marque} {self.modele} roule sur la route."

class Bicyclette(Vehicule):
    def __init__(self, marque, type_bicyclette):
        self.marque = marque
        self.type_bicyclette = type_bicyclette

    def deplacer(self):
        return f"La bicyclette {self.marque} ({self.type_bicyclette}) se déplace à une vélo."

# Exemple d'utilisation

voiture = Voiture("Toyota", "Corolla")
bicyclette = Bicyclette("BMX", "VTT")

print(voiture.deplacer())  
print(bicyclette.deplacer()) 




