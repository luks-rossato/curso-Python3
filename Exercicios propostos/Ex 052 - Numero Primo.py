count = 0

n = int(input('Digite o numero que quer saber se é primo: '))

for i in range(1,n+1):
    if(n%i == 0):
        count += 1
if count == 2 :
    print('O numero {} é um numero primo!'.format(n))
else:
    print('O numero {} NÂO é primo!'.format(n))