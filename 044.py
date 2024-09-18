# Algoritmo 44
# Fatorial

# Usando while

numero = int(input("Insira um número para saber o seu fatorial: "))
fatorial = 1 #começa em 1 para não ser multiplicado por zero
i = 2
while i <= numero: # vai parar de multiplicar quando chegar no valor do numero
    fatorial = fatorial * i # vai multiplicando a cada loop com um valor maior de i até i chegar no valor do numero
    i = i + 1 # vai começar em e adicionando de 1 em 1 até chegar no numero

print(f"O valor de {numero}! é = {fatorial}")

# Usando for
fatorial2 = 1
for i in range (numero, 0, -1):
    fatorial2 *= i
    i * (i - 1)
    print (i, " X ", i -1, )# for debug
print(fatorial2)
