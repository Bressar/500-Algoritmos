# Algoritmo 63
# Média escolar de um aluno - usando banco de dados, sqlite

import pandas as pd
import sqlite3

# Criando o database e atabela diretamentye no python:
# nome do banco de dados: estudantes.db
# -> nome da tabela estudantes:
# colunas da tabela id(primary key), nome, nota1, nota2, nota3, nota4

def criar_banco_de_dados():
    # conectar ao banco de dados ou criar se não existir
    conn = sqlite3.connect("database/estudantes.db")
    cursor = conn.cursor()
    
    # Criação da tabela, caso não exista
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudante
    (
        id TEXT PRIMARY KEY,
        nome TEXT ,
        nota1 REAL,
        nota2 REAL,
        nota3 REAL,
        nota4 REAL,
        media REAL
    )
    """)

    # confirma criação de tabela
    conn.commit()
    conn.close()

# executando a função pra criar o banco de dados:
criar_banco_de_dados()
print("Banco de dos criado com sucesso!!")


class Estudantes:
    
    db_estudantes = "database/estudantes.db"
    
    def __init__(self, id_estudante=None, nome_estudante=None, notas=[]):
        self.__id_estudante = id_estudante
        self.__nome_estudante = nome_estudante
        self.__notas = notas
        
    def linha(self, padrao='--', valor=0):
        print(padrao * valor)
    
        
    def adicionar_aluno(self): 
        while True: # Adicionar ID
            self.__id_estudante = str(input("ID estudante (4 números): ")).strip()
            if len(self.__id_estudante) == 4 and self.__id_estudante.isdigit():
                try:
                    with sqlite3.connect(self.db_estudantes) as conn:
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO estudante (id) VALUES (?)", (self.__id_estudante,))
                        conn.commit()
                    print('ID cadastrado no sistema')
                    self.linha('--', 30)
                    break
                except sqlite3.Error as e:
                    print(f"Erro ao inserir ID: {e}")
                    self.linha('--', 30)               
            else:
                print("Formato inválido! O ID deve ter 4 números.")                          
        while True: #Adicionar nome
            try:
                self.__nome_estudante = input("Nome do aluno(a): ").strip().title()
                if not all(part.isalpha() for part in self.__nome_estudante.split()):
                    raise ValueError("O nome deve conter apenas letras.")
                else:
                    with sqlite3.connect(self.db_estudantes) as conn:
                        cursor = conn.cursor()
                        cursor.execute("UPDATE estudante SET nome = ? WHERE id = ?", (self.__nome_estudante, self.__id_estudante))
                        conn.commit()
                    print(f"{self.__nome_estudante} cadastrado no sistema")
                    self.linha('--', 30)   
                    break
            except ValueError:
                print("Formato inválido! tente novamente.")
                self.linha('--', 30)
            except sqlite3.Error as e:
                print(f"Erro ao inserir nome: {e}")
                self.linha('--', 30)    
                
       
    def remover_estudante(self):
        self.__id_estudante = str(input("Digite o ID para remover o estudante do cadastro:\n")).strip()
        try:
            with sqlite3.connect(self.db_estudantes) as conn:
                cursor = conn.cursor()                
                # Verifica se o ID existe na tabela
                cursor.execute("SELECT * FROM estudante WHERE id = ?", (self.__id_estudante,))
                estudante = cursor.fetchone()  # Verifica se o estudante existe               
                if estudante:
                    # O estudante foi encontrado, então removemos
                    cursor.execute("DELETE FROM estudante WHERE id = ?", (self.__id_estudante,))
                    conn.commit()  # Confirma a remoção
                    print(f"Estudante com ID {self.__id_estudante} removido com sucesso!")
                else:
                    # O estudante não foi encontrado
                    print(f"ID {self.__id_estudante} não encontrado no banco de dados.")                
                self.linha('--', 30)
        except sqlite3.Error as e:
            print(f"Erro ao remover estudante: {e}")
        
                                    
    def acrescentar_notas(self):
        self.__notas = []
        for i in range(1, 5):  # Loop de 1 a 4 para cada bimestre
            while True:
                try:
                    nota = float(input(f'Insira a nota do {i}° Bimestre: '))
                    if 0 <= nota <= 10:  # Condição para verificar se a nota está entre 0 e 10
                        self.__notas.append(nota)  # Armazena a nota na lista
                        break  # Sai do loop e passa para a próxima nota
                    else:
                        print('A nota deve ser maior/igual a 0 ou menor/igual a 10!')
                        self.linha('--', 30)
                except ValueError:
                    print('Valor inválido! Tente novamente')
                    self.linha('--', 30)
        media_final = sum(self.__notas) / len(self.__notas)  # Calcula a média       
        # Atualizando as notas no banco de dados
        try:
            with sqlite3.connect(self.db_estudantes) as con:
                cursor = con.cursor()
                cursor.execute("""
                    UPDATE estudante
                    SET nota1 = ?, nota2 = ?, nota3 = ?, nota4 = ?, media = ?
                    WHERE id = ?""", (*self.__notas,  media_final, self.__id_estudante))
                con.commit()
        except sqlite3.Error as e:
            print(f"Erro ao atualizar notas {e}")
    
    
    def listar_estudantes_notas(self):
        try:
            with sqlite3.connect(self.db_estudantes) as con:
                query = "SELECT * FROM estudante"  # Consulta tabela no .db
                data_frame = pd.read_sql_query(query, con)  # cria o dataframe para ser lido com o pandas
                # Retorna a representação em string dos dados do DataFrame
                print(data_frame.to_string(index=False)) # exibe o dataframe sem a numeração do pandas
                return data_frame
        except sqlite.Error as e:
            print(f"Erro ao listar estudantes: {e}")
            
                       
    def buscar_estudante(self):
        identificador = input("Inisira o ID ou o nome que deseja acessar: ").strip().title() 
        try:
            with sqlite3.connect(self.db_estudantes) as con:
                # Verifica se o identificador é um ID (4 dígitos)
                if identificador.isdigit() and len(identificador) == 4:
                    query = "SELECT * FROM estudante WHERE id = ?"
                    data_frame = pd.read_sql_query(query, con, params=(identificador,))
                else:
                    query = "SELECT * FROM estudante WHERE nome = ?"
                    data_frame = pd.read_sql_query(query, con, params=(identificador.title(),))
                 # Verifica se o DataFrame está vazio
                if data_frame.empty:
                    print(f"Nenhum estudante encontrado com o ID ou nome '{identificador}'.")
                else:
                    print(data_frame.to_string(index=False))  # Exibe o DataFrame sem a numeração do pandas
                return data_frame
        except sqlite3.Error as e:
            print(f"Erro ao buscar estudante: {e}")
            return None


    def editar_estudante(self):
        identificador = input("Digite o ID do estudante que deseja editar: ").strip()       
        try:
            with sqlite3.connect(self.db_estudantes) as con:
                cursor = con.cursor()
                # Buscar estudante pelo ID
                cursor.execute("SELECT * FROM estudante WHERE id = ?", (identificador,))
                estudante = cursor.fetchone() # seleciona a row do id escolhido
                if estudante:
                    # Exibir os dados atuais do estudante
                    print("Dados atuais do estudante:")
                    print(f"ID: {estudante[0]}")
                    print(f"Nome: {estudante[1]}")
                    print(f"Nota 1: {estudante[2]}")
                    print(f"Nota 2: {estudante[3]}")
                    print(f"Nota 3: {estudante[4]}")
                    print(f"Nota 4: {estudante[5]}")
                    print(f"Média: {estudante[6]}")
                    # Editar nome
                    if input("Deseja modificar o nome? (s/n): ").strip().lower() == "s":
                        novo_nome = input("Digite o novo nome: ").strip().title()
                        cursor.execute("UPDATE estudante SET nome = ? WHERE id = ?", (novo_nome, identificador))
                    # Editar notas
                    for i in range(1, 5):
                        if input(f"Deseja modificar a Nota {i}? (s/n): ").strip().lower() == "s":
                            while True:
                                try:
                                    nova_nota = float(input(f"Digite a nova Nota {i} (0 a 10): "))
                                    if 0 <= nova_nota <= 10:
                                        cursor.execute(f"UPDATE estudante SET nota{i} = ? WHERE id = ?", (nova_nota, identificador))
                                        break
                                    else:
                                        print("A nota deve estar entre 0 e 10.")
                                except ValueError:
                                    print("Valor inválido! Tente novamente.")
                    # Calcular a nova média
                    cursor.execute("SELECT nota1, nota2, nota3, nota4 FROM estudante WHERE id = ?", (identificador,))
                    notas = cursor.fetchone()
                    if notas:
                        nova_media = sum(notas) / len(notas)
                        cursor.execute("UPDATE estudante SET media = ? WHERE id = ?", (nova_media, identificador))
                    con.commit()
                    print("Dados do estudante atualizados com sucesso.")
                else:
                    print(f"Estudante com ID {identificador} não encontrado.")
        except sqlite3.Error as e:
            print(f"Erro ao editar estudante: {e}")


# implementação
programa = Estudantes(None, None, [])

while True:
    programa.linha('**', 30)
    print("MENU DE OPERAÇÕES\nBanco de Dados")
    programa.linha('**', 30)  
    option = input("""[1] Adicionar estudante
[2] Remover estudante
[3] Listar todos Estudantes
[4] Apresentar um determinado estudante
[5] Editar informações de um estudante
[S] Sair """).strip().upper() 
    programa.linha('**', 30)
    if option == "S":
        print("Encerrando o programa...")
        programa.linha('**', 30)
        break
    elif option == "1":
        programa.adicionar_aluno()
        programa.acrescentar_notas()
    elif option == "2":
        programa.remover_estudante()
    elif option == "3":
        programa.listar_estudantes_notas()       
    elif option == "4":
        programa.buscar_estudante()
    elif option == "5":
        programa.editar_estudante()
    else:
        print("'ERRO!' Escolha uma opção válida!")
        
