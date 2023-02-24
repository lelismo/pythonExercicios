print('Descubra o número maior entre três números')
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
lista = [numero1, numero2, numero3]
lista_ordem = sorted(lista)
print(f'O numero maior é {lista_ordem[-1]}')
print(f'O numero menor é {lista_ordem[0]}')
