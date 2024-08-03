# Algoritmo 021
# Sudoku 

# é um quebra-cabeça de colocação de números jogado em um tabuleiro 9x9. 
# O jogador deve preencher o tabuleiro de uma maneira muito específica:

# cada linha do tabuleiro deve conter todos os dígitos de 0 a 9 (a ordem não importa)
# cada coluna do tabuleiro deve conter todos os dígitos de 0 a 9 (novamente, a ordem não importa)
# cada um dos nove "blocos" 3x3 (vamos chamá-los de "sub-quadrados") da tabela deve conter todos os dígitos de 0 a 9.
# Se precisar de mais detalhes, você pode encontrá-los aqui.

# Um programa que:

# leia 9 linhas do Sudoku, cada uma contendo 9 dígitos
# (verifique cuidadosamente se os dados inseridos são válidos)
# exiba "Sim" se o Sudoku for válido, e "Não" caso contrário.


# Uma função que verifica se uma lista passada como argumento contém
# nove dígitos de '1' a '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# Uma lista de linhas representando o sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Digite a linha #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Dados da linha incorretos - são necessários 9 dígitos")
    rows.append(row)

ok = True

# Verifica se todas as linhas são válidas.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Verifica se todas as colunas são válidas.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Verifica se todos os sub-quadrados (3x3) são válidos.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Cria uma string contendo todos os dígitos de um sub-quadrado.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Imprime o veredito final.
if ok:
    print("Sim")
else:
    print("Não")
