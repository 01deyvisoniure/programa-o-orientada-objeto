class Conta:
    def __init__(self, numero_conta,nome_cliente,tipo_conta):
        self.limite=0
        self.numero_conta=numero_conta
        self.saldo=0
        self.status_conta=True
        self.nome_cliente=nome_cliente
        self.tipo_conta=tipo_conta
    def sacar(self,saque):
        if self.status_conta==False:
            print(f"conta está desativada")
        else:
            if saque>self.saldo:
                print("saldo insuficiente.")
            else:
                self.saldo-=saque
                print(f"{self.nome_cliente} sacou: R${saque}")
    def depositar(self,deposito):
        if self.status_conta==False:
            print(f"conta está desativada")
        else:
            self.saldo+=deposito
            print(f"deposito de : R${deposito}\nsaldo atual de: R${self.saldo}")
    def ver_saldo(self):
        if self.status_conta==False:
            print("conta desativada.")
        else:
            print(f"seu saldo é de: {self.saldo}")
    def desativar(self):
        if self.saldo==0 and self.status_conta==True:
            self.status_conta=False
            print("sua conta foi desativada com sucesso.")
        else:
            if self.saldo>0:
                print("não foi possivel desativar sua conta, você ainda tem dinheiro em conta.")
            else:
                if self.saldo<0:
                    print("não foi possivel desativar sua conta, seu saldo está negativo.")
                else:
                    print("sua conta já está desativada.")
    def ativar(self):
        if self.status_conta == False:
            self.status_conta = True
            print("sua conta foi ativada.")
        else:
                print("sua conta ja esta ativada")
    def info(self):
        if self.status_conta==True:
            print(f"nome usuario: {self.nome_cliente}")
            print(f"numero da conta: {self.numero_conta}")
            print(f"tipo da conta: {self.tipo_conta}")
            print(f"saldo: R${self.saldo}")
            print(f"status da conta: ativa")
        else:
            print(f"nome usuario: {self.nome_cliente}")
            print(f"numero da conta: {self.numero_conta}")
            print(f"tipo da conta: {self.tipo_conta}")
            print(f"saldo: R${self.saldo}")
            print(f"status da conta: desativada")
usuario01=Conta(11,"iure","poupança")
escolha=0
while escolha!=7:

