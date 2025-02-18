nome = str(input('NOME: '))
sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('POR FAVOR DIGITE UMA ALTERNATIVA VALIDA')
    sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
print('OBRIGADO !!!')