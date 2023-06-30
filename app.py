import controle
import datetime
sistema = True
menu = "digite s para sacar\ndigite d para depositar\ndigite e para obter o estrato\ndigide q para sair\ndigite c para obter informações da conta"
aux = 0



hoje = datetime.date.today()

def receberValor():
    print("Digite o valor: ")
    aux = int(input())
    return aux
    
ciclos = 0
print(menu)
while sistema == True:
    
    if ciclos >= 1:
        print(f"######### O que deseja fazer agora? ######### \n")
    
    
    sel = str(input())
    
    if sel == "s":
        controle.podeFazerSaque(receberValor())
    elif sel == "e":    
        print(controle.chamarExtrato())
    elif sel == "d":
        controle.controleDeSaldo(receberValor())
    elif sel == "c":
        print(controle.chamarInfoConta())
    elif sel == "q":
        break
    
        
    ciclos = ciclos + 1
        
    

    