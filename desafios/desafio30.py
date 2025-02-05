n = (input('Digite um numero inteiro: '))
if n.isdigit():
    numero = int(n)

    if numero % 2 == 0:
        print('Seu numero é par')
    else:
        print('Seu numero é impar')
        
else:
    print('Por favor, digite um numero inteiro válido.')