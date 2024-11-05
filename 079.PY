# Algoritmo 079
#

import sqlite3

def testar_consulta_metadados():
    """Testa o acesso aos metadados para verificar se o banco está acessível e com sintaxe correta."""
    db_path = "database/estudantes.db"
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Realiza uma consulta nos metadados para verificar as tabelas, usando aspas simples
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' OR type='view';")
        
        # Exibe o nome das tabelas encontradas (ou avisa se não houver nenhuma)
        tables = cursor.fetchall()
        if tables:
            print("Tabelas encontradas no banco de dados:", [table[0] for table in tables])
        else:
            print("Nenhuma tabela encontrada no banco de dados.")
        
    except sqlite3.Error as e:
        print(f"Erro ao acessar metadados do banco de dados: {e}")
    finally:
        if conn:
            conn.close()

# Executa o teste de consulta a metadados
testar_consulta_metadados()
