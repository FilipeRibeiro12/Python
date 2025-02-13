n = int(input('Digite um numero inteiro: '))
cont = 1
fat = 1
while cont != n:
    cont += 1
    fat *= cont
print(f'O fatorial de {n}, é {fat}')
