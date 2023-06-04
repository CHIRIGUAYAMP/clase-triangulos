from figura_geometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, base:float=0.0, altura:float=0.0):
        super().__init__(ancho=base, alto=altura)

    def __str__(self):
        return f'Triangulo [base = {self.ancho}, altura ={self.alto},]'

    def calcular_area(self):
        return (self.alto * self.ancho)/2

    def calcular_perimetro(self):
        return 3 * self.ancho

if __name__ == '__main__':
    c1 = Triangulo(base=8, altura=10)
    print(c1)
    print(f'El área del Triangulo es: {c1.calcular_area()}')
    print(f'El perimetro del Triangulo es: {c1.calcular_perimetro()}')
