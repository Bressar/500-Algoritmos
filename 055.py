# Algoritmo 55
# Qual a capital do Brasil

def capital_do_brasil():
    while True:
        resposta = str(input("Qual a capital do Brasil? ")).strip()
        if resposta == "Brasília" or resposta == "BRASÍLIA":         
            print("Parabéns! Você acertou!")
            break       
        elif resposta == "Brasilia" or resposta == "BRASILIA" or resposta == "Brazilia" or resposta == "BRAZÍLIA":
            print("Quase lá!\nMas atenção para a grafia: Brasília ou BRASÍLIA")   
        else:
            print("BURRÃO!\nVai estudar geografia!")


capital_do_brasil()
