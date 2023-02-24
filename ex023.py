numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')

numero = int(input('Digite um numero de 0 a 9000: ')) + 10000
strnumero = str(numero)
print(f'unidade: {strnumero[4]}')
print(f'dezena: {strnumero[3]}')
print(f'centena: {strnumero[2]}')
print(f'milhar: {strnumero[1]}')


