distancia = float(input('Digite a distancia da vigem: '))
preço1 = distancia * 0.50
preço2 = distancia * 0.45

if distancia <= 200:
    print(f'O preço da passagem é: R${preço1:.2f}')
else: 
    print(f'O preço da passagem é: R${preço2:.2f}')