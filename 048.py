# Algoritmo 48
# Cálculo em salários mínimos

def calculo_salario_minimo():
    while True:
        try:
            salario_minimo = float(input("Entre com o valor do sário mínimo: "))
            break
        except ValueError:
            print("ERRO! digite novamente")       
    while True:
        try:
            salario_pessoa = float(input("Entre com o salário da pessoa: "))
            break
        except ValueError:
            print("ERRO! digite novamente")
            
    resultado = salario_pessoa / salario_minimo

    print(f'A pessoa ganha: {resultado:.2f} salários mínimos')
   
    
calculo_salario_minimo()
