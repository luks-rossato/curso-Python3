lista = list()
quer = 's'
while True:
    if input('Quer continuar?[s/n]') == 'n':
        break
    v = int(input('Digite um valor pra por na lista: '))
    lista.append(v)
print(f'Foram digitados {len(lista)} valores!\n')
lista.sort(reverse=True)
for i in range(0,len(lista)):
    print(f'Lista[{i}] = {lista[i]}')

if 5 in lista:
    print('o 5 está na lista!')
else:
    print('O 5 não esta na lista!')
