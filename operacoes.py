from contas import buscar_conta

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
