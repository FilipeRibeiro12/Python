from datetime import date
ano = int(input('Digite um ano: Para analizar o ano atual, digite 0 '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano}, é um ano bissexto.')
else:
    print(f'o ano {ano}, não é um ano bissexto')