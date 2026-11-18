class contabancaria:
    def __init__(self,titular,numero_da_conta,saldo):
        self.titular = titular
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
    def consultar_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: {self.saldo:.2f}kz")

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor:.2f}kz realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def levantar(self,valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Levantamento de {valor:.2f}kz realizado com sucesso.")
        else:
            print("Valor de levantamento inválido ou saldo insuficiente.")

#criar um objeto da classe contabancaria
conta1 = contabancaria("João", 12345, 1000.00)
conta2=contabancaria("Eurico", 67890, 500.00)
#depositar
conta1.depositar(100.00)
conta2.depositar(5000.00)
#levantar
conta1.levantar(200.00)
conta2.levantar(600.00)

#saldo atual
print(f"Saldo atual da conta de {conta1.titular}: {conta1.saldo:.2f}kz")
print(f"Saldo atual da conta de {conta2.titular}: {conta2.saldo:.2f}kz")