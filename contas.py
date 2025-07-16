from clientes import buscar_cliente, clientes

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []

contas = []

def criar_conta():
    print("\n--- Nova Conta ---")
    cpf = input("CPF do cliente: ").strip()
    cliente = buscar_cliente(cpf)
    if not cliente:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return
    numero = input("Número da conta: ").strip()
    for conta in contas:
        if conta.numero == numero:
            print("Número de conta já existente.")
            return
    conta = Conta(numero, cliente)
    contas.append(conta)
    print(f"Conta {numero} criada para cliente {cliente.nome}.")

def listar_contas():
    print("\n--- Contas Cadastradas ---")
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"Número: {conta.numero} | Cliente: {conta.cliente.nome} | Saldo: R$ {conta.saldo:.2f}")

def buscar_conta(numero):
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None
