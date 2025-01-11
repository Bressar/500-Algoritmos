# Algoritmo 081

"""   Algoritmo de uma biblioteca que:
- leia o nome do livro que será emprestado
- tipo de usuário (aluno ou professor) 
- considerar que o professor tem um prazo de devolução de 10 dias, aluno 5 dias
- imprimir recibo com: nome livo, tipo usuário e total de dias
 """

# versão simples.

tipo = ''
dias = 0

livro = input(str('Digite o nome do livro: ')).strip().title()

while True:
    escolha = input(str('Escolha: [P] professor ou [A] aluno: ')).strip().upper()

    if escolha == 'P':
        tipo = 'Professor'
        dias = 10
        break
    elif escolha == 'A':
        tipo = 'Aluno'
        dias = 5
        break
    else:
        print('Erro! escolha uma opção válida!')
    
print(f'\n>>> RECIBO <<<\nNome do livro: {livro}\nTipo de usuário: {tipo}\nTotal de dias: {dias}')
    
    