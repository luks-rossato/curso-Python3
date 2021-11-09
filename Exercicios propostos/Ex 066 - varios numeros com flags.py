n = s = count = 0

while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
    count += 1
print(f'A Soma de todos os {count} elementos foi {s}')