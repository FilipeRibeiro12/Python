print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
lista = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.40,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)

for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end ='')
    if pos % 2 == 1:
        print(f'R${lista[pos]:7.2f}')
print('-'*40)
