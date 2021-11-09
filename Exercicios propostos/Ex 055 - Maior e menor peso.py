maior = 0
menor = 1000

for i in range(0,5):
    peso = int(input('Digite um peso (kg): '))
    if(peso>maior):
        maior = peso
    if(peso<menor):
        menor = peso

print('O maior peso foi {} kg e o menor peso foi {}kg'.format(maior, menor))