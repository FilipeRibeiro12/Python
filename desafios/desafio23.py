numero = str(input('Digite um numero inteiro de 0 a 9999: ').zfill(4))
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]
print(f'''  A unidade = {unidade}
      A dezena = {dezena}
      A centena = {centena}
      O milhar = {milhar}''')