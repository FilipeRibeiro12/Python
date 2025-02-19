cp = 0
cm = 0
cf20 = 0
while True:
    nome = str(input('NOME: ')).strip().upper()
    idade = input('IDADE: ')
    while True:
        if idade.isdigit():
            id = int(idade)
            break
        else:
            print('POR FAVOR DIGITE SOMENTE NUMEROS')
            idade = input('IDADE: ')
    sexo = str(input('SEXO: [M/F]')).strip().upper()[0]
    while True:
        if sexo not in 'MF':
            print('POR FAVOR DIGITE UMA ALTERNATIVA VALIDA')
            sexo = str(input('SEXO: [M/F]')).strip().upper()[0]
        else:
            break
    pergunta = str(input('Você quer cadastrar mais uma pessoa ? [S/N]')).upper().strip()[0]
    while True:
        if pergunta not in 'SN':
            print('POR FAVOR DIGITE SOMENTE S ou N')
            pergunta = str(input('Você quer cadastrar mais uma pessoa ? [S/N]')).upper().strip()[0]
        else:
            break  
    if id > 18:
        cp += 1
    if sexo == 'M':
        cm += 1
    if id < 20 and sexo == 'F':
        cf20 += 1
    if pergunta == 'N':
        break
print(f'''Nas pessoas que você cadastrou:
Existem {cp} pessoas com mais de dezoito anos.
Existem {cm} homens cadastrados.
Existem {cf20} mulheres cadastradas com menos de vinte anos.''')
