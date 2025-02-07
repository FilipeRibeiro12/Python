name = input('Qual é o seu nome ? ').strip()
id = input('Qual é a sua idade ? ')

if id.isdigit() and name.replace(' ', '').isalpha():

    idade = int(id)
    nome = str(name)

    if idade <= 9:
        print(f'Olá {nome}, sua categoria é a MIRIM')
    elif idade <= 14:
        print(f'Olá {nome}, sua categoria é a INFANTIL')
    elif idade <= 19:
        print(f'Olá {nome}, sua categoria é a JUNIOR')
    elif idade <= 25:
        print(f'Olá {nome}, sua categoria é a SENIOR')
    else:
        print(f'Olá {nome}, sua categoria é a MASTER')
else:
    print('Digite Somente seu nome e os numeros da sua idade.')