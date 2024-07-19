## Algoritmo 001
# Fritar Ovo

fogo = False
recomecar = False
frigideira = False
ovo = False
oleo = False
sal = False

def fritar_ovo(frigideira=False, ovo=False, oleo=False, sal=False, fogo=False):
    global recomecar
    while recomecar == False:
        if frigideira == False and ovo == False and oleo == False and sal == False:
            print("Pegar frigideira, ovo, óleo e sal")
            recomecar = True
        else:
            recomecar = False
            if frigideira == True:
                print('colocar óleo na frigideira')
            else:
                print('frigideira sem óleo, recomece')
                recomecar = True
            if oleo == True:
                print("Acender o fogo")
            else:
                print('fogo apagado, recomece')
                recomecar = True    
            if fogo == True:
                print("Esperar o óleo esquentar")
            elif ovo == True:
                print("Colocar o ovo")           
            else:
                print('falta o ovo, recomece')
                recomecar = True  
            if sal == True:
                print("coloque o sal")
            else:
                print("acabou o sal, recomece")
            print("retirar quando pronto")
            break
        
fritar_ovo(True, True, True, True)
print()
fritar_ovo()
  