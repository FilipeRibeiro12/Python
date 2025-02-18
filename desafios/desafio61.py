t = int(input('DIGITE O PRIMEIRO TERMO DE UMA PA: '))
r = int(input('DIGITE A RAZÃO DE UMA PA: '))
cont = 0
pa = 0
while cont != 10:
    pa = t + r * cont
    cont += 1
    print(pa, end = " --> " )
print('ACABOU')