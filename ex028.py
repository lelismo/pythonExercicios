from random import randint
numero_aleatorio = randint(0, 5)
print('Tente adivinhar um número aleatório de 1 a 5...')
numero_digitado = int(input('Digite um número de 1 a 5: '))
if numero_aleatorio == numero_digitado:
    print('VOCÊ ACERTOU!!!')
else:
    print('ERRRRROU!!!')
