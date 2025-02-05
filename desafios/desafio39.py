nome = str(input('Digite seu nome: ')).strip()
id = input('Digite sua idade: ').strip()

if id.isdigit():
    idade = int(id)
    
    print('''Qual é o seu sexo ? 
          digite "1" para masculino e "2" para feminino. ''')
    
    sexo = input('').strip

    if sexo == 1:
        print('Voce se fudeo')
    
else:
    print('Digite somente números')


