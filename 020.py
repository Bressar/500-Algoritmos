# Algoritmo 020
# Encontre a palavra

word = input("Escreva a palavra que você quer encontrar: ").upper()
strn = input("Digite a string na qual você deseja procurar: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Yes")
else:
	print("No")
	   