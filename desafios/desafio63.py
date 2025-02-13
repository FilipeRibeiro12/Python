n = int(input('DIGA A QUNTIDADE DE ELEMENTOS DE UMA SEQUUENCIA DE FIBONACCI: '))
cont = 0
f = 0
while cont != n:
    cont += 1
    f = f * (cont -1) + f * (n -2)
    print(f, end = ' --> ')
print('ACABOU')