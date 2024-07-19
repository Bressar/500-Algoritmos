## Algoritmo 003
# Trocar lâmpada

lampada = str(input("A lâmpada está fora do alcance? [S] ou [N]? ")).strip()
if lampada in "Ss":
    print("Pegar a escada")
else:
    print("Pegar a lâmpada")
quente = str(input("A lâmpada está quente? [S] ou [N]? ")).strip()
if quente in "Ss":
    print("Pegar pano e tirar a lâmpada queimada")
else:
    print("Tirar lâmpada queimada")
    
print("Colocar lâmpada boa.")
