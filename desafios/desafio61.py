t = int(input('DIGITE O PRIMEIRO TERMO DE UMA PA: '))
r = int(input('DIGITE A RAZÃO DE UMA PA: '))
t10 = 11
cont = 1
while cont != t10:
    t = + cont * r
    cont += 1
    print(t, end = " --> " )
print('ACABOU')