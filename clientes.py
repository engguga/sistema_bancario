class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

clientes = []

def criar_cliente():
    print("\n--- Novo Cliente ---")
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    for c in clientes:
        if c.cpf == cpf:
            print("Cliente já cadastrado com este CPF.")
            return
    cliente = Cliente(nome, cpf)
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso.")

def listar_clientes():
    print("\n--- Clientes Cadastrados ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for c in clientes:
        print(f"Nome: {c.nome} | CPF: {c.cpf}")

def buscar_cliente(cpf):
    for c in clientes:
        if c.cpf == cpf:
            return c
    return None
