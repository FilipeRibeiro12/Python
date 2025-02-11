totid = 0
media = 0
maioridhomem = 0
nomevelho = ''
totfem20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('NOME: ')).upper().strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper().strip()
    totid += idade
    if p == 1 and sexo == 'M':
        maioridhomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridhomem:
        maioridhomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totfem20 += 1

media = totid / 4 
print(f'A media de idade do grupo é de {media} anos.')
print(f'O homem mais valho tem {maioridhomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totfem20} mulheres que tem menos que 20 anos.')
    