def contar_mayus_minus(cadena):
    mayusculas = 0
    minusculas = 0
    for char in cadena:
        if char.isupper():
            mayusculas += 1
        elif char.islower():
            minusculas += 1
    return {"mayusculas": mayusculas, "minusculas": minusculas}


resultado = contar_mayus_minus("Hola Programación")
print(f"Mayúsculas: {resultado['mayusculas']}, Minúsculas: {resultado['minusculas']}")

