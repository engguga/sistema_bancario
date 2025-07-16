def criar_conta(agencia, numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ").strip()
    cliente = next((c for c in clientes if c["cpf"] == cpf), None)

    if not cliente:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return

    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "cliente": cliente,
        "saldo": 0,
        "extrato": [],
        "saques_realizados": 0
    }
    contas.append(conta)
    print("Conta criada com sucesso.")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n=== Contas Cadastradas ===")
    for conta in contas:
        cliente = conta["cliente"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Titular: {cliente['nome']}")

def buscar_conta(cpf, contas):
    return next((conta for conta in contas if conta["cliente"]["cpf"] == cpf), None)
