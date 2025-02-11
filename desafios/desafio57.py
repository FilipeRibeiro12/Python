nome = ''
sexo = ''
while sexo != 'M' and sexo != 'F':
    nome = str(input('NOME: '))
    sexo = str(input('SEXO [M/F]: ')).upper().strip()
    print('POR FAVOR DIGITE UMA ALTERNATIVA VALIDA')
print('OBRIGADO !!!')