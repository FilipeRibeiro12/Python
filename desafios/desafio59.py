import time
print('=' * 12)
print('CALCULADORA')
print('='* 12)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:
    time.sleep(1)
    escolha = int(input('''Escolha as opções entre 1 e 5: 
          [1] SOMAR OS VALORES DIGITADOS
          [2] MULTIPLICAR OS VALORES DIGITADOS
          [3] SABER QUAL È O MAIOR DOS VALORES DIGITADOS
          [4] DIGITAR NOVOS VALORES
          [5] SAIR DA CALCULADORA 
                        '''))
    soma = n1 + n2
    mult = n1 * n2
    if escolha == 1:
        print(f'A soma dos valores digitados é {soma} ')
    if escolha == 2:
        print(f'O produto dos valores é {mult} ')
    if escolha == 3:
        if n1 > n2:
            print(f'O valor {n1} é maior que o valor {n2}')
        elif n1 == n2:
            print(f'O valor {n1} é igual ao {n2}')
        else:
            print(f'O valor {n2} é maior que o valor {n1}')
    if escolha == 4:
        n1 = int(input('Digite o primeiro novo valor: '))
        n2 = int(input('Digite o segundo novo valor: '))
print('Você saiu da calculadora')
