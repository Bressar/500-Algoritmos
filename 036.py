# Algoritmo 36
# Cálculo de salário

def calculo_salario():
    while True:
        print("Insira as informações: \n")
        try:
            valor_hora_aula = float(input('Valor da hora aula: '))
            total_horas_mes = int(input('Total de horas trabalhadas no mês: '))
            break
        except ValueError:
            print('Erro! Valor inválido')
            
    desconto_inss = (valor_hora_aula * total_horas_mes) * 0.1 # 10% do salário bruto
    desconto_irs = (valor_hora_aula * total_horas_mes) * 0.2 # 20% do salário bruto
    salario_liquido = (valor_hora_aula * total_horas_mes) - (desconto_inss + desconto_irs)

    print('--' * 20)
    print(f'valor hora/aula: \t€ {valor_hora_aula:.2f}')
    print(f'Total de horas trabalhadas no mês:€ {total_horas_mes:.2f}')
    print(f'Desconto INSSS:\t€ {desconto_inss:.2f}')
    print(f'desconto IRS:\t€ {desconto_irs:.2f}')
    print('--' * 20)
    print(f'Salário Líquido: € {salario_liquido:.2f}')
    print('--' * 20)


calculo_salario()
