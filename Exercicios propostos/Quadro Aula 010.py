

print('\033[30mTESTE\033[m')

num = int(input('Digite um numero para converter'))

print('''O numero ficaria:
Binario: {}
Hexadecimal: {}
Octal: {}'''.format(bin(num)[2:], hex(num)[2:], oct(num)[2:]))