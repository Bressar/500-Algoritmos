# Algoritmo 113
# Inner functions - funções internas

# As funções internas só existem no escopo da função principal, se forem chamdas 'fora' não irão funcionar!!

# Exemplo 1

def principal():
    print("Executando a função principal")
    
    def funcao_interna():
        print("executando a função interna")
        
    def funcao_2():
        print("Executando a função 2")
        
    funcao_interna()
    funcao_2()
    
principal()


print('\n-----------------------------------\n' )


# Exemplo 2

def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mult(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div
  
    
print(calculadora("+"))   
print(calculadora("-"))  
print(calculadora("*"))  
print(calculadora("/"))  

print('\n-----------------------------------\n' )

print(calculadora("+")(4,4))   
print(calculadora("-")(4,2))  
print(calculadora("*")(2,2))  
print(calculadora("/")(4,2)) 

print('\n-----------------------------------\n' )
# guardando em uma variável
op = calculadora("+")
print(op(2,2)) 
op = calculadora("-")
print(op(2,2)) 
op = calculadora("*")
print(op(2,2)) 
op = calculadora("/")
print(op(2,2)) 
