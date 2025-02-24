numeros = ('zero','um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um numero de 0 à 20: '))
    if n < 0 or n > 20:
        print('Tente novamente ')
    else:
        print(f'Você digitou o numero {numeros[n]}')
        break
    