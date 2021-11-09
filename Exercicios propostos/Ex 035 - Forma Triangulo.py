r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if (r1+r2)>r3 and (r3+r2)>r1 and (r1+r3)>r2 :
    print("Formam um triângulo!")
else:
    print('Não formam um triângulo!')