n1 = input('Digite um numero inteiro: ').strip()
n2 = input('Digite outro numero inteiro: ').strip()

if n1.isdigit() and n2.isdigit():
    num1 = int(n1)
    num2 = int(n2)

    if num1 > num2:
        print(f'O numero {num1} é o maior')
    elif num1 < num2: 
        print(f'O numero {num2} é o maior')
    else: 
        print(f'Os numeros {num1} e {num2}, são iguais ')

else:
    print('Digite um numero inteiro válido')