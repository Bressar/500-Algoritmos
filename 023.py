# Algoritmo 023
# Dias da Semana
# 
""" Implementar uma classe chamada Weeker. – esse nome vem do fato de que os objetos dessa classe serão capazes de armazenar e manipular os dias da semana.

O construtor da classe aceita um argumento – uma string. A string representa o nome do dia da semana e os únicos valores aceitáveis devem vir do seguinte conjunto:

Mon Tue Wed Thu Fri Sat Sun

Invocar o construtor com um argumento fora desse conjunto deve gerar a exceção WeekDayError.

A classe deve fornecer as seguintes funcionalidades:

Objetos da classe devem ser "imprimíveis", ou seja, devem ser capazes de se converter implicitamente em strings da mesma forma que os argumentos do construtor;

A classe deve ser equipada com métodos de um parâmetro chamados add_days(n) e subtract_days(n), onde n é um número inteiro, e que atualizam o dia da semana armazenado dentro do objeto de forma a refletir a mudança de data pelo número indicado de dias, para frente ou para trás.
Todas as propriedades do objeto devem ser privadas;

Saída esperada:
    
Mon
Tue
Sun
Sorry, I can't serve your request. """


class WeekDayError(Exception):
    pass

class Weeker:
    DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day): # construtor recebe 1 parâmetro (nome do dia) e confere se ele existe na lista
        if day not in self.DAYS_OF_WEEK:
            raise WeekDayError("Invalid day of the week") 
        self.__day = day

    def __str__(self):
        return self.__day
    
    def add_days(self, n):  # recebe 1 parâmetro (numero do dia)
        current_index = self.DAYS_OF_WEEK.index(self.__day)
        new_index = (current_index + n) % 7 # % 7 garante que o novo índice esteja dentro do intervalo de 0 a 6
        self.__day = self.DAYS_OF_WEEK[new_index]

    def subtract_days(self, n):
        current_index = self.DAYS_OF_WEEK.index(self.__day)
        new_index = (current_index - n) % 7
        self.__day = self.DAYS_OF_WEEK[new_index]
    
    
"""método add_days da classe Weeker. Ele recebe um parâmetro n, que representa o número de dias
    a serem adicionados ao dia atual armazenado no objeto.

O que cada linha faz:

current_index = self.DAYS_OF_WEEK.index(self.__day): Esta linha encontra o índice do dia atual
(self.__day) na lista de dias da semana (self.DAYS_OF_WEEK). Isso nos dá a posição do dia atual na lista.

new_index = (current_index + n) % 7: Esta linha calcula o novo índice do dia após adicionar n dias ao índice atual.
Como há 7 dias na semana, o operador % 7 garante que o novo índice esteja dentro do intervalo de 0 a 6, 
permitindo que a semana "dê a volta" quando ultrapassar o último dia.

self.__day = self.DAYS_OF_WEEK[new_index]: Esta linha atualiza o dia armazenado no objeto para
o novo dia correspondente ao novo índice calculado na linha anterior.
Isso significa que o dia do objeto agora será o dia correspondente ao novo índice na lista de dias da semana.  """  


try:
    weekday = Weeker('Mon') # determina qual é o dia da semana, se existe, imprime
    print(weekday)
    print('*' * 20)
    
    weekday.add_days(15) # a contar de 'Mon', 15 dias no futuro dá terça-feira
    print(weekday)
    print('*' * 20)
    
    weekday.subtract_days(23) #  # a contar de 'Mon', 23 dias para trás dá domingo 'Sun'
    print(weekday)
    print('*' * 20)
    
    weekday = Weeker('Monday')# não existe, dá erro
    print('*' * 20)
    
except WeekDayError:
    print("Sinto muito, não posso responder...")

