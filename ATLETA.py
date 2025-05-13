class Atleta():
    def __init__(self,peso):
        self.peso=peso
        self.aposentado=False
        self.aquecido=False
    def aposentar(self):
        if self.aposentado==True:
            print(" atleta ja esta aposentado.")
        else:
            self.aposentado=True
            print("atleta aposentado com sucesso.")
    def aquecer(self):
        if self.aposentado==False:
            self.aquecido=True
            print("atleta aquecido.")
        else:
            print("atleta está aposentado.")
class Corredor(Atleta):
    def __init__(self):
        super().__init__(self.peso)
    def correr(self):
        if self.aquecido==True:
            print("atleta começou a correr.")
        else:
            print("atleta não está aquecido.")
class Nadador(Atleta):
    def __init__(self):
        super().__init__(self.peso)
    def nadar(self):
        if self.aquecido==True:
            print("atleta começou a nadar.")
        else:
            print("atleta não está aquecido.")
class Ciclista(Atleta):
    def __init__(self):
        super().__init__(self.peso)
    def nadar(self):
        if self.aquecido==True:
            print("atleta começou a pedalar.")
        else:
            print("atleta não está aquecido.")
class Triatleta(Nadador,Ciclista,Corredor):
    def __init__(self):
        super().__init__(self.peso)


