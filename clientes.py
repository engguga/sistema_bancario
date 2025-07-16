clientes = []
contas = []
numero_conta = 1001

def criar_cliente(nome, cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("Cliente já cadastrado.")
            return None
    novo_cliente = {
        'nome': nome,
        'cpf': cpf,
    }
    clientes.append(novo_cliente)
    return novo_cliente

def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None

def criar_conta(cliente):
    global numero_conta
    conta = {
        'numero': numero_conta,
        'cliente': cliente,
        'saldo': 0.0,
        'extrato': []
    }
    contas.append(conta)
    numero_conta += 1
    return conta

def listar_clientes():
    return clientes
