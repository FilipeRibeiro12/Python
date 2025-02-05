salario = float(input('Qual o seu salario ? '))

if salario > 1250:
    print('você tem direito a 10% de aumento')
    print(f'Seu salario de R${salario}, vai para R${salario * 1.10:.2f}')
else: 
    print('Você tem direito a 15% de aumento')
    print(f'Seu salario de R${salario}, vai para R${salario * 1.15:.2f}')
