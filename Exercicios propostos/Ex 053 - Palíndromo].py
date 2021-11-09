palavra = str(input('Digite a frase: '))

palavra = palavra.strip().upper()

analise = palavra.split()
analise = ''.join(analise)
inverso = ''

for letra in range(len(analise)-1, -1, -1):
    inverso += analise[letra]
print(analise)
print(inverso)

if (analise == inverso):
    print('\nTEMOS UM PALINDROMO')
else:
    print('\nNÂO TEMOS UM PALÍNDROMO')