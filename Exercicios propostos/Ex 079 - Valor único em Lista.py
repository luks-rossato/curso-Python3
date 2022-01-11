lista = list()
for i in range(0,11):
    v = int(input('Digite um valor:'))
    if v in lista:
        print()
    else:
        print()
        lista.append(v)
lista.sort()
for i in range(0,len(lista)-1):
    print(f'lista[{i}] = {lista[i]}\n')
