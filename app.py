
import controle
import datetime

hoje = datetime.date.today()

def receberValor():
    print("Digite o valor: ")
    aux = int(input())
    return aux


while True:
    
    
    sel = controle.menu()
    
    if sel == "s":
        controle.chamarSaque(receberValor())
    elif sel == "e":    
        print(controle.chamarExtrato())
    elif sel == "d":
        controle.controleDeSaldo(receberValor())
    elif sel == "c":
        print(controle.chamarInfoConta())
    elif sel == "nu":
        controle.cadastrar_usuario()
    elif sel == "lu":
        controle.chamar_lista_usuarios()
    elif sel == "nc":
        controle.associar_conta()
    elif sel == "q":
        break
        
    

    