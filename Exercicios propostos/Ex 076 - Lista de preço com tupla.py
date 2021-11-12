lista = ('Caderno', 3.5, 'Apontador', 1, 'Caneta', 2.5, 'Pasta',0.99)

print('*'*50)
print(f"{'LISTA DE MATERIAIS ESCOLARES':^50}")
print('*'*50)
for item in range(0,len(lista)):
    if item%2 == 0:
        print(f'{lista[item]:.<40}', end=' ')
    else:
        print(f'R${lista[item]:>10.2f}'),
print('*'*50)
