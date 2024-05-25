# Constantes
LIMITE_SAQUES = 3
LIMITE = 500

# Variáveis globais
saldo = 0
extrato = ""
numero_saques = 0

# Menu
menu = """
Escolha uma das opções:
[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR

Opção: """

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou: o valor depositado é inválido.")

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor > saldo:
        print("Operação falhou: Você não tem saldo suficiente.")
    elif valor > LIMITE:
        print("Operação falhou: O valor de saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou: Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou: O valor informado é inválido.")

def mostrar_extrato():
    print("\nEXTRATO")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("")

def main():
    global saldo, extrato, numero_saques
    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                depositar(valor)
            except ValueError:
                print("Operação falhou: O valor informado é inválido.")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor de saque: "))
                sacar(valor)
            except ValueError:
                print("Operação falhou: O valor informado é inválido.")

        elif opcao == "e":
            mostrar_extrato()

        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma das opções do menu.")

if __name__ == "__main__":
    main()