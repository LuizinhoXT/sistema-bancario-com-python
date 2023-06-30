import datetime
saldo = 0
LIMITE_SAQUES = 3
countSaques = 0
operacao = 0
extrato = []

hoje = datetime.date.today()

data = f"{hoje.day}/{hoje.month}/{hoje.year}"

def registarOperacao(num, tipo, valor, data):
    global operacao
    aux = (num, tipo, valor, data)
    extrato.append(aux)
    operacao = operacao + 1
    
def depositar(valor):
    lc_tipo_operacao = "deposito"
    global saldo
    saldo = saldo + valor
    registarOperacao(operacao, lc_tipo_operacao, valor, data)
    
def sacar(valor):
    lc_tipo_operacao = "saque"
    global saldo, countSaques
    saldo = saldo - valor
    print(f"valor sacado \n saldo atual: {saldo}")
    countSaques = countSaques + 1
    
    registarOperacao(operacao, lc_tipo_operacao, valor, data)

def estadoDaConta():
    meta_dados = {"Saldo": saldo, "Operações Realizadas": operacao, "Saques disponíveis": LIMITE_SAQUES - countSaques}
    mensagem = "\n".join([f"{chave.title()} = {valor}" for chave, valor in meta_dados.items()]  )
    return mensagem


def retornarExtrato():
    
    for linha in extrato:
        print(linha) 
    
    print(f"\nSaldo atual: {saldo}")