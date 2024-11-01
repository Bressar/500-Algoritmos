# Algoritmo 077 - by Bressar
# Versão em  POO
# Criar uma equipe de 3 jogadores
# ler os pontos de cada jogadr da equipe e exibir em ordem decrescente
# Se a soma dos 3 jogadores for > que 100, exibir média e acrescentar no ranking de equipes
# se for < 100 -> equipe desclassicada
# apresentar ranking final



class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = {}
    
    def adicionar_jogador(self, nome, pontos):
        self.jogadores[nome] = pontos

    def ordenar_jogadores(self):
        # Ordena os jogadores em ordem decrescente de pontos
        self.jogadores = dict(sorted(self.jogadores.items(), key=lambda item: item[1], reverse=True))
    
    def total_pontos(self):
        return sum(self.jogadores.values())
    
    def media_pontos(self):
        return self.total_pontos() / len(self.jogadores) if self.jogadores else 0

    def exibir_equipe(self):
        print(f'\nEquipe: {self.nome}')
        print("Ranking de Pontos:")
        for nome, pontos in self.jogadores.items():
            print(f'{nome}: {pontos} pontos')
        print(f'Soma total dos pontos da equipe: {self.total_pontos()}')
        print(f'Média de pontos: {self.media_pontos():.2f}')

class Ranking:
    def __init__(self):
        self.equipes = []
    
    def adicionar_equipe(self, equipe):
        if equipe.total_pontos() > 100:
            equipe.ordenar_jogadores()
            self.equipes.append(equipe)
            print(f"\nEquipe CLASSIFICADA! Média de pontos: {equipe.media_pontos():.2f}")
        else:
            print("\nEquipe DESCLASSIFICADA!")
    
    def exibir_ranking(self):
        # Ordena as equipes no ranking por média de pontos em ordem decrescente
        equipes_ordenadas = sorted(self.equipes, key=lambda equipe: equipe.media_pontos(), reverse=True)
        
        print("\nRanking Final das Equipes Classificadas:")
        for posicao, equipe in enumerate(equipes_ordenadas, start=1):
            print(f"{posicao}º - Equipe: {equipe.nome} | Média: {equipe.media_pontos():.2f} pontos | Total: {equipe.total_pontos()} pontos")
            equipe.exibir_equipe()

# Uso das classes
ranking = Ranking()

# Exemplo de criação de 3 equipes
for _ in range(3):  # Ajuste a quantidade de equipes conforme necessário
    nome_da_equipe = input("Digite o nome da equipe: ").strip().title()
    equipe = Equipe(nome_da_equipe)
    
    # Adiciona 3 jogadores para cada equipe
    for i in range(3):
        nome_jogador = input("Digite o nome do jogador: ").strip().title()
        while True:
            try:
                pontos = int(input("Digite o número de pontos: "))
                break
            except ValueError:
                print("Erro: Digite um número inteiro para os pontos.")
        equipe.adicionar_jogador(nome_jogador, pontos)
    
    # Adiciona a equipe ao ranking se classificada
    ranking.adicionar_equipe(equipe)

# Exibe o ranking final das equipes
ranking.exibir_ranking()
