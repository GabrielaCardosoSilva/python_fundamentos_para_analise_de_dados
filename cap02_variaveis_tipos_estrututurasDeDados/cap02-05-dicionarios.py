# Dicionários são declarados com {} e são compostos por uma chave e um valor
# Chave : valor
dicionario = {"chave1":"valor1", "chave2":"valor2", "chave3":"valor3"}

# Retornar valor através da chave
dicionario["chave2"]

# Adicionar uma chave e um valor
dicionario["chave4"] = "valor4"

# Limpar um dicionário
dicionario.clear()

# Excluir um dicionário
del dicionario

# Retornar o comprimento de um diocionario
len(dicionario)

# Retornar apenas as chaves do dicionario
dicionario.keys()

# Retornar apenas os valores do dicionario
dicionario.values()

# Retornar os itens do dicionário (chave:valor)
dicionario.items()

# Atualizar um dicionário a partir de outro
dicionario2 = {"chave5":"valor5", "chave6":"valor6", "chave7":"valor7"}
dicionario.update(dicionario2)

# Criar um dicionário de lista
dicionario3 = {"chave1":"valor1", "chave2":["valor2", "valor2.1", "valor2.2"], "chave3":"valor3"}

# Acessar um item da lista dentro do dicionário
dicionario3["chave2"][1]

# Operações com itens da lista
dicionario3["chave2"][1] + 2
dicionario3["chave2"][1] -= 2

# Dicionário aninhado
dict_aninhado = {'Chave1':{'Chave2_aninhada':{'Chave3_aninhada':'Dict aninhado em Python'}}}

# Para acessar o dicionário aninhado
dict_aninhado['Chave1']['Chave2_aninhada']['Chave3_aninhada']