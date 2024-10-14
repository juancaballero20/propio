class pow:
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcular(self):
        return self.base ** self.exponente
    
base = int(input("Ingrese el número base: "))
exponente = int(input("Ingrese el número al que se va a elevar: "))
calculo = pow(base, exponente)

print(f"El resultado de {base} elevado a la {exponente} es: {calculo.calcular()}")

