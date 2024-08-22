# Algoritmo 027
# Histograma de Frequência de Caracteres

""" Um arquivo de texto contém algum texto (nada incomum),
mas precisamos saber com que frequência (ou quão raramente) cada letra aparece no texto.
Tal análise pode ser útil em criptografia, então queremos ser capazes de fazer isso em relação ao alfabeto latino.

**Sua tarefa é escrever um programa que:**

- Solicite ao usuário o nome do arquivo de entrada;

- Leia o arquivo (se possível) e conte todas as letras latinas
    (letras minúsculas e maiúsculas são tratadas como iguais);
    
- Imprima um histograma simples em ordem alfabética 
    (somente contagens não zero devem ser apresentadas).
    
- Crie um arquivo de teste para o código e verifique se o seu histograma contém resultados válidos.

Assumindo que o arquivo de teste contém apenas uma linha preenchida com: 
    
    aBc
    
O resultado é:
    
    a -> 1
    b -> 1
    c -> 1

*Dica: Um dicionário é um meio de coleta de dados perfeito para armazenar as contagens.
       As letras podem ser as chaves, enquanto os contadores podem ser os valores.* """
       
from os import strerror

# Criação do dicionário com todas as letras / 26 contadores para cada letra latina.
# Usando compreensão para fazer isso.
contadores = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
# print(contadores) # for debug

nome_do_arquivo = input("Escreva o nome do arquivo: ")

try:
    arquivo = open(nome_do_arquivo, 'rt')
    for line in arquivo: 
        for char in line:
            if char.isalpha(): # se for uma letra
                contadores[char.lower()] += 1 # será tratada como minúscula e atualiza o contador apropriado.
    arquivo.close()       

# exibindo os contadores
    for char in contadores.keys():
        contador = contadores[char]
        if contador > 0:
            print(char, '->', contador)
            
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    
    
    
    

    
### Versão refatorada

""" **Refatorar o código anterior**

- O histograma de saída será ordenado com base na frequência dos caracteres 
    (o contador maior deve ser apresentado primeiro).
    
- O histograma deve ser enviado para um arquivo com o mesmo nome do arquivo de entrada,
    mas com o sufixo ".hist" (ele deve ser concatenado ao nome original).
    
- Assumindo que o arquivo de entrada contenha apenas uma linha preenchida com:
    
    cBabAa

O resultado é:

    a -> 3
    b -> 2
    c -> 1 """
    
from os import strerror

dicionario = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
nome_do_arquivo = input("Escreva o nome do arquivo: ")

try:
    # Primeiro bloco: leitura do arquivo
    file = open(nome_do_arquivo, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                dicionario[char.lower()] += 1
    file.close()

    # Segundo bloco: escrita no arquivo .hist
    file = open(nome_do_arquivo + '.hist', 'wt') # salva com o  com o sufixo ".hist" 
    
    # Ordenando e escrevendo o histograma no arquivo
    # Observação:função lambda para acessar os elementos do dicionário e configur o reverse para obter uma ordem válida.
    for char in sorted(dicionario.keys(), key=lambda x: dicionario[x], reverse=True):
        c = dicionario[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    
    file.close()
    print("Histograma salvo em", nome_do_arquivo + '.hist')

except IOError as e:
    print("Ocorreu um erro de E/S: ", strerror(e.errno))
    
    
# Visualizando o resultado
leitura = open(nome_do_arquivo + '.hist', "rt")
line = leitura.readline()

while line != '':
    print(line, end='')  # Imprime a linha inteira sem adicionar uma nova linha extra
    line = leitura.readline()

leitura.close()
   
