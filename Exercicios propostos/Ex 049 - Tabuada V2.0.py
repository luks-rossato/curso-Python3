n = int(input('Digite o numero que gostaria de ter a tabuada: '))

for i in range(0,11):
    print('{} x {} = {}'.format(i, n, n*i))