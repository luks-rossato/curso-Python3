

a = int(input('Digite o valor "a"'))
b = int(input('digite o valor "b"'))
cmd = 0

while cmd != 1:
    print("""
    Digite a opção desejada:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    dig = int(input(''))
    if dig == 1:
        print('A soma dos valores é: {}'.format(a+b))
    elif dig == 2:
        print('A multiplicação dos valores é: {}'.format(a*b))
    elif dig == 3:
        if a > b:
            print('O maior valor é o "a", que é {}'.format(a))
        else:
            print('O maior valor é o "b", que é {}'.format(b))
    elif dig == 4:
        a = int(input('Digite o novo valor "a":'))
        b = int(input('digite o novo valor "b":'))
    elif dig == 5:
        cmd = 1
        break

