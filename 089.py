# Algoritmo 88
# A partir da placa de um veículo informar o mês de licenciamento, usando um dicionário ou uma tabela

# Versão usando um DICIONÁRIO - menos processamento
tabela_dut_data = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abril',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '0': 'Outubro'
}

while True:
    placa_final = input('Digite a placa (6 caracteres):\n').strip()

    if len(placa_final) == 6:
        numero_final = placa_final[-1]
        
        if numero_final.isnumeric():
            break
        else:
            print('O último caractere da placa deve ser um número.')
    else:
        print('A placa deve ter exatamente 6 caracteres.')

# mes_licenciamento = tabela_dut_data.get(numero_final, 'Mês não encontrado')
# # versão com mais uma verificação, mas desnecessária nesse caso.

mes_licenciamento = tabela_dut_data[numero_final]

print(f'O mês de licenciamento do veículo é {mes_licenciamento}.')  



# Versão usando uma TABELA # faz mais iterações
tabela_dut_data =[
                    ['1', 'Janeiro'],
                    ['2', 'Fevereiro'],
                    ['3', 'Março'],
                    ['4', 'Abril'],
                    ['5', 'Maio'],
                    ['6', 'Junho'],
                    ['7', 'Julho'],
                    ['8', 'Agosto'],
                    ['9', 'Setembro'],
                    ['0', 'Outubro']                  
                ]
while True:
    placa_final = input('Digite a placa:\n').strip() # placa de carro deve ter 6 caracteres - padrão PT

    if len(placa_final) == 6 and placa_final[-1].isnumeric():
        numero_final = placa_final[-1]
        break
    else:
        print('Valor inválido, digite a placa novamente')

for numero, mes in tabela_dut_data:
    if numero == numero_final:
        mes_licenciamento = mes
        break

print(f'O mês de licenciamento do veículo é {mes_licenciamento}.')  
  