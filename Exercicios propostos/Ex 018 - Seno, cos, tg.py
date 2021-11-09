import math

a = float(input('Informe o angulo: '))
a = math.radians(a)
print(a)

print('Para o angulo temos:\nsen = {:.0f}\ncos = {:.0f}\ntan = {:.0f}'.format(math.sin(a), math.cos(a), math.tan(a)))