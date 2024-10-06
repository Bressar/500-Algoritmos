# Algoritmo 61
# Encontrar o Gentílico

def gentilico_brasil():
    siglas_estados = {
    "AC" : "Acreano",
    "AL" : "Alagoano",
    "AP" : "Amapaense",
    "AM" : "Amazonense",
    "BA" : "Baiano",
    "CE" : "Cearense",
    "DF" : "Brasiliense",
    "ES" : "Capixaba",
    "GO" : "Goiano",
    "MA" : "Maranhense",
    "MT" : "Mato-grossense",
    "MS" : "Sul-mato-grossense",
    "MG" : "Mineiro",
    "PA" : "Paraense",
    "PB" : "Paraibano",
    "PR" : "Paranaense",
    "PE" : "Pernambucano",
    "PI" : "Piauiense",
    "RJ" : "Carioca",
    "RN" : "Potiguar",
    "RS" : "Gaúcho",
    "RO" : "Rondoniense",
    "RR" : "Roraimense",
    "SC" : "Catarinense",
    "SP" : "Paulista",
    "SE" : "Sergipano",
    "TO" : "Tocantinense"
    }

    while True:
        print('--' * 30)
        sigla = input("Digite a sigla do Estado que você quer saber o gentílico\n(nome dos indivíduos que nascem nesses estados):\n").strip().upper()
        if sigla not in siglas_estados:
            print('--' * 20)
            print("Sigla inexistente, Digite novamente.")
            print('--' * 20)
        else:
            for key in siglas_estados:
                if key == sigla:
                    print('--' * 30)
                    print(f'Quem nasce em {sigla} é {siglas_estados[key]}.')
                    print('--' * 20)               
        sair = input("Para continuar prima qualquer tecla.\nPara sair prima [S]\n").upper().strip()
        if sair == "S":
            print('--' * 20)
            print("Encerrando o programa...")
            print('--' * 20)
            break
                
                
gentilico_brasil()   
             