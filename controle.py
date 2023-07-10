import textwrap
import conta
import usuario


cadastro = []

def cadastrar_usuario(test = None):
    if test == None:
        aux = int(input("digite o seu cpf para verificar se já possui cadastro: "))
        test = aux
    
    if usuario.filtrar_cpf(test):
        print("@@@ Erro! Usuário já cadastrado")
    else:
        print(">>> Bem-vindo! Primeira vez aqui né? \n Digite as informações para cadastro")
        cadastro.append(usuario.formulario_usuario(usuario.lista_usuarios, usuario.lista_cpfs))
        a = str(input(f"deseja associar o CPF : {test} uma nova conta? [s, n]" ))
        if a == "s":
            associar_conta(test)

def associar_conta(cpf = None):
    
    if cpf == None:
        aux = int(input(">>> Agora vamos associar um CPF à sua conta sua conta\n Para criar sua conta digite digite o mesmo CPF que usou no cadastro: "))
    
        if usuario.filtrar_cpf(aux):
            conta.criar_conta(aux,conta.Lista_de_contas)
            print(f">>> Conta associada ao CPF{aux}")
        else:
            sel = str(input("@@@ erro: CPF não cadastrado (só possível associar uam conta a um CPF já cadastrado) \n\nDeseja realizar o cadastro agora? [s, n]"))
            if sel == "s":
                cadastrar_usuario(aux)
    elif cpf != None:
        conta.criar_conta(cpf,conta.Lista_de_contas)
                   
def chamar_lista_contas():
    conta.retornar_lista_de_contas()
     
def chamar_lista_usuarios():
    usuario.retornar_lista_de_usuarios()
    
def chamarSaque(a):
    print("Chegou")
    if conta.countSaques == conta.LIMITE_SAQUES:
        print(f"Não é possível realizar saque pois a conta da excedei o limite diário de saques: {conta.LIMITE_SAQUES}")
        return False
    elif conta.saldo == 0:
        print(f"@@@ Não é possível realizar saque! \n saldo atual: {conta.saldo}")
    elif a > conta.saldo:
        print(f"@@@ não é possível realizar saque! \n você pode sacar um valor até: {conta.saldo}")
    elif a > 500:
         print("Você só pode realizar saques de até R$ 500 \n vamos tentar de novo?")
    else:                                
        conta.sacar(valor = a)
                
def controleDeSaldo(a):
    valor = a
    
    conta.depositar(valor)
"""    if conta.saldo < 0:
        print("Conta com saldo negativo!")
        conta.depositar(valor)
        print(f"Saldo atual: {conta.saldo}")
"""

def chamarExtrato():
    if conta.countOperacao == 0:
        mensagem = "sem informçãoes"
        return mensagem, False
    else:
        aux = conta.retornarExtrato()
    return aux

def chamarInfoConta():
    aux = conta.estadoDaConta()
    return aux

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    [c]\tInformações da conta
    
    => """
    return input(textwrap.dedent(menu))

