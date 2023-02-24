from random import choice
aluno_1 = input('1o alune: ')
aluno_2 = input('2o alune: ')
aluno_3 = input('3o alune: ')
aluno_4 = input('4o alune: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(lista)
print(f'O alune escolhido foi {escolhido}') # método choice da classe random