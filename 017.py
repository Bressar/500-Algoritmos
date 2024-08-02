# Algoritmo 017
# Palindromos

# modelo de lista invertida -> text[::-1]

text = input("Escreva o texto: ")

# Remove todos espaços...
text = text.replace(' ','')

if len(text) > 1 and text.upper() == text[::-1].upper():
    # Se o comprimento do texto (depois da remoção dos espaços) é maior que 1 (len(text) > 1).
    # Se o texto, convertido para maiúsculas (text.upper()), é igual à sua versão invertida
    # e também convertida para maiúsculas (text[::-1].upper()).
	print("É um palíndromo")
else:
	print("Não é um palíndromo")
