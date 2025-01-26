#Exercice 1:
def safe_division(a,b):
    if b ==0:
        raise ValueError("cannot devide by 0")
    return a/b
try:
    print(safe_division(10,2))
except ValueError as e:
    print(e)
#Exercice 2:
def convert_to_int(value):
    try:
        return int (value)
    except ValueError:
        raise ValueError(f"la conversion echoué.")
try:
    print(convert_to_int("42"))
except ValueError as e :
    print (e)
# Exercice 3:
def read_file(filename):
    try:
        with open(filename,'r') as file:
            content= file.read()
            print(content)
    except FileNotFoundError as e:
        print (e)
    finally:
         print("Tentative terminée")
content=read_file("example.txt")
#Exercice 4:
class NegativeAgeError(Exception):
    pass
def set_age(age):
    if age< 0:
        raise NegativeAgeError("L'age ne peut pas etre negatif")
    else: 
        print("L'age a ete défini ")
try:
    age= -5
    set_age(age)
except NegativeAgeError as e :
    print(f"Une erreur s'est produite:{e}")
#Exercice 5:
def process_input(user_input):
    try:
        # Tentative de conversion en entier
        number = int(user_input)
        # Tentative de division par 10
        result = number / 10
        print(f"Le résultat est : {result}")
    except ValueError:
        # Gestion des erreurs de conversion
        print("Erreur : La saisie doit être un nombre entier.")
    except ZeroDivisionError:
        # Gestion des erreurs de division par zéro
        print("Erreur : La division par zéro n'est pas autorisée.")

# Exemple d'utilisation
if __name__ == "__main__":
    user_input = input("Entrez une valeur : ")
    process_input(user_input)
#Exercice 6:
def process_input(user_input):
    try:
        # Tentative de conversion en entier
        number = int(user_input)
        # Tentative de division par 10
        result = number / 10
    except ValueError:
        print("Erreur : La saisie doit être un nombre entier.")
    except ZeroDivisionError:
        print("Erreur : La division par zéro n'est pas autorisée.")
    else:
        print(f"Le résultat est : {result}")
        print("La division a été effectuée avec succès.")
    finally:
        print("La fonction est terminée.")

# Exemple d'utilisation
if __name__ == "__main__":
    user_input = input("Entrez une valeur : ")
    process_input(user_input)
#Exercice 7:
def process_input(user_input):
    try:
        # Tentative de conversion en entier
        number = int(user_input)
        # Tentative de division par 10
        result = number / 10
    except ValueError:
        print("Erreur : La saisie doit être un nombre entier.")
    except ZeroDivisionError:
        print("Erreur : La division par zéro n'est pas autorisée.")
    else:
        print(f"Le résultat est : {result}")
        print("La division a été effectuée avec succès.")
    finally:
        print("La fonction est terminée.")

# Exemple d'utilisation
if __name__ == "__main__":
    user_input = input("Entrez une valeur : ")
    process_input(user_input)
#Exercice 7:
import logging

# Configuration de la journalisation
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_error(message):

    logging.error(message)

def read_file(file_path):
 
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Contenu du fichier :")
            print(content)
    except FileNotFoundError as e:
        print("Erreur : Fichier introuvable.")
        log_error(f"FileNotFoundError - {e}")
    except Exception as e:
        print("Une erreur inattendue s'est produite.")
        log_error(f"UnexpectedError - {e}")
    finally:
        print("Tentative de lecture terminée.")

# Exemple d'utilisation
if __name__ == "__main__":
    file_path = input("Entrez le chemin du fichier : ")
    read_file(file_path)
#Exercice 8:
import unittest
def division(a, b):
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être zéro.")
    return a / b

class TestDivision(unittest.TestCase):
    def test_division_zero(self):
        # Vérifie si ValueError est levée lorsque le diviseur est zéro
        with self.assertRaises(ValueError) as context:
            division(10, 0)
        self.assertEqual(str(context.exception), "Le diviseur ne peut pas être zéro.")
    
    def test_division_valide(self):
        # Vérifie le cas normal où aucune exception n'est levée
        self.assertEqual(division(10, 2), 5)

# Exécution des tests si ce fichier est exécuté directement
if __name__ == "__main__":
    unittest.main()

#Exercice 9:

def get_positive_integer():
    while True:
        try:
            user_input = input("Veuillez entrer un entier positif : ")
            number = int(user_input)
            if number > 0:
                print(f"Vous avez saisi : {number}")
                return number
            else:
                print("Erreur : Le nombre doit être strictement positif.")
        except ValueError:
            print("Erreur : La saisie doit être un nombre entier.")
#Exercice 10 :
import logging

# Configuration de la journalisation
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_error(message):
    logging.error(message)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Contenu du fichier :")
            print(content)
    except FileNotFoundError as e:
        print("Erreur : Fichier introuvable.")
        log_error(f"FileNotFoundError - {e}")
    except Exception as e:
        print("Une erreur inattendue s'est produite.")
        log_error(f"UnexpectedError - {e}")
    finally:
        print("Tentative de lecture terminée.")

def get_positive_integer():
    while True:
        try:
            user_input = input("Veuillez entrer un entier positif : ")
            number = int(user_input)
            if number > 0:
                print(f"Vous avez saisi : {number}")
                return number
            else:
                print("Erreur : Le nombre doit être strictement positif.")
        except ValueError:
            print("Erreur : La saisie doit être un nombre entier.")

if __name__ == "__main__":
    # Saisie du fichier
    file_path = input("Entrez le chemin du fichier : ")
    read_file(file_path)

    # Saisie d'un entier positif
    get_positive_integer()
