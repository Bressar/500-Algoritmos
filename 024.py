# Algoritmo 024
# Pontos em um Plano ( coordenadas cartesianas )

""" Vamos visitar um lugar muito especial – um plano com o sistema de coordenadas cartesianas (você pode aprender mais sobre esse conceito aqui: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Cada ponto localizado no plano pode ser descrito como um par de coordenadas, comumente chamadas de x e y. Queremos que você escreva uma classe em Python que armazene ambas as coordenadas como números de ponto flutuante. Além disso, queremos que os objetos dessa classe avaliem as distâncias entre dois pontos situados no plano.

A tarefa é bastante fácil se você usar a função chamada hypot() (disponível no módulo math), que avalia o comprimento da hipotenusa de um triângulo retângulo (mais detalhes aqui: https://en.wikipedia.org/wiki/Hypotenuse e aqui: https://docs.python.org/3.7/library/math.html#trigonometric-functions).

É assim que imaginamos a classe:

Ela se chama Point;
Seu construtor aceita dois argumentos (x e y, respectivamente), ambos com valor padrão zero;
Todas as propriedades devem ser privadas;
A classe contém dois métodos sem parâmetros chamados getx() e gety(), que retornam cada uma das duas coordenadas (as coordenadas são armazenadas de forma privada, então não podem ser acessadas diretamente de fora do objeto);
A classe fornece um método chamado distance_from_xy(x, y), que calcula e retorna a distância entre o ponto armazenado dentro do objeto e o outro ponto dado como um par de valores de ponto flutuante;
A classe fornece um método chamado distance_from_point(point), que calcula a distância (como o método anterior), mas a localização do outro ponto é dada como outro objeto da classe Point.
Complete o modelo que fornecemos no editor, execute seu código e verifique se a saída é igual à nossa. """

#Expected output
""" 1.4142135623730951
    1.4142135623730951 """

import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.getx() - x, self.gety() - y)

    def distance_from_point(self, point):
        return math.hypot(self.getx() - point.getx(), self.gety() - point.gety())

# Example usage:
point1 = Point(1, 1)
point2 = Point(2, 2)
print(point1.distance_from_xy(2, 2))  # Output: 1.4142135623730951
print(point1.distance_from_point(point2))  # Output: 1.4142135623730951
