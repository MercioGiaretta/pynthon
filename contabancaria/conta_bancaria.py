class ContaBancaria:
    def __init__(self,numero,titular,saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo =+ valor
    
    def exibir_detalhes(self):
        print("Número da Conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)

    def sacar(self,valor):
        if self.saldo >=  valor:
            self.saldo -= valor
        else:
            print("Lhe falta kwanzas")

numero_acc = input("Digite o número da sua conta: ")
titular_acc = input("Digite o número do titular: ")
saldo_acc = float(input("Digite o Saldo Atual: ").replace(",","."))

conta_do_mercio = ContaBancaria(numero_acc, titular_acc, saldo_acc)
deposito = float(input("Digite o valor a ser depositado ").replace(",","."))
saque = float(input("Digite o valor a ser sacado ").replace(",","."))

conta_do_mercio.depositar(4100)
conta_do_mercio.sacar(200)
conta_do_mercio.exibir_detalhes()