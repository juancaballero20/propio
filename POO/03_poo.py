class circle:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * (self.radio ** 2)
    
    def perimetro(self):
        return 2 * pi * self.radio
    
pi = 3.1416
radio = int(input("Ingrese la medida del radio del circulo: "))

circulo = circle(radio)
area = circulo.area()
perimetro = circulo.perimetro()

print(f"El area del circuo es {area}")
print(f"El perimetro del circulo es de {perimetro}")
