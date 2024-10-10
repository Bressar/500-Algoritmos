# Algoritmo 65
# Função para calcular o determinante de uma matriz quadrada 2x2

def calcular_determinante(matriz):
    # Diagonal principal
    DetPrincipal = 0
    DetSecundaria = 0
    dimensao = len(matriz)

    # Calculando a diagonal principal
    for i in range(dimensao):
        DetPrincipal += matriz[i][i]

    # Calculando a diagonal secundária
    for i in range(dimensao):
        DetSecundaria += matriz[i][dimensao - 1 - i]

    # O determinante é a diferença entre a diagonal principal e a secundária
    determinante = DetPrincipal - DetSecundaria
    return determinante

# Função principal
def main():
    # Entrada da dimensão da matriz (2x2, 3x3, etc.)
    dimensao = int(input("Informe a dimensão da matriz quadrada para cálculo do determinante: "))

    # Criando a matriz de acordo com a dimensão informada
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            valor = int(input(f"Informe o valor para matriz[{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)

    # Calculando o determinante
    determinante = calcular_determinante(matriz)
    
    # Exibindo o resultado
    print(f"\nO determinante da matriz é: {determinante}")

# Execução do programa
if __name__ == "__main__":
    main()
