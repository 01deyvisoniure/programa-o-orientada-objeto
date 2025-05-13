class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0
class Triangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.altura=altura
        self.base=base
    def calcularea(self):
        self.area = (self.base*self.altura) /2
        print(self.area)
    def calcularperi(self):
        self.area = (self.base * self.altura) / 2
        self.perimetro= self.area+self.base+self.altura
        print(self.perimetro)
class Retangulo(Forma):
    def __init__(self,altura,base):
        super().__init__()
        self.altura=altura
        self.base=base
    def calculararea(self):
        self.area= self.base*self.altura
    def calcularperi(self):
        self.perimetro=2*(self.base+self.altura)