import datetime
saldo = 0
LIMITE_SAQUES = 3
countSaques = 0
countOperacao = 1
numero_da_conta = 0
extrato = []
numero_da_conta = 1
Lista_de_contas = []

hoje = datetime.date.today()

data = f"{hoje.day}/{hoje.month}/{hoje.year}"

def criar_conta(cpf,lista_contas):
    global Lista_de_contas
    
    conta = {"cpf": cpf,"ägência" : "0001" , "numero da conta" : numero_da_conta}
    
    lista_contas.append(conta)

def retornar_lista_de_contas():
    for conta in Lista_de_contas:
        print(conta)
 
def registarOperacao(**args):
    global countOperacao
    aux = (args)
    extrato.append(aux)
    countOperacao = countOperacao + 1
    
def depositar(valor):
    global saldo
    saldo = saldo + valor
    registarOperacao(id = countOperacao, tipo_de_operacao = "deposito", valor = valor, data = data)
    
def sacar(*,valor):
    global saldo, countSaques
    saldo = saldo - valor
    countSaques = countSaques + 1
    
    registarOperacao(id = countOperacao, tipo_de_operacao = "saque", valor = valor, data = data)

def estadoDaConta():
    meta_dados = {"Saldo": saldo, "Operações Realizadas": countOperacao, "Saques disponíveis": LIMITE_SAQUES - countSaques}
    mensagem = "\t||\t".join([f"{chave.title()} = {valor}" for chave, valor in meta_dados.items()]  )
    return mensagem

def retornarExtrato():
    
    for linha in extrato:
        print(linha) 
    
    print(estadoDaConta())