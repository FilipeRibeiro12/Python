n = int(input('Digite um numero inteiro: '))
cont = n
fat = 1
print(f'Calculando {n}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f'{fat}')