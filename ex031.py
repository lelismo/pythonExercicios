'''print('Preço da viagem') #Meu resultado
distancia = float(input('Digite a distância: '))
if distancia <= 200:
    print(f'A viagem vai custar R${distancia * 0.50:.2f} reais')
else:
    print(f'A viagem vai custar R${distancia * 0.45:.2f} reais')'''

distancia = float(input('Digite a distância: ')) #Resultado professor
print(f'Você vai começar uma viagem de {distancia}Km')
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 # If Simplificado
if distancia <= 200:
    preço = distancia * 0.50 #Variável preço com dois atributos diferentes
else:
    preço = distancia * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')
