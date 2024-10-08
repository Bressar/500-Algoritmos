# Algoritmo 63
# Média escolar de um aluno - usando banco de dados


class Estudantes:
    
    media_final = 0
    
    def __init__(self, id_estudante=None, nome_estudante=None, notas=[]):
        self.__id_estudante = id_estudante
        self.__nome_estudante = nome_estudante
        self.__notas = notas
        
    def linha(self, padrao='--', valor=0):
        print(padrao * valor)
    
        
    def adicionar_aluno(self):
        while True:
            self.__id_estudante = str(input("ID estudante (4 números): ")).strip().upper()
            if len(self.__id_estudante) == 4 and self.__id_estudante.isalpha():
                # acrescenta ao banco de dados
                print('ID cadastrado no sistema')
                self.linha('--', 30)
                break
            else:
                print("Formato inválido! O ID deve ter 4 números.")           
        while True:
            try:
                self.__nome_estudante = input("Nome do aluno(a): ").strip().title()
                if not all(part.isalpha() for part in self.nome__estudante.split()):
                    raise ValueError("O nome deve conter apenas letras.")
                else:
                    # acrescenta ao banco de dados
                    print(f"{self.__nome_estudante} cadastrado no sistema")
                    self.linha('--', 30)   
                    break
            except ValueError:
                print("Formato inválido! tente novamente.")
                self.linha('--', 30)
                
                
    def remover_estudante(self):
        self.__id_estudante = str(input("Digite o ID para remover o estudante do cadastro:\n")).strip().upper()
        if self.__id_estudante not in #banco de dados#:
            print('ID encontrado!')
        else:
            #remove(remover_ID)
            print('ID Removido!')
            self.linha('--', 10)

                    
    def acrescentar_notas(self):
        self.__notas = []
        for i in range(1, 5):  # Loop de 1 a 4 para cada bimestre
            while True:
                try:
                    nota = float(input(f'Insira a nota do {i}° Bimestre: '))
                    if 0 <= nota <= 10:  # Condição para verificar se a nota está entre 0 e 10
                        self.__notas.append(nota)  # Armazena a nota na lista
                        
                        #banco de dados recebe nota do bimestre[i]
                        
                        break  # Sai do loop e passa para a próxima nota
                    else:
                        print('A nota deve ser maior/igual a 0 ou menor/igual a 10!')
                        self.linha('--', 30)
                except ValueError:
                    print('Valor inválido! Tente novamente')
                    self.linha('--', 30)
        media_final = sum(self.__notas) / len(self.__notas)  # Calcula a média
        return media_final


# implementação

base_dados_estudantes = Estudantes(None, None, [])

self.linha('**', 20)
print("MENU DE OPERAÇÕES\nBanco de Dados")
self.linha('**', 20)
option = input("""[A] Adicionar estudante
[R] Remover estudante
[N] Acrescentar Notas
[L] Listar Notas
[F] Apresentar média final
[E] Editar informações
[S] Sair """).strip().upper()[0]
self.linha('**', 20)

base_dados_estudantes.adicionar_aluno()
base_dados_estudantes.remover_estudante()
base_dados_estudantes.acrescentar_notas()
























        
    """ def acrescentar_notas():
        while True:
            try:
                bimestre_1 = float(input('Insira a nota do 1° Bimestre: '))
                if bimestre_1 >= 0 and bimestre_1 <= 0:
                    break 
                    #banco de dados recebe bimestre_1
                else:
                    print('A nota deve ser maior/igual a 0 ou ser menor/igual a 10!')
            except ValueError:
                print('Valor inválido! Tente novamente')
        while True:
            try:
                bimestre_2 = float(input('Insira a nota do 2° Bimestre: '))
                if bimestre_2 >= 0 and bimestre_2 <= 0:
                    break 
                    #banco de dados recebe bimestre_2
                else:
                    print('A nota deve ser maior/igual a 0 ou ser menor/igual a 10!')
            except ValueError:
                print('Valor inválido! Tente novamente')
        while True:
            try:
                bimestre_3 = float(input('Insira a nota do 3° Bimestre: '))
                if bimestre_3 >= 0 and bimestre_3 <= 0:
                    break 
                    #banco de dados recebe bimestre_3
                else:
                    print('A nota deve ser maior/igual a 0 ou ser menor/igual a 10!')
            except ValueError:
                print('Valor inválido! Tente novamente')           
        while True:
            try:
                bimestre_4 = float(input('Insira a nota do 4° Bimestre: '))
                if bimestre_4 >= 0 and bimestre_4 <= 0:
                    break 
                    #banco de dados recebe bimestre_3
                else:
                    print('A nota deve ser maior/igual a 0 ou ser menor/igual a 10!')
            except ValueError:
                print('Valor inválido! Tente novamente')             
                
        media_final = (bimestre_1 + bimestre_2 + bimestre_3 + bimestre_4 ) / 4
        return media_final

    """