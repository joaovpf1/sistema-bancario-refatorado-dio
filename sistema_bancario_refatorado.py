menu = """
    Escolha uma opção:
    [1] Sacar
    [2] Depositar
    [3] Visualizar Extrato
    [4] Criar cliente
    [5] Criar conta
    [6] Sair

    => """


def criar_cliente(clientes):
    cpf = input("Digite o seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n Já existe cliente com esse CPF!")
        return

    nome = input("Digite o seu nome: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereço = input(
        "Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    clientes.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereço": endereço,
        }
    )
    print("\nCliente criado com sucesso!")


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_conta(agencia, num_conta, clientes):
    cpf = input("Digite o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "num_conta": num_conta, "cliente": cliente}
    else:
        print("\n Não foi possível encontrar um cliente com este CPF.")


def saque(*, saldo, quantidade_saque, extrato):
    if quantidade_saque <= 3:
        valor_saque = float(input("Digite o valor que deseja sacar: R$ "))
        if valor_saque <= 500:
            print(saldo)
            if valor_saque <= saldo:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                quantidade_saque += 1
                print(
                    "Saque efetuado com sucesso, retire seu dinheiro na boca do caixa."
                )
                print(f"O valor atual da sua conta é de R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print(
                "Valor máximo que é permitido execido, autorizado: R$500,00 por saque."
            )
    else:
        print("Quantidade de saques diários execidos, tente novamente amanhã.")
    return saldo, extrato


def deposito(saldo, extrato):
    valor_deposito = float(input("Digite o valor que deseja depositar: R$ "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Depósito realizado com sucesso. Agora você tem R$ {saldo:.2f}")
    return saldo, extrato


def extrato_final(saldo, /, *, extrato):
    print("\n========== Extrato ==============")
    print("Não foram realizadas movimentações bancárias." if not extrato else extrato)
    print("==================================")
    print(f"\nSeu saldo atual é de R$ {saldo:.2f}")
    print("==================================")


def main():
    saldo = 0
    quantidade_saque = 0
    extrato = " "
    clientes = []
    contas = []
    agencia = "0001"
    num_conta = 0

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            saldo, extrato = saque(
                saldo=saldo, quantidade_saque=quantidade_saque, extrato=extrato
            )
        elif opcao == 2:
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == 3:
            extrato_final(saldo, extrato=extrato)
        elif opcao == 4:
            criar_cliente(clientes)
        elif opcao == 5:
            num_conta = len(contas) + 1
            conta = criar_conta(agencia, num_conta, clientes)
            if conta:
                contas.append(conta)
        elif opcao == 6:
            break
        else:
            print("Opção inválida, tente novamente.")


main()
