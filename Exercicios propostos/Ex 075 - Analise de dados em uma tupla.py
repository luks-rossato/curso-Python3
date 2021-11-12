p1 = int(input('Digite um valor:'))
p2 = int(input('Digite outro valor:'))
p3 = int(input('Digite mais um valor:'))
p4 = int(input('Digite o último valor:'))

tupla = (p1, p2, p3, p4)

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) != 0:
    print(f'O valor 3 foi digitado na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado!')
print('Os valores pares encontrados foram:')
for c in tupla:
    if c%2 == 0:
        print(c)