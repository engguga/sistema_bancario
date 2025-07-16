class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []

clientes = []
contas = []

def criar_cliente():
    print("\n--- Novo Cliente ---")
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    # Verificar se já existe cliente com CPF
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

def depositar():
    print("\n--- Depósito ---")
    numero = input("Número da conta: ").strip()
    conta = buscar_conta(numero)
    if not conta:
        print("Conta não encontrada.")
        return
    try:
        valor = float(input("Valor a depositar: "))
        if valor <= 0:
            print("Valor deve ser positivo.")
            return
    except ValueError:
        print("Valor inválido.")
        return
    conta.saldo += valor
    conta.extrato.append(f"Depósito: +R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def sacar():
    print("\n--- Saque ---")
    numero = input("Número da conta: ").strip()
    conta = buscar_conta(numero)
    if not conta:
        print("Conta não encontrada.")
        return
    try:
        valor = float(input("Valor a sacar: "))
        if valor <= 0:
            print("Valor deve ser positivo.")
            return
    except ValueError:
        print("Valor inválido.")
        return
    if conta.saldo < valor:
        print("Saldo insuficiente.")
        return
    conta.saldo -= valor
    conta.extrato.append(f"Saque: -R$ {valor:.2f}")
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def extrato():
    print("\n--- Extrato ---")
    numero = input("Número da conta: ").strip()
    conta = buscar_conta(numero)
    if not conta:
        print("Conta não encontrada.")
        return
    print(f"Extrato da conta {conta.numero} - Cliente: {conta.cliente.nome}")
    if not conta.extrato:
        print("Nenhuma movimentação.")
    else:
        for registro in conta.extrato:
            print(registro)
    print(f"Saldo atual: R$ {conta.saldo:.2f}")

def menu():
    print("\n===== SISTEMA BANCÁRIO =====")
    print("[1] Novo Cliente")
    print("[2] Nova Conta")
    print("[3] Depositar")
    print("[4] Sacar")
    print("[5] Extrato")
    print("[0] Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            criar_cliente()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            extrato()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
