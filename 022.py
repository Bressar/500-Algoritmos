# Algoritmo 022
# Timer

""" Precisamos de uma classe capaz de contar segundos.
A classe que você vai escrever será usada para lançar foguetes em missões internacionais para Marte. É uma grande responsabilidade.

Sua classe será chamada Timer. Seu construtor aceita três argumentos que representam horas (um valor no intervalo [0..23] – usaremos o formato de horário militar), minutos (no intervalo [0..59]) e segundos (no intervalo [0..59]).

Zero é o valor padrão para todos os parâmetros acima. Não é necessário realizar nenhuma verificação de validação.

A própria classe deve fornecer as seguintes funcionalidades:

Objetos da classe devem ser "imprimíveis", ou seja, devem ser capazes de se converter implicitamente em strings no seguinte formato: "hh:mm
", com zeros à esquerda adicionados quando qualquer um dos valores for menor que 10;
A classe deve ser equipada com métodos sem parâmetros chamados next_second() e previous_second(), que incrementam o tempo armazenado dentro dos objetos em +1/-1 segundo, respectivamente.
Use as seguintes dicas:

Todas as propriedades do objeto devem ser privadas;
Considere escrever uma função separada (não um método!) para formatar a string de tempo.  """

# Versão 1
# mostra 1 segundo a frente e um segundo atrás do valor fornecido

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__format_time(self.__hours)}:{self.__format_time(self.__minutes)}:{self.__format_time(self.__seconds)}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23

    def __format_time(self, time):
        return f"0{time}" if time < 10 else str(time)


timer = Timer(23, 59, 59)
print(f'horário atual ->  {timer}')
timer.next_second()
print(f'horário futuro ->  {timer}')
timer.prev_second()
print(f'horário pasado - >  {timer}')


# Versão 2
# Versão melhorada:

def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return two_digits(self.__hours) + ":" + \
               two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    