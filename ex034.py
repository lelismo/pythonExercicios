print('Calcular aumento de funcionário')
salario = float(input('Digite o salário: '))
if salario >= 1250:
    print('Você ganha mais de R$1250,00. Seu aumento é de 10%.')
    print(f'Seu salário agora é {salario + (salario*10/100):.2f}')
else:
    print('Você ganha menos de R$1250,00. Seu aumento é de 15%.')
    print(f'Seu salário agora é {salario + (salario*15/100):.2f}')
