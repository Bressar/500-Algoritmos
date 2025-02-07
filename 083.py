# Algoritmo 083
""" 
Algoritmo que: informe a quantidade de calorias de uma refeição, a partir da escolha do usuário, que deverá informar: 
- prato
- sobremesa
- bebida
Usando a tabela fornecida: """

class calculo_calorias:
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
            if self.prato not in '1234':
                print('Escolha inválida! Tente novamente!') 
            elif self.prato == "1":
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
            self.linha()
   
            
if __name__ == "__main__":
    calculo_calorias()  # Criando um objeto para rodar a lógica
      

 
 
 
 
 
 
 
 
 
 
 
# tabela_1 = [
#             {'prato': 
#                 {'vegetariano': 180,
#                     'peixe': 230,
#                     'frango': 250,
#                     'carne': 350}
#             },
#             {'sobremesa':
#                 {'abacaxi': 75,
#                  'sorvete diet':110,
#                  'mousse diet': 170,
#                  'mousse chocolate': 200}               
#             },
#             {'bebida':
#                 {'chá': 20,
#                  'suco de laranja': 70,
#                  'suco de melão': 100,
#                  'refrigerante diet': 65                    
#                 }               
#             }
#         ]
       
        
        
       # print (self.tabela[0][1][1])
        # print (self.tabela[0][1][3])
        # print (self.tabela[0][1][5])
        # print (self.tabela[0][1][7])   
        # self.linha()
        # print (self.tabela[1][1][0])
        # print (self.tabela[1][1][2])
        # print (self.tabela[1][1][4])
        # print (self.tabela[1][1][6])  
        # self.linha()
        # print (self.tabela[2][1][0])
        # print (self.tabela[2][1][2])
        # print (self.tabela[2][1][4])
        # print (self.tabela[2][1][6])  
        # self.linha()   