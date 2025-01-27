dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros rodados teve nestes dias ? '))
preço = dias * 60 + km * 0.15
print(f'O Preço do carro por esses {dias} dias, e pelos {km}km rodados é: R${preço:.2f}')