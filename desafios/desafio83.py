expressao = str(input('Digite uma expressão: '))
pilha = list()
for simb in expressao:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break

if len(pilha) == 0:
  print('Sua expressao está correta!')
else:
  print('Sua expressao não é valida!')