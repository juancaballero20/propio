class rectangle:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def area(self):
        return self.longitud * self.anchura
    
longitud = int(input("Ingrese la medida de la longitud del rectangulo:"))
anchura = int(input("Ingrese la media de la anchura del rectangulo: "))

rectangulo = rectangle(longitud, anchura)
area = rectangulo.area()

print(f"El area del rectangulo es de {area}") 
