nj = npc = count = aux = 0
esc = ''
import random
print('VAMOS JOGAR PAR OU IMPAR!')
while True:
    esc = input('Par ou Impar?')
    esc = esc.upper()
    nj = int(input('1..2..3..e:'))
    npc = random.randint(0,100000)
    aux = nj + npc
    if aux%2 == 0 and esc == 'PAR':
        break
    elif aux%2 != 0 and esc == 'IMPAR':
        break
    count += 1
print(f'O joog acabou e você teve {count} vitórias consecutivas!')