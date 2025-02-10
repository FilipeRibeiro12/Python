from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'em que ano a {c}° pessoa nasceu ? '))
    if ano <= date.today().year:
        if date.today().year - ano >= 21:
            maior += 1
        if date.today().year - ano < 21:
            menor += 1
    else:
        print('POR FAVOR DIGITE UM ANO MENOR QUE O ANO ATUAL')
if maior >= 1:
    print(f'{maior} Pessoas são maiores de idade')
if menor >= 1:
    print(f'{menor} Pessoas são menores de idade')