import math
c1 = float(input('Digite o valor do cateto oposto '))
c2 = float(input('Digite o valor do cateto adjacente '))
h = math.sqrt(pow(c1,2)+pow(c2,2))
print(f'O comprimento da hipotenusa é {h:.2}')