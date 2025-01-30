# Python
CURSO EM VIDEO PYTHON

* É uma linguagem de proposito geral
* Multiplataforma
* batteries inclded
* livre
* Orientada a objetos
* Muitas bibliotecas

![alt text](image.png)

# Principais áreas
* Inteligência Artificial
* Biotecnolgia
* Computação 3D

# Quem usa Python
* ZOPE
* Air Canada
* BitTorrent
* Globo
* Google
* YouTube
* Nasa
* Industrial Light&Magic
* AutoDesk

# Tipos Primitivos e Saidas de Dados
* int()➡ tudo dentro do parentese é número inteiro
* float()➡ número reais
* bool()➡ valores lógicos ou booleanos
* str()➡ valores caractere ou strings

![alt text](image-1.png)
![alt text](image-2.png)

# trabalhando com Módulos
* import nome-do-modulo
para importar somente uma função do modulo
* from nome-modulo import nome-função

* ou pip install nome-do-modulo

# Manipulando cadeias de texto

* Fatiamento
![alt text](image-3.png)

* Analise
frase = 'Curso em video Python'

len(frase) --> espaço ou tamanho
frase.count('o') --> contar as vezes que aparece o caractere
frase.find('deo') --> encontrar o caractere
frase.fase('Android') --> quando colocar string que nao existe, recebe valor -1
'Curso' in frase --> existe a palavra curso na frase 

* Transformação

frase.replace('Python', 'Android') --> Troca a primeira palavra pela segunda
frase.upper() --> transforma os caracteres em maiusculos
frase.lower() --> transforma os caracteres em minusculas
frase.captalize() --> coloca somente o primeiro caractere em maiusculo 
frase.title() --> transforma o primeiro caractere de cada palavra na string em maiusculo
frase.strip() --> remove todos os espaços inuteis da string
frase.rstrip() --> remove somente os ultimos espaços
frase.lstrip() --> remove somente os primeiros espaços

* Divisão

frase.split() --> divide os espaços da string, cada palavra recebe uma indexação nova

* Junção

'-'.join(frase) --> juntar a string que foi separada