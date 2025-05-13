class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f"o {self.nome} foi comer...")
class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"{self.nome} está miando...")
class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"{self.nome} esta latindo...")
class Vaca (Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def mugir(self):
        print(f"{self.nome} esta mugindo...")
class Coelho(Animal):
    def init(self,nome,cor):
        super().__init__(nome,cor)
    def chiar(self):
        print(f"{self.nome} esta guinchando...")



