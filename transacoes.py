def depositar(conta, valor):
    if valor <= 0:
        print("Valor inválido para depósito.")
        return False
    conta['saldo'] += valor
    conta['extrato'].append(f"Depósito: +{valor:.2f}")
    return True

def sacar(conta, valor):
    if valor <= 0:
        print("Valor inválido para saque.")
        return False
    if conta['saldo'] < valor:
        print("Saldo insuficiente.")
        return False
    conta['saldo'] -= valor
    conta['extrato'].append(f"Saque: -{valor:.2f}")
    return True

def imprimir_extrato(conta):
    print(f"Extrato da conta {conta['numero']}:")
    for evento in conta['extrato']:
        print(evento)
    print(f"Saldo atual: {conta['saldo']:.2f}")
