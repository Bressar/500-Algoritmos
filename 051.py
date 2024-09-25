# Algoritmo 51
# Locadora de Vídeos - !Isso é antigo...rs!

""" Algoritmo que:
    
- leia a quantidade de fitas que a locadora possui
- valor que cobra por cada aluguel

Mostrar o seguinte:
    
Sabendo que um terço da fitas são alugadas por mês, exiba o faturamento anual da locadora

Quando há atraso, é cobrada uma multa de 10% sobre o valor do aluguel.
Sabendo que um décimo das fitas são entregadas com atraso, calcule o valor ganho com multas por mês

Sabendo que 2% das fitas estragam por ano, e 1 décimo do total é comprado para reposição, exiba o total de fitas que a locadora terá no final

 """

class Locadora:
    def __init__(self, valor_aluguel=None, multas=None, quantidade=None):
        self.__valor_aluguel = valor_aluguel
        self.__multas = multas
        self.__quantidade = quantidade
      
        
    def linha(self, valor):
        print('--' * valor) 
     
        
    def faturamento_anual(self):
        if self.__quantidade is not None and self.__valor_aluguel is not None:
            fatura_anual = (self.__quantidade / 3) * self.__valor_aluguel * 12
            print(f'Faturamento Anual: R$ {fatura_anual:.2f}')
        else:
            print("Erro: Faltam informações para calcular o faturamento anual.")
     
            
    def multas_mensais(self):
        if self.__quantidade is not None and self.__valor_aluguel is not None and self.__multas is not None:
            multas = self.__valor_aluguel * 0.1 * (self.__quantidade / 10)
            print(f'Multas Mensais: R$ {multas:.2f}')
        else:
            print("Erro: Faltam informações para calcular o valor das multas mensais.")
      
            
    def quantidade_fitas(self):
        if self.__quantidade is not None and self.__valor_aluguel is not None and self.__multas is not None:
            quantidade_final = int(self.__quantidade - (self.__quantidade * 0.02) + (self.__quantidade / 10))
            print(f"Quantidade de fitas em estoque no final do ano: {quantidade_final}")
        else:
            print("Erro: Faltam informações para calcular a quantidade final de fitas.")

                       
    def relatorio_ano_locadora(self):
        while True:
            try:
                ano_indicado = input('Digite o ano para o registro: ')
                if len(ano_indicado) != 4 or not ano_indicado.isdigit():
                    raise ValueError("O ano indicado deve ter exatamente 4 dígitos.")
                ano_indicado = int(ano_indicado)
                break
            except ValueError as e:
                print(f"ERRO! {e}. Digite novamente")
                self.linha(35)       
        while True:
            try:
                quantidade = int(input('Digite a quantidade de fitas: '))
                break
            except ValueError as e:
                print(f"ERRO! {e}. Digite novamente")
                self.linha(35)       
        while True: 
            try: 
                valor_aluguel = float(input('Digite o valor do Aluguel: '))
                break
            except ValueError as e:
                print(f"ERRO! {e}. Digite novamente")
                self.linha(35) 
        while True:
            try:
                multas = int(input("Quantidade de multas mensais: ") )
                break
            except ValueError as e:
                print(f"ERRO! {e}. Digite novamente")
                self.linha(35)
        
        self.__valor_aluguel = valor_aluguel
        self.__multas = multas
        self.__quantidade = quantidade
        
        self.linha(25)
        self.linha(25)
        print(f'RELATÓRIO DO ANO DE {ano_indicado}')
        self.linha(25)
        self.faturamento_anual()
        self.multas_mensais()
        self.quantidade_fitas()
        self.linha(25)
                

# Dessa forma o user entra com os dados pelo terminal, !depois melhoro o código e adiciono um banco de dados!        
ano_0000 = Locadora()   
ano_0000.relatorio_ano_locadora()
