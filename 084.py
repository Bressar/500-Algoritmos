# Algoritmo 084
""" 
Algoritmo que: lê um destino de viagem, se inclui (ida e volta) informar preço da passagem 
Usando a tabela fornecida."""

class Viagem:
    def __init__(self):
        self.tabela = {
            "Região Norte": [500, 900],
            "Região Nordeste": [350, 650],
            "Região Centro-Oeste": [350, 600],
            "Região Sul": [300, 550]
        }


        while True:
            self.calcular_viagem()
            sair= input('Para continuar pressione [S]\nPara sair pressione qualquer tecla\n>> ').strip().upper()
            if sair == 'S':
                continue
            else:
                print('Encerrando o programa...')
                self.linha()
                break
                
    def calcular_viagem(self):
        #print(tabela["Região Norte"][1])  # Saída: 900
        while True:
            self.linha()
            self.destino = input('Escolha a região de destino:\n[1] Região Norte\n[2] Região Nordeste\n[3] Região Centro-Oeste\n[4] Região Sul\n>> ').strip()
            if self.destino == '1':
                for key in self.tabela:
                    if key == "Região Norte":
                        self.destino_final = key
                self.ida = self.tabela["Região Norte"][0]
                self.ida_volta = self.tabela["Região Norte"][1]
                break
            elif self.destino == '2':
                for key in self.tabela:
                    if key == "Região Nordeste":
                        self.destino_final = key
                self.ida = self.tabela["Região Nordeste"][0]
                self.ida_volta = self.tabela["Região Nordeste"][1]
                break
            elif self.destino == '3':
                for key in self.tabela:
                    if key == "Região Centro-Oeste":
                        self.destino_final = key
                self.ida = self.tabela["Região Centro-Oeste"][0]
                self.ida_volta = self.tabela["Região Centro-Oeste"][1]
                break
            elif self.destino == '4':
                for key in self.tabela:
                    if key == "Região Sul":
                        self.destino_final = key
                self.ida = self.tabela["Região Sul"][0]
                self.ida_volta = self.tabela["Região Sul"][1]
                break
            else:
                print('Valor inválido! Escolha novamente.')
                    
        while True:
            self.linha()
            self.percurso = input('Escolha o percurso:\n[1] Ida\n[2] Ida e Volta\n>> ').strip()
            if self.percurso == '1':
                print(f'Valor da passagem de ida para {self.destino_final}: \nR$ {self.ida:.2f}')
                self.linha()
                break
            elif self.percurso == '2':
                print(f'Valor da passagem de ida-volta para {self.destino_final}: \nR$ {self.ida_volta:.2f}')
                self.linha()
                break
            else:
                print('Valor inválido! Escolha novamente.')
            
        
    def linha(self):
        print("---" * 20)
        
if __name__ == "__main__":
    Viagem()
    
    