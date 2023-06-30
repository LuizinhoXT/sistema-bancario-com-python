import conta



def podeFazerSaque(a):
    valor = a
    #saldo_anterior = (conta.sacar- valor)
    msg_falha = f"Não é possível realizar saque pois a conta da excedei o limite diário de saques: {conta.LIMITE_SAQUES}"
    if conta.countSaques == conta.LIMITE_SAQUES:
        
        print(msg_falha)
        return False
    else:
        if conta.saldo == 0:
            print(f"Não é possível realizar saque! \n saldo atual: {conta.saldo}")
        elif valor > conta.saldo:
            print(f"não é possível realizar saque! \n você pode sacar um valor até: {conta.saldo}")
        else:
            if valor > 500:
                print("Você só pode realizar saques de até R$ 500 \n vamos tentar de novo?")
            else:                
                
                conta.sacar(valor)
                

    
def controleDeSaldo(a):
    valor = a
    
    conta.depositar(valor)
"""    if conta.saldo < 0:
        print("Conta com saldo negativo!")
        conta.depositar(valor)
        print(f"Saldo atual: {conta.saldo}")
"""

def chamarExtrato():
    if conta.operacao == 0:
        mensagem = "sem informçãoes"
        return mensagem, False
    else:
        aux = conta.retornarExtrato()
    return aux

def chamarInfoConta():
    aux = conta.estadoDaConta()
    return aux
