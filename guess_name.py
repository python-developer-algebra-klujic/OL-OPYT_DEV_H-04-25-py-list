# Zadatak:
#   Dodati brojac pokusaja te prilagoditi ispis nakon sto korisnik pogodi,
#   tako da napise iz koliko pokusaja je pogodio naziv programskog jezika


# import - ovoe cemo uskoro raditi, ali za sada zanemriti
import random


# deklaracija pocetnih vrijednosti
languages = ['Python', 'Java', 'C#', 'Javascript', 'Typescript', 'Golang', 'Rust', 'Lua']
selected_language_index = random.randint(0, 7)
# print(languages[selected_language_index])


# glavni dio aplikacije
while True:
    users_guess = input('Pogodite naziv programskog jezika: ')

    if users_guess.lower() == languages[selected_language_index].lower():
        print('Cestitamo!!! Pogodili ste naziv programskog jezika!!!')
        break
    else:
        print('Na zalost niste pogodili! Pokusajte ponovno.')



    next_round = input('Zelite li nastaviti? (Da/Ne): ')
    if next_round == 'ne':
        break


# zavrsetak aplikacije
print()
print('Pozdrav, do slijedeceg puta!')
print()
