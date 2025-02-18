print('-'*36)
print('BEM VINDO AO PROGRAMA DA TABUADA')
print('-'*36)
c = 0
while True:
    n = int(input('DIGITE UM NUMERO PARA VER SUA TABUADA: '))
    if n < 0:
        break
    else:
        c+=1
        t = n * c
    print(f'{n} X {c} = {t}')
print('ACABOU')
