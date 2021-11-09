n = 0

while True:
    n = int(input('Digite um numero:'))
    if n < 0:
        break
    print(f"TABUADA DO {n}")
    for i in range(0,11):
        print(f'{i} x {n} = {i*n}')
print('FIM DO JOGO!')