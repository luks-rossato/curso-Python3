tn = 0
tpn = 1
aux = 0
n = int(input('Digite a quantidade de termos de fibonacci que quer ver:'))
count = 2
if n <= 1:
    print('0')
if n == 2:
    print('0\n1')
else:
    print('0\n1')
    while count < n:
        aux = tpn
        tpn = tpn + tn
        tn = aux
        print('{}'.format(tpn))
        count += 1