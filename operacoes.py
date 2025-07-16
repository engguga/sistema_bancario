LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor <= 0:
        print("Valor inválido.")
        return
    conta["saldo"] += valor
    conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
    print("Depósito realizado com sucesso.")

def sacar(conta):
    if conta["saques_realizados"] >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
        return

    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("Valor inválido.")
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
        return
    if valor > LIMITE_VALOR_SAQUE:
        print("O valor excede o limite por saque.")
        return

    conta["saldo"] -= valor
    conta["extrato"].append(f"Saque: R$ {valor:.2f}")
    conta["saques_realizados"] += 1
    print("Saque realizado com sucesso.")

def exibir_extrato(conta):
    print("\n=== Extrato ===")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in conta["extrato"]:
            print(movimento)
    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
