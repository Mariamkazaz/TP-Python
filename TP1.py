#Exercice 1:
def somme_list(liste):
    return sum(liste)
print(somme_list([1,2,3,4]))
 
#Exercice 2:
def max_tuple(t):
    return max(t)
print(max_tuple((1,2,3,8,19)))

#Exercice 3:
def  intersection (ensemble1, ensemble2):
    return ensemble1&ensemble2
print(intersection({1,2,3,4},{2,3,8,9}))

#Exercice 4:
def compte_occurrences(liste):
    return{mot: liste.count(mot) for mot in set(liste)}
print(compte_occurrences(["chien","chat","chien","chat","lion","chien","chien"]))

#Exercice 5:
def factorielle(n):
    if n==0:
        return 1
    else:
        return (n*factorielle(n-1))
print(factorielle(5))

#Exercice 6:
carre=lambda n:pow(n,2)
print(carre(2))

#Exercice 7:
def salutation(nom, message="Bonjour"):
    print(f"{message},{nom} !")
salutation ("Alice")
salutation("Bob","Salut")

#Exercice 8:
def somme_varags(*args):
    return sum(args)
print("La somme est:",somme_varags(1,2,3))

#Exercice 9:
def analyse_texte(texte):
    nombre_mots =len(texte.split())
    nombre_caracteres= len(texte)
    resultat = {"mots": nombre_mots, "caracteres":nombre_caracteres}
    return resultat
texte= "Python est une langage de programmation"
resultat =analyse_texte(texte)
print("Analyse du texte :", resultat)

#Exercice 10:
def fusionner_dicts(dict1, dict2):
    fusion= dict1.copy()
    for cle, valeur in dict2.items():
        if cle in fusion:
            fusion[cle] +=valeur
        else:
            fusion [cle] = valeur
    return fusion
dict1= {"a": 1, "b":2, "c":3}
dict2={"b":3, "c":4, "d":5}
resultat = fusionner_dicts(dict1, dict2)
print("Dictionnaire fusionné :",resultat)