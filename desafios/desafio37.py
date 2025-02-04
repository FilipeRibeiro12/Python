n = input('Digite um número inteiro: ').strip()

if n.isdigit():
    numero = int(n)
    binario = bin(numero)[2:]
    octal = oct(numero)[2:]
    hexadecimal = hex(numero)[2:].upper()

    print(f'Escolha "1" para converter {numero} para Binario:')
    print(f'Escolha "2" para converter {numero} para Octal:')
    print(f'Escolha "3" para converter {numero} para hexadecimal:')

    escolha = int(input(''))


    if escolha == 1:
        print(f'O Valor {numero}, em sua forma binaria é {binario}')
    elif escolha == 2:
        print(f'O valor {numero}, em sua forma octal é {octal} ')
    elif escolha == 3:
        print(f'O valor {numero}, em sua forma hexadecimal é {hexadecimal} ')
    else:
        print('Escolha uma opção valida por favor')
else:
    print('Digite um numero válido')

