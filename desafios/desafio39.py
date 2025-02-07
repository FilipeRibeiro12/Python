from datetime import date

nome = str(input('Digite seu nome: ')).strip()
id = input('Digite sua idade: ').strip()
ano = date.today().year

if id.isdigit():

    idade = int(id)
    nascimento = ano - idade
    alistar = nascimento + 18
    
    print('Qual é o seu sexo ? digite "1" para masculino e "2" para feminino.')

    sexo = int(input(''))
    if sexo == 1:
        print(f'Olá {nome}, você tem a obrigatoriedade de se alistar')
        if alistar > ano:
            print(f'Você deverá se alistar em {alistar}, faltam {alistar - ano} anos')
        elif alistar == ano:
            print('Você deverá se alistar este ano')
        else:
            print(f'Você deveria ter se alistado em {alistar}, passou do prazo {idade - 18} anos')
    elif sexo == 2:
        print(f'Olá {nome} Você não tem obrigatoriedade de se alistar')
    else:
        print('Por favor, digite uma alternativa valida')

else:
    print('Por favor, Digite somente seu nome e somente os numeros da sua idade.')
