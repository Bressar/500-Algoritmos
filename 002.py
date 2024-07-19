## Algoritmo 002
# Mascar chiclete

chiclete = str(input("tem um chiclete?[S] ou [N]")).upper().strip()
if chiclete == "S":
    while True:
        resposta = str(input("tirou o papel? [S] ou [N]")).upper().strip()
        if resposta == "S":
            print("Mastigar e jogar o papel no lixo")
            break
        else:
            print("Tire o papel!")
else:
    print("Pegue um chiclete")
    