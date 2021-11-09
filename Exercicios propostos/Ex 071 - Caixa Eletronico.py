aux = aux2 = aux3 = 0.0

while True:
    valor = float(input('Digite o valor a ser sacado:'))
    aux = valor%50
    aux = aux/50
    aux2 = valor/50
    aux3 = aux2-aux
    if aux3 != 0:
        print(f'{aux3:.0f} notas de R$ 50\n')
    valor = valor - 50*aux3
    aux = valor % 20
    aux = aux / 20
    aux2 = valor / 20
    aux3 = aux2 - aux
    if aux3 != 0:
        print(f'{aux3:.0f} notas de R$ 20\n')
    valor = valor - 20 * aux3
    aux = valor % 10
    aux = aux / 10
    aux2 = valor / 10
    aux3 = aux2 - aux
    if aux3 != 0:
        print(f'{aux3:.0f} notas de R$ 10\n')
    valor = valor - 10 * aux3
    aux = valor%5
    aux = aux / 5
    aux2 = valor/5
    aux3 = aux2-aux
    if aux3 != 0:
        print(f'{aux3:.0f} notas de R$ 5\n')
    valor = valor - 5*aux3
    aux = valor % 1
    aux = aux / 1
    aux2 = valor / 1
    aux3 = aux2 - aux
    if aux3 != 0:
        print(f'{aux3:.0f} notas de R$ 1\n')

    cont = str(input('Quer continuar? [S/N]')).upper()
    if cont == 'N':
        break