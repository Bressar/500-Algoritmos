# Algoritmo 014
# # Cifra de César – mais detalhes aqui: https://en.wikipedia.org/wiki/Caesar_cipher.

# Cada letra da mensagem é substituída pela sua próxima consequente (A torna-se B, B torna-se C, e assim por diante).
# A única exceção é Z, que se torna A.

text = input("Escreva a mensagem: ")
cipher = ''
for char in text: # percorre todos os caracteres da string
    if not char.isalpha(): # Se não for uma letra, pula o loop
        continue
    char = char.upper() # deixa em maiúscula
    code = ord(char) + 1 # passa para code point e acrescenta +1
    if code > ord('Z'): # se o cde point for maior que Z, passa pro A
        code = ord('A')
    cipher += chr(code) # sifra recebe letra por letra, já convertida em caracter novamente

print(cipher)

# agora decripitando:

cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)


# Cifra de César - versão 2
# Aceita maiúsculas e minúsculas e pede um valor de distância entre uma letra


text = input("Escreva a mensagem: ")

# Insira um valor de deslocamento válido (repita até conseguir)).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Digite o valor de deslocamento (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Valor de deslocamento incorreto!")

cipher = ''

for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Make correction.
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char

print(cipher)
    

