extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    c = int(input('Digite um numero:'))
    if 0 <= c <=20:
        break
    print('Digite um numero válido entre 0 e 20!')

print(f'Voce digitou o numero {c}, por extenso seria {extenso[c]}')