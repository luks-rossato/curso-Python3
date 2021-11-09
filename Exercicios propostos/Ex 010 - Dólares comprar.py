din = float(input("Quantos reais você tem?"))

if din>1000 :
    print('UAU! Você pode comprar {:.2f} dólales'.format(din/3.27))
else :
    print('Talkey! Você pode comprar {:.2f} dólales'.format(din/3.27))