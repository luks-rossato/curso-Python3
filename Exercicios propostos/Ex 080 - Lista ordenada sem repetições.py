lista = list()

for i in range(0,6):
    j = 0
    v = int(input(f'Digite o valor {i} = '))
    if i == 0:
        lista.append(v)
    else:
        while j != 6:
            if lista[j] >= v:
                j+=1
            else:
                lista.insert(j,v)

for i in range(0,6):
    print(f'Lista[{i}] = {lista[i]}')