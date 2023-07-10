lista_usuarios = []
lista_cpfs = []

def formulario_usuario(usuario,cpfs):
    cpf = input("digite numero do cpf (soente numeros): ")
    nome = input("digite o nome: ")
    data_nasc= input("digite a data de nascimentoe: ")   
    logadrouro = input("digite o logradouro: ")
    bairro = input("digite o nome do bairro: ")
    cidade = input("digite a sigla da cidade: ")
    estado = input("digite o nome do estado: ")

    endereco = f"{logadrouro} {bairro} {cidade} {estado} "
    
    pessoa = {"nome": nome, "data_nasc": data_nasc, "CPF" : cpf, "endereço" : endereco}
    
    usuario.append(pessoa)
    cpfs.append(cpf)
    
    print(">>> sucesso: usuário cadastrado")
    
    
    return pessoa
    
def filtrar_cpf(cpf):
    global lista_cpfs
    
    if cpf not in lista_cpfs:
        return False
    else:
        return True
    
def retornar_lista_de_usuarios():
    for usuario in lista_usuarios:
        print(usuario)
 