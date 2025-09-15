# ZADATAK dio 1. dodati mogucnost izbora teme pogadanja naziva:
# teme mogu biti proizvoljne, a evo primjera: filmovi, sport, slavne osobe, mitologija ...
# HINT - za svaku temu kreirajte kolekciju i ovisno o izboru izvucite nasumicno jednog clana te kolekcije

# Ako zelite dodajte i hint korisniku tako da mu prikazete prvo slovo naziva kojeg pogada, ALI nakon treceg pokusaja!!!

# import - ovo cemo uskoro raditi, ali za sada zanemriti
import os
import random
# import time


# deklaracija pocetnih vrijednosti
languages = ['Python', 'Java', 'C#', 'Javascript', 'Golang', 'Rust', 'Lua']
movies = [
    'The Shawshank Redemption',
    'Inception',
    'The Godfather',
    'The Matrix',
    'Interstellar',
    'Pulp Fiction',
    'Fight Club'
]
bands = [
    'The Beatles',
    'Pink Floyd',
    'Queen',
    'Nirvana',
    'Radiohead',
    'Metallica',
    'Coldplay'
]
selected_theme = []
counter = 0


# glavni dio aplikacije
# petlja koja pokrece igru dok god korisnik to zeli
while True:
    os.system('cls')
    print('*'*60)
    print('\tPython Guess Game')
    print()
    print()
    print('\tGlavni Menu')
    print()
    print('\t1. Programski jezici')
    print('\t2. Filmovi')
    print('\t3. Bandovi')
    print('\t0. Exit')
    print()
    users_select_theme = input('Selektirajte jednu od tema tako da upisete broj ispred teme: ')

    if users_select_theme == '1':
        selected_theme = languages
        print()
        print('Selektirali ste temu programskih jezika')
        print()
    elif users_select_theme == '2':
        selected_theme = movies
        print()
        print('Selektirali ste temu filmova')
        print()
    elif users_select_theme == '3':
        selected_theme = bands
        print()
        print('Selektirali ste temu bandova')
        print()
    elif users_select_theme == '0':
        break
    else:
        print('Krivi izbor, pokusajte ponovo!')
        print()
        input('Za nastavak pritisnite tipku ENTER')
        # time.sleep(5)
        continue

    selected_theme_index = random.randint(0, 6)
    counter = 0

    # nova whle petlja koja obraduje jednu partiju
    while True:
        users_guess = input('Pogodite naziv trazenog pojma: ')
        counter += 1

        if users_guess.lower() == selected_theme[selected_theme_index].lower():
            print(f'Cestitamo!!! Pogodili ste naziv trazenog pojma iz {counter}. puta!!!')  
            print()
            input('Za nastavak pritisnite tipku ENTER')          
            break
        else:
            print('Na zalost niste pogodili! Pokusajte ponovno.')
            if counter >= 3:
                print()
                print(f'HINT: {selected_theme[selected_theme_index][counter - 3]}')
                input('Za nastavak pritisnite tipku ENTER')

        next_round = input('Zelite li pokusati ponovno? (Da/Ne): ')
        if next_round == 'ne':
            break


    new_game = input('Zelite li novu igru? (Da/Ne): ')
    if new_game.lower() != 'da':
        break


# zavrsetak aplikacije
print()
print('Pozdrav i do slijedeceg puta!!!')
print()
