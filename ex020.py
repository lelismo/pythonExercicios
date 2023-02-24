from random import shuffle
alune_1 = input('1o alune: ')
alune_2 = input('2o alune: ')
alune_3 = input('3o alune: ')
alune_4 = input('4o alune: ')
lista = [alune_1, alune_2, alune_3, alune_4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}')