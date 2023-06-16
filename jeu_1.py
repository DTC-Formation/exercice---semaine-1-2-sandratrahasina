#Jeu 1: Devinez le nombre

#Générez un nombre aléatoire entre 1 et 100.
#Demandez à l'utilisateur de deviner le nombre.
#Comparez la réponse de l'utilisateur avec le nombre généré.
#Affichez des messages "Trop grand" ou "Trop petit" en fonction de la réponse de l'utilisateur.
#Répétez les étapes 2 à 4 jusqu'à ce que l'utilisateur devine correctement le nombre.

import random

my_random_number = random.randint(1, 100)

print(my_random_number)

while (1==1) :
    my_input = input()
    if(my_random_number < int(my_input)) :
        print(my_input + " est trop grand")
    elif(my_random_number > int(my_input)) :
        print(my_input + " est trop petit")
    else :
        print("felicitation vous avez trouvez le bon chiffre")
        break