from time import sleep
numeros = ('zero','um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um numero de 0 à 20: '))
    if n < 0 or n > 20:
        print('Tente novamente ')
    else:
        print(f'Você digitou o numero {numeros[n]}')
        pergunta = str(input('Você quer continuar ? [S/N]')).upper()
    
        if pergunta == 'S':
            sleep(0.5)
        elif pergunta == 'N':
            print('FINALIZANDO...')
            sleep(0.5)
            break
        while True:
            if pergunta not in 'SN':
                print('Tente uma alternativa valida')
                pergunta = str(input('Você quer continuar ? [S/N]')).upper()
            else:
                break
print('VOLTE SEMPRE')
    