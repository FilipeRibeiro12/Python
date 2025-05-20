galera = list()
dado = list()
for c in range(0, 3):
  dado.append(str(input('Qual o seu nome ?')))
  dado.append(int(input('Qual a sua idade ?')))
  galera.append(dado[:])
  dado.clear()

for p in galera:
  if p[1] >= 21:
    print(p)