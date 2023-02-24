frase = str(input('Digite uma frase: ')).upper().strip()
print(f"A letra A aparece {frase.count('A')} vezes")
print(f"A letra A aparece pela primeira vez na posição {frase.find('A')}")
print(f"A letra A aparece pela última vez na posição {frase.rfind('A')}")
