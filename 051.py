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
      
        
    def linha(self):
        print('--' * 25) 
     
        
    def faturamento_anual(self):
        if self.__quantidade is not None and self.__valor_aluguel is not None:
            fatura_anual = (self.__quantidade / 3) * self.__valor_aluguel * 12
            self.linha()
            print(f'Faturamento Anual: R$ {fatura_anual:.2f}')
            self.linha()
        else:
            print("Por favor, defina 'quantidade' e 'valor_aluguel' antes de calcular o faturamento.")
     
            
    def multas_mensais(self):
        if self.__quantidade is not None and self.__valor_aluguel is not None and self.__multas is not None:
            multas = self.__valor_aluguel * 0.1 * ((self.__quantidade / 3) / 10)
            self.linha()
            print(f'Multas Mensais: R$ {multas:.2f}')
            self.linha()
        else:
            print("Por favor, defina 'quantidade', 'valor_aluguel' e 'quantidade de multas'.\nAntes de calcular o faturamento.")
      
            
    def quantidade_fitas(self):
        if self.__quantidade is not None and self.__valor_aluguel is not None and self.__multas is not None:
            quantidade_final = int(self.__quantidade * (self.__quantidade * 0.02) + (self.__quantidade / 10))
            self.linha()
            print(f"Quantidade de fitas em estoque no final do ano: {quantidade_final}")
            self.linha()
        else:
            print("Por favor, defina 'quantidade', 'valor_aluguel' e 'quantidade de multas'.\nAntes de calcular o faturamento.")

                       
    def relatorio_ano_locadora(self, ano):
        ano_indicado = int(input('Digite o ano para o registro: '))
        quantidade = int(input('Digite a quantidade de fitas: '))
        valor_aluguel = float(input('Digite o valor do Aluguel: '))
        multas = int(input("Quantidade de multas mensais: ") )
        self.__valor_aluguel = valor_aluguel
        self.__multas = multas
        self.__quantidade = quantidade
        ano = Locadora(valor_aluguel=self.__valor_aluguel, multas=self.__multas, quantidade=self.__quantidade)
        
        self.linha()
        print(f'Relatório do Ano de {ano_indicado}')
        
        return ano.faturamento_anual(), ano.multas_mensais(), ano.quantidade_fitas()
                
           
ano_0000 = Locadora(valor_aluguel=0, multas=0, quantidade=0)   
ano_0000.relatorio_ano_locadora(ano=1998)

# Debug
# ano_1997.faturamento_anual()
# ano_1997.multas_mensais()
# ano_1997.quantidade_fitas()
