menu = """
Opciones de operaciones:
1. Area circulo
2. Area triangulo
3. Area rectangulo
"""
print(menu)

operacion = int(input("Ingrese el número de la opción deseada: "))

if operacion == 1:
    def area_circulo(radio):
        pi = 3.1416
        return pi * (radio ** 2)
    
    radio = float(input("Ingrese el radio del circulo: "))
    area = area_circulo(radio)
    print(f"El área del circulo es: {area}")

elif operacion == 2:
    def area_triangulo(base, altura):
        return (base * altura) / 2
    
    base = float(input("Ingrese la medida de la base del triangulo: "))
    altura = float(input("Ingrese la medida de la altura del triangulo: "))
    area = area_triangulo(base, altura)
    print(f"El área del triangulo es: {area}")
    
elif operacion == 3:
    def area_rectangulo(base, altura):
        return base * altura
    
    base = float(input("Ingrese la medida de la base del rectangulo: "))
    altura = float(input("Ingrese la medida de la altura del rectangulo: "))
    area = area_rectangulo(base, altura)
    print(f"El área del rectangulo es: {area}")

else:
    print("Ingresar una opción válida")
