lista = list()
maior = 0
menor = 0
for i in range(0,5):
    lista.append(int(input('Digite um valor:')))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if maior < lista[i]:
            maior = lista[i]
        if menor > lista[i]:
            menor = lista[i]

print(f'O maior valor encontrado foi o {maior} na posição ', end=' ')
for v, p in enumerate(lista):
    if p == maior:
        print(f'{v}\n')
print(f'O menor valor encontrado foi o {menor} na posição ', end=' ')
for v, p in enumerate(lista):
    if p == menor:
        print(f'{v}\n')


