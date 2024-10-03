# Algoritmo 57
# Calculo de peso em cada Planeta

def calculo_gravidade(peso_terra, gravidade_planeta):
    peso_relativo = peso_terra * (gravidade_planeta / 1)
    return peso_relativo

planetas_gravidade = {1: 0.37, 2: 0.88, 3: 0.38, 4: 2.53, 5: 1.07, 6: 0.89, 7: 1.14, 8: 0.063, 9: 0.1653}
planetas_nome = {1: "Mercúrio", 2: "Vênus", 3: "Marte", 4: "Júpiter", 5: "Saturno", 6: "Urano", 7: "Netuno",  8: "Plutão", 9: "Lua"}

while True:
    print('**' * 20)
    print("CALCULADORA PLANETÁRIA DE PESO")
    print('**' * 20)
    peso_terra = float(input('Informe seu peso em Kgs: '))
    print('--' * 20)

    while True:
        print('--' * 20)
        print("""[1] - Mercúrio
[2] - Vênus
[3] - Marte
[4] - Júpiter
[5] - Saturno
[6] - Urano
[7] - Netuno
[8] - Plutão
[9] - Lua""")
        print('--' * 20)
        planeta_escolhido = str(input('Escolha um planeta: ')).strip()
        if len(planeta_escolhido) !=1 or planeta_escolhido not in "123456789":
            print("Valor inválido, escolha novamente!")
        else:
            planeta_escolhido = int(planeta_escolhido)
            break
        print('--' * 20)
    
    nome_planeta = planetas_nome[planeta_escolhido]    
        
    peso_relativo = calculo_gravidade(peso_terra, planetas_gravidade[planeta_escolhido])
    # gravidade = planetas_gravidade[planeta_escolhido]
    # peso_relativo = peso_terra * (gravidade / 1)
    
    print(f'\nO seu peso de {peso_terra:.2f} Kg na Terra.\nSerá de {peso_relativo:.2f} Kg em {nome_planeta}.')
    print('--' * 20)

    sair = input("\nPara continuar pressione a tecla [C]\nPara sair pressione qualquer tecla.\n").strip().upper()
    if sair != "C":
        print('--' * 20)
        print("Saindo do programa...")
        print('--' * 20)
        break
    

# print(calculo_gravidade(70, 0.38)) # peso de 70 kg em Marte
