razao = int(input('Digite a Razão da P.A.: '))
prim = int(input('Informe o primeiro termo da P.A.: '))

for i in range(0,11):
    print('O termo {} é o : {}'.format(i, prim+(razao*i)))