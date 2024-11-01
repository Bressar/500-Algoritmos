# cria equipe com 3 competidoes e seus pontos
def criar_equipe(nome_da_equipa= "Nome da equipa"):
    equipe = {} 
    # Lê os nomes e pontos dos jogadores
    for i in range(3): 
        nome = input("Digite o nome do jogador: ").strip().title()
        while True:
            try:
                pontos = int(input("Digite o número mos de pontos: "))
                break
            except ValueError as e:
                print(f'{e} - Digite um número inteiro')
        equipe[nome] = pontos
        
    # Ordena a equipe em ordem decrescente de pontos
    equipe_ordenada = dict(sorted(equipe.items(), key=lambda item: item[1], reverse=True))
    
    # Calcula a soma dos pontos da equipe
    total_pontos_equipes = sum(equipe_ordenada.values())
    
    return nome_da_equipa, equipe_ordenada, total_pontos_equipes

# criando equipe e recebendo os dados
nome_da_equipa, equipe1, total_pontos_equipe1 = criar_equipe(nome_da_equipa="Equipe 1")

# apresenta a equipe ordenada
print('--' * 30)
print(f'Team: {nome_da_equipa}')
print('--' * 30)
print("Ranking de Pontos:")
for nome, pontos in equipe1.items():
    print(f'{nome}: {pontos} pontos')
print('--' * 30)    
# Apresenta a soma de todos os pontos da equipe
print(f'Soma total dos pontos da equipe: {total_pontos_equipe1}')
print('--' * 30)

ranking_de_equipes = []

if total_pontos_equipe1 > 100:
    ranking_de_equipes.append(equipe1)
    media_pontos_equipe = total_pontos_equipe1 / 3 # ou len(equipe_ordenada)
    print(f"\nEquipe CALSSIFICADA! Média de pontos: {media_pontos_equipe} pontos")
else:
    print("\nEquipe ELIMINADA!!")
    
for equipe in ranking_de_equipes:
    print(equipe, end="\n")
    






















# Função para visualizar dados da tabela `salas` com JSON (Banco de Dados com Lista JSON)
def visualizar_salas():
    print("--" * 30)
    print("Visualização da Tabela 'salas' com listas JSON")
    
    # Conectar ao banco de dados das salas
    conn = sqlite3.connect("slas.db")
    cursor = conn.cursor()
    
    # Consulta para recuperar dados
    cursor.execute("SELECT sala, alunos FROM salas ORDER BY sala")
    salas = cursor.fetchall()
    
    # Exibir os dados
    for sala in salas:
        sala_numero = sala[0]
        alunos = json.loads(sala[1])  # Carregar JSON de volta para lista
        print(f"\nAlunos da Sala {sala_numero}:")
        for aluno in sorted(alunos):
            print(f" - {aluno}")
    
    # Fechar a conexão
    conn.close()
    print("--" * 30)













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
        nome TEXT NOT NULL,
        nota1 REAL,
        nota2 REAL,
        nota3 REAL,
        nota4 REAL
    )
    """)

    # confirma criação de tabela
    conn.commit()
    conn.close()

# executando a função pra criar o banco de dados:
criar_banco_de_dados()
print("Banco de dos criado com sucesso!!")




# print(min(max(False, -3, -4), 2,7))








# Algoritmo 059
# Cálculo de idade, atual e em uma data aleatória

""" 
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_atual = datetime.today() # Obtendo a data atual


def linha():
    print('--' * 15)
    

def ano_bissexto(ano):# Função para verificar se o ano é bissexto
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def definir_data(titulo=""):
    linha()
    print(titulo)
    while True: # Validação Ano
        try:
            year = input("Ano: ").strip()
            if  len(year) != 4:
                print("Digite um ano válido\nO ano deve ter 4 dígitos")
                linha()
            else:
                year = int(year)
                break
        except ValueError:
            print("Digite um ano válido.")
            linha()  
    while True: # Validação Mês
        try:
            month = int(input("Mês: "))
            if month < 1 or month > 12:
                print("Digite um mês válido\nO mês deve ser entre 1 e 12")
                linha()
            else:
                break
        except ValueError:
            print("Digite um mês válido.")
            linha()               
    while True: # Validação dia
        try:
            day = int(input("Dia: "))       
            if day < 1 or day > 31 :
                print("ERRO!\nO dia deve ser entre 1 e 31")
                linha()
                continue            
            if month in [4,6,9,11] and day > 30: # Verifica meses com 30 dias
                print("ERRO\nEste mês só tem 30 dias")
                linha()
                continue           
            if month == 2:  # Verifica fevereiro
                if ano_bissexto(year) and day > 29:
                    print("ERRO!\nFevereiro só tem 29 dias em anos bissextos.")
                    linha()
                    continue
                elif not ano_bissexto(year) and day > 28:
                    print("ERRO!\nFevereiro só tem 28 dias em anos não bissextos.")
                    linha()
                    continue        
# Se passou por todas as validações, o dia é válido    
            break
        
        except ValueError:
            print("Digite um dia válido.")
            linha()
    
    data = datetime(year=year, month=month, day=day) #objeto datetime para a data de nascimento 
    return data              


# Implementação 
while True:
    print('***' * 17)
    print("CALCULADORA DE IDADE".center(50))
    print('***' * 17)
    escolha = str(input("Para saber sua idade nesse exato momento [A]: \nPara saber sua idade em uma data aleatória [X] \nPara sair digite qualquer tecla. ")).strip()
    print('***' * 17)

    if escolha in "aA":
        data_nascimento = definir_data("Insira sua data de nascimento: ")
        diferenca = data_atual - data_nascimento # Calculando a diferença entre as datas
        # Convertendo a diferença para dias totais e separando anos, meses, dias e horas
        anos = diferenca.days // 365
        meses = (diferenca.days % 365) // 30
        dias = (diferenca.days % 365) % 30
        horas = diferenca.seconds // 3600
        linha()
        print(f'Sua idade é de:\n- {anos} anos,\n- {meses} mese(s),\n- {dias} dia(s) \n- {horas} hora(s)')
        linha()   
            
    elif escolha in "xX":
        data_nascimento = definir_data("Insira sua data de nascimento: ")
        while True:
            data_aleatoria = definir_data("Insira uma data aleatória: ")
            if data_aleatoria < data_nascimento:
                print("ERRO!\nData escolhida é anterior a data de nascimento. ")
            else:
                diferenca = data_aleatoria - data_nascimento # Calculando a diferença entre as datas
                anos = diferenca.days // 365
                meses = (diferenca.days % 365) // 30
                dias = (diferenca.days % 365) % 30
                horas = diferenca.seconds // 3600
                linha()
                print(f'Nessa data sua idade correspondia a:\n- {anos} anos,\n- {meses} mese(s),\n- {dias} dia(s) \n- {horas} hora(s)')
                linha()
                break   

    else:
        print("Encerrando o programa...\nAdeus Velinho(a)!!!")
        linha()
        break """



# num = int(input())

# for i in range(0, num + 1):
#     if (i % 2 != 0):
#     	print (i, end='\n')
    

# def dis(price, discount):
#     price_discount = price - ((price * discount) / 100)
#     return round(price_discount, 2)
		
		
# print(dis(1500, 50))
# print(dis(89, 20))
# print(dis(100, 75))

# print('--' * 25)

# def dis(price, discount):
# 	discount = discount / 100
# 	newPrice = price - (price * discount)
# 	return round(newPrice,2)


# print(dis(1500, 50))
# print(dis(89, 20))
# print(dis(100, 75))
