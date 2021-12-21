# Listas são criadas com []
lista = ["item 1", "item 2", "item 3"]

# Imprimir a lista
print(lista)

# Atribuir valores da lista à variáveis
v1 = lista[0]
v2 = lista[1]
v3 = lista[2]

# Imprimir apenas 1 item da lista
print(lista[0])

# Atualizar lista
lista[2] = "new item 3"

# Deletar um item da lista
del lista[1]

# Criar uma lista aninhada 
# Em python, listas de listas são matrizes
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Atribuir um item da lista/matriz a uma variável
# O exemplo abaixo guardará [1, 2, 3]
a = matriz[0]

# Para guardar apenas 1 item
b = a[0]

# --------- OPERAÇÕES COM LISTAS ---------

# Atribuir à variável o valor da primeira linha e coluna da matriz
# [linha][coluna]
c = matriz[0][0]

# Operações
d = matriz[0][1] + 2
e = matriz[0][1] - 2
f = matriz[0][1] * 2
g = matriz[0][1] / 2

# Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_total = lista1 

# --------- OPERADOR IN ---------
# Verificar se o número 5 está na lista
lista_teste = [1, 2, 3, 4, 5]
print(5 in lista_teste)

# --------- FUNÇÕES BUILT-IN ---------

# Retornar o comprimento da lista
len(lista_teste)

# Retorna o valor máximo da lista
max(lista_teste)

# Retornar o valor mínimo da lista
min(lista_teste)

# Adicionar um item à lista
lista_teste.append(6)

# Contar o número de ocorrências de um item em uma lista
lista_teste.count(2)

# Verificar o tipo
type(lista_teste)

# Copiar os itens de uma lista para outra 
old_list = [1, 2, 3]
new_list = []

for i in old_list:
    new_list.append(i)

# Adicionar itens ao final de uma lista
lista_teste.extend([4, 5, 6, 7])

# Retornar o índice de um item na lista
lista_teste.index(7)

# Inserir na posição 2, o valor 100
lista_teste.insert(2, 100)

# Remover um item da lista
lista_teste.remove(100)

# Reverter a lista
lista_teste.reverse()

# Ordenar a lista
lista_teste.sort()