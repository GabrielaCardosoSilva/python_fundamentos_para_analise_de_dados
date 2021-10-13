# Uma única palavra
print('Oi')

# Uma frase
print('Criando uma string em Python')

# Com aspas duplas
print("Podemos usar aspas duplas ou simples para strings em Python")

# Combinar aspas duplas e simples
print("Testando strings em 'Python'")

# Quebra de linha
print ('Testando \nStrings \nem \nPython')
print ('\n')

# Atribuir uma string
s = 'Data Science Academy'

# Imprimir strings
print(s)

# Primeiro elemento da string. 
print(s[0])

# Segundo elemento da string. 
print(s[1])

# Retornar todos os elementos da string, começando pela posição 1( até o fim da string.
s[1:]

# Retorna tudo até a posição 3
s[:3]

#retornar toda a string
s[:]

# Usar a indexação negativa e ler de trás para frente.
s[-1]

# Retornar tudo, exceto a última letra
s[:-1]

# Retornar a string toda, saltando a cada 1 caractere
s[::1]

# Retornar a string toda, saltando a cada 2 caracteres
s[::2]

# Retornar a string toda, saltando a cada 1 caractere, ao contrário
s[::-1]

# Concatenar strings
s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'
s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'

# Multiplicar strings
letra = 'w'
letra * 3

# ### Funções Built-in de Strings
# Upper Case 
s.upper()

# Lower case
s.lower()

# Dividir uma string por espaços em branco (padrão)
s.split()

# Dividir uma string por um elemento específico
s.split('y')

# ### Funções String
s = 'seja bem vindo ao universo de python'

# Tornar a string maiúscula
s.capitalize()

# Contar quantas letras 'a' existem
s.count('a')

# Encontrar a posição da letra 'p'
s.find('p')

# Centralizar a string em 20 espaços e preencher com o caracter 'z'
s.center(20, 'z')

# Verificar se o conteúdo é numérico
s.isalnum()

# Verificar se o conteúdo é alfanumérico
s.isalpha()

# Verficar se possui apenas letras minúsculas
s.islower()

# Verficar se possui apenas espaços
s.isspace()

# Verficar se termina com a letra 'o'
s.endswith('o')

# Divide a string em 3 elementos:
# 1) tudo antes de '!'
# 2) o elemento '!'
# 3) tudo depois de '!'
s.partition('!')

# Comparação de Strings
print("Python" == "R")
print("Python" == "Python")

# script desenvolvido com base no material didático da DSA.
