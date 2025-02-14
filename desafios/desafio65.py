pergunta = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while pergunta == 'S':
    n = int(input('\033[33m DIGITE UM NUMERO INTEIRO:\033[m '))
    pergunta = str(input('\033[33m DESEJA DIGITAR MAIS UM NUMERO ?\033[m ')).upper().strip()
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else :
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print(f'\033[33mO maior valor digitado é \033[31m{maior}\033[m')
print(f'\033[33mO menor valor digitado foi o \033[31m{menor}\033[m')
print(f'\033[33mA soma dos valores digitados é \033[31m{soma}\033[m \033[33me a media é igual a \033[31m{media:.2f}\033[m')
