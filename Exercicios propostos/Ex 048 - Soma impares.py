s = 0

for i in range(0,501):
    if(i%2 != 0):
        if(i%3 == 0):
            s += i
print('A soma dos impares multiplos de 3 foi: {}'.format(s))