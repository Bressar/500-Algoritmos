# Algoritmo 69
# Ler o nome do aluno e indicar em qual sala ele fará a prova.
# São 3 salas:
# A - K : sala 101
# L - N : sala 102
# O - Z : sala 103
# depois de concluido, gravar essas listas em um banco de dados, lista em JSON

import sqlite3
import json

sala_101 = []
sala_102 = []
sala_103 = []

while True:
    # Entrada do nome e validação
    while True:
        try:
            print('--' * 30)
            nome_estudante = input("Digite o nome do(a) estudante: ").strip().title()
            if not all(part.isalpha() for part in nome_estudante.split()):
                raise ValueError("O nome deve conter apenas letras.")
            else:
                break
        except ValueError:
            print("Valor inválido! tente novamente!")

    # Determinação da sala
    primeira_letra = nome_estudante[0]
    if 'A' <= primeira_letra < 'L':
        sala_101.append(nome_estudante)
        nome_sala = 101
    elif 'L' <= primeira_letra < 'O':
        sala_102.append(nome_estudante)
        nome_sala = 102
    else:
        sala_103.append(nome_estudante)
        nome_sala = 103
        
    print(f'O aluno(a) {nome_estudante} fará a prova na sala {nome_sala}') # for debug
    print('--' * 30)
    sair = input('Para continuar pressione [C] ou [S] para sair: \n').upper()
    if sair == "S":
        print("Encerrando programa...")
        print('--' * 30)
        break


# função exibir listas
def imprimir_lista_sala(nome_sala=" ", nome_lista=[]):
    print('--' * 20)
    print("Lista de alunos na", nome_sala)
    for aluno in sorted(nome_lista):
        print(aluno, end = "\n")

    
imprimir_lista_sala("sala 101", sala_101)
imprimir_lista_sala("sala 102", sala_102)
imprimir_lista_sala("sala 103", sala_103)


# Gravar dados das listas em um banco de dados
# Banco de Dados Relacional (SQL)

conn = sqlite3.connect("database/alunos.db")
cursor = conn.cursor()

# Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sala INTEGER NOT NULL
)
""")
conn.commit()

#Funçaõ para inserir os alunos no Banco de dados
def inserir_alunos(nome, sala):
    cursor.execute("INSERT INTO alunos (nome, sala) VALUES (?,?)", (nome, sala))
    conn.commit()

# Exemplo de inserção
for aluno in sala_101:
    inserir_alunos(aluno, 101)
for aluno in sala_102:
    inserir_alunos(aluno, 102)
for aluno in sala_103:
    inserir_alunos(aluno, 103)
# Fechar a conexão
conn.close()


#  Salvar em Arquivos JSON e Armazenar em Banco de Dados (JSON em SQL)
# criando uma nova tabela, agora refrenciadno por sala e não por aluno

conn = sqlite3.connect('database/salas.db')
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS salas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   sala INTEGER NOT NULL,
                   alunos TEXT NOT NULL
               )
               """)


# Funçaõ para inserir JSON em uma Tabela SQL
def inserir_sala(sala, novos_alunos):
    # Recuperar alunos já existentes na sala
    cursor.execute("SELECT alunos FROM salas WHERE sala = ?", (sala,))
    resultado = cursor.fetchone()

    if resultado:
        # Carregar a lista existente e adicionar novos alunos
        alunos_existentes = json.loads(resultado[0])
        alunos_atualizados = sorted(set(alunos_existentes + novos_alunos))  # Evitar duplicatas
        alunos_json = json.dumps(alunos_atualizados)

        # Atualizar o registro da sala
        cursor.execute("UPDATE salas SET alunos = ? WHERE sala = ?", (alunos_json, sala))
    else:
        # Inserir nova sala com a lista de alunos
        alunos_json = json.dumps(sorted(novos_alunos))  # Ordenar para manter a consistência
        cursor.execute("INSERT INTO salas (sala, alunos) VALUES (?, ?)", (sala, alunos_json))
    
    conn.commit()

# # essa função apaga as listas dentro do DB toda vez que for executada
""" def inserir_sala(sala, alunos):
    alunos_json = json.dumps(alunos) # Convertendo a lista de alunos para JSON
    # verificar se a sala já existe
    cursor.execute("SELECT COUNT(1) FROM salas WHERE sala = ?", (sala,))
    existe = cursor.fetchone()[0]
    
    if existe:
        # atualiza o registo existente
        cursor.execute("UPDATE salas SET alunos = ? WHERE sala = ?", (alunos_json, sala)) 
    else:
        # inserir novo registo
        cursor.execute("INSERT INTO salas (sala, alunos) VALUES (?, ?)", (sala, alunos_json))
    conn.commit() """ 
# inserção das listas de alunos
inserir_sala(101, sala_101)
inserir_sala(102, sala_102)
inserir_sala(103, sala_103)

conn.close()


# Visualizando os bancos de dados:

# Visualizando a tabela alunos
def visualizar_alunos():
    print('--' * 30)
    print("Visualização da Tabela 'Alunos'")
    conn = sqlite3.connect("database/alunos.db")
    cursor = conn.cursor()
    # Consulta para recuperar dados ordenados por sala e nome
    cursor.execute("SELECT nome, sala FROM alunos ORDER BY sala, nome")
    alunos = cursor.fetchall()
    # Exibir dados
    for sala in [101, 102, 103]:
        print(f"\nAlunos da sala {sala}:")
        for aluno in alunos:
            if aluno[1] == sala:
                print(f" - {aluno[0]}")
    conn.close()
    print("--" * 30)            

# implementação
visualizar_alunos()


# Visualizando por sala o arquivo JSON, por lista
def visualizar_salas():
    print('--' * 30)
    print("Visualização da Tabela 'Salas' com listas JSON")
    conn = sqlite3.connect("database/salas.db")
    cursor = conn.cursor()
    # Consulta para recuperar dados
    cursor.execute("SELECT sala, alunos FROM salas ORDER BY sala")
    salas = cursor.fetchall()
    # Exibir dados
    for sala in salas:
        sala_numero = sala[0]
        alunos = json.loads(sala[1]) # Carregar JSON de volta para lista
        print(f"\nAlunos da Sala {sala_numero}:")
        for aluno in sorted(alunos):
            print(f" - {aluno}")
    conn.close()
    print("--" * 30)   
   
# implementação
visualizar_salas()
    