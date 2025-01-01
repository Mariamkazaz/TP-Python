#Exercice1
try:
    # Ouvrir le fichier en mode lecture
    with open("exemple.txt", "r") as fichier:
        # Lire toutes les lignes du fichier
        lignes = fichier.readlines()
        
        # Afficher chaque ligne avec son numéro
        for numero, ligne in enumerate(lignes, start=1):
            print(f"Ligne {numero}: {ligne.strip()}")
except FileNotFoundError:
    print("Le fichier 'exemple.txt' est introuvable.")
#Exercice 2:

phrases = []
for i in range(1, 4):
    phrase = input(f"Entrez la phrase {i} : ")
    phrases.append(phrase)

# Enregistrer les phrases dans le fichier "phrases.txt"
try:
    with open("phrases.txt", "w") as fichier:
        for phrase in phrases:
            fichier.write(phrase + "\n")
    print("Les phrases ont été enregistrées dans le fichier .")
except Exception as e:
    print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {e}")
#Exercice 3:

def ajouter_phrases(fichier):
    while True:
        phrase = input("Entrez une phrase à ajouter (ou appuyez sur Entrée pour terminer) : ")
        if phrase == "":
            break
        fichier.write(phrase + "\n")
    print("Les nouvelles phrases ont été ajoutées au fichier.")

# Demander les premières phrases
phrases = []
for i in range(1, 4):
    phrase = input(f"Entrez la phrase {i} : ")
    phrases.append(phrase)

# Enregistrer les phrases dans le fichier 
try:
    with open("phrases.txt", "w") as fichier:
        for phrase in phrases:
            fichier.write(phrase + "\n")
    print("Les phrases ont été enregistrées dans le fichier .")
    
    # Demander si l'utilisateur souhaite ajouter d'autres phrases
    reponse = input("Souhaitez-vous ajouter d'autres phrases ? (oui/non) : ").strip().lower()
    if reponse == "oui":
        with open("phrases.txt", "a") as fichier:  # Mode "a" pour ajouter à la fin du fichier
            ajouter_phrases(fichier)

except Exception as e:
    print(f"Une erreur s'est produite : {e}")
#Exercice 4:
import csv

# Script pour lire le fichier CSV et afficher les informations de chaque contact
try:
    # Ouvrir le fichier avec gestion de l'encodage
    with open("contacts.csv", "r", encoding="utf-8") as fichier_csv:
        # Lire le fichier en tant que dictionnaire
        lecteur = csv.DictReader(fichier_csv)
        
        # Vérifier si les colonnes nécessaires existent
        colonnes_attendues = ["Nom", "Âge", "Ville"]
        if not all(colonne in lecteur.fieldnames for colonne in colonnes_attendues):
            raise KeyError(f"Les colonnes attendues {colonnes_attendues} ne sont pas toutes présentes dans le fichier.")
        
        # Afficher les informations des contacts
        for ligne in lecteur:
            print(f"Nom : {ligne['Nom']}, Âge : {ligne['Âge']}, Ville : {ligne['Ville']}")
except FileNotFoundError:
    print("Le fichier 'contacts.csv' est introuvable. Assurez-vous qu'il existe dans le même dossier que ce script.")
except KeyError as e:
    print(f"Une erreur s'est produite : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")
#Exercice 5:
import json

#  Créer un dictionnaire contenant les informations des étudiants
etudiants = {
    "etudiants": [
        {"nom": "Alice", "âge": 20, "note": 15.5},
        {"nom": "Bob", "âge": 22, "note": 14.0},
        {"nom": "Charlie", "âge": 21, "note": 16.0},
    ]
}

#  Enregistrer le dictionnaire dans un fichier 
try:
    with open("etudiants.json", "w", encoding="utf-8") as fichier_json:
        json.dump(etudiants, fichier_json, ensure_ascii=False, indent=4)
    print("Les informations des étudiants ont été enregistrées dans 'etudiants.json'.")
except Exception as e:
    print(f"Une erreur s'est produite lors de l'écriture dans le fichier JSON : {e}")

#  Lire le fichier JSON et afficher les informations
try:
    with open("etudiants.json", "r", encoding="utf-8") as fichier_json:
        donnees = json.load(fichier_json)  # Charger les données depuis le fichier JSON
        print("\nInformations des étudiants :")
        for etudiant in donnees["etudiants"]:
            print(f"Nom : {etudiant['nom']}, Âge : {etudiant['âge']}, Note : {etudiant['note']}")
except FileNotFoundError:
    print("Le fichier 'etudiants.json' est introuvable. Assurez-vous qu'il existe dans le même dossier que ce script.")
except Exception as e:
    print(f"Une erreur s'est produite lors de la lecture du fichier JSON : {e}")

#Exercice 6:
import os


# Renommer le fichier 'phrases.txt' en 'anciennes_phrases.txt'
try:
    os.rename("phrases.txt", "anciennes_phrases.txt")
    print("Le fichier 'phrases.txt' a été renommé en 'anciennes_phrases.txt'.")
except FileNotFoundError:
    print("Le fichier 'phrases.txt' est introuvable. Assurez-vous qu'il existe dans le même dossier que ce script.")
except Exception as e:
    print(f"Une erreur s'est produite lors du renommage du fichier : {e}")

#  Supprimer le fichier 'anciennes_phrases.txt'
try:
    os.remove("anciennes_phrases.txt")
    print("Le fichier 'anciennes_phrases.txt' a été supprimé.")
except FileNotFoundError:
    print("Le fichier 'anciennes_phrases.txt' est introuvable. Assurez-vous qu'il existe dans le même dossier que ce script.")
except Exception as e:
    print(f"Une erreur s'est produite lors de la suppression du fichier : {e}")
#Exercice 7:
import shutil
import os

#  Copier le fichier "journal.txt" en "journal_copie.txt"
try:
    shutil.copy("journal.txt", "journal_copie.txt")
    print("Le fichier 'journal.txt' a été copié en 'journal_copie.txt'.")
except FileNotFoundError:
    print("Le fichier 'journal.txt' est introuvable. Assurez-vous qu'il existe.")
except Exception as e:
    print(f"Une erreur s'est produite lors de la copie : {e}")

#  Créer un dossier "archives" (s'il n'existe pas déjà)
try:
    if not os.path.exists("archives"):
        os.mkdir("archives")
        print("Le dossier 'archives' a été créé.")
except Exception as e:
    print(f"Une erreur s'est produite lors de la création du dossier : {e}")

#  Déplacer "journal_copie.txt" dans le dossier "archives"
try:
    shutil.move("journal_copie.txt", "archives/journal_copie.txt")
    print("Le fichier 'journal_copie.txt' a été déplacé dans le dossier 'archives'.")
except FileNotFoundError:
    print("Le fichier 'journal_copie.txt' est introuvable.")
except Exception as e:
    print(f"Une erreur s'est produite lors du déplacement : {e}")

#Exercice 8:

try:
    with open("inexistant.txt", "r") as fichier:
        contenu = fichier.read()
        print(contenu)
except FileNotFoundError:
    print("Erreur : Le fichier 'inexistant.txt' est introuvable.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
#Exercice 9:

try:
    with open("exemple.txt", "r", encoding="utf-8") as fichier:
        # Initialisation des compteurs
        total_lignes = 0
        total_mots = 0
        total_caracteres = 0
        
        # Parcourir chaque ligne du fichier
        for ligne in fichier:
            total_lignes += 1  # Compter les lignes
            total_caracteres += len(ligne)  # Compter les caractères dans la ligne
            total_mots += len(ligne.split())  # Compter les mots dans la ligne
            
        # Afficher les statistiques
        print(f"Nombre total de lignes : {total_lignes}")
        print(f"Nombre total de mots : {total_mots}")
        print(f"Nombre total de caractères : {total_caracteres}")
        
except FileNotFoundError:
    print("Erreur : Le fichier 'exemple.txt' est introuvable.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
#Exercice 10:
import csv
import os

# Chemin du fichier CSV
fichier_csv = "contacts.csv"

# Fonction pour ajouter un contact
def ajouter_contact():
    nom = input("Entrez le nom du contact : ")
    age = input("Entrez l'âge du contact : ")
    ville = input("Entrez la ville du contact : ")

    # Ajouter le contact au fichier CSV
    with open(fichier_csv, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([nom, age, ville])
    print(f"Contact {nom} ajouté avec succès.")

# Fonction pour afficher tous les contacts
def afficher_contacts():
    if os.path.exists(fichier_csv):
        with open(fichier_csv, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Ignorer l'en-tête
            for row in reader:
                print(f"Nom : {row[0]}, Âge : {row[1]}, Ville : {row[2]}")
    else:
        print("Aucun contact n'est enregistré pour le moment.")

# Fonction pour rechercher un contact par nom
def rechercher_contact():
    nom_recherche = input("Entrez le nom du contact à rechercher : ")
    trouve = False
    if os.path.exists(fichier_csv):
        with open(fichier_csv, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Ignorer l'en-tête
            for row in reader:
                if row[0].lower() == nom_recherche.lower():
                    print(f"Nom : {row[0]}, Âge : {row[1]}, Ville : {row[2]}")
                    trouve = True
                    break
    if not trouve:
        print(f"Aucun contact trouvé pour {nom_recherche}.")

# Fonction pour supprimer un contact
def supprimer_contact():
    nom_suppression = input("Entrez le nom du contact à supprimer : ")
    contacts_restants = []
    trouve = False
    if os.path.exists(fichier_csv):
        with open(fichier_csv, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)  # Lire l'en-tête
            contacts_restants.append(header)  # Conserver l'en-tête
            for row in reader:
                if row[0].lower() != nom_suppression.lower():
                    contacts_restants.append(row)
                else:
                    trouve = True
        # Si le contact est trouvé, on réécrit le fichier sans ce contact
        if trouve:
            with open(fichier_csv, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(contacts_restants)
            print(f"Contact {nom_suppression} supprimé avec succès.")
        else:
            print(f"Aucun contact trouvé pour {nom_suppression}.")
    else:
        print("Le fichier des contacts est vide.")

# Menu principal de l'application
def menu():
    while True:
        print("\n--- Gestion des Contacts ---")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5) : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir entre 1 et 5.")

# Démarrer l'application
if __name__ == "__main__":
    # Créer le fichier CSV si il n'existe pas
    if not os.path.exists(fichier_csv):
        with open(fichier_csv, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nom", "Âge", "Ville"])  # Ajouter l'en-tête
    # Lancer le menu
    menu()


