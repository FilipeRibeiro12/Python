from  time import sleep
maismil = 0
menor = 0
cont = 0
total = 0
nomemenor = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maismil += 1
    if cont == 1:
        menor = preco
        nomemenor = nome
    if preco < menor:
        menor = preco
        nomemenor = nome
    pergunta = str(input('Você deseja passar mais algum produto ? [S/N] ')).strip().upper()[0]
    while True:
        if pergunta not in 'SN':
            print('\033[31mPOR FAVOR DIGITE UMA ALTERNATIVA VALIDA\033[m')
            pergunta = str(input('Você deseja passar mais algum produto ? [S/N] ')).strip().upper()[0]
        else:
            break
    if pergunta == 'N':
        print('FINALIZANDO A COMPRA...')
        sleep(1)
        break
print(f'O total gasto na compra é de R${total:.2f}')
print(f'Na sua compra existem {maismil} produtos que custam mais de R$1000,00')
print(f'O nome do produto com o menor preço é {nomemenor}, que custa {menor}')
