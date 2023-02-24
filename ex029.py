print('Limite de velocidade: 80 km/h')
velocidade = int(input('Digite a velocidade do carro: '))
print(f'O carro está a {velocidade} km/h')
if velocidade >= 80:
    print('Você foi multado!')
    print(f'Sua multa é de R${(velocidade - 80) * 7} reais')
else:
    print('Você está seguro!')
