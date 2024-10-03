a = float(input("Ingrese la primera nota: "))
b = float(input("Ingrese la segunda nota: "))
c = float(input("Ingrese la tercera nota: "))
d = float(input("Ingrese la cuarta nota: "))
e = float(input("Ingrese la quinta nota: "))

promedio = (a + b + c + d + e) / 5
if  promedio >= 3.0:
    print(f"El estudiante aprobó con una nota  de {promedio}")


else:
    print(f"El estudiante reprobó con una nota  de {promedio}")

