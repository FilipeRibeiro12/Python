ValorCasa = float(input('Qual é o valor da casa ? '))
Salario = float(input('Qual é o seu salario ? '))
Anos = int(input('Em quantos anos você vai pagar a casa ? '))
Mes = Anos * 12
Prestacao = ValorCasa / Mes

print(f'O valor da prestação mensal é de R${Prestacao:.2f} ')
if Prestacao > Salario * 0.30:
    print('Seu emprestimo foi negado pois as parcelas mensais excederam 30% do seu salario')
else:
    print('PARABENS!!! Seu emprestimo foi aprovado')