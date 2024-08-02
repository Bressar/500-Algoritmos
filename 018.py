# Algoritmo 018
# Anagramas

str_1 = input("Digite a 1° string: ").upper().strip()
str_2 = input("Digite a 2° string: ").upper().strip()

str_1 = str_1.replace(' ', '')
str_2 =str_2.replace(' ', '')

# list_1 = str_1.split() # só funciona se a string tiver + de uma palavra
# list_2 = str_2.split()

list_1 = sorted(list(str_1))
list_2 = sorted(list(str_2))

# list_1.sort()
# list_2.sort()

# print(list_1) # for debug
# print(list_2)

palavra_1 = ''.join(list_1)
palavra_2 = ''.join(list_2)

if palavra_1 == palavra_2:
    print(f'{str_1} e {str_2} são um anagrama')
else:
     print(f'{str_1} e {str_2} não são um anagrama')   


# Versão pro

str_1 = input("Digite a 1° string: ")
str_2 = input("Digite a 2° string: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print(f'{str_1} e {str_2} são um anagrama')
else:
	print(f'{str_1} e {str_2} não são um anagrama')
 
 