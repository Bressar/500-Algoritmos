# Algoritmo 026
# # Gerador de Fibonacci

# p = pp = 1: Inicializa as duas primeiras variáveis da
# sequência de Fibonacci (p e pp) com o valor 1,
# que representam os dois primeiros números de Fibonacci.

# O loop for i in range(n) itera n vezes, onde i representa
# o índice da iteração atual (0 a n-1).

# Condições no loop:
# Se i é 0 ou 1 (os dois primeiros números da sequência),
# a função usa yield 1 para retornar 1 como o próximo número de Fibonacci.

# Para índices maiores que 1, a sequência de Fibonacci começa a ser calculada:
# n = p + pp: Calcula o próximo número de Fibonacci como a soma dos dois anteriores (p e pp).
# pp, p = p, n: Atualiza os valores de pp e p. Agora, pp assume o valor de p,
# e p assume o valor do novo número de Fibonacci calculado (n).

# yield n: Retorna o próximo número de Fibonacci.
    
    
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)
