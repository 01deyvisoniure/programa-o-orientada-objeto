class Pessoa():
    def __init__(self, nome, idade, peso,falando,comendo,dormindo):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.falando=False
        self.comendo=False
        self.dormindo=False
    def falar(self):
        if self.falando==True:
            print("ele já está falando.")
        else:
            if self.comendo==True:
                print("esta de boca cheia, não pode falar enquanto come.")
            else:
                if self.dormindo==True:
                    print("não pode falar pq ja esta roncando.")
                else:
                    if self.falando==False:
                        print(f"{self.nome} começou a falar")
                        self.falando=True
    def calar(self):
        if self.falando==True:
            self.falando=False
            print(f"{self.nome} parou de falar")
        else:
            print(f"{self.nome} não está  falando.")
    def comer(self,comida):
        if self.comendo==True:
            print("ele já esta comendo.")
        else:
            if self.dormindo==True:
                print("não pode comer enquanto dorme.")
            else:
                if self.falando==True:
                    print("não pode falar enquanto come.")
                else:
                    if self.comendo==False:
                        print(f"{self.nome} começou a comer {comida}.")
    def dormir(self):
        if self.dormir==True:
            print("não da pra dormir  duas vezes.")
        else:
            if self.comendo==True:
                print("nao pode dormir enquanto come.")
            else:
                if self.falando==True:
                    print("não pode dormir enquanto fala.")
                else:
                    if self.dormir==False:
                        print(f"{self.nome} começou a dormir")
                        self.dormir=True
    def acordar(self):
        if self.dormindo==True:
            self.dormindo=False
            print(f"{self.nome} acordou")
        else:
            print("ele não está dormindo.")
    def parar_comer(self):
        if self.comendo==True:
            self.comendo=False
            print(f"{self.nome} parou de comer.")
        else:
            print(f"{self.nome} ja esta comendo.")








aluno01=Pessoa("iure",19,73,False,False,False)
aluno01.falar()
aluno01.dormir()
aluno01.comer("pipoca")