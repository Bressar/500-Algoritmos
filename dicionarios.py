# Dicionários

# 2 maneiras de criar um dicionário
dados1 = {"nome": "Creuza", "idade": 99, "telefone": "93312-2402"}

dados2 = dict(nome="Oldaque", idade=102, telefone= "1234-2345")

print(f'{dados1} \n{dados2}')

# para mudar os itens:
dados1["nome"] = 'Chica'
dados1["idade"] = 77
dados1["telefone"] = "1234-0987"

print(dados1)

# Dicionário aninhados - igual a um banco de dados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

extra =contatos["melaine@gmail.com"]['extra']["a"]
print(extra)

# Iterar em um dicionário

for chave in contatos:
    print(chave, contatos[chave])

contatos["nova chave: "] = "valor da nova chave"

for chave, valor in contatos.items():
    print(chave, valor)
    
    
    # Métodos

contatos.clear() # {} -> apaga tudo

# copy
    
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}   


# fromKeys   
# Retorna None se não tiver um item definido, só a chave

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# Determina uma palvra para ficar no lugar do 'NONE'
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
resultado = dict.fromkeys(["nome", "telefone"], "Abable") 
print(resultado)


print('---' * 20)
# Método GET

contatos = {"odete@gmail.com": {"nome": "Odete", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError - se a chave não existir no dicioanrio dá erro
print(contatos["odete@gmail.com"])

resultado = contatos.get("chave")  # None se não existir no get dá None
print(resultado)

resultado = contatos.get("chave", 'não encontrado!')  # {} pode definir um valor default se não encontrar a chave
print(resultado)

resultado = contatos.get(
    "odete@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)


# Items retorna uma lista iterável

print(contatos.items()) # dict_items([('odete@gmail.com', {'nome': 'Odete', 'telefone': '3333-2221'})])

# Keys

novo= {"a": 1, "b": 2, "c": 3}

resultado = novo.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)


# POP

# remove a chave ou remove e deixa um valor default

resultado = novo.pop('a') # mostra o item removido
print(resultado)

resultado = novo.pop('a', 'não encontrou!')
print(resultado)


# popitem

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)


# contatos.popitem()  # KeyError se estiver vazio


# Set default -> adiciona uma chave/item se ela não existir
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # não troca, mantém # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) # se não existe a chave, ele adiciona  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}


# Update 
# Atualiza um dado existente ou acrescenta um novo
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}}) # atualiza
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}) # acrescenta
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)


# Values -> retorna os values 

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)

# In


resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)


# Del

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)

del contatos # apaga tudo

print(contatos) # Erro, pq foi apagado