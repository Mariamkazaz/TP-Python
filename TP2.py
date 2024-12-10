#Exercice 1:
class chien:
    
      def __init__(self,nom, race,age):
        self.nom= nom
        self.race= race
        self.age=age
      def Aboyer(self):
           print("woof!")
mon_chien=chien("ch","b",3)
mon_chien.Aboyer()

#Exercice 2:
class voiture:
    def __init__(self,marque,modél,année):
        self.marque= marque
        self.modél= modél
        self.année= année
    def Afficher_info(self):
        print(f"marque:{self.marque},modél:{self.modél},année:{self.année}")
Voiture1= voiture("Dacia","sandero",2018)
Voiture2= voiture("CLIO","C5",2022)
Voiture3= voiture("PEUGEOT","P208",2019)
Voiture1.Afficher_info()
Voiture2.Afficher_info()
Voiture3.Afficher_info()

#Exercice 3:
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
    def deposer(self, montant):
        """Ajoute un montant au solde du compte."""
        if montant > 0:
            self.solde += montant
            print(f"{montant}€ ont été déposés sur le compte de {self.titulaire}.")
        else:
            print("Le montant à déposer doit être positif.")

    def retirer(self, montant):
        """Retire un montant du solde si le solde est suffisant."""
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                print(f"{montant}€ ont été retirés du compte de {self.titulaire}.")
            else:
                print(f"Retrait refusé : solde insuffisant. Solde actuel : {self.solde}€.")
        else:
            print("Le montant à retirer doit être positif.")

    def afficher_solde(self):
        print(f"Le solde actuel du compte de {self.titulaire} est de {self.solde}€.")

# Création d'un compte et test des méthodes
compte = CompteBancaire("Mariam", 1000)
compte.afficher_solde()

compte.deposer(500)
compte.afficher_solde()

compte.retirer(300)
compte.afficher_solde()

compte.retirer(1500)  # Cas de solde insuffisant

#exercice04
# Définition de la classe Personne
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Mon nom est{self.prenom} {self.nom}, j'ai {self.age} ans.")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"L'étudiant {self.prenom} {self.nom} (matricule : {self.matricule}) .")

personne = Personne("A", "B", 30)
personne.se_presenter()

etudiant = Etudiant("Alami", "Mari", 20, "B1360")
etudiant.se_presenter()
etudiant.etudier()

etudiant = Etudiant("jean", "Anna", 30, "B360")
etudiant.se_presenter()
etudiant.etudier()
#exercice05
class Animal:
    def faire_du_bruit(self):
        print("Cet animal fait un bruit.")

class Chien(Animal):
    def faire_du_bruit(self):
        print("woof woof!")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Miaou Miaou!")

animal_general = Animal()
chien = Chien()
chat = Chat()

animal_general.faire_du_bruit()  
chien.faire_du_bruit()          
chat.faire_du_bruit()            

#exercice06
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

rectangle = Rectangle(2, 10)
print("Surface :", rectangle.calculer_surface())
print("Périmètre :", rectangle.calculer_perimetre())

#exercice07
class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            for livre in self.livres:
                print(f"{livre.titre}, {livre.auteur} ({livre.annee_publication})")

livre1 = Livre("AB", "Jack", 1880)
livre2 = Livre("B", "Jean", 2003)

biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)

biblio.afficher_livres()

#exercice8
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []  # Liste pour stocker les amis

    def ajouter_ami(self, ami):
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami.prenom} {ami.nom} ami de {self.prenom}.")
        else:
            print(f"{ami.prenom} {ami.nom} amis dejà.")

    def afficher_amis(self):
        if not self.amis:
            print(f"{self.prenom} pas d'amis.")
        else:
            print(f"Les amis de {self.prenom} sont :")
            for ami in self.amis:
                print(f"- {ami.prenom} {ami.nom}")

personne1 = Personne("Ahmed", "B", 30)
personne2 = Personne("Salma", "AL", 25)
personne3 = Personne("Imane", "Ben", 28)

personne1.ajouter_ami(personne2)
personne1.ajouter_ami(personne3)
personne1.afficher_amis()

personne3.afficher_amis() 
