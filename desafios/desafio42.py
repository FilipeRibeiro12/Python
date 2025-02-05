r1 = input('Digite o primeiro segmento de reta.')
r2 = input('Digite o segundo segmento de reta.')
r3 = input('Digite o terceiro segmento de reta.')

if r1.isdigit() and r2.isdigit() and r3.isdigit():
     reta1 = float(r1)
     reta2 = float(r2)
     reta3 = float(r3)

     if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
              if reta1 == reta2 and reta1 == reta3:
                    print('Você formou um triangulo equilatero')
              elif reta1 == reta2 and reta1 != reta3 or reta1 == reta3 and reta1 != reta2 or reta2 == reta3 and reta2 != reta1:
                    print('Você formou um triangulo isóceles')
              else:
                    print('Você formou um triangulo escaleno')
     else:
          print('Nao é um triangulo')
else:
     print('Por favor, digite somente numeros')