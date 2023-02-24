nome_completo = str(input("Digite nome completo: ")).strip()
print('Analisando seu nome...')
print(f'NOME COM TODAS MAIÚSCULAS: {nome_completo.upper()}')
print(f'nome com todas minúsculas: {nome_completo.lower()}')

nome_sem_espaço = nome_completo.replace(' ','')
print(f'Seu nome tem ao todo {len(nome_sem_espaço)} letras')
# print(f"Seu nome tem ao todo {len(nome_completo) - nome_completo.count(' ')} letras")

nome_sobrenome = nome_completo.split()
print(f'Seu primeiro nome é {nome_sobrenome[0]} e ele tem {(len(nome_sobrenome[0]))} letras')
print(f'Seu sobrenome é {nome_sobrenome[1]} e ele tem {len(nome_sobrenome[1])} letras')


