# Algoritmo 104
# Validação de e-mail (verificar se é um e-mail válido)

email = input("Digite o e-mail: ").strip()

def validar_email(email):
    # Regra 1: Deve conter exatamente um '@'
    if email.count('@') != 1:
        return False

    # Regra 2: Não pode começar ou terminar com '@'
    if email.startswith('@') or email.endswith('@'):
        return False

    # Regra 3: Não pode conter espaços
    if ' ' in email:
        return False

    # Regra 4: Deve terminar com '.com' (domínio simples)
    if not email.endswith('.com'):
        return False

    # Regra 5: Deve ter algo depois do '@' (domínio)
    dominio = email.split('@')[1] # tudo que vem de pois do @
    if len(dominio) < 5:  # mínimo "x.com" (exemplo)
        return False

    return True

# Entrada do usuário

if validar_email(email):
    print("Email válido")
else:
    print("Email inválido")
