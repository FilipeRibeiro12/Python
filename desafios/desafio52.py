numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    n = int(numero)

    if n < 2: # numeros menor que dois nnão são primos
        print(f'O numero {n} NÃO é primo')
    else:
        contador = 0 # Conta quantos divisores o numero tem

        for c in range(1, n + 1): # Testa os numeros de 1 até n
            if n % c == 0: # se for divisível incrementa o contador
                contador +=1
        if contador == 2: # Se o contador tiver exatamente 2 divisores, é primo
            print(f'O numero {n} é primo')
        else:
            print(f'O numero {n} NÃO é primo')

else:
    print('POR FAVOR, DIGITE UM NUMERO INTEIRO VALIDO')