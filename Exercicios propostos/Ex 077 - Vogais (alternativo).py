lista = ('lapis', 'caneta', 'borracha', 'mel', 'celular', 'controle')

for item in lista:
    print(f'\nNa palavra {item} temos as vogais: ', end= ' ')
    for i in range(0,len(item)):
        if item[i].lower() in 'aeiou':
            print(item[i], end= ' ')