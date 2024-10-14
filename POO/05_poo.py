class Ave:
    def __init__(self, nombre, color, tamaño, puede_volar):
        self.nombre = nombre
        self.color = color
        self.tamaño = tamaño
        self.puede_volar = puede_volar

    def describir(self):
        vuelo = "sí" if self.puede_volar else "no"
        return f"Soy un(a) {self.nombre}, de color {self.color}, tamaño {self.tamaño} y {vuelo} puedo volar."

class Paloma(Ave):
    def __init__(self):
        super().__init__(nombre="Paloma", color="Blanco", tamaño="Pequeño", puede_volar=True)

class Aguila(Ave):
    def __init__(self):
        super().__init__(nombre="Águila", color="Marrón", tamaño="Grande", puede_volar=True)

    def cazar(self):
        return f"El {self.nombre} está cazando desde el aire."

class Pinguino(Ave):
    def __init__(self):
        super().__init__(nombre="Pingüino", color="Negro y Blanco", tamaño="Mediano", puede_volar=False)

    def nadar(self):
        return f"El {self.nombre} está nadando en el agua fría."

paloma = Paloma()
aguila = Aguila()
pinguino = Pinguino()

print(paloma.describir())  
print(aguila.describir())  
print(aguila.cazar())      
print(pinguino.describir())  
print(pinguino.nadar())     
