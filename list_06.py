# broj elemenata liste

# nacin da range konvertiramo u listu
numbers = list(range(10))
number_of_elements = len(numbers)
print(f'Lista numbers ima {number_of_elements} clanova.')


numbers.append(11)
numbers.append(21)
numbers.append(31)

number_of_elements = len(numbers)
print(f'Lista numbers ima {number_of_elements} clanova.')
print()


names = []
# names = [
#     'Pero Peric',
#     'Ana Anic',
#     'Iva Ivic'
# ]

if len(names) == 0:
    print('U kolekciji nema podataka')
else:
    for name in names:
        print(name)
