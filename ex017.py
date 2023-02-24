from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimeto do cateto adjacente: '))
print(f'A hipotenusa vai medir: {hypot(cateto_oposto, cateto_adjacente):.2f}')
