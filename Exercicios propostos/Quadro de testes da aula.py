#1 = int(input('Digite o primeiro valor:'))
#2 = int(input('Digite o segundo valor: '))

#res = n1//n2

#print('A operação entre os numeros resultou em ', res)




#nome = input('Digite seu nome: ')

#print('Prazer em te conhecer {:=^20}! Como você está?'.format(nome), end='>>>>>>')
#print('Just testing from this point on')


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))
for pos, c in enumerate(lanche):
    print(f'Vou comer {c} na ordem {pos}')

a = (1,2,3)
b = (4,5,6)
c = a + b
print(c)
c += c
print(c)