# Algoritmo 024
# Dosagem de remédio

""" 
A partir da idade e peso do paciente calcula a dosagem de determinado medicamento
e imprime a receita informando quantas gotas tomar por dose.
O medicamento possui 500mg por ml, cada ml equivale a 20 gotas.
Adultos e >= 12 anos, e acima de 60 kg devem tomar 100 mg, peso abaixo de 60 kg tomar 875 mg.

Crianças abaixo de 12 anos, a dosagem é a seguinte:
    5 a 9 kg -> 125 mg
    9.1 a 16 kg -> 250 mg
    16.1 a 24 kg -> 375 mg
    24.1 a 30 kg -> 500 mg
    30 a 59.99 kg -> 750 mg 
"""
class Paciente:
    gotas = int(500 / 20)
    dosagem_gotas = 0
    
    def __init__(self, nome=None, idade=None, peso=None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
    
    def __str__(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade}, Peso: {self.__peso} kg"
    
    def print_receita(self):
        print("--" * 30)
        print(f"RECEITA:\n"
            f"Paciente: {self.__nome}\n"
            f"Peso: {self.__peso} Kg\n"
            f"Idade: {self.__idade}\n"
            f"Deve tomar {self.dosagem_gotas} gotas a cada dose da medicação.")
        print("--" * 30)
    
    def dosagem(self):
        if self.__peso < 5:
            print("Não pode tomar a medicação, abaixo do peso!\n Consulte seu Médico.")
        elif self.__idade >= 12 and self.__peso >= 60:
            self.dosagem_gotas = int(1000 / self.gotas)  # acima de 60 kg
            self.print_receita()
        elif self.__idade >= 12 and self.__peso < 60:
            self.dosagem_gotas = int(875 / self.gotas)  # abaixo de 60 kg
            self.print_receita()
        elif self.__idade < 12:  # Lógica para crianças abaixo de 12 anos
            if 5 <= self.__peso <= 9:
                self.dosagem_gotas = int(125 / self.gotas)
            elif 9.1 <= self.__peso <= 16:
                self.dosagem_gotas = int(250 / self.gotas)
            elif 16.1 <= self.__peso <= 24:
                self.dosagem_gotas = int(375 / self.gotas)
            elif 24.1 <= self.__peso <= 30:
                self.dosagem_gotas = int(500 / self.gotas)
            elif 30 < self.__peso <= 59.99:
                self.dosagem_gotas = int(750 / self.gotas)
            self.print_receita()
        else:
            pass


paciente1 = Paciente("Oldaque", 103, 70)
paciente2 = Paciente("Jurema", 99, 42)
paciente3 = Paciente("Zulmira", 11, 40)
paciente4 = Paciente("Joseverson", 9, 25)
paciente5 = Paciente("Creuza", 8, 23)
paciente6 = Paciente("Biafra", 6, 15)
paciente7 = Paciente("Esqueletinho", 5, 8)
paciente8 = Paciente("Bebê diabo", 1, 4)


paciente1.dosagem()
paciente2.dosagem()
paciente3.dosagem()
paciente4.dosagem()
paciente5.dosagem()
paciente6.dosagem()
paciente7.dosagem()
paciente8.dosagem()
