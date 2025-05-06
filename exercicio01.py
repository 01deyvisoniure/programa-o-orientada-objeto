class Pessoa():
    def __init__(self, nome, idade, peso,falando,comendo,dormindo):
        self.nome=nome
        self.idade=idade
        self.peso=False
        self.comendo=False
        self.dormindo=False
    def falar(self):
            print(f"{self.nome} começou a falar.")
    def comer(self,comida):
        if falando==True:
            print("falar enquanto fala é feio")
        else:
            print(f"{self.nome} começou a comer {comida}.")

    def dormir(self):
        print("Zzzz..")
        dormindo
aluno01=Pessoa("iure",19,73)
aluno01.falar()
aluno01.dormir()
aluno01.comer("pipoca")