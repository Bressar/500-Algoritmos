# Algoritmo 016
# Validador de IBAN

# Um número de conta compatível com IBAN consiste em:

# um código de país de duas letras retirado do padrão ISO 3166-1 (por exemplo, FR para França, 
# GB para Grã-Bretanha, DE para Alemanha, e assim por diante)

# dois dígitos de verificação usados para realizar verificações de validade – testes rápidos e simples,
# mas não totalmente confiáveis, que mostram se um número é inválido (distorcido por um erro de digitação)
# ou parece estar correto;

# o número de conta real (até 30 caracteres alfanuméricos – o comprimento dessa parte depende do país)
# O padrão diz que a validação requer os seguintes passos (de acordo com a Wikipedia):

# (pass0 1) Verifique se o comprimento total do IBAN está correto conforme o país
# (este programa não fará isso, mas você pode modificar o código para atender a esse requisito,
#  se desejar; nota: você precisa ensinar ao código todos os comprimentos usados na Europa)

# (pass0 2) Mova os quatro caracteres iniciais para o final da string 
# (ou seja, o código do país e os dígitos de verificação)

# (pass0 3) Substitua cada letra na string por dois dígitos, expandindo assim a string,
# onde A = 10, B = 11 ... Z = 35;

# (pass0 4) Interprete a string como um número inteiro decimal e calcule o restante 
# desse número dividindo-o por 97; se o restante for 1, o teste do dígito de verificação 
# é aprovado e o IBAN pode ser válido.

# IBAN Validator.

iban = input("Enter IBAN, please: ")
# peça ao usuário para inserir o IBAN (o número pode conter espaços, 
# pois eles melhoram significativamente a legibilidade do número...

iban = iban.replace(' ','') 
# removendo os espaços em branco

if not iban.isalnum():
    print("You have entered invalid characters.")
# o IBAN inserido deve consistir apenas de dígitos e letras    
    
elif len(iban) < 15:
    print("IBAN entered is too short.")
# o IBAN não deve ser menor que 15 caracteres (esta é a variante mais curta, usada na Noruega)

elif len(iban) > 31:
    print("IBAN entered is too long.")
#o IBAN não pode ter mais que 31 caracteres (esta é a variante mais longa, usada em Malta)

else:
    iban = (iban[4:] + iban[0:4]).upper()
    # move os quatro caracteres iniciais para o final do número e converta todas as letras para maiúsculas 
    iban2 = ''
    #variável usada para completar o número, criada substituindo as letras por dígitos 
    for ch in iban:
        if ch.isdigit():# se o caractere for um dígito
            iban2 += ch # é feita a cópia 
        else: # caso contrário...
            iban2 += str(10 + ord(ch) - ord('A')) # .converta-o em dois dígitos 
    iban = int(iban2) # transforma em um número inteiro
    if iban % 97 == 1: # o resto da divisão do iban2 por 97 é igual a 1?
        print("IBAN entered is valid.") # se sim, então sucesso;
    else:
        print("IBAN entered is invalid.") # se não, número inválido

# British: GB72 HBZU 7006 7212 1253 00
# French: FR76 30003 03620 00020216907 50
# German: DE02100100100152517108

