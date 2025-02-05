preço = float(input('Qual o preço do produto ? '))
avista = preço * 0.90
avistaCartao = preço * 0.95
cartao3 = preço * 1.20

print('''Qual a forma de pagamento do produto ?
      Digite 1 para à vista em dinheiro ou cheque para ter 10% de desconto
      Digite 2 para à vista no cartão para ter 5% de desconto
      Digite 3 para dividido no cartão em ate 2x sem juros
      Digite 4 para dividido no cartão em 3x ou mais com juros de 20%
      ''')
escolha = int(input(''))

if escolha == 1:
    print(f'O preço do produto à vista com 10% de desconto é de R${avista:.2f}')
elif escolha == 2:
    print(f'O preço à vista no cartão tem 5% de desconto é de R${avistaCartao:.2f}')
elif escolha == 3:
    print(f'O preço do produto divido no cartão em ate 2x sem juros é R${preço}')
else:
    print(f'O preço do produto divido 3x no cartão é {cartao3}')