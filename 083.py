# Algoritmo 083
""" 
Algoritmo que: informe a quantidade de calorias de uma refeição, a partir da escolha do usuário, que deverá informar: 
- prato
- sobremesa
- bebida
Usando a tabela fornecida: """

class CalculoCalorias:
    def __init__(self):
        self.total_calorias = 0
        self.tabela = {
            "Prato": {
                "Vegetariano": 180,
                "Peixe": 230,
                "Frango": 250,
                "Carne": 350,
            },
            "Sobremesa": {
                "Abacaxi": 75,
                "Sorvete Diet": 110,
                "Mousse Diet": 170,
                "Mousse Chocolate": 200,
            },
            "Bebida": {
                "Chá": 20,
                "Suco de Laranja": 70,
                "Suco de Melão": 100,
                "Refrigerante Diet": 65,
            }
        }

        # Executa a escolha para cada categoria
        for categoria, opcoes in self.tabela.items():
            self.escolha_comida(categoria, opcoes)

        self.linha()
        print(f"Total de Calorias: {self.total_calorias} calorias.")
        self.linha()

    def linha(self):
        print("--" * 20)

    def escolha_comida(self, categoria, opcoes):
        """ Exibe as opções e solicita a escolha do usuário. """
        print(f"\nEscolha {categoria}:")
        lista_opcoes = list(opcoes.keys())

        for i, item in enumerate(lista_opcoes, start=1):
            print(f"[{i}] {item}")

        while True:
            escolha = input(">> ").strip()

            if escolha.isdigit() and 1 <= int(escolha) <= len(lista_opcoes):
                comida = lista_opcoes[int(escolha) - 1]
                calorias = opcoes[comida]
                self.total_calorias += calorias
                self.linha()
                print(f"{categoria}: {comida} tem {calorias} calorias.")
                break
            else:
                print("Escolha inválida! Tente novamente.")

if __name__ == "__main__":
    CalculoCalorias()





# Versão com Tabelas
""" class calculo_calorias:
    def __init__(self):
        self.prato = None
        self.caloria = 0
        self.total_calorias = 0
        self.tabela = [
                    ['Prato',
                        ['vegetariano', 180,
                            'peixe', 230,
                            'frango', 250,
                            'carne', 350]
                    ],
                    ['Sobremesa',
                        ['abacaxi', 75,
                        'sorvete diet', 110,
                        'mousse diet', 170,
                        'mousse chocolate', 200]           
                    ],
                    ['Bebida',
                        ['chá', 20,
                        'suco de laranja', 70,
                        'suco de melão', 100,
                        'refrigerante diet', 65                    
                        ]            
                    ]
                ] 
       
        #Implementação
        self.escolha_comida('Prato', 'Vegetariano', 'Peixe', 'Frango', 'Carne')
        self.escolha_comida('Sobremesa', 'abacaxi', 'sorvete diet', 'mousse diet', 'mousse chocolate')
        self.escolha_comida('Bebida', 'chá', 'suco de laranja', 'suco de melão', 'refrigerante diet')
        
        self.linha()
        print (f'Total de Calorias: {self.total_calorias} calorias.')
        self.linha()
                       

    def linha(self):
        print('--' * 20)
        

    def escolha_comida(self, refeição, item_1, item_2, item_3, item_4):
        if refeição == 'Prato':
            self.tipo_refeicao = 'Prato'
            self.tipo_comida = 0
        elif refeição == 'Sobremesa':
            self.tipo_comida = 1
            self.tipo_refeicao = 'Sobremesa'
        elif refeição == 'Bebida':
            self.tipo_comida = 2
            self.tipo_refeicao = 'Bebida'
            
        while True:
            self.linha()
            self.prato = input(f'Escolha {refeição}:\n[1] {item_1}\n[2] {item_2}\n[3] {item_3}\n[4] {item_4}\n>> ').strip() 
            # if self.prato != '1' or self.prato != '2' or self.prato != '3' or self.prato != '4':
            #     print('Escolha inválida! Tente novamente!') 
            # else:
            if self.prato == "1":
                self.prato = 0
                self.caloria = self.tabela[self.tipo_comida][1][1]
                self.total_calorias += self.caloria
                self.linha()
                print (f'{self.tipo_refeicao}: {self.tabela[self.tipo_comida][1][0]} tem {self.caloria} calorias.')  
                break
            elif self.prato == "2":
                self.prato = 2
                self.caloria = self.tabela[self.tipo_comida][1][3]
                self.total_calorias += self.caloria
                self.linha()
                print (f'{self.tipo_refeicao}: {self.tabela[self.tipo_comida][1][2]} tem {self.caloria} calorias.')  
                break
            elif self.prato == "3":
                self.prato = 4
                self.caloria = self.tabela[self.tipo_comida][1][5]
                self.total_calorias += self.caloria
                self.linha()
                print (f'{self.tipo_refeicao}: {self.tabela[self.tipo_comida][1][4]} tem {self.caloria} calorias.')  
                break
            elif self.prato == "4":
                self.prato = 6
                self.caloria = self.tabela[self.tipo_comida][1][7]
                self.total_calorias += self.caloria
                self.linha()
                print (f'{self.tipo_refeicao}: {self.tabela[self.tipo_comida][1][6]} tem {self.caloria} calorias.')  
                break
            else:
                print('Escolha inválida! Tente novamente!') 

            self.linha()
   
            
if __name__ == "__main__":
    calculo_calorias()  # Criando um objeto para rodar a lógica
      

  """
 
 
 