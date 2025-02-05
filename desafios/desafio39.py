nome = str(input('Digite seu nome: ')).strip()
id = input('Digite sua idade: ').strip()

if id.isdigit():
    idade = int(id)

    print('Qual é o seu sexo ? digite "1" para masculino e "2" para feminino.')
    sexo = int(input(''))
    if sexo == 1:
       print(f'Olá {nome}, você se fudeo')
    elif sexo == 2:
        print(f'Olá {nome} Você não tem obrigatoriedade de se alistar')
    else:
        print('Por favor, digite uma alternativa valida')

else:
    print('Por favor, Digite somente seu nome e somente os numeros da sua idade.')


