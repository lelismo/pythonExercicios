nome = str(input('Digite o nome completo: ')).strip()
nome_completo = nome.split()
print(f'Nome: {nome_completo[0]}')
print(f'Sobrenome: {nome_completo[-1]}')

# o [-1] pode ser utilizado para se referir
# ao último objeto de uma lista, assim como [-2]
# seria a penúltima e assim por diante.