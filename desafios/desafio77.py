palavras = ('aprender', 'perder', 'destino', 'logica', 'carinho', 'teste', 'sono')

for p in palavras:
    print(f'\nNa palavra {p.upper()}, temos ', end = '')

    for l in p:
        if l.lower() in 'aeiou':
            print(f'{l}', end = ' ')