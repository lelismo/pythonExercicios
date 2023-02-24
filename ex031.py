print('Preço da viagem')
distancia = int(input('Digite a distância: '))
if distancia <= 200:
    print(f'A viagem vai custar R${distancia * 0.50:.2f} reais')
else:
    print(f'A viagem vai custar R${distancia * 0.45:.2f} reais')
