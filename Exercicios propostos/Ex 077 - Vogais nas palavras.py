lista = ('lapis', 'caneta', 'borracha', 'mel', 'celular', 'controle')
vogais = ('a', 'e', 'i', 'o', 'u')
for item in lista:
    print(f'\nNa palavra {item} temos as vogais: ', end= ' ')
    for i in range(0,len(item)):
        for v in range(0,5):
            if item[i] == vogais[v]:
                print(item[i], end=' ')
                break
