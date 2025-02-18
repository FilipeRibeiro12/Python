t = int(input('DIGITE O PRIMEIRO TERMO DE UMA PA: '))
r = int(input('DIGITE A RAZÃO DE UMA PA: '))
t10 = 10
cont = 0

while cont != t10:
    pa = t + cont * r
    cont += 1
    print(pa, end = ' --> ')
    if cont == t10:
        print('VOCÊ QUER QUE CONTINUE A CONTAR ? [S/N] ')
        escolha = str(input('')).upper().strip()
        if escolha == 'S':
            print('QUER QUE AUMENTE QUANTOS TERMOS ? ')
            tmais = int(input(''))
            t10 += tmais
            print(pa, end = ' --> ')
print(f'PROGRESSÃO FINALIZADA COM {cont} termos')