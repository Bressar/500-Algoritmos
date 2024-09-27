# Algoritmo 52
# Sistema de Estacionamento(veículos)

class Estacionamento:
    
    def __init__(self, preco_inicial=1.0, preco_hora=1.0, lista_veiculos=[]):
        self.__preco_inicial = preco_inicial
        self.__preco_hora = preco_hora
        self.__lista_veiculos = lista_veiculos
        
    total_a_pagar = 0    
    
    
    def linha(self, padrao='--', valor=0):
        print(padrao * valor)
    
    
    def valores_entrada(self):
        while True:
            try:
                self.__preco_inicial = float(input('Digite a taxa inicial: € '))
                break
            except ValueError:
                print(f"ERRO! Valor inválido, Digite novamente")
                self.linha('--', 30)
        while True:
            try:
                self.__preco_hora = float(input('Digite o valor da hora: € '))
                break
            except ValueError:
                print(f"ERRO! Valor inválido, Digite novamente")
                self.linha('--', 30)                
        while True:
            try:                
                quantidade_horas = int(input('Digite a quantidade de horas: '))
                break
            except ValueError:
                print(f"ERRO! Valor inválido, Digite novamente")
                self.linha('--', 30)
                
        total_a_pagar = self.__preco_inicial + (self.__preco_hora * quantidade_horas)  
        
        self.linha('---', 20)
        print(f'Taxa de estacionamento: € {self.__preco_inicial:.2f}\n'
              f'Valor da Hora: € {self.__preco_hora:.2f}\n'
              f'Tempo de permanência: {quantidade_horas} horas\n'
              f'TOTAL A PAGAR: € {total_a_pagar:.2f}') 
        self.linha('---', 20)  

                   
    def adicionar_veiculo(self):
        # Falta fazer uma verificação para a inserção de um valor válido para uma placa de carro
        placa_veiculo = str(input("Digite a placa do veículo para estacionar: \n")).strip().upper()
        self.__lista_veiculos.append(placa_veiculo)
        print('-> Veículo cadastrado')
        self.linha('---', 10)

        
    def remover_veiculo(self):
        remover_veiculo = str(input("Digite a placa para remover o veículo:\n")).strip().upper()
        
        #for debug .- esse trecho tá bugando!!!
        # print(f"Placa digitada: {remover_veiculo}")
        # print(f"Lista de veículos: {self.__lista_veiculos}")
     
        if remover_veiculo not in self.__lista_veiculos:
            print('Veículo não encontrado!')
        else:
            self.__lista_veiculos.remove(remover_veiculo)
            print('Veículo Removido!')
            self.linha('--', 10)
            self.valores_entrada()    
        #return self.__lista_veiculos
        
        
    def listar_veiculos(self):
        if len(self.__lista_veiculos) == 0:
            print('Não há veículos listados')
        else:
            self.linha('---', 10)
            print('OS VEÍCULOS ESTACIONADOS SÃO:')
            for placa in self.__lista_veiculos:
                print(f'Placa: {placa}')
            self.linha('---', 10)
                
                
    def menu_opcoes(self):        
        while True:
            while True:
                self.linha('---', 10)
                print(
                    """DIGITE SUA OPÇÃO:
[1] -> Cadastrar Veículo
[2] -> Remover Veículo
[3] -> Listar Veículo
[4] -> Encerrar""")
                self.linha('---', 10)
                escolha = input()
                try:
                    if len(escolha) != 1 or not escolha.isdigit():
                        raise ValueError("O número indicado deve ter exatamente 1 dígito.\nEscolha um número entre 1 e 4")
                    elif escolha not in '1234':
                        print('ERRO! Escolha um número entre 1 e 4')
                        self.linha('---', 10)
                    else:
                        break
                except ValueError as e:
                    print(f"ERRO! {e} - Digite novamente")
                    self.linha('---', 20)    
                  
            if escolha == '1':
                self.adicionar_veiculo()
            elif escolha == '2':
                self.remover_veiculo()
            elif escolha == '3':
                self.listar_veiculos()
            elif escolha == '4':
                self.linha('---', 10)
                print('Encerrando o programa')
                self.linha('---', 10)
                break


# implementação     
parking = Estacionamento(preco_inicial=2, preco_hora=1.5, lista_veiculos=[])  
parking.menu_opcoes()


#parking2 = Estacionamento(preco_inicial=2, preco_hora=1.5, lista_veiculos=['ex-100', 'ex-300'])  
# parking1.adicionar_veiculo()
# parking1.remover_veiculo()
#parking2.listar_veiculos()
#parking1.valores_entrada()
