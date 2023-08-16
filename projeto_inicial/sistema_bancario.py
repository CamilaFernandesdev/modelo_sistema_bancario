class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_diarios < 3 and valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif self.saques_diarios >= 3:
            print("Limite diário de saques atingido.")
        elif valor > 500:
            print("Limite máximo de saque é R$ 500.")
        else:
            print("Saldo insuficiente para saque.")

    def extrato(self):
        print("Extrato:")
        print("Depósitos:")
        for deposito in self.depositos:
            print(f"R$ {deposito:.2f}")
        print("Saques:")
        for saque in self.saques:
            print(f"R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


def main():
    sistema = SistemaBancario()

    while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            valor = float(input("Digite o valor a depositar: "))
            sistema.depositar(valor)
        elif escolha == 2:
            valor = float(input("Digite o valor a sacar: "))
            sistema.sacar(valor)
        elif escolha == 3:
            sistema.extrato()
        elif escolha == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
