#Exercice 1:

#Créez une liste nombres contenant les nombres de 1 à 10.
#Utilisez une boucle for pour afficher uniquement les nombres pairs de la liste.

print('Exercice 1')

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list_1 :
    if(i%2==0) :
        print(i)

#Exercice 2:

#Créez une variable phrase contenant une phrase de votre choix.
#Vérifiez si la phrase contient le mot "Python" en utilisant une condition if. Affichez un message approprié en fonction du résultat.

print('Exercice 2')

phrase_1 = "bonjour daholo ianareo ry dev Python isany"

if(phrase_1.__contains__("Python")) :
    print("la phrase contient le mot Python")
else :
    print("la phrase ne contient pas le mot Python")


#Exercice 3:

#Créez une variable age contenant votre âge.
#Utilisez une condition if pour vérifier si vous êtes majeur (âge >= 18). Affichez un message approprié en fonction du résultat.

print("Exercice 3")

age  = 22

if(age >= 18) :
    print("vous etes deja majeur")
else :
    print("vous etes encore mineur")


#Exercice 4:

#Créez une variable chaine contenant une chaîne de caractères de votre choix.
#Utilisez une méthode des objets str pour convertir la chaîne en majuscules.
#Affichez la chaîne convertie en majuscules.

print("Exercice 4")

phrase_2 = "ity ilay ho atao majuscule"

phrase_2_maj = phrase_2.upper

print(phrase_2_maj)

#Exercice 5:

#Créez une liste nombres contenant quelques nombres.
#Utilisez une boucle for pour calculer la somme de tous les nombres de la liste.
#Affichez le résultat de la somme.


print("Exercice 5")

list_2 = [1, 5, 7, 2]

somme = 0

for i in list_2 :
    somme += i

print(somme)