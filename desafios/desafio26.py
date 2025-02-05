frase = str(input('Digite uma frase: ')).strip()
letras_A = frase.lower().count('a')
posicao_0A = frase.lower().find('a') + 1
posicao_1A = frase.lower().rfind('a') + 1

print(f'''Na sua frase tem {letras_A} letras 'a'
    A letra 'a' aparece na posição {posicao_0A} pela primeira vez
      E aparece na posição {posicao_1A} pela ultima vez  ''')